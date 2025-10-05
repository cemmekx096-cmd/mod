label june16start:
    stop music
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionvictoria01 with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june16day"
    play ambient "sound effects/cricket.wav"
    scene w3_3581 with blinds
    show screen qmenu with dissolve

    if minaCheat == True and minaBreakOff == False:
        $ w3MinaHotelFucked = True
    if minaCleanStart == True:
        $ w3MinaHotelFucked = True
    if w3MinaHotelFucked == True and hanaGF == True:
        $ hanaTwoTime = True
        $ hanaCheat +=1

    "...................................."
    "................................."
    ".............................."
    "..........................."
    scene w3_3582 with dissolve
    "........................"
    "....................."
    scene w3_3583 with dissolve
    "............"
    "........."
    scene w3_3584 with dissolve
    "......"
    "..."
    stop ambient fadeout 3.0
    play music "music/no7-alone-with-my-thoughts.ogg"
    scene w3_3585 with dissolve
    show screen textbox2 with dissolve
    mct "(That's new...)"
    show june16day with squares
    "The early morning hours stretched thin, but I couldn't sleep."
    "Instead of staring at the inside of my eyelids, I counted sheep while looking up at my childhood room's painted ceiling."
    scene w3_3586 with dissolve
    mct "(...why am I here?)"
    "I had been in that apartment for weeks."
    mct "(Even if there were listening devices, another night wouldn't have mattered...)"
    scene w3_3585 with dissolve
    "But, the whole exchange with Dr. Van Doren was simply too odd and too clearly pointed for how mysterious it was."
    mc "Goddamn it..."
    "Quite frankly, it was unsettling."
    scene w3_3584 with dissolve
    mct "(The last time I asked Ian about Darius I got nothing, but...)"
    "......"
    scene w3_3585 with dissolve
    "..."
    scene w3_3587 with dissolve
    mct "(...it's worth a shot.)"
    play sound "sound effects/phonemenu.wav"
    scene w3_3588 with dissolve
    "{i}It's at least an attempt at quieting my mind.{/i}"
    play ambient "sound effects/ringing-outbound.mp3"
    scene w3_3589 with dissolve
    "Paying no mind to the hour, I gave my friend a call."
    "The phone rung, rung, and rung."
    "And just when I thought I would get a voicemail box--"
    stop ambient
    scene w3_3590 with dissolve
    kil "Heeeeeey, [mcf]!"
    "Ian answered the phone in an all-tellingly boisterous way."
    scene w3_3591 with dissolve
    mc "Sheesh, volume control, man."
    scene w3_3590 with dissolve
    "He was drunk."
    scene w3_3592 with cmet
    kil "Ah! What's up, dude?!"
    scene w3_3593 with dissolve
    "I was growing less confident in the prospect of a productive conversation, but at the very least, Ian's voice was a nice reprieve from my scattered thoughts."
    mc "Two nights in a row? Do I need to stage an intervention?"
    scene w3_3594 with dissolve
    kil "Ha! Hell no!"
    kil "Don't you know being drunk on a Tuesday is one of the perks of mooching off your family's fortune?"
    scene w3_3593 with dissolve
    mc "At least you seem to be in a good mood."
    scene w3_3592 with dissolve
    kil "What about you? You doing okay?"
    scene w3_3593 with dissolve
    mc "Besides the obvious hour, what gave me away?"
    scene w3_3595 with dissolve
    kil "I can tell by your tone that you're not feeling right, dude."
    scene w3_3596 with dissolve
    mc "Come on... other than tired, I don't sound {i}particular{/i}, do I?"
    scene w3_3595 with dissolve
    kil "Ha! You sound {i}friendly{/i}, but only in the way you get when you're stressed, pissed off, or looking for someone to commensurate with."
    scene w3_3597 with dissolve
    mc "I think you mean {i}commiserate{/i}."
    scene w3_3598 with dissolve
    kil "Eh? What the fuck did I say?"
    scene w3_3596 with dissolve
    mc "Ahhh... but you're not wrong right now, so I'll just take my lumps like a good self-serving asshole."
    scene w3_3595 with dissolve
    kil "Fuck it, man. I don't see it that way. There's nothing wrong with only calling when something's on your mind. We're not chicks!"
    kil "So, tell me what's crawled up your ass. I want to hear it."
    "He sounded like he genuinely meant that."
    scene w3_3599 with dissolve
    mc "...I had a patron drop by the apartment yesterday evening. Abel Van Doren."
    scene w3_3600 with dissolve
    kil "August already has you pulling dinosaur duty, huh? That's a drag."
    kil "Sometimes talking to those old fucks is like squeezing out that last turd that refuses to drop."
    scene w3_3599 with dissolve
    mc "Colorful..."
    scene w3_3600 with dissolve
    kil "It's like, stop dragging out the goddamn point, you know?"
    scene w3_3599 with dissolve
    mc "I wasn't playing entertainer. He and Sophia came by unannounced, wanting to- ah... actually, to be honest, {b}I'm not sure what it was about.{/b}"
    scene w3_3602 with dissolve
    kil "Damn, dude. You sound actually..."
    scene w3_3601 with dissolve
    mc "{b}Yeah{/b}. I'm perturbed, because when I said they dropped by unannounced, I mean he {b}broke{/} the fuck into my home."
    scene w3_3602 with dissolve
    kil "...you must mean he invited himself in like he owned the place?"
    scene w3_3601 with dissolve
    mc "No, I mean he full-on broke in."
    mc "His aide gave me an hour's notice by phone to be there, he had some goons sweep my {i}very much{/i} locked place, and then sat comfortably waiting for me until I arrived home."
    scene w3_3603 with dissolve
    kil "What the shit, dude?! Like... {i}why?{/i} Like why, in the absolute fuck, would he do that?"
    scene w3_3604 with dissolve
    mc "That's why I can't sleep right now; I can't figure it out. He said he was there to offer me advice, but it was like he purposefully avoided saying anything valuable."
    scene w3_3605 with dissolve
    kil "Bah, that's just how those assholes talk in my experience. I'd bet good money that when you're surrounded by people that kiss your ass and anticipate your every need, you don't spell anything out."
    kil "It's when they have to explain something to you bluntly that things are serious."
    scene w3_3604 with dissolve
    mc "...is that how it is?"
    scene w3_3605 with dissolve
    kil "Give me some credit. In matters like this, I'm your senior."
    scene w3_3604 with dissolve
    mc "...maybe, but I don't think it was {i}nothing{/i}."
    scene w3_3605 with dissolve
    kil "I want you to tell me everything you two talked about, but let me make some privacy first."
    scene w3_3606 with dissolve
    mc "Wait! You're not alone?! You should've told me! We're talking about club shit!"
    scene w3_3607 with wipeleft
    kil "Relax, man. It's {i}just{/i} Alice, and it's not like you can make anything out so far from my end of this conversation."
    kil "I'll send her into the other room, then we can talk more about what's making you anxious and hopefully set you on the path to feeling better!"
    scene w3_3608 with dissolve
    mc "I think I should probably just let you-"
    scene w3_3609 with dissolve
    kil "No, seriously, dude. Let's talk; I know how you are. You'll just lie awake imagining the worst."
    kil "Let me be a friend right now."
    scene w3_3610 with dissolve
    kil "Ah, shit. Hold on a second..."
    scene w3_3611 with dissolve
    kil "{size=-10}I said keep your eyes on the fucking floor!{/size}"
    mct "(Uh...)"
    scene w3_3612 with dissolve
    alice "You said my name, so I ju--"
    kil "Eyes down, shit-for-brains!"
    scene w3_3613 with dissolve
    mc "Uh... I'm going to hang up now..."
    hide screen textbox2 with dissolve
    scene w3_3617 with dissolve
    kil "Don't be hasty. It's not what it sounds like! We're just playing a game."
    kil "She's not very good at it, but I haven't figured out if that's on purpose or not."
    scene w3_3615 with dissolve
    mc "That doesn't clear it up in the way you think it does..."
    scene w3_3616 with dissolve
    kil "Hmmm... don't you remember when I'd get in trouble and she'd make me stand in the corner to think about what I'd done? It's like that!"
    scene w3_3615 with dissolve
    "........."
    "......"
    mc "...and she's {i}actually{/i} into this?"
    scene w3_3614 with dissolve
    kil "Yeah! The bitch is into being treated like this. Allow me to prove it..."
    scene w3_3618 with dissolve
    kil "Tell [mcf] the truth. You're a nasty slut, aren't you?"
    scene w3_3619 with dissolve
    alice "......"
    scene w3_3620 with dissolve
    alice "..."
    "I honestly thought about cutting the call right here, but like passing a car wreck, Ian's viciousness had me momentarily ensnared."
    "I wanted to hear what the gracious and kindhearted woman, who I had known for most of my life, would say to his degrading question."
    kil "If you want me to fuck your old ass later, tell the truth."
    scene w3_3621 with dissolve
    alice "...I'm a shameless woman."
    scene w3_3620 with dissolve
    "Well, there I had it, further shattering my increasingly fucked up image of the woman I had long known."
    kil "...{b}and?{/b}"
    scene w3_3622 with dissolve
    alice "I'm a shameless old woman addicted to young cock."
    scene w3_3623 with dissolve
    mct "(Not that I had any right to judge another person's proclivities...)"
    scene w3_3624 with dissolve
    kil "Do you hear that shit? Oh, man. {b}Older women.{/b} The more bored they are, the more twisted they get inside."
    kil "It's fucking beautiful. You wanna see?"
    scene w3_3625 with dissolve
    "......"
    "..."

    menu:
        "Show me(w3AliceSeen=True)"(chg=["killian_up"]):
            $ Killian_Bromance += 1
            $ w3AliceSeen = True
            show screen textbox2 with dissolve
            alice "Maybe you shouldn't bring him into this, Ian. He's clearly uncomfortable with--"
            scene w3_3626 with dissolve
            mc "Yeah... let me see."
            scene w3_3627 with pixellate
            "Alice was one of the earliest positive female influences in my life. In a way, she filled the role that a friend's mother would. She took us to amusement parks, got us ice cream, and refereed our petty childhood disagreements..."
            "The dichotomy of seeing that maternal image naked, horny, and shamed filled me with an ugliness that I didn't have the energy to hide right now."
            scene w3_3628 with pixellate
            mc "Put me on video."
            scene w3_3629 with dissolve
            "If she's into it... {i}why should I pretend to be something I'm not, all when it doesn't cost me anything?{/i}"
            scene w3_3630 with dissolve
            kil "I was already going to do that. Switching now~ feast your eyes on this pathetic slut!"
            alice "Ah, I-Ian--"
            scene w3_3629 with dissolve
            hide screen textbox2 with dissolve
            kil "Stand up so my friend can get a better look at you! And don't try to hide your sagging tits!"
            scene w3_3631 with dissolve:
                subpixel True
                yalign 0.78
                xalign 0.6
                linear 5 yalign 0.2
            "Like the professional he was, my friend's hand was steady, holding the camera out and allowing me to catch the masochistic woman scrambling to her feet faster than a dog at dinner time."
            "Alice's soft curves shook like gelatin from the abrupt change in position, and that pleasant jiggle continued as she struggled with the feeling coming back to her legs."
            scene w3_3632 with dissolve
            mct "(Huh...)"
            scene w3_3633 with dissolve
            alice "I, uhh-♥"
            scene w3_3634 with dissolve
            mc "Can she see me?"
            scene w3_3633 with dissolve
            alice "[mcf], I..."
            scene w3_3634 with dissolve
            kil "Yep! You're basically looking right at each other!"
            mc "......"
            mc "...hello, Alice."
            scene w3_3635 with dissolve
            alice "Ah, h-hey... [mcf]..."
            scene w3_3636 with dissolve
            "The image of sweet Alice in dirty aprons and oversized sweaters was immediately erased from my mind, replaced by the audacious arrangement of pixels being beamed into my eyeballs."
            scene w3_3637 with dissolve
            "What she had on didn't qualify as undergarments. The thin straps of her \"bra\" did nothing to hide her large, puffy areolae from view and gave little support to her tits' losing fight against gravity."
            scene w3_3638 with dissolve
            "The decorative cut of her panties was lost in the dark black sheen of her pubic hair, with a pair of heels accentuating her hips' egregiously breedable curves."
            scene w3_3639 with dissolve
            kil "Eh? Do you think you're on a first-name-basis, you fucking trash bag?"
            scene w3_3640 with dissolve
            alice "Hnnngg...♥ H-hello, s-sir."
            scene w3_3641 with dissolve
            "A look of embarrassed excitement colored her wrinkled face, and in that moment, I believed Ian's claim that Alice was getting off on this."
            scene w3_3642 with dissolve
            kil "So, what do you think? She looks nothing like you remember? Pathetic, right?"
            scene w3_3641 with dissolve
            "Oh, {i}I had words{/i}."

            menu:
                "She's even better than you remember.(Dialogue/Render changes only)":
                    mc "She's... {i}lovely{/i}."
                    "Perhaps the contrarian in me wanted to deny sweet Alice the venomous appraisal she wanted and expected, but I also did mean my words."
                    scene w3_3643 with dissolve
                    mc "You were always so soft-spoken but firm. You were moderate, patient, and thoughtful. But this..."
                    scene w3_3640 with dissolve
                    alice "I, aah..?"
                    scene w3_3644 with dissolve
                    mc "I'm lucky to see this side of you, Alice."
                    scene w3_3645 with dissolve
                    alice "O-ohhh..."
                    scene w3_3646 with dissolve
                    kil "Ha, stop, dude! She looks more embarrassed than I've ever seen her and I've had my balls stuffed down her throat at a family friend's wedding!"
                    scene w3_3647 with dissolve
                    "As much as I thought it would, my image of Alice wasn't so much tarnished as it was renewed."
                    alice "T-thank you, sir. It's nice to see you all grown up as well..."
                    scene w3_3648 with dissolve
                    mc "How's Andrew? Did he finish his doctorate?"
                    "...but my sadism wasn't completely in check, as I brought up a question about her son."
                    scene w3_3647 with dissolve
                    alice "O-oh, u-uh..."
                "Agree with him. This woman is nothing like the one from your memory.":

                    mc "The Alice I remember once instructed us on good posture."
                    scene w3_3639 with dissolve
                    kil "That was when she helped us prep for a class presentation once, right? I was so nervous I let you do all the talking, haha!"
                    scene w3_3641 with dissolve
                    mc "You taught us that a good stance and posture reflect a proper state of mind, Alice."
                    scene w3_3649 with dissolve
                    alice "...you remember my exact words?"
                    scene w3_3650 with dissolve
                    mc "It was an important lesson that I took to heart, which does prompt a question for you, Alice..."
                    scene w3_3649 with dissolve
                    alice "Yes, sir?"
                    scene w3_3651 with dissolve
                    mc "If you're going to act like a dirty whore, standing naked in front of two men you saw grow up, don't you think that you should take care to present yourself with the confidence of a whore?"
                    scene w3_3640 with dissolve
                    alice "I'm sorry if I'm not--"
                    scene w3_3641 with dissolve
                    mc "The Alice I knew was soft-spoken but firm. She was moderate, patient, and thoughtful. But this..."
                    scene w3_3652 with dissolve
                    kil "Bahaha! Fuck! Look at her squirm!"
                    mc "...all I'm looking at is a pig. Not a prize-winning one at that, either."
                    alice "...Ahh, hhaa...♥"
                    scene w3_3653 with dissolve
                    kil "Man, I wish you were here right now! We could correct her posture together!"
                    "As I watched Alice try to hide the delight in her expression, I couldn't help but feel the same; the world is truly filled with all kinds."
                    scene w3_3648 with dissolve
                    mc "How's Andrew? Did he finish his doctorate?"
                    scene w3_3647 with dissolve
                    alice "H-huhuhh...?"
                    "She seemed shocked by the sudden turn in the conversation."


            scene w3_3654 with dissolve
            alice "H-he... he did."
            scene w3_3655 with dissolve
            alice "He's in Indonesia right now, studying the Coconut Palm Beetle."
            scene w3_3656 with dissolve
            mc "You must get lonely."
            scene w3_3655 with dissolve
            alice "Sometimes, especially since David died, but... I keep {i}busy.{/i}"
            scene w3_3656 with dissolve
            mc "That must be tough, but Andrew's got a lot to be proud of, huh. I bet that's double for you."
            scene w3_3657 with dissolve
            alice "It is! I'm {i}exceedingly{/i} proud! How could I not be?"
            alice "Whenever I think about him, I feel so excited for him."
            scene w3_3658 with dissolve
            kil "{size=-5}This is going off script...{/size}"
            mc "I'm glad to hear he's doing okay. He had a lot of good advice for me when I started college."
            mc "I still don't get his love of bugs, though..."
            scene w3_3657 with dissolve
            alice "{i}Same.{/i}"
            scene w3_3658 with dissolve
            mc "......."
            scene w3_3656 with dissolve
            alice "..."
            mc "Alice, would you do me a favor?"
            "This had been a remarkable distraction, but I did want to talk to Ian about Darius."
            scene w3_3655 with dissolve
            alice "...uh, s-sure. Anything, sir."
            scene w3_3656 with dissolve
            "She looked uncertain. Caught between this friendly aside and the master/servant dynamic she was playing into."

            menu:
                "Kindly send her away so you and Ian can talk in private(Dialogue/Render changes only).":
                    mc "Ian and I have something to talk about in private."
                    scene w3_3659 with dissolve
                    "Her gaze wandered off the phone's screen and to Ian, seeking instruction from her master."
                    kil "You heard him: {b}Go{/b}. Wait for me in the bedroom."
                    scene w3_3660 with dissolve
                    alice "Yes, sir!"
                "Not-so-kindly send her away(Dialogue/Render changes only).":

                    mc "{b}Now{/b}, Alice... would you mind getting your fat, disgusting ass out of here? Ian and I have something to talk about in private."
                    scene w3_3661 with dissolve
                    alice "I, aahhh.. uh..."
                    scene w3_3662 with dissolve
                    "Like the good masochistic pig she was, she looked to Ian for his permission."
                    kil "You heard him. Wait for me in the bedroom."
                    scene w3_3663 with dissolve
                    alice "Yes, sirs!"

            scene black with fade
            "Like that, she stumbled off, quickly disappearing from the camera's view while Ian and I gave it a moment before picking up where we left off."
            "......"
            "..."
        "You'll pass.":

            scene w3_3664 with dissolve
            show screen textbox2 with dissolve
            mc "I {i}really{/i} should leave you to it. I'm interrupting your fun."
            scene w3_3624 with dissolve
            kil "No, no, no! Sorry, just let me send her to the bedroom."
            scene w3_3664 with dissolve
            mc "Don't inconvenience Alice for my sa--"
            scene w3_3624 with dissolve
            kil "She gets off on being inconvenienced. It's no biggie!"
            kil "{size=-5}Go wait in the bedroom, please.{/size} I need to speak to [mcf] in private."
            scene w3_3665 with dissolve
            alice "Yes, sir!"
            scene w3_3624 with dissolve
            "......"
            "..."
            kil "Okay, we got the room. So, tell me what the fuck that old dude wanted."
            scene black with fade
            "Ian truly was unique. He hadn't missed a beat amidst the ongoing circus."
            "......"
            "..."

    scene w3_3666 with circlewipe
    show screen textbox2 with dissolve
    mc "*Sigh* You are something else."

    if w3AliceSeen == True:
        scene w3_3667 with dissolve
        kil "To be honest, I'm surprised you agreed to that."
        scene w3_3666 with dissolve
        mc "...I'm just as sick as you, buddy."

    scene w3_3667 with dissolve
    kil "I like to think of it as... free therapy? Now, where were we?"
    scene w3_3666 with dissolve
    mc "Alice can't hear us, right?"
    scene w3_3668 with dissolve
    kil "We're safe. We're about as far apart as I can be without leaving the apartment."
    scene w3_3666 with dissolve
    mc "*Sigh* Alright... so, where did I leave off?"
    scene w3_3667 with dissolve
    kil "You were going to tell me what that ghoulish old fuck wanted."
    scene w3_3666 with dissolve
    mc "Riiight... I've got a lot to unpack here, so listen up."
    scene w3_3669 with dissolve
    "{i}I explained the situation to my friend.{/i}"
    "The contents of my and Abel's talk, the cryptic caution, the listening device, and how it possibly predated my tenancy."
    "He had many of the same questions as I did, which was a relief. It was proof that my anxiety over this wasn't an overreaction."
    "I mean {i}of course it wasn't{/i}, but my life had quickly become a series of outrageous events, so even the smallest affirmation helped make sure my calibration wasn't off. "
    scene w3_3670 with dissolve
    kil "Yeah, I'd say that's a big {b}what the fuck!{/b} Like all of it."
    scene w3_3671 with dissolve
    kil "Still, I wouldn't worry too much about being spied on. Who knows what the hell August used that place for in the past? He might've been keeping tabs on some girl or blackmailing some dirty rich fuck."
    scene w3_3672 with dissolve
    mc "Yeeeeah... and it's not like anyone has a reason to spy on me."
    scene w3_3673 with dissolve
    kil "Yeah, exactly... though maybe... and this is just a maybe... what if the club didn't place it there?"
    scene w3_3672 with dissolve
    mc "I hadn't even thought about that. I was so focused on the idea it was the club's."
    scene w3_3670 with dissolve
    kil "What if it was like the cops or something?"
    scene w3_3672 with dissolve
    mc "I don't think it is. The club's got the cops taken care of, right?"
    scene w3_3671 with dissolve
    kil "Either way, let's ask August or my uncle about it. It would be the most straightforward way of getting an answer."
    scene w3_3674 with dissolve
    "......"
    "..."
    scene w3_3675 with dissolve

    if kat_polite == True:
        mc "It might be related to Mrs. Pulman."
    else:
        mc "It might be related to Kathleen."

    scene w3_3674 with dissolve
    kil "How do 'ya figure?"
    scene w3_3675 with dissolve
    mc "... because, according to the woman herself, Darius blackmailed her."
    scene w3_3674 with dissolve
    kil "Eh? What the fuck are you talking about? {b}No, he didn't.{/b} Not a fucking chance."
    scene w3_3675 with dissolve
    mc "I just know what she personally told me."
    mc "So, what if the club was spying on your friend? He lived here before me, right?"
    scene w3_3674 with dissolve
    kil "H-he.. ah, he did, but... don't get me wrong, Darius was a dumb fuck druggie asshole, but he wasn't THAT dumb. What exactly did Kathy say?"
    scene w3_3675 with dissolve
    mc "She said he blackmailed her, she paid him to save herself the embarrassment, and then he ran off with one of the house girls."
    scene w3_3676 with dissolve
    "......"
    "..."
    scene w3_3677 with dissolve
    kil "Ah... what the fuck. I don't know what to make of that, dude."
    kil "I really, {i}really{/i} don't."
    kil "A few months before he disappeared, he did fall stupidly head-over-heels for one of the house girls, but she split a month before Darius did."
    scene w3_3678 with dissolve
    mc "That didn't seem weird to you?"
    scene w3_3677 with dissolve
    kil "I didn't think anything of it. Girls come and go all the time."
    scene w3_3678 with dissolve

    if kat_polite == True:
        mc "I don't even want to think about it, but... Mrs. Pulman wouldn't have {i}done something{/i} to Darius, right?"
    else:
        mc "I don't even want to think about it, but... Kathleen wouldn't have {i}done something{/i} to him, right?"

    scene w3_3677 with dissolve
    kil "{i}Something...?{/i} I have no fucking clue with that woman, but whether she paid him or dealt with him some other way, think about it for a second. Why would she tell {i}you{/i} about it?"
    scene w3_3678 with dissolve
    mc "It makes absolutely no sense to me, either."
    scene w3_3677 with dissolve
    kil "What was going on when she let something like that slip?"
    scene w3_3678 with dissolve
    mc "She was fucking with me, you know how she is, talking about..."
    scene w3_3679 with dissolve
    "...talking about speaking to my mother on the phone."
    kil "Maybe it was bullshit, then?"
    scene w3_3681 with dissolve
    mc "That's a weird thing to bullshit about."
    scene w3_3680 with dissolve
    kil "This whole thing is fucking weird, but maybe it's a test to see if you'd blather about it? New employee and all, you know? That kinda game is right up her alley."
    scene w3_3681 with dissolve
    mc "...you think? That would make {i}some{/i} sense..."
    scene w3_3680 with dissolve
    kil "I don't fucking know. Maybe, but then what about the bug? Unrelated?"
    scene w3_3679 with dissolve
    "......"
    "..."
    scene w3_3683 with dissolve
    kil "I really think we should tell my uncle. It's not okay for a patron to break into your apartment."
    mc "Isn't the customer always right?"
    kil "Fuck no! There are lines, and my uncle draws them."
    scene w3_3672 with dissolve
    mc "Maybe, but I don't really know if I want to further put myself in the middle of whatever the fuck those two have going on."
    scene w3_3673 with dissolve
    kil "You're already in the middle of it."
    scene w3_3672 with dissolve
    mc "I'd feel better if I knew what \"it\" was before I did anything."
    scene w3_3673 with dissolve
    kil "You can trust my uncle, but I'll leave it up to you to say anything."
    scene w3_3671 with dissolve
    kil "Just know I have your back. Look no further if you want help turning over some rocks or just a place to sleep."
    scene w3_3672 with dissolve
    mc "Thanks, man. I appreciate that."
    "......"
    "...I think I want to find out what happened to the last person who had my job."
    scene w3_3670 with dissolve
    kil "Eh, you could just not think about it and go back to fucking whores."
    scene w3_3672 with dissolve
    mc "Are you not worried about your friend?"
    scene w3_3682 with dissolve
    kil "...I just don't think, assuming he did something stupid, that Darius would be dealt with in the way you're thinking."
    mc "What makes you so confident? August, Warren, even Jacob... they're..."
    kil "Even if August or Kathleen wanted to, Uncle Chuck wouldn't allow it."
    scene w3_3685 with dissolve
    mc "I'm not so sure of that, dude."
    scene w3_3684 with dissolve
    kil "{b}I am{/b}. Here's the thing: my uncle calls the shots and wouldn't get his hands dirty that way."
    scene w3_3685 with dissolve
    mc "...and what would he do if someone who worked for him betrayed and blackmailed him?"
    scene w3_3684 with dissolve
    kil "...there'd be so much blowback that his own family would wish he was dead?"
    scene w3_3687 with dissolve
    mc "Jesus Christ!"
    scene w3_3679 with dissolve
    kil "Aaahk, that sounded worse than it is!"
    kil "All I'm saying is he wouldn't use violence; he's not the type. I'm one hundred percent certain of that."
    kil "With money, there's a lot of {i}legal{/i} ways you can punish someone."
    scene w3_3681 with dissolve
    mc "...uh, do you think that sounds any better?"
    scene w3_3680 with dissolve
    "......"
    kil "I mean... {i}yeah?{/i}"
    "..."
    scene w3_3688 with dissolve
    mc "Ha! What is wrong with me? We're talking about the possibility of one of my bosses disappearing someone and I'm not flipping out."
    scene w3_3689 with dissolve
    kil "That's because all Darius did was run off like the flaky prick he was, Kathleen's just fucking with you, and you're just being your usual worrying self. I'd be much more irked about that old fuck not respecting boundaries."
    kil "I wouldn't even try to understand that changing tide shit; why those vampires do anything only makes sense to them. I'd just make sure it didn't happen again."
    scene w3_3690 with dissolve
    mc "You might be right... after all, at the end of the day, maybe he really thought he was being charitable..."
    scene w3_3689 with dissolve
    kil "Yeah, look at August and Hana. Guy's trying to pretend he's not a piece of shit father all of a sudden."
    kil "I think something clicks in your brain when you get old and you pretend you can white out all the horrible shit you've done."
    scene w3_3674 with dissolve
    "......"
    "..."
    scene w3_3685 with dissolve
    mc "...first, I think I just want to be comfortable with where I will be putting my head for the foreseeable future."
    scene w3_3684 with dissolve
    kil "I got you, man. I'll drop by your mom's tomorrow; you google how to search for bugs. We'll make an afternoon of it. "
    scene w3_3685 with dissolve
    mc "...ha, yeah, I'd actually appreciate it."
    scene w3_3684 with dissolve
    kil "Maybe we'll even hatch a plan to prove Darius is just an ass hat. Of course, nothing's happened, but... {i}it would be nice to know for sure.{/i}"
    scene w3_3691 with dissolve
    "Sounded like Killian liked Darius more than he let on."
    scene w3_3672 with dissolve
    mc "Yeah. We'll be a banger pair of detectives. A real Mutt and Jeff."
    scene w3_3692 with dissolve
    kil "I'll play Riggs, you can be Murtaugh."
    scene w3_3693 with dissolve
    mc "I'm comfortable with that..."
    scene w3_3694 with dissolve
    mck "Bahaha...!"
    scene w3_3695 with dissolve
    mc "Yelling at an old woman aside, thanks for the laugh, Ian."

    if w3AliceSeen == True:
        scene w3_3696 with dissolve
        kil "Wasn't that part of the laughs? You seemed to enjoy it."
        scene w3_3697 with dissolve

        hide screen textbox2 with dissolve

        menu:
            "There is a certain appeal you won't deny(Dialogue/Render changes only).":
                show screen textbox2 with dissolve
                mc "Well, I'm going to stop pretending I don't get the appeal."
                scene w3_3696 with dissolve
                kil "Oooooh, you must really be shaken if you're not even going to bother putting on airs about it."
                scene w3_3697 with dissolve
                mc "My brain doesn't want to get it, but my dick sure does. That woman helped raise you, and you..."
                scene w3_3692 with dissolve
                kil "...know how to have a {i}good{/i} time."
                scene w3_3693 with dissolve
                mc "You like Alice, don't you?"
                scene w3_3671 with dissolve
                kil "{b}Fuck no{/b}. That whore was only around because my mom paid her, and now she's only clinging to me to get her kicks."
            "You simply love watching Ian work(Dialogue/Render changes only).":

                show screen textbox2 with dissolve
                mc "What can I say? You have a way with women that's interesting to watch."
                scene w3_3696 with dissolve
                kil "Ha! Yeah, I have a real charming personality, huh?"
                scene w3_3697 with dissolve
                mc "That or something's in the water around here."
                scene w3_3671 with dissolve
                kil "It's just people aren't as complicated as they think they are. She was only around because my mom paid her, and now she's barking up my tree to get her kicks."
                scene w3_3672 with dissolve
                mc "Don't act like you don't like Alice, dude."
                scene w3_3673 with dissolve
                kil "Fuck no, she's a whore."
            "It was sheer curiosity.":

                show screen textbox2 with dissolve
                mc "...it was hard to look away."
                scene w3_3696 with dissolve
                kil "It was my raw magnetism, right?"
                scene w3_3697 with dissolve
                mc "It was like a Giallo. Hard to comprehend and gruesome, but you watch it anyway."
                scene w3_3692 with dissolve
                kil "You're saying I've got style?"
                scene w3_3693 with dissolve
                mc "...be honest with me... you like Alice, don't you?"
                scene w3_3671 with dissolve
                kil "{b}Fuck no{/b}. That whore was only around because my mom paid her, and now she's only clinging to me to get her rocks off."
    else:
        if ianIntrospect == True:
            scene w3_3670 with dissolve
            kil "Yeeeah... sorry about trying to drag you into that. I should've known it made you uncomfortable."
            mct "(That's surprisingly reflective of him...)"
        else:
            scene w3_3670 with dissolve
            kil "Yeah, my bad. I should've known you'd be a square about it."

        scene w3_3672 with dissolve
        mc "...you like Alice, don't you?"
        scene w3_3671 with dissolve
        kil "{b}Fuck no{/b}. That whore was only around because my mom paid her, and now she's only clinging to me to get her rocks off."

    scene w3_3672 with dissolve
    mc "Really? I like Alice."
    scene w3_3698 with dissolve
    kil "...yeah, okay."
    kil "She's alright. It was better to have her around growing up than not. Although, maybe..."
    scene w3_3699 with dissolve
    "......"
    "..."
    mc "You can say it."

    if ianIntrospect == True:
        scene w3_3698 with dissolve
        kil "Sometimes I wonder if my parents would've tried a bit harder if they couldn't have shoveled the responsibility onto someone else."
        scene w3_3699 with dissolve
        mc "That's not her fault."
        scene w3_3698 with dissolve
        kil "I know, but... it doesn't make bullying her any less fun. Speaking of which..."
    else:
        scene w3_3698 with dissolve
        kil "Nothing. Just a dumb thought that's not worth voicing. I've got a lot of those, y'know?"
        scene w3_3699 with dissolve
        mc "Well, then... I should leave you to your dumb thoughts."

    scene w3_3700 with dissolve
    kil "Will you be able to fall asleep?"
    scene w3_3701 with dissolve
    mc "Probably not, but you should go reward Alice for putting up with you. So, see you tomorrow?"
    scene w3_3700 with dissolve

    if w3AliceSeen == True:
        kil "You knoooooow.... {i}we don't have to get off the phone just because of that.{/i}"
        kil "Could be fun."
        mc "....."
        mc "..."
        hide screen textbox2 with dissolve

        menu w3SleeplessCallMenu:
            "{color=#FF1493}[[Bromance]{/color} It would be fun(w3AliceOffer=True)"(chg=["killian_up2"]) if Killian_Bromance >= 20:
                $ Killian_Bromance +=2
                $ w3AliceOffer = True
                scene w3_3701 with dissolve
                show screen textbox2 with dissolve
                mc "I wouldn't want to intrude."
                scene w3_3700 with dissolve
                kil "Alice and I would both enjoy having you watch."
                scene w3_3702 with dissolve
                mc "Well, if you're going to beg me like this..."
                scene w3_3703 with dissolve
                kil "Ah, y-yeah? Ha! Fuck yes!"
                scene w3_3704 with dissolve
                mc "Don't be so excited, it's we--"
                stop music fadeout 3.0
                scene black with fade
                mct "(...he's moving faster than---)"
                jump w3AliceFakeThreesome

            "{color=#FF1493}[[Voyeur]{/color} You do like to watch...(w3AliceOffer=True)"(chg=["killian_up2"]) if history_voyeur == True:
                $ Killian_Bromance +=2
                $ w3AliceOffer = True
                scene w3_3701 with dissolve
                show screen textbox2 with dissolve
                mc "...sure, alright?"
                scene w3_3705 with dissolve
                kil "W-what? For real? That easy? No-"
                scene w3_3702 with dissolve
                mc "You're rubbing off on me, pal."
                scene w3_3703 with dissolve
                kil "Ah, y-yeah? Ha! Fuck yes!"
                scene w3_3704 with dissolve
                mc "Don't be so excited, it's we--"
                stop music fadeout 3.0
                scene black with fade
                mct "(...he's moving faster than---)"
                jump w3AliceFakeThreesome

            "Once was enough for you." if w3HanaDP <=3 and w3MinaHotelFucked == False:
                scene w3_3701 with dissolve
                show screen textbox2 with dissolve
                mc "Thanks for the offer, but once was enough for me."
                scene w3_3700 with dissolve
                kil "Yeeeeah, I figured, but it's polite to ask."
                scene w3_3707 with dissolve
                mc "Pfft, yeah, right. Night man."
                kil "Good night!"
                stop music
                play sound "sound effects/phonemenu.wav"
                scene w3_3587 with dissolve
                "Ahhhh..."
                scene w3_3584 with dissolve
                "I took a deep breath to clear my head and center myself. To my pleasant surprise, it worked."
                "My words to Ian were honest; our conversation made me feel better."
                mct "(Maybe I {i}can{/i} sleep.)"
                jump w3SleeplessNight

            "You have other ways of spending your sleepless hours." if w3HanaDP >=4 or w3MinaHotelFucked == True:
                scene w3_3701 with dissolve
                show screen textbox2 with dissolve
                mc "Thanks for the offer, but once was enough for me."
                scene w3_3700 with dissolve
                "Plus, there was someone a lot cuter that I wanted to call."
                kil "Yeeeeah, I figured, but it's polite to ask."
                scene w3_3707 with dissolve
                mc "Pfft, yeah, right. Night man."
                kil "Good night!"
                stop music
                play sound "sound effects/phonemenu.wav"
                "*Beep!*"
                jump w3CutieCall

            "{color=#696969}[[Bromance] It would be fun.{/color}" if Killian_Bromance <= 19:
                jump w3SleeplessCallMenu

            "{color=#696969}[[Voyeur] You do like to watch...{/color}" if history_voyeur == False:
                jump w3SleeplessCallMenu
    else:

        kil "Ha! You bet! See you tomorrow!"
        scene w3_3707 with dissolve
        "*Beep!*"
        stop music
        play sound "sound effects/phonemenu.wav"
        if w3HanaDP >=4 or w3MinaHotelFucked == True:
            jump w3CutieCall
        else:
            scene w3_3587 with dissolve
            "Ahhhh..."
            scene w3_3584 with dissolve
            "I took a deep breath to clear my head and center myself. To my pleasant surprise, it worked."
            "My words to Ian were honest; our conversation made me feel better."
            mct "(Maybe I {i}can{/i} sleep.)"
            jump w3SleeplessNight


label w3CutieCall:
    scene w3_3583 with dissolve
    "......"
    scene w3_3713 with dissolve
    "..."
    scene w3_3583 with dissolve
    "I took a deep breath to clear my head and center myself. To my pleasant surprise, it worked."
    "My words to Ian were honest; our conversation made me feel better, but..."
    scene w3_3713 with dissolve
    mc "*Sigh* It's late..."
    scene w3_3585 with dissolve

    if w3MinaHotelFucked == True:
        "I remembered I told Mina I'd give her a call."

        if w3HanaDP >=4:
            mct "(Plus, there was Hana. It hadn't even been a full day, but I felt like speaking to her.)"
    else:
        mct "(Should I call Hana...?)"
        "It hadn't even been a full day, but I felt like speaking to her."

    scene w3_3586 with dissolve
    "...so, should I?"
    scene w3_3585 with dissolve
    hide screen textbox2 with dissolve
    $ mod_var = False
    menu w3CutieCallMenu:
        "[mod_option] Both"(chg=["maid"]) if w3HanaDP >=4 and w3MinaHotelFucked:
            $ mod_var = True
            jump mod_w3CutieCall_hana

        "Call Hana(hana DP>=4)(w3HanaCutieCall-True)."(chg=["hana_up"]) if w3HanaDP >=4:
            label mod_w3CutieCall_hana:
            $ w3HanaCutieCall = True
            $ Hana_Affection += 1
            scene w3_3587 with dissolve
            show screen textbox2 with dissolve
            "Fuck it. She'll be cool with it."

            scene w3_3588 with dissolve
            play sound "sound effects/phonemenu.wav"
            if hanaGF == True:
                "...and, if she's not, it's not like she has many dateable options."
            else:
                "If she doesn't want late-night calls, she should rethink this fuck buddy thing."

            scene w3_3589 with dissolve
            "......"
            "..."
            jump w3CutieCallHana

        "Call Mina(w3MinaCutieCall=True)."(chg=["mina_up"]) if w3MinaHotelFucked == True:
            label mod_w3CutieCall_mina:
            $ w3MinaCutieCall = True
            $ Mina_Affection += 1
            scene w3_3587 with dissolve
            show screen textbox2 with dissolve
            "{i}I did tell her I'd call.{/i}"
            scene w3_3588 with dissolve
            play sound "sound effects/phonemenu.wav"
            "I'm a real Chatty Cathy today..."
            scene w3_3589 with dissolve
            "............"
            "........."
            "......"
            "..."
            jump w3CutieCallMina
        "Fucking someone doesn't mean you can call them in the dead of morning.":

            show screen textbox2 with dissolve
            mct "(Naaaaah.)"
            "Why ruin someone else's night of sleep because of my own?"
            scene w3_3584 with dissolve
            mct "(I'll just try and get to sleep.)"
            jump w3SleeplessNight

        "{color=#696969}[[Hana] Call your goth lover.{/color}" if w3HanaDP <=3:
            jump w3CutieCallMenu

        "{color=#696969}[[Mina] Call the bubbly blonde.{/color}" if w3MinaHotelFucked == False:
            jump w3CutieCallMenu

label w3CutieCallHana:
    if _in_replay:
        show screen textbox2 with dissolve

    play music "music/stoned.ogg"
    scene w3_3590 with dissolve

    if hanaGF == True:
        hana "'sup, boyfriend."
    else:
        hana "Heeeeey, [mcf]."

    scene w3_3708 with dissolve
    mc "Oh good, it sounds like I didn't wake you."
    scene w3_3709 with dissolve
    hana "Yep, burning the midnight oil. Have you ever seen a movie called {i}The Machine Girl{/i}?"
    scene w3_3708 with dissolve
    mc "Can't say that I have."
    scene w3_3710 with dissolve
    hana "Ha, it's fucking crazy! I'm in the middle of watching it."
    scene w3_3711 with dissolve
    mc "Give me the rundown."
    scene w3_3712 with dissolve
    hana "A Japanese schoolgirl's younger brother is killed and she takes revenge on the bullies who did it."
    hana "Along the way, she replaces her arm with a machine gun and goes head-to-head with a Ninja-Yakuza family."
    scene w3_3597 with dissolve
    mc "Sounds like my kind of movie."
    scene w3_3598 with dissolve
    hana "Yeah, it's excellent! {i}A lot of splatter!{/i}"
    hana "Hell, there's a scene where the main character's arm gets coated in tempura batter and deep-fried! Like, what the fuck? I was laughing my ass off."
    scene w3_3597 with dissolve
    mc "Show it to me sometime. I'd love to see it."
    scene w3_3598 with dissolve
    hana "Yeeeah, you bet! So, what's up? Booty call?"
    hide screen textbox2 with dissolve
    scene w3_3595 with dissolve

    menu:
        "You missed her voice."(chg=["hana_up"]):
            $ Hana_Affection +=1
            scene w3_3714 with dissolve
            show screen textbox2 with dissolve
            mc "I was just lying here and realized I missed your voice."
            scene w3_3715 with dissolve
            hana "...you just come out and say stuff like that, huh?"
            scene w3_3716 with dissolve
            mc "Too clingy?"
            scene w3_3717 with dissolve
            hana "Hell no. You should say what you feel, for example... I'm... {i}happy you called{/i}."
            scene w3_3716 with dissolve
            mc "Missing me already?"
            scene w3_3715 with dissolve
            hana "Hehe, no. Just {b}happy you called.{/b}"
        "Playfully chide her over the idea.":

            scene w3_3714 with dissolve
            show screen textbox2 with dissolve
            mc "Why do you immediately jump to sex? What happened to romance?"
            scene w3_3717 with dissolve
            hana "Romance goes to bed by 1 AM."
            scene w3_3714 with dissolve
            mc "Sorry to disappoint you. This isn't a booty call."
            scene w3_3715 with dissolve
            hana "Really? Oh well, I guess I'll live."

    scene w3_3716 with dissolve
    mc "How was your day?"
    scene w3_3718 with dissolve
    hana "Above average. As you know, I woke up in a good mood."
    scene w3_3719 with dissolve
    mc "Go on..."
    scene w3_3718 with dissolve
    hana "You may or may not have played a part in that."
    scene w3_3719 with dissolve
    mc "Go on, go on..."
    scene w3_3720 with dissolve
    hana "After we ate, I went home, got grilled by my mom, grabbed a biiiiig lunch with Jerrica and Spider, and put in a killer effort at the gym."
    scene w3_3721 with dissolve
    mc "You work out?"
    scene w3_3722 with dissolve
    hana "Oh, god. Such a guy thing to say."
    hana "Do you think I look as good as I do naturally? It takes a lot of work."
    scene w3_3723 with dissolve
    mc "Well, thank you for your hard work."
    scene w3_3724 with dissolve
    hana "I don't do it for you, asshole."
    scene w3_3723 with dissolve
    mc "You didn't then, but how about now?"
    scene w3_3722 with dissolve
    hana "We'll see, but if you want to keep my tight ass, you must keep things interesting for me."
    scene w3_3725 with dissolve
    mc "That right...?"
    scene w3_3726 with dissolve
    "Suddenly, I felt {b}horny.{/b}"
    scene w3_3725 with dissolve
    mc "What are you wearing?"
    scene w3_3726 with dissolve

    if w3HanaMutual == True:
        hana "Oh...? We're fucking doing {b}this{/b}, huh?"

    scene w3_3727 with dissolve
    mct "(Well, I do know what might put me to sleep...)"
    scene w3_3728 with dissolve

    if hanaGF == True:
        mc "I'm just a curious guy, wondering what my girlfriend is wearing."
        scene w3_3729 with dissolve
        hana "Well, you called me in the middle of the night, as I was going to bed, so about the usual..."
        hana "{b}...nothing but a smile and an old pair of 7-inch {i}fuck me{/i} heels."
        hana "What about you, boyfriend?"
    else:
        mc "I'm just a curious guy, wondering what you're wearing."
        scene w3_3729 with dissolve
        hana "Well, you called me in the middle of the night, as I was going to bed, so about the usual..."
        hana "{b}...nothing but a smile and an old pair of 7-inch {i}fuck me{/i} heels."
        hana "What about you, [mcf]?"

    scene w3_3730 with dissolve
    mc "Holy shit, I can't believe it. I'm wearing the same."

    scene w3_3731 with dissolve
    "......"
    "..."
    mc "I'm having trouble sleeping, babe."
    scene w3_3732 with dissolve
    hana "Mmmmhh~ Oh, poor baby. Let Hana help with that..."
    scene w3_3731 with dissolve
    "Her voice dropped an octave, taking on an unusually sweet note of indulgence."
    scene w3_3733 with dissolve
    hana "If ONLY I was there..."
    scene w3_3734 with dissolve
    "Her words then dwindled into a thick whisper, trailing off and allowing my imagination to fill in the gaps."
    mc "Yeah? What would you do to me?"
    "But it wasn't my imagination I was interested in. I wanted the vivid details straight from Hana's lips."
    scene w3_3733 with dissolve
    hana "I'll do you one better than that. I can tell you what I promise I'll do to you the next time we see each other..."
    scene w3_3734 with dissolve
    "She teased me with another pregnant pause, full of meaning and more tantalizing than the last."
    scene w3_3731 with dissolve
    mc "Don't let me die here, beautiful. I'm waiting."
    mct "(Was every woman that surrounded me a born succubus?)"
    scene hana_ps_01_a with dissolve
    hana "Mmmhhh...♥ How hard are you right now?"
    hide screen textbox2 with dissolve

    menu:
        "Be truthful(Dialogue/Render Chnages only).":
            scene hana_ps_01_a with dissolve
            show hana_ps_01 with dissolve
            mc "About halfway there and getting harder by the syllable. You've got a real enchanting voice, you know that?"
            hana "That's the horny talking."
            mc "Take me there, Hana. Tell me what you're going to do to me."
            hana "MMmhhh...♥ Next time I see you, no matter where we are, I'm going to get down on my knees and blow you."
        "Don't just be passive. Mix in your own dirty talk(Dialogue/Render Chnages only).":

            scene hana_ps_01_a with dissolve
            show hana_ps_01 with dissolve
            mc "You should have a pretty good idea. How hard was it when I buried all eight inches inside your cunt Sunday night?"
            hana "It doesn't take much to get you going."
            mc "It's all you, Hana. I'm hard for {b}you{/b}."
            hana "Haaa-♥ Then, you better have that same enthusiasm the next time I see you. Because no matter where we are, I will get down on my knees and blow you."


    mc "Anywhere...?"
    hana "{b}Wherever{/b}. No matter if it's at your place, the club, or even a restaurant bathroom... nothing's gonna stop me until I'm satisfied and I suck out all your children."
    mc "You're just saying that to get me off..."
    hana "No bullshit, just a promise. I'm going to taste EVERY inch of you."
    hana "I'll lick your balls, I'll clean the underside of your shaft with my tongue, and I'll strangle your cock so hard with my tight throat that we might just end up with a medical emergency on our hands."
    mc "Baha, what? Holy shit! Where's this coming from...?"
    hana "Mmmhh...♥ The other night~"
    hana "Don't get me wrong, Sunday was wonderful, but you stopped dicking down my face too soon."
    hana "I meeeean, you barely scuffed my makeup, [mcf], even after I asked you {i}nicely{/i} to {b}really{/b} let me have it."
    mc "Ahh, f-fuck...!"
    "She knew how to appeal to the animal in me."
    scene w3_3735 with dissolve
    hana "...how hard are you right now?"
    scene hana_ps_02_a with dissolve
    show hana_ps_02 with dissolve

    menu:
        "Be truthful(Dialogue/Render Chnages only).":
            mc "So hard that it hurts."
            hana "Are you stroking yourself?"
            mc "Ahh, y-yeah...! You know I am."
            hana "Good, I'm touching myself too right now - ahhh...♥"
            scene hana_ps_03_a with dissolve
            show hana_ps_03 with dissolve
            hana "I'm touching myself to the thought of what you'd do to me, [mcf]. Aahhh...♥ Tell me what you're going to do to me!"
        "Be truthfully truthful(Dialogue/Render Chnages only).":

            mc "So hard that the only thing that eases the pain is the image of your snot, spittle, and runny makeup rolling down your face as I shoot a fat load down your throat."
            hana "W-woahh... ahh....♥ Ehaha... you're feeling it bad, huh? You're stroking yourself, right?"
            mc "Aahhaa...! You know EXACTLY what you're doing to me, slut."
            scene hana_ps_03_a with dissolve
            show hana_ps_03 with dissolve
            hana "Good! I'm touching myself too...♥ Tell me what you will to do to me, [mcf]!"

    mct "(What would I do...?)"
    "It was so much easier when she was the one talking..."
    hana "My fingers are spreading my pretty pink pussy for you...♥"
    "As the possibilities pooled in my head, trying to fish out the answer proved difficult."
    hana "I'm playing with myself thinking of you, [mcf]. Come on..."
    "Hana kept her tone sultry, but tiny, delectable cracks formed in her persona."
    hana "You and your giant, delicious cock...♥"

    if hanaGF == True:
        hana "I'm waiting... tell me, boyfriend..."
    else:
        hana "I'm waiting. {b}Tell me.{/b}"

    "Spread out in the pitch-black darkness, those small imperfections become my sole focus, making me forget all about yesterday."
    hana "What would you do if I was there right now...? How would you fuck me?"
    "I hung on Hana's every word, gratified by the way her enunciation would subtly falter while she coaxed herself into a state of arousal."
    hana "Gh- Mmmhhhmmhhm~ [mcf]..."
    "I was absorbed in how she masked her sighs with more ear-pleasing, lyric-like purring."
    scene hana_ps_02_a with dissolve
    show hana_ps_02 with dissolve
    mct "(Ah- ahh, f-fuck...!)"
    "She's waiting..."
    mc "What would I do after you've \"sucked me for all I'm worth\", you mean? It's simple."
    mc "I'd give you a long, deep kiss worthy of your oral devotion."
    hana "A kiss...? That's what you-"

    menu:
        "Make it (gross and) lewd(Dialogue/Render Chnages only).":
            scene hana_ps_04_a with dissolve
            show hana_ps_04 with dissolve
            mc "I would taste myself on your lips and the inside of your mouth, relishing that a part of me is coating the inside of your esophagus."
            hana "Ooofh, y-yeah?"
            mc "Your mouth would reek of me, my semen clinging to your throat, but I wouldn't mind because it's not just me I'm tasting or smelling."
            hana "[mcf]... that's... {i}wow...{/i}"
            mc "What can I say? You do funny things to me."
            mc "It's the result of your care and attention, and proof of how much of a good cock-sucking bitch you are."
            hana "Haha, gross, but aah...♥ But I did a good job~ I guess I would deserve a kiss..."
            mc "Exactly. A dirty, messy, sloppy, {b}disgusting{/b} kiss and then..."
        "Describe it passionately(Dialogue/Render Chnages only).":

            scene hana_ps_04_a with dissolve
            show hana_ps_04 with dissolve
            mc "You know the kind of kiss I mean. The kind I gave you when we were on the karaoke room floor, full of promise of what's to come. "
            hana "..ehehe, and what's to {i}cum{/i}, [mcf]? You? Me?"
            mc "Shut up. I'm doing my best here."
            hana "Sorry, sorry... {i}I'm into it.{/i} Go on..."
            mc "I'd press {b}hard{/b} into you, towering over you. All you'd see is my face and those broad shoulders you like, but you'd feel my burning cock curve and bend flat against your stomach."
            hana "Oooh, I'm picturing it now."
            mc "We'd lose track of the time. My hands would trace up your ribcage, circle around your fat tits, snake past your clavicle, and..."

    hana "Mmmhh♥ And then what...?"

    menu:
        "You'll take her breath away(Dialogue/Render Chnages only).":
            mc "You'd feel my grip on your neck. Not enough to hurt, but to control and slowly bring your breathing to a crawl."
            hana "Ah, hhhaaa-♥ Fuck yeah!"
            mc "Your head will be pounding, blood will congest in your brain, and you'll feel lightheaded. "
            hana "Mmmhh~ [mcf]...!"
            mc "Every breath you take will be at my discretion. You'll be so turned on that any puff of air I allow you will be a precious thing to savor."
            hana "Ah, fuck, ha! How did you know?"
            mc "Whenever I sparingly loosen my grip on your throat, the euphoria of oxygen returning to the brain will hit you like a freight train."
            hana "Fuck me, we should try this...♥"
        "You'll strip her bare(Dialogue/Render Chnages only).":

            mc "No matter where we are, I'd strip you completely naked. {b}Down to your toes.{/b}"
            mc "Maybe we're just in my apartment and it's no big deal."
            hana "Mmmhh, maybe..."
            mc "Maybe we'll be at the club and you'll just be dressed for your part."
            hana "Baha! Mmmh, f-fuck you...! Keep talking!"

    scene hana_ps_05_a with dissolve
    show hana_ps_05 with dissolve
    mc "Gaaah, hhhhaaa... Hana. Do you hear that?"
    "*Fwap, chwap, fap!*"
    "I went silent, picking up the pace, hoping the lewd sounds of hand-on-dick contact would reach her."
    hana "Haa, yeah, I hear it..."
    mc "Good. I'm jackhammering my cock so hard to that thought of you that it hurts."
    "*Fap, fap, fap!*"
    hana "I love that sound! Hehe, we should include it in one of our songs~"
    mc "O-ohh, hhngg... I'm getting close!"
    scene hana_ps_03_a with dissolve
    show hana_ps_03 with dissolve
    hana "Not yet... haa, hhhaa...♥ Don't blow yet! Tell me how you'd fuck me as you cum!"
    "I wasn't going to stop, so I had to find the words quickly. "

    menu:
        "You'll fuck her slow and deep(Dialogue/Render Chnages only).":
            mc "I'd take it slow, fucking you deeply."
            hana "Haahh, yyeeahh-?"
            mc "Slow enough that you'll feel every inch of me enter you and every thrust would be a memory fucked into your brain."
            hana "Hnngg, I f-feel it...♥"
            scene hana_ps_04_a with dissolve
            show hana_ps_04 with dissolve
            mc "I'd pull out slowly and then push in as far as you could take me."
            hana "I feel you [mcf]...♥♥ Mmmhh, yes! I'd wrap my legs around you, pushing you even deeper!"
            hana "Uuugh, I'd hold you tight, begging you to go faster-♥♥♥ Hggg- M-making you go faster!"
            hana "You won't escape me until you give me everything! Ah... cum for me, [mcf]! Go ahead and--"
            mc "H-Hana, I'm--"
        "You'll fuck her fast and hard(Dialogue/Render Chnages only).":

            mc "How else do you think I'll fuck you? You're not the type to hide how you like it; I'd push your face into the fucking ground!"
            hana "Haa, hhaa...♥ Keep going-"
            mc "I'd spank your ass, pull your hair, and pound away. No rhythm, no thought, no... we'd just rut."
            hana "Keep going, k-keep going...♥"
            scene hana_ps_04_a with dissolve
            show hana_ps_04 with dissolve
            mc "The sound would be something else! Ball slapping, skin-on-skin... anyone who passed by would know exactly what we were doing."
            hana "[mcf]...♥ [mcf]...♥♥"
            mc "You'd be moaning my name just like that. I'd grunt, eyes rolled into the back of my head, calling out yours- hhaa, hhnna..."
            hana "Mmhh, hhaa- [mcf]♥♥♥"
            mc "H-hana, I'm--"

    if hanaGF == True:
        hana "{b}Explode for me{/b}, boyfriend."
    else:
        hana "{b}Explode for me{/b}, lover."

    scene w3_3736 with dissolve
    with flash
    play sound "sound effects/spurt.wav"
    with vpunch
    "I didn't give much thought to the mess; I just let myself explode all over my old bedroom."
    scene w3_3737 with dissolve
    mc "Mmmh-"
    "Not like it was the first time I'd jacked off in here."
    scene w3_3738 with dissolve
    "......"
    "..."
    scene w3_3739 with dissolve
    hana "Sounds like you had a nice finish. Did Hana make you feel better?"
    scene w3_3740 with dissolve
    mc "You're the best. I think I'm going to sleep like a baby."
    $ renpy.end_replay()
    scene w3_3739 with dissolve
    if not persistent.w3HanaPhoneSex:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3HanaPhoneSex = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    hana "You're not wrong about the first part. That was... {i}fun{/i}."
    hana "I've never had phone sex before. I figured it would be a lot more embarrassing than it was."
    scene w3_3741 with dissolve
    mc "Maybe you're just shameless."
    scene w3_3742 with dissolve
    hana "That's a real possibility, but I'd be in good fucking company."
    scene w3_3741 with dissolve
    mc "Heh, come to think of it, that was my first time too."
    mc "I mean, why would you ever do it over the phone unless you're in a long-distance relationship?"
    scene w3_3742 with dissolve
    hana "You're the one who started it, so you tell me."
    scene w3_3741 with dissolve
    mc "I didn't plan on it when I called. I'm actually sleeping at my mom's house right now."
    scene w3_3743 with dissolve
    hana "How come? What's up?"
    scene w3_3744 with dissolve
    mc "It's a long story. One that I'll tell you about later."
    scene w3_3742 with dissolve
    hana "Alright... you want me to stay on the phone until you fall asleep?"
    scene w3_3741 with dissolve
    mc "That won't be necessary. Heh, you've done enough for me..."
    scene w3_3745 with dissolve
    "For a few minutes, we continued our small talk until it had all run out, leaving us with nothing much to say."
    "We fumbled to find conversational threads, not wanting to get off the phone, but our brief chat had run its natural course and I felt my eyes getting heavy."
    mc "So, uh, yeah... I'll talk to you later?"
    scene w3_3746 with dissolve
    hana "There's a good chance you'll hear from me again."
    scene w3_3745 with dissolve
    mc "Heh, I feel bad getting off the phone so soon after-"
    scene w3_3746 with dissolve
    hana "Pssh, what do you take me for? I know you need your beauty rest."
    hana "In fact, you made my night interesting."
    scene w3_3745 with dissolve
    mc "...was it good for you?"
    scene w3_3746 with dissolve
    hana "Ha! I hate this lingering-around feeling, so I'm hanging up now."
    scene w3_3747 with dissolve

    if hanaGF == True:
        hana "Get a good night's sleep, boyfriend."
    else:
        hana "Get a good night's sleep, [mcf]."

    play sound "sound effects/phonemenu.wav"
    stop music
    scene w3_3748 with dissolve
    show screen textbox2 with dissolve
    mct "(Heh.)"
    scene w3_3749 with dissolve
    "......"
    "..."
    mct "(I will.)"
    scene black with fade
    "...after I clean up my cum."
    if mod_var:
        $ mod_var = False
        m_dev "Let's call mina now"
        jump mod_w3CutieCall_mina
    "........."
    "......"
    "..."
    jump w3BreakfastWithIan

label w3CutieCallMina:
    scene w3_3590 with dissolve
    mina "Mmhh... wwwahha...? Heeeeeeyyyy...!"
    "Just before the final ring sent me to voice mail, a sleepy Mina broke through with a sloppy and slurred salutation."
    hide screen textbox2 with dissolve

    menu:
        "Make a joke. Tell her you couldn't sleep(Dialogue/Render Chnages only).":
            scene w3_3591 with dissolve
            show screen textbox2 with dissolve
            mc "Yes, hello, I'd like to order one cutie, please."
            scene w3_3590 with dissolve
            mina "............"
            mina "........."
            mina "......"
            play music "music/inner-light.ogg"
            scene w3_3751 with dissolve
            mina "...is a woman's beauty sleep a joke to you, [mcf]?"
            scene w3_3752 with dissolve
            mc "I think you're beautiful no matter how much sleep you've had."
            "......"
            scene w3_3753 with dissolve
            "..."
        "Start by apologizing for not calling her earlier."(chg=["mina_up"]):

            $ Mina_Affection +=1
            scene w3_3750 with dissolve
            show screen textbox2 with dissolve
            mc "Heeeeey, guess what asshole said they'd call you yesterday and then didn't?"
            scene w3_3591 with dissolve
            mc "I hope waking you up in the middle of the night conveys my sincere apologies. I just couldn't wait, you know?"
            scene w3_3590 with dissolve
            mina "............"
            mina "........."
            mina "......"
            play music "music/inner-light.ogg"
            scene w3_3751 with dissolve
            mina "Heh, mmmhmhhhh..... hehe... it's cool. Not hearing from you did make me a little anxious, but I knew I was being stupid."


    scene w3_3754 with dissolve
    mina "Yaaaaaawwwhhhhnn, mmmh... what time is it?"
    scene w3_3753 with dissolve
    mc "A little past two in the morning."
    scene w3_3755 with dissolve
    mina "Is everything alright?"
    scene w3_3756 with dissolve
    mc "I couldn't sleep."
    scene w3_3757 with dissolve
    mina "...so you thought I shouldn't either?"
    scene w3_3756 with dissolve
    mc "...sorry about that."
    scene w3_3758 with dissolve
    mina "Ah, crud. Me too. I sounded more peeved than I wanted to."
    scene w3_3756 with dissolve
    mc "It's 2 AM. I woke you up... I get it."
    scene w3_3760 with dissolve
    mina "I'm happy that you called. It means that I'm on your mind."
    scene w3_3759 with dissolve
    mc "How could you not be?"
    scene w3_3760 with dissolve
    mina "Heh, flattery isn't the worst way to wake up, either."
    scene w3_3759 with dissolve
    mc "Do you ever get sick of being complimented? You must get a lot of it. "
    scene w3_3598 with dissolve
    mina "It depends on who's giving it and the why... right now, mmmhhh..."
    mina "Was your apartment okay?"
    scene w3_3761 with dissolve
    mc "My apartment, what do...? Aaaaaaaah, {i}yeah.{/i}"
    scene w3_3762 with dissolve
    "My half-assed excuse for splitting on her."
    scene w3_3596 with dissolve
    mc "Everything was fine. The water didn't get in."
    scene w3_3595 with dissolve
    mina "That's good... why can't you sleep then? Are you not tired after {i}today?{/i}"
    scene w3_3597 with dissolve
    mc "The answer to that is quite simple and really stupid. {b}I had a nap.{/b}"
    scene w3_3763 with dissolve
    mina "Pffhhh- wwwwh... the nappy wappy did it?"
    scene w3_3764 with dissolve
    mc "If you really think about it, it's all your fault."
    scene w3_3765 with dissolve
    mina "Oooooh? How did you figure, [mcf]?"
    scene w3_3766 with dissolve
    mc "Just sayin'... I didn't tucker myself out on my own."
    scene w3_3765 with dissolve
    mina "And what do you want me to do about it?"
    scene w3_3766 with dissolve
    mc "Good question. Do you know anything that might help me sleep?"
    scene w3_3767 with dissolve
    mina "Have you tried counting sheep?"
    scene w3_3768 with dissolve
    mc "I tried, but I lost count."
    scene w3_3767 with dissolve
    mina "How about you warm up a glass of milk?"
    scene w3_3768 with dissolve
    mc "Milk after my \"nappy wappy?\" That would complete the package."
    scene w3_3769 with dissolve
    mina "Hmmm, alright..."
    scene w3_3770 with dissolve
    scene w3_3771 with dissolve
    mina "Let's just have a long-distance sleepover!"
    scene w3_3772 with dissolve
    mc "What does that entail? Should I go get some chocolate and marshmallows?"
    mina "That's a campout. You don't have s'mores at a sleepover."
    mc "Okay, what does a sleepover involve?"
    scene w3_3773 with dissolve
    mina "It's simple. We'll just chat, chat, chat until one of us falls asleep."
    scene w3_3774 with dissolve
    mc "Do we just hang up if one of us falls asleep?"
    scene w3_3773 with dissolve
    mina "...no. You got to listen to the other person snooze."
    scene w3_3774 with dissolve
    "......"
    scene w3_3775 with dissolve
    "..."
    scene w3_3776 with dissolve
    mina "I hope that doesn't sound stupid."
    scene w3_3775 with dissolve
    mc "Sounds perfect to me."
    scene w3_3777 with dissolve
    mina "{b}Good{/b}... the idea kinda reminds me of when I was in middle school and I'd stay up past my bedtime talking to my best friend at the time. Life was simpler back then..."
    scene w3_3778 with dissolve
    mc "You and I are both too young to say things like that."
    scene w3_3777 with dissolve
    mina "Speaking of youth, let's get down to the nitty-gritty. What was your favorite cartoon growing up? And don't pretend like you don't have one."
    scene w3_3778 with dissolve
    mc "It's going to be one of those kind of chats?"
    scene w3_3777 with dissolve
    mina "You're the one who called me in the middle of the night, so I get to pick the topic. Deal with it."
    "So it was, we opined nostalgically. Talking about the things we used to enjoy, filling in the blanks for each other about what helped turn us into the messes we are."
    stop music fadeout 3.0
    scene black with fade
    "It turned out I was the first casualty. Somewhere discussing the proper procedure of pouring milk into a bowl of cereal and if said cereal was considered a salad or a stew."
    "When I awoke the next morning, there was no Mina on the line, sleeping or not. The little liar broke her own rule, not that I blame her."
    "{i}Who would want to listen to someone sleep?{/i}"
    jump w3BreakfastWithIan

label w3AliceFakeThreesome:
    kil "Good news, cow! [mcf] wants to watch me pound you stupid!"
    play music "music/as-i-figure.ogg"
    scene w3_4284 with wipeleft
    alice "W-watch...? Uh, b-but..."
    scene w3_4281 with dissolve
    "In no time at all, my friend had me back on a video call and pointed at the bewildered maid."
    mc "Hello again, Alice."
    "...I awkwardly called out through the divide of Ian's phone screen."
    scene w3_4282 with dissolve
    alice "...ah, h-hey again..."
    scene w3_4283 with dissolve
    kil "Why are you just sitting there with a dumber look than usual on your face? Didn't you hear what I said?"
    scene w3_4284 with dissolve
    alice "You said [mcf]'s going to watch..."
    scene w3_4285 with dissolve
    kil "That's right. He can't sleep and your sorry ass is going to be his entertainment."
    scene w3_4286 with dissolve
    alice "......"
    scene w3_4288 with dissolve
    "I wasn't entirely sure where Alice ended and where her character in this rehearsed play started, but the embarrassment and shame written on Alice's face made for an enticing image."
    scene w3_4287 with dissolve
    alice "...anything you want, Ian."
    scene w3_4288 with dissolve
    kil "{i}I{/i} want...? Oh no, no, no, no, no, no."
    scene w3_4289 with dissolve
    kil "Look at me."
    kil "You did this the last time I involved someone else in your training. You played coy and tried to hide just how much of a slut you happily are."
    kil "That act has its charms, but that's not going to cut it tonight. [mcf]'s special. I want him to see your {b}real{/b} face."
    scene w3_4290 with dissolve
    alice "That's... uh... a l-little-"
    scene w3_4289 with dissolve
    kil "{b}Answer me.{/b}"
    kil "Who knows you better than I do?"
    scene w3_4290 with dissolve
    alice "...uh, n-no one?"
    scene w3_4289 with dissolve
    kil "That's right. We've known each other my whole life and I've seen every side of you, Alice."
    kil "I've seen the good, the bad, the sad, and even the parts that you're too afraid to show anybody else."
    scene w3_4291 with dissolve
    alice "You're so obnoxious..."
    scene w3_4292 with dissolve
    kil "{b}Look at me{/b}, slut."
    alice "Hnnggg..."
    kil "I've got the complete picture of Alice Mendoza. {b}It's mine.{/b}"
    scene w3_4293 with dissolve
    alice "Mmmmhh....♥"
    hide screen textbox2 with dissolve
    play ambient "sound effects/fel3.wav"
    scene alice_ir_finger_a with dissolve
    show alice_ir_finger with dissolve
    mct "(Um... did they forget I was here?)"
    kil "But what do you do with a picture you cherish, Alice? Do you lock it away in a scrapbook and forget about it? Or do you frame it proudly and show it off?"
    kil "Let's widen the circle of people who know you tonight. If there's anyone else who can see and accept you like I do, it's [mcf]."
    alice "Hmmm, ehhuuhh-♥♥"
    "My friend had the stalwart woman eating out of the palm of his hand."
    kil "He's got everything you want. He's young, got a big cock..."
    "Something in his words triggered Alice."
    alice "*Slurp, chwuuup~* Mmhh...♥♥♥"
    kil "Most importantly, {b}you know him{/b}. He's not going to judge you."
    mct "(Was it me or...)"
    "Right now, on my tiny screen, Alice looked different."
    kil "You can be yourself.."
    "She looked younger."
    kil "You can let go."
    "She looked..."
    alice "Mmhh, mmmh, ehhuuu-"
    stop ambient
    scene w3_4294 with dissolve
    alice "W-waohhh- ahh-ahh..."
    scene w3_4295 with dissolve
    alice "P-please let me suck your cock!"
    "...{i}lewd.{/i}"
    scene w3_4296 with dissolve
    "The older woman fell at my friend's feet, absorbed in a cock-hungry daze."
    kil "There it is. That's the Alice I wanted to see."
    scene w3_4297 with dissolve
    kil "You getting a good look at this?"
    mc "Yeah, I'm seeing her..."
    kil "She changed her tone real quick. She was stiff as a board with Amber, but this..."
    play music "music/hypnosis.ogg"
    scene w3_4298 with fade
    kil "Isn't this her best look? Fifty-five years of life and she's elated to have the balls of the man she raised on her chin."
    "I could tell from the enthusiasm in his words that Ian was relishing showing her off to me."
    kil "What. A. Fucked. Up. Bitch."
    scene w3_4299 with dissolve
    alice "C-can I...?"
    scene w3_4298 with dissolve
    "He was proud of his work."
    scene w3_4300 with hpunch
    kil "Nope! Get your fat ass on the bed!"
    scene black with fade
    kil "I told you from the beginning how this was going to play."
    scene w3_4301 with goslow
    "In short order, my friend had his nanny bent over the bed, the three of us face-to-face-to-face."
    scene w3_4302 with dissolve
    alice "Ah, uh... this is new to me. I apologize if-"
    scene w3_4301 with dissolve
    mc "...don't hide it, Alice."
    scene w3_4303 with dissolve
    kil "She getting my good side, bro?"
    scene w3_4304 with dissolve
    mc "Yeah, you look like a million bucks."
    scene w3_4303 with dissolve
    kil "Awesome. Watch her expression as I put it in."
    scene w3_4305 with dissolve
    "Wasting no time, he made good on the claim and..."
    scene w3_4306 with instantdissolve
    alice "--♥"
    kil "Cute, right?"
    scene w3_4307 with dissolve
    kil "This right here is the hag's best feature."
    scene w3_4308 with dissolve
    mc "Are you trying to sell me a car?"
    scene w3_4307 with dissolve
    kil "She might not look like much, but when you get her ass up like this..."
    scene w3_4309 with dissolve
    play sound "sound effects/slap3.wav"
    scene w3_4310 with vpunch
    alice "Ah! O-ohh..."
    scene w3_4311 with dissolve
    kil "She's more attractive than a woman half her age."
    scene w3_4312 with dissolve
    "It was difficult to disagree. From this limited angle, the maid's ass loomed like a mountain and towered with the majesty of years of robust living."
    scene w3_4313 with dissolve
    alice "Hnhhhg...♥ I-Ian, you talk too much..."
    scene w3_4314 with dissolve
    mc "He's over-compensating for years of shyness."
    scene w3_4315 with dissolve
    alice "Heh... mayb-"
    scene w3_4316 with dissolve
    alice "Ah, haahaa-"
    "Ian gently rolled his hips, catching Alice off guard and getting us back to the task at hand."
    kil "Now, watch it in motion!"
    play music "music/six-days-of-heat-pt2.ogg"
    scene alice_ir_dog2_a with dissolve
    show alice_ir_dog2 with dissolve
    "I did as he asked, my perverse curiosity from earlier still burning as strong as ever as I watched Alice's ass endure impact after impact of my friend's swinging hips."
    kil "Ha! You being here is better than any foreplay. This greedy cunt is already swallowing me whole!"
    "Each collision sent Alice's rear-end shaking like gelatin, hypnotically bouncing up and down, as I felt myself growing hard at the thought of wearing the old woman's prodigious ass like a cockholster."
    scene alice_ir_dog1_a with dissolve
    show alice_ir_dog1 with dissolve
    alice "That's, ah... hnggg... you've kept me waiting a-all night..."
    kil "Bullshit. You like showing [mcf] your slutty face!"
    "Each well-timed thrust was like a lullaby to my sleep-deprived mind; the stark {i}plap, plap, plap{/i} forcing my complete focus on something other than the idle clamor going on between my ears."
    alice "That's not it... it's just- aaah... it turns me on making you happy...!"
    kil "Yeah, right! It turns you on imagining being stuffed from both ends with cock, doesn't it?"
    alice "No? Yes? M-maybe-?"
    kil "I thought you came around to being honest, but you went right back to this wishy-washy crap! I don't get it..."
    "Ian began laying into Alice, and I could tell by her expression, that it was fanning something vile in her that she didn't understand. "
    kil "Is it more fun when you feel mixed up on the inside? Or is it just more exciting to pretend like you're not a disgusting fuck-pig wanting to be broken by a younger dick?"
    alice "Ah, hahaa-♥ I-Ian-♥"
    kil "Don't \"Ian\" me, bitch! My friend's right in front of your eyes! Focus on him!"
    alice "Ahh, hhhuu- buuut-"
    kil "{b}Imagine{/b} that it's [mcf]'s dick filling you right now! You'd like that, wouldn't you?"
    alice "Ahh, hhh mahhh-- he"
    kil "Fucking cunt! Imagine the feeling of his new, {i}you've-never-tasted-before{/i} cock ripping you a new one."
    alice "Mmmhh, h-he w-wouldn't want that...!"
    kil "Sure he would! Look at how closely he's watching you. He's scrutinizing every wrinkle on your face!"
    scene w3_4317 with dissolve
    kil "He's bigger than me, y'know? And he could give it to you just as hard!"
    alice "Haat...♥"
    mct "(This was so fucking weird, but...)"
    scene w3_4318 with dissolve
    kil "Imagine {i}us{/b} coming at you from both ends! You would like that, wouldn't you?"
    alice "M-maaybe-!"
    "Ian was speaking my language, liberally feeding his ugliness without compunction, and {b}that{/b} pulled me in."
    scene alice_ir_dog2_a with dissolve
    show alice_ir_dog2 with dissolve
    kil "Maybe? Should I stop fucking you then, you coy cunt?"
    alice "N-no, d-don't-"
    kil "Then ask [mcf] to keep fucking you."
    "Despite his threats, Ian switched his steady-even rhythm for a more fervent display."
    alice "Ah, [mcf]...? B-but y-you-!"
    kil "Ask him to keep riding your fat, piggy ass~"
    "His words were underlined by the melodious pistoning of the pair's hips wantonly seeking orgasm."
    alice "K-keep fucking me, [mcf]!"
    kil "Ha! You're imagining it, aren't you?"
    alice "Haaa, y-yes! I'm im-imagining it-!"
    kil "I can tell! You're sucking me in so hard~ you like imagining someone else other than me is fucking you!"
    alice "I-Ian, that's not-"
    play sound "sound effects/thud-floor.mp3"
    play ambient "sound effects/boobjob.wav"
    scene alice_ir_dog3_a with vpunch
    show alice_ir_dog3 with dissolve
    alice "Aggg-♥"
    kil "Don't backpedal, you sorry hag!"
    alice "Soooowhhtyy!"
    kil "You stupid, greedy slut!"
    alice "Ah, hhhnggg-♥♥"
    kil "Don't you backpedal!"
    alice "I w-wont, aahh, hhhh- ssoohhh-"
    kil "Don't you FUCKING backpedal, you sorry cunt!"
    alice "Y-yes...♥♥♥"
    kil "Stupid. Fucking. Sorry. Cunt!"
    alice "Hnnng-!"
    kil "All your empty head needs to do is imagine two thick cocks straining your worn-out holes~"
    alice "Hhh, I'm picturing it-!"
    kil "Would you like that, Ms. Mendoza?"
    alice "Y-yes! Heeea-♥♥ Y-yes, I'll t-take both of you!"
    kil "Would you like that you well-fucked piece-of-shit?"
    alice "Ghh, hhnnaaaa-♥ Yeeeehhhss-♥♥"
    kil "Ha! You hear that bro? Any time you want!"
    alice "Ooohh, wwhwhhoooo-♥♥♥♥♥♥"
    kil "Anytime you want this ass is yours!"
    alice "Ghh, mhmhhh, yyeehhhss- a-aanyyy-"
    kil "Say his fucking name, bitch!"
    alice "[mcf]!"
    kil "Do you wish he was here?!"
    alice "Yeeeehhhsssh!"
    kil "Tell him!"
    alice "I w-wish eehhhyou whherrere hwwhere. I wish [mcf] was fucking my p-p-ppshhhyyy...!"
    kil "Bahaha!"
    "*Plap, plap~*"
    kil "That's right! Say my fucking king's name!"
    alice "[mcf]!"
    kil "{b}Bahahaha!{/b} There it is, let go, beautiful!"
    "*Plap, plhahp, plwwwahp~!*"
    "Content with her submission, no more prodding jeers left Ian's lip."
    alice "A-h, aahhh...!"
    "Instead he let her wallow solely in her own slutty thoughts as my brightly transmitted face peered at her from the other side of the screen."
    alice "Ghh, hheee... [mcf]..."
    "Indeed, the blinders of lust on, her hazy focus had turned toward me, leaving me to wonder again just what kind of expression I was making."
    alice "Oh, o-oh... ahh... hhaa...♥ G-give me y-our- cohhhohk♥"
    "In one breath, she seemed keenly aware of my voyeurism, basking in the twisted dynamic."
    "{b}*PLAP, PLAP, PLAP!*{/b}"
    scene w3_4319 with flash
    alice "Ahh, hhhn-♥ Mmmh, I-Ian-! Dehhs- destttroyy meee...!"
    "In another breath, it was like I vanished before her eyes, her mind off at a distant destination, aware of nothing other than my friend turning her into a cock sleeve."
    kil "That's right, lose it!"
    scene alice_ir_dog3_a with dissolve
    show alice_ir_dog3 with dissolve
    alice "Ian, [mcf]! Ian, [mcf]! Gahh, hheyyy...♥"
    "No matter how she looked at me, I watched her oscillating expressions with great interest, marveling at how Ian had worn down her sense of propriety."
    alice "Ian[mcf]Ian[mcf]Ian[mcf]Ian[mcf]Ian[mcf]Ian[mcf]Ian[mcf]Ian[mcf]...!"
    "*{i}Plap, plap, plap!*{/i}"
    alice "Gyyahh, hhhaa- hhhggg-"
    "Her brain was scrambled."
    scene w3_4319 with flash
    kil "Lose it, you shameless bitch!"
    alice "Gehhh- ♥ Eyywwahh-♥ Hnngg~"
    "Was she always like this? Did Ian mold her to his liking?"
    alice "Ahhh, mhmhhh-"
    scene alice_ir_dog3_a with dissolve
    show alice_ir_dog3 with dissolve
    alice "Gehhh- ♥ Eyywwahh-♥ Hnngg~"
    "I myself stopped caring about anything other than the scene in front of me, impressed with my friend's conquest."
    kil "Where you want to see it, bro? Viewer's choice."
    mc "What...?"
    "Ian asked me a question, pulling me away from the reverie of Alice's face twisting in pleasure."
    kil "Where do you want me to blow my load? I'm almost-!"
    alice "H-haaah...♥"
    kil "Ah, my sweet lovely Alice~ don't you DARE drop the camera! G-gahhh-"
    "Where did I want to see him make a mess...?"
    kil "Seriously dude, a-answer! I'm about to-"

    menu:
        "You want to see Alice's expression when he packs her full of cum(Dialogue/Render Chnages only).":
            mc "{b}Inside.{/b}"
            "It was simple. I was caught up following every contour of Alice's face and I wanted to see this to its natural conclusion."
            kil "You got it!"
            "I wanted to see the expression she would make as her womb was drenched in the jizz of someone half her age."
            kil "Here I-- aaahhhh-♥"
            stop ambient
            stop music
            play sound "sound effects/spurt.wav"
            scene w3_4320 with flash
            alice "Gh, hhhnk-♥"
            "My friend rolled his hips forward, extending himself as deep as he could go, and letting it all out into the old woman's depths."
            play sound "sound effects/spurt.wav"
            with flash
            kil "Drink it up, bitch!"
            scene w3_4321 with dissolve
            alice "Ahh, hhaaa, mmhhhhh-♥"
            kil "Ha... man, I don't normally shoot that quick."
            mc "...I'm not taking credit for that."
            alice "Ghh, hhnngg dhhiicckk... eeeughh..."
        "You want to see her lathered with jizz(Dialogue/Render Chnages only).":

            scene w3_4322 with pixellate
            "Abruptly, an image of a younger Alice's demure countenance sprang to mind."
            scene alice_ir_dog3_a with pixellate
            show alice_ir_dog3 with dissolve
            mc "Do it on her face!"
            "It was absurd, but I answered, momentarily delighted in having control over my friend's actions."
            kil "You got it!"
            stop ambient
            scene w3_4323 with dissolve
            alice "W-aah, ahhh...?"
            "I wanted to see the face of the mild, unassuming Alice of my past stained with cum."
            scene w3_4324 with dissolve
            kil "You know the drill! Get ready for it!"
            scene w3_4325 with dissolve
            "True to my friend's claim, she parted her mouth and dutifully offered her tongue."
            kil "Good bitch! Bon appetit--"
            stop music
            play sound "sound effects/spurt.wav"
            scene w3_4326 with flash
            kil "Gaaah-!"
            "In an instant, Alice's homely face disappeared and was replaced by a disaster."
            play sound "sound effects/spurt.wav"
            scene w3_4327 with flash
            kil "You're fucking nothing!"
            "Layer after layer of spunk plastered her face, transforming her from the woman I knew into a disgusting, pitiful creature."
            play sound "sound effects/spurt.wav"
            scene w3_4328 with flash
            kil "W-worthless... ahh..."
            "It was beautiful."
            kil "Ha... man, I don't normally shoot that quick."
            mc "...I'm not taking credit for that."

    scene w3_4329 with circlewipe
    "Ian was right. That was {i}interesting{/i}. We ended up talking for another ten minutes, once we got through the awkwardness of him coming down from his cum-high."
    "All throughout, the distant sound of Alice sucking his cock could be heard - and again, I felt an almost strange admiration that I would never admit to. Still..."
    scene black with fade
    show screen textbox2 with dissolve

    if not persistent.w3AlicePhoneSex:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3AlicePhoneSex = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

    "Eventually, sleep came."
    $ renpy.end_replay()
    m_dev "Picking this option made you miss calling one of the girls, would you like to call them now?"
    menu:
        "Yes":
            jump w3CutieCall
        "No":
            pass
    jump w3BreakfastWithIan


label w3SleeplessNight:
    scene black with fade
    "......"
    "..."
    scene w3_3779 with fade
    scene w3_3780 with dissolve
    mct "(Mmmmh, {i}crap{/i}.)"
    scene w3_3781 with dissolve
    "Sleep that night was a hard-won battle, but in time, I eventually got there."
    scene black with fade
    "Just as the sun was coming up."
    "......"
    "..."
    jump w3BreakfastWithIan

label w3BreakfastWithIan:
    play music "music/dog-park.ogg"
    scene w3_3782 with circlewipe
    vic "...what are you boys doing today?"
    kil "Playing secret agents."
    vic "Secret, huh?"
    scene w3_3783 with dissolve
    kil "I told [mcf] I'd help make sure his place isn't bugged with listening devices."
    vic "If it's something you don't want to tell me, you could just tell me you're hanging out."
    kil "Why would I keep a secret from you, Vicky?"
    scene w3_3784 with dissolve
    vic "I don't know, but it seems like [mcf] has his secrets these days."
    kil "Maybe he's just at that age?"
    scene w3_3785 with dissolve
    vic "...I'm being serious. There's something different about him that I can't put my finger on..."
    kil "Like what?"
    scene w3_3786 with dissolve
    vic "It's hard to put into words. His general demeanor has been... {i}off{/i} for the past few weeks, if that makes any sense."

    if w2ExEndingVictoria == True:
        vic "I know something's been bothering him. He doesn't usually show up out of the blue two times in just a few days to watch movies and sleep here."
    else:
        vic "I can tell something's been bothering him. He doesn't normally show up out of the blue to watch movies and sleep here."

    scene w3_3787 with dissolve
    vic "Plus, he asked me if I knew some Autumn Burns or another..."
    scene w3_3788 with dissolve
    kil "{size=-5}Byrnes...?{/size}"
    scene w3_3787 with dissolve
    vic "He didn't really explain after that. I thought it might be a director, but he was weirdly emphatic when he asked about it."
    scene w3_3786 with dissolve
    vic "It's not like I have an actual reason to be concerned, it's just a creeping feeling, but I was hoping you might know something."
    scene w3_3789 with dissolve
    kil "You've always coddled him, you know?"
    scene w3_3790 with dissolve
    vic "...excuse me? He's my son. If I were EVER overindulgent with him, I could very well be forgiven."
    scene w3_3791 with dissolve
    kil "I didn't mean that in a bad way. I'm just saying you worry too much. He's a big boy living his life and you are a..."
    scene w3_3792 with dissolve
    vic "Finish your sentence..."
    scene w3_3793 with dissolve
    kil "You are a widowed, single woman."
    scene w3_3792 with dissolve
    vic "What does that have anything to do with [mcf] acting weird?"
    scene w3_3793 with dissolve
    kil "Probably nothing, but it is {i}slightly{/i} possible that you're latching onto minor things because you want to parent him."
    scene w3_3794 with dissolve
    vic "*Scoff* This isn't an empty nest thing. He's been moved out for a few years."
    vic "Do you know how offensive that suggestion is?"
    scene w3_3795 with dissolve
    kil "You know I didn't mean anything by it. I'm just a dumbass."
    scene w3_3796 with dissolve
    vic "......"
    scene w3_3797 with dissolve
    vic "...no, you're not. Don't talk like that. You're just being honest."
    vic "You're an annoyingly astute but wonderfully sensitive kid."
    scene w3_3798 with dissolve
    kil "Yeah, right..."
    scene w3_3799 with dissolve
    vic "Afraid so, Ian. It's true."
    scene w3_3800 with dissolve
    vic "Remember when your mother was {i}strongly{/b} giving me advice on how to correct [mcf]'s behavior?"
    vic "I was so mortified and deeply embarrassed at the time... but I know it wasn't a coincidence that you just happened to spill soda all over the work she brought home."
    scene w3_3801 with dissolve
    vic "I was relieved at the change in topic, but in hindsight... you shouldn't have felt you needed to be scolded just to smooth out an uncomfortable situation between adults."
    scene w3_3802 with dissolve
    kil "I'm just clumsy."
    scene w3_3800 with dissolve
    vic "I remember when [mcf] was sick with scarlet fever the week of your class field trip to the aquarium. You were so afraid he was missing out that you called him a dozen times that day just to fill him in."
    scene w3_3801 with dissolve
    vic "Did you even get a chance to enjoy that day yourself?"
    scene w3_3802 with dissolve
    kil "I remember it being a {i}very{/i} good day."
    scene w3_3803 with dissolve
    vic "You've always picked up on specific details and gone out of your way to make someone feel better. You're not dumb... and you're probably not completely wrong, either."
    scene w3_3804 with dissolve
    kil "I was honestly running my mouth. Don't listen to me."
    scene w3_3805 with dissolve
    vic "Still, I'm not gonna give you a pass on your phrasing. \"Widowed, single woman\"...?"
    scene w3_3806 with dissolve
    kil "...you're going to rake me over the coals for this one, huh?"
    scene w3_3807 with dissolve
    vic "It's a teachable moment. You should work on the way you talk to women, Ian."
    scene w3_3806 with dissolve
    kil "...alright, fine. I'll dig myself deeper, then."
    scene w3_3807 with dissolve
    vic "This will be good."
    scene w3_3808 with dissolve
    kil "...how come you've always been single?"
    scene w3_3809 with dissolve
    vic "*Scoff* Oh {b}gooooood{/b}, now little Ian is looking down on me too. I get enough of being called a spinster from my own son."
    vic "You're really doubling down on this \"you need something to do\" thing in the worst possible way, you know that?"
    scene w3_3810 with dissolve
    kil "No, it's a genuine question. You're a beautiful woman; you've always been and you're even more now."
    scene w3_3811 with dissolve
    vic "Is it an anomaly that needs to be understood? You're not suggesting there's something wrong with a \"beautiful\" woman if she doesn't have a man, are you dear?"
    scene w3_3812 with dissolve
    kil "They're usually crazy, yeah, but I know for a fact that you're not. In fact, you're astonishingly personable and kind. So, I was just wondering... what's been the deal with that?"
    scene w3_3813 with dissolve
    vic "......"
    kil "...teachable moment, remember?"
    scene w3_3814 with dissolve
    vic "So this is how you do it? One part feigned stupidity, one part charm? Like a chauvinistic puppy dog?"
    scene w3_3813 with dissolve
    kil "Uh, no- I mean, uhh, well--"
    scene w3_3815 with dissolve
    vic "Pfffh, mahahaa-! Don't hurt yourself trying to worm out of this one. I'll answer your question."
    scene w3_3816 with dissolve
    vic "If we're talking about romance, I've never felt the need after [mcf]'s father."
    vic "I've had my responsibilities as a parent, my work, my interests, and other distractions that kept me occupied and happy."
    scene w3_3817 with dissolve
    kil "Yep, I'm an idiot! That's a great answer! I'm glad I could finish this conversation with all my fingers--"
    scene w3_3818 with dissolve
    vic "If we're talking about physical needs, then as you've said, I am a beautiful woman and it's very simple to-"
    kil "We can leave it at that, please."
    scene w3_3819 with dissolve
    kil "...so [mcf]'s still not up, huh?"
    stop music fadeout 3.0
    scene w3_3820 with dissolve
    "......"
    scene w3_3821 with dissolve
    vic "...Ian? I already know the answer, so don't try to lie."
    scene w3_3822 with dissolve
    kil "I don't ever lie to you if I can help it..."
    scene w3_3821 with dissolve
    vic "I know, but you also know I can tell when you're lying, right? I can read you like a book."
    scene w3_3823 with dissolve
    kil "I need to go to the bathroom."
    vic "You WOULD tell me if [mcf] gets himself in a bad spot, wouldn't you?"
    scene w3_3824 with dissolve
    "......"
    scene w3_3825 with dissolve
    "..."
    play music "music/dog-park.ogg"
    scene w3_3826 with dissolve
    kil "You {b}absolutely{/b} know I would."
    scene w3_3827 with dissolve
    kil "...not that I would ever let him get into a bad spot to begin with. If anything, it'd be the other way around."
    scene w3_3828 with dissolve
    vic "Thank you, Ian."
    scene w3_3829 with dissolve
    mc "*Yawwwwwwwn* When you said you'd drop by in the morning, I didn't think you meant this early..."
    scene w3_3830 with dissolve
    kil "It's not {i}that{/i} early. You just slept in late, lazy ass."
    scene w3_3831 with dissolve

    if w3HanaCutieCall == True:
        "All in all, despite the late start, it wasn't a bad night's sleep. I had Ian and Hana to thank for that."
    elif w3MinaCutieCall == True:
        "All in all, despite the late start, it wasn't a bad night's sleep. I had Ian and Mina to thank for that."
    else:
        mct "(You know I didn't get much sleep last night, asshole...)"

    scene w3_3832 with dissolve
    mc "How are you not hungover? You were blasted last night."
    kil "I wasn't that drunk. It was a mild night."
    "The pair looked like they were having a fairly serious conversation. I can only imagine what..."
    scene w3_3833 with dissolve
    mc "Hey, Mom. Sleep well?"
    vic "Good morning, hun. I slept pretty good. How about you?"
    mc "Not too great. I think I'm too used to the memory foam mattress at the apartment. What's up?"
    scene w3_3834 with dissolve
    vic "I've just been talking to Ian. What are you two getting up to today?"
    scene w3_3835 with dissolve
    "I cast my friend a surreptitious glance as if I had ANY hope of beating this well-worn tactic and discerning what he had told her."
    scene w3_3836 with dissolve
    vic "He said you were playing secret agent and hunting for bugs in your apartment."
    scene w3_3838 with dissolve
    mc "He's helping me put up a security camera."
    scene w3_3837 with dissolve
    "Half-truths. I really was planning to put up a camera today."
    scene w3_3839 with dissolve
    mc "A homeless guy wandered into the building a few nights ago and spooked everyone on my floor with a disturbance."
    scene w3_3840 with dissolve
    vic "Aw, poor man. Was he okay?"
    mc "Was he okay...?"
    scene w3_3841 with dissolve
    "......"
    "..."
    scene w3_3842 with dissolve
    mc "He ended up leaving, but it got me thinking about security. So yeah... thought it was better for Ian to climb up a ladder than me, you know?"
    scene w3_3843 with dissolve
    kil "Oh, before I break my neck, there's another thing. I'm scheduled for a haircut. You don't mind coming with me, right?"
    scene w3_3844 with dissolve
    mc "Why didn't you just come after your appointment?"
    scene w3_3845 with dissolve
    kil "I woke up, had some time to kill, and thought my best friend and I would make a morning of it. Hell, wanna get a mani-pedi while we're at it?"
    scene w3_3844 with dissolve
    mc "I'll pass on anyone touching my feet, but actually..."
    scene w3_3846 with dissolve
    mc "I could use a trim. Do they take walk-ins?"
    kil "I know one of the girls. She'll fit you in."
    scene w3_3847 with dissolve
    "Sure... a haircut, sweep for bugs, install a security camera."
    "I've got a veritable to-do list ahead of me."
    mc "When's your appointment?"
    scene w3_3848 with dissolve
    vic "Hmmm..."
    mc "...what is it?"
    scene w3_3849 with dissolve
    vic "You should change your style."
    mc "What's wrong with my hair?"
    scene w3_3850 with dissolve
    kil "You're twenty-two and look like an egghead."
    vic "No, you don't. You look handsome, but I realized I haven't seen your forehead in years."
    scene w3_3851 with dissolve
    mc "You've seen my forehead. I brushed my hair back last night while we watched {i}Nothing Underneath{/i}."
    vic "I meant in the light of day, honey."
    mc "...wait, I look like an egghead?"
    scene w3_3852 with dissolve
    kil "Ha! Got him!"
    mc "Nah, uh uh. I'm just getting a trim."
    kil "You won't after you let that shit fester an hour, egghead."
    scene w3_3853 with dissolve
    vic "Awww, don't listen to him. I like your head as the perfect oval it is."
    stop music fadeout 3.0
    scene black with fade
    mc "Don't think I won't go bald just to spite you two."
    play sound "sound effects/car.wav"
    "......"
    "..."
    play music "music/scissor-vision.ogg"
    scene w3_3854 with cmet
    kil "So, I thought some more about the Darius thing."
    "As soon as we got to his car, Ian immediately got on topic, looking rather serious compared to this morning's congeniality."
    mc "Let me hear it."
    scene w3_3855 with dissolve
    kil "I've been thinking Darius isn't the slickest dude. He would've left some kind of a paper trail going wherever he fucked off to."
    mc "Sure, but that's not something you or I could look into, Columbo."
    scene w3_3856 with dissolve
    kil "What about hiring an investigator to do it?"
    scene w3_3857 with dissolve
    mc "I thought you said you thought about it."
    scene w3_3858 with dissolve
    kil "I did! I know it's a bit nuclear to debunk some weird thing Kathy told you, but it would be the most conclusive way of getting peace of mind."
    scene w3_3859 with dissolve
    mc "I think hiring an independent third party to investigate a former employee of the prostitution ring that we're both members of is, to put it mildly, a bad idea."
    "......"
    scene w3_3864 with dissolve
    "..."
    scene w3_3860 with dissolve
    kil "Ah, shit. Yeah, that's a {i}real{/i} dumb idea! That's what I get for trying to cook up something while mid-nut."
    scene w3_3863 with dissolve
    mc "Well, your heart is in the right place, and most importantly, you raised a good point."
    scene w3_3862 with dissolve
    kil "Did I?"
    scene w3_3861 with dissolve
    mc "If he really did just split, he didn't just drop off the face of the earth. So it {i}is{/i} something that can be looked into and possibly confirmed."
    scene w3_3860 with dissolve
    kil "I guess the question is... how bad do we really want to know?"
    scene w3_3863 with dissolve
    mc "...you think it's a bad idea?"
    "I could think of a few reasons, but I wanted to hear Ian's thoughts."
    scene w3_3865 with dissolve
    kil "I'm only saying this because I know he's fine, but... it might be better just not knowing, yeah?"
    scene w3_3866 with dissolve
    mc "Do you mean better in the sense that we wouldn't be burdened with the knowledge?"
    scene w3_3867 with dissolve
    kil "For the record, I'm all for figuring it out. I'd like to know where the hell the guy went and I know clearing it up will give my best friend some peace of mind."
    scene w3_3868 with dissolve
    mc "........."
    scene w3_3869 with dissolve
    mc "......"
    scene w3_3870 with dissolve
    mc "...hypothetically speaking, what would you do if you learned something bad happened to Darius? Would it change anything?"
    "I was posing that question to myself as much as Ian."
    scene w3_3871 with dissolve
    kil "I mean, fuck man. I wouldn't be able to look August or the old woman in the eyes."
    mc "That's it...?"
    scene w3_3872 with dissolve
    kil "Are you asking me if I would quit the club?"
    mc "{i}Would{/i} you quit the club?"
    scene w3_3873 with dissolve
    kil "...prostitution is one thing, but Darius is my friend. So, I m-mean... y-yes?"
    kil "If I'm getting real for a second, I don't think I could fucking take it. I'm just a spoiled-- ahh..."
    "Ian's moral clarity was surprising to me, because..."
    scene w3_3874 with dissolve
    kil "What about you?"
    "I was of two minds about it."
    scene w3_3875 with dissolve
    "One: if a guy, who I didn't even know, got himself into trouble by blackmailing a prostitution ring orbiting the influential and powerful, then he had effectively chosen to step in front of a bus."
    "The other, like Ian... {i}holy shit{/i}."
    mc "I... uh..."
    "I, too, was a dumb, sheltered asshole. My brain might know what kind of place it is, but I hadn't seen the true weight of it."
    scene w3_3876 with dissolve
    kil "Yeeeeah... that's why I think it's a damn good question to ask ourselves before we continue down this road."
    "He was right. Sometimes it was better not knowing, but my inner voice wasn't easily quelled by convenience."
    kil "...again I'm all for it, but there {i}is{/i} a non-zero possibility... and this is the kind of tidbit that once you learn, you can't play hot potato with it. It's in your lap and you got to fucking deal with it."
    scene w3_3877 with dissolve
    kil "How about we let the \"looking into Darius\" thing sit a while? Today, let's take care of your surroundings and get you some {i}immediate{/i} peace of mind. You know, put up that camera and make sure no one is listening to you jerk off?"
    mc "Yeah... one day at a time."
    "My inner voice wasn't easily quelled by convenience, but it also wouldn't be the first time I ignored that nagging bitch."
    "There was no need to be hasty before I could adequately take stock and compartmentalize conflicting feelings."
    scene w3_3878 with dissolve
    mc "Thanks again, Ian."
    kil "Not even a thing between us, bro. Now..."
    kil "...let's go get a haircut, egghead."
    stop music fadeout 3.0
    scene black with fade
    mct "(I'm just getting a trim.)"
    play music "music/hotshot.ogg"
    scene w3_3879 with blinds
    kil "Thanks for squeezing him in, babe."
    amber "Yeah, heh... no problem, I had some time before your appointment."
    kil "You're the best."
    amber "Stop it, I'm at work."
    kil "Sure, sure, sure..."
    scene w3_3880 with wipeleft
    amber "So, uhh... we've..."
    scene w3_3881 with dissolve
    mc "Yep. We've met before, but I'm surprised you remember me."
    kil "Eh? You two have met?"
    scene w3_3882 with dissolve
    amber "Hehehe, I wasn't that-- ah, ha... {i}yeah.{/i}"
    scene w3_3883 with dissolve
    amber "Sorry again about scaring you that night."
    scene w3_3884 with dissolve
    mc "I wasn't {i}scared{/i}."
    "When I haphazardly agreed to a haircut, I didn't imagine the person cutting my hair would be..."
    scene w3_3883 with dissolve
    amber "Oh, yeah, of course not. I just mean--"
    scene w3_3971 with pixellate
    "One of Ian's recurring flings."
    scene w3_3885 with pixellate
    amber "I just mean {i}sorry.{/i}"
    scene w3_3886 with dissolve
    mc "Wasn't your fault. It's that jackass' behind us."
    scene w3_3887 with dissolve
    kil "Seriously? When did you two meet? I think I would remember that..."
    scene w3_3888 with dissolve
    amber "How do you not? Were you seriously that hosed--"
    scene w3_3970 with pixellate
    "That wasn't the only time either, but she doesn't know about that..."
    scene w3_3889 with pixellate
    kil "Ah, whatever. It's not important. Just do your job."
    scene w3_3890 with dissolve
    amber "My job? I'm cutting your hair for free!"
    scene w3_3891 with dissolve
    amber "......"
    scene w3_3892 with dissolve
    amber "*sigh* ...how do you want your hair, sweetie?"
    mc "I'm just here to get a..."
    scene w3_3893 with dissolve
    mc "...actually, I want to try something new, but I'm not sure what would look good. What's your expert opinion?"
    amber "Hmm..."
    scene w3_3894 with dissolve
    amber "May I...?"
    mc "Go ahead."
    scene w3_3895 with dissolve
    amber "I wouldn't really go any shorter than this, so how about I clean up your sides and maybe try styling it differently?"
    amber "That way, if you don't like it, we won't have done anything too drastic."
    scene w3_3896 with dissolve
    mc "Whatever you think is best."
    scene w3_3897 with dissolve
    amber "You know, people who say that are usually either the worst or best customers. Which one are you?"
    scene w3_3898 with dissolve
    mc "The kind that appreciates you for making time for me last minute."
    scene w3_3899 with dissolve
    amber "That's a good answer."
    scene w3_3900 with dissolve
    amber "Don't just lurk behind me, Ian. Go sit down."
    scene black with fade
    "......"
    "..."
    "Two haircuts later, Ian and I..."
    kil "Ah, look here!"
    mc "What are you doing?"
    kil "Getting a picture to send to Vicky."
    mc "Why? She'll just see it later anyway..."
    stop music
    play sound "sound effects/camera-phone-shutter.wav"
    kil "There, got it! You were making a stupid face though."
    mc "What? Let me see it..."
    kil "This is going on ALL my accounts!"
    mc "Eh, don't post it without my--"
    scene w3_3901 with w20
    kil "Man, we look damn good. We should go out tonight."
    mc "I'll pass."
    kil "I knew you'd say that because {i}obviously{/i} we need to get you some new duds first."
    mc "I'll pass."
    scene black with fade
    kil "I knew you'd say that, too, party pooper."
    scene w3_3902 with circlewipe
    play music "music/sneaky-snitch.ogg"
    kil "We should've sprung for the more expensive ones. I would have paid for them."
    mc "I'm not trying to film the wrinkles of an intruder's asshole here, Ian. Should anyone poke around here while I'm not gone, I just want to be alerted."
    scene w3_3903 with dissolve
    mc "I prefer my overreactions to be as inexpensive as possible."
    kil "Okay, well, setting up the cameras is simple enough. But do you have any idea how to search for microphones?"
    scene w3_3904 with dissolve
    mc "I did some research. I bought an RF detector when we got the cameras, but I want to be more thorough than that. I'm glad you're here... this is a big place."
    scene w3_3905 with dissolve
    kil "You mean there's not an app that just {i}beep beeps?{/i}"
    scene w3_3906 with dissolve
    mc "I'm leaving no room for doubt."
    scene w3_3907 with dissolve
    kil "...alright, just uh... you're buying me pizza later."
    scene w3_3908 with dissolve
    mc "Eh? You volunteered."
    scene w3_3909 with dissolve
    kil "You cheap ass."
    scene w3_3910 with dissolve
    mc "Cheap? I was the only one of us who paid for his haircut today."
    kil "What are you talking about? I pay Amber in my own way."
    scene w3_3911 with w24
    "So, we did our {i}detecting.{/i}."
    "We shut off all the appliances and listened for any electrical hums. We looked for errant wires and checked the light fixtures."
    scene w3_3912 with wiperight
    "We wandered around, flashlights in tow, searching for reflections bouncing back off tiny lenses."
    scene black with fade
    "An hour and a half later, I felt relatively sure of one thing - {i}no one was spying on my dorky ass.{/i}"
    scene w3_3913 with fade
    kil "So, peace of mind achieved?"
    scene w3_3914 with dissolve
    mc "I feel a little better. Thanks for humoring me."
    scene w3_3915 with dissolve
    kil "I wasn't humoring you. You had cause for concern."
    scene w3_3914 with dissolve
    mc "I appreciate it even more, then."
    scene w3_3916 with dissolve
    "......"
    "..."
    scene w3_3914 with dissolve
    mc "Tell me more about Darius - and don't just call him a flaky asshole like everyone else. I'd like to hear something good."
    scene w3_3917 with dissolve
    kil "...something good? He... he had plenty of good things about him."
    scene w3_3918 with dissolve
    mc "Tell me some."
    scene w3_3919 with dissolve
    kil "Well, for example, he was hilarious. Everyone at the club loved him because he could make anyone laugh without fail."
    scene w3_3920 with dissolve
    mc "And what else?"
    "For some reason, I thought getting a fuller picture of what kind of guy my predecessor was, was a good idea."
    scene w3_3921 with pixellate
    kil "He always said what was on his mind and never bullshitted. Of course, it rarely did him any favors, but he'd outright tell you if he thought something was boring, stupid, or unfair."
    kil "The last one is the good one, the rest made him pretty annoying, but at least for the people in front of his face, he looked out for them."
    scene w3_3922 with pixellate
    kil "Basically, he was the kind of guy who wore his heart on his sleeve. He'd be in love with a different girl every month and I think the idiot really meant it."
    kil "Chasing a girl brought him over from Hawaii in the first place."
    scene w3_3923 with pixellate
    mc "Oh yeah, you mentioned a week ago that his family has a business up there."
    scene w3_3924 with dissolve
    kil "That's something he and I had in common. He was happy to be away from all that crap."
    scene w3_3925 with dissolve
    "......"
    "..."
    scene w3_3927 with dissolve
    kil "So, uh... does any of this make you want to find out where he went {i}more{/i} or does it encourage you to just let sleeping dogs lie?"
    scene w3_3926 with dissolve
    mc "I don't know. Have you ever thought of getting in contact with his family?"
    scene w3_3925 with dissolve
    kil "There was no reason to before now. I'd have to track them down, but that shouldn't be difficult. Should I?"
    scene w3_3923 with dissolve
    mc "On the one hand, it might immediately clear everything up. On the other, if they haven't heard from him, it would just make me wonder even harder..."
    scene w3_3923 with dissolve
    mc "Not sure what I'll do with it, but try to find it, will ya?"
    scene w3_3924 with dissolve
    kil "Yeah, sure thing. I'll look into it tonight. I think he mentioned the business name in an old text or something... They run a big textile plant."
    scene w3_3926 with dissolve
    mc "Thanks..."
    scene w3_3928 with dissolve
    "......"
    "..."
    scene w3_3929 with dissolve
    mc "I'm tired."
    scene w3_3930 with dissolve
    kil "Rest your eyes."
    mc "I think I just might..."
    kil "While you do that, can I take a shower? Feelin' a bit itchy after my trim."
    scene w3_3931 with dissolve
    mc "Mi casa es tu casa. Just don't drown, amigo."
    kil "I'll try, but keep an ear out, just in case."
    mct "(Heh. Since when does he ask...?)"
    stop music fadeout 3.0
    scene black with fade
    "......"
    "..."
    play music "music/no7-alone-with-my-thoughts.ogg"
    scene w3_3932 with fade
    "As my mind gradually let go of its thoughts, I felt distant."
    "Was I in a movie? The question of hunting down a missing man's parents felt preposterous, but the underlying sense of anxiety that pervaded me since yesterday was, oddly enough, at an all-time low."
    "Something in me intrinsically understood that - Darius aside - this was a needed reality check, perhaps in the way that the home-invading old prick intended. It offered a chance to put things in order for myself and have a securer grasp on the future."
    scene w3_3933 with dissolve
    mct "(...bottom line, do I like how my life is going?)"
    "These last few weeks have been..."
    hide screen textbox2 with dissolve

    menu:
        "Interesting(Dialogue/Render Chnages only).":
            show screen textbox2 with dissolve
            "It's been a lot of things, but it hasn't been boring."
            "Money, women, and now even a little dash of intrigue..."
        "Confusing(Dialogue/Render Chnages only).":

            show screen textbox2 with dissolve
            "No two ways around it. I've felt at odds with myself."
            mct "(Life used to be a lot simpler. I certainly never worried about {i}this{/i}.)"
            "Well, it's not like I plan on blackmailing my bosses, but still..."

    scene w3_3934 with dissolve
    mc "Mmmhhh..."
    "As my mind further let go of its thoughts, an image snaked into my brain."

    if w3PromoShockFullSadism == True:
        hide screen textbox2 with dissolve
        scene w3_3968 with pixellate
        $ renpy.pause(1, hard=True)
        scene w3_3967 with pixellate
        $ renpy.pause(1, hard=True)
        scene w3_3969 with pixellate
        show screen textbox2 with dissolve
        "That was fun, wasn't it?"

    elif w3FeliciaMeanShock == True:
        scene w3_3969 with pixellate
        mc "That happened yesterday, huh?"

    elif w3RosalindMeanShock == True:
        scene w3_3968 with pixellate
        mc "That happened yesterday, huh?"
    elif w3VeronicaMeanShock == True:
        scene w3_3967 with pixellate
        mc "That happened yesterday, huh?"
    else:

        scene w3_5392 with pixellate
        mc "That happened yesterday, huh?"

    "........."
    scene w3_3934 with dissolve
    "......"
    scene w3_3935 with dissolve
    mct "(...I should check on the girls.)"
    scene w3_3936 with fade
    hide screen textbox2 with dissolve

    menu w3CarnationCall:
        "Call Rosalind(w3CarnationCallRosalind = True)." if w3CarnationCallRosalind == False:
            $ w3CarnationCallRosalind = True

            play ambient "sound effects/ringing-outbound.mp3"

            if w3CarnationCallFelicia == True and w3CarnationCallVeronica == True:
                scene w3_3937 with dissolve
                "Now, last but not least, let's give Rosie a call..."
                "It rung."
                "It rung and rung and rung, but..."
                stop ambient
                play sound "sound effects/phonemenu.wav"
                "Nothing."
                scene w3_3936 with dissolve
                "I should try again."
                pass

            elif w3CarnationCallFelicia == False and w3CarnationCallVeronica == False:
                scene w3_3937 with dissolve
                "I decided to start with Rosalind."
                "It rung."
                "It rung and rung and rung, but..."
                stop ambient
                play sound "sound effects/phonemenu.wav"
                "Nothing."
                scene w3_3936 with dissolve
                mct "(I'll try again after the others.)"
                jump w3CarnationCall
            else:
                scene w3_3937 with dissolve
                "Next, I decided to give Rosalind a call."
                "It rung."
                "It rung and rung and rung, but..."
                stop ambient
                play sound "sound effects/phonemenu.wav"
                "Nothing."
                scene w3_3936 with dissolve
                mct "(Hmm... I'll try again after the others.)"
                jump w3CarnationCall

        "Call Felicia(w3CarnationCallFelicia = True)." if w3CarnationCallFelicia == False:
            $ w3CarnationCallFelicia = True

            play ambient "sound effects/ringing-outbound.mp3"

            if w3CarnationCallRosalind == True  and w3CarnationCallVeronica == True:
                scene w3_3937 with dissolve
                "Okay, let's try Felicia now."
                "*Ring, ring...*"
                mct "Hmmm..."
                "*Ring, ring, ring~*"
                mct "(Is she not going to pick up eith--)"
            elif w3CarnationCallRosalind == False and w3CarnationCallVeronica == False:
                scene w3_3937 with dissolve
                "I decided to start with the bombastic blonde herself."
                "*Ring, ring...*"
                "The call dragged on."
                "*Ring, ring, ring~*"
                "...and just when I thought it would go to voicemail--"
            elif w3CarnationCallRosalind == True and w3CarnationCallVeronica == False:
                scene w3_3937 with dissolve
                "Okay, let's try Veronica next."
                "*Ring, ring...*"
                mct "Hmmm..."
                "*Ring, ring, ring~*"
                mct "(Is she not going to pick up eith--)"
            else:
                scene w3_3937 with dissolve
                "Okay, let's try Felicia next."
                "*Ring, ring....*"
                "The call dragged on."
                "Ring, ring, ring~*"
                "...and just when I thought it would go to voicemail--"

            stop ambient
            play sound "sound effects/phonemenu.wav"
            scene w3_3939 with w21
            fel "Hello?"
            scene w3_3938 with dissolve
            "Felicia answered in a not-too-lively, flat tone."
            mc "Hey... it's [mcf]."
            scene w3_3939 with dissolve
            fel "I know who it is, [mcf]."
            scene w3_3938 with dissolve
            mc "I'm calling to see how you were feeling after yesterday."
            scene w3_3939 with dissolve
            fel "That's very kind of you."
            scene w3_3938 with dissolve
            mc "Are you okay? You sound a bit... off."
            scene w3_3939 with dissolve
            fel "I'm fine."
            scene w3_3940 with dissolve
            "Short, to-the-point answers."
            mc "...Just fine? It was... {i}pretty rough{/i} yesterday, huh?"
            scene w3_3941 with dissolve
            fel "The wellness check is unnecessary. Check-in with one of the other girls."
            hide screen textbox2 with dissolve

            menu:
                "{color=#FF1493}[[Sugar Baby]{/color} You two are a little more than that."(chg=["felicia_up"]) if feliciaSugarBaby == True:
                    $ Felicia_Affection +=1
                    scene w3_3943 with dissolve
                    mc "Oh, come on... don't be like that, baby. We're not just business, are we?"
                    scene w3_3944 with dissolve
                    fel "Ha! Ah...? That's cute. Trying it on for size?"

                    if hanaGF == True:
                        mct "(I wonder if Hana would consider this part of my club duties...)"

                    scene w3_3942 with dissolve
                    mc "Give me some credit. I'm calling because I'm worried and I know you didn't have as much fun as you usually do yesterday."
                "You're calling as her friend."(chg=["felicia_up"]):

                    $ Felicia_Affection +=1
                    scene w3_3943 with dissolve
                    mc "I remember us being on more friendly terms than that. We get along, don't we?"
                    mc "Seriously, how are you feeling? I know yesterday wasn't exactly your speed."
                "Be that as you may, you're talking now.":

                    scene w3_3942 with dissolve
                    mc "I'm talking to you, Felicia. It was pretty rough yesterday, huh?"


            if w3FeliciaMeanShock == True:
                scene w3_3941 with dissolve
                fel "...and who made it extra rough for me yesterday?"
                scene w3_3945 with dissolve
                mc "Did I take it too far?"
                scene w3_3947 with dissolve
                fel "Yeah, you kinda did, [mcf]. You seemed to really-- ah..."
                scene w3_3948 with dissolve
                "Felicia stopped herself, mid-thought and let the implication stand on its own."
                mc "...but did I do anything wrong?"
                scene w3_3946 with dissolve
                fel "...*sigh* That's not... I know that's the nature of the game, but you showed your teeth."
                scene w3_3945 with dissolve

                menu:
                    "Apologize(Dialogue/Render Chnages only).":
                        mc "Sorry. I got lost in the moment. You know what that's like, right?"
                        scene w3_3946 with dissolve
                        fel "You pushed it pretty far."
                        scene w3_3945 with dissolve
                        mc "I know, I know... and I apologize."
                        scene w3_3947 with dissolve
                        fel "I wasn't asking for an apology. Apologizing means you'll never do it again and we both know you need to do your job."
                        scene w3_3948 with dissolve
                        mc "...you're upset, but you don't want me to apologize?"
                        scene w3_3947 with dissolve
                        fel "Yeah, sometimes you get miffed, even when you know the circumstances can't be helped. I guess I was just surprised at how enthusiastic you got?"
                        scene w3_3946 with dissolve
                        fel "*sigh* ...but, like you said, I know what getting lost in the moment is like."
                        scene w3_3945 with dissolve
                        mc "Well, if I can't apologize, what can I do to make it up to you?"

                        if feliciaFlag == True:
                            scene w3_3949 with dissolve
                            fel "Hmmm... I don't know if you can."
                            scene w3_3951 with dissolve
                            mc "I'll do what I can."
                            scene w3_3949 with dissolve
                            fel "That'll be your homework then. Think about it {i}real hard{/i} and put all your contrition behind showing me a good time, alright?"

                            if hanaGF == True:
                                "There wasn't any harm in going with her to the exhibition tomorrow night, but Hana once again popped into my head."
                                "Even if I could justify that it was under the purview of keeping my charge happy, getting physical with Felicia went against the spirit of our \"outside of the club\" agreement."
                                mct "(Hana... I promised her something so small, but something so difficult. Not that she'd ever find out, but...)"

                                if feliciaSugarBaby == True:
                                    scene w3_3972 with pixellate
                                    mct "(And certainly, this whole absurd sugar baby arrangement went beyond the pale.)"
                                    "Not that she'd ever find out, but why make that promise in the first place, then?"
                                    fel "Think you can do that for me, [mcf]?"
                                    "Well, the arrangement was always tentative. We can hang out tomorrow and I can just be frank with her. Felicia would respect that."

                                    if rosalindFelSolution == True:
                                        mct "(...that's the least I can do, considering she footed the bill for Rosalind's loan shark problem.)"
                                    else:
                                        "...not that she'd ever find out, but why make that promise in the first place, then?"
                                        fel "Think you can do that for me, [mcf]?"
                                        "Well, we can hang out tomorrow and I can just be frank with her. Felicia would respect that."

                                scene w3_3950 with pixellate
                                mc "We'll have a great time, Felicia."
                                scene w3_3949 with dissolve
                                fel "Good!"
                            else:

                                scene w3_3950 with dissolve
                                mc "You'll have me at my most contrite, beautiful."
                                scene w3_3949 with dissolve
                                fel "Good!"
                        else:

                            scene w3_3949 with dissolve
                            fel "There's nothing to make up; I'll be over it in a day. I'm not stupid, you know?"
                            fel "I signed up for this."
                            scene w3_3951 with dissolve
                            mc "You could at least let me buy you lunch sometime."
                            scene w3_3949 with dissolve
                            fel "...is that a joke?"
                            scene w3_3950 with dissolve
                            mc "Yeah, that's a joke."
                            scene w3_3949 with dissolve
                            fel "Hmpfh..."
                    "Call her on her bullshit(Dialogue/Render Chnages only).":


                        mc "That's a load of crap, and you know it."
                        scene w3_3952 with dissolve
                        fel "Excuse me? What is?"
                        scene w3_3953 with dissolve
                        "Felicia's voice hit a {i}distinct{/i} high note, suddenly switching to an entitled housewife voice that befitted her station."
                        scene w3_3952 with dissolve
                        fel "What's a load of crap, [mcf]? Tell me."
                        scene w3_3953 with dissolve
                        "Yeah... she wasn't in a good mood today and I was poking the bear."
                        mc "You tell me. You shouldn't step in shit if you don't like the smell. Did I do anything wrong yesterday?"
                        scene w3_3952 with dissolve
                        fel "You zapped me double the number of times as the other girls!"
                        scene w3_3953 with dissolve
                        mc "So what? Are you going to pout about it like a spoiled little girl?"
                        scene w3_3954 with dissolve
                        "I didn't quite understand why I felt so antagonistic, but..."
                        mc "We're both where we chose to be, on our own terms, trying to squeeze as much fun as possible from the situation. Isn't that how you live your life?"
                        scene w3_3955 with dissolve
                        fel "Holy shit, I was just a little surprised, okay? I'm just feeling a bit... {i}{b}blah{/b}{/i} today."
                        fel "Let a bitch vent, will 'ya?"
                        scene w3_3956 with dissolve
                        mc "Don't run away from it, Felicia. Yesterday wasn't your speed, so you tried to blame me for it, but I KNOW you're not the type of person who lives like that."
                        scene w3_3949 with dissolve
                        fel "*sigh* No, I'm not..."
                        scene w3_3950 with dissolve
                        mc "You're better than that."

                        if feliciaFlag == True:
                            scene w3_3951 with dissolve
                            mc "It's one of the things I like best about you."
                            scene w3_3949 with dissolve
                            fel "Pssh, yeeeeah, sure... all you like is that I'm a pair of tanned legs leading to a set of holes."

                            menu:
                                "Agree with her(Dialogue/Render Chnages only).":
                                    scene w3_3950 with dissolve
                                    mc "You do use 'em well."
                                    scene w3_3958 with dissolve
                                    fel "Fuck you!"
                                    scene w3_3957 with dissolve
                                    mc "What? I thought you were fishing for a compliment."
                                    scene w3_3958 with dissolve
                                    fel "Yeah, yeah, yeah... read the room, {i}asshole{/i}."
                                    scene w3_3957 with dissolve
                                    "Felicia's cute when she's mad."
                                    mc "You're also a nice stomach, a lovely pair of breasts, a beautiful face, and..."
                                    scene w3_3958 with dissolve
                                    fel "Stop! Are you trying to be funny?"
                                    scene w3_3957 with dissolve
                                    mc "Maybe..."
                                "Talk her up(Dialogue/Render Chnages only).":

                                    scene w3_3951 with dissolve
                                    mc "There's more than that. You're fun to be around and you make me think."
                                    scene w3_3958 with dissolve
                                    fel "...about what? Sex?"
                                    scene w3_3957 with dissolve
                                    mc "About the value of things."
                                    scene w3_3958 with dissolve
                                    fel "Fucking weirdo."
                                    scene w3_3957 with dissolve
                                    mc "For real. I knew you were something special the night we had dinner. You stood up for little old me, dazzled me with your talk about the hierarchy of needs, and looked good doing it."
                                    scene w3_3959 with dissolve
                                    mc "You're a total package and you know it. Don't let a little cattle prod tell you otherwise."
                                    scene w3_3960 with dissolve
                                    fel "Pfhh, oh god. Life is {i}absurd{/i}."
                                    scene w3_3959 with dissolve
                                    mc "It really is..."


                            "......"
                            scene w3_3961 with dissolve
                            fel "Are we still on for tomorrow?"
                            scene w3_3957 with dissolve
                            mc "You know it."

                            if hanaGF == True:
                                scene w3_3966 with dissolve
                                "There wasn't any harm in going with her to the exhibition tomorrow night, but Hana once again popped into my head."
                                "Even if I could justify it to myself that was under the purview of keeping my charge happy, getting physical with Felicia went against the spirit of our \"outside of the club\" agreement."
                                mct "(Hana... I promised her something so small, but something so difficult. Not that she'd ever find out, but...)"

                                if feliciaSugarBaby == True:
                                    scene w3_3941 with dissolve
                                    mct "(And certainly, this whole absurd sugar baby arrangement went beyond the pale.)"
                                    "...not that she'd ever find out, but why make that promise in the first place, then?"
                                    fel "I'm glad. I've been looking forward to it."
                                    "Well, the arrangement was always tentative. We can hang out tomorrow and I can just be frank with her. Felicia would respect that."

                                    if rosalindFelSolution == True:
                                        mct "(...that's the least I can do, considering she footed the bill for Rosalind's loan shark problem.)"
                                else:
                                    scene w3_3941 with dissolve
                                    "...not that she'd ever find out, but why make that promise in the first place, then?"
                                    fel "I'm glad. I've been looking forward to it..."
                                    "Well, we can hang out tomorrow and I can just be frank with her. Felicia would respect that."

                                scene w3_3943 with dissolve
                                mc "You and I will have a lovely time."
                                scene w3_3944 with dissolve
                                fel "There's no backing out from that."
                            else:

                                scene w3_3943 with dissolve
                                mc "I'll make it worth your time, beautiful."
                                scene w3_3944 with dissolve
                                fel "Please. I'm going to have to teach you everything, aren't I?"
                        else:

                            scene w3_3949 with dissolve
                            fel "Yeah, thanks for the pep talk, stud."
            else:
                scene w3_3946 with dissolve
                fel "It's what I signed up for. I won't pretend that was fun for me, but not everything can be."
                scene w3_3945 with dissolve
                mc "Yeah, but how are you feeling today?"
                scene w3_3947 with dissolve
                fel "How am I feeling...? What, you genuinely asking?"
                scene w3_3945 with dissolve

                menu:
                    "{color=#FF1493}[[Sugar Baby]{/color} Of course you are."(chg=["felicia_up"]) if feliciaSugarBaby == True:
                        $ Felicia_Affection +=1
                        mc "Hey! You and I stand to become pretty close, baby."

                        if hanaGF == True:
                            mct "(I wonder if Hana would consider this part of my club duties...)"

                        scene w3_3962 with dissolve
                        fel "...heh. You're the baby, [mcf]. Provisionally."
                        scene w3_3945 with dissolve
                        mc "...seriously, how are you?"
                    "You're calling as her friend."(chg=["felicia_up"]):

                        $ Felicia_Affection +=1
                        mc "Of course, I am, Felicia. I'm concerned about you."
                        scene w3_3947 with dissolve
                        fel "When have I ever given you a reason to be concerned?"
                        scene w3_3948 with dissolve
                        mc "Never, but I'm still asking. How are you?"
                    "It is why you called.":

                        mc "I wouldn't ask if I didn't want an answer."
                        scene w3_3946 with dissolve
                        fel "Sure, yeeeah..."
                        scene w3_3945 with dissolve
                        mc "How are you, Felicia? Tell me."


                scene w3_3946 with dissolve
                fel "I am...{i}blaaaaaah.{/i} Worn out? Drained? {i}Whatever.{/i}."
                scene w3_3945 with dissolve
                mc "Sounds complicated."
                scene w3_3946 with dissolve
                fel "Not really. Sometimes things rub you the wrong way, there's no sense to it, and you just got to let it wash over you."
                scene w3_3957 with dissolve
                mc "That's not true. There's always a reason. Sometimes we just don't want to expend the energy to comprehend it."
                scene w3_3958 with dissolve
                fel "It doesn't take much to comprehend you don't like to be zapped with electricity."
                scene w3_3957 with dissolve
                mc "Ha, yeeeah. Kinda a stupid thing to say, huh?"
                "I did suspect something more behind her mood than the day-past physical discomfort of the trial, but there was no value in pushing that point."
                scene w3_3961 with dissolve
                fel "By the way, I appreciate what you did when it was my turn. Kathy seemed dead set on me getting it good, but you at least made me feel part of the proceedings."
                scene w3_3959 with dissolve
                mc "I just wanted a different tempo, is all."
                scene w3_3963 with dissolve
                fel "Hmmfh..."
                mc "So you're just letting it \"wash\" over you?"
                scene w3_3962 with dissolve
                fel "It's easy to do when you got a pool in your penthouse."
                scene w3_3963 with dissolve
                mc "You sure do keep it real, Felicia."
                scene w3_3962 with dissolve
                fel "Shut up. I know how I sound."

                if feliciaFlag == True:
                    scene w3_3949 with dissolve
                    fel "You know what's going to make me feel better, though?"
                    scene w3_3950 with dissolve
                    mc "What?"
                    scene w3_3949 with dissolve
                    fel "Are we still on for our date tomorrow?"
                    scene w3_3951 with dissolve
                    mc "I wouldn't dream of letting you down."
                    scene w3_3950 with dissolve

                    if hanaGF == True:
                        "There wasn't any harm in going with her to the exhibition tomorrow night, but Hana once again popped into my head."
                        "Even if I could justify it to myself that was under the purview of keeping my charge happy, getting physical with Felicia went against the spirit of our \"outside of the club\" agreement."
                        mct "(Hana... I promised her something so small, but something so difficult. Not that she'd ever find out, but...)"

                        if feliciaSugarBaby == True:
                            scene w3_3972 with pixellate
                            mct "(And certainly, this whole absurd sugar baby arrangement went beyond the pale.)"
                            "Not that she'd ever find out, but why make that promise in the first place, then?"
                            fel "I'm happy to hear it."
                            "Well, the arrangement was always tentative. We can hang out tomorrow and I can just be frank with her. Felicia would respect that."

                            if rosalindFelSolution == True:
                                mct "(...that's the least I can do, considering she footed the bill for Rosalind's loan shark problem.)"
                            else:
                                "...not that she'd ever find out, but why make that promise in the first place, then?"
                                fel "I'm happy to hear it."
                                "Well, we can hang out tomorrow and I can just be frank with her. Felicia would respect that."
                            scene w3_3938 with pixellate
                else:

                    scene w3_3949 with dissolve
                    fel "My self-awareness is one of my best qualities."
                    scene w3_3950 with dissolve
                    mc "Are you aware of how {i}that{/i} sounds?"
                    scene w3_3949 with dissolve
                    fel "Quiet, you."
                    scene w3_3938 with dissolve



            "........."
            "......"
            "..."
            scene w3_3940 with dissolve
            "Our call was brief, but the silence was damning. There was nothing else to be said."
            scene w3_3939 with dissolve
            fel "Now that the obligatory health check is done, can I return to pre-gaming my book club meeting?"
            scene w3_3938 with dissolve
            mc "You drink at book club meetings?"
            scene w3_3939 with dissolve
            fel "You don't think we read books, do you?"
            scene w3_3938 with dissolve
            mc "Ha! Stupid me, right? Yeah, sorry to disturb you."

            if feliciaFlag == True:
                scene w3_3965 with dissolve
                fel "No, it's... no. I'm glad you called."
                scene w3_3964 with dissolve
            else:
                scene w3_3939 with dissolve
                fel "You're just doing your job."
                scene w3_3938 with dissolve

            mc "Bye, Felicia."

            if w3CarnationCallRosalind == True and w3CarnationCallVeronica == True:
                "All that is left is to try Rosalind one more time."
                play sound "sound effects/phonemenu.wav"
            else:
                scene w3_3936 with dissolve
                mct "Who's next?"
                jump w3CarnationCall


        "Call Veronica(w3CarnationCallVeronica = True)." if w3CarnationCallVeronica == False:
            $ w3CarnationCallVeronica = True

            play ambient "sound effects/ringing-outbound.mp3"

            if w3CarnationCallRosalind == True  and w3CarnationCallFelicia == True:
                scene w3_3937 with dissolve
                "Okay, let's try Veronica now."
                "*Ring, ring...*"
            elif w3CarnationCallRosalind == False and w3CarnationCallFelicia == False:
                scene w3_3937 with dissolve
                "I decided to start with Veronica."
                "*Ring, ring...*"
            elif w3CarnationCallRosalind == True and w3CarnationCallFelicia == False:
                scene w3_3937 with dissolve
                "Okay, let's try Veronica next. Hopefully, I'll have better luck."
                "*Ring, ring...*"
            else:
                scene w3_3937 with dissolve
                "Okay, let's try Veronica next."
                "*Ring, ring...*"

            stop ambient
            play sound "sound effects/phonemenu.wav"
            "Almost immediately, the ringing ceased, accompanied by a slightly too long pause that made me wonder if the call had been dropped."
            if w2ExEndingVeronica == True:
                scene w3_3973 with w27
                mc "Hey, Ronnie."
                scene w3_3937 with dissolve
                "So long that I decided to take the initiative with the salutations."
                scene w3_3976 with dissolve
                ver "...you're still insisting on that dumb nickname, huh?"
                scene w3_3974 with dissolve
                mc "It's not dumb; it's cute."
                scene w3_3976 with dissolve
                ver "So, your goal is to infantilize me?"
                scene w3_3974 with dissolve
                mc "What...? No. Why does everything have to be confrontational with you?"
                scene w3_3975 with dissolve
                ver "It's fun. So, why are you calling?"
                scene w3_3974 with dissolve
                mc "I wanted to hear how you were doing."
                scene w3_3949 with dissolve
                ver "How am I doing...?"
                scene w3_3950 with dissolve
                mc "Is that an unusual question for a friend to ask?"
                scene w3_3949 with dissolve
                ver "Uuugh, I said that, didn't I?"
                scene w3_3950 with dissolve
                mc "And don't say you don't know what got into you."
                scene w3_3949 with dissolve
                ver "You and I aren't exactly chummy enough for phone conversations."
                scene w3_3951 with dissolve
                mc "Agree to disagree. Now, I'm genuinely asking: how are you feeling today?"
            elif veronicaFriend == True:
                scene w3_3973 with w27
                mc "Hello? You there?"
                scene w3_3937 with dissolve
                "I decided to take the initiative with the greetings."
                scene w3_3975 with dissolve
                ver "...hey, [mcf]."
                scene w3_3974 with dissolve
                mc "Hey, how are you doing?"
                scene w3_3949 with dissolve
                ver "How am I doing...?"
                scene w3_3950 with dissolve
                mc "It's a commonly used phatic expression to signal the start of a conversation."
                scene w3_3949 with dissolve
                ver "You and I aren't exactly chummy enough for phone conversations."
                scene w3_3951 with dissolve
                mc "Agree to disagree. Now, I'm genuinely asking: how are you feeling today?"
            else:
                "......still, I could see the call was connected, so I waited."
                "..."
                scene w3_3976 with w27
                ver "Hey, what?"
                scene w3_3974 with dissolve
                mc "Is that how you answer all your calls?"
                scene w3_3976 with dissolve
                ver "Of course not. You're special, [mcf]."
                scene w3_3974 with dissolve
                mc "That's what my mom tells me. So, how are you doing?"
                scene w3_3949 with dissolve
                ver "How am I doing...?"
                scene w3_3950 with dissolve
                mc "It's a commonly used phatic expression to signal the start of a conversation."
                scene w3_3949 with dissolve
                ver "I know what it is."
                scene w3_3951 with dissolve
                mc "How are you feeling today? I'm genuinely asking."


            scene w3_3980 with dissolve
            ver "You're checking in on me."
            scene w3_3979 with dissolve
            mc "Of course, I am. Yesterday was rough."

            if w3VeronicaMeanShock == True:
                scene w3_3980 with dissolve
                ver "Funny of you to say, considering you stepped on me."
                scene w3_3981 with dissolve
                mc "You wouldn't forgive me if I half-assed it, would you? Besides, it was fun having my foot on your chest."
                "Why did I feel the need to be so candid in that moment...?"
                scene w3_3982 with dissolve
                ver "You're so obnoxious."

                if w2ExLosersAll == True:
                    scene w3_4109 with pixellate
                    mc "I'm just being honest, like you were when you had the girls served up to you on a slab yesterday."
                    ver "You saw that...? That was... I just got carried away because of whatever it was she gave me."
                    mc "Don't lie. You had fun doing whatever you wanted; you were happy to have the excuse."
                    ver "..."
                    "I took her silence as tacit agreement."
                    scene w3_3985 with pixellate

                elif w2ExLoserFelicia == True:
                    scene w3_4110 with pixellate
                    mc "I'm just being honest, like you were when you had Felicia served up to you yesterday."
                    ver "You saw that...? I... just followed Rosie's example."
                    mc "Don't lie. You had fun making a rich bitch hot blonde piss herself."
                    scene w3_3984 with pixellate
                    ver "...yeah, I did."
                    scene w3_3983 with dissolve
                    "I respected the fact she would readily admit it."
                    scene w3_3985 with dissolve
                else:

                    scene w3_3979 with dissolve
                    mc "I'm just being honest. It's the foundation of any productive relationship. "
                    scene w3_3980 with dissolve
                    ver "Do you see this as productive?"
                    scene w3_3979 with dissolve
                    mc "Maybe. You're working toward a goal, and I'm here to make sure you get through the finish line."
                    scene w3_3982 with dissolve
                    ver "Ah, that's so fucked up."
                    scene w3_3981 with dissolve
                    "I let a brief silence serve as an agreement."
                    scene w3_3985 with dissolve


                ver "So, you want to know how I am...? Alright... I'm..."
                scene w3_3986 with dissolve
                ver "I'm fine."
                mc "Of course you would say that."
            else:

                scene w3_3980 with dissolve
                ver "Sure, but it was educational."
                scene w3_3979 with dissolve
                mc "Is that right?"
                scene w3_3985 with dissolve
                ver "I learned a lot about myself and my competition. And ultimately... it wasn't that bad."
                mc "Of course you would say that."
                scene w3_3986 with dissolve
                ver "Don't get me wrong. It wasn't fun, but..."


            scene w3_3988 with dissolve
            ver "I'm not putting on a stiff upper lip, [mcf]. That {b}spider{/b} was a kick to the stomach, the chalice of--"
            scene w3_3987 with dissolve
            mc "{b}Fair point.{/b} So you're really not...?"
            scene w3_3989 with dissolve
            ver "Stewing in a pile of my own misery? Who do you think I am?"
            scene w3_3990 with dissolve
            "Was she talking herself up?"
            scene w3_3991 with dissolve
            ver "I absolutely am. What do you think brought me to the club?"
            scene w3_3990 with dissolve
            mc "Man, that's uh..."
            "Scratch that. She's pulling herself the other way."
            mc "That's candid of you."
            scene w3_3989 with dissolve
            ver "When have I been anything but?"
            scene w3_3990 with dissolve

            if w2ExEndingVeronica == True:
                mc "I think you hide a lot."
                scene w3_3991 with dissolve
                ver "I may have said we can be friends, but we're not that kind of friends. No need to dig too deep."
                scene w3_3990 with dissolve
                mc "I wasn't really trying to."
            elif veronicaFriend == True:
                mc "I think you hide a lot."
                scene w3_3988 with dissolve
                ver "Just cause I had a moment in the shower doesn't mean I'm an open book, string bean."
                scene w3_3987 with dissolve
                mc "I wasn't trying to pry you open or anything. It's just an observation."
            else:
                mc "Well, that elbow you gave Samson WAS pretty candid."
                scene w3_3987 with dissolve
                "...but she WAS full of shit about other stuff."

            scene w3_3941 with dissolve
            ver "Be honest, did you expect to find me weepy?"

            menu:
                "There was a possibility.":

                    if veronicaFriend == True:
                        scene w3_3978 with dissolve
                        mc "Well, like you said, it wouldn't be the first time."
                    else:
                        scene w3_3978 with dissolve
                        mc "It wouldn't be the first time."

                    scene w3_3977 with dissolve
                    ver "Everyone has days like that."
                    scene w3_3978 with dissolve
                    mc "I don't think quite like that..."
                    scene w3_3977 with dissolve
                "You're just checking in.":

                    scene w3_3942 with dissolve
                    mc "I just thought it would be good to check-in."
                    scene w3_3941 with dissolve
                    ver "You're giving all the girls a call?"
                    scene w3_3942 with dissolve
                    mc "That's right."
                    scene w3_3977 with dissolve
                    ver "Awww, I'm not special?"

            "Talking to the Amazon was exhausting."
            scene w3_3978 with dissolve
            mc "This is the most I've ever worked for a \"how are you doing\", you know?"


            if veronicaFriend == True:
                scene w3_3993 with dissolve
                ver "Because people don't talk about this kind of shit over the phone, idiot. If you want to hear someone genuinely pour their guts out, you got to do it over drinks."
                scene w3_3992 with dissolve
                mct "(Drinks, eh...?)"

                menu:
                    "{color=#FF1493}[[Friends]{/color} Invite her for drinks tonight(verobardate=True).":
                        $ w3VeroBarDate = True
                        mc "Okay, then. Let's get some drinks tonight. It'll be my treat."
                        scene w3_3994 with dissolve
                        "......"
                        "..."
                        mc "You there?"
                        scene w3_3995 with dissolve
                        ver "I wasn't fishing for an invitation."
                        scene w3_3996 with dissolve
                        mc "Well, I extended one. What do you say? Blow off some steam with me."
                        scene w3_3998 with dissolve
                        ver "I, uh..."
                        scene w3_3997 with dissolve
                        mc "You don't need to be glued to your gym 24/7, do you?"
                        scene w3_3998 with dissolve
                        ver "I, I... {i}no thanks{/i}."
                        scene w3_3996 with dissolve
                        "Damn, I thought I had her."
                        mc "You sure? We don't need to talk about anything related to the club. I promise you a good time."
                        scene w3_3995 with dissolve
                        ver "Yeah... {b}I'm sure.{/b}"
                        scene w3_3996 with dissolve
                        mc "Alright..."
                    "You don't want to go drinking with her. Let the comment pass.":

                        pass
            else:

                scene w3_3993 with dissolve
                ver "My ex-wife used to say the same."
                scene w3_3992 with dissolve
                "I think she meant that as a joke, but her delivery was so deadpan that I held back any noise that might confirm comprehension of what she said."


            scene w3_3993 with dissolve
            ver "Is there anything else you need?"
            scene w3_3992 with dissolve
            mc "Nope, I'm satisfied that it's business as usual."

            if w2ExEndingVeronica == True:
                scene w3_3937 with dissolve
                ver "Good. Talk to you later, Bones."
                scene w3_3973 with dissolve
                mc "See you, Ron--"
            else:
                scene w3_3937 with dissolve
                ver "Good. Talk to you later, [mcf]."
                scene w3_3973 with dissolve
                mc "See you, Ver--"

            play sound "sound effects/phonemenu.wav"
            scene w3_3937 with dissolve
            "That was painfully brief, but mission accomplished... I think?"
            scene w3_3936 with dissolve
            mct "(She at least seemed normal.)"

            if w3CarnationCallRosalind == True and w3CarnationCallVeronica == True:
                "All that is left is to try Rosalind one more time."
            else:
                mct "Now... who's next?"
                jump w3CarnationCall

    stop music fadeout 3.0
    play ambient "sound effects/ringing-outbound.mp3"
    scene w3_3937 with dissolve
    "Like last time, it rang."
    "It rung and rung and rung."
    "And just when I thought it would turn up the same result--"
    stop ambient
    play sound "sound effects/phonemenu.wav"
    scene w3_3941 with dissolve
    show screen textbox2 with dissolve
    "The call was connected."
    scene w3_3942 with dissolve
    mc "Hello...?"
    scene w3_3999 with dissolve
    "And, before I could finish my greeting, the call ended."
    scene w3_4000 with dissolve
    "I'll try again--"
    scene w3_3977 with dissolve
    phone "You have reached {i}Rosalind Carter{/i}, after the tone--"
    "Straight to voice mail."
    scene w3_4001 with dissolve
    mct "(That's weird...)"
    "Not picking up, that'd be one thing, but picking up and THEN turning her phone off...?"
    "Maybe it was just the kind of day I was having, but I felt a prickly suspicion that something wasn't right."
    mct "(Would it be crazy to go check on her...?)"
    scene w3_4002 with dissolve
    "......"
    "..."
    scene w3_4003 with dissolve
    mc "Killian!"
    kil "What?!"
    scene w3_4004 with dissolve
    mc "Finish your shower!"
    scene w3_4005 with CropMove(0.3, "wipeleft")
    with vpunch
    play sound "sound effects/whoosh.wav"
    kil "What's up, bro?"
    scene w3_4006 with dissolve
    mc "We should go check on Rosalind."
    scene w3_4007 with dissolve
    kil "Is something--"
    scene w3_4008 with dissolve
    "Noticing how serious I must look, Killian changed his tune."
    scene w3_4009 with dissolve
    kil "Yeah, let's go. I'll be less than a minute."
    scene black with fade
    kil "Do you know where she lives?"
    play sound "sound effects/car-door-close.wav"
    if roseFlag == True:
        mc "Yeah, I've been there."
    else:
        mc "Yeah, it was written down in her info."

label w3RosalindConfrontation:
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionrosalind06 with blinds
    $ renpy.pause(6, hard=True)
    play sound "sound effects/car-beep.wav"
    scene w3_4010 with blinds
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    "So, off we went, in a likely foolish endeavor, done for probably no good reason, prompted by something that was perhaps easily explainable."
    mct "(Hell, she might just not want to be bothered.)"
    play sound "sound effects/walk-wood.mp3"
    scene w3_4011 with cmet
    kil "Which one is it?"
    "Still, given the other day, I just wanted to be sure."
    mc "It's at the end of the hall."
    stop sound
    scene w3_4013 with fade

    if roseFlag == True:
        kil "So, you've been here before."
        scene w3_4014 with dissolve
        play sound "sound effects/door-bell.wav"
        "*Ding-dong!*"
        kil "You dog."
        scene w3_4013 with dissolve
        mc "Shut up."
    else:
        kil "She might not be home."
        scene w3_4014 with dissolve
        play sound "sound effects/door-bell.wav"
        "*Ding-dong!*"
        scene w3_4013 with dissolve
        mc "Guess we'll see."

    scene w3_4012 with dissolve
    "Ian and I just stood and listened while the seconds piled up."
    play sound "sound effects/door-bell.wav"
    scene w3_4014 with dissolve
    "*Ding-dong!*"
    mc "Hey, Rose? It's [mcf]."
    scene w3_4012 with dissolve
    "Time marched on, but no signs of anyone coming to the door."
    "......"
    "..."
    scene w3_4015 with dissolve

    if roseFlag == True:
        kil "Guess she isn't home?"
    else:
        kil "Guess she isn't?"

    scene w3_4016 with dissolve
    mc "Yeeeah, this is probably silly, let's--"
    play sound "sound effects/walk-wood.mp3" fadein 3.0
    scene w3_4017 with dissolve
    "Just then, the faint sound of footsteps stole our attention."
    "The pitter-patter grew louder, followed by the fumbling of a lock and the jiggle of the doorknob."
    scene w3_4015 with dissolve
    kil "Looks like you were worried for nothing."
    scene w3_4017 with dissolve
    "And finally, breaking the arduous anticipation..."
    play sound "sound effects/door-open.wav"
    scene w3_4018 with dissolve
    rose "Oh... hey."
    play music "music/i-knew-a-guy.ogg"
    scene w3_4019 with dissolve
    "Rosalind's mouse-like face poked ever so slightly from the crevice of her front door."
    scene w3_4020 with dissolve
    mc "Oh, good! Hey! I know this sounds crazy, but... I got worried after our call got dropped."
    scene w3_4019 with dissolve
    mct "(Her phone probably died, right?)"
    scene w3_4021 with dissolve
    rose "Oh, uh... thanks for checking in?"
    scene w3_4019 with dissolve
    mct "(But if that was the case, why does she look uneasy?)"
    "Her face was red, nervous looking, and uncertain."
    scene w3_4022 with dissolve
    kil "Is... everything alright?"
    "He noticed it too."
    scene w3_4021 with dissolve
    rose "Yeah! Sorry, I just... I was in the middle of something, and {i}I didn't want to be disturbed,{/i} so I turned my phone off."
    scene w3_4019 with dissolve
    "......"
    scene w3_4024 with dissolve
    "..."
    "I was quite obviously scrutinizing her, so much so that the motherly beauty skirted my gaze."
    scene w3_4023 with dissolve
    rose "I wanted to disconnect, y'know? For the first time in a while..."
    scene w3_4024 with dissolve
    "Something {i}was{/i} weird here."
    scene w3_4025 with dissolve
    mc "Hey, Rose... why are you talking to us through the door?"
    scene w3_4019 with dissolve
    "No other way to cut it. Something {i}is{/i} off."
    scene w3_4021 with dissolve
    rose "I hadn't noticed."
    scene w3_4026 with dissolve
    rose "I've got unexpected company. {b}Family{/b} from out town. You can understand why I might..."
    scene w3_4027 with dissolve
    mc "......"
    mc "..."
    scene w3_4028 with dissolve
    mc "Hey, Rose?"
    scene w3_4026 with dissolve
    rose "W-what is it?"
    scene w3_4029 with dissolve
    mc "Do you usually leave things knocked over and thrown about the floor when you have company?"
    rose "I, uhh--"
    play music "music/leaving-home.ogg"
    scene w3_4030 with dissolve
    man "Just open the door."
    "I knew that voice."
    scene w3_4031 with fade
    rose "Ah, b-ut-"
    olly "Didn't you hear her? She has company. You come off as creepy when you don't take the hint."
    scene w3_4032 with dissolve
    kil "Who the fuck are you? Mary Poppins?"
    "The loan shark who had been pestering Rosalind, in the flesh."
    scene w3_4033 with dissolve
    olly "Yeah, bend over. I've got an umbrella for your ass."
    scene w3_4034 with dissolve
    kil "Yeah?! Get--"
    mc "{b}Stop.{/b}"
    scene w3_4035 with dissolve
    "It hit me."
    "A sinking, snaking feeling that unfurled itself from my id and coiled around my mother wit."
    "I knew this feeling well."
    "It was {b}agitation{/b}, not born from principle or righteous indignation, but from instinct."
    hide screen textbox2 with dissolve
    scene w3_4036 with dissolve
    "It was my body deciding to fight over flight, getting juiced to face down a challenge."
    olly "I thought I recognized your voice. You're the one I spoke to on the phone, werren'you? What was your name again?"
    "The problem was, this wasn't a childhood scrap."
    "The man in front of us wasn't some bloviating bully or drunkard, and there were ramifications for my position at the club, Rosalind's predicament, and even my immediate safety."

    menu:
        "Be direct (Dialogue/render changes only).":
            scene w3_4037 with dissolve
            mc "What are you doing here? You were supposed to fuck off for a couple of weeks."
            scene w3_4036 with dissolve
            mct "(I have to deal with this decisively. If I budge an inch, he'll walk all over us.)"
            olly "...was I, now? And who are you to say that?"
            scene w3_4038 with dissolve
            "The way I saw it, I had a few priorities here. Chief among them was chasing this prick out of here."
            "Lesser concerns: avoiding a commotion that would draw the attention of Rosalind's neighbors, avoiding getting the cops called on us, and..."
            scene w3_4041 with dissolve
            kil "Your ugly whore mother just calls him Payday, Britbong."
            "...{b}not getting punched in the face.{/b}"
            scene w3_4042 with dissolve
            mc "You're not helping."
            scene w3_4039 with dissolve
            mc "My name's [mcf]."
            scene w3_4045 with dissolve
            mc "This is Ian."
            scene w3_4039 with dissolve
            mc "And you're Oliver. Great, now we all know each other, {b}why are you here?{/b}"
            scene w3_4040 with dissolve
            olly "Oh, yeah. That's what you said your name was. Want a word of advice, [mcf]?"
            scene w3_4043 with dissolve
            olly "{b}Scram.{/b} We're havin' a private conversation and you're sourin' my mood."
        "Be amiable(w3RosalindConfrontationAmiable = True).":

            $ w3RosalindConfrontationAmiable = True
            scene w3_4037 with dissolve
            mc "Olly to your friends, right?"
            scene w3_4036 with dissolve
            mct "(I have to deal with this delicately. If we start a shoving match, literal or otherwise, we are more likely to budge.)"
            olly "Oh, is this friendly?"
            scene w3_4038 with dissolve
            "The way I saw it, I had a few priorities here..."
            scene w3_4039 with dissolve
            mc "No, we're not, but it's in all our interests that we take it down a notch."
            "Chief among them was diffusing the situation and getting this man out of her home."
            scene w3_4038 with dissolve
            "Lesser concerns..."
            scene w3_4040 with dissolve
            olly "Actually, it's in your best interest to get the fuck outta here. You're sticking your nose in a private conversation."
            "...avoiding a commotion that would draw the attention of Rosalind's neighbors, avoiding getting the cops called on us, and--"
            scene w3_4041 with dissolve
            kil "Take your own advice before we fuck you up, asshole."
            "--not getting punched in the face."
            scene w3_4043 with dissolve
            olly "Try me."
            scene w3_4044 with dissolve
            mc "Not helping."
            scene w3_4039 with dissolve
            mc "...people are going to start wondering what's going on."
            scene w3_4040 with dissolve
            olly "Let 'em. I ain't listening to a toddler lecture me about my business."
            scene w3_4041 with dissolve
            kil "You have no idea who you're fucking with."
            scene w3_4040 with dissolve
            olly "By all means, fill me in."
            scene w3_4045 with dissolve
            mc "I'm [mcf]. This is Ian."
            scene w3_4040 with dissolve
            olly "Oh, yeah. Those fit a pair of wankers like you real well."
        "Ask if Rosalind is okay."(chg=["rosalind_up"]):


            $ Rosalind_Affection +=1
            scene w3_4054 with dissolve
            mc "Are you okay, Rose?"
            scene w3_4055 with dissolve
            mct "(When dealing with this, I must be mindful of Rose and not make her situation worse.)"
            olly "Eh? Don't talk to her. You're talking to me."
            scene w3_4047 with dissolve
            "The way I saw it, I had a few priorities here. Chief among them was getting this prick away from Rosalind and ensuring she was safe."
            scene w3_4046 with dissolve
            mc "{b}Are you okay?{/b}"
            scene w3_4047 with dissolve
            "Lesser concerns: avoiding a commotion that would draw the attention of Rosalind's neighbors, avoiding getting the cops called on us, and not getting punched in the face."
            scene w3_4048 with dissolve
            rose "Um, y-yeah, I'm... can't you just leave, please?"
            scene w3_4046 with dissolve
            mc "Not an option, I'm afraid."
            scene w3_4040 with dissolve
            olly "How's it not when you got two perfectly workin' legs at the moment?"
            scene w3_4041 with dissolve
            kil "Get over here, Rose."
            scene w3_4049 with dissolve
            olly "{b}Stay the fuck where you are{/b}, cunt."
            scene w3_4048 with dissolve
            rose "S-seriously, [mcf]. You can go, I'm... I'm fine."
            scene w3_4040 with dissolve
            olly "Oh, that's right. You said your name was [mcf]."

    if rosalindAugSolution == True:
        scene w3_4056 with dissolve
        mc "August Byrnes asked you to back off, didn't he? Did you not get the message?"
        olly "Yeah, I got the \"message.\" The thing is, I was real gobsmacked about why some dinosaur I've never met was poking around in my business."
        olly "Now that I see the arse-mongers he associates with, I can safely say he's nothing."
        kil "You seriously have no fucking idea what kind of problem you're making for yourself."
        scene w3_4053 with dissolve
        olly "No, what I can't figure out is why August Byrnes had the nerve to try and throw his irrelevant ass around like it meant somethin' to me."
        scene w3_4051 with dissolve
        olly "Actually, I was tryin' to get to the bottom of that before you came a-knocking. It's not every day a bitch sends someone to try and strong-arm me."
        scene w3_4050 with dissolve
        mc "She didn't send anyone. It was my idea."
        scene w3_4051 with dissolve
        olly "Yours? Who the fuck are you?"
        scene w3_4050 with dissolve
        mc "A friend."
        scene w3_4051 with dissolve
        olly "Well, \"friend\" just don't cut it. I figure it like this: out of us bunch, I'm the only one who's got a legitimate claim here. Rosie is into me for some serious money, and I'm not stopping my trade just because someone asked nicely."
        scene w3_4053 with dissolve
        olly "What fuckin' right do you have to tell me to back off?"
        scene w3_4050 with dissolve
        mct "(Well, {b}shit{/b}....)"
        scene w3_4057 with dissolve
        "We didn't have a leg to stand on if the old man's name meant nothing to him. But, nevertheless, he had to go and it was up to us to convince him."
        "Our choices were not to flinch or try a more diplomatic approach."
        stop music fadeout 3.0

        menu:
            "Ramp up the antagonism(Dialogue/render changes only).":
                play music "music/Darkdub.ogg"
                scene w3_4058 with dissolve
                mc "Yeah, I see what the problem was... you were asked {i}nicely{/i}."
                "I had NO intention of fighting him. Sure, there were two of us, but knocking heads was his job. If we could get him out in the hall, we {i}might{/i} be able to corner him, but I still didn't like my chances."
                scene w3_4060 with dissolve
                olly "That's not as cool as you think it is."
                scene w3_4059 with dissolve
                "Plus, even with our numbers, it only took one errant hit to make this a 1-on-1. Not to mention, brawling in the middle of a hallway might get us arrested. "
                scene w3_4061 with dissolve
                mc "They're expensive."
                scene w3_4059 with dissolve
                "I could only HOPE that he was cognizant of that reality as well, and this was just a matter of posturing. After all, I was chained to August's narrative and he believed us to share in the same line of work."
                scene w3_4060 with dissolve
                olly "Well...?"
                scene w3_4059 with dissolve
                "To get anywhere with him, we had to speak the same language."
                scene w3_4061 with dissolve
                mc "The way I see it is this: you're outnumbered."
                scene w3_4062 with dissolve
                olly "Not outmatched."
                scene w3_4061 with dissolve
                mc "That's something we can find out if you want."
                scene w3_4059 with dissolve
                "This was fucking stupid, he was a career criminal and I most certainly wasn't, but I was going with my gut."
                scene w3_4061 with dissolve
                mc "All up to you."
                scene w3_4063 with dissolve
                kil "Just walk away. You've made your point."
                scene w3_4062 with dissolve
                olly "Don't tell me how to do my business."
                scene w3_4061 with dissolve
                mc "Is there a point to this? There's nothing gained here. You can't get money that's not there, and us acting like Neanderthals won't change that."
                scene w3_4060 with dissolve
                olly "I can think of a couple things. One, sending a message, and the other... the fun of kicking your teeth in."
                scene w3_4064 with dissolve
                mc "{b}Go home for the day.{/b} You'll have your money in due time."
                scene w3_4065 with dissolve
                "........."
                scene w3_4064 with dissolve
                "......"
                "..."
                scene w3_4066 with dissolve
                olly "Tell you what. If your boss wants me to be a ghost, all it takes is to pay me what I'm owed, geddit?"
                scene w3_4064 with dissolve
                mc "I can pass the message along."
                scene w3_4068 with dissolve
                olly "That easy, huh?"
                scene w3_4064 with dissolve
                mc "Yeah. Just leave Rosalind alone in the meantime."
                "It was funny. Even if I could get the money - which, realistically, I very well could... {i}paying him off wasn't an option.{/i}"
                "Her being on the hook with him meant she was on the line with the Club."
                scene w3_4068 with dissolve
                olly "Really...? Your boss must think she's one hell of a lay."
                scene w3_4064 with dissolve
                "It was a twisted, parasitic relationship that ultimately benefitted my bottom line too. That was something I needed to remind myself of before my agitation changed its tune to moral contempt."
                scene w3_4064 with dissolve
                mc "Will you leave?"
                scene w3_4067 with dissolve
                olly "How did you manage to fall in with these fools? Hubby owes them money too?"
                scene w3_4065 with dissolve
                rose "I-- uh..."
                scene w3_4064 with dissolve
                mc "Our business isn't yours."
                scene w3_4066 with dissolve
                olly "Oi, the balls on you! You're the one mucking about in other people's!"
                scene w3_4069 with dissolve
                mc "You can tell me exactly what she owes."
                scene w3_4072 with dissolve
                olly "..."
                scene w3_4071 with dissolve
                olly "I'm going to leave today, but let's be clear. I'm going to come back tomorrow. And then the next day. And then the next day after that until everything's settled."
                olly "Every time I'm gonna be a little less happy."
                scene w3_4070 with dissolve
                "That was fine."
                scene w3_4071 with dissolve
                olly "I don't know what business you have with her and I don't care. You and your boss are pissin' in my neck of the woods and that isn't okay."
                scene w3_4070 with dissolve
                "All we needed was for him to be removed from our immediate reality and then we could figure out the future."
                scene w3_4073 with dissolve
                olly "Hmpf. After all, let's talk about what she owes. "
                "That went easier than it had any right to."
                scene w3_4074 with dissolve
                mc "Was he the only one here, Rose?"
                scene w3_4075 with dissolve
                rose "Ummm- y-yes."
                scene w3_4076 with dissolve
                "She looked so small right now, contrary to the veiled tenacity she had at the club."
                scene w3_4077 with dissolve
                mc "Stay back with Rose."
                scene w3_4078 with dissolve
                kil "That's not a good idea."
                scene w3_4077 with dissolve
                mc "It's not, but I'm just going to talk to him down the hall. So, keep a lookout for both of us, alright?"
                scene w3_4079 with dissolve
                "Ian looked like he didn't want to, but..."
                scene w3_4078 with dissolve
                kil "Yeah, man. I'll keep an eye out."
                scene w3_4077 with dissolve
                mc "Thanks."
                scene w3_4080 with fade
                "We only ventured a little bit down the hall before Oliver stopped."
                olly "I want to be clear about something."
                scene oli_punch_a with dissolve
                mc "Yeah--"
                stop music
                scene edwinsuckerpunched with dissolve
                show oli_punch with dissolve
                mc "Hnngggg-!!!"
                olly "{b}That.{/b}"
                "I had never been punched like that."
                play music "music/hypnosis.ogg"
                scene w3_4082 with dissolve
                mc "G-gahhh-"
                mct "(Is this son-of-a-bitch a boxer or-- {b}s-shit?!{/b})"
                mc "*Cough, cough* Hnngg, haaaaa-"
                rose "[mcf]!"
                scene w3_4083 with dissolve
                olly "You're a pussy. I knew that from the beginning."
                "I tried to bitterly suck down air, but my body resisted that notion. Every puff of air that passed through my pharynx {b}hurt me.{/b}"
                olly "I'm not afraid of your boss. Be sure to include that with the message."
                scene w3_4084 with dissolve
                kil "You son of a bitch!"
                "Agitation gave way to anger. My brain was in panic mode, trying to reconcile the fact that I could no longer breathe the way I was used to, and it compelled me to do something stupid and futile."

                menu w3SuckerPunched:
                    "{color=#FF1493}[[Strongman]{/color} Tackle him." if perk_strongman == True:
                        "I could hear Ian approach and I knew he wasn't bullshitting earlier. He outmatched us."
                        play music "music/ninja-tortoise.ogg"
                        scene w3_4085 with vpunch
                        "My only chance was--"
                        scene w3_4086 with dissolve
                        "Mustering every bit of strength in my body, I went low and fast and hard in a vain attempt to knock him off balance."
                        play sound "sound effects/thud-heavy.wav"
                        scene w3_4087 with hpunch
                        "Surprisingly, we both ended up on the dirty, cold floor. Now, I could only hope that Ian-"
                        scene w3_4088 with dissolve
                        pause
                        play sound "sound effects/thud-floor.mp3"
                        scene w3_4089 with vpunch
                        pause
                        scene w3_4090 with dissolve
                        mct "{b}(Shit!{/b} That didn't have the impact we needed--)"
                        scene w3_4091 with dissolve
                        mct "(What the fuck?!)"
                        scene w3_4093 with dissolve
                        mct "(What the hell is that strength?)"
                        "He tossed me back like I weighed nothing and we found ourselves upright and each relatively unscathed, our slight advantage of getting him on the ground gone in an instant."
                        "{i}This was a mistake{/i}."
                        scene w3_4092 with dissolve
                        olly "Ahahaha-"
                        scene w3_4093 with dissolve
                        "He chuckled, inordinately amused by this outcome. We were out of our depths."
                        scene w3_4092 with dissolve
                        olly "How'd you blow that one, boys? You both should've pinned me."
                        scene w3_4093 with dissolve
                        "...and he knew he was dealing with amateurs."
                        scene w3_4094 with dissolve
                        "After, all four of us didn't make a sound or a move."
                        "Oliver was performing something of a cost analysis while I fruitlessly considered what my options were if this wasn't the end of it."
                        stop music
                        play sound "sound effects/door-open.wav"
                        scene w3_4095 with dissolve
                        olly "..."
                        neighbor "Is everything okay, Rose?"
                        rose "Ah, umm ehh--"
                        scene w3_4096 with dissolve
                        olly "See you around, boys. Remember to pass on my message."
                        "That was well-timed."
                        rose "Yeah, everything's good. Sorry for the commotion."
                        scene black with fade
                        mc "...let's get inside. I feel like I'm about to puke."
                        $ w3RCTussled = True
                        jump w3RosalindPostConfrontation
                    "Attack him.(w3EdwinKnockedOut = True)":

                        $ w3EdwinKnockedOut = True
                        scene w3_4097 with dissolve
                        "--!"
                        "He didn't even budge, and..."
                        stop music
                        play sound "sound effects/punch.wav"
                        scene w3_4098 with hpunch
                        "Every action has an opposite and equal reaction."
                        scene w3_4099 with dissolve
                        kil "Shit! [mcf]!"
                        scene black with fade
                        "........."
                        "......"
                        "..."
                        $ w3RCKnockout = True
                        jump w3RosalindPostConfrontation
                    "Resist the urge. Let him have his petty victory.":

                        scene w3_4100 with dissolve
                        mc "Stop! *Cough-* I'm fine!"
                        scene w3_4101 with dissolve
                        kil "What the fuck, bro? Don't just let him-"
                        mc "Don't fuckin' do anything!"
                        scene w3_4102 with dissolve
                        kil "Wh- ahh-"
                        mc "...it's cool. He just wanted me to pass along a message."
                        scene w3_4103 with dissolve
                        "No sense in letting this devolve further when he's already out the door."
                        scene w3_4104 with dissolve
                        olly "Smart. Stay down."
                        scene w3_4105 with dissolve
                        mc "...is that all you're going to dictate?"
                        scene w3_4104 with dissolve
                        olly "Let's be clear: the only reason I'm leaving is because I'm done here. You can't squeeze blood from a stone, but lucky for me, this slag found me a cactus."
                        scene w3_4106 with dissolve
                        olly "Tell your boss to come see me in person next time if he does want to buy the debt. Otherwise, {b}fuck off{/b}."
                        stop music fadeout 3.0
                        scene w3_4107 with dissolve
                        "That stupid mother fucker truly has no idea, huh?"
                        scene w3_4108 with dissolve
                        kil "Shit, man, you alright?"
                        scene black with fade
                        mc "...let's get inside. I feel like I'm about to puke."
                        $ w3RCSuckerPunched = True
                        jump w3RosalindPostConfrontation

                    "{color=#696969}[[Strongman] Tackle him.{/color}" if perk_strongman == False:
                        jump w3SuckerPunched
            "Explain the situation calmly.":


                play music "music/landing.ogg"
                scene w3_4111 with dissolve
                mc "We just need you to stop hassling her for a couple of weeks. That's for as long as we have business with her."
                scene w3_4112 with dissolve
                olly "And what business is that?"
                scene w3_4113 with dissolve
                "......"
                "..."
                scene w3_4111 with dissolve
                mc "You don't need to know."
                scene w3_4112 with dissolve
                olly "That's rich, considering you're trying to trample on mine."
                scene w3_4111 with dissolve
                mc "It's not like we're asking you to forgive her debt. She owes what she owes, but is there any harm in cutting her a break until the end of June?"
                scene w3_4112 with dissolve
                olly "You could ask me, \"What time is it?\" and I'll still tell you to fuck off. You're overstepping the bounds."
                scene w3_4111 with dissolve
                mc "You can't get money that she doesn't have, but she is working on it. What's the point of hounding her and breaking her shit in the meantime?"
                scene w3_4112 with dissolve
                olly "Oi, are we actually in the same line of work? What load of shite is that?"
                scene w3_4111 with dissolve
                mc "We're not loan sharks."
                scene w3_4112 with dissolve
                olly "What happened to \"I didn't need to know\", eh?"
                scene w3_4113 with dissolve
                "We couldn't just come out with the truth. Besides not talking about the club, Rosalind's compensation was tenuous and wouldn't likely inspire confidence that he would get what he's owed after the two weeks were up."
                scene w3_4050 with dissolve
                mc "She's performing for us."
                scene w3_4051 with dissolve
                olly "Oh, yeah...? Now THAT is a surprise. They always do, but she acted like she was above that line of work."
                scene w3_4114 with dissolve
                olly "How you'd fall in with these cocksuckers? Hubby owes them too?"
                rose "Um, well..."
                scene w3_4050 with dissolve
                mc "It doesn't matter. Just give us two weeks."
                scene w3_4053 with dissolve
                olly "Eh? Wasn't I clear? You're the improper fuckers here. The only courtesy I'm giving you is keeping this peaceable-like."
                scene w3_4115 with dissolve
                mck "..."
                scene w3_4117 with dissolve
                mc "What do you know about our boss? I'm starting to think the message wasn't relayed very well."
                scene w3_4118 with dissolve
                olly "Enough to know he's a washed-up old timer who thinks he has pull. I've got a few boys and he doesn't seem to have much of a stake anymore, y'know?"
                scene w3_4116 with dissolve
                "To be honest, I didn't know if his appraisal of August was correct. And even if August did have weight to throw around like he himself implied, I was just a suburbanite kid. I didn't have the gravitas that would convince the man in front of me otherwise."
                scene w3_4118 with dissolve
                olly "Besides, it's the principle o' the matter. Whatever this sad bitch has going with your boss isn't my concern."
                scene w3_4116 with dissolve

                menu:
                    "{color=#FF1493}[[Social Chameleon]{/color} Bluff that he has a dangerous misconception." if perk_socialChameleon == True:
                        scene w3_4120 with dissolve
                        mc "That's the thing..."
                        scene w3_4121 with dissolve
                        "I did my best to sound cold, but I was aware of how I looked. However, I didn't have too many options now that {i}please{/i} failed."
                        scene w3_4120 with dissolve
                        mc "{b}It is your problem.{/b} You just don't know it yet."
                        scene w3_4121 with dissolve
                        "We wanted him gone and he didn't want to be gone, and this fucker spoke a particular language."
                        scene w3_4122 with dissolve
                        olly "You hear that line in a movie?"
                        scene w3_4123 with dissolve
                        mc "You're looking at us like you have nothing to be afraid of and you're right."
                        mc "We're nothing. You could kick our asses pretty handily, but it isn't us you have to worry about."
                        mc "We're not your problem."
                        scene w3_4120 with dissolve
                        mc "{b}August Byrnes is your problem.{/b} The only question is just how late will you be in recognizing it? Because that's the great thing about morons like you is that you make it easy."
                        scene w3_4124 with dissolve
                        mc "Have you ever heard \"Beware of an old man in a profession where men usually die young?\" August may be old, but that just means he's had time to find the pockets of people who are very much a problem for idiots like you."
                        mc "If you don't get smart quick, you're going to find his dick buried in your ass, choking on your blood and bleating like a stuck goat."
                        scene w3_4125 with dissolve
                        "We stared, unblinking at each other. On the absolute edge."
                        scene w3_4126 with dissolve
                        "......"
                        "...for what seemed to be way too long. I expected to get decked at any moment; there was no way that worked."
                        scene w3_4127 with dissolve
                        olly "You finished?"
                        scene w3_4128 with dissolve
                        kil "You really should call it a day and ask around before you make any hasty decisions."
                        scene w3_4127 with dissolve
                        olly "Let's be clear on something. I'll be back tomorrow, and if I see either of you again, I'm going to be less polite."
                        scene w3_4129 with dissolve
                        mc "See you tomorrow."
                        scene w3_4130 with dissolve
                        "That was all I was hoping for, to get him far away from us right now. Once that had been achieved, we could start thinking about the after."
                        play sound "sound effects/thud-floor.mp3"
                        scene w3_4131 with vpunch
                        mc "-gh!"
                        olly "Full of air, are you?"
                        scene w3_4132 with dissolve
                        "......"
                        "..."
                        scene w3_4166 with dissolve
                        mc "How the hell did that work?!"
                        kil "Ha, bro, that was totally cringe! Bleating like a stuck goat?"
                        mc "Whatever, it worked!"
                        stop music fadeout 3.0
                        scene black with fade
                        mc "Let's get inside."
                        $ w3RCTalkedDown = True
                        jump w3RosalindPostConfrontation



                    "Tell him that it will become his concern." if perk_socialChameleon == False:
                        scene w3_4117 with dissolve
                        mc "I would rethink that perspective. Our boss is a pretty scary guy."
                        scene w3_4118 with dissolve
                        olly "Is he?"
                        scene w3_4133 with dissolve
                        mc "You have no idea the kind of people he--"
                        play music "music/Darkdub.ogg"
                        play sound "sound effects/thud-heavy.wav"
                        scene w3_4134 with vpunch
                        mc "Ghh-?!"
                        play sound "sound effects/punch.wav"
                        scene w3_4135 with hpunch
                        kil "--!"
                        scene w3_4136 with dissolve
                        rose "Ah, s-stop--"
                        "It was fast, it was decisive, and it was absolute."
                        rose "-boys!"
                        scene w3_4137 with dissolve
                        "Neither Ian or I got up, our bodies a step ahead in recognizing what our brains, wracked with panic from still processing the sudden violence, did not."
                        "{i}Stay down.{/i} Do not get hit again."
                        "You can't breathe. You can't breathe. Youcantbreathe. YoucantbreatheYoucantbreatheYoucantbreatheYoucantbreathe. "
                        scene w3_4138 with dissolve
                        olly "Get the message?"
                        mc "Hnggg- I cant'-"
                        scene w3_4139 with dissolve
                        rose "Eehh, eeehh-"
                        scene w3_4138 with dissolve
                        olly "There's no worming your way out of what you owe me! Get it?"
                        scene w3_4139 with dissolve
                        rose "I, ehhh-"
                        scene w3_4138 with dissolve
                        olly "Right? Right?! You fucking get me?! Tell me you get it!"
                        scene w3_4139 with dissolve
                        rose "I understand!"
                        play sound "sound effects/thud-floor.mp3"
                        scene w3_4140 with vpunch
                        rose "Gehh-"
                        olly " I swear to God. Some old fuck telling me to fuck off, you're lucky I don't--"
                        scene w3_4141 with dissolve
                        "It was overwhelming and brokered no discussion."
                        olly "I'm guessin' I'll see you boys later. I'll be around."
                        scene w3_4142 with dissolve
                        "Well... we wanted him gone and now he was gone. If only I could {i}breathe{/i}."
                        kil "Geeeuhh- what happened...?"
                        mc "*Cough, c-cough-!*"
                        mct "(Was I going to die?)"
                        rose "A-are you okay?"
                        scene w3_4143 with dissolve
                        rose "Oh, no. Oh, no. I'm sorry!"
                        mc "*Cough, cough!!!!*"
                        stop music fadeout 3.0
                        scene black with fade
                        "Once we collected ourselves, we went inside."
                        $ w3RCDoubleAssBeat = True
                        jump w3RosalindPostConfrontation
                    "His concern is about money, so you play to that.":


                        scene w3_4064 with dissolve
                        mc "...then how about we cover what she owes for the next two weeks?"
                        "That WAS my original idea, before the old man erroneously assured me his name was good for taking care of this..."
                        scene w3_4066 with dissolve
                        olly "No."
                        scene w3_4144 with dissolve
                        mc "Just... no? Isn't this all about money?"
                        scene w3_4145 with dissolve
                        olly "You got it. And for whatever reason, and I got no inklin' as to why, these two weeks sound important to your boss..."
                        scene w3_4146 with dissolve
                        "He closed the distance, like a shark that smelled blood in the water."
                        kil "Back the fuck up, asshole."
                        olly "--and to top it all off, you've been disrespectful. so I'm not feelin' all that amiable, geddit?"
                        scene w3_4148 with dissolve
                        mc "...okay, then. What {i}will{/i} it take for you to leave her alone?"
                        scene w3_4149 with dissolve
                        olly "Settle her account, a dollar-twenty on the dollar for my trouble. "
                        scene w3_4147 with dissolve
                        "That seemed unlikely. Rosalind being on the hook to him meant she was on the line to the club, although thinking about it... getting her indebted to the club might be even better for \"our\" purposes..."
                        scene w3_4148 with dissolve
                        mc "I can ask our boss."
                        scene w3_4147 with dissolve
                        "Truthfully, I didn't know which was better for her, but my only goal right now was to get him to leave. Figuring out the rest could come later."
                        scene w3_4149 with dissolve
                        olly "Yeah, you do that and we won't have anybody stepping on each other's toes. Now..."
                        scene w3_4150 with dissolve
                        olly "......"
                        scene w3_4151 with dissolve
                        olly "...let's go out in the hall and continue this chat. I'm feelin' a bit cramped."
                        scene w3_4152 with dissolve
                        mc "After you..."
                        scene w3_4153 with dissolve
                        "With the vibes he was putting off, I didn't really want to turn my back on the guy."
                        scene w3_4154 with dissolve
                        olly "Y'know, I've kept shop for three years and it's always something."
                        scene w3_4155 with dissolve
                        olly "People always find a new excuse or new ways to try and weasel out of what's due, but the thing I love about this job, is that my part never changes. The solution is always the same."
                        scene w3_4156 with dissolve
                        olly "I haven't been clear enough about my displeasure about all of this."
                        "{i}Shit{/i}."
                        play music "music/Darkdub.ogg"
                        play sound "sound effects/thud-heavy.wav"
                        scene w3_4157 with hpunch
                        mc "-Ghhk!"
                        "In a flash, the loan shark had me pinned and breathless, weight bearing down from his tree trunk-like forearms and threatening to snap my neck."
                        kil "G-et off him!"
                        scene w3_4158 with dissolve
                        "Ian called out, but thankfully, he had enough sense not to move. If the large man wanted, he could have me choked out before my friend closed the distance."
                        kil "I said, get the fuck off him, asshole!"
                        scene w3_4159 with dissolve
                        "Ian tried again, but got no response in return. Instead, Oliver and I were doing all the communicating necessary."
                        scene w3_4160 with dissolve
                        "After all, the look on the mean man's face told me everything he had to say."
                        "It made clear his anger, showcased the outcome of fucking with him, and told me how lucky I was that this was the end of it."
                        mc "Ghhhk- yhhh-"
                        scene w3_4161 with dissolve
                        "I did my best not to panic and waste the little air I had left in my lungs, but as time passed I felt myself get dizzy-headed."
                        mc "Ghh, hhk-!"
                        mct "(W-wait, was this the end of it, he's not really going to--!)"
                        scene w3_4162 with dissolve
                        "That's when the panic set in. He was really going to choke me out."
                        mc "Hhhak, hhhg...!"
                        mct "(D-damn it, I get the message, you p-prick! Just-!)"
                        scene w3_4163 with dissolve
                        mc "*Cough* Gauhh- hhhaa..!"
                        olly "Hmpfh. Pussy."
                        scene w3_4164 with dissolve
                        olly "Tell your boss the next time he has a message, he should deliver it himself."
                        scene w3_4165 with dissolve
                        rose "[mcf]! Are you okay?"
                        kil "Goddamn it, bro. I didn't know what to do. Like, like--"
                        mc "It's cool, I'm fine, don't worry about it..."
                        stop music fadeout 3.0
                        scene black with fade
                        mc "Let's just get inside. We need to talk."
                        $ w3RCThreatened = True
                        jump w3RosalindPostConfrontation

                    "{color=#696969}[[Social Chameleon] Bluff that he has a dangerous misconception. {/color}" if perk_socialChameleon == False:
                        jump w3AugustRoseCalmSubMenu
    else:


        scene w3_4056 with dissolve
        mc "You're paid up in advance. You shouldn't be here."
        olly "Ah, so you're the git she got the money from?"
        olly "I honestly expected someone a bit older. Fleecin' kids out of their milk money, are you?"
        scene w3_4167 with dissolve
        rose "See... I wasn't holding out on you. You can leave."
        scene w3_4168 with dissolve
        olly "I'm hurt. You pretended like it was above you, but then you went and spread your legs to bleed money from some stupid kid?"
        scene w3_4169 with dissolve
        olly "If you were going to use your body to settle things, there was no need for a middle man."
        rose "..."
        scene w3_4170 with dissolve
        "He kept an eye on both of us, but it was clear that he thought lightly of the situation. He didn't regard us as threats."
        mc "You have your money. I don't understand what you're doing here."
        scene w3_4171 with dissolve
        olly "Don't tell me my business. Until the account is settled, I keep an eye on my investments. 'Specially when they pull five grand out of thin air and then refuse to answer my questions about it."
        scene w3_4172 with dissolve

        if w3RosalindConfrontationAmiable == True:
            mc "Well, you got it right, I'm the sucker that paid you. Now, would you please leave?"
            scene w3_4173 with dissolve
            olly "I'll leave when I want to."
            kil "My friend asked you nicely. Get the fuck out of here, asshole."
        else:
            mc "Well, there you have it. I'm indeed the sucker that paid you. Now, {b}leave{/b}."
            scene w3_4173 with dissolve
            olly "I get it, you're trying to look tough in front of the bird, so I'm not going to take offense at you telling me what to do."
            kil "Didn't you hear my friend? Get out of here, asshole."


        scene w3_4150 with dissolve
        "Ian squared up next to me. That was a small relief, although I had no plans of this coming to blows."
        scene w3_4149 with dissolve
        olly "That's very cute, coming from a pair of cocksuckers."
        scene w3_4147 with dissolve
        "To be honest, I didn't like our chances. This guy knocked heads for a living, and no matter who got the worst of it, the only thing we would achieve is making things more difficult for Rosalind."
        stop music fadeout 3.0

        menu:
            "Keep calm and reason with him she doesn't need these reminders(Dialogue/render changes only).":
                play music "music/landing.ogg"
                scene w3_4148 with dissolve
                mc "...we're getting off on the wrong foot here."
                scene w3_4151 with dissolve
                olly "Are we? How do you figure?"
                scene w3_4148 with dissolve
                mc "There's no need to get into each other's face when you've already been paid."
                scene w3_4149 with dissolve
                olly "You like repeating yourself, huh?"
                scene w3_4148 with dissolve
                mc "I mean, the fact of the matter is, I just gave you five grand. That's a pretty good chunk of change and you're not helping things by putting the screws to Rosalind in the meantime."
                scene w3_4174 with dissolve
                olly "Hell, I might just start swinging by {b}daily{/b}."
                scene w3_4175 with dissolve
                mct "(Goddamn it...)"
                "The whole point of paying him in advance was to get Rosalind some breathing room, but like I suspected, this bastard is smelling blood in the water."
                scene w3_4176 with dissolve
                kil "Sounds like a good way to get arrested, asshole."
                olly "You think I work alone?"
                scene w3_4177 with dissolve
                rose "B-be reasonable... you'll get your money..."
                scene w3_4178 with dissolve
                olly "I've been more than fair to you, cunt!"
                "My blood ran cold at the sight of Rosalind's fearful face."
                "Suddenly her reality wasn't just an abstraction anymore."
                scene w3_4179 with dissolve
                "The anxiety-filled nights sobbing into a pillow, all the stiff-upper lips and fake smiles for her daughter... suddenly it all became very appreciable. I could see and hear it all, yet I knew I had no leg to stand on."
                "Her being on the hook to this bastard kept her on the line at the club, which in turn I made money from. That's something I tried to keep in mind, while I..."

                menu w3PaidOffRoseCalmSubMenu:
                    "{color=#FF1493}[[Social Chameleon]{/color} Reassure him he'll get his money." if perk_socialChameleon == True:
                        scene w3_4180 with dissolve
                        mc "Hey, listen... I get it. You're just doing your job and this bitch has jerked you around, right?"
                        scene w3_4181 with dissolve
                        "This was about money and respect and our feelings, wants and sense of right didn't factor into it."
                        "The most expedient way of getting him to leave was appealing to those needs."
                        "Once he was gone, we could then figure out how to keep Rosalind secure until the competition was over."
                        scene w3_4180 with dissolve
                        mc "Talk to me instead. We'll come to terms."
                        scene w3_4127 with dissolve
                        olly "Oh? You think you can set terms?"
                        scene w3_4126 with dissolve
                        mc "Well, we can try. I know you're not getting much out of her proactively. That's a dead end, and I know you have other ways to extract it, but I have an easier solution for you."
                        scene w3_4127 with dissolve
                        olly "What's that, kid? You gonna borrow your mommy's credit card?"
                        scene w3_4126 with dissolve
                        mc "My friend and I? We shoot porn."
                        scene w3_4182 with dissolve
                        olly "Yeah, what about it? You don't mean..."
                        scene w3_4183 with dissolve
                        olly "Oi, fuckin' A. You're...?"
                        scene w3_4184 with dissolve
                        mc "Yeah, she's working for us."
                        scene w3_4185 with dissolve
                        olly "You don't look the part."
                        scene w3_4186 with dissolve
                        mc "It's a small production. You know, couple young guys fucking older women? We make those sort of videos."
                        scene w3_4067 with dissolve
                        "The man scoffed."
                        olly "Huh, they always act like that's beneath them at first. It's like pulling a tooth to get these dumb bitches to face reality."
                        scene w3_4064 with dissolve
                        mc "What can I say? I guess you drove her into my corner."
                        scene w3_4068 with dissolve
                        olly "You expect me to believe you paid her five grand? Unless you're morons, that's a pretty big take."
                        scene w3_4064 with dissolve
                        mc "For one video? Sure, but she's staring in a series of them. She really does look nice on camera."
                        scene w3_4065 with dissolve
                        olly "......"
                        scene w3_4066 with dissolve
                        olly "... okay, maybe you do look the part. But so, what? Your business isn't mine."
                        scene w3_4111 with dissolve
                        mc "Sure, but yours is fucking with mine. So let's figure this out."
                        scene w3_4187 with dissolve
                        olly "Keep talking."
                        scene w3_4188 with dissolve
                        mc "To start things off... I'm not paying off her debt. She isn't worth that to me."
                        scene w3_4190 with dissolve
                        olly "You're not as stupid as you look."
                        scene w3_4188 with dissolve
                        mc "I've already given her five grand, but... well, shit. We'll call it an investment. I'll cover what she owes over the next week and a half and then some on top of that to make it worth your while."
                        scene w3_4189 with dissolve
                        "The man looked me over, trying to catch a whiff of bullshit."
                        scene w3_4190 with dissolve
                        olly "You got an office?"
                        scene w3_4188 with dissolve
                        mc "We don't have a fixed location. We used friend's apartments, hotels, other places we rent... like I said, we're small and independent."
                        scene w3_4191 with dissolve
                        mc "...you think I'm bullshitting you? Doesn't money talk?"
                        scene w3_4190 with dissolve
                        olly "I want to know where I can find you."
                        scene w3_4192 with dissolve
                        "Like hell I'm giving this asshole my address."
                        scene w3_4188 with dissolve
                        mc "You can get the money from Rosalind, like last time - and after that, I want you to stop bothering her."
                        scene w3_4190 with dissolve
                        olly "I'll come by tomorrow then. And if she's not here or empty-handed, I'm not going to be happy."
                        scene w3_4193 with dissolve
                        mc "C'mon, let's talk."
                        scene w3_4194 with dissolve
                        rose "......"
                        scene w3_4195 with dissolve
                        kil "...that's my dude."
                        scene w3_4196 with fade
                        mc "I said {i}some{/i} on top. You're taking advantage."
                        "With the money we've already given him, he's asking for over half of what she owes. This prick takes us for suckers."
                        scene w3_4197 with dissolve
                        olly "I'll be here tomorrow."
                        "Not that I had any plans of asking the bosses for the money. Once he got paid, he'd be back in here a few days, attempting to leech more out of us."
                        scene w3_4198 with dissolve
                        "Plus, at that point, the club might as well just outright buy Rosalind's debt and hold it over her head themselves..."
                        scene w3_4199 with dissolve
                        mct "(Seriously, {b}goddamn it...{/b})"
                        scene w3_4200 with dissolve
                        mc "...wanna invite us inside, Rose?"
                        scene black with fade
                        "We had to think of alternatives."
                        $ w3RCTalkedDown = True
                        jump w3RosalindPostConfrontation
                    "Keep keeping calm and just get rid of him.":

                        scene w3_4201 with dissolve
                        mc "She's right. We'll get you more money."
                        scene w3_4202 with dissolve
                        "This was about money. The most expedient way of getting him to leave was to dangle some in front of him."
                        olly "And how do you plan on doing that, mommy's credit card?"
                        scene w3_4201 with dissolve
                        mc "I make good money at my job."
                        scene w3_4202 with dissolve
                        olly "Which is...?"
                        scene w3_4201 with dissolve
                        mc "I'm in IT."
                        scene w3_4185 with dissolve
                        olly "Oh. Of course, you are."
                        scene w3_4186 with dissolve
                        mc "As I understand it, Rosalind owes you a couple hundred dollars every three days. I can give you that every two, to cover the interest and then some, and then every other Thursday I'll pay you three grand until her debt is gone."
                        scene w3_4203 with dissolve
                        olly "You'd really go that far for this bitch? You in love?"
                        scene w3_4184 with dissolve
                        mc "You're not trying to talk me out of it, are you? Don't look a foolish gift horse in the mouth."
                        scene w3_4186 with dissolve
                        "I, of course, had no plans of paying him. At that point, the club might as well just buy her debt outright and hold it over Rosalind's head ourselves. I just needed him to think I was a sucker to get him to go away peaceably."
                        scene w3_4130 with dissolve
                        olly "......"
                        "Figuring out what the fuck we were actually going to do about this could come later."
                        scene w3_4204 with dissolve
                        olly "...you just seem a bit too eager is all."
                        scene w3_4131 with dissolve
                        olly "C'mon, let's talk."
                        scene w3_4205 with dissolve
                        mc "Stay here."
                        scene w3_4206 with dissolve
                        olly "I'll collect the money from Rosie. If she's not here or if she's empty-handed, I'm not going to be happy."
                        mc "We're not going to jerk you around."
                        scene oli_punch_a with dissolve
                        mc "Don't worry--"
                        stop music
                        scene edwinsuckerpunched with dissolve
                        show oli_punch with dissolve
                        mc "Hnngggg-!!!"
                        "I had never been punched like that."
                        olly "I want to make myself clear."
                        play music "music/hypnosis.ogg"
                        scene w3_4082 with dissolve
                        mc "G-gahhh-"
                        mct "(Is this son-of-a-bitch a boxer or-- {b}s-shit?!{/b})"
                        mc "*Cough, cough* Hnngg, haaaaa-"
                        rose "[mcf]!"
                        scene w3_4083 with dissolve
                        olly "I want to be clear."
                        "I tried to bitterly suck down air, but my body resisted that notion. Every puff of air that passed through my pharynx {b}hurt me.{/b}"
                        olly "If you want to be that bitch's wallet, fine. You're on the hook now."
                        olly "Just know I'll take it out on her if you jerk me around."
                        scene w3_4084 with dissolve
                        kil "You son of a bitch!"
                        "Agitation gave way to anger. My brain was in panic mode, trying to reconcile the fact that I could no longer breathe the way I was used to, and it compelled me to do something stupid and futile."

                        menu w3SuckerPunched2:
                            "{color=#FF1493}[[Strongman]{/color} Tackle him." if perk_strongman == True:
                                "I could hear Ian approach and I knew he wasn't bullshitting earlier. He outmatched us."
                                play music "music/ninja-tortoise.ogg"
                                scene w3_4085 with vpunch
                                "My only chance was--"
                                scene w3_4086 with dissolve
                                "Mustering every bit of strength in my body, I went low and fast and hard in a vain attempt to knock him off balance."
                                play sound "sound effects/thud-heavy.wav"
                                scene w3_4087 with hpunch
                                "Surprisingly, we both ended up on the dirty, cold floor. Now, I could only hope that Ian-"
                                scene w3_4088 with dissolve
                                pause
                                play sound "sound effects/thud-floor.mp3"
                                scene w3_4089 with vpunch
                                pause
                                scene w3_4090 with dissolve
                                mct "{b}(Shit!{/b} That didn't have the impact we needed--)"
                                scene w3_4091 with dissolve
                                mct "(What the fuck?!)"
                                scene w3_4093 with dissolve
                                mct "(What the hell is that strength?)"
                                "He tossed me back like I weighed nothing and we found ourselves upright and each relatively unscathed, our slight advantage of getting him on the ground gone in an instant."
                                "{i}This was a mistake{/i}."
                                scene w3_4092 with dissolve
                                olly "Ahahaha-"
                                scene w3_4093 with dissolve
                                "He chuckled, inordinately amused by this outcome. We were out of our depths."
                                scene w3_4092 with dissolve
                                olly "How'd you blow that one, boys? You both should've pinned me."
                                scene w3_4093 with dissolve
                                "...and he knew he was dealing with amateurs."
                                scene w3_4094 with dissolve
                                "After, all four of us didn't make a sound or a move."
                                "Oliver was performing something of a cost analysis while I fruitlessly considered what my options were if this wasn't the end of it."
                                stop music
                                play sound "sound effects/door-open.wav"
                                scene w3_4095 with dissolve
                                olly "..."
                                neighbor "Is everything okay, Rose?"
                                rose "Ah, umm ehh--"
                                scene w3_4096 with dissolve
                                olly "I'll be back tomorrow."
                                "That was well-timed."
                                rose "Yeah, everything's good. Sorry for the commotion."
                                scene black with fade
                                mc "...let's get inside. I feel like I'm about to puke."
                                $ w3RCTussled = True
                                jump w3RosalindPostConfrontation
                            "Attack him(w3EdwinKnockedOut = True).":

                                $ w3EdwinKnockedOut = True
                                scene w3_4097 with dissolve
                                "--!"
                                "He didn't even budge, and..."
                                stop music
                                play sound "sound effects/punch.wav"
                                scene w3_4098 with hpunch
                                "Every action has an opposite and equal reaction."
                                scene w3_4099 with dissolve
                                kil "Shit! [mcf]!"
                                scene black with fade
                                "........."
                                "......"
                                "..."
                                $ w3RCKnockout = True
                                jump w3RosalindPostConfrontation
                            "Resist the urge. Let him have his petty victory.":

                                scene w3_4100 with dissolve
                                mc "Stop! *Cough-* I'm fine!"
                                scene w3_4101 with dissolve
                                kil "What the fuck, bro? Don't just let him-"
                                mc "Don't fuckin' do anything!"
                                scene w3_4102 with dissolve
                                kil "Wh- ahh-"
                                mc "...it's cool. He just wanted us to be clear on something."
                                scene w3_4103 with dissolve
                                "No sense in letting this devolve further when he's already out the door."
                                scene w3_4104 with dissolve
                                olly "Smart. Stay down."
                                scene w3_4105 with dissolve
                                mc "...I think we have an understanding?"
                                scene w3_4104 with dissolve
                                olly "I'll be back tomorrow for my first payment."
                                scene w3_4108 with dissolve
                                kil "Shit, man, you alright?"
                                scene black with fade
                                mc "...let's get inside. I feel like I'm about to puke."
                                $ w3RCSuckerPunched = True
                                jump w3RosalindPostConfrontation

                            "{color=#696969}[[Strongman] Tackle him.{/color}" if perk_strongman == False:
                                jump w3SuckerPunched2
                    "Switch gears. Threaten that he leave.":

                        scene w3_4207 with dissolve
                        mc "You should leave. {b}Now{/b}. Rosalind's current on her payment and you have no right."
                        scene w3_4208 with dissolve
                        olly "Oi, you're a broken record, aren't you?"
                        olly "I've made myself clear. I'll be back tomorrow and if she doesn't have anything for me I'm not going to be pleased."
                        scene w3_4207 with dissolve
                        mc "I got a lot of friends and we can also come by day after day."
                        scene w3_4066 with dissolve
                        olly "You don't want to play it that way."
                        scene w3_4064 with dissolve
                        mc "Don't I? You're not giving me much choice. Paying you didn't work."
                        scene w3_4065 with dissolve
                        kil "You have no idea who we work for. You ever hear of August Byrnes?"
                        scene w3_4209 with dissolve
                        olly "That supposed to mean something to me?"
                        scene w3_4065 with dissolve
                        kil "He's not the kind of guy you want to fuck with."
                        scene w3_4210 with dissolve
                        olly "*sigh* You're taking me lightly."
                        scene w3_4134 with vpunch
                        play music "music/Darkdub.ogg"
                        play sound "sound effects/thud-heavy.wav"
                        mc "Ghh-?!"
                        play sound "sound effects/punch.wav"
                        scene w3_4135 with hpunch
                        kil "--!"
                        rose "Ah, s-stop--"
                        "It was fast, it was decisive, and we practically asked for it."
                        scene w3_4136 with dissolve
                        rose "-boys!"
                        "Neither Ian or I got up, our bodies a step ahead in recognizing what our brains, wracked with panic from the sudden violence, did not."
                        olly "You understand it now, right?"
                        scene w3_4137 with dissolve
                        "If we got up, he'd hit us again."
                        scene w3_4211 with dissolve
                        olly "The two of you are pussies. Your supposed friends? I reck'n they're also pussies."
                        olly "I could take you all myself, but maybe next time I won't come alone."
                        scene w3_4212 with dissolve
                        rose "A-ahh, they didn't--"
                        olly "And you--"
                        scene w3_4138 with dissolve
                        olly "There's no worming your way out of what you owe!"
                        scene w3_4139 with dissolve
                        rose "I, ehhh- I wasn't-"
                        olly "Shut the fuck up unless you're telling me you get it!"
                        scene w3_4139 with dissolve
                        rose "I g-get it! I get it!"
                        play sound "sound effects/thud-floor.mp3"
                        scene w3_4140 with vpunch
                        rose "Gehh-"
                        olly " I swear to God. I'll break your fucking legs if you try something like this again."
                        scene w3_4141 with dissolve
                        "It was overwhelming and brokered no discussion."
                        olly "If you don't want that, you best keep paying for this cunt. You stepped in shit, boys."
                        scene w3_4142 with dissolve
                        "Well... we wanted him gone and now he was gone. If only I could {i}breath{/i}."
                        kil "Geeeuhh- what happened...?"
                        mc "*Cough, c-cough-!*"
                        mct "(Was I going to die?)"
                        rose "A-are you okay?"
                        scene w3_4143 with dissolve
                        rose "Oh, no. Oh, no. I'm sorry!"
                        mc "*Cough, cough!!!!*"
                        stop music fadeout 3.0
                        scene black with fade
                        "Once we collected ourselves, we went inside."
                        $ w3RCDoubleAssBeat = True
                        jump w3RosalindPostConfrontation

                    "{color=#696969}[[Social Chameleon] Reassure him he'll get his money.{/color}" if perk_socialChameleon == False:
                        jump w3PaidOffRoseCalmSubMenu
            "Make a stand. Under no terms is he coming back until after the competition.":

                play music "music/Darkdub.ogg"
                "...indeed, fighting was a non-option, but he smelled blood. We couldn't look like pushovers or else he'd push it further and take advantage."
                scene w3_4213 with dissolve
                mc "How are you trying to play this, asshole? You refuse to leave and then what? Going to stand around and twiddle your thumbs?"
                scene w3_4214 with dissolve
                mc "You don't think she gets the message?"
                scene w3_4215 with dissolve
                olly "Maybe this is about making sure you get the message."
                scene w3_4214 with dissolve
                mc "Stay the fuck away from Rosalind for the next week and a half, asshole."
                scene w3_4218 with dissolve
                olly "What are you going to do if I don't?"
                scene w3_4216 with dissolve
                "......"
                scene w3_4219 with dissolve
                "..."
                scene w3_4217 with dissolve
                mc "There's a lot of neighbors around. Making some noise might be more trouble than it's worth."
                scene w3_4216 with dissolve
                "The goal was giving him an out without making him feel like he was backing down. I could only hope he was as cognizant of our surroundings as I was."
                scene w3_4218 with dissolve
                olly "In my experience, neighbors tend to keep their nose out of it, but maybe you're right. There's nothing productive about this."
                olly "I'll leave now, but maybe I'll come back tomorrow, and the day after, and then the day after that. Just to keep the fire lit under your ass and keep your wallet open, geddit?"
                scene w3_4216 with dissolve
                "Good."
                scene w3_4220 with dissolve
                mc "Message received. Let's go talk about what she owes."
                "All we needed was for him to leave right now and then we could figure out the rest later."
                scene w3_4221 with dissolve
                olly "After you."
                scene w3_4222 with dissolve
                mc "...hey, Rose. It was just him, right?"
                scene w3_4223 with dissolve
                rose "Yeah... he came alone."
                scene w3_4224 with dissolve
                mc "...stay here."
                scene w3_4225 with dissolve
                kil "I don't think that's a good idea."
                scene w3_4224 with dissolve
                mc "I won't be long. Just keep an eye on both of us from here."
                scene w3_4225 with dissolve
                kil "...got it."
                scene w3_4226 with dissolve
                olly "So, what are you? In love?"
                mc "Are you trying to talk me out of paying for her?"
                scene w3_4227 with dissolve
                olly "Your body language didn't say it. Your response was measured, too put together... especially for a kid."
                mc "You don't have to worry. I care enough to pay you."
                scene w3_4228 with dissolve
                olly "..."
                "{i}Shit{/i}."
                play music "music/Darkdub.ogg"
                play sound "sound effects/thud-heavy.wav"
                scene w3_4157 with hpunch
                mc "-Ghhk!"
                "In a flash, the loan shark had me pinned and breathless, weight bearing down from his tree trunk-like forearms and threatening to snap my neck."
                kil "G-et off him!"
                scene w3_4158 with dissolve
                "Ian called out, but thankfully, he had enough sense not to move. If the large man wanted, he could have me choked out before my friend closed the distance."
                kil "I said, get the fuck off him, asshole!"
                scene w3_4159 with dissolve
                "Ian tried again, but got no response in return. Instead, Oliver and I were doing all the communicating necessary."
                scene w3_4160 with dissolve
                "After all, the look on the mean man's face told me everything he had to say."
                "It showcased the outcome of fucking with him and told me how lucky I was that this was the end of it."
                mc "Ghhhk- yhhh-"
                scene w3_4161 with dissolve
                "I did my best not to panic and waste the little air I had left in my lungs, but as time passed I felt myself get dizzy-headed."
                mc "Ghh, hhk-!"
                mct "(W-wait, was this the end of it, he's not really going to--!)"
                scene w3_4162 with dissolve
                "That's when the panic set in. He was really going to choke me out."
                mc "Hhhak, hhhg...!"
                mct "(D-damn it, I get IT, you p-prick! Just-!)"
                scene w3_4163 with dissolve
                mc "*Cough* Gauhh- hhhaa..!"
                olly "Remember this."
                scene w3_4164 with dissolve
                olly "I'm guessin' I might see you around."
                scene w3_4165 with dissolve
                rose "[mcf]! Are you okay?"
                kil "Goddamn it, bro. I didn't know what to do. Like, like--"
                mc "It's cool, I'm fine, don't worry about it..."
                stop music fadeout 3.0
                scene black with fade
                mc "Let's just get inside. We need to talk."
                $ w3RCThreatened = True
                jump w3RosalindPostConfrontation

label w3RosalindPostConfrontation:

    play music "music/called-upon.ogg"
    scene w3_4229 with w24
    show screen textbox2 with dissolve

    if w3RCKnockout == True:
        kil "Shit man, you sure you're okay?"
        "What came after being laid out was more a vague impression rather than a recollection of events that I could say I experienced firsthand. I recalled a sharp pain, the strength in my legs giving out, and the plodding of my friend's feet as he rushed down the hallway."
        mc "Yeah, no... no need for a hospital, man. I just... ughh..."
        scene w3_4230 with dissolve
        "As Ian explained to me after he helped me up and we had hobbled into the apartment, Rose had defused the situation by tactfully deploying one of a woman's strongest weapons: a sharp, frightful scream. A move that very well saved my friend from getting his ass beat, although he probably wouldn't admit it."
        scene w3_4231 with fade
        mc "So, that was pretty uncool of me huh?"
        scene w3_4232 with dissolve
        kil "What are you talking about? You got--"
        scene w3_4280 with dissolve
        mc "A-ahk-"
        "It stung, but Rosalind's kind smile was a suitable salve."
        rose "Shut up. I..."
        scene w3_4233 with dissolve
        rose "I appreciate you two checking in on me. I really do."
        rose "Although, he's definitely going to come back in a worse mood, so I kinda wish you didn't."
        "Well, at least she was being honest."

    if w3RCDoubleAssBeat == True:
        kil "Uhg, that wasn't our best showing..."
        mc "{size=-5}Tell me about it...{/size}"
        "Thankfully, I hadn't died, but talking after getting punched in the throat proved a painful prospect."
        "There were no two ways of splitting it: we got completely trounced and we were now nursing our wounds in Rosalind's living room."
        scene w3_4230 with dissolve
        kil "If he didn't sucker--"
        mc "Nooohh you {size=-5}wouldn't have.{/size}"
        scene w3_4231 with fade
        rose "Here you go, boys."
        "It was absurd, but I felt embarrassed that Rosalind saw me get completely demolished."
        scene w3_4232 with dissolve
        rose "Are you two...?"
        mc "Yeah. Rather wounded pride than a crushed trachea, right?"
        scene w3_4233 with dissolve
        rose "Thank you both for checking in on me. I appreciate it, although..."
        rose "Although, I think it might've made things worse. He's going to come back in a worse mood."

    if w3RCTussled == True:
        kil "What a fucking asshole. Acts like he's tough and then he sucker punches you?!"
        mc "You know we got lucky. That could have easily gone a lot worse."
        "On the face of it, it ended in a draw, but that guy completely handled us. He took our advantage and unraveled it in seconds."
        scene w3_4230 with dissolve
        kil "You don't know that."
        mc "He blocked your kick without even looking at you!"
        scene w3_4231 with fade
        rose "Here you go, boys."
        mc "Sorry about causing a scene with your neighbor."
        scene w3_4232 with dissolve
        rose "Ah, it's okay... I'm thankful for you two checking up on me."
        kil "What fucking timing we had, huh?"
        scene w3_4233 with dissolve
        rose "Hehe, yeah..."
        rose "Although, I kinda wish you didn't. He's going to come back in a worse mood."

    if w3RCSuckerPunched == True:
        kil "What a fucking asshole. Acts like he's tough and then--"
        mc "He would've kicked our ass, dude. I was trying to avoid that."
        scene w3_4230 with dissolve
        "Sure, my pride was a little hurt too, but better than a broken cheekbone."
        kil "I could've taken him!"
        mc "I saved you from an ass beating, dude."
        scene w3_4231 with fade
        rose "Here you go boys."
        mc "Thanks."
        scene w3_4232 with dissolve
        rose "No, thank you. I was shocked to see you, but I do appreciate you checking up on me. Only..."
        kil "Only what?"
        scene w3_4233 with dissolve
        rose "Only I wish that you hadn't. I think it might've made things worse. He's going to come back in a worse mood."


    if w3RCThreatened == True:
        kil "I would've done something, but--"
        mc "I told you, it's cool. Stop talking about it."
        "All things considered, it ending at him threatening me wasn't the worst outcome. I'd much rather that than a cracked skull or a broken leg."
        scene w3_4230 with dissolve
        kil "Cheap son of a bitch..."
        scene w3_4231 with fade
        rose "Here you go boys."
        mc "Thank you."
        scene w3_4232 with dissolve
        rose "No, thank you for showing up. I appreciate you checking on me."
        mc "Like I said, I had a feeling something was wrong."
        scene w3_4233 with dissolve
        rose "I kinda wished you didn't though. He's going to come back in a worse mood."


    if w3RCTalkedDown == True:
        "After bullshitting our way out of a confrontation, the big question of what to do now loomed overhead."
        kil "What a fucking asshole."
        scene w3_4230 with dissolve
        "The answers that came to mind were relatively obvious, but unpleasant."
        mc "You said it..."
        scene w3_4231 with fade
        rose "Here you go boys."
        rose "Sorry about lying to you at the door, I--"
        scene w3_4232 with dissolve
        mc "It's understandable."
        rose "I'm glad you two showed up. Thanks for that."
        scene w3_4233 with dissolve
        kil "Don't mention it. [mcf] got one of his nagging feelings is all."
        rose "I'm glad, but I'm also... {b}not{/b}. I kinda wish you didn't. He's going to come back in a worse mood."


    scene w3_4234 with dissolve
    kil "Well, fuck you too."
    rose "Don't be crass. I didn't mean it that way. I really do--"
    scene w3_4235 with dissolve
    mc "{b}Sit down.{/b}"
    scene w3_4236 with fade
    "Rosalind, true to fashion, obediently did as I asked."
    "I hadn't meant it to come out so commanding, but I tended to be terse when there's a problem at hand."
    mc "You alright?"
    scene w3_4237 with dissolve
    rose "This whole year is going to be one I'll never forget."
    scene w3_4238 with dissolve
    "Right, even if this was at the root of everything, dealing with harassment was just one ingredient in a whole shit sandwich."
    scene w3_4239 with dissolve
    mc "Did he hurt you in any way before we got here?"
    scene w3_4237 with dissolve
    rose "Not really... he just--"
    scene w3_4238 with dissolve
    "Rosalind stopped herself as if weighing just how much of the truth she should share."
    scene w3_4239 with dissolve
    mc "Be honest."
    scene w3_4238 with dissolve
    "Another command, but I needed the full picture before deciding on our course of action."
    scene w3_4240 with dissolve
    rose "...he just knocked me down a couple of times, shouting about how I was wasting his time and how I should just let his associates put me to work."
    mc "...and you don't want to do that?"
    "Normally it would be a stupid question, but considering how she was currently trying to get the money..."
    scene w3_4241 with dissolve
    rose "Of course not! There's no telling how long it would take me to pay him back or if they'd even let me go, it's just too... well..."
    scene w3_4242 with dissolve
    mc "Say no more, I get it."
    "Although, if she doesn't win the exhibition, that might just be her future anyway."
    scene w3_4243 with dissolve
    mc "...I'll take care of this..."
    scene w3_4245 with dissolve
    rose "Not that I don't believe you, but..."
    scene w3_4243 with dissolve
    mc "I know. I thought we had gotten him out of your hair too, but evidently we will need to be more drastic."
    scene w3_4244 with dissolve
    mct "(Was I seriously considering...?)"

    if rosalindAugSolution == True:
        "This morning I was in a tizzy about the people surrounding me, and now I was seriously thinking about just how easily someone like Warren or Jacob could get that asshole to extend the professional courtesy August spoke of."
    else:
        "This morning I was in a tizzy about the people surrounding me, and now I was seriously thinking about just how easily someone like Warren or Jacob could break that asshole's legs..."

    scene w3_4246 with dissolve
    rose "I don't know... I think you might make it worse..."
    scene w3_4247 with dissolve
    kil "When [mcf] says something will be taken care of, it'll be taken care of."
    "Ian, who had been quiet up to this point, picked now to interject."
    "I felt his confidence in me misplaced, but truth be told, I welcomed it right now."
    scene w3_4246 with dissolve
    rose "I don't know, I think I can endure him coming around for another two weeks..."
    rose "It might be better to leave things be..."
    scene w3_4250 with dissolve
    mc " A line has to be drawn."
    scene w3_4249 with dissolve
    mc "Him being here today is proof of that. He knows your husband ran off and he's going to make sure you're cornered."
    scene w3_4248 with dissolve
    "She did have a point though. Further meddling will just agitate him, meaning the club's next move would have to be decisive."
    scene w3_4250 with dissolve
    mc "How would you feel if the club bought your debt? Does who you owe make a difference to you?"
    scene w3_4251 with dissolve
    "I mean, isn't that something the club should've done in the first place? It would greatly simplify things while also potentially lining up a new star house girl coming hot off a failed exhibition."
    rose "You mean... I'd owe the club instead of Oliver?"
    scene w3_4250 with dissolve
    mc "I don't know about the kind of work he'd put you up to, but at least the club is a known quantity. If you lose the exhibition and had to work there after the--"
    scene w3_4251 with dissolve
    rose "I don't want that. I couldn't keep the charade up with Nora... I need this to be over with this month."

    if rosalindKatSolution == True:
        scene w3_4248 with dissolve
        "She was already in debt to the club for the five thousand Kathleen gave her, but there was no point in mentioning that right now."

    scene w3_4249 with dissolve
    mc "You might not have a choice in the matter."
    scene w3_4248 with dissolve
    "No matter if this got solved fiscally or {b}otherwise{/b}, I was pretty sure the end result would be the same: Rosalind {i}will{/i} owe the club."
    scene w3_4252 with dissolve
    rose "By the way..."
    "Maybe that was the inevitable underlining to this whole thing. I saw it happen with Lucy, after all; she had lost, but the club still extended its claws."
    rose "I like your new hairstyle."
    scene w3_4253 with dissolve
    mc "H-huh...?"
    rose "You've been looking kinda scary since we got into the apartment. I just wanted to say something nice."
    scene w3_4254 with dissolve
    mc "Oh, uh... thanks."
    rose "You too. You look nice, Ian."
    scene w3_4255 with dissolve
    kil "Aw, she's coming on to me. See that, [mcf]?"
    rose "...do you want me to make you something to eat?"
    "It was like she went into mothering mode to diffuse the tension."
    scene w3_4256 with dissolve
    rose "It's the least I can do for my two heroes."
    mc "You mean your pimps?"
    scene w3_4257 with dissolve
    rose "No... I know I didn't sound grateful, but it is nice {i}someone{/i} checked in. And even if it's your job..."
    scene w3_4258 with dissolve
    rose "You were cool. And things like that, in tough situations, become a relief."

    if w3RCKnockout == True:
        mct "(Cool? I got my ass beat...)"
    elif w3RCDoubleAssBeat == True:
        mct "(Cool? We got our ass beat...)"
    elif w3RCSuckerPunched == True:
        mct "(Cool? All I did was get sucker punched...)"

    scene w3_4257 with dissolve
    rose "So, it's not much, but how about some lunch?"

    if rosalindKilSolution == True:
        scene w3_4259 with dissolve
        kil "I can think of something I'd like to eat."
        scene w3_4260 with dissolve
        rose "W-whaa...?"
        kil "Remember that threesome we have set up? I do believe you still owe us a good time, Mrs. Carter."
        rose "Ah, o-oh, y-yeah... do you two want to--"
        scene w3_4261 with dissolve
        kil "--is something I'd like to say, but now's not really the right mood, is it?"
        rose "O-oh..."
        mc "You asshole. You should have seen her face."
        scene w3_4262 with dissolve
        kil "She just looks mad."
        scene w3_4263 with dissolve
        rose "I about jumped out of my skin."
        mc "He has that effect on women."
        "In his own way, Ian had lightened the mood."
        scene w3_4264 with dissolve
        rose "I mean... it's got to happen sometime, right...?"
        scene w3_4265 with dissolve
        mc "Like my friend said, now's not the time."
        scene w3_4266 with dissolve
        kil "For the price I paid, you got to make it special. For one, you're not going to wear some crummy old rags."
        scene w3_4265 with dissolve
        mc "It's more like we have other things to deal with right now. Get your things."
        scene w3_4267 with dissolve
        rose "My things...?"
        scene w3_4265 with dissolve
        mc "You're going to stay at my place for the time being."
        "Yet another command, but I wasn't going to leave her room to refuse."
        scene w3_4268 with dissolve
        rose "I can't just... don't you think that's... he's going to think I--"
        scene w3_4269 with dissolve
        rose "........."
        mc "......"
        scene w3_4270 with dissolve
        rose "...I understand."
        scene w3_4271 with dissolve
        mc "Good, Ian and I will clean up while you do. Wouldn't want to leave your home in a mess, right?"
        rose "Right!"
    else:

        scene w3_4272 with dissolve
        mc "We'll pass."
        kil "Eh? I'm kinda hungry..."
        scene w3_4273 with dissolve
        mc "You'll live. Right now..."
        scene w3_4274 with dissolve
        mc "You should get your things instead. You're going to stay at my place for the time being."
        scene w3_4275 with dissolve
        "Yet another command, but I wasn't going to leave her room to refuse."
        scene w3_4276 with dissolve
        rose "I can't just... don't you think that's... he's going to think I--"
        scene w3_4275 with dissolve
        rose "........."
        mc "......"
        scene w3_4277 with dissolve
        rose "...I understand."
        scene w3_4278 with dissolve
        mc "Good, Ian and I will clean up while you do. Wouldn't want to leave your home in a mess, right?"
        rose "Right!"

    stop music fadeout 3.0
    scene black with fade
    "After reiterating to Rosalind that things would turn out okay and that I would keep a handle on the Oliver situation. We cleaned and packed and--"
    scene w3_4279 with cmet
    $ history_rosalind = "Rosalind will be staying with me for awhile, until her troubles get sorted out."
    $ unread_rosalind = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "Got comfortable with my place, left a key, and then--"
    play ambient "sound effects/city-night.wav"
    scene w3_4330 with circlewipe
    "It was time to see what could be done. Ian had some stuff to take care of, which was fine and dandy, as part of me preferred tackling this alone."
    stop ambient fadeout 3.0
    scene w3_4331 with blinds
    "The way I saw it, it was either pay him off completely or scare him, neither of which I was equipped to do, but maybe the bosses had a better idea."
    scene w3_4332 with dissolve
    "However, the decision of who to bring it up to was made for me."
    scene black with fade

    if kat_polite == True:
        "Mrs. Pulman was out and both August and Chuck were in the VIP room..."
    else:
        "Kathleen was out and both August and Chuck were in the VIP room..."

    play music "music/i-knew-a-guy.ogg"
    scene w3_4333 with dissolve
    mct "(...this place has a monthly poker game?)"
    "That seemed almost quaint. There were only a couple of house girls milling about by the bar and neither was engaged in coitus."
    chuck "Aha, lad! Impeccable timing! We're down a man."
    scene w3_4334 with dissolve
    "I quickly took stock of the room. There was the tenor, the chief of police, and Warren."
    mct "(The chief of police, huh...?)"
    scene w3_4335 with dissolve
    jim "Yeah, sit down! I'm tired of losing to this goddamn cheat."
    mc "I actually came here because I had a problem with one of the Carnations that needs to be solved."
    scene w3_4336 with dissolve
    chuck "Sit down."
    "Not one to be refused, my former mentor insisted."
    chuck "It's not so urgent that you need to bother us during our card game, is it?"
    "My gut reaction was to say that a card game wasn't important, but that would be an intensely foolish observation. These men had their priorities and the problems of a whore weren't very high on it."
    scene w3_4337 with dissolve
    aug "He can speak about it if he wants."
    "Well, except for maybe August, but the Carnations weren't exactly his purview either."
    scene w3_4338 with dissolve
    chuck "It's not like anyone's about to die, surely?"
    scene w3_4339 with dissolve
    mc "I don't like to gamble."
    scene w3_4338 with dissolve
    chuck "Call it an exercise in managing risk then, lad. Either way, sit down."
    scene w3_4340 with dissolve
    "Dr. Chuck seemed insistent, but August seemed open to talking. The question was, business first or later? And was getting both their inputs better than just one?"

    hide screen textbox2 with dissolve
    menu:
        "Business first. Ask August to talk privately(w3RosalindViolentSolution = True)."(chg=["august_up","chuck_down"]):
            $ August_Friendship += 1
            $ Chuck_Friendship -= 1
            $ w3RosalindViolentSolution = True

            scene w3_4341 with dissolve
            show screen textbox2 with dissolve
            mc "Can I talk to you for a second? Privately?"
            "There was no need to air the dirty laundry in front of the patrons, but I wanted to fill him in all the same."
            scene w3_4342 with dissolve
            mc "Just by the bar. It won't take long."
            aug "...sure."
            scene black with fade
            aug "You guys give us a sec, huh?"
            scene w3_4343 with dissolve
            mc "I didn't want to bring this up in front of the patrons."
            scene w3_4344 with dissolve
            aug "I appreciate that. So, what's this about?"

            if rosalindAugSolution == True:
                scene w3_4343 with dissolve
                mc "Ian and I had a run-in with that loan shark you told off."
                scene w3_4344 with dissolve
                aug "A run-in, eh? You bump elbows?"
                scene w3_4345 with dissolve

                if w3RCKnockout == True:
                    mc "Something like that. He actually got a couple of good ones in and kicked my ass."
                elif w3RCDoubleAssBeat == True:
                    mc "He put both of us on our ass. {b}Hard.{/b}"
                elif w3RCTussled == True:
                    mc "It got a bit dicey. We barely escaped an ass-kicking."
                elif w3RCSuckerPunched == True:
                    mc "I got sucker-punched for my trouble."
                else:
                    mc "He was pretty {b}emphatic{/b} about telling you to fuck off or pay him."

                mc "Basically, he doesn't think you're shit."
                scene w3_4346 with dissolve
                "I knew what I was doing. I was trying to get the man's pride involved."
                scene w3_4347 with dissolve
                aug "The man's running a business. Try not to take it personally; that's my job."
                scene w3_4348 with dissolve
                "...that wasn't quite the reaction I was expecting, but it was a reminder that he's been around the block a time or two before."
                mc "I'm not. But you did assure me you'd get him to stop bothering Rosalind."
                scene w3_4350 with dissolve
                aug "To be honest, I kinda expected he wouldn't."
                scene w3_4351 with dissolve
                mc "Really? You seemed pretty--"
                scene w3_4349 with dissolve
                aug "You got to try asking nicely first, understood?"
                scene w3_4348 with dissolve
                mc "I see..."
                "So, he anticipated this?"
                scene w3_4350 with dissolve
                aug "After that, you don't have to ask so nice."
                scene w3_4351 with dissolve
                "I didn't want to know the details, but I did have a relevant question."
                scene w3_4352 with dissolve
                mc "Won't getting aggressive with him just make things more difficult for Rose?"
                scene w3_4349 with dissolve
                aug "Jacob can be pretty convincing when he sets his mind to it. I think you'll find that asshole a lot more agreeable."
                scene w3_4353 with dissolve
                aug "*sigh* Kathleen should've taken care of this from the start, but you see... she likes problems like these."
                scene w3_4352 with dissolve
                mc "Do I have your guarantee?"
                scene w3_4354 with dissolve
                aug "You never had anything to worry about."
            else:

                scene w3_4343 with dissolve
                mc "Ian and I had a run-in with Rosalind's loan shark."
                scene w3_4344 with dissolve
                aug "...you good?"
                scene w3_4345 with dissolve

                if w3RCKnockout == True:
                    mc "He kicked my ass."
                elif w3RCDoubleAssBeat == True:
                    mc "He put both of us on our ass. {b}Hard.{/b}"
                elif w3RCTussled == True:
                    mc "It got a bit dicey. We barely escaped an ass-kicking."
                elif w3RCSuckerPunched == True:
                    mc "I got sucker-punched for my trouble."
                else:
                    mc "Nothing worth complaining about, but he wasn't friendly."

                scene w3_4355 with dissolve
                aug "Goddamn it, Kathy knows better to take care of these things before her little show even begins."
                scene w3_4348 with dissolve
                mc "The thing is, we paid him enough to put her ahead a couple of weeks, so the exhibition won't have any problems, but--"
                scene w3_4349 with dissolve
                aug "He saw an open wallet and is taking you for a sucker."
                scene w3_4348 with dissolve
                mc "Precisely."
                scene w3_4350 with dissolve
                aug "That's good business sense in that line of work."
                scene w3_4351 with dissolve
                mc "Until everything's settled, he's going to ramp up the harassment. I'm coming to you about this, because, well..."
                scene w3_4350 with dissolve
                aug "I'll have Jacob handle it."
                scene w3_4351 with dissolve
                "I didn't want to know the details, but I did have a relevant question."
                scene w3_4352 with dissolve
                mc "Won't getting aggressive with him just make things more difficult for Rose?"
                scene w3_4350 with dissolve
                aug "He'll get the message across. I think you'll find him a lot less greedy."
                scene w3_4351 with dissolve
                mc "Simple as that?"
                scene w3_4354 with dissolve
                aug "Simple as that."


            scene w3_4356 with dissolve
            mc "......"
            "Business was done, but..."
            scene w3_4357 with dissolve
            chuck "You coming over, lad? We're still down a man."
            "{i}It would be the appropriate move to play a few hands.{/i}"
            scene w3_4358 with dissolve
            mc "You going to comp me enough to play?"
            chuck "Bahaha, I know what you get paid. You can afford the buy-in."
            scene w3_4359 with fade
            mc "Just trying to manage risk."
            scene w3_4360 with dissolve
            chuck "Deal him in."
            scene w3_4361 with dissolve
            war "Fresh meat."
            scene w3_4362 with dissolve
            "So we played. Playing conservatively didn't seem to work."
            jim "Ahaha, finally!"
            scene w3_4363 with circlewipe
            "Playing aggressively got me walked all over."
            war "It's not your lucky day."
            scene w3_4364 with ccirclewipe
            "Soon, my competitive edge was whet, and I got lost in the moment - putting aside the business at hand and focusing wholeheartedly on a game I had no hope of winning."
            mc "I raise!"
            scene w3_4365 with vpunch
            mc "Ah, shit."
            vinc "You lose some, you lose some."
            "...it just dawned on me, I had never played poker in my life, Texas Hold'em or otherwise."
            scene w3_4366 with dissolve
            "The downside of a single mother, I guess."
            jim "What's so amusing?"
            scene w3_4367 with dissolve
            mc "I think I'm getting the hang of this."
            "There was a social currency involved here that outvalued dollars and it would be foolish not to avail myself to it."
            scene black with fade
            stop music fadeout 3.0
            mc "Let me buy back in."
            "........."
            "......"
            "..."
            jump w3BackToRosalind
        "Sit down."(chg=["chuck_up"]):


            $ Chuck_Friendship += 1
            show screen textbox2 with dissolve

    "Part of me wanted to note that not playing {i}was{/i} managing risk, but that would be another foolish observation. There was a social currency involved here that outvalued dollars."
    scene w3_4368 with dissolve
    mc "What's the buy-in?"
    "...and refusing Dr. Chuck thrice, would run detrimental to my goal of getting someone with a bigger stick than me to solve the problem. "
    chuck "You can afford it. I've seen your paycheck."
    scene w3_4369 with fade
    "........."
    "......"
    scene w3_4370 with dissolve
    mc "...deal me in."
    scene black with fade
    "So we played a few hands."
    scene w3_4362 with dissolve
    "I played conservatively and gained no ground."
    jim "Ahaha, finally!"
    scene w3_4363 with circlewipe
    "I played aggressively and got walked all over."
    war "It's not your lucky day."
    scene w3_4364 with ccirclewipe
    "Soon, my competitive edge was whet, and I got lost in the moment - putting aside the business at hand and focusing wholeheartedly on a game I had no hope of winning."
    mc "I raise!"
    scene w3_4365 with dissolve
    "Eventually, when I had felt like I had paid the toll and had earned the acceptance of the room..."

    if rosalindAugSolution == True:
        scene w3_4371 with dissolve
        mc "By the way, that loan shark didn't do as you asked."
        "I moved onto why I was here."
        scene w3_4372 with dissolve
        aug "Oh...?"
        "The old man looked lost in thought, as if trying to pinpoint exactly what I was talking about."
        scene w3_4373 with dissolve
        aug "Ah, that was what was likely to happen. No self-respecting man shows his belly without good reason. I'll take the next step."
        scene w3_4374 with dissolve
        mc "...and what's the next step?"
        scene w3_4375 with dissolve
        aug "Giving him a good reason."
        scene w3_4376 with dissolve
        "While I understood there was a natural escalation, I couldn't help but feel like paying him off would've been preferable to a protracted dick-measuring contest."
        "I was burned once by his reassurance and I wanted this to be the end of it..."
        hide screen textbox2 with dissolve

        menu:
            "Try to rile August up(w3RosalindViolentSolution=True)."(chg=["august_down","warren_up"]):

                $ August_Friendship -= 1
                $ Warren_Friendship += 1
                $ w3RosalindViolentSolution = True

                scene w3_4377 with dissolve
                show screen textbox2 with dissolve
                mc "I hope you'll take care of it. That loan shark acted like you weren't shit."
                scene w3_4378 with dissolve
                war "Ha! Just came out and said it."
                "I knew what I was doing, in front of Chuck and the other patrons, I was trying to twist the old man's pride to my ends."
                scene w3_4377 with dissolve
                mc "I'm not the one who said it. All I'm saying is Ian and I had a run-in with the prick. It wasn't very friendly."
                scene w3_4379 with dissolve
                chuck "A run-in...? He didn't threaten you, did he?"
                scene w3_4380 with dissolve
                "Suddenly, Dr. Chuck seemed a lot more interested in the problem."

                if w3RCKnockout == True:
                    mc "Actually, he got a couple of good ones in and I got my ass kicked. He was pretty emphatic in telling you to fuck off or pay him."
                elif w3RCDoubleAssBeat == True:
                    mc "He sucker punched both of us and put us on our ass. He was pretty emphatic in telling you to fuck off or pay him."
                elif w3RCTussled == True:
                    mc "It got a bit dicey. We barely escaped an ass-kicking. He was pretty emphatic in telling you to fuck off or pay him."
                elif w3RCSuckerPunched == True:
                    mc "I got sucker-punched for my trouble. He was pretty emphatic in telling you to fuck off or pay him."
                else:
                    mc "He was pretty {b}emphatic{/b} about telling you to fuck off or pay him."

                scene w3_4381 with dissolve
                chuck "You should've started with that from the moment you walked in the door."
                scene w3_4382 with dissolve
                chuck "You allowed this to happen?"
                scene w3_4383 with dissolve
                aug "You don't need to fuss like an over-protective parent, you know men get into tussles sometimes. Hell, I remember your Army days, Charles."
                scene w3_4384 with dissolve
                chuck "That was different. It was all in good fun, and when it wasn't, we took care of our own."
                scene w3_4385 with dissolve
                aug "And I will take care of it, with provocation on my side."
                "August looked a little unhappy."
                scene w3_4386 with dissolve
                aug "It's not like I expected the boys to have a dust-up over this, and even if I did, I can't just send Jacob to have a discussion with the man without good reason."
                scene w3_4384 with dissolve
                chuck "Make sure you do. I don't like people putting hands on what's mine, but I'm leaving this up to you since your nose is already in it."

                if w3RCTalkedDown == True:
                    "He didn't actually touch us, but it was to my benefit not to dispute that..."

                scene w3_4387 with dissolve
                aug "Kathy should anticipate these kinds of problems and plan for them accordingly, instead of leaving it to me and [mcf] to solve. She should've settled the account before the show even began."
                scene w3_4388 with dissolve
                chuck "Perhaps, but you know exactly why she didn't and {i}we{/i} tolerate those proclivities because we're family."
                scene w3_4389 with dissolve
                mc "So, I have your assurance that Rosalind won't have anyone beating down her door for awhile?"
                scene w3_4390 with dissolve
                aug "Give it a few days."
                scene w3_4391 with dissolve
                "I didn't want to know the details, but I did have a relevant question."
                scene w3_4392 with dissolve
                mc "Won't getting aggressive with him just make things more difficult for Rose?"
                scene w3_4393 with dissolve
                aug "Jacob and Warren can be pretty persuasive when they need to."
                scene w3_4394 with dissolve
                war "We work real nice together."
                "...there I had it. What was hopefully the end of this matter."
                scene w3_4393 with dissolve
                aug "It won't blow back on Rose, I can assure you of that. All you'll find is that asshole will become a lot more agreeable."
                scene w3_4395 with dissolve
                mc "......"
                scene black with fade
                stop music fadeout 3.0
                mc "...what are we waiting for, let's keep playing."
                "........."
                "......"
                "..."
                jump w3BackToRosalind
            "Suggest the club buys the debt and simply be done with it(w3RosalindConnectionSolution = True)"(chg=["chuck_up"]):

                $ w3RosalindConnectionSolution = True
                $ Chuck_Friendship += 1
                scene w3_4377 with dissolve
                show screen textbox2 with dissolve
                mc "...wouldn't it be easiest to just buy the debt? If she wins the exhibition, it's cleared all the same. If she loses, she can owe the club."
                scene w3_4396 with dissolve
                aug "That's what Kathy should've done from the onset, but now I'm handling it, eh?"
                scene w3_4377 with dissolve
                mc "I just think that would be the quickest and least likely option to impede the exhibition."
                scene w3_4396 with dissolve
                mct "(...and it would mean Rosalind wouldn't have to see him tomorrow, and the next day, and the next day.)"
                aug "He ignored my request."
                scene w3_4397 with dissolve
                "Part of me wanted to say \"so, what?\", but that was the third stupid thing to cross my mind."
                scene w3_4398 with dissolve

                if w2KillianRoseOffer == True:
                    chuck "...this about that thing with the sad-looking lass?"
                    scene w3_4399 with dissolve
                    "...the one you didn't want to have anything to do with?"
                    mc "That's the one."
                else:
                    chuck "...what's this about?"
                    scene w3_4399 with dissolve
                    mc "One of the Carnations is having trouble with her personal circumstances."

                scene w3_4400 with dissolve
                chuck "You know I'm not a fan of the way you handle things, Augie."
                scene w3_4386 with dissolve
                aug "I would sooner not clean up someone's mess, but it is perpetually left up to me. Despite being equipped to do it, neither of you ever seem to want to."
                scene w3_4400 with dissolve
                chuck "You're not the same young man you were anymore. You should think outside the box, in a way befitting the company you now keep."
                scene w3_4401 with dissolve
                aug "What do you mean...?"
                scene w3_4402 with dissolve
                aug "I'm still surrounded by crooks, aren't I? The only difference is the company I used to keep was a lot more honest."
                chuck "Baha! You fuck!"
                scene w3_4403 with dissolve
                "He looked at Jim when he said that, but I had a feeling he meant Dr. Chuck too."
                jim "Fuck you, bottom feeder."
                scene w3_4404 with dissolve
                chuck "This man's a loan shark?"
                scene w3_4401 with dissolve
                aug "It's a small operation."
                scene w3_4400 with dissolve
                chuck "That must mean he's into some other things too, yeah? Prostitution, money laundering, stuff like that?"
                scene w3_4401 with dissolve
                aug "More or less."
                scene w3_4405 with dissolve
                chuck "My, my, my... sounds like you've been derelict in your duties, Jim. How can you be sitting here playing cards while criminals are proliferating in the street?"
                scene w3_4406 with dissolve
                jim "........."
                chuck "......"
                scene w3_4407 with dissolve
                jim "...yeah, alright. I'll take care of it."
                scene w3_4408 with dissolve
                mct "(...what? It was that simple? The thought had crossed my mind when I entered the room, but--)"
                aug "You really going to ruin a businessman's livelihood for no good reason like that?"
                scene w3_4409 with dissolve
                chuck "He ignored your request."
                scene w3_4410 with dissolve
                jim "I'll let you know when it's handled. It may be a day or two."
                chuck "That's fine."
                scene w3_4411 with dissolve
                mc "...what happens to Rosalind's debt? If he goes to jail, isn't she..."
                scene w3_4412 with dissolve
                chuck "Don't know. We'll just have to see how well she does these next two weeks."
                scene w3_4413 with dissolve
                aug "*Sigh* Kathy sure does like watching the gears turn."
                chuck "She keeps it interesting."
                "With just a request that sounded more like an order, he got the city's police chief to take care of something that Dr. Chuck didn't even care about."
                mct "(...he's just showing off, isn't he?)"
                scene w3_4414 with dissolve
                mc "...what are we waiting for, let's keep playing."
                scene black with fade
                stop music fadeout 3.0
                "I was starting to see the enormity of the people I was surrounded by."
                "........."
                "......"
                "..."
                jump w3BackToRosalind
    else:

        scene w3_4371 with dissolve
        mc "By the way, I had a run-in with Rosalind's loan shark."
        scene w3_4372 with dissolve
        aug "Is that right...?"
        scene w3_4371 with dissolve
        mc "Yeah, me and Ian, to be exact. It wasn't very friendly and he made a lot of threats."

        if rosalindFelSolution == True or rosalindKilSolution == True:
            mc "You see we paid him off in advance for a few weeks, but he just--"
            scene w3_4415 with dissolve
            aug "Took you for a sucker."

        if rosalindKatSolution == True or rosalindKatSolutionFree == True:
            mc "Kathleen paid him a few weeks in advance, but he hasn't let up. In fact, it made it worse. He--"
            scene w3_4415 with dissolve
            aug "He took you for a sucker?"

        scene w3_4416 with dissolve
        mc "Exactly."
        scene w3_4417 with dissolve
        chuck "...were you guys hurt?"
        scene w3_4418 with dissolve

        if w3RCKnockout == True:
            mc "I got my ass beat."
        elif w3RCDoubleAssBeat == True:
            mc "Ian and I got our asses handed to us."
        elif w3RCTussled == True:
            mc "It got a bit dicey. We barely escaped an ass-kicking."
        elif w3RCSuckerPunched == True:
            mc "Not really, but I got sucker-punched for my trouble."
        else:
            mc "All I'll say is he was pretty {b}emphatic{/b} about making sure we keep paying."

        scene w3_4419 with dissolve
        chuck "...I don't like that."

        if w2KillianRoseOffer == True:
            "I internally scoffed at Dr. Chuck's change in concern, given he refused to help earlier, but I was also thankful that this got his interest."

        scene w3_4420 with dissolve
        aug "*Sigh* Kathleen should've settled the account in the first place. Fickle bitch."
        chuck "Be that as it may, he needs to be taken care of. He put his hands on one of ours."

        if w3RCTalkedDown == True:
            "He didn't actually touch us, but it was to my benefit not to dispute that..."

        scene w3_4421 with dissolve
        aug "I'll handle it like usual."
        chuck "The thing is your usual way is unimaginative and dull, and unbefitting of the company you now keep."
        scene w3_4396 with dissolve
        aug "Well, I'm the only one who doesn't sit on their ass around here. It doesn't really matter how you do it if he never threatens the boys again, eh?"
        scene w3_4376 with dissolve
        "There it was: an opportunity to get things done. I had their interest, the only question was how to capitalize on it."
        hide screen textbox2 with dissolve

        menu:
            "Suggest you solve it simply and to the point(w3RosalindConnectionSolution = True)"(chg=["chuck_up"]):

                $ Chuck_Friendship += 1
                $ w3RosalindConnectionSolution = True
                scene w3_4377 with dissolve
                show screen textbox2 with dissolve
                mc "I think we should just buy out her debt; that's the simplest and most direct option."
                scene w3_4396 with dissolve
                "At the end of the day, the ultimate goal was to get Rosalind some relief."
                scene w3_4377 with dissolve
                mc "If she wins the exhibition, it's cleared all the same. If she loses, she can owe the club."
                scene w3_4398 with dissolve
                chuck "I would agree with you if he didn't disrespect my nephew and you."
                scene w3_4399 with dissolve
                mc "Like Mr. Byrnes said, he was just doing his job."
                scene w3_4398 with dissolve
                chuck "Aye, and that's his prerogative. Just as it's my own to not allow people to trample on what's mine."
                scene w3_4422 with dissolve
                mct "(I mean, at the end of the day, what did I care about how this got solved?)"
                "Killian's assurance from last night rang in my mind."
                "{i}All I'm saying is he wouldn't use violence; he's not the type. I'm one hundred percent certain of that. At worst, the person would just wish they were dead.{/i}"
                scene w3_4404 with dissolve
                chuck "This man's a loan shark?"
                scene w3_4401 with dissolve
                aug "It's a small operation."
                scene w3_4400 with dissolve
                chuck "That must mean he's into some other things too, yeah? Prostitution, money laundering, stuff like that?"
                scene w3_4401 with dissolve
                aug "More or less."
                scene w3_4423 with dissolve
                chuck "Handle it."
                scene w3_4424 with dissolve
                jim "Excuse me?"
                scene w3_4405 with dissolve
                chuck "How can you be sitting here playing cards while criminals are proliferating in the street?"
                scene w3_4406 with dissolve
                jim "........."
                chuck "......"
                scene w3_4407 with dissolve
                jim "...yeah, alright. I'll take care of it."
                scene w3_4408 with dissolve
                mct "(...what? It was that simple? The thought had crossed my mind when I entered the room, but--)"
                aug "You really going to ruin a businessman's livelihood for no good reason like that?"
                scene w3_4409 with dissolve
                chuck "I don't need a reason, but I say I have a pretty good one."
                scene w3_4408 with dissolve
                aug "I don't like bringing the cops into this."
                scene w3_4409 with dissolve
                chuck "As the drill sergeant liked to say, tough titties."
                scene w3_4408 with dissolve
                aug "...it's your call."
                scene w3_4410 with dissolve
                jim "I'll let you know when it's handled. Maybe a day or two."
                chuck "That's fine."
                scene w3_4411 with dissolve
                mc "...what happens to Rosalind's debt? If he goes to jail, isn't she..."
                scene w3_4412 with dissolve
                chuck "I guess we'll just see how the next two exhibitions go, won't we?"
                scene w3_4413 with dissolve
                "With just a request that sounded more like an order, and like paving over a mountain to get a better view, he got the city's police chief to deconstruct the entire problem."
                mct "(...he's just showing off, isn't he?)"
                scene w3_4414 with dissolve
                mc "...what are we waiting for, let's keep playing."
                scene black with fade
                stop music fadeout 3.0
                "I was starting to see the enormity of the people I was surrounded by."
                "........."
                "......"
                "..."
                jump w3BackToRosalind
            "Angle for August to handle it(w3RosalindViolentSolution = True)"(chg=["august_up","warren_up"]):

                $ August_Friendship += 1
                $ Warren_Friendship += 1
                $ w3RosalindViolentSolution = True
                scene w3_4377 with dissolve
                show screen textbox2 with dissolve
                mc "...Mr. Byrnes is right. He's not going to relent because it's his job and he has no reason to."
                scene w3_4378 with dissolve
                "We had tried paying him, but now was the time to point someone at him who could speak his language."
                scene w3_4377 with dissolve
                mc "This is your wheelhouse, right?"
                scene w3_4396 with dissolve
                aug "It's not my first rodeo."
                scene w3_4399 with dissolve
                mc "...do you think you can get him to back off?"
                scene w3_4425 with dissolve
                aug "I'll do more than that. I'll put Jacob and Warren on it."
                "I didn't really want to know the details, I just wanted the reassurance."
                aug "I think you'll find him a lot more agreeable after that."
                scene w3_4426 with dissolve
                war "Heh. Payday."
                scene w3_4401 with dissolve
                aug "Is that okay with you? As always, it's your call."
                scene w3_4422 with dissolve
                mct "(I mean, at the end of the day, what did I care about how this got solved?)"
                "Killian's assurance from last night rang in my mind."
                "{i}All I'm saying is he wouldn't use violence; he's not the type. I'm one hundred percent certain of that. At worst, the person would just wish they were dead.{/i}"
                scene w3_4404 with dissolve
                chuck "Have I mentioned how much I disdain your go-to touch? You have a lot more resources at your fingertips than you did when you were young."
                scene w3_4386 with dissolve
                aug "I'm not trying to impress anyone. I'm in the company of crooks all the same."
                scene w3_4427 with dissolve
                jim "Fuck you."
                aug "So, should I dance for Kathy?"
                scene w3_4428 with dissolve
                chuck "... *sigh* Fine. Since you speak that scumbag's language; just make sure you're as clear as a bell. Leave {i}no{/i} room for misunderstanding. I want no margin for even the dumbest mother fucker to go get ideas about hassling my nephew and [mcf] ever again."
                aug "Thy will be done, Charles."
                scene w3_4429 with dissolve
                vinc "Andrea! Get over here! The mood's getting a bit thick!"
                aug "Give it a few days, kid."
                vinc "Nothing a fat-ass redhead can't change for the better!"
                scene w3_4430 with dissolve
                mc "......"
                scene w3_4431 with dissolve
                mc "... Vincenzo's right. What are we waiting for? Let's keep playing."
                scene black with fade
                stop music fadeout 3.0
                "This was the company I now keep, despite all the mind-wringing I did earlier. At least, I could make it work for me."
                "........."
                "......"
                "..."
                jump w3BackToRosalind

label w3BackToRosalind:
    play sound "sound effects/door-openclose.wav"
    play music "music/jazz-piano-bar.ogg"
    scene w3_4432 with circlewipe
    "When I returned home, it was evident that Rosalind had been busy."
    "The rich and hearty smell of simmering meat wafted through the open door and I found the woman tucked away in the kitchen, wiping down the counter."
    mc "Hey honey, I'm home."
    scene w3_4433 with dissolve
    "A joke, but the moment her ears registered my greeting, she froze and returned a sheepish reply."
    rose "Uh... {i}heh{/i}... welcome back."
    "As if being caught red-handed doing something she wasn't supposed to be doing."
    scene w3_4434 with dissolve
    rose "It was awkward just sitting around, so I..."
    scene w3_4435 with dissolve
    mc "Good thinking. I'm starving. I haven't eaten all day."
    scene w3_4436 with dissolve
    mc "I'm sorry about just leaving you here, but as messed up as it is..."
    rose "I don't really have a say in this situation."
    scene w3_4437 with dissolve
    "Rosalind was a flower at the mercy and whims of the wind. Her husband, Oliver, the club..."
    "She landed in this situation thanks to her husband's malfeasance, and now her reins were handed off to another, all in a short span of time that she had no say over."
    scene w3_4438 with dissolve
    mc "That's gotta be frustrating, huh?"
    scene w3_4437 with dissolve
    "She didn't speak up, but I got an answer all the same. She looked weary and out-of-place, her shoulders slumping as if trying to disappear into the background."
    scene w3_4439 with dissolve
    mc "Tired?"
    scene w3_4440 with dissolve
    rose "A little."
    scene w3_4441 with dissolve
    "Perhaps she was coming down from the earlier excitement, but..."
    mc "You can have my bed if you want to lay down."
    scene w3_4442 with dissolve
    rose "It's not the kind of tiredness that goes away from a nap."
    scene w3_4443 with dissolve
    "In a moment of honesty from the poker-faced woman, she said what I was thinking."
    scene w3_4444 with dissolve
    rose "...how'd it go?"
    scene w3_4445 with dissolve
    mc "Talking to the old farts? Give it a few days and everything will be settled."
    scene w3_4444 with dissolve
    rose "What does \"settled\" mean...?"
    scene w3_4445 with dissolve
    mc "It means that unwitting bastard walked into a land mine and blew himself to bits without even realizing it."
    scene w3_4446 with dissolve
    rose "...?"
    mc "In short, he'll be off your back. {b}Most certainly{/b}."
    scene w3_4447 with dissolve
    rose "Oh..."
    mc "Two or three days and you'll be good to go home. If Oliver calls in the meantime, just don't answer it."
    scene w3_4448 with dissolve
    "........."
    "......"
    scene w3_4449 with dissolve
    rose "...got it."
    scene w3_4450 with dissolve
    mc "I bet you still wish I never interfered."
    scene w3_4451 with dissolve
    rose "No... it's {i}something{/i}."
    scene w3_4452 with dissolve
    "She willed a bit of life back into her face as her lips formed into a pale smile."
    scene w3_4451 with dissolve
    rose "Two or three days away from home doesn't sound so bad."
    scene w3_4452 with dissolve
    "That admission surprised me a little. I wasn't sure if she was trying to convince me or herself."
    mc "You think...?"
    "But as soon as my question left my lips, the answer unfolded itself in my head."
    scene w3_4453 with dissolve
    rose "I don't know... I guess?"
    scene w3_4454 with dissolve
    "Home simply didn't feel like home."
    scene w3_4455 with dissolve
    mc "You have the run of the place then."
    scene w3_4456 with dissolve
    rose "Thanks, [mcf]..."
    scene w3_4457 with dissolve
    "It was two or three days to feel a little more {i}removed{/i}."
    scene w3_4456 with dissolve
    rose "If that's the case..."
    scene w3_4458 with dissolve
    rose "You said you're starving?"
    scene w3_4459 with dissolve
    "I nodded my head in affirmation."
    mc "What's in the pot?"
    scene w3_4458 with dissolve
    rose "You had a mishmash of ingredients, so I made a stew. I hope it's to your liking."
    scene w3_4459 with dissolve
    mc "A stew sounds {i}really{/i} good."
    "To be precise, a home-cooked meal from a lovely woman sounded like a salve after the day I was having."
    scene w3_4460 with dissolve
    rose "Go eat. I've kept it hot."

    if roseFlag == True:
        "If this was part of a seduction, she had really stepped up her game since her first foray."
        "Even weary and out of place, she was full of charm."

    "My feet followed after her, spellbound, on my stomach's volition."

    scene black with fade
    rose "...I'll spoon it out. Wash your hands."
    mc "...yes, Ma'am."
    "......"
    "..."
    scene w3_4461 with dissolve
    "While I gobbled up the stew, Rosalind took care of the dishes. I was emphatic about leaving the clean up to me, but it was like talking to a wall."
    rose "The rest is in the fridge if you want some more."
    scene w3_4462 with dissolve
    mc "I'll have some more later. Are you not going to eat?"
    rose "It's late."
    scene w3_4463 with dissolve
    rose "I'll just push through to dinner."
    scene w3_4464 with dissolve
    rose "How was it?"
    scene w3_4465 with dissolve
    mc "{i}Really{/i} tasty and {b}especially{/b} filling."
    scene w3_4466 with dissolve
    rose "Heh, good."
    scene w3_4467 with dissolve
    "A tiny smile tried to go unnoticed on her face."
    scene w3_4466 with dissolve
    rose "I didn't know if I added enough salt or not. It can be tricky when you're working freestyle."
    scene w3_4467 with dissolve
    mc "Do you cook a lot?"
    scene w3_4468 with dissolve
    rose "As much as I can, which is... {i}tough{/i} nowadays."
    scene w3_4469 with dissolve
    rose "By the way, I noticed your clothes hamper was full..."
    scene w3_4470 with dissolve
    mc "...you're not here to do chores."
    scene w3_4471 with dissolve
    rose "You said I had the run of the place."
    scene w3_4472 with dissolve
    mc "I meant for you to be comfortable."
    scene w3_4473 with dissolve
    stop music
    $ renpy.music.set_volume(.2, 0, channel = "ambient")
    play ambient "sound effects/ringing-inbound.wav"

    if roseFlag == True:
        rose "What else am I going to do? You wanna screw?"
    else:
        rose "I like to stay--"

    scene w3_4474 with dissolve
    mc "Is it Oliver?"
    scene w3_4475 with dissolve
    rose "Unlikely... given the time, it's probably..."
    scene w3_4476 with dissolve
    rose "It's my daughter."
    scene w3_4477 with dissolve
    "A blood-curdling look impelled me to keep my trap shut and stay silent."
    stop ambient
    $ renpy.music.set_volume(1, 0, channel = "ambient")
    play sound "sound effects/phonemenu.wav"
    scene w3_4478 with dissolve
    rose "Hey honey. How are you? How's camp?"
    scene w3_4479 with dissolve
    "The thing is, I wouldn't have been able to utter a single word even if I wanted to."
    scene w3_4480 with dissolve
    rose "Oh, really? That's too bad. Did you bring it up to your counselor?"
    scene w3_4479 with dissolve
    "Rosalind's face shone with a luminosity that rendered me speechless."
    scene w3_4481 with dissolve
    rose "Don't be pessimistic. You may be right, they probably won't do anything about it... but it's guaranteed nothing will be done if you just keep it to yourself."
    scene w3_4482 with dissolve
    "It was a common, everyday exchange between mother and daughter, yet..."
    scene w3_4480 with dissolve
    rose "Me? The usual. I've been making a dent in my reading list."
    scene w3_4479 with dissolve
    "...it was like the persevering woman's walls instantly crumbled before my eyes, and I was catching a bare glimpse of something I had no business being privy to."
    scene w3_4480 with dissolve
    rose "No, I'm not going to..."
    scene w3_4482 with dissolve
    "........."
    scene w3_4484 with dissolve
    "......"
    scene w3_4483 with dissolve
    "..."
    scene w3_4485 with dissolve
    rose "I miss you very, {i}very{/i} much. I'll talk to you later, enjoy your swim--"
    scene w3_4486 with dissolve
    play sound "sound effects/phonemenu.wav"
    rose "..."
    scene w3_4487 with dissolve
    rose "Heh. She always hangs up before the other person finishes speaking..."
    scene w3_4488 with dissolve
    "The Rosalind before me, for a fast fleeting moment, was a night-and-day difference from the woman who had walked into my apartment."
    "Not that she wasn't lovely in the first place, but {i}her present affectation was so intensely attractive.{/i}"
    play music "music/lobby-time.ogg"
    scene w3_4490 with dissolve
    mc "So, I've got a question for you."
    scene w3_4491 with dissolve
    rose "Okay...?"
    scene w3_4490 with dissolve
    mc "Do you... {i}regret{/i} how things have turned out?"
    scene w3_4489 with dissolve
    "On the face of it, that was a stupid question, but its roots had abruptly taken hold in me."
    scene w3_4492 with dissolve
    rose "That's random..."
    scene w3_4493 with dissolve
    mc "You just looked really happy after you got off the phone."
    "Intellectually I understood how much she cared for her daughter, and it was evident from her actions, but seeing her {b}positively glow{/b} was another thing entirely."
    mc "It was like I caught a glimpse of the absolute best version of you right now."
    scene w3_4494 with dissolve
    "And, even though they're different people, with different circumstances, it was a question I'd never be able to ask my own mother."
    scene w3_4495 with dissolve
    rose "Uh... isn't that how it goes?"
    scene w3_4496 with dissolve
    mc "What do you mean?"
    scene w3_4495 with dissolve
    rose "Everyone's got that one, two, or handful of things that cuts through the {i}blah{/i} and keeps you going."
    scene w3_4497 with dissolve
    "How it goes indeed..."
    scene w3_4498 with dissolve
    rose "Life would be dreary if you had nothing, right?"
    scene w3_4499 with dissolve
    mc "True, but I do think you're a little atypical, Rosie."
    scene w3_4498 with dissolve
    rose "Not really, but let me ask you a question..."
    scene w3_4499 with dissolve
    mc "You didn't actually answer mine, but okay. What?"
    scene w3_4498 with dissolve
    rose "What makes the day easier for you? What do you think about when things get difficult or annoying?"
    scene w3_4499 with dissolve
    mc "I don't know... does that make me dreary?"
    scene w3_4500 with dissolve
    rose "Really? You can't think of a thing?"
    scene w3_4501 with dissolve
    rose "......"
    rose "..."
    scene w3_4502 with dissolve
    mc "......"
    scene w3_4503 with dissolve
    mc "..."
    scene w3_4504 with dissolve
    rose "Uh, so... what were you asking?"
    mct "(She thinks I'm a sad sack!)"
    scene w3_4505 with dissolve
    rose "...if I wish things were different?"
    mc "...I wanted to know if you would do anything differently if you could. About any of this."
    scene w3_4506 with dissolve
    rose "No."
    scene w3_4507 with dissolve
    "She didn't even think about it."
    mc "Simple as that?"

    scene w3_4506 with dissolve
    rose "I was naive when I married Rupert, but that man through all his faults and blunders, gave me the center of my world. If I wouldn't change that, then I have to accept everything after as a consequence."
    scene w3_4507 with dissolve
    mc "Isn't it messed up? In the scheme of things, what you owe that prick isn't a lot of money, yet..."
    scene w3_4508 with dissolve
    rose "Not a lot...?"
    scene w3_4509 with dissolve
    mc "I said in the scheme of things."
    "She looked at me like I was a privileged twat."
    scene w3_4508 with dissolve
    rose "Maybe it's not a lot to someone like you, but when you're left with almost no money and the interest is piling on and on, it might as well be a million dollars."
    scene w3_4509 with dissolve
    "{i}...was I a privileged twat?{/i}"
    scene w3_4510 with dissolve
    rose "I mean, should I have sold my car? It's worth only a quarter of that and I {b}need{/b} it."
    rose "Start selling off all my other belongings? Try to find someplace cheaper to live in {i}this{/i} city? Uproot my daughter from her life and flee?"
    scene w3_4507 with dissolve
    mc "Good points..."
    scene w3_4508 with dissolve
    rose "How does a woman like me make money quickly? There's a reality to this and we both know the answer... and I was close to putting up an ad on the internet when Mrs. Pulman dropped this in my lap."
    scene w3_4511 with dissolve
    rose "No, I wouldn't do anything different, even... {i}this{/i}."
    scene w3_4512 with dissolve
    mc "I admire that."
    scene w3_4513 with dissolve
    "It was fucked up but she had mettle."
    "I don't know why the thought crossed my mind, but if she did lose, she had the gumption to make her gains as a house girl."
    "She kinda reminded me of Dalia..."
    scene w3_4517 with dissolve
    rose "I'll take this."
    scene w3_4518 with dissolve
    "This woman was ridiculous. Cooking for me, cleaning up, doing my laundry... and she had only been here a few hours."
    hide screen textbox2 with dissolve

    menu:
        "Do something nice for Rosalind. Probably(w3RosalindMassaged=True)."(chg=["rosalind_up"]):
            $ w3RosalindMassaged = True
            $ Rosalind_Affection += 1
            scene w3_4519 with dissolve
            mc "Nuh-uh. No way."
            scene w3_4520 with dissolve
            rose "...could you be a bit more clear?"
            scene w3_4519 with dissolve
            mc "Stop playing housewife."
            scene w3_4520 with dissolve
            rose "...don't tell me what to do."
            scene w3_4519 with dissolve
            mc "Take a load off."
            scene w3_4520 with dissolve
            rose "Sitting around doing nothing isn't taking a load off."
            scene w3_4521 with dissolve
            mc "You're right, but you're not going to sit around doing nothing."
            stop music fadeout 3.0
            scene w3_4522 with dissolve
            mc "Come on!"

            if roseFlag == True:
                rose "Wait, if you want to have sex let me take a shower--"
            else:
                rose "Wait, what are you--"
            jump w3RosalindMassage
        "Let her get her chore on.":

            scene w3_4523 with dissolve
            mc "Yeah, go ahead."
            "I myself understood the comfort in staying busy. If she wants to do housework while she's here, well..."
            mc "Do what makes you happy."
            scene w3_4524 with dissolve
            "Good for me."
            stop music fadeout 3.0
            scene black with fade
            "Some time passed, and..."
            scene w3_4525 with dissolve
            "Heh. So much for not being the kind of tired that needed sleep."
            mct "(She must have really been exhausted...)"
            scene w3_4526 with dissolve
            "Me too, actually. Today had been hectic."
            "Between the Abel-induced existential crisis and dealing with the Rosalind thing, I felt emotionally drained."

            if w3VeroBarDate == True:
                scene w3_4527 with dissolve
                play sound "sound effects/sms-chime.wav"
                "*Bleeup!*"
                "It was nice having a housemate again..."
                scene w3_4528 with dissolve
                mct "(Rosalind can be my first line of defense if Abel nosferatu'd himself through my door while I'm sleeping.)"
                scene w3_4529 with dissolve
                mct "(Veronica...)"
                scene w3_4530 with dissolve
                play sound "sound effects/sms-chime.wav"
                "*Bleeup!*"
                mc "...?"
                scene w3_4531 with dissolve
                call phone_start_ver from _call_phone_start_ver
                call message_start ("Veronica", "Decided to get drinks last minute.") from _call_message_start_25
                call message ("Veronica", "9431 Henenlotter Lane. The Hideaway.") from _call_message_81
                call message ("Veronica", "Come if you want, but you don't have to.") from _call_message_82
                call phone_end_ver from _call_phone_end_ver
                scene w3_4530 with dissolve
                "......"
                "..."
                scene w3_4532 with dissolve
                mct "(She acts so stupid...)"
                scene w3_4533 with dissolve
                "That saves me the trouble of figuring out what to do."
                scene w3_4534 with dissolve
                "I considered inviting Rosalind along too, but I didn't really know how that would play with Veronica."
                "Inviting me out to drink was already a big show of trust for the Amazon, and despite my pretenses, Rosalind was her competitor..."
                scene w3_4535 with dissolve
                mct "(Yeeeeeah... still in the same clothes from yesterday.)"
                scene black with fade
                "A shower and change was in order, so I let Veronica know she could expect me in about an hour."
                "{i}She didn't respond{/i}."
                jump w3VeronicaDatePrep
            else:
                "It was nice having a housemate again..."
                scene black with fade
                "......"
                "..."
                hide screen textbox2 with dissolve
                menu roseNightInMenu1:
                    "{color=#FF1493}[[Rosalind Deal]{/color} It {i}really{/i} was nice having a housemate again(w3RoseStayLewd += 1)." if roseFlag == True:
                        $ w3RoseStayLewd += 1
                        jump w3RosalindNightInLewd
                    "You had a nice night in, watching a movie.":
                        jump w3RosalindNightInPlatonic
                    "{color=#696969}[[Rosalind Deal] It {i}really{/i} was nice having a housemate again.{/color}" if roseFlag == False:
                        jump roseNightInMenu1


label w3RosalindMassage:
    scene w3_4536 with dissolve
    show screen textbox2 with dissolve
    mc "Sit down and relax."
    scene w3_4537 with dissolve
    rose "Nothing helps you relax like being told to relax..."
    scene w3_4536 with dissolve
    mc "I get it. You're a do or think kinda gal."
    scene w3_4538 with dissolve
    mc "I'm the same way. Constantly looking for outlets for my nervous energy."
    scene w3_4539 with dissolve
    mc "You try to be frank with yourself on an intellectual level, hoping it will unravel that knot of anxiety in your stomach, but in reality you're just playing mental abacus and shuffling it around."
    scene w3_4540 with dissolve
    rose "...and how does one do that?"
    mc "I guess it depends on the person, but do you find housework relaxing? Be honest."
    rose "Not really..."
    play music "music/select.ogg"
    scene w3_4541 with dissolve
    mc "Yeah, just something to do isn't the same as letting off some steam, is it?"
    mc "Although, I think you were on the right track when you said being away from home was a silver lining."
    scene rosa_mass1_a with dissolve
    show rosa_mass1 with dissolve
    "With one hand, I began to gently knead Rosalind's neck, in a blind attempt to make her feel nice."
    mc "In reality, what you miss is picking up after your daughter, don't you?"
    rose "Of course, I do... this is the longest she's ever been away from me."
    mc "That must make a difficult situation even harder."
    rose "That feels... nice..."
    "A little physical comfort to go hand-in-hand with some empathy and understanding. That was what I was aiming for."
    mc "Good. Just clear your head, think about the stuff that keeps you anchored, and let me bumble in my attempt at a massage."
    rose "We'll try it your way..."
    scene rosa_mass2_a with dissolve
    show rosa_mass2 with dissolve
    mc "Thank you, cause let me tell you. You feel {i}tense{/i}. You've got knots in your shoulders."
    "That was what people said during this type of thing, right?"
    rose "Mmhm..."
    "{i}I couldn't actually feel the knots{/i}."
    mc "In the meantime, tell me something. Do you and your daughter have a place that you'd both love to go?"
    mc "As in a dream vacation or whatever?"
    rose "Paris..."
    rose "I don't even remember who first thought of it, but it became a {i}thing{/i}."
    rose "I always pictured us going after she graduated, but thinking that far ahead is... inconceivable."
    mc "Isn't a long time from now a comfortable thought?"
    rose "Yeah... I can't wait to see her grow into a young woman..."
    "......"
    "..."
    mc "What's your favorite food?"
    rose "Ah, mmmhhh... there's a local place, Harry's, that has the BEST cheeseburgers..."
    mc "Sounds like dinner."
    rose "Ah, yeeeah... that would be good... their fries are to die for... the seasoning is just..."
    mc "Hungry?"
    rose "I think I'll order two later..."
    "I could see she was coming around on the idea of taking it easy."
    mc "That's the spirit. The next few days, just... {i}indulge.{/i}"
    mc "Catch up on any shows you're behind on, order and eat anything you want, and just give it time for you to become sick of doing nothing."

    if roseFlag == True:
        mc "Consider it part of our deal, okay?"

    scene rosa_mass3_a with dissolve
    show rosa_mass3 with dissolve
    rose "Uh, huh... mmmh... yeah... I'll try..."
    "Rosalind was even more tired than she let on. Quickly and surely, the tension vanished from her body."
    "Her shoulders went slack and all resistance to my touch, the involuntary twitching and readjusting for comfort, dissipated."
    "In minutes, her breath evenly slowed, and I knew her consciousness was fading."
    stop music fadeout 3.0
    scene black with fade
    mct "(She really must be exhausted...)"
    scene w3_4542 with fade
    "Me too, actually. Today had been hectic."
    "Between the Abel-induced existential crisis and dealing with the Rosalind thing, I felt emotionally drained."
    "I didn't really know what to do, but I kinda just felt content sitting here..."

    if w3VeroBarDate == True:
        scene w3_4543 with dissolve
        play sound "sound effects/sms-chime.wav"
        "*Bleeup!*"
        "It WAS nice having a housemate again..."
        scene w3_4544 with dissolve
        mct "(For example, Rosalind can be my first line of defense if Abel nosferatu'd himself through my door while I'm sleeping.)"
        scene w3_4545 with dissolve
        mct "(Veronica...)"
        scene w3_4546 with dissolve
        play sound "sound effects/sms-chime.wav"
        "*Bleeup!*"
        mc "...?"
        scene w3_4547 with dissolve
        call phone_start_ver from _call_phone_start_ver_1
        call message_start ("Veronica", "Decided to get drinks last minute.") from _call_message_start_26
        call message ("Veronica", "9431 Henenlotter Lane. The Hideaway.") from _call_message_83
        call message ("Veronica", "Come if you want, but you don't have to.") from _call_message_84
        call phone_end_ver from _call_phone_end_ver_1
        scene w3_4546 with dissolve
        "......"
        "..."
        scene w3_4548 with dissolve
        mct "(She's so stupid...)"
        scene w3_4549 with dissolve
        "That saves me the trouble of figuring out what to do."
        scene w3_4550 with dissolve
        "I considered inviting Rosalind along too, but I didn't really know how that would play with Veronica."
        "Inviting me out to drink was already a big show of trust for the Amazon, and despite my pretenses, Rosalind was her competitor..."
        scene w3_4551 with dissolve
        mct "(Hmm...?)"
        scene black with fade
        "A shower and change was in order, so I let Veronica know she could expect me in about an hour."
        "{i}She didn't respond{/i}."
        jump w3VeronicaDatePrep
    else:
        "It was nice having a housemate again..."
        scene black with fade
        "......"
        "..."
        hide screen textbox2 with dissolve
        menu roseNightInMenu2:
            "{color=#FF1493}[[Rosalind Deal]{/color} It {i}really{/i} was nice having a housemate again." if roseFlag == True:
                $ w3RoseStayLewd += 1
                jump w3RosalindNightInLewd
                jump w3RosalindNightInPlatonic
            "You had a nice night in, watching a movie.":
                jump w3RosalindNightInPlatonic
            "{color=#696969}[[Rosalind Deal] It {i}really{/i} was nice having a housemate again.{/color}" if roseFlag == False:
                jump roseNightInMenu2

label w3VeronicaDatePrep:
    scene w3_4552 with dissolve
    show screen textbox2 with dissolve
    "It looked like a fairly nice place from a quick internet search, so why not dress the part?"
    scene w3_4553 with dissolve
    "It was silly."
    scene w3_4554 with dissolve
    "New haircut, nice clothes..."
    "I was feeling like a million bucks. I hated them, but..."
    mct "(Contacts it is.)"
    scene w3_4555 with dissolve
    "Taking a page from {i}She's All That{/i}..."

    if w3HanaDP >=4:
        scene black with fade
        play sound "sound effects/ringing-inbound.wav"
        "*Ring, ring...*"
        stop sound
        play sound "sound effects/phonemenu.wav"
        scene w3_4556 with wipeleft
        mc "Hey, how's it going?"
        scene w3_4557 with dissolve
        hana "Just checking in. Seeing how you're doing."
        play music "music/modern-situations.ogg"
        scene w3_4559 with dissolve

        if w3HanaCutieCall == True:
            hana "Don't expect any masturbation though."
        else:
            hana "That's a thing people do, right?"

        scene w3_4558 with dissolve
        mc "I'm good. I'm about to meet Veronica for some drinks."
        scene w3_4559 with dissolve
        hana "...you see the Carnations a lot outside of the club?"
        scene w3_4558 with dissolve
        mc "I do..."
        mc "In fact, Rosalind's spending a few days at my place right now."
        scene w3_4561 with dissolve
        hana "...yeah?"
        scene w3_4560 with dissolve
        mc "What, jealous?"
        scene w3_4561 with dissolve
        hana "Of course not, but what's the situation?"
        scene w3_4560 with dissolve
        mc "The guy she owes money to tore up her place."
        mc "It was a whole thing today."
        scene w3_4561 with dissolve
        hana "A thing...?"
        scene w3_4560 with dissolve
        mc "Yeah, I almost got killed."
        scene w3_4563 with dissolve
        hana "What?!"
        scene w3_4562 with dissolve
        mc "Sorry, that was a joke. I'm exaggerating."
        scene w3_4563 with dissolve
        hana "...do you have to deal with crap like that?"
        scene w3_4562 with dissolve
        mc "Apparently. We can't all be bourgey owners, y'know?"
        scene w3_4563 with dissolve
        hana "What about Veronica? Is she okay?"
        scene w3_4562 with dissolve
        mc "Yeah. Just trying to keep morale up there."
        mc "The old woman laid into the Carnations hard yesterday."
        scene w3_4564 with dissolve
        mc "What about you? What are you up to?"
        scene w3_4565 with dissolve
        hana "Well, this bourgey bitch is playing bartender for a birthday party."
        scene w3_4564 with dissolve
        mc "Whose birthday is it?"
        scene w3_4565 with dissolve
        hana "Jim's."
        scene w3_4564 with dissolve
        mc "No shit? I played cards with him today."
        scene w3_4565 with dissolve
        hana "Seems like we're both in ass-kissing mode then."
        scene w3_4564 with dissolve
        mc "August put you up to it?"
        scene w3_4566 with dissolve
        hana "He thought it would be good for me to be around."
        scene w3_4567 with dissolve
        "......"
        "..."
        scene w3_4568 with dissolve
        mc "Keep your chin up."
        scene w3_4569 with dissolve
        hana "I'll try. And you be safe tonight, okay?"
        scene w3_4568 with dissolve
        mc "Will do. I'm on my way out the door, so--"
        scene w3_4569 with dissolve
        hana "Bye, [mcf]."
        scene w3_4570 with dissolve
        play sound "sound effects/phonemenu.wav"
        mct "(Heh, alright...)"
        scene w3_4571 with dissolve
        mct "(Now where did I put my...)"
    else:

        mct "(Now where did I put my...)"
    stop music fadeout 3.0
    scene black with fade
    if w3RosalindMassaged == True:
        "Rosalind was still asleep when I ventured out, so I left a note and put in a timed delivery order for those burgers she wanted."
        "A whole sackful of them."
    else:
        "Rosalind was still asleep when I ventured out, so I left a note and put in a timed delivery order for a pizza."
        "Not quite home cooking, but it's the thought that counts, right?"

    stop music
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionveronica05 with blinds
    $ renpy.pause(6, hard=True)
    scene w3_4572 with blinds
    play music "music/timeless.ogg"
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    $ date = "june16night"
    "Veronica's chosen hole-in-the-wall was aptly named."
    "A meager sign-posting on a side of a building led to a long stretch of stairs, and at the top of it all..."
    scene w3_4573 with wiperight
    "{i}A hideaway{/i}."
    "A forest of people tucked away from the city, amidst a mingling of herbal scents and the faint smell of acetone."
    scene w3_4574 with dissolve
    "...and there was Veronica, easy to spot as the tallest tree in the forest."
    "One thing that I noticed..."
    scene w3_4575 with cmet
    mc "So, a gay bar, huh?"
    "That was clear enough. As I ventured into the foliage, there was a conspicuous lack of {i}stamens{/i} amongst the flowers. "
    mc "I'm out of place."
    scene w3_4576 with dissolve
    ver "[mcf]..."
    "Veronica gave me a curious look up and down."
    bart "You don't have to worry. No one here is paying attention to you, sweetheart."
    scene w3_4577 with dissolve
    ver "Huh. You don't clean up so bad..."
    scene w3_4578 with dissolve
    mc "I'm not used to seeing you in regular clothes, either."
    "......"
    "..."
    scene w3_4579 with dissolve
    ver "He's a {i}friend.{/i} We work out together, so don't get any ideas, Karli."
    scene w3_4580 with dissolve
    karli "Like that helps? I know exactly the kinds of things you get up to with both your workout partners."
    scene w3_4581 with dissolve
    ver "This is Karli."
    karli "Charmed to meet you, [mcf]."
    scene w3_4582 with dissolve
    ver "She owns the place."
    karli "When Frankie told me she was waiting for someone, I was curious about {i}what{/i} was going to walk into the door."
    scene w3_4583 with dissolve
    mc "Frankie...?"
    mc "You two must be good friends."
    scene w3_4584 with dissolve
    ver "As a bartender, serving me drinks."
    scene w3_4585 with dissolve
    karli "Ha! I officiated her wedding."
    mc "And here I thought she was just standoffish with me."
    scene w3_4586 with dissolve
    karli "Aw, naaaaw... Frankie here is a sweetie."
    karli "She's just afraid of being teased about it."
    scene w3_4587 with dissolve
    karli "By the way... can I see your ID?"
    scene w3_4588 with dissolve
    mc "Uh... yeah?"
    scene w3_4589 with dissolve
    ver "Don't pull out your wallet. She's fucking with me."
    karli "I could lose my license serving a minor."
    scene w3_4590 with dissolve
    ver "I'm going to the bathroom. Get it out of your system while I'm gone."
    scene w3_4591 with dissolve
    "......"
    "..."
    scene w3_4592 with dissolve
    karli "What are you drinking?"
    scene w3_4591 with dissolve
    mc "Rum with coke."
    scene w3_4593 with dissolve
    karli "You guys really friends?"
    scene w3_4594 with dissolve
    mc "Did you really officiate her wedding?"
    scene w3_4593 with dissolve
    karli "Liliana is my goddaughter."
    scene w3_4594 with dissolve
    mc "Ah..."
    scene w3_4595 with dissolve
    mc "I'm {i}trying{/i} to be her friend. Getting some drinks was my idea and--"
    scene w3_4596 with fade
    mc "...it took a few steps to get here. Enough steps for it to turn into Veronica's idea."
    karli "Well, this one's on the house if you keep trying, alright? And the next one too, since I haven't seen Frankie in ages."
    "Right, yeah... drinking was a luxury she really couldn't afford right now, was it?"
    scene w3_4597 with dissolve
    mc "Hey..."
    "And here I was casually asking her out to do it."
    mc "This place always this busy on a Tuesday?"
    scene w3_4598 with dissolve
    karli "It's a little on the slow side. Why do you ask?"
    mc "Just a random question..."
    "Seeing all these faces, I wonder if Veronica ever considered running a women's only gym? I mean, surely she had?"
    scene w3_4599 with dissolve
    mc "Seems like you do pretty good."
    karli "I like to think of us as a pillar of the community."
    scene w3_4600 with dissolve
    mc "Hmmm..."
    "I also couldn't help but notice a couple of women who had their eyes glued to Veronica in the short time I was here."
    scene w3_4601 with dissolve
    mc "I bet {i}Frankie{/i} is pretty popular around here."
    scene w3_4602 with dissolve
    "She looked at me like she was trying to figure out what I meant."
    scene w3_4603 with dissolve
    karli "She's a striking woman, I guess."
    scene w3_4602 with dissolve
    "That probably came off as a weird question, but it was a good reminder of just how magnetizing Veronica was."
    "It was easy to forget when you've paraded her around like a dog and viewed her getting demolished by a monster strap-on."
    scene w3_4604 with dissolve
    karli "She used to get approached a lot because of her looks."
    scene w3_4605 with dissolve
    karli "Quite a few have had their eyes on her tonight. Better watch yourself, gym partner."
    scene w3_4606 with dissolve
    mc "Thanks..."
    scene w3_4607 with dissolve
    ver "You tell him how you got that scar?"
    scene w3_4608 with dissolve
    karli "He didn't ask."
    scene w3_4609 with dissolve
    mc "How'd you get that scar?"
    scene w3_4610 with dissolve
    karli "Eating pineapple."
    scene w3_4611 with dissolve
    "......"
    "..."
    scene w3_4612 with dissolve
    ver "Don't feel bad. No one ever laughs at that."
    mc "...say hello to my little friend?"
    scene w3_4613 with dissolve
    ver "Come on, let's go drink in private."
    scene black with fade
    ver "Keep 'em coming, Karli."
    scene w3_4614 with fade
    mc "I'm glad you reconsidered about tonight."
    mc "It's been an unusually stressful day for me, so it's good to blow off some steam."
    scene w3_4615 with dissolve
    ver "Yeah...? Tell me about it."
    scene w3_4614 with dissolve
    mc "Just club stuff on top of club stuff; the details aren't so important. So, what made you change your mind?"
    scene w3_4616 with dissolve
    ver "I didn't change my mind. I decided to go out and then I just happened to remember that you asked earlier."
    scene w3_4614 with dissolve
    mc "Right, right... yeah."
    "I wanted to burst out laughing, but refrained."
    mc "And how are you tonight?"
    scene w3_4617 with dissolve
    ver "I'm out drinking with you, aren't I?"
    mc "Pffh-ha!"
    "This time I didn't bother."
    scene w3_4618 with dissolve
    ver "...your treat, you said?"
    mc "Did I--"
    scene w3_4619 with dissolve
    mc "... ah, that seems like a fair trade for your time and company."
    scene w3_4620 with dissolve
    "*Glug, gluh, glug...!*"
    mc "Although, I won't be offended if you slow down."
    scene w3_4621 with dissolve
    ver "Aaaaaah~ work hard, play hard. I don't half-ass things."
    scene w3_4622 with dissolve
    mc "I'm pretty fond of saying that too..."
    scene w3_4623 with dissolve
    ver "So, no... seriously... what's stressful about your job? Genuinely asking."
    scene w3_4624 with dissolve
    mc "...someone broke into my house last night and then I had to deal with one of the girl's homes getting smashed up by an asshole."
    scene w3_4625 with dissolve
    ver "It isn't just all bubblegum and fucking whores?"
    scene w3_4624 with dissolve
    mc "Evidently not, but should I complain? It's hard to call any of what I've been asked to do up to this point work."
    scene w3_4625 with dissolve
    ver "Why even be a doctor then?"
    scene w3_4624 with dissolve
    mc "Hopes and dreams aside, I don't reckon playing gopher for a prostitution ring is a long-term, sustainable career path."
    scene w3_4626 with dissolve
    "Just as Veronica's lips were starting to look lonesome, a drink appeared."
    scene w3_4627 with dissolve
    ver "*Sigh* Alright, then..."
    mc "Alright what...?"
    scene w3_4628 with dissolve
    "*Glug, glug, glug*...!"
    "Just as quickly as the glass met her mouth, the contents disappeared down her gullet."
    scene w3_4629 with dissolve
    ver "You give me no choice but to play the role of older sister tonight. I'll just have to teach you how an Olympian lets loose."
    "Just as I had hoped, she was more receptive to coloring the night as her doing me a favor."
    scene w3_4630 with dissolve
    ver "Hurry up and finish your drink."
    scene w3_4631 with dissolve
    ver "I want to go move my body."
    scene w3_4632 with dissolve
    mc "You want to dance? With me?"
    scene w3_4633 with dissolve
    ver "It's not a marriage proposal, you dweeb."
    scene w3_4634 with dissolve
    mct "(Alright, let's...)"
    "......"
    "..."
    scene w3_4635 with dissolve
    mc "You can take the lead."
    stop music fadeout 3.0
    scene black with fade
    ver "Let's go."
    scene w3_4636 with fade
    ver "YOU KNOW--"
    "Veronica raised the pitch of her voice, to be heard over the music."
    ver "I don't care who you are... you could be the best damn conversationalist in the world, but NOTHING is more revealing than dancing with a person."
    scene w3_4637 with dissolve
    mc "I don't think that's a good basis for judging character..."
    ver "Of course it isn't, but it's a starting point!"
    scene w3_4638 with dissolve
    play music "music/ily-baby.ogg"
    hide screen textbox2 with dissolve
    mc "It's not like we're meeting for the first time."
    scene w3_4639 with dissolve
    ver "{b}We might be.{/b}"
    mc "Oh...?"
    scene w3_4640 with dissolve
    ver "Well, have we {i}met{/i} before?"
    scene w3_4641 with dissolve
    mc "Well, I've seen you--"
    scene vd_dance1_a with dissolve
    show vd_dance1 with dissolve
    ver "~not listening."
    "Veronica took the lead, spinning on her heels and corralling my attention to her waist with a flick of her hips."
    "A flick that continued on, to-and-fro, teeter-tottering back and forth in pursuit of the music's rhythm."
    "The way Veronica moved her large frame was magnetizing, a snake-charming package of power and womanly wiles that defied my preconceptions."
    "She was lithe."
    "She was graceful."
    scene vd_dance2_a with dissolve
    show vd_dance2 with dissolve
    "It was like her body was made for dancing. Not throwing a lead ball, not preening on a stage, but {i}writhing{/i}."
    "Twisting."
    "Bending, curving, {i}wriggling{/i}."
    mct "(I really shouldn't be too surprised...)"
    scene w3_4642 with pixellate
    "My mind went back to the first week's exhibition..."
    scene vd_dance2_a with pixellate
    show vd_dance2 with dissolve
    ver "What's the matter? Not properly lubricated?"
    "Resting behind her glasses was a light unseen, an expression adrift from reality, and the totality of a woman being blown along by the music as if it was the wind."
    ver "You don't have to force yourself, but come on... move your hips, [mcf]. Show me a bit of who you are."
    "Most of all, Veronica was offering me a sledgehammer to break the ice."

    menu:
        "Dance...?(Dialogue/Render changes only)":
            scene vd_dance3_a with dissolve
            show vd_dance3 with dissolve
            mc "Alright, you asked for it..."
            "I willed myself to do something, {i}anything{/i}, and the result went how you'd expect it."
            mc "This is what I got!"
        "Dance...!(Dialogue/Render changes only)":

            scene vd_dance3_a with dissolve
            show vd_dance3 with dissolve
            mc "Alright. It's just moving your body, let's--"
            "I jumped into it. It's not like I've never danced before, and even though I admittedly felt a little more out-of-place than usual, I knew enough not to try to match her."
            mct "(Just take it easy...)"

    ver "That's more like it!"
    "The pair of us squared away, doing our own thing in pursuit of the music's beat."
    mct "(She didn't seem drunk, but...)"
    mc "How much did you drink before I got here?"
    ver "What? None!"
    "Was she always capable of this? Could she be this easygoing?"
    mc "You must really, REALLY like to dance!"
    ver "I wanted to be a dancer when I was a kid!"
    mc "No shit? Like ballet?!"
    ver "No! Like in music videos! I wanted to moonwalk!"
    mc "Really?! That's funny!"
    ver "Is it? Well, my mom even bought me a fedora for a talent show!"
    mc "Ha! And what about pole dancing?"
    ver "Not a childhood dream, but it's... {b}fun!{/b} Closest a dumbass like me gets to feeling creative!"
    mc "Eh? You're not dumb!"
    ver "Yes I am, but let's not get into it!"
    mc "YOU'RE NOT DUMB!"
    scene black with fade
    ver "Just focus on moving your tush!"
    "........."
    "......"
    "..."
    scene w3_4643 with fade
    ver "You know what?! I think I need to get more drinks in you."
    scene w3_4644 with dissolve
    mc "Ha! You say that to all your dates?"
    scene w3_4643 with dissolve
    ver "This isn't a date."
    scene w3_4644 with dissolve
    mc "So, what? You don't like my dancing, then?"
    scene w3_4645 with dissolve
    ver "I didn't say that! I just think you can still loosen up!"
    scene w3_4646 with dissolve
    mc "Are you sure you're just not trying to take advantage of me?"
    scene w3_4647 with dissolve
    ver "...I'm going to go get some more drinks. You can decide what you want to do."
    scene w3_4648 with dissolve
    mc "{size=-5}I don't think she likes my dancing!{/size}"
    stop music fadeout 3.0
    scene black with fade
    mc "Sure, alright! Get me one too!"
    "Tonight I resolved myself to put the mantra \"I'm not a big drinker\" out of mind."
    scene w3_4649 with circlewipe
    show screen textbox2 with dissolve
    mc "Wait, for real? They measure where the shot lands by hand?"
    scene w3_4650 with cmet
    "Bring on the hangover."
    ver "No. That's fucking weird!"
    mc "...really?"
    play music "music/timeless.ogg"
    scene w3_4651 with blinds
    "A few rounds later we were still going toe-to-toe."
    ver "...and what about you?"
    scene w3_4652 with dissolve
    mc "What about me?"
    scene w3_4651 with dissolve
    ver "You never thought, \"Hey, that guy's cute!\"?"
    scene w3_4652 with dissolve
    mc "Not really."
    scene w3_4653 with dissolve
    ver "Not even an \"Eh, why not?\" sort of way? I mean a pretty face is a pretty face."
    scene w3_4654 with dissolve
    mc "Any hole is a goal?"
    scene w3_4655 with dissolve
    ver "I'm not saying don't have standards! It's just, out of all the men in the world, there's no one you would go gay for?"
    scene w3_4656 with dissolve
    mc "What, like a celebrity pick?"
    scene w3_4657 with dissolve
    ver "Sure, we can go with that angle."
    scene w3_4658 with dissolve
    mc "Mmmh, well... I don't think banging Sonny Chiba is ever in my cards."
    scene w3_4659 with dissolve
    ver "Hold on, who's that?"
    scene w3_4660 with dissolve
    "......"
    "..."
    scene w3_4661 with dissolve
    ver "Well, {b}that's{/b} an interesting pick."
    mc "I didn't pick anyone."
    scene w3_4662 with dissolve
    ver "Yeah, yeah... point is, human beings are preeeetty fucking adaptable when the situation calls for it."
    mc "...hmm, do you think that applies to everything?"
    scene w3_4663 with dissolve
    ver "What do you mean?"
    mc "Do you think other things in life - beliefs, conviction, love, right and wrong, and {i}whatever{/i} is subject to the whims of circumstance?"
    scene w3_4664 with dissolve
    ver "Of course not!"
    scene w3_4665 with dissolve
    "She said it confidently."
    scene w3_4666 with dissolve
    ver "There's stuff in life that is set in stone. North, East, South, West... {i}basic human decency{/i}, the golden rule..."
    scene w3_4667 with dissolve
    ver "...the only thing that fucks shit up is what's going on up here, but no matter how twisted up you get, there's a right and wrong. {b}Fuck yeah, there is.{/b}"
    scene w3_4665 with dissolve
    mc "That kind of perspective suits you, like a valorous knight."
    scene w3_4668 with dissolve
    ver "Ahah! And how should I take that?"
    scene w3_4669 with dissolve
    mc "From a place of goodwill, I hope."
    scene w3_4670 with dissolve
    ver "Psssh, idiot. What about you? Do you think all of life is so wishy-washy?"
    scene w3_4669 with dissolve
    "..."
    scene w3_4671 with dissolve
    "..."
    scene w3_4672 with dissolve
    mc "...should I go get us another round?"
    scene w3_4673 with dissolve
    ver "Not so fast. Answer your own question!"
    scene w3_4674 with dissolve
    mc "Well... I know that there's people in my life I want to see happy and things that I very much hope stand the test of time."
    mc "I don't need that written into the DNA of the universe to pursue those feelings."
    scene w3_4675 with dissolve
    ver "Alright, good enough. You can go get us another drink."
    scene w3_4676 with dissolve
    mc "Although, if I'm being intellectually honest..."
    ver "Nope, you had it right the first time. Go."
    scene w3_4677 with dissolve
    mc "Be right back."
    scene w3_4678 with wipeleft
    mc "Two more, please."
    karli "Coming right up, Captain."
    scene w3_4679 with dissolve
    karli "Enjoying the atmosphere?"
    mc "Oh, absolutely."
    mc "It's nice to finally just drink in peace without anyone hitting on me."
    scene w3_4680 with dissolve
    woman "You know, not everyone here swings that way."
    mc "Sounds like a bad fielding strategy."
    scene w3_4681 with dissolve
    woman "I'm here with my friend. She's new to this."
    scene w3_4682 with dissolve
    mc "New to bars?"
    scene w3_4681 with dissolve
    woman "New to picking up women and hooking up."
    scene w3_4683 with dissolve
    woman "She's over there."
    scene w3_4684 with dissolve
    mc "Oh yeah... she's cute."
    woman "Yeah, fucking adorable and looking for some fun."
    scene w3_4682 with dissolve
    mc "Why are you telling me this then?"
    scene w3_4685 with dissolve
    woman "Well..."
    scene w3_4686 with dissolve
    woman "My friend is interested in your friend."
    scene w3_4687 with dissolve
    mc "You're a good friend, huh?"
    scene w3_4688 with dissolve
    woman "Nah, she's a better friend than I deserve."
    scene w3_4689 with dissolve
    woman "Looks like she didn't have any luck. She's been eyeing your friend all night."
    scene w3_4690 with dissolve
    woman "She made her move as soon as you got up. Isn't that some shit?"
    mc "Not everyone has a wing-woman like you."
    scene w3_4691 with dissolve
    mc "So you want me to help or something?"
    woman "I don't know your situation, but I think you're cute and hoping you might keep my friend in mind if the big girl over there is looking for a cute, inexperienced thing."
    scene w3_4692 with dissolve
    woman "If you do that, maybe we can all be friendly with each other."
    mc "You're a REALLY good friend, eh?"
    scene w3_4693 with dissolve
    woman "Maybe. We'll be here another hour or two."
    "Like that, she went back to her friend."
    scene w3_4694 with dissolve
    mct "(Well, her friend is pretty cute... and probably a good morale booster for Veronica to end the night with.)"
    mct "(Maybe I should keep that in mind.)"
    scene w3_4695 with dissolve
    karli "Well, that was interesting."
    mc "I've bet you've seen a million things like that play out with your job."
    karli "I've got my stories."
    scene w3_4696 with dissolve
    mc "Have one ready for me when I come back."
    karli "Sure, they're complimentary!"
    scene w3_4697 with dissolve
    mc "So, leggy models aren't your type?"
    scene w3_4698 with dissolve
    ver "Not tonight. She didn't strike my fancy."
    ver "Besides, I don't want to be rude. You and I are drinking."
    scene w3_4697 with dissolve
    mc "You're fucking kidding me? She was pretty hot."
    scene w3_4699 with dissolve
    ver "Don't look at me like I'm stupid. I'm valorous, remember? You said it yourself."
    scene w3_4700 with dissolve
    mc "Well, I appreciate you not abandoning me like some loser."
    ver "I appreciate you inviting me out tonight. It's better than being cooped up in a closet."
    scene w3_4701 with dissolve
    ver "...It's a frail thing, but I did say we'd be friends."
    scene w3_4702 with dissolve
    "Like an alcoholic exclamation mark to emphasize her sad point, Veronica tossed back her head and imbibed."
    scene w3_4703 with dissolve
    ver "The alcohol is warming my body, the dancing is fun, and your company has been surprisingly... {i}inoffensive?{/i}"
    scene w3_4704 with dissolve
    mc "My mother always said if they don't find you handsome, let them find you... {i}inoffensive.{/i}"
    scene w3_4705 with dissolve
    ver "I did say you clean up nicely, didn't I?"
    scene w3_4706 with dissolve
    mc "That was a joke, not a setup for a compliment."
    scene w3_4705 with dissolve
    ver "I know, but doesn't it feel nice to hear? What was the occasion?"
    scene w3_4707 with dissolve
    mc "Just a whim, but I'll admit it, I did end up feeling pretty good about it afterwards. It's kinda silly, isn't it?"
    scene w3_4708 with dissolve
    mc "How small things can affect your mood, I mean."
    scene w3_4709 with dissolve
    ver "The little things matter more when you're starved for positivity. That's something I've learned through my work."
    scene w3_4710 with dissolve
    mc "Does complimenting your clients keep them paying you?"
    scene w3_4711 with dissolve
    ver "My job is to make people feel good on both the inside and out, and positive reinforcement helps keep people healthy."
    scene w3_4712 with dissolve
    mct "(Positive reinforcement, huh?)"
    hide screen textbox2 with dissolve

    menu:
        "Tell her she looks nice too.":
            scene w3_4713 with dissolve
            show screen textbox2 with dissolve
            mc "You look good tonight too."
            scene w3_4714 with dissolve
            ver "You're the type who can't stand compliments, huh? Gotta give one after you get 'em?"
            scene w3_4713 with dissolve
            mc "No, I {i}really{/i} like the way you did your hair."
            scene w3_4711 with dissolve
            ver "You noticed that, huh?"
            scene w3_4713 with dissolve
            mc "How could I not? It's on top of your head."
            scene w3_4715 with dissolve
            ver "I just threw it up."
            scene w3_4716 with dissolve
            mc "Really? Not a strand's out of place and you usually wear your hair up differently."
            scene w3_4717 with dissolve
            ver "Well, shouldn't look like a slob. I'm a known face around here."
            scene w3_4716 with dissolve
            mc "Karli said it's been a while since you've been here."
            scene w3_4717 with dissolve
            ver "Yeah, it has..."
            scene w3_4718 with dissolve
            mc "Let's make the most of tonight then."
            scene w3_4719 with dissolve
            ver "...what do you have in mind?"
            scene w3_4729 with dissolve
            "If I really wanted to demonstrate my goodwill, I needed to be bold, maybe at even the cost of my pride..."
        "Pet her head and call her a good girl."(chg=["veronica_down"]):

            $ Veronica_Affection -=1
            scene w3_4720 with dissolve
            show screen textbox2 with dissolve
            mc "Like a dog?"
            ver "Shut up. Don't you even go th--"
            scene w3_4721 with dissolve
            mc "Good girl... {i}good girl{/i}..."
            "Perhaps it was the alcohol that caused me to risk my hand, but it nevertheless found a playful perch on top of Veronica's noggin."
            scene w3_4722 with dissolve
            mc "What? You were just extolling the value of positive reinforcement. Isn't this how you do it?"
            "My head rub became even more intense as I enveloped my fingertips in her fiery-red hair and finagled my way to her scalp."
            scene w3_4723 with dissolve
            ver "What the hell do you think you're doing?"
            "That was a look that didn't find {i}any of that{/i} as endearing."
            scene w3_4724 with dissolve
            mc "Sorry... uh..."
            scene w3_4725 with dissolve
            mc "I guess invading your personal space wasn't as funny as I thought. Heh."
            scene w3_4726 with dissolve
            ver "Definitely not drunk enough to be petted in public, you weirdo."
            scene w3_4727 with dissolve
            mc "Ah, but it'd be cool in pr--"
            scene w3_4728 with dissolve
            ver "......"
            "..."
            scene w3_4730 with dissolve
            "Okay, let's not compound my faux pas. Let's do something to redeem myself."

    scene w3_4731 with dissolve
    "I could invite her to dance again, and further enjoy the two of us spending time together or alternatively I could go invite that bubbly girl and her bookish friend to join us."
    scene w3_4732 with dissolve
    "If everything went well there, the night might end prematurely for me, but I will have done God's work in getting two women to bang."
    mct "(Hmm...)"
    hide screen textbox2 with dissolve

    menu:
        "[mod_option] Do both"(chg=["maid"]):
            scene black with fade
            $ mod_week3_veronica_dance_split = True
            m_dev "Hold up, my Master just wanted me to let you now something, at the end of this \"option\" the choice will be the same as picking \"realstionship/sex route\""
            m_dev "Now back to the game"
            jump mod_week3_veronica_dance_split_both_wing
        "Let go of {b}ALL{/b} your inhibitions and invite Veronica to dance. (realstionship/sex route)"(chg=["veronica_up2"]):

            label mod_week3_veronica_dance_split_both:
            $ Veronica_Affection += 2
            scene w3_4733 with dissolve
            show screen textbox2 with dissolve
            mc "Leeeeeet's..."
            scene w3_4734 with dissolve
            mc "Let's dance. I'm lubed up and you're about to be {b}impressed.{/b}"
            scene w3_4735 with dissolve
            ver "Nice phrasing."
            scene w3_4736 with dissolve
            mc "Come on. The dance floor is calling our names."
            "{i}I turned on the cheese.{/i}"
            scene w3_4737 with dissolve
            ver "That's perhaps the most agreeable thing that's ever come out of your mouth."
            scene black with fade
            stop music fadeout 3.0
            mc "Who says you only get one chance at a first meeting?"
            jump w3VeronicaDanceOff
        "Play wingman for Veronica. (Freind route bathroom Blowjob)"(chg=["veronica_up"]):

            label mod_week3_veronica_dance_split_both_wing:
            $ Veronica_Affection += 1
            scene w3_4738 with dissolve
            show screen textbox2 with dissolve
            mc "How about I find us some cute girls to drink with? That way you won't be ditching me."
            scene w3_4739 with dissolve
            ver "...you're going to go try and pick up women at a lesbian bar?"
            scene w3_4740 with dissolve
            mc "I can be charming when I want to."
            scene w3_4741 with dissolve
            ver "No you can't."
            scene w3_4742 with dissolve
            mc "Wanna bet?"
            scene w3_4743 with dissolve
            ver "...what are we betting?"
            scene w3_4744 with dissolve
            mc "If I find us a couple of girls, and convince them to come drink with me, you'll call me \"your highness\" the rest of the night."
            scene w3_4743 with dissolve
            ver "What do I get?"
            scene w3_4744 with dissolve
            mc "Doesn't matter, since I'm going to win, but something?"
            scene w3_4743 with dissolve
            ver "Make it your majesty, dweeb."
            scene w3_4745 with dissolve
            mc "Alright. {b}Bet.{/b}"
            scene w3_4746 with dissolve
            ver "Bet."
            scene black with fade
            stop music fadeout 3.0
            mc "Be back in a jiffy."
            jump w3VeronicaGroup

label w3VeronicaDanceOff:
    scene w3_4747 with fade
    "With mismatched strides, we lumbered the short distance to the dance floor."
    mc "Lucky me, this is my song."
    "I was about to fully embarrass myself, but that was okay."
    play music "music/drop-the-tapes.ogg"
    scene w3_4748 with dissolve
    ver "{b}This{/b} is your song?"
    mc "Yeah! Never heard this before in my life, but..."
    scene vd_edance1_a with dissolve
    show vd_edance1 with dissolve
    "In an act of necromancy, I threw caution to the wind."
    "Bone and ligament came to life, bending unnaturally under the control of a rum-fueled spell of black magic."
    "I was by no means a dancer, but... it was funny."
    mct "({i}Was dancing hard?{/i})"
    "Simple repetitive movements and a rare case of body over mind."
    "Just don't think about what you're doing."
    "Just don't conceive of even the faintest possibility of looking stupid."
    "The moment you feel a pang of doubt, {i}that's when you become stupid{/i}."
    "At least that was my utterly {b}soaked{/b} line of thinking."
    "{i}Maybe I did look stupid, but who cares?{/i}"
    mct "(Did I know ANY of these people?)"
    "No."
    scene w3_4749 with dissolve
    "The only person I'll see again is Veronica and her expression said it all."
    ver "Geez..."
    "She found this amusing."
    scene w3_4750 with dissolve
    ver "You're uh... {i}night and day.{/i}"
    scene vd_edance1b_a with dissolve
    show vd_edance1b with dissolve
    mc "Impressed?"
    "......"
    "..."
    ver "Fuck, I'm not even going to lie. Kinda."
    "That was ALL I wanted to hear, all I needed to, before my mind retreated back into oblivion."
    "Words required logic, and logic risked getting tangled up in treacherous tendrils of inhibition."
    "{i}And right now, I was saying fuck you to inhibition{/i}."
    "Why? What had possessed me?"
    mct "({i}I don't know.{i})"
    "Maybe I was under the delusion that I was proving something to Veronica, that despite circumstance, in the very depths of my being existed a genuine strand of goodwill."
    "Could stupidly shaking my body accomplish that?"
    mct "{b}(Fuck you doubt!){/b}"
    scene w3_4751 with dissolve
    "Another thing in a long list of things not to think about."
    ver "Hmm... alright, alright... you really are full of surprises."
    "The only thing I needed to think about was..."
    scene vd_edance2_a with dissolve
    show vd_edance2 with dissolve
    mct "(The music.)"
    "In some ways, it was like fucking."
    "The same principle applied, at least."
    "Physical exertion. {i}Losing yourself.{/i}"
    "Then the thoughts receded into feelings."
    "{i}Memories{/i} of feelings that hung like stalactites from my brain."
    scene w3_4752 with pixellate
    "{i}Happy memories.{/i}"
    "Memories that, absent of ego, colored my being a lovely, warm shade."
    scene w3_4753 with pixellate
    ver "......"
    ver "..."
    scene vd_edance3_a with dissolve
    show vd_edance3 with dissolve
    "What the hell was any of this?"
    "I had no idea."
    "Not."
    "A."
    "Single."
    "Fucking."
    "Iota."
    "I just let the music groove me, my hips following the cries of the horn and letting my arms ride the highs and lows."
    "I had never moved like this before in my life, and I had a feeling, I might never again."
    "Was this what they called divine inspiration?"
    "Divine intervention?"
    "Serendipity?"
    "All I knew is it made my body tingle."
    "My calves burned."
    "All my meaty insides were sloshing around."
    mct "(Duh, duhduh, duhduh, duuuuh, dduhduhhh.)"
    mct "(Bzzz, buuuh, buh, buh!)"
    ".................."
    "..............."
    "............"
    "........."
    "......"
    "..."
    "Just kidding! It's not over!"
    ".................."
    "..............."
    "............"
    "........."
    "......"
    "..."
    mct "(Fuck yeah, I was--)"
    scene w3_4754 with dissolve
    scene w3_4755 with dissolve
    "--!"
    "Shit. I got a bit too into it and fell on my ass."
    scene w3_4756 with dissolve
    ver "Pffh, haa- haa! That was..."
    "My self-awareness came flooding back."
    "The floor was dirty and I had a few pairs of eyes on me, but..."
    scene w3_4757 with dissolve
    ver "S+ for effort, [mcf]."
    mc "Really...?"
    scene w3_4758 with dissolve
    ver "You should've seen yourself."
    scene w3_4759 with dissolve
    mc "I bet I looked like an idiot."
    scene w3_4758 with dissolve
    ver "You look like someone I want to dance with."
    scene w3_4760 with dissolve
    "......"
    "..."
    scene w3_4761 with dissolve
    ver "Come closer, they're playing my song."
    scene w3_4762 with dissolve
    mc "It's still the same--"
    scene w3_4763 with dissolve
    ver "{b}Exactly.{/b}"
    scene w3_4764 with cmet
    "So we danced."
    "We weren't just two people dancing next to each other."
    "We were dancing together."
    "So we danced, body to body, imbued with a feeling of goodwill."
    scene w3_4765 with w20
    "Maybe Veronica was onto something. Maybe you could learn a lot about somebody from the way they danced."
    "If that was the case, what did I learn about Veronica...?"
    "Nothing revelatory."
    "Just the first page of a long book, but at least it felt like I had finally cracked it open."
    scene w3_4766 with w21
    "She felt things strongly, both good and bad. Through her mindfulness of my own movements, she showed care and patience."
    "There was a fun, sensual streak absent in her exhibition persona that she was willfully putting on display here."
    "Yeah... she was onto something."
    stop music fadeout 3.0
    scene black with fade

    if not persistent.w3VeronicaDance:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3VeronicaDance = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

    "...who needed words?"
    "We stubbornly refused to let go of the goodwill of earlier. Instead, we absconded with a bottle of coffee liqueur and made our way into the cool summer night."
    "......"
    play ambient "sound effects/waves.ogg"
    "..."
    $ renpy.end_replay()
    jump w3VeronicaStroll

label w3VeronicaGroup:
    if not mod_week3_veronica_dance_split:
        $ w3VeronicaWingman = True
    "......"
    "..."
    play music "music/edm-detection-mode.ogg"
    scene w3_4767 with fade
    ver "Goddamn it."
    mc "Impressed? This is Olivia and Brittany."
    $ unread_veronica = True
    $ history_veronica = "I took Veronica out and played wingman for her, hoping some brief fun would be a nice reprieve from her troubles."
    play sound "sound effects/notification.wav"
    scene w3_4768 with dissolve
    show bioupdate with dissolve
    mc "Turns out, Olivia has had her eyes on you all night."
    hide bioupdate with dissolve
    scene w3_4769 with dissolve
    brit "Isn't she cute? Mind if we drink with you?"
    scene w3_4770 with dissolve
    olivia "Um... h-hello."
    scene w3_4771 with dissolve
    ver "...{i}hey.{/i}"
    scene w3_4772 with dissolve
    "Veronica looked very amused by the nerdy girl's faltering tone."
    scene w3_4773 with dissolve
    ver "I'm Veronica."
    scene w3_4774 with dissolve
    olivia "...you're taller up close."
    "For a moment, it looked like Olivia was running the calculation in her head and liking what was outputted."
    scene w3_4775 with dissolve
    ver "You're deceptively forward, aren't you?"
    scene w3_4776 with dissolve
    olivia "...a-ah... was that awkward of me to say?"
    scene w3_4775 with dissolve
    ver "I'm okay with forward."
    scene w3_4777 with dissolve
    brit "Olivia's coming out of her first relationship with a woman and this is her first time trying something like this."
    olivia "{size=-5}Don't tell her that, she's going to think I'm a...{/size}"
    scene w3_4778 with dissolve
    ver "I get it, break ups are hard, but you want to meet new people and it's hard. I've been there."
    olivia "...you have?"
    scene w3_4779 with dissolve
    ver "Yeah, I'd love for you two to join us."
    brit "Awesome!"
    scene w3_4780 with dissolve
    brit "We'll take over here."
    "...{i}I was caught.{/i}"
    scene w3_4781 with dissolve
    ver "You set me up. You don't think I saw you and blue-hair talking?"
    scene w3_4782 with dissolve
    mc "Isn't it on you if you didn't think something was amiss when I was so confident about our bet?"
    scene w3_4783 with dissolve
    "......"
    "..."
    hide screen textbox2 with dissolve

    menu:
        "Insist on the bet(w3VeroHighness=True).":
            $ w3VeroHighness = True
            scene w3_4784 with dissolve
            show screen textbox2 with dissolve
            mc "A bet is a bet, Veronica."
            scene w3_4785 with dissolve
            ver "So it is, your highness."
        "You were just messing around. Let the terms of your bet go. ":
            scene w3_4786 with dissolve
            show screen textbox2 with dissolve
            mc "Alright. Point made. The bet is invalidated."

    scene w3_4787 with dissolve
    mc "Cute girl though, isn't she?"
    scene w3_4788 with dissolve
    ver "She reminds me of someone."
    scene w3_4789 with dissolve
    mc "Who?"
    scene w3_4790 with dissolve
    ver "You."
    scene w3_4791 with dissolve
    mc "That's offensive. Do you think everyone with glasses and brown hair looks alike?"
    scene black with fade
    mc "...or does that mean I'm cute?"
    "Two or four people, it turned out, didn't make much of a difference. The locale's offerings were just the same."
    scene w3_4792 with w20
    "Drinking..."
    scene w3_4793 with w21
    "Dancing..."
    show screen textbox2 with dissolve
    scene w3_4794 with w12
    "Drinking, some more..."
    brit "No shiiiiiit?! That means you were on TV?!"
    "Olivia had her mousey charms and Brittany was {i}quite{/i} friendly."
    scene w3_4795 with dissolve
    ver "Just briefly."
    scene w3_4796 with dissolve
    olivia "Wow, that's..."
    "Every so often, Veronica would steal a conspiratorial glance, looking at ease."
    "{i}This was a good call{/i}."
    scene w3_4797 with dissolve
    ver "Not really!"
    "More people meant it was easier to forget about just how we were connected in the first place. One-on-one, the club lingered, but in a group... it was pure socializing."
    scene w3_4798 with dissolve
    brit "...so, what do {b}you{/b} do for work, [mcf]?"
    "Plus, it was just nice being able to sit back and not feel like I had to keep the conversation going."
    scene w3_4799 with dissolve

    if w3VeroHighness == True:
        ver "His highness is an investment banker."
        "Veronica swooped in, deftly saving me from the chance of fumbling my lie."
        scene w3_4800 with dissolve
        brit "Really? Huh!"
    else:
        ver "He's an investment banker."
        "Veronica swooped in, deftly saving me from the chance of fumbling my lie."
        scene w3_4800 with dissolve
        brit "Really? Huh!"

    scene w3_4801 with dissolve
    ver "I mean, doesn't he look like a prick? He's got a lot of money though."
    "...was that her version of playing wingman?"
    scene w3_4802 with dissolve
    brit "Pftt-! You two are an odd pair!"
    scene w3_4803 with dissolve
    mc "You're one to talk, considering how different you two seem to be."
    scene w3_4804 with dissolve
    brit "It's symbiotic. I like to yak my head off and she's good at listening."
    scene w3_4803 with dissolve
    mc "Same, but instead of listening, I give Veronica someone to scowl at."
    scene w3_4805 with dissolve
    ver "I don't scowl, I... uh-"
    scene w3_4806 with dissolve
    mc "Glower? Grimace?"
    scene w3_4807 with dissolve
    ver "Shut up!"
    scene w3_4806 with dissolve
    mc "See...? See what I mean? But she makes it work for her, {i}real{/i} smoldering intensity."
    scene w3_4808 with dissolve
    olivia "Hehe~ Brittany's right. You two are funny. How long have you known each other?"
    scene w3_4809 with dissolve
    ver "Would you believe me if I said we met for the first time tonight?"
    scene w3_4810 with dissolve
    olivia "No...?"
    brit "Absolutely not!"
    ver "I guess it just feels like it then."
    scene w3_4811 with dissolve
    ver "...so literature? What's your--"
    scene w3_4812 with dissolve
    brit "Hey, you."
    scene w3_4813 with dissolve
    mc "They seem to be getting along."
    scene w3_4812 with dissolve
    brit "Yeah, and I should say thanks for helping me get Liv out of her shell."
    scene w3_4814 with dissolve
    mc "Thanks received, but my friend has been having a tough time too. So, {i}symbiotic{/i}."
    scene w3_4812 with dissolve
    brit "Is that why you're here tonight?"
    scene w3_4813 with dissolve
    mc "Well, I don't normally drink at lesbian bars."
    scene w3_4815 with dissolve
    brit "I guess we're kinda in the same bucket."
    scene w3_4816 with dissolve
    mc "...or is it more like a jungle?"
    scene w3_4817 with dissolve
    brit "Heh. See any snakes?"
    mc "Don't underestimate my friend."
    scene w3_4818 with dissolve
    brit "What do you--"
    brit "Woah!"
    scene vd_lez1_a with dissolve
    show vd_lez1 with dissolve
    mc "She's gonna eat yours alive."
    "It {i}was{/i} interesting to see Veronica comfortably work and hunt in her own territory."
    ver "It sounded like you two just needed time apart."
    olivia "Ah, ha, yeeeeah... that's what she said..."
    ver "Well... you're young, you're a student... none of it's wasted time. It's all a building block to make you the wonderful person you'll become one day."
    ver "Try to keep a healthy perspective on it."
    olivia "I know a lot of bitter people that could just easily--"
    scene w3_4819 with dissolve
    olivia "Ah-!"
    ver "It's difficult to build anything if frustration and bitterness prevail."
    ver "You'll be wonderful. You gotta think it to achieve it."
    scene w3_4820 with dissolve
    olivia "Ah, heh... you got such big hands..."
    scene w3_4821 with dissolve
    ver "You're not listening to me at all, are you?"
    olivia "I a-am!"
    scene w3_4822 with dissolve
    brit "Damn, no kidding, but it's what I was counting on. Someone with experience to take the lead."
    brit "Your friend has got total mommy vibes, y'know?"
    brit "Muscle~ mommy~"
    scene w3_4823 with dissolve
    mc "...are you sure we're in the same bucket?"
    brit "I'm just speaking objectively. FYI, I am very {i}firmly{/i} into dudes."
    scene w3_4824 with dissolve
    brit "...or is it the \"Blue is the Warmest Color\" thing I got going on up here?"
    scene w3_4825 with dissolve
    mc "I've been told everyone's a little bit gay. You wouldn't ever...?"
    brit "Not really my bag, but I guess there's a world. Romance and sex ARE two different things. But for me..."
    scene w3_4826 with dissolve
    brit "*Glug, glug, glug~*"
    scene w3_4827 with dissolve
    brit "Mmmh, one is a pretty narrow interest and the other is absolutely non-existent."
    mc "Are you saying you're a v--"
    scene w3_4828 with dissolve
    brit "No! God no! I'm aromantic!"
    scene w3_4829 with dissolve
    mc "... is that a thing outside of chemistry?"
    scene w3_4830 with dissolve
    brit "They've got a lot more words for things nowadays. It means I don't feel romantic attraction. Don't know why, it's just never clicked that way in my head."
    scene w3_4831 with dissolve
    brit "I feel the other kind of attraction though."
    "If I had to be honest... after Felicia, the flirtation of a normal woman seemed quaint."
    scene w3_4832 with dissolve
    mc "Isn't that called just being a guy?"
    scene w3_4833 with dissolve
    brit "You got a dim view of your gender."
    scene w3_4832 with dissolve
    mc "No, I've got a dim view of myself that I unfairly extrapolate to my gender. Don't we all?"
    scene w3_4834 with dissolve
    brit "Ha, that's--"
    scene w3_4835 with dissolve
    ver "You're not even listening to me anymore are you?"
    "Both our attentions were stolen by the Amazon and her companion."
    scene w3_4836 with dissolve
    olivia "Am too..."
    scene w3_4835 with dissolve
    ver "What did I say?"
    scene w3_4837 with dissolve
    olivia "You'd give me a discount."
    scene w3_4838 with dissolve
    ver "You'd be surprised at what a little strength training can do for your dating life."
    scene w3_4837 with dissolve
    olivia "I'd look so silly."
    scene w3_4838 with dissolve
    ver "I'm not saying you'd look like me, just..."
    scene w3_4839 with dissolve
    ver "{size=-5}A little extra stamina in a tight package can do wonders for nights like this."
    scene w3_4840 with dissolve
    olivia "Nights like this?"
    scene w3_4839 with dissolve
    ver "Am I being the too forward one this time?"
    scene w3_4841 with dissolve
    olivia "Uh, ummm...."
    olivia "{b}No.{/b}"
    scene w3_4842 with dissolve
    mc "What are we, spectators? It's kinda weird, don't you think?"
    scene w3_4843 with dissolve
    brit "Well, what do you want to talk about?"
    brit "I'm studying zoology, but you don't really give a shit."
    scene w3_4844 with dissolve
    mc "What's your favorite animal?"
    scene w3_4845 with dissolve
    brit "You're cute. Have I said that before?"
    brit "I'd rather focus on that."
    scene w3_4846 with dissolve
    "......"
    "..."
    scene w3_4847 with dissolve
    brit "I'm feeling a bit... mmmh, how should I say it?"
    brit "Envious...? Competitive?"
    scene w3_4848 with dissolve
    mc "Competitive with your friend?"
    brit "Uh huh. Does that even make any fucking sense? The brain's funny, but there's something about the vibe that's... well..."
    scene w3_4849 with dissolve
    ver "You be the one to do it."
    scene w3_4850 with dissolve
    olivia "......"
    olivia "..."
    scene w3_4851 with dissolve
    brit "It's like seeing a waiter bring out a tasty-looking dessert to another table. You start {i}missing.{/i}"
    scene vd_lez2_a with dissolve
    show vd_lez2 with dissolve
    brit "Isn't my friend just a {i}snack?{/i}"
    "She was one weird chick, but the sight playing out before us did confirm that I had successfully handed Veronica off for the night."
    brit "We should probably give them some space. Don't want to be third wheelin'..."
    "Was I just going to go home now, or...?"

    hide screen textbox2 with dissolve
    menu:
        "Tell her you have a girlfriend and go home." if hanaGF == True:
            scene w3_4852 with dissolve
            show screen textbox2 with dissolve
            mc "Sorry, this would be a good time to tell you I have a girlfriend."
            scene w3_4853 with dissolve
            brit "Aaaaah. Got it."
            "She seemed pretty cool about it. She didn't make it awkward or, if she was second guessing if I was telling the truth, her face bore an inscrutable smile."
            scene w3_4854 with dissolve
            brit "I'll call tonight a win regardless."
            mc "Yeah. Looks like we both succeeded in our mission tonight."
            brit "And how."
            scene w3_4855 with dissolve
            mc "Hey, Vero."
            scene w3_4856 with dissolve
            "......"
            "..."
            scene w3_4857 with dissolve
            ver "Y-yeah?"
            scene w3_4858 with dissolve
            mc "I'm going to head out. You seem to be in good hands."
            brit "Me too, Liv."
            scene w3_4859 with dissolve
            olivia "Oh, no, you don't- we can-"
            brit "Enjoy yourself munchkin."
            ver "Hey, [mcf]. C'mere."
            scene w3_4860 with dissolve
            mc "Yeah...?"
            ver "A little closer."
            scene w3_4861 with dissolve
            mc "Yeeeeah....?"
            scene w3_4862 with dissolve
            ver "Thanks for tonight."
            scene w3_4863 with dissolve
            mc "You got it."
            stop music fadeout 3.0
            scene black with fade
            if mod_week3_veronica_dance_split:
                m_dev "Rewind time"
                jump mod_week3_veronica_dance_split_both
            "With that, I parted. Picking up the tab and heading home drunk and by my lonesome."
            "Yet, somehow... I felt pretty warm and good on the inside."
            jump w3June16EndHalf

        "Go home." if hanaGF == False:
            scene w3_4854 with dissolve
            show screen textbox2 with dissolve
            mc "Looks like we both succeeded in our mission tonight."
            brit "And how."
            scene w3_4855 with dissolve
            "Thankfully, Brittany picked up on the fact that I wasn't feeling it and saved us any awkwardness."
            mc "Hey, Vero."
            scene w3_4856 with dissolve
            "......"
            "..."
            scene w3_4857 with dissolve
            ver "Y-yeah?"
            scene w3_4858 with dissolve
            mc "I'm going to head out. You seem to be in good hands."
            brit "Me too, Liv."
            scene w3_4859 with dissolve
            olivia "Oh, no, you don't- we can-"
            brit "Enjoy yourself munchkin."
            ver "Hey, [mcf]. C'mere."
            scene w3_4860 with dissolve
            mc "Yeah...?"
            ver "A little closer."
            scene w3_4861 with dissolve
            mc "Yeeeeah....?"
            scene w3_4862 with dissolve
            ver "Thanks for tonight."
            scene w3_4863 with dissolve
            mc "You got it."
            stop music fadeout 3.0
            scene black with fade
            if mod_week3_veronica_dance_split:
                m_dev "Rewind time"
                jump mod_week3_veronica_dance_split_both
            "With that, I parted. Picking up the tab and heading home drunk and by my lonesome."
            "Yet, somehow... I felt pretty warm and good on the inside."
            jump w3June16EndHalf
        "Be bold. No harm in both of you having some fun tonight(hanaTwoTime = True, hanacheat +1).":

            if hanaGF == True:
                $ hanaTwoTime = True
                $ hanaCheat +=1
            scene w3_4864 with dissolve
            show screen textbox2 with dissolve
            mc "You think I'm cute, do you?"
            scene w3_4865 with dissolve
            brit "{b}Very{/b} cute."
            scene w3_4864 with dissolve
            mc "Well, looks like we both succeeded in our mission tonight."
            scene w3_4866 with dissolve
            mc "It wouldn't hurt for us to have some fun."
            "She said she liked the vibe worming its way in from our periphery..."
            scene w3_4867 with dissolve
            mc "May I...?"
            scene w3_4868 with dissolve
            mct "(I could muster some of that.)"
            scene w3_4869 with dissolve
            mc "Come closer."
            brit "Alright~"
            scene w3_4870 with dissolve
            mc "Not like that."
            "I nodded toward Veronica and her lap warmer, hoping she'd get the picture."
            scene w3_4871 with dissolve
            brit "..."
            scene w3_4872 with fade
            "She got the message, all the while looking like she wanted to say something, but stopping herself in favor of reading my expression."
            "......"
            scene w3_4873 with dissolve
            "..."
            mc "Wanna make a bet?"
            scene w3_4874 with dissolve
            brit "Suuuure~"
            scene w3_4873 with dissolve
            mc "I've got the biggest dick you've never seen."
            scene w3_4875 with dissolve
            brit "Does that line usually work?"
            scene w3_4876 with dissolve
            mc "You're the first one I've tried it on. You're not a-curious too, are you?"
            stop music fadeout 3.0
            scene w3_4877 with dissolve
            brit "......"
            brit "..."
            scene w3_4878 with dissolve
            brit "Heheh~"
            scene black with fade
            "......"
            "..."
            jump w3BathroomFrollick



label w3VeronicaStroll:

    scene w3_4879 with wet
    "The music no longer reached us, but our bodies did not know that."
    "Every step into the inky black night was devil-may-care, as we made way too much fucking noise, all sense of propriety vacated by our earlier revelry."
    scene w3_4880 with dissolve
    ver "--Then the son of a bitch flew out the door and shouted \"he's in the laundry room\" and I had never seen someone so blinded by rage before. I thought I was going to see someone die that night."
    "I never liked the feeling of {i}otherness{/i} that came from partying, but right now, it felt liberating."
    scene w3_4881 with dissolve
    mc "Why the hell did he snitch like that?"
    ver "Thought it would be funny I guess."
    mc "Man, that's fucked up. Did your friend get hurt?"
    $ renpy.music.set_volume(.2, 3, channel = "ambient")
    play music "music/smooth-and-cool.ogg" fadein 6.0
    scene w3_4882 with dissolve
    ver "Nah. Luckily, the team held him back until he came to his senses, but THAT'S why you shouldn't fuck around with Roman candles."
    mc "I was... I was just joking. Heh..."
    scene w3_4883 with dissolve
    "So she didn't like my bad idea."
    mc "Like we could even find a fireworks store open at this time of the evening..."
    scene w3_4884 with dissolve
    "......"
    scene w3_4885 with dissolve
    "..."
    scene w3_4886 with dissolve
    "Was {i}she{/i} the responsible one right now?"
    scene w3_4887 with dissolve
    mc "It's a nice night, don't you agree? I don't get to this side of the city too often."
    scene w3_4888 with dissolve
    mc "Ahhhh-"
    "I paused for a moment to listen to the sound of waves breaking against the city's edge, as well as take in the briny sea smell."
    scene w3_4889 with dissolve
    "We were alone."
    "Surprisingly alone, in stark contrast to the jungle of people from whence we had escaped."
    scene w3_4890 with dissolve
    mc "Yep, it's really nice."
    ver "I, uh... heh..."
    mc "You don't think so?"
    scene w3_4891 with dissolve
    ver "If you make fun of me, I'm going to punch you."
    scene w3_4892 with dissolve
    "......"
    "..."
    scene w3_4891 with dissolve
    ver "I think it's kinda scary."
    scene w3_4892 with dissolve
    "I waited, giving her time to elaborate."
    scene w3_4891 with dissolve
    ver "If I think about it, I find it... {b}suffocating.{/b}"
    scene w3_4893 with dissolve
    ver "The city's pushing at our back, the sky's covering us like a dark blanket, and in front of us..."
    ver "A black and swirling void. It's like there's no escaping."
    scene w3_4894 with dissolve
    mc "Ah, so you're a sad drunk, eh?"
    scene w3_4895 with dissolve
    ver "I'm going to hit you."
    scene w3_4896 with dissolve
    mc "The big woman's afraid of the dark, eh?"
    scene w3_4897 with dissolve
    ver "I'm really going to--"
    scene w3_4898 with dissolve
    mc "It's cool. I slept with a nightlight until I was ten."
    ver "I'm not afraid of the--"
    mc "I know, but can I offer a different perspective?"
    scene w3_4899 with dissolve
    "A frustrated frown told me to continue."
    mc "The city's behind us. It's nice to feel {i}away{/i} and {b}apart{/b} for once."
    mc "I mean... instead of being choked up about it, why not finally breathe?"
    scene w3_4900 with dissolve
    "......"
    "..."
    scene w3_4901 with dissolve
    ver "Aaaah-"
    "In the same exaggerated motion as me."
    scene w3_4902 with dissolve
    ver "Smells like a salty shit."
    scene w3_4903 with dissolve
    mc "Ha! You're... ah.. haha..."
    mc "I like the way you think."
    scene w3_4904 with dissolve
    ver "And you're a bag of surprises yourself."
    scene w3_4905 with dissolve
    mc "Believe me when I say I'm not normally this loosey-goosey."
    scene w3_4906 with dissolve
    ver "Does that usually disarm women?"
    scene w3_4907 with dissolve
    mc "Do you think I'm trying to get in your pants tonight?"
    scene w3_4908 with dissolve
    ver "...ah, who knows? Seems likely."
    scene w3_4907 with dissolve
    mc "You cocky bitch."
    scene w3_4906 with dissolve
    ver "Just admit it, you've got some hope in the back of your mind."
    scene w3_4907 with dissolve
    mc "Why do you always think that?"
    scene w3_4908 with dissolve
    ver "Because I'd try in your position."
    scene w3_4909 with dissolve
    "She was fond of saying that too."
    scene w3_4910 with dissolve
    mc "*Sigh* If I {i}just{/i} wanted to bang you, do you think I'd jump through this many hoops when I could just wait for the inevitable sometime over the next two weekends?"
    scene w3_4911 with dissolve
    ver "Maybe, but the thrill's in the conquest. Having something handed to you for free isn't nearly as fun."
    scene w3_4912 with dissolve
    mc "...and is that what you think I'm doing tonight?"
    scene w3_4913 with dissolve
    "......."
    "..."
    scene w3_4914 with dissolve
    mc "I didn't ask you out tonight scheming to fuck you."
    scene w3_4915 with dissolve
    ver "Honestly? I know you didn't."
    ver "You wouldn't have danced like an embarrassing idiot if you were looking to get laid, but..."
    scene w3_4916 with dissolve
    "......"
    "..."
    scene w3_4917 with dissolve
    mc "...but what?"
    scene w3_4918 with dissolve
    ver "But {b}pride{/b} is a son of a bitch. I'm in this stupid competition because of it, and even now I'm fighting back an irrational anger that tonight has just been you looking down on me."
    scene w3_4919 with dissolve
    mc "You're too tall for me to look down on."
    scene w3_4920 with dissolve
    ver "Ha, ha. {i}Funny fucker.{/i}"
    scene w3_4921 with dissolve
    mc "I'm actually semi-serious. I'm in no position in my own life to be looking down on anyone."
    scene w3_4922 with dissolve
    ver "When has a little self-awareness ever gotten in the way of that?"
    scene w3_4923 with dissolve
    mc "This hasn't been some sort of pity party, either."
    ver "I know! I said it was irrational!"
    scene w3_4924 with dissolve
    "......"
    scene w3_4925 with dissolve
    mc "...it's hard to let go, isn't it?"
    scene w3_4926 with dissolve
    ver "It's so fucking hard, [mcf]. You have no idea."
    scene w3_4925 with dissolve
    mc "Well, you're in this stupid competition because of it."
    scene w3_4927 with dissolve
    ver "Wow! How {i}did{/i} you know?"
    scene w3_4928 with dissolve
    mc "I'm an insightful drunk, with a working short-term memory."
    scene w3_4927 with dissolve
    ver "Well, yeah, news flash! Pride's a prickly bitch! Who doesn't know that?"
    scene w3_4928 with dissolve
    mc "...yet, it's good to have pride in some things."
    scene w3_4929 with dissolve
    ver "Of course it is! A woman {b}should{/b} have pride!"
    scene w3_4930 with dissolve
    ver "Pride in your work."
    ver "Pride in your family."
    ver "Pride in your person."
    scene w3_4931 with dissolve
    mc "...but too much of anything is a bad thing?"
    ver "That's what makes it so thorny. Cause like I said..."
    mc "Yeah. {i}We're here{/i}... at least you can say you're aware of it."
    scene w3_4932 with dissolve
    ver "Well, I'm a \"life coach\", remember? I'd be a shit one if I wasn't aware of what was fucking me in the ass."
    scene w3_4933 with dissolve
    mc "Elegantly put."
    scene w3_4934 with dissolve
    "......"
    scene w3_4935 with dissolve
    mc "...I think, on some levels, refusing to let go of certain things is normal. I've seen it enough, at least."
    scene w3_4936 with dissolve
    "Ian. My mother. Even myself."
    scene w3_4937 with dissolve
    ver "{i}Personally{/i} speaking?"
    scene w3_4938 with dissolve
    mc "...yeah, and in other people too. But the details aren't important."
    scene w3_4937 with dissolve
    ver "We're having a conversation aren't we? Fucking share something with me, you prick."
    scene w3_4939 with dissolve
    mc "...ha, fair enough."
    scene w3_4940 with dissolve
    ver "Uhg, but let's sit down first. The smell of the water is making me dizzy..."
    scene w3_4941 with dissolve
    mc "...so what the fuck were we yammering about?"
    scene w3_4942 with dissolve
    ver "You were {i}just{/i} bragging about your short-term memory."
    scene w3_4941 with dissolve
    mc "Yeah, yeah, yeah, yeah, yeah."
    "I was {i}keenly{/i} feeling the effects of our drinking myself, but I wasn't going to blame it on the sea."
    scene w3_4942 with dissolve
    ver "I wanted you to add your {b}own{/b} experience to this conversation. {b}So we can actually have one{/b}, instead of you just leeching off my side of things so you can get away spot clean."
    scene w3_4943 with dissolve
    "........."
    "......"
    scene w3_4944 with dissolve
    mc "Okay, uh... on the subject of pride and letting go... I really do get why you're doing what you're doing."
    mc "I understand just how much a place can mean to someone."
    scene w3_4945 with dissolve
    mc "Ideals live on up here."
    scene w3_4946 with dissolve
    mc "And they say people live on in here, but..."
    scene w3_4947 with dissolve
    "Veronica shifted her posture, seemingly quite interested in what I had to say."
    scene w3_4948 with dissolve
    mc "A home, or {i}a gym{/i} isn't just four walls with some stuff inside of them. Sometimes we give hallways, rooms, and corridors a deep meaning that we don't want to let go of."
    mc "After my dad died, my mom fought tooth and nail to keep things the same. Things {i}weren't{/i} the same of course, but the trappings were familiar."
    scene w3_4949 with dissolve
    mc "Same home, same school, {i}same TV channels.{/i}"
    mc "As illogical as it is, I don't necessarily think it's stupid or silly to hold onto that meaning."
    scene w3_4950 with dissolve
    mc "We're human beings. That's how we fuckin' roll, eh?"
    scene w3_4951 with dissolve
    ver "...guess you do kinda get it."
    scene w3_4952 with dissolve
    mc "Even more than that, actually..."
    scene w3_4953 with dissolve
    "She looked at me, waiting for even more."
    "...but should I continue?"
    hide screen textbox2 with dissolve

    menu:
        "You're drunk. Be brutally honest(w3VeronicaShared = True).":
            $ w3VeronicaShared = True
            scene w3_4954 with dissolve
            show screen textbox2 with dissolve
            mc "That tooth and nail I was talking about? It's... not all that dissimilar to what you're doing."
            scene w3_4955 with dissolve
            ver "I'd be surprised..."
            scene w3_4956 with dissolve
            mc "You know... she... uh..."
            scene w3_4957 with dissolve
            mc "Eh? You know?"
            scene w3_4958 with dissolve
            "I don't know why I didn't just say it outright. I was certainly capable of it."
            scene w3_4957 with dissolve
            mc "On camera."
            scene w3_4958 with dissolve
            ver "Ah..."
            scene w3_4959 with dissolve
            mc "So, yeah. I get both the reason and the directions that can take you."
            mc "I wish I didn't. It's actually kinda done a number on me..."
            scene w3_4960 with dissolve
            ver "I bet. My dad fucked up my shit and he did it in a socially acceptable way."
            scene w3_4959 with dissolve
            mc "There's nothing shameful about it!"
            scene w3_4960 with dissolve
            ver "I wasn't saying there was."
            scene w3_4959 with dissolve
            mc "...sorry, I know. I don't know why I feel so defensive all of a sudden."
            scene w3_4960 with dissolve
            ver "Opening up to someone can do that."
            scene w3_4961 with dissolve
            "...wait, is that what I'm doing? When did I start opening up to {i}Veronica{/i} of all people? Or am I just leveraging my past as part of my job?"
            scene w3_4954 with dissolve
            mc "To keep it on topic, I guess it's a thing I can't let go of. Never have been, ever since I learned about it."
            mc "Logically I know it's not a big deal, but it's always lingered in the back of my mind. Especially now that I have this job, I've been thinking about it more and more lately."
            scene w3_4962 with dissolve
            mc "I see it in Rosalind. I see it in you. I even see it in Felicia."
            scene w3_4963 with dissolve
            "........."
            scene w3_4959 with dissolve
            mc "...I wish the best for you three."
            scene w3_4960 with dissolve
            ver "I believe you."
            scene w3_4954 with dissolve
            mc "...you do?"
            scene w3_4964 with dissolve
            ver "Yeah."
            scene w3_4965 with dissolve
            "......"
            "..."
            scene w3_4966 with dissolve
            ver "Makes sense too. You've got to be all sorts of screwy to hug a crying, naked woman, and tell her you want to be a friend."
            scene w3_4967 with dissolve
            "......"
            "..."
            scene w3_4962 with dissolve
            mc "...so, I shared. What about you?"
            mc "Are you having second thoughts about your choices?"
            scene w3_4955 with dissolve
            ver "I was just saying you're an easy target for my anger and I know it."
        "Don't overshare.":

            scene w3_4962 with dissolve
            show screen textbox2 with dissolve
            mc "With the way you brought up the pride stuff.. are you having second thoughts about your choices?"
            scene w3_4955 with dissolve
            ver "I was just saying you're just an easy target to be angry at and I know it."

    scene w3_4968 with dissolve
    mc "Well... it's not {i}entirely{i} unwarranted."
    scene w3_4969 with dissolve
    ver "Maybe, but my dumb brain does think being angry at other people is better than being angry at myself, which is, let me tell you... {b}nooooot{/b} helpful."
    scene w3_4968 with dissolve
    mc "At least it's a motivator, right?"
    scene w3_4969 with dissolve
    ver "Yeah, one that's just as likely to have you do something stupid as much as {i}whatever{/i}."
    scene w3_4968 with dissolve
    mc "This plays out in your head a lot?"
    scene w3_4969 with dissolve
    ver "Too much. It'd even be {i}fascinating{/i} if it didn't sting like a bitch."
    scene w3_4970 with dissolve
    ver "I mean... the way you can know a decision is stupid, knowing what the outcome will be, yet you do it anyway?"
    ver "Smoking... over-eating... holding onto a failing business and, in the process, convincing the one person you found that could actually stomach you that you're {i}really{/i} {b}everything{/b} you're afraid you are."
    scene w3_4971 with dissolve
    ver "Sometimes I'm not even sure if I have a good reason to be angry anymore, but I can't turn it off. It's like watching a knife enter your body in slow-motion and just letting it happen."
    scene w3_4972 with dissolve
    mc "Are you sure you're not having second thoughts?"
    "...was I asking because it was my job to make sure she wasn't or was it? Was that it, or...?"
    scene w3_4973 with dissolve
    ver "Never, ever. Until the bitter end. That's just how my stupid heart works."
    scene w3_4974 with dissolve
    "Or was what I'm feeling right now a genuine pang of concern?"
    "......"
    scene w3_4975 with dissolve
    mc "...you look like you could use a drink."
    scene w3_4976 with dissolve
    ver "...thanks."
    scene w3_4977 with dissolve
    "There {i}was{/i} something bugging me about her words..."
    scene w3_5025 with dissolve
    mc "I'm going to say something, even though you're going to think I have ulterior motives."
    scene w3_5026 with dissolve
    ver "Just say it."
    scene w3_5027 with dissolve
    mc "Well, it's been a lot of dumb brain this and stupid heart that, but..."
    "It {i}was{/i} my job to make sure she kept trucking, but that didn't mean I didn't believe what I was about to say."
    mc "I think you're pretty cool. Nah, actually..."
    scene w3_5028 with dissolve
    mc "I know you're pretty cool. You're tenacious, you know?"
    mc "Like, seriously? The balls on you to try and unionize the Carnations yesterday."
    scene w3_5029 with dissolve
    ver "Not really. I'm just throwing myself against walls."
    scene w3_5030 with dissolve
    mc "There's something romantic to be said of going down kicking and screaming."
    scene w3_5031 with dissolve
    ver "From your comfortable, dick-swinging perspective maybe."
    scene w3_5032 with dissolve
    mc "Just take the fucking compliment! You're a strong person and you have some qualities that I {i}genuinely{/i} admire."
    mc "You hold yourself to a standard, you're clearly hard-working, you keep moving, and you're willing to self-reflect."
    "Some of her decisions may be questionable, but..."
    scene w3_5033 with dissolve
    mc "You're fucking cool. No question about it."
    scene w3_5034 with dissolve
    ver "......"
    ver "..."
    scene w3_5035 with dissolve
    ver "{i}Stupid{/i} kid."
    scene w3_5036 with dissolve
    mc "{i}Dumb{/i} old bitch."
    scene w3_5037 with dissolve
    ver "Ah, hehehe~"
    "......"
    scene w3_4977 with dissolve
    "..."
    "As our words receded, and there was only moonlight between us, I was left with an impression."
    scene w3_4978 with dissolve
    "Despite her defeatism, or maybe in tandem with it, the moon lent Veronica's pale skin a transient, ethereal-like beauty."
    scene w3_4979 with dissolve
    "I hadn't invited her out to make a move on her, {i}that was the truth{/i}, but at the moment..."
    scene w3_4980 with dissolve
    "I'd be full of shit if I said I didn't feel a pull right about now."
    scene w3_4981 with dissolve
    ver "What a strange pair of drinking buddies we are."
    scene w3_4982 with dissolve
    mc "You said it."
    scene w3_4983 with dissolve
    "......"
    "..."
    scene w3_4984 with dissolve
    ver "Pffh!"
    mc "...what is it?"
    scene w3_4985 with dissolve
    ver "Your face is red!"
    mc "...I'm drunk."
    scene w3_4986 with dissolve
    ver "...it's even redder now that I mentioned it!"
    mc "I'll just have to take your word for it, since I can't see my own face or feel it for the matter."
    mc "Speaking of which..."
    scene w3_4987 with dissolve
    "I don't half-ass things. Let's never feel my face again~"
    "........."
    "......"
    "..."
    scene w3_4988 with dissolve
    mct "(Ah...?)"
    mc "Mmmmmhh...?"
    scene w3_4989 with dissolve
    mc "...s'all gone."
    scene w3_4990 with dissolve
    mc "We should've lifted two bottles. What the hell do we do now?"
    scene w3_4991 with dissolve
    ver "Should we just call it a night?"
    scene w3_4990 with dissolve
    mc "Is that what you want to do?"
    scene w3_4992 with dissolve
    ver "Not really. Go home and sleep in my closet? {b}Fuck.{/b}"
    scene w3_4993 with dissolve
    ver "I mean..."
    scene w3_4994 with dissolve
    ver "{b}Fuuuuuuuuuuuuck!{/b}"
    scene w3_4995 with dissolve
    "Veronica screamed into the night, but the only thing that called back was a pale imitation."
    scene w3_4996 with dissolve
    ver "If it's up to me, I'll take this salty-shit air, thank you very much."
    scene w3_4997 with dissolve
    mc "........."
    mc "......"
    scene w3_4998 with dissolve
    mc "...alright. That settles it. We may be out of booze, but..."
    scene w3_4999 with dissolve
    mc "We still have our feet."
    scene w3_5000 with dissolve
    ver "Pssh, what? Yeah... yeah right."
    mc "I thought you loved dancing."
    scene w3_5001 with dissolve
    ver "You want to drunkenly dance in the moonlight?"
    mc "... uh, which part of that is the problem? Is it cause there's no music?"
    stop music fadeout 3.0
    scene w3_5002 with dissolve
    mc "If that's the case, {b}hoooold on{/b}, I can fix that."
    mc "It's a poor stand-in for a stereo and we've got shit acoustics, but--"
    scene w3_5003 with dissolve
    "......"
    "..."
    scene w3_5004 with dissolve
    mc "{b}Here.{/b}"
    play music "music/blue-mood.ogg" fadein 3.0
    scene w3_5005 with dissolve
    mc "And the Lord said, let there be music!"
    scene w3_5006 with dissolve
    "........."
    "......"
    scene w3_5007 with dissolve
    ver "...this is so stupid."
    scene w3_5008 with dissolve
    mc "You didn't think it was stupid when there were people around, so why is it stupid now?!"
    scene w3_5009 with dissolve
    ver "...because I said it is!"
    scene w3_5008 with dissolve
    mc "Oh, is that it?"
    scene w3_5009 with dissolve
    ver "How do you not think it is?!"
    scene w3_5010 with dissolve
    mc "Juuuust dance with me, Veronica. Pleeeeease!!!"
    mc "It's a nice night."
    scene w3_5011 with dissolve
    "..............."
    scene w3_5012 with dissolve
    "............"
    "........."
    scene w3_5011 with dissolve
    "......"
    scene w3_5013 with dissolve
    ver "...fine!"
    scene w3_5014 with dissolve
    ver "One more dance to end the night, okay?!"
    scene w3_5015 with dissolve
    mct "(...what am I doing?)"
    mct "(Why aren't I just going home?)"
    "Those questions fought hard to penetrate through the inebriated fog."
    scene w3_5016 with dissolve
    ver "...but let's do it slowly."
    scene w3_5017 with dissolve
    mc "Right. Don't want to get dizzy, do we?"
    scene w3_5018 with dissolve
    ver "...that means you should use your scrawny arms to hold onto me."
    scene w3_5019 with dissolve
    mc "Like this?"
    scene w3_5020 with dissolve
    ver "...no need to be ginger about it. Go lower, grab my waist."
    scene w3_5021 with dissolve
    mc "You sure are demanding for someone blasé on the idea."
    scene w3_5022 with dissolve
    ver "I mean, if we're going to dance by the ocean - AT NIGHT - how else would we do it?"
    scene w3_5021 with dissolve
    mc "Alright~"
    scene w3_5023 with dissolve
    "Quickly, and with feeling, I pulled us chest-to-chest."
    "My head felt fuzzy, too fuzzy, and Veronica deceptively soft."
    scene w3_5024 with dissolve
    mc "Shall we?"
    $ renpy.music.set_volume(.6, 3, channel = "ambient")
    scene w3_5038 with dissolve
    "That was how, enveloped on all sides by darkness, we began our dance."
    scene w3_5039 with dissolve
    "Surprisingly, I took the lead, the headstrong woman ceding to my sluggish movements."
    scene w3_5040 with dissolve
    ver "Your choice in music is weird..."
    scene w3_5039 with dissolve

    if w2ExEndingVeronica == True:
        mc "Yeah? You don't like it? And what's on your workout mix, Ronnie? Speed metal?"
    else:
        mc "Yeah? You don't like it? And what's on your workout mix? Speed metal?"

    scene w3_5041 with dissolve
    ver "...uh, mostly a mix of early 2000s pop songs."
    scene w3_5039 with dissolve
    mc "Damn. You're old."
    scene w3_5042 with dissolve
    ver "What? You were alive then too!"
    scene w3_5043 with dissolve
    mc "Barely. The first ten years of your life hardly count as living."
    scene w3_5044 with dissolve
    ver "Fuck you, you're a baby."
    $ renpy.music.set_volume(.2, 2, channel = "ambient")
    scene w3_5045 with dissolve
    mc "Hehehe-"
    scene w3_5046 with dissolve
    "In actuality, I don't think either of us was dancing to the shallow sound of my phone's speakers, nor was it the breaking of the waves that timed our steps."
    scene w3_5047 with dissolve
    "The playback was entirely in our murky, diluted heads."
    scene w3_5046 with dissolve
    ver "Well, maybe this wasn't a stupid idea..."
    scene w3_5049 with dissolve
    mc "You sure you're not saying that because it beats the alternative?"
    scene w3_5046 with dissolve
    ver "Pretty sure..."
    jump w3VeronicaBeachKiss


label w3VeronicaBeachKiss:
    if _in_replay:
        play ambient "sound effects/waves.ogg"

    scene w3_5047 with dissolve
    "Even if my senses were dull, the mood being what it was, the question that I should've been asking myself finally surfaced."
    "{i}What exactly was I doing by asking her to dance alone like this?{/i}"
    scene w3_5046 with dissolve
    "Was Veronica on the money with her accusation? Was I going in for the kill on a lonely, liquored-up divorced woman on a hot summer night?"
    "{i}Did I simply want to dance with a \"friend\", full stop?{/i} Was I just seeing where it all lead?"
    scene w3_5048 with dissolve
    mct "(What am I doing...?)"
    "For a moment that turned into minutes, I didn't search for the answer to that question, as it would be difficult to outright untangle it from the muddied mess caking the inside of my skull."
    scene w3_5050 with dissolve
    "So for minutes that turned into a big moment, it just sat square in my brain, marinating until the answer cooked itself."
    scene w3_5051 with dissolve
    "Until the mood was thick, and I was all too conscious of the red-headed beauty."
    scene w3_5052 with dissolve
    mc "Your face is red."
    scene w3_5053 with dissolve
    ver "...the night's cool and you're warm."
    scene w3_5054 with dissolve
    "There {i}were{/i} some things I implicitly knew about this situation, however."
    scene w3_5055 with dissolve
    "I knew I enjoyed her company tonight."
    "I knew, without a doubt, I found Veronica attractive."
    scene w3_5056 with dissolve
    "I also knew that with one willful act she may very well give herself to me."
    "Yet, rejected or not, all the goodwill I built over the past few days might just be expended in an instant."
    "...but what was the point of this goodwill? It would all evaporate in a week and a half, and we would never see each other again. This night might be the one chance for me to have her on our own terms."
    scene w3_5055 with dissolve
    "The cautious side of my brain, bogged down by rum and desperate to be heard, whispered not to do it."
    "However, the uninhibited animal side of my brain, emboldened by the liquor, was much more certain of the outcome."
    hide screen qmenu with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Do it.":
            pass
        "Do it.":
            pass
        "Don't do it.":
            scene w3_5057 with dissolve
            show screen qmenu with dissolve
            show screen textbox2 with dissolve
            "Whether it would happen for the right or wrong reasons, I pulled back."
            "I resisted."

            if hanaGF == True and w3MinaRejection == False and minaCleanStart == False:
                show screen qmenu with dissolve
                mct "(I would...)"
                scene w3_5080 with pixellate
                "Keep my promise."
                "It doesn't do to be greedy..."
                scene w3_5058 with pixellate
            else:
                scene w3_5058 with dissolve

            show screen qmenu with dissolve
            ver "You had a pretty obvious look on your face."
            scene w3_5059 with dissolve
            mc "No, I didn't."
            scene w3_5058 with dissolve
            ver "Did too."
            scene w3_5059 with dissolve
            mc "...I'm drunk."
            scene w3_5057 with dissolve
            "I offered the same excuse as last time."
            scene w3_5058 with dissolve
            ver "Yeah... we are..."
            scene w3_5057 with dissolve
            "......"
            "..."
            scene w3_5060 with dissolve
            ver "I guess you changed your mind."
            scene w3_5061 with dissolve
            "The pull wasn't just in my head; there was a moment there and she had felt it too."
            scene w3_5062 with dissolve
            mc "What are you talking about? Isn't {i}this{/i} nice?"
            scene w3_5060 with dissolve
            ver "It takes some getting used to, but..."
            scene w3_5058 with dissolve
            ver "Yeah. Turns out I'm starved for this kinda sappy shit."
            scene w3_5059 with dissolve
            mc "You know earlier... I never danced like that before in my life. It was fun."
            mc "Guess you brought it out of me..."
            scene w3_5058 with dissolve
            ver "You're not going to blame the alcohol for the third time tonight?"
            stop music fadeout 3.0
            scene w3_5059 with dissolve
            mc "Credit where credit is due."
            scene w3_5063 with dissolve
            mc "Ah... the song's over..."
            scene w3_5064 with dissolve
            ver "Who cares? Let's just keep on for a little while... please?"
            scene w3_5065 with dissolve
            mc "Sure, I don't have anywhere to be..."
            scene w3_5066 with dissolve
            "It felt reassuring that this time she was the one to pull me into the hug."
            "Veronica's grip {i}was{/i} secure and comforting..."
            mct "(Wouldn't it be nice if this night went on longer...?)"
            scene black with fade
            "......"
            "..."
            hide screen textbox2 with dissolve

            menu:
                "On second thought(if hana gf,hanatwotime=True and hanacheat+1)."(chg=["veronica_up2"]):
                    $ Veronica_Affection += 2
                    if hanaGF == True:
                        $ hanaTwoTime = True
                        $ hanaCheat +=1
                    scene w3_5067 with dissolve
                    show screen textbox2 with dissolve
                    mct "(Ah, fuck it!)"
                    ver "Mmmh...?!"
                    scene vd_promekiss1_a with dissolve
                    show vd_promekiss1 with dissolve
                    "The mood's the fucking mood. Screw my doubts, screw the calculus of \"goodwill\" - whatever the fuck that is."
                    "Veronica is open to this just as much as I am."
                    scene w3_5068 with dissolve
                    ver "I wasn't saying I'm starved-- I w-wasn't looking for you to ki--"
                    scene vd_promekiss1_a with dissolve
                    show vd_promekiss1 with dissolve
                    ver "MMmhhh!"
                    "Despite her protest, she was quick to kiss me back."
                    "Her tongue explored my mouth with a remarkable degree of control."
                    "To my mind and my body, it seemed an explosive taste of things to come."
                    scene vd_promekiss2_a with dissolve
                    show vd_promekiss2 with dissolve
                    ver "Ah, hhhh~ *chwup~*"
                    "It told me that what came after this wouldn't be one-sided, and there was a growing anticipation in my perverted heart about how she might use her strength and flexibility on me..."
                    ver "Mmmhh, hhh..."
                    "...or how I might bend those qualities to my pleasure."
                    mct "(The challenge of conquest...)"
                    "{b}Goddamn it...{/b} she wasn't {i}wrong.{/i}"
                    scene w3_5069 with dissolve
                    mc "A-ah... About our conversation earlier..."
                    scene w3_5070 with dissolve
                    ver "What part of it...?"
                    scene w3_5069 with dissolve
                    mc "Good, doesn't matter. Just don't say I told you so."
                    scene vd_promekiss3_a with dissolve
                    show vd_promekiss3 with dissolve
                    "{i}I really hadn't asked her out to drink intending this.{/i}"
                    "However..."
                    scene w3_5071 with dissolve
                    "Intentions don't mean much when put against a tall, full-bodied, lonely beauty."
                    stop ambient fadeout 3.0
                    $ renpy.music.set_volume(1, 0, channel = "ambient")
                    "........."
                    "......"
                    "..."
                    jump w3VeronicaFinallyFuckingPraiseBe
                "Stick to your guns(unread_veronica = True).":

                    $ renpy.end_replay()
                    $ unread_veronica = True
                    $ history_veronica = "I took Veronica out, hoping it would be a nice reprieve from her troubles. I thought better of making a move."
                    play sound "sound effects/notification.wav"
                    show bioupdate with dissolve
                    "No, this was a good place to end it."
                    hide bioupdate with dissolve
                    stop ambient
                    jump w3June16EndHalf
        "Do it(if hanagf, hanaTwoTime=true and hanacheat+1)."(chg=["veronica_up2"]):

            pass

    $ Veronica_Affection += 2
    if hanaGF == True:
        $ hanaTwoTime = True
        $ hanaCheat +=1
    stop music
    show screen qmenu with dissolve
    show screen textbox2 with dissolve
    scene vd_promekiss1_a with dissolve
    ver "Mmmmhh..."
    scene vd_promekiss1_a with dissolve
    show vd_promekiss1 with dissolve
    "The animal side of me knew she wouldn't rebuff me. Veronica was like a wounded deer, after all."
    "She didn't fight it."
    "She didn't push me away."
    "She didn't even act surprised."
    "No, like she was expecting it, she kissed me back."
    ver "Mmmhhhh-"
    scene vd_promekiss2_a with dissolve
    show vd_promekiss2 with dissolve
    "She was showing me that she needed this as much as I wanted it and that she would give as good as she got."
    ver "Ah, haaammm-"
    "She was showing me that it wouldn't be so one-sided, filling me with a growing anticipation in my perverted heart about how she might use her strength and flexibility on me..."
    ver "Mmmhh, hhh..."
    "...or how I might bend those qualities to my pleasure."
    mct "(The challenge of conquest...)"
    "{b}Goddamn it...{/b} she wasn't {i}wrong.{/i}"
    scene w3_5069 with dissolve
    mc "You can blame it on the alcohol and hate me in the morning..."
    scene w3_5070 with dissolve
    ver "Yeah, I may just take you up on that..."
    scene vd_promekiss3_a with dissolve
    show vd_promekiss3 with dissolve
    "{i}I really hadn't asked her out to drink intending this.{/i}"
    "Not that it matters."
    scene w3_5071 with dissolve
    show screen textbox2 with dissolve

    if not persistent.w3VeronicaKiss:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3VeronicaKiss = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)


    "Intentions don't mean much when put against a tall, full-bodied, lonely beauty."
    stop ambient fadeout 3.0
    $ renpy.music.set_volume(1, 0, channel = "ambient")
    $ renpy.end_replay()
    jump w3VeronicaFinallyFuckingPraiseBe


label w3VeronicaFinallyFuckingPraiseBe:
    $ w3VeronicaSex = True
    play music "music/jazz-piano-bar.ogg"
    hide screen textbox2 with dissolve
    scene w3_5072 with Dissolve (4.0)
    "Veronica had no desire to shack up at the gym and my place was out for the obvious reason."
    "So, where to go...? Well..."
    "Our jaunt into the night took us to an {i}intermediary{/i} location."
    play ambient "sound effects/kissing1.mp3"
    scene vds_kiss1_a with dissolve
    show vds_kiss1 with dissolve
    "Our position was secured with a quick and simple phone call that confirmed a date with a certain hair stylist."
    ver "Mmmh, hhhm-"
    "So, wasting no time..."
    ver "Euuhh, mmh-"
    "...and {i}straight to business.{/i}"
    "We left no room for awkward chit-chat or our tiresome brand of back-and-forth."
    "Words might have brought second thoughts, so as soon as we got in the door, Veronica allowed herself to melt into my arms."
    scene vds_kiss2_a with dissolve
    show vds_kiss2 with dissolve
    mc "Mh... *chup~*"
    "The fire was dim."
    mc "Leave it to me..."
    "Dimmed by drink and most likely Veronica's clawing thoughts."
    scene vds_kiss2b_a with dissolve
    show vds_kiss2b with dissolve
    mc "Shut your mind off..."
    "Was she swallowing her anger towards me right now?"
    mc "Get out of your head for a few hours..."
    "Whatever the case, a dim flame burns just the same."
    mc "You can reduce yourself down... *Chwup, chup~* ...or be as complicated as you want."
    "It only needed some {i}stoking.{/i}"
    ver "That, mmmhh--"
    "And every now and then I'd get a shudder out of her signaling I was on the right track."
    ver "...s'what I'm doing, string--"
    play ambient "sound effects/kissing2.mp3"
    scene vds_kiss1b_a with dissolve
    show vds_kiss1b with dissolve
    ver "{size=-5}Mmmmhmhh...{/size}"
    "The faintly cute sounds she was making right now were so unlike her and I {i}loved{/i} that."
    ver "Mmm, hhhm..."
    "It was like hearing a lion purr like a house cat."
    ver "Ewuuh~"
    "The budding cocky bastard in me was beginning to swell, full of thoughts of making the large woman sing to my tune."
    play ambient "sound effects/kissing1.mp3"
    scene vds_kiss2b_a with dissolve
    show vds_kiss2b with dissolve
    mc "When did you~ *chwup* ~decide you were okay with this tonight?"
    ver "Mmh...? Ah... when... when {b}I told you so.{/}"
    play ambient "sound effects/kissing2.mp3"
    scene vds_kiss1b_a with dissolve
    show vds_kiss1b with dissolve
    "{i}Shut up{/i}."
    ver "Mmmh, hhhmm~ hhew-hehe~"
    play ambient "sound effects/kissing1.mp3"
    scene vds_kiss1_a with dissolve
    show vds_kiss1 with dissolve
    "Slowly but surely, the alcohol in our blood would be replaced with each other."
    "Kiss by kiss..."
    "Peck by peck..."
    "...it wasn't enough to get us there."
    scene w3_5073 with dissolve
    "My hand, knowing that and as if possessing a mind of its own, positioned itself to {i}escalate.{/i}"
    mc "Mmmhh~"
    scene w3_5074 with dissolve
    "I had seen them plenty, but that didn't do a damn thing to hamper the anticipation as my fingers bit into Veronica's flesh."
    ver "Ah, mmhhh- mmmmhhh-"
    stop ambient
    scene w3_5075 with dissolve
    "However, unlike a Christmas present..."
    "I was content in slowly unwrapping them."
    scene w3_5076 with fade
    "An intermission in the action gave me the chance to appraise Veronica's expression."
    scene w3_5077 with dissolve
    "......"
    "..."
    scene w3_5078 with dissolve
    ver "I liked it better when your hands and lips were doing something."
    scene w3_5079 with dissolve
    mc "Is that your way of saying you like the way I touch you?"
    scene w3_5078 with dissolve
    ver "Let's get something straight--"
    scene vds_rub1_a with dissolve
    show vds_rub1 with dissolve
    ver "A-ahh... I'm just feeling you out for a minute."
    mc "Is that so...?"
    "Slowly, finger by finger, I ran my hand across her breast, catching and pulling at Veronica's teat."
    mc "You like it when your partners {i}dance{/i} for you then?"
    "Her reply came in the form of a look, and in the way her nipple stiffened against the brush of my fingertips."
    ver "Mmmh... it isn't so bad making a handsome man work for you."
    mc "You like me without my glasses, huh?"
    ver "Don't get ahead of yourself. I don't really like handsome men, I like cute ones..."
    ver "Lucky for you, a little obedience can make you cute."
    "It was stupid..."
    scene vds_rub2_a with dissolve
    show vds_rub2 with dissolve
    ver "You want to be cute for me, [mcf]?"
    "...but being called handsome, from Veronica of ALL people--"
    ver "...you want to be cute for Mommy Veronica?"
    "--{b}was {i}such{/i} a dopamine hit.{/b}"
    stop music fadeout 3.0

    menu:
        "Dance, monkey(w3VeronicaWorship = True).":
            $ w3VeronicaWorship = True
            scene w3_5081 with dissolve
            "I didn't know about obedience, but..."
            scene w3_5082 with dissolve
            "I could do a little devotion."
            scene w3_5083 with dissolve
            "A small kiss here."
            scene w3_5084 with dissolve
            "A small kiss there."
            ver "That tickles..."
            scene w3_5085 with dissolve
            "Attention worthy of a well-sculpted body like hers."
            scene w3_5086 with dissolve
            mc "Don't worry. I'm not going to neglect a single inch of you."
            scene black with fade
            "*Chwup, fhwup~*"
            "Some fumbling with clothes later and..."
            "*{b}Chwup, fhhwup, chup~*{/b}"
            play music "music/brooklyn-nights.ogg"
            scene w3_5087 with fade
            ver "Ah, heh... hehe..."
            scene w3_5088 with dissolve
            "In this position, with a firm grasp on Veronica's forearm, I wasn't really sure who was the obedient one here."
            scene w3_5089 with dissolve
            mc "You're a work of art."
            scene w3_5088 with dissolve
            "Was it the one slathering her with affection or the one letting a pervert have free range at her vulnerable parts?"
            scene w3_5089 with dissolve
            mc "Every part of you deserves some loving attention."
            scene w3_5088 with dissolve
            "However, the question of which one of us was more subservient to our desires was an unimportant one, because..."
            scene w3_5087 with dissolve
            ver "You're not thinking of--"
            scene w3_5088 with dissolve
            "...Veronica's body remained alluring no matter how you turned, twisted, or flexed it."
            scene w3_5087 with dissolve
            ver "It's summer... I'm going to be nast--"
            scene vds_pitlick_a with dissolve
            show vds_pitlick with dissolve
            ver "A-ah... yeeeeah-"
            "Did not care."
            "Slowly, but persistently, I dug my tongue into Veronica's armpits, mapping out its attractive outline as if I'd have a use for it later."
            ver "Hnng... d-don't I taste bad there?"
            "Nope!"
            "It tasted like flesh like any other, but made sweet by drink and the churning sexual desire in my belly."
            ver "A-ah.. hehe--"
            "And, what of the smell...?"
            ver "Heh, you {i}freak.{/i} Ha.. this is... this is actually a little embarrassing..."
            "Veronica's raw stench, developed over the course of a hot summer night?"
            scene vds_pitlick2_a with dissolve
            show vds_pitlick2 with dissolve
            mc "Mmh, hhmhmhmm-"
            "{i}It was honest.{/i}"
            "{b}Raw{/b}."
            "It injected into my nose a conceited feeling that I was probably one of few, if any, to ever attack her from this angle."
            "{i}Freak?{i}?"
            "Right on the money."
            "If I didn't already feel like one, this was to be the advent of my deviancy, no doubt."
            "But, simply put, {i}every part of Veronica was appealing.{/i}"
            "Every curve and divot was worthy of affection."
            "As my tongue scraped the rough and prickly surface, a strange and sudden notion grabbed me."
            scene vds_pitlick_a with dissolve
            show vds_pitlick with dissolve
            "A notion that feverishly burrowed itself into my being, compelling me to demonstrate it in earnest."
            "In this give and take, a woman like Veronica was worthy of worship."
            scene w3_5096 with dissolve
            mc "I love the way you taste and smell."
            scene w3_5097 with dissolve
            ver "Ah, fuck...."
            mc "What?"
            ver "That kind of shit gets you going too...?"
            scene w3_5098 with dissolve
            if w2ExEndingVeronica == True:
                mc "I'm afraid we might just be more simpatico than you're comfortable with, Ronnie."
            else:
                mc "I'm afraid we might just be more simpatico than you're comfortable with."

            scene w3_5099 with dissolve
            ver "Yeah? Well, if only you had a set of tits."
            scene w3_5100 with dissolve
            mc "Lean back."
            mc "You've worked so hard for your body, the least I can do is show you I recognize that."
            scene w3_5101 with dissolve
            ver "...I'll give you ten minutes."
            scene w3_5102 with dissolve
            mc "What happens after ten minutes?"
            scene w3_5101 with dissolve
            ver "You'll see."
            scene black with fade
            "Let's not waste them then."
        "Tell her to kiss you.":

            play music "music/brooklyn-nights.ogg"
            scene w3_5090 with dissolve
            "I swelled with undue confidence."
            scene w3_5091 with dissolve
            mc "Kiss me yourself."
            scene w3_5092 with dissolve
            "Simple ask, but my intention was clear."
            ver "..."
            "Cut the bullshit. {i}She already found me attractive{/i}."
            "The way she was perched on my lap, large freckled ass pressing into my crotch told me she didn't have any qualms about \"handsome\" men."
            scene w3_5093 with dissolve
            mc "I'm waiting, Veronica."
            scene w3_5094 with dissolve
            ver "........."
            ver "......"
            scene w3_5095 with dissolve
            ver "...s'alright."
            scene vds_kiss3_a with dissolve
            show vds_kiss3 with dissolve
            "{b}Yes.{/b}"
            "She sprung forth, closing the gap in a flash, and forming a seal around my mouth."
            mc "Mmmhh~"
            "The feeling of the Amazon's mouth pressed into mine, all of her own volition, was sobering."
            ver "Hmmm, hhhmm-"
            "As was the way she intertwined her tongue with mine."
            "It wasn't a delicate dance, no."
            "It was strong and overpowering, just like her, and fitting for a woman worthy of {i}conquest.{/i}"
            "It was funny how Veronica's words continued to stick in my mind, even as my whole body was hit by a rush of staggering elation."
            mc "Mhh, ahh- *Chwup~*"
            "And it was amazing that a mere kiss, a submissive meeting in the middle from a tempestuous woman, could make one feel powerful."
            "*Chwup, fwhup~*"
            "How it grabbed a man by the brain stem, shook his head's soupy contents vigorously, and cajoled him into thinking {i}I deserve this{/i}."
            scene vds_kiss3b_a with dissolve
            show vds_kiss3b with dissolve
            "In her own way, intentional or not, Veronica was exerting control over me."
            "The sloppy way she thrashed around in my mouth interrupted the constant flow of {i}me, me, me{/i} and replaced it with ego-bereft bursts of white."
            ver "Mmh, hhheea-"
            "Her intermittent moans, let out during brief windows of breathing, went straight into my ears and down to my toes."
            "It was now my turn to {i}melt{/i}."
            mc "Mh, hhaaa-"
            mct "(Veronica--)"
            "--and melt I did, in the strong grasp and comforting shadow of a woman unlike any other I've tasted before."
            "Felicia was forward and wild, but Veronica...."
            scene w3_5103 with dissolve
            ver "Grab my breast."
            "Veronica had no pretense in a moment like this."
            scene w3_5104 with dissolve
            mc "Alright..."
            "She had an innate, natural energy that loomed over me like a fuckable oak tree."
            scene w3_5105 with dissolve
            ver "How was tha--"
            scene w3_5106 with dissolve
            ver "Ah, hnn-♥"
            mc "Perfect."
            scene w3_5107 with dissolve
            "{i}Women were scary creatures{/i}."
            scene w3_5108 with dissolve
            mc "Lie back."
            scene w3_5107 with dissolve
            "{i}...or was I just an idiot?{/i}"
            "Whatever the case, it didn't matter. I wouldn't be outdone here."
            scene w3_5109 with dissolve
            ver "Okay, but I'll give you ten minutes."
            scene w3_5108 with dissolve
            mc "What happens after ten minutes?"
            scene w3_5109 with dissolve
            ver "You'll see."
            scene black with fade
            "Let's not waste them then."

    scene w3_5110 with fade
    mct "(...{i}why do all the women in my life have such incredible tits?{/i})"
    scene w3_5111 with dissolve
    ver "...you got me how you want me. What comes next, {i}big strong man?{/i}"
    scene w3_5112 with dissolve

    menu:
        "Wiping that smile off your face.":
            scene w3_5114 with dissolve
            mc "Try and hold that smile as long as you can, because I'm going to enjoy demolishing it."
            scene w3_5115 with dissolve
            "All she did was double down on that cheeky look."
            scene w3_5114 with dissolve
            mc "Alright then..."
        "You continue the worship." if w3VeronicaWorship == True:
            scene w3_5113 with dissolve
            mc "Just enjoy. That's all."
            scene w3_5111 with dissolve
            ver "I'm wait--"
        "What comes next? She enjoys herself." if w3VeronicaWorship == False:
            scene w3_5113 with dissolve
            mc "Just enjoy. That's all."
            scene w3_5111 with dissolve
            ver "Well, I'm wait--"

    scene w3_5116 with dissolve
    "*Chwup~*"
    ver "A-hah... again with the..."
    scene w3_5117 with dissolve
    "*{b}Chup~*{/b}"

    if w3VeronicaWorship == True:
        scene w3_5118 with dissolve
        mc "Your body fascinates me..."
        scene w3_5119 with dissolve
        "*Chwup, chup~*"
        scene w3_5120 with dissolve
        mc "It's somehow firm and soft in all the right ways."
        scene w3_5121 with dissolve
        mc "I wonder what this part of you tastes like...?"
        scene vds_ablick_a with dissolve
        show vds_ablick with dissolve
        ver "O-oh, ah... what are you, a dog?"
        "To some, the belly was an erogenous zone. To Veronica...?"
        ver "A-ahh... you going to give every part of me a bath?"
        "Unlikely, but I think she can appreciate the sight of a man slavishly loving her body."
        "--and what a body part to love."
    else:

        scene w3_5118 with dissolve
        mc "You see right here...?"
        scene w3_5119 with dissolve
        "*Chwup, chup~*"
        scene w3_5120 with dissolve
        mc "That's about where I'll reach."
        scene w3_5121 with dissolve
        "{b}*Chup~*{/b}"
        scene w3_5120 with dissolve
        mc "That's about where I'll be later tonight."
        scene w3_5119 with dissolve
        ver "Time's ticking, [mcf]."
        scene w3_5118 with dissolve
        mc "You know, it's been really hard to resist doing this..."
        ver "Wh-"
        scene vds_ablick_a with dissolve
        show vds_ablick with dissolve
        ver "O-oh, ah... what are you, a dog?"
        "{i}Possibly.{/i}"
        ver "A-ah, well... do what you like, pervert."
        "That one was {i}more{/i} accurate, but who could blame me?"

    "Musculus rectus abdominis."
    ver "Ah, hh-huh-"
    mct "(What was this...?)"
    "In the process of devouring her, Veronica would help me develop a hands-on appreciation for my anatomy studies."
    ver "Aheh, he-♥"
    "The catch and pull of my tongue inside and around the ridges of Veronica's tummy not only produced a girlish giggle from the Amazon, but proved an odd tactile delight for my own."
    ver "...t-this wasn't quite what I had in mind when I said I preferred your hands and mouth busy."
    "Maybe not..."
    ver "F-fuck--"
    "--{i}but she liked it{/i}."
    ver "Damn, that feels weird..."
    "And even through the denim, as my hands played up and down Veronica's muscular thighs, trespassing along the edge of her sex, I could feel the warm need from within."
    ver "H-heugg...♥"
    "All thanks to the way my fingers and mouth worked in tandem, digits teasing Veronica's entrance while the other pressed down on her womb from above."
    "Gradually though..."
    scene w3_5122 with dissolve
    "...the peaks that towered over me drew my gaze, {i}commanding{/i} me to bask in their enormity and marvel at the perfection of their shape, and bit by bit..."
    "........."
    scene w3_5123 with dissolve
    "......"
    "..."
    "{i}There was a call.{/i}"
    "A siren's song, to return to the primordial ooze from which all hopes and dreams originated."
    scene w3_5124 with dissolve
    ver "Ah, ha... fuck me, I'm going to regret asking this, but... penny for your thoughts?"
    scene w3_5125 with dissolve
    mc "My thoughts...?"
    scene w3_5123 with dissolve
    mct "(My myriad thoughts?)"
    hide screen qmenu with dissolve

    menu:
        "Those freckled breasts are supernatural.":
            pass
        "Those tits are not of this world.":
            pass
        "They're freakin' impossible. An anomaly.":
            pass
        "They're driving me mad.":
            pass
        "How does reality accept such contradicting boobs?":
            pass
        "Your breasts are literally divine.":
            pass
        "I want them on my face.":
            pass

    scene w3_5126 with dissolve
    show screen qmenu with dissolve
    mc "Eh, not thinking about much."
    scene w3_5127 with dissolve
    ver "Go ahead. I know what you want."
    ver "I know how good they look..."
    scene w3_5128 with dissolve
    ver "Come to Mama."
    scene w3_5129 with dissolve
    "A little forward momentum later, Veronica was back on my lap."
    "{i}Face-to-tit.{/i}"

    if w3VeronicaWorship == True:
        "{i}All roads of worship inevitably led here, of course.{/i}"

    scene w3_5130 with dissolve
    mc "You know, I kinda wonder, since you play both teams... have you ever looked at yourself in the mirror and--"
    scene w3_5131 with dissolve
    ver "Pfft, don't be stupid. That'd be weird."
    mc "Would it...? Hehe, can you blame me for thinking that when--"
    scene w3_5132 with dissolve
    "Hands behind her back, and as if making an offering, Veronica pushed out her chest."
    scene vds_tsuck1_a with dissolve
    show vds_tsuck1 with dissolve
    ver "Ha-♥ Heh..."
    "If that was her way of telling me to shut my drunken ass up, it was quite effective."
    mc "Mmmmh~"
    "Instead of forming my inane musings, my lips were far better put to use clasped around Veronica's breast."
    ver "There, there... heh...♥"
    "Rather than wagging, my tongue was better utilized swaddling the redhead's bloated tip, in a fruitless pursuit of succor that wasn't on tap."
    mc "Hhhhrrr-!"
    "My excess fervor piped out in the form of a growl."
    mc "Ha, hhhmmmm-"
    ver "There, there... you perverted little fiend..."
    "Veronica's voice dropped down to a sultry pitch, tickling my ears with not so much an accusation as it was the naked truth."
    ver "You look {b}good{/b} with my tits in your mouth. Right at home..."
    "As I focused on my task, only half of what Veronica said reached my temporal lobe."
    ver "Hell... you almost look ... {i}innocent{/i}."
    "{i}That felt doubtful{/i}."
    ver "A-ah... but... that shit about admiring me was a lie. You don't have -ah, haa...♥"
    "{i}No, it wasn't{/i}."
    ver "Y-you don't have a single ounce of respect for me."
    "{i}I did. In my own, fucked up way{/i}."
    ver "Mmmh, not that I can blame you... I haven't given you any reason to, not before or now..."
    "...but as I was, I wasn't in any position to retort."
    ver "I wouldn't if I were you. I mean, look at me, giving my chest to--"
    scene vds_tsuck2_a with dissolve
    show vds_tsuck2 with dissolve
    ver "Ah, hhha-♥♥ {b}Goddamn it!{b}"
    "If I wanted to shut her up and put a pin in her creeping self-deprecation, I had only one avenue to do it."
    ver "Why am I so fucking turned on right now?!"
    "So, doubly as before and as if clinging onto a lifeline, I gripped Veronica's breasts and got rough with it."
    "*Thwup, thchhup, chhhhhup!*"
    ver "You f-fuckin' vacuum-!"
    "There wasn't any nuance to it."
    ver "Ah, hhnngg-♥"
    "If it didn't feel good, the least it could be was overwhelming."
    "*{b}Twhup, kwwhup, hwwwup, kkkhh, uuuhhk, ehhhup!{/b}*"
    "It wasn't long until her accusations, aimed at both me and her, stopped."
    "*{size=+5}{b}Twhup, kwwhup, hwwwup, kkkhh, uuuhhk, ehhhup!!!{/b}{/size}*"
    "A little longer, the cursing stopped too."
    ver "Ha, hhaa-♥"
    "In its wake was the profane sound of sucking and the Amazon's sweet, half-stifled moans."
    ver "Hnnng, y-you...!"
    "--she wasn't complacent though. Her body remained willful, chest pushed out more and more, as if trying to drive herself deeper into pleasure."
    "*{size=+10}{b}Twhup, kwwhup, hwwwup, kkkhh, uuuhhk, ehhhup!!!{/b}{/size}*"
    "So I focused intently, as difficult as it was with my own sexual desire mounting."
    ver "Y-you, vvvauh-!"
    "Minute after minute, maybe even ten minutes... waiting for a certain feverish note that would mark the crescendo."
    ver "Ah, rrhhi, hha-♥"
    "The highest point."
    ver "{size=+15}Hhh, hhaaa, eeeeugh-♥{/size}"
    "Because after the highest point, the natural direction to go was--"
    ver "{size=+20}Euugh, hhha, mmmhg, hhhaaa, DAMN IT-♥♥♥{/size}"
    scene vds_tsuck3_a with dissolve
    show vds_tsuck3 with dissolve
    "Diminuendo."
    ver "{size=-5}What, eeh... waht...?!{/size}"
    "You had to go back down."
    ver "D-don't do that-!"
    "Softer and slower."
    "*Chwup, fwhup~*"
    ver "{size=-10}D-don't-- D-DON'T!!{/size}"
    "Kiss after kiss, there was no escape."
    "*Chwup, fwhup, hwwwup~*"
    ver "If you suddenly stop like that--"
    "Because when the tension is at its highest, when the wall is about to break, when her body is so overwrought, it only takes..."
    $ renpy.music.set_volume(.2, 2, channel = "music")
    scene vds_tsuck4_a with flash
    show vds_tsuck4 with flash
    ver "F-fuuuuuhk it!"
    "One."
    ver "Gah, hhaaa-"
    "Little."
    ver "Haa, haaa, f-full body--"
    "Push."
    ver "H-holy, s-shit!"
    "As I watched Veronica quiver, with an undoubtedly smug look on my face, I had a thought."
    ver "Hee, haaa..."
    "{i}No, I had a confirmation.{/i}"
    scene w3_5133 with dissolve
    ver "Ha, haa, hhaaa..."
    "...I was getting pretty fucking good at this."
    scene w3_5134 with dissolve
    ver "Hnnngg... you g-goddamn devil."
    "{i}If I said so myself.{/i}"
    scene w3_5135 with dissolve
    ver "...hehehe~ hehehh... you know what?"
    scene w3_5136 with dissolve
    ver "Fuck it, good work."
    scene w3_5137 with dissolve
    mc "...I do respect you, Veronica."
    scene w3_5138 with dissolve
    ver "Shut up."
    scene w3_5139 with dissolve
    mc "...that's probably not going to happen, you know that, right?"
    scene w3_5140 with dissolve
    ver "Hehe, ha..."
    $ renpy.music.set_volume(1, 2, channel = "music")
    scene w3_5141 with dissolve
    ver "I don't know if it's been ten minutes or not, but..."
    ver "...it's my turn now."
    "Suddenly, Veronica was towering over me, bringing her size and weight to bear."
    scene w3_5142 with dissolve
    mc "...we're taking turns?"
    "It felt strangely warm."
    scene w3_5143 with dissolve
    ver "Wouldn't you say one good turn deserves another?"
    "Oddly comforting, even."
    mc "We can go with that."
    scene vds_pounce_a with dissolve
    show vds_pounce with dissolve
    mc "Mmmh, mhh-"
    "I didn't mind. Veronica's imposing form felt like a blanket securing and shielding me from the dreary night."
    "*Chwup~*"
    "Her kisses to my neck, however, weren't. Those were like little jolts to my system."
    "*Chwup, chwup~*"
    "Prickly things of burgeoning anticipation, pushing all active thoughts from my skull and pacifying my will."
    "{i}It would be really nice to just lie back and let the redhead work, wouldn't it?{/i}."
    "{b}Yes, it would.{/b}"
    "An overwhelming part of me wanted to see where this leads and bask in the unbelievable thought of Veronica's {i}pleasing me.{/i}"
    scene w3_5144 with dissolve
    mc "I'll give you ten minutes."
    scene w3_5145 with dissolve
    "......"
    ver "..."
    scene w3_5146 with dissolve
    "Wordlessly, and with concentrated haste, Veronica fumbled with my clothes one button at a time."
    scene w3_5147 with fade
    "Then my pants and my underwear."
    scene w3_5148 with fade
    "Until I was but a specimen, served up on a slab, to be dissected by Veronica's cutting gaze."
    scene w3_5149 with dissolve
    mc "You know, you've seen me wearing this before..."
    scene w3_5150 with dissolve
    "Perhaps satisfied by the show of self-consciousness, she just smiled glibly in return."
    scene w3_5151 with dissolve
    mc "Time to even the field..."
    scene w3_5152 with dissolve
    mc "...huh?"
    scene w3_5153 with dissolve
    ver "{i}Down.{/i}"
    scene w3_5154 with dissolve
    ver "Patience, little boy..."
    scene w3_5155 with dissolve
    "She tossed me like a sack of potatoes."

    menu:
        "You like it.":
            mct "(Why does that turn me on?)"
            scene w3_5156 with dissolve
            mc "Yes, Ma'am..."
        "Damn it, you...":
            scene w3_5156 with dissolve
            mc "...bitch."
            scene w3_5157 with dissolve
            ver "Uh huh. Just you wait."

    scene w3_5158 with dissolve
    "First her shoes and then..."
    scene w3_5159 with dissolve
    "Inch by inch, Veronica peeled the denim from her freckled skin, making a show of it..."
    scene w3_5160 with dissolve
    "Gradually revealing her sizeable ass, muscular thighs, and {b}shapely{/b} legs."
    scene w3_5161 with dissolve
    "Everything but her panties, and from my lowly position, it was my turn to admire the cut of the Amazon's figure."
    ver "It's better if I leave this bit on, right?"
    scene w3_5162 with dissolve
    mc "It does have an appeal..."
    scene w3_5163 with dissolve
    "{i}Like a tiger cornering her prey...{/i}"
    "She had me cornered, waiting with bated breath."
    scene w3_5164 with dissolve
    ver "*Chwup* Don't..."
    scene w3_5165 with dissolve
    ver "...don't expect the same kind of loving treatment from me. I'm a selfish bitch."
    ver "To the point at hand..."
    scene w3_5166 with dissolve
    ver "Mmmmhh..."
    "The Amazon regarded my gonads like a freshly baked pie."
    scene w3_5168 with dissolve
    ver "You smell... {b}thick.{/b}"
    mc "Is that why you gave me a workout before your photoshoot last week?"
    scene w3_5167 with dissolve
    ver "Mmmmhhh...♥"
    mc "You do that for all the men you fuck?"
    scene w3_5168 with dissolve
    ver "Aaaaaah~"
    scene w3_5169 with dissolve
    "She had no words for my dumb provocation, only a look."
    "{i}She was serious.{/i}"
    mct "(Should I fear for my--)"
    scene w3_5170 with dissolve
    ver "*Chwup~*"
    scene w3_5171 with dissolve
    "{i}She advanced.{/i}"
    scene w3_5172 with dissolve
    "Slowly, she took me in, bit by bit."
    "Making me truly feel like she was about to consume me."
    scene w3_5173 with dissolve
    ver "You're cute enough."
    scene w3_5174 with dissolve
    ver "Mmmmh..."
    "Her trap set, Veronica lulled me into its terrible embrace with a kiss."
    scene w3_5175 with dissolve
    mc "A-ahh-"
    "A distraction, as Veronica {i}coiled{/i} around my cock, snuffing out any notion of escape."
    scene w3_5176 with dissolve
    "Her eyes showed the vast difference in our experience."
    "If I was in her position, I'd be overly excited, brimming over with venom and childish malice."
    "For Veronica, however, it was due course. Her control needed no vulgarity to mask its shortcomings."
    scene w3_5177 with dissolve
    mc "Hnngg, aha, s-shit..."
    "Veronica held me strangled, between thigh and calf."
    scene w3_5176 with dissolve
    "So very, {i}very{/i} tight..."
    "{i}Crushing.{/i}"
    scene w3_5178 with dissolve
    mc "Ahk, what are you...?"
    ver "You were so interested in mine..."
    scene w3_5179 with dissolve
    mc "MMmhh-!"
    "As her lips sealed around my nipples, I didn't expect to feel a thing, but {i}Veronica made it feel good{/i}."
    mc "Ah, ahh- ha-♥"
    "Her control over my cock {i}made it feel like it was the very best place to touch me{/i}, extracting girlish moans from my lips."
    "{i}Tricking my mind that she could make anything a reality...{/i}"
    scene w3_5180 with dissolve
    "Her eyes again said it all."
    "She didn't try to make me beg, like I probably would."
    "A snake didn't ask its prey for encouragement, it just made due on the promise of death."
    scene vds_thigh1_a with dissolve
    show vds_thigh1 with dissolve
    mc "Y-yeah..."
    "{i}Finally.{/i}"
    "Veronica worked me methodically, her body holding me down with a loving, comfortable authority."
    ver "Mmmh, hmmm... that's the look... heh..."
    ver "You're making me {i}swoon{/i}, [mcf]."
    mc "Mmmh, y-eaah..?"
    ver "You lady killer, you."
    "Her fangs pierced my skin, delivered by a husky voice, injecting venom into my ears."
    mc "...I could learn a thing or two from you."
    "The act itself was clumsy and how couldn't it be?"
    "In this position, twisted up like this, wedged between the bend of Veronica's leg..."
    "It didn't matter though."
    mc "Ha, hnnnng♥"
    "It wasn't complicated. The human body was a simple and pleasure-yielding thing."
    mc "D-damn...! This feels...!"
    "I felt like my dick was about to pop, overly engorged, skin stretched painfully with desire..."
    ver "Good...?"
    "All before you added Veronica's {i}clamp{/i} to the mix, constricting and pulling, mashing and rubbing."
    mc "Fuck, you sure got it!"
    "{i}Clumsy worked.{/i} I was growing dim-witted under a feverish spell."
    ver "Hmmmmm....what are you thinking about?"
    mc "How much I want to fuck the shit out of you..."
    ver "{i}Good{/i}."
    scene vds_thigh2_a with dissolve
    show vds_thigh2 with dissolve
    mc "A-aah, hhn-"
    "It would be a slow death, I was so far from cumming, but desire had made me sick."
    ver "Good, good, good..."
    "...but it didn't make me want to curse. Veronica peered into me reassuringly and formed a contradiction."
    "{i}She made it comfortable.{/i}"
    ver "Because... well, I kinda need it, [mcf]."
    "{i}She made a connection.{/i}"
    mc "Y-yeah, I thought you might..."
    ver "I needed a night like tonight..."
    "{i}A warm kind of torture.{/i}"
    ver "Some drinking, some dancing, some..."
    "She paused, the answer evident, but her voice full of captivation."
    ver "I mean, all those cute girlies at the bar tonight and this is how it ended up?"
    ver "Pfft, ha, hahaa-!"
    mc "You liked my dancing!"
    ver "...mmmh, I guess I did."
    mc "A, hhhaaaa-!"
    "Her hold on my cock was resolute."
    "{i}A bear hug.{/i}"
    ver "You want to \"fuck the shit out of me,\" [mcf]. It's crude, but..."
    mc "Euughh-"
    ver "{b}Okay...{/b} feel free to fuck all the sense out of you and into me. I'll do the same."
    mc "D-deal...!"
    ver "...and we'll see which one of us can walk afterwards. Doesn't that sound fun?"
    mc "A, eeu-yeuhhuup!"
    mc "Good, good, good, {b}good{/b}..."
    "The goods mounted, and I was hard-pressed to disagree."
    scene vds_thigh3_a with dissolve
    show vds_thigh3 with dissolve
    ver "Just..."
    "The seductive glean in her eye diminished as she searched my expression, as if making sure I was suitably under control."
    ver "Let's enjoy tonight. Like two people who want to be together."
    mc "Ah, haaa-♥"
    "Her devilish facade crumbled to a vague look of genuineness and vulnerability, but the torture down below continued."
    ver "{i}Please{/i} don't make me regret it, [mcf]."
    mc "Why would--"
    "Despite her pleading, Veronica hadn't stopped mercilessly working my cock."
    "The mix of give and take, of going out on a limb from loneliness, of being caught up in sexually-charged abandon..."
    "A yearning look in search of a connection,{i}of taking it where you can get it{/i}, and putting your trust in another person."
    mc "Mmh, hh-"
    "And again, that word. {b}Conquest.{/b} Boiling over from my mind and scalding my insides with a ruinous desire to blank the entire world white with my cum."
    mc "I can't say how you'll feel about it later, but... a-ah..."

    menu:
        "You promise she won't be walking afterward(w3ChallengeAccepted = True)":
            $ w3ChallengeAccepted = True
            mc "I can promise you that you won't be able to stand up after this."
            scene w3_5181 with dissolve
            ver "Ha! Fat fucking chance! Have you seen my legs?"
            scene w3_5182 with dissolve
            mc "I've got m-my work cut out for me!"
            scene w3_5181 with dissolve
            ver "Oh, yeah...? Hehe... let's take a look at yours."
            scene w3_5183 with dissolve
            "Veronica stopped, leaving my loins with a needy, lonely ache."
            mc "Why are you stopping...? I'm--"
            ver "Because I'm not going to need these."
            scene black with fade
            mc "Guess--"
            mc "Wha, o-oh...?!"
            $ renpy.music.set_volume(.2, 2, channel = "music")
            scene w3_5188 with fade
            "With an alarming amount of strength, and some horny-addled compliance from my end, Veronica had upended me and had my legs spread like a bitch."
            ver "Not bad, you've got some tone to them..."
            mc "Thank you...?"
        "You {i}do{/i} want to be together."(chg=["veronica_up"]):


            $ Veronica_Affection += 1
            mc "S-speaking for myself? Tonight..."
            "She peered into my eyes, exposed and waiting."
            mc "Hnng, I don't want to be anywhere else in the world... the rest of the {i}two{/i} people part is on you!"
            scene w3_5184 with dissolve
            ver "..."
            "Veronica stopped, leaving my loins with a needy, lonely ache -- but I didn't quite mind it so much."
            "All that dominant bluster was replaced with an adorable smile."
            scene w3_5185 with dissolve
            mc "Mmmh, you're cute you know that?"
            scene w3_5186 with dissolve
            ver "So are you. Do you mind if I try something?"
            scene w3_5187 with dissolve
            mc "...I'd {i}love{/i} for you to try something."
            ver "Mmmh, good..."
            scene black with fade
            mc "What do you have--"
            mc "Wha, o-oh...?!"
            $ renpy.music.set_volume(.2, 2, channel = "music")
            scene w3_5188 with fade
            "With an alarming amount of strength, and some horny-addled compliance from my end, Veronica had upended me and had my legs spread like a bitch."
            mc "A-ah... you want to do it like this?"

    scene w3_5189 with dissolve
    "...suddenly, there was a funny-like {i}exposed{/i} feeling that confused my desire to fuck the whole wide earth."
    mc "I mean, you're about to--"
    scene w3_5190 with dissolve
    ver "Ah, h-holy shit-!"
    "Yep. {i}All at once.{/i}"
    mc "Hnggg-"
    scene w3_5191 with dissolve
    "I was instantly plunged into Veronica's embrace, trading the awkward machinations of Veronica's leg with the mind-blanking sublimity of her sex."
    scene w3_5193 with dissolve
    mc "H-holy shit is, y-yeeep..."
    scene w3_5191 with dissolve
    "Thankfully, she didn't just jump into it..."
    scene w3_5192 with dissolve
    ver "Just lie there a sec. I still got time on the clock."
    scene w3_5191 with dissolve
    "...it was like she was giving {i}me{/i} time to ease into things."
    "{i}She was so fucking tight...{/i}"
    "It was nothing like the brutish way she was milking me before, but it didn't lack in the same unyielding control."
    scene w3_5194 with dissolve
    mc "Euugh-"
    "I couldn't even {b}dream{/b} of moving."
    scene w3_5192 with dissolve
    ver "Your face says it all..."
    scene w3_5191 with dissolve
    "...was she tightening herself up on purpose?"
    scene w3_5193 with dissolve
    mc "Well, this {i}is{/i} a new one for me..."
    scene w3_5192 with dissolve

    if w3ChallengeAccepted == True:
        ver "Me too, actually. But I've always wanted to try it. You don't mind starting like this, do you?"
        scene w3_5194 with dissolve
        mc "F-fuck, a-ah... I mean... doesn't matter how it's done, I'm going to pack you full of cum tonight."
    else:
        ver "Me too, actually. You don't mind, do you?"
        scene w3_5194 with dissolve
        mc "W-well, a-ah... you feel... hehe... {i}could be fun{/i}."
        mct "(Who could say no to a pussy like this?)"

    scene w3_5192 with dissolve
    ver "Good."
    scene w3_5195 with dissolve
    ver "Let me know if it starts to hurt."
    scene w3_5196 with dissolve
    mc "Very funny."
    scene w3_5197 with dissolve
    ver "I'm not kidding. I'm~ gonna~ {i}fuck{/i}~ {b}you{/b} like an earthquake."
    scene w3_5198 with dissolve
    "She spoke down to me, with a scary look of a woman delivering the judgment of God, but the only thing that formed on my lips was a meager.."
    scene w3_5199 with dissolve

    if w3ChallengeAccepted == True:
        mc "I'd like to see you try."
    else:
        mc "Good luck to us all..."

    scene w3_5200 with dissolve
    ver "Hehe~"
    $ renpy.music.set_volume(1, 0, channel = "music")
    play music "music/thunder.ogg"
    scene vds_amazon1_a with dissolve
    show vds_amazon1 with dissolve
    mc "Hnngg-♥"
    "The moment she began to move, I felt many things."
    mc "Fu- fu- fuck!"
    "I felt my soul being scraped out of my body, Veronica's insides clung possessively to my shaft, pulling sweetly at my nerves as she climbed."
    ver "Oh, God-♥"
    "The muscles in my legs tightened, burning from being stretched in a way that they had never before had during sex."
    ver "Good, good, good, good, {b}GOOD!{/b}"
    "Most of all, I felt the impact of Veronica's descent, {i}as she let go{/i}, her muscular ass careening to the earth and all my soft, sensitive, precious bits below."
    scene vds_amazon2_a with dissolve
    show vds_amazon2 with dissolve
    "{i}The result was an earthquake{/i}."
    ver "Mmmh-♥ Yeah, you look--"
    "Every {b}punch{/b} made me feel {i}uneven{/i}."
    mc "Ah, s-shut up!"
    "Disconnected."
    mc "I can't hear myself think!"
    "My being interrupted, chipped away at by Veronica's plunging hips."
    mc "Hnng, hahaaaa-♥♥"
    scene vds_amazon3_a with dissolve
    show vds_amazon3 with dissolve
    "I could feel the force of her weight in my bones, as it traveled from my pelvis to my ribs, and dissipated into the softly crying couch below."
    "A primal, panicky part of me feared she was going to break me."
    "That Veronica was going to fold me in half, quarter me, and trample on my unrecognizable body."
    "It was a wholly new sensation, but not an {b}unwelcome{/b} one."
    "The feeling of a woman bearing down on me, lust in her eyes, abs tightening and tits flailing."
    mc "Ahaha...♥♥♥"
    "{b}No, it felt pretty fucking good.{/b}"
    "It felt AMAZING to be discombobulated and have your brain scrambled on the down fuck of every arc."
    ver "J-just jumping into the deep end is really the best! Don't you agree, cutie?"
    mc "Hhhng-♥♥♥♥"
    "Yeah... letting her do all the work was its own brand of pleasure."
    mc "Hee, hheee-"
    scene vds_amazon2_a with dissolve
    show vds_amazon2 with dissolve
    "Amazing how a change in direction made novel the act of drunken rutting."
    ver "No need to say it. I can read the answer on your adorable~ face..."
    "However, as pleasurable as this was, it was only a momentary distraction."
    "A temporary setback to my plans to bathe the whole wide world in my color..."
    mc "Ha, haaat-♥♥♥♥"
    "{i}...even if the garbled moans she pried from my vocal cords told a different story.{/i}"
    ver "Hhhng--"
    scene vds_amazon3_a with dissolve
    show vds_amazon3 with dissolve
    "Separate from my head, my body not content with just being gobbled up, mounted its own paltry resistance."
    "My hands gripped the back of the couch with knuckle-white tension."
    ver "Ha, ha, haa~"
    "Conquer."
    "That word clacked around like a bullet in my skull."
    "{i}Conquer. Conquer.{/i}"
    "Snuffing out all my neurons."
    "{b}Conquer. Conquer. Conquer.{/b}"
    "Turning my head into mince meat."
    scene vds_amazon2_a with dissolve
    show vds_amazon2 with dissolve
    "{i}Rearrange Veronica's insides the same way she's doing to you.{/i}"
    "Turn the tables..."
    "My lower body pitifully pushed up, trying to fuck a little bit of myself into Veronica in return."
    ver "Hhhng, mmmhh...♥ Ah, you...♥"
    "A futile effort, like trying to escape the churning sea, but there is meaning in making an effort."
    scene w3_5201 with dissolve
    ver "...you want to switch?"
    scene w3_5202 with dissolve
    mc "Gah, hee, y-you can tell?"
    scene w3_5201 with dissolve
    ver "Yeah, {i}I can tell.{/I}"
    scene w3_5203 with dissolve
    ver "...shall we?"
    scene w3_5204 with dissolve
    "Veronica's vibe got oh so soft, all so sudden. An aura of openness and reassurance that played ticklish to my inebriated mind."
    scene w3_5205 with dissolve
    mc "You're having fun, aren't you?"
    scene w3_5203 with dissolve
    ver "You know what else would be fun?"
    scene w3_5206 with dissolve
    ver "...showing you just how {i}flexible{/i} I am."
    scene w3_5207 with dissolve
    ver "Get up, cutie."
    scene black with fade
    ver "Well? What do you think?"
    scene w3_5208 with fade
    mct "(...what did I think?)"
    "Left leg pulled back, vulgarly exposing herself...?"
    "{i}Her twat was practically winking at me.{/i}"
    scene w3_5209 with dissolve
    mc "{i}I think...{/i}"
    scene w3_5210 with dissolve
    "{i}I'd show her what I think{/i}."
    "Not a word. Just a wry smile and a welcoming hole."
    scene w3_5211 with hpunch
    ver "A-aahh- e-eager-"
    "There was no need to be ginger about it. I had all the intentions of matching the same fervent pace as she set, but as soon as I entered her, she closed down around me like a Venus flytrap."
    scene w3_5212 with dissolve
    "{i}Holding me in place, not allowing.{/i}"
    mc "Hhng, you're... showing off."
    scene w3_5214 with dissolve
    ver "What do you mean? I'm just laying here."
    scene w3_5213 with dissolve
    mc "You're telling me you're not flexing your pelvic floor muscles?"
    scene w3_5214 with dissolve
    ver "{b}{i}Weeeeeeell{/b}{/i}, it iiiiis the one part of me boys get to appreciate that the girlies don't."
    scene w3_5213 with dissolve

    if w2ExEndingVeronica == True:
        mc "All the better. Tighten all you want, Ronnie. Because..."
    else:
        mc "All the better. Tighten all you want, because..."

    scene w3_5215 with dissolve
    ver "Ha, hha, haa-♥"

    scene vds_flex1_a with dissolve
    show vds_flex1 with dissolve
    if w3ChallengeAccepted == True:
        "I wasn't going to let the chokehold she had on my dick prevent me from fucking her stupid."
    else:
        "I wasn't going to let the chokehold she had on my dick slow me down."

    "The tighter she squeezed just meant the harder I'd have to push to split her open."
    ver "Ah, d-damn it-!!"
    "Dizzying as it was pushing through a chokehold that threatened to pop my dick off, I embraced the challenge."
    mc "It's best just diving into the deep end, right? Those were your words?!"
    ver "Ah, haaaaa~ fuck yeah, they were!"
    "A challenge made all the more worth it by the enraptured look spreading on Veronica's face."
    ver "Mmmmh, {i}fuck me deep!{/i}"
    "Her eyes added, {i}\"I'd like to see you try\"{/i}."
    ver "C'mon!"
    "...but not in a mocking way. {i}It was an eager one.{/i}"
    ver "C'mon! C'mon!"
    "Over and over I rolled my hips forward into the vice only to rip myself violently free of its teeth."
    "{i}Over and over.{/i}"
    "Every thrust was a battle of attrition."
    "{i}Over and over.{/i}"
    "All for the promise of a mere brief instance of self-annihilation."
    mc "Hhhnng-♥"
    ver "Put your back into it!"
    "The more I thrusted, the more the redhead egged me on."
    scene vds_flex2_a with dissolve
    show vds_flex2 with dissolve
    ver "Fuck me like {i}I'm{/i} the last chance you'll ever get to use your ugly cock!"
    mc "Heeeug, f-fhuuck-!"
    "Her lust-laced provocation hit the target."
    mc "--what do you think I'm doing?!"
    "It excited something in me."
    ver "Mmmh, h-ha, y-you tell me~"
    "Fueled me."
    ver "With me, you can do it harder than any other girlie you've ploughed before."
    "{i}Combusted me{/i}."
    ver "Ha, hhh- that's it!"
    mc "Euuughh!"
    "Even on her back and gaping around my cock, Veronica felt like she was the one in the driver's seat."
    mc "F-fuck, s-shit...!"
    "{i}An expressive verdict, delivered by my lips for the situation.{/i}"
    mc "Mmmh-"
    "One suitable for the strain on my back and the fire in my calves."
    ver "--that's it! That's it, cutie-! Haat!"
    ver "Give it your all! Mmmh, give {i}me{/i} your all!"
    mc "D-dddaahm! Ahhhgg-!"
    scene vds_flex1_a with dissolve
    show vds_flex1 with dissolve
    "Words that felt like I was gladly laid at this woman's feet."
    ver "A-all for me! A-all mine! All V-Veronica's-"
    "However, the diminishing return on her own eloquence told me I wasn't the only one being turned inside out."
    ver "Pretend like, haa-"
    "I wasn't the only one whose mind was reduced down to a sauce sloshing around an empty skull."
    ver "J-just for tonight-♥♥♥ Ha-haaaa-!"
    "...but in my reduction, my drunk-ass suddenly found a thread."
    ver "B-be mine!"
    "A thread of {i}something{/i}, to follow and unravel to an understanding."
    ver "J-just b-be mine-♥♥ "
    "{i}Let's enjoy tonight. Like two people who want to be together.{/i}"
    ver "B-belong to me-!!"
    mc "A-ahh, hhaaa-♥"
    "Those were her words."
    scene vds_flex2_a with dissolve
    show vds_flex2 with dissolve
    mct "(She couldn't be more pointed could she?)"
    "In a lusty haze, I felt like my mind had finally appreciated the bitter-sweet meaning."
    mc "H-aha... hahahaha-!"
    ver "W-what?! Why are you--"
    "The question of who would be able to walk after this?"
    mc "Bahah, haaa-!"
    "A fun idea, but that wasn't what she wanted."
    scene w3_5216 with dissolve
    mc "God, you're so fucking cute. Hahaha- haaa-!"
    scene w3_5217 with dissolve
    ver "S-seriously? What the shit?"
    scene w3_5216 with dissolve
    "She was asking for a different tempo."
    "When two people dance, it isn't a one-sided affair."
    "This, like the rest of tonight, should just be two idiots dancing."
    mc "Aaa-aah... we're dumb, aren't we?"
    scene w3_5217 with dissolve
    ver "A-ahhh... w-where's this coming from?"
    scene w3_5218 with dissolve
    mc "Come here, idiot!"
    ver "W-whaa-♥"
    play music "music/drop-the-tapes.ogg"
    scene w3_5219 with dissolve
    mc "Dance {i}with{/i} me."
    scene w3_5220 with dissolve
    "Why were we pitting ourselves against each other?"
    scene w3_5221 with dissolve
    ver "A-aahh..."
    scene vds_miss1_a with dissolve
    show vds_miss1 with dissolve
    "A night like tonight?"
    ver "Ha, hahaaa-♥"
    "{i}Tandem{/i}."
    mc "Mmh, hhngg-"
    "We should move in tandem."
    ver "Ahhhg-"
    "Our grunting and moaning should be music."
    ver "Ahh, mmmhh- keep-"
    "Two people, writhing in the cold night..."
    ver "That's the spot, cutie. You- ahh--"
    "A coda to tonight's {i}movement{/i}."
    ver "Mmmh, you idiot-♥"
    "Gyrating, bumping, and {i}boogeying{/i}."
    scene w3_5222 with dissolve
    ver "Mmmhhhh-♥"
    "Like this, we were melting into each other."
    scene w3_5223 with dissolve
    ver "Mmmh, mmhmhhh--"
    "Melting into the couch."
    scene w3_5222 with dissolve
    ver "Mh, hhh-♥"
    "Melting into the apartment."
    scene vds_miss1_a with dissolve
    show vds_miss1 with dissolve
    ver "F-fucking idiot...♥♥"
    "Melting into the earth itself."

    menu:
        "You have a name.":
            mc "Name's [mcf]."
            ver "Ah, aaahh-♥"
            mc "Say it."
            ver "Mhh, nah, fuck you-"
            scene w3_5222 with dissolve
            ver "Mhh, hhhu-♥"
            "{i}Say it.{/i}"
            scene w3_5223 with dissolve
            ver "Mhh, hhhhmmm-"
            "{i}Say it.{/i}"
            scene vds_miss1_a with dissolve
            show vds_miss1 with dissolve
            ver "[mcf]..."
            "{i}That's right...{/i}"
        "Forget it. Sweet, sweet nothings.":

            mc "{i}I'm yours.{/i}"
            ver "Hee-huhh-♥ I didn't mean it like that-"
            "Of course she didn't, but one night of escape..."
            mc "{b}I'm yours.{/b}"
            ver "A-ahhh... s-hut up."
            scene w3_5222 with dissolve
            ver "Mhh, hhhu-♥"
            "{i}Don't get so self-conscious you goddamn idiot.{/i}"
            scene w3_5223 with dissolve
            ver "Mhh, hhhhmmm-"
            scene vds_miss1_a with dissolve
            show vds_miss1 with dissolve
            "{i}I'm yours.{/i}"
            ver "Hhhng, ah, haa-- o-okay..."

    mc "Ahe, hehee-"
    "Like this, we pushed into each other, slowly."
    "Nothing like before."
    ver "Mmmh..."
    "{i}Less spicy, more savory...{/i}"
    scene vds_miss2_a with dissolve
    show vds_miss2 with dissolve
    ver "...you smell good."
    "{i}In sync.{/i}"
    mc "{i}Weirdo{/i}."
    ver "Mmmmh, so what? Ah, aah-"
    "{i}In step.{/i}"
    ver "You really do..."
    "Two people moving as one."
    mc "Mhh, euuugh..."
    "Was I being swept away by the drink?"
    "{i}Probably{/i}."
    "Still, the way Veronica held and squeezed me felt like a conquest."
    ver "Ha, hhaaa-♥"
    "It was warm and comfortable."
    mc "Ha, haaaa-"
    "{i}A feeling that wouldn't survive the break of dawn.{/i}"
    mc "Hnng, haaaahhhk-!"
    "A feeling, I feared, that might not last the moment I busted."
    mc "Ha, hhaaa-♥♥"
    "...but one moment was as good as any."
    ver "Don't pull out..."
    "As sweet and seductive as anything that came from Veronica's mouth..."
    ver "You can shoot it inside..."
    mc "Ah, hhaa-♥"
    "{i}Yeah{/i}."
    ver "{b}Don't pull out.{/b}"
    "I was close and that command dressed up like a tempting request sounded good to me."
    mc "Ah, hhaa- a-alright..."
    scene vds_miss3_a with dissolve
    show vds_miss3 with dissolve
    "I wasn't going to fight it."
    ver "Ah, aaah-♥"
    "I wasn't going to try to hold out longer."
    ver "Mmmh, haa, come on... c'mon...."
    "{i}Like a dance, going with the flow...{/i}"
    "....................."
    ".................."
    "..............."
    "............"
    "........."
    "......"
    $ renpy.music.set_volume(.1, 0, channel = "music")
    play sound "sound effects/spurt.wav"
    scene w3_5224 with flash
    "Hnngg-!"
    scene vds_miss4_a with dissolve
    show vds_miss4 with dissolve
    "She pulled me in, taking everything I poured into her."
    ver "Ahh, hhaaa..."
    "It felt nice."
    ver "Hmmmhhh-♥"
    "It felt secure."
    ver "Ha, hhaaa... {i}good boy{/i}."
    "On the back of a tiresome morning, a long day, and the night of drinking..."
    ver "Good boy..."
    scene w3_5225 with dissolve
    "It pulled me perilously into sleep."
    scene black with fade
    "........."
    "......"
    "...had she gotten what she wanted out of this?"
    "........."
    "......"
    ver "Ah, hhaa...? [mcf]...?"
    scene w3_5226 with fade
    "No sleep."
    ver "Ahh, hhaaa-♥"
    $ renpy.music.set_volume(1, 0, channel = "music")
    $ renpy.music.set_volume(0.4, 0, channel = "ambient")
    play ambient "sound effects/boobjob.wav"
    scene vds_rush1_a with dissolve
    show vds_rush1 with dissolve
    "Not yet."
    ver "Ah, Hhh, hhaaa-♥"
    "No one was home upstairs."
    ver "What are you... aren't you...?"
    "At least, it didn't feel like it."
    ver "Ha, nnggg- o-okay...♥"
    "Part of me felt like I {i}was{/i} sleeping, but my body pushed on."
    ver "If that's what you want..."
    "That someone {i}other{/i} than me was driving my body forward into Veronica's sloppy hold."
    ver "Ah, hhhmmm-♥ You can k-keep going..."
    "Perhaps it was the redhead's girlish coos animating my body..."
    ver "Hehea, heee... {i}I don't mind.{/i}"
    "...or foolish pride wanting to finish what I started."
    ver "Ah, hhnggg, k-keeep fuucking me...!"
    "Either way, I packed my cum deeper and deeper into Veronica's sex."
    "{b}*Schlick, fwhhhuck, wwhhucck...!*{/b}"
    ver "Hnnggg... fhhuuuckk, hnngg...♥"
    "Sloshing and mixing and stirring..."
    ver "Haa...!"
    "Folding her over..."
    ver "{b}Ha, hhaaaa...!{/b}"
    "Fucking her slacked body into the couch..."
    ver "C-crazy... i-dhoiiittt... aahh...♥♥♥"
    "Stretching the night as far as I could take it."
    ver "Haat, hhaaa...♥ Damn it, you're making it h-hard to think... I'm, haaah..."
    "Pounding."
    ver "Hnnng...♥"
    "Pounding. Pounding."
    ver "Wha, hhaan, hhhaaa-♥♥"
    "Pounding. Pounding. Pounding, and..."
    stop ambient
    scene w3_5227 with dissolve
    ver "Aah, aaaahhh-♥♥♥♥♥♥"
    stop music fadeout 12.0
    scene vds_rush2_a with dissolve
    show vds_rush2 with dissolve
    "...how much time had passed before I felt Veronica tense up in my arms?"
    ver "Ghh, eeeuhhh-♥♥♥"
    "Was it as brief or long as it felt before she clamped down, quivering and pushing out the roiling cum sticking to her insides?"
    ver "Ha, hhaaaa, haha..."
    scene w3_5228 with dissolve
    mc "Heuugh..."
    "In that time, the world became a tangled mess of limbs and torsos."
    ver "Ah, haa..."
    "Turns out, Veronica made for an..."
    scene w3_5229 with dissolve
    ver "Mmmh, good boy."
    mc "Hehe, haa..."
    scene black with fade
    "...an extremely comfortable pillow."
    $ renpy.end_replay()
    "........."
    "......"
    "..."
    stop music
    scene w3_5230 with w12
    mc "Mmmh..."
    $ unread_veronica = True
    $ history_veronica = "I took Veronica out, hoping it would be a nice reprieve from her troubles. We ended up fucking."
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "I woke up alone, tangled up with {i}myself{/i}."
    hide bioupdate with dissolve
    scene w3_5231 with dissolve
    mct "(Had she left...?)"
    play sound "sound effects/water-splash.wav"
    scene w3_5232 with dissolve
    mc "Fwwwwwwwhhh-!"
    scene w3_5231 with dissolve
    "No..."
    play ambient "sound effects/water-splash3.wav"
    scene w3_5233 with dissolve
    mct "(...splashing,)"
    mc "Heh..."
    "Bleary-eyed as I was, it kinda felt like a dream seeing Veronica of all people frolicking nude in my friend's pool, while I laid spent on the couch."
    stop ambient
    $ renpy.music.set_volume(1, 0, channel = "ambient")
    scene w3_5234 with dissolve
    mct "(...should I chalk this up to the alcohol, perks of the job, or greed?)"

    if hanaGF == True:
        "Along with how quickly I promised fidelity to Hana, maybe I'm more like my predecessor Darius than I care to admit."

    scene w3_5235 with dissolve
    "...{i}whatever.{/i}"
    "I'm just glad she stuck around."
    play music "music/ocean-view.ogg"
    scene w3_5236 with dissolve
    mc "Hey..."
    ver "....HEEEEEEY."
    scene w3_5237 with fade
    mc "Felt like a swim?"
    scene w3_5239 with dissolve
    ver "Yeeeeah... uh... nice dipping into a pool that doesn't have a bunch of screaming kids pissing in it, y'know?"
    scene w3_5238 with dissolve
    ver "Haven't had much occasion for that, recently..."
    scene w3_5237 with dissolve
    mc "It's cool. Ian's probably passed out in the tits of his hairdresser right about now."
    scene w3_5238 with dissolve
    ver "Hairdresser...?"
    scene w3_5237 with dissolve
    mc "Not really important. Point is, we don't have to rush to get out of here."
    scene w3_5238 with dissolve
    ver "Heh. It took me forever to find out how to open the freakin' windows."
    ver "You rich pricks..."
    scene w3_5240 with dissolve
    mc "What, I'm not--"
    "Okay, my life was pretty comfortable up to this point..."
    mc "I didn't grow up in a house with a transformable façade!"
    scene w3_5241 with dissolve
    ver "Heh... hehehe."
    mc "What about you?"
    scene w3_5242 with dissolve
    ver "Me...?"
    scene w3_5243 with dissolve
    mc "Yeah, what kind of environment did you grow up in?"
    scene w3_5244 with dissolve
    ver "Comfortably middle class. My mom married down with a career military man slash amateur athlete."
    scene w3_5243 with dissolve
    mc "Is that where you inherited your stern looks from?"
    scene w3_5245 with dissolve
    ver "I come by that on my own honestly -- {i}and{/i} I'll thank you for not making that comparison again."
    scene w3_5243 with dissolve
    mc "Pfft, it was that easy to get a thank you out of you?"
    scene w3_5246 with dissolve
    ver "Mmmh, [mcf]... {i}thank you for fucking me{/i}. Your cock is a gift to womankind."
    scene w3_5247 with dissolve
    "......"
    "..."
    scene w3_5248 with dissolve
    mc "Your words, not mine."
    scene w3_5249 with dissolve
    play sound "sound effects/slap1.wav"
    scene w3_5250 with hpunch
    ver "You fucking idiot!"
    scene w3_5251 with dissolve
    ver "Get in the pool..."
    mc "...eh?"
    play sound "sound effects/water-splash2.wav"
    scene w3_5252 with dissolve
    "*Kttthuk*"
    "And like that..."
    scene w3_5253 with dissolve
    ver "The water's fine!"
    "...the world got a bit more wet."
    scene w3_5254 with dissolve
    mc "...uuugh, you say that {i}BEFORE{/i} you drag someone in the pool."
    scene w3_5255 with dissolve
    ver "Ah, damn..."
    mc "...what?"
    ver "It just occurred to me that..."
    scene w3_5256 with dissolve
    mc "Ghhehhhkkt...?!"
    scene w3_5257 with vpunch
    play sound "sound effects/water-splash2.wav"
    "........."
    scene w3_5258 with dissolve
    "......"
    "..."
    scene w3_5259 with vpunch
    play sound "sound effects/water-splash2.wav"
    ver "Mmmhh...!"
    "Somehow, under the water and from Veronica's hand, it turned out like this."
    mc "Oooght..."
    scene w3_5260 with dissolve
    mc "*Cough* Hhhaahk...!"
    mc "Blah, eeuhk..."
    "{i}Water in my nose...{/i}."
    scene w3_5261 with dissolve
    ver "You smell like chlorine now..."
    ver "Mmmh, too bad."
    mc "...you haven't sobered up yet, have you?"
    ver "Leave tomorrow for tomorrow."
    scene w3_5262 with dissolve
    "The meaning was pretty clear. The rising of the sun would make the thought of casually touching like this anathema once more, but until then..."
    "Our gentle treading in the water made for one final dance."
    scene w3_5263 with dissolve
    ver "..."
    scene w3_5264 with dissolve
    mc "Do you still find the night suffocating?"
    scene w3_5265 with dissolve
    ver "Yeah... and looking up at it right now is making me feel weightless."
    scene w3_5264 with dissolve
    mc "Then why are you doing it?"
    scene w3_5266 with dissolve
    ver "...have you lived in the city your whole life?"
    scene w3_5267 with dissolve
    mc "I'm a suburbanite. What about you?"
    scene w3_5266 with dissolve
    ver "Moved around a few times."
    scene w3_5267 with dissolve
    mc "Right, military brat."
    scene w3_5268 with dissolve
    ver "I didn't feel like I had roots until high school."
    scene w3_5269 with dissolve
    mc "Is that when you got into track and field?"
    scene w3_5268 with dissolve
    ver "You got it. Throwing a weighted ball doesn't sound very exciting does it?"
    scene w3_5267 with dissolve
    mc "To be honest? I've never seen anyone do shot put."
    scene w3_5266 with dissolve
    ver "Well... it's hardly a spectator sport, but its simplicity is beautiful."
    scene w3_5267 with dissolve
    mc "Throwing a weighted ball is beautiful?"
    scene w3_5270 with dissolve
    ver "Hell yeah it is. It's a rush."
    ver "Sure, there's a science behind your performance, but it {i}is{/i} simple. And that makes the competition more pure."
    scene w3_5272 with dissolve
    ver "It's a battle against yourself. Your whole world shrinks down to a 7-foot circle and your whole being becomes one simple, precise task."
    ver "{i}Chin-knee-toe.{/i} It'd be lonely if it didn't feel so freeing - and the drama!"
    scene w3_5273 with dissolve
    mc "Drama?"
    scene w3_5272 with dissolve
    ver "{i}The drama{/i}. The moment you let go of the shot, you feel it all."
    scene w3_5266 with dissolve
    ver "A {i}weightlessness{/i}, just like I was feeling right now... followed by an anticipation that makes you want to hurl. Was the throw as good as it felt it was?"
    scene w3_5272 with dissolve
    ver "And you forget about that anticipation just as quick as it came. You just watch the shot soar, rising and cutting through the sky like a bird, like an extension of your will."
    ver "Sometimes I wonder if that's what art feels like..."
    scene w3_5273 with dissolve
    mc "I didn't realize you were so romantic."
    scene w3_5268 with dissolve
    ver "Then the anticipation comes back. It begins to drop."
    ver "Hurtle towards its end, short-lived. Was the throw as good as it felt it was?"
    ver "It collides with the ground. {i}You left your mark{/i}."
    scene w3_5266 with dissolve
    ver "Then the world is no longer seven feet. You hear the crowd and the judges measure the distance."
    scene w3_5267 with dissolve
    mc "Was it as good as it felt it was?"
    scene w3_5268 with dissolve
    ver "Sometimes, a lot of times even... but... {i}not when it counted the most.{/i}"
    scene w3_5274 with dissolve
    ver "...what the hell am I going to do if this month is all for nothing, [mcf]? Should I just accept being a failure?"
    "{i}...with how she connected this and that, does she really think being a silver medalist makes her a failure?"
    mc "...plenty of people have ventures that don't work out for them. They say success is built on failure."
    scene w3_5275 with dissolve
    ver "I don't give a fuck what they say. The thought of picking myself off the ground? I just know it makes me want to vomit."
    scene w3_5276 with dissolve
    mc "...sure, but no matter how it makes you {i}feel{/i}, shouldn't you do it anyway? I think that's what real failure would be..."
    scene w3_5275 with dissolve
    ver "Blaaaah..."
    scene w3_5276 with dissolve
    mc "I was thinking, tonight... have you ever thought about catering the gym to women, or say... even a gay audience?"
    scene w3_5277 with dissolve
    ver "Not really. Shouldn't a gym be inclusive?"
    scene w3_5278 with dissolve
    mc "Eh, I don't know... I just know if I was a tubby fuck, I'd be more embarrassed to work out around women than I would be men."
    mc "And... the bar you took me to is pretty popular, isn't it?"
    scene w3_5280 with dissolve
    ver "Hideaway's an institution. It's got history. I don't."
    scene w3_5281 with dissolve
    mc "Yeah, but your ex's godmother is the owner. There's probably some promotional--"
    scene w3_5280 with dissolve
    ver "Eh. Nah..."
    scene w3_5279 with dissolve
    "Well, I could understand if she didn't want to lean on that..."
    scene w3_5281 with dissolve
    mc "...meh, just a drunken, half-assed thought. But, honestly... just knowing when something has run its course won't make you a loser."
    scene w3_5278 with dissolve
    mc "Being a loser is a matter of mindset."
    mct "(...{i}just don't see it that way until the exhibition is over.{/i})"
    scene w3_5277 with dissolve
    ver "Knowing that and believing it are two separate things..."
    scene w3_5278 with dissolve
    mc "Eh, leave tomorrow for tomorrow, right?"
    scene w3_5282 with dissolve
    ver "...you know, it's good talking to someone about this. And considering the secrecy behind this entire thing, it's a shortlist of someones."
    scene w3_5283 with dissolve

    if kat_polite == True:
        mc "I hear Mrs. Pulman keeps an open-door policy."
    else:
        mc "I hear Kathleen keeps an open-door policy."

    scene w3_5282 with dissolve
    ver "Hehe, yeah..."
    scene w3_5280 with dissolve
    ver "I hope getting some of {i}this{/i} is worth my blathering."
    scene w3_5281 with dissolve
    mc "What do you think?"
    scene w3_5280 with dissolve
    ver "...I think this whole situation is fucking weird."
    scene w3_5283 with dissolve
    mc "Tonight's been fun though. I don't think I'll forget the first woman to do {i}that{/i} to me."
    scene w3_5284 with dissolve
    ver "Of course you won't!"
    scene w3_5285 with dissolve
    kil "Heeeeeeeeeey! Woah, you're here and with... uhh..."
    mc "......"
    ver "..."
    scene w3_5286 with dissolve
    mct "(Ah, crap.)"
    ver "Nice place you got, pretty boy."
    scene w3_5287 with dissolve
    kil "Thanks! And nice tits!"
    scene w3_5288 with dissolve
    amber "Ummm... we're seeing a lot of each other, huh? Sorry for the... {i}intrusion?{/i}"
    scene w3_5289 with dissolve
    kil "Oh, yeah. Damn, I forgot. You called me about this! So this was who you're with..."
    scene w3_5290 with dissolve
    mc "You mean curiosity got the better of you?"
    scene w3_5291 with dissolve
    kil "No, I forgot! Honest! Heh, hehe... {i}you fucking killer.{/i}"
    scene w3_5292 with dissolve
    "........."
    "......"
    scene w3_5293 with dissolve
    kil "...soooooo since you're here, and butt naked, you wanna have a foursome or something?"
    scene w3_5294 with dissolve
    ver "...is it weird I want to take a shit in the pool right now?"
    kil "No, I mean... come on...! Just trying to be hospitable!"
    mc "No, it's a perfectly reasonable defense mechanism..."
    scene w3_5295 with dissolve
    kil "We're all hot and horny adults here, right? A little fun--"
    ver "I think it's time to call it a night."
    kil "No, I'll leave! I'll leave! I'll leave, don't let me--"
    scene w3_5296 with dissolve
    mc "It's your place, dude."
    ver "Yeah, let's..."
    ver "Thanks for the hospitality."
    scene w3_5297 with dissolve
    mc "FYI, you might want to get Alice to scrub your sofa tomorrow. I might've left some of myself on it."
    scene w3_5298 with dissolve
    amber "U-um... w-what?!"
    stop music fadeout 1.0
    scene black with fade

    if not persistent.w3VeronicaSex:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3VeronicaSex = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

    "......"
    "..."
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionveronica06 with blinds
    $ renpy.pause(6, hard=True)
    jump w3June16EndFull


label w3BathroomFrollick:

    play music "music/time-piece.ogg"
    scene w3_5299 with cmet
    brit "Wooooooah, you weren't kiddin'. Real fuckin' stallion~"
    mc "...is that your opinion as a zoologist?"
    brit "That is my opinion as a {i}cock-hungry bitch.{/i}"
    mc "...and we really just met, huh?"
    brit "Don't play coy now! Thank you for the meal!"
    scene w3_5300 with dissolve
    mc "A-ah..."
    mct "(I'm getting my dicked sucked at a lesbian bar. {b}That's new.{/b})"
    scene w3_5301 with dissolve

    if hanaGF == True:
        mct "(Sorry, Hana...)"

    mc "That hungry, huh...?"
    brit "Mmmh, mmmh, mmhhh..."
    scene w3_5302 with dissolve
    brit "I'm starving~"
    scene w3_5303 with dissolve
    mc "Have at it, then. All you can eat."
    scene w3_5305 with dissolve
    brit "...but it looks so tasty that I want to {i}savor{/i} it."
    scene w3_5303 with dissolve
    mc "I'm afraid we don't got the time for that."
    scene w3_5305 with dissolve
    brit "Mmmh, how 'bout you feed it to me then--"
    scene w3_5306 with hpunch
    brit "Ghhhuu-?!"
    $ renpy.music.set_volume(.2, 3, channel = "music")
    hide screen textbox2 with dissolve
    scene vd_toiletbj1_a with dissolve
    mc "{b}Suck it{/b}."
    brit "Mmmmhh~"
    show vd_toiletbj1 with dissolve
    play ambient "sound effects/fel3.wav"
    mc "If it's alright with you, I'm going to borrow your throat for the next few minutes."
    brit "Mmmh, mmhhhhh-!"
    mc "You can have it back when I pipe a fat wad down your throat, sound good?"
    brit "Mmmuh, uhhhuh-"
    "She seemed to agree with this direction, as she went with the flow, scarfing down my cock and letting me guide her head without fuss."
    mc "{i}Good girl.{/i}"
    "Something about the situation, and maybe everything up to this point, made me feel duly in control."
    brit "Gh, hhhu-"
    "I felt like I was entitled to face fuck the whole world, and she wasn't doing anything to dispel that notion."
    mc "Good {b}fucking{/b} girl, Brittany."
    "It was a unique sort of high, having my dick gliding in and out of a stranger's throat."
    brit "Hhuuh, ghhu...!"
    mct "(Is this what Ian feels when it just drops into his lap?')"
    "However, as my dick barreled into this slut's uvula, I found Veronica oddly on my mind."
    mct "(Heh... I hope Veronica gets something out of this tonight, even if it's just some haphazard fun...)"
    "Ah, fuck..."
    mct "(After all, she's got it rough, and I guess I kinda have her to thank for this.)"
    "*Chwup, fchwwup, kwwhup!*"
    mc "Good... ah..."
    brit "Mmmh, hhhhhmm-!"
    mc "That's it..."
    brit "Ghk, hhhu-"
    mc "{b}Swallow{/b} it... mmhhhmm..."
    brit "Hkk, hgggg-"
    mc "We're {b}just{/b} getting started..."
    play ambient "sound effects/fel4.wav"
    $ renpy.music.set_volume(.05, 2, channel = "music")
    scene w3_5307 with dissolve
    "Lewd sucking filled the bathroom."
    "If anyone came in, {i}they'd know{/i}."
    mct "(At least this was the men's room at a lez bar... so, that was probably a low chance of happening, yeah?)"
    "Not that I really cared..."
    brit "Ghh, hhhk-"
    "The privacy of a stall?"
    play ambient "sound effects/fel5.wav"
    scene vd_toiletbj2_a with dissolve
    show vd_toiletbj2
    "Turns out that was enough for me."
    mc "I'm going to go faster now, alright...?"
    "Actually, it may even be the opposite..."
    brit "Mmmh, mmmhhhhh, hhuuu-!"
    mct "(Part of me kinda wished someone would come in.)"
    "The thought alone made my balls tighten."
    scene w3_5391 with pixellate
    mct "(Just like with Rosalind...)"
    brit "Khu, hhkkuk- hhhkkuk..."
    mct "(Ha! Damn my tastes.)"
    scene vd_toiletbj2_a with pixellate
    show vd_toiletbj2
    brit "Hkku, hhhuhhkhk-"
    "To her complete credit, she was taking it like a {b}champ.{/b}"
    mc "A-ah! You're good at this!"
    "Letting me use her face like a tool..."
    brit "Khuk, hkuk, hhhkk!"
    mct "(What. An. Angel.)"
    brit "Hkkuk, hgghhuu, hheeeuuughh-"
    brit "Hkkh, ghhuhhukk, hhhk, eeeuhuhh-"
    brit "Hkk, hhhkk, huukkk, hhhk, pphhhk-"
    "{b}What a slut!{/b}"
    scene w3_5308 with dissolve
    mc "Ah, that's--"
    scene w3_5309 with dissolve
    play sound "sound effects/chair-squeek.wav"
    "*Creeeeeeeeeak*"
    mct "(Ah, crap... I got my wish...)"
    scene w3_5310 with dissolve
    brit "Hkk, hhehhh-"
    "...but I didn't stop."
    scene w3_5311 with dissolve
    ver "Jeez..."
    scene w3_5312 with dissolve
    ver "You fucking animal."
    scene w3_5313 with fade
    mc "Ah, Veronica...?"
    scene w3_5314 with dissolve
    ver "That's me."
    play ambient "sound effects/fel2.wav"
    scene vd_toiletbj3_a with dissolve
    show vd_toiletbj3 with dissolve
    mc "W-where's Olivia?! I hope she didn't ditch you..."
    brit "Hkuuk, hhhkkk-"
    "I didn't just not {i}stop.{/i} {b}I sped up.{/b}"
    ver "Actually, she's waiting outside. She's too embarrassed to come into the men's room."
    brit "Hkukk, hhhhhkkk, hhhhkk"
    ver "Kinda cute, huh?"
    scene w3_5315 with dissolve
    brit "Hkk, hhhhhukk, hhhhhkk-"
    scene w3_5316 with dissolve
    ver "Fuck, don't you think you should let her breathe?"
    scene w3_5315 with dissolve
    mc "W-what are you doing in here?"
    scene w3_5314 with dissolve
    ver "Olivia and I are heading out, but I didn't want to leave without saying a word."
    scene w3_5313 with dissolve
    mc "A-ah, is that right...? Nice!"
    scene vd_toiletbj3_a with dissolve
    show vd_toiletbj3 with dissolve
    brit "Euugh, hhhk, hhhgg-"
    mc "You hear that, Brit? Mission accomplished."
    brit "Ghh, hhhhk, hhhhhk-"
    mc "My friend and your friend are going to have a great night together."
    brit "Ghhhk, hhhhk-"
    mc "Good job."
    brit "Heuuk, hhhgghhhk-!"
    mc "Have a nice night, alright?"
    ver "Yeah, {b}it's going to be a good one{/b}. But, hey, Brittany?"
    brit "Hkk, hhhk, hhhhk?"
    "That would have to suffice as acknowledgment of the redhead's words."
    ver "Olivia says thanks for taking her out tonight."
    brit "Hnngg, hggggghkk-"
    ver "And, I feel the same way, [mcf]. Friends, right?"
    mc "Yeah, {i}friends{/i}..."
    scene w3_5317 with dissolve
    ver "Welp, we're going, then. Don't get a homicide charge, you big-dicked bastard."
    scene w3_5318 with dissolve
    brit "Hkkuhhhkk--"
    mc "Hey, wait..."
    "{i}A thought crossed my mind, but...{/i}"

    menu:
        "Disregard it.":
            mc "See you around."
            scene w3_5317 with dissolve
            ver "No doubt."
            scene w3_5319 with dissolve
            "......"
            scene w3_5320 with dissolve
            "..."
            scene vd_toiletbj3_a with dissolve
            show vd_toiletbj3 with dissolve
            mc "Sounds like mission accomplished.."
            brit "Hkk, hhhhuuk-!"
            mc "We should probably finish things..."
            "Honestly, Veronica's sudden appearance had pushed me near the edge..."
            brit "Hkk, eeuughhk, hhhk-!"
            "All that was left was..."
            brit "Hkkk-!"
            brit "Hkkk-! Hkhhhk-!"
            brit "Geeehhuu-! Hkkk!"
            stop ambient
            stop music
            play ambient "sound effects/gulp3.mp3"
            scene vd_toiletbj4_a with flash
            show vd_toiletbj4
            mc "{b}Take it!{/b}"
            "I let it all out."
            brit "Hnngg, hhhggg..."
            "A nice fat load for this tubby girl's stomach."
        "Ask her to stay for a minute."(chg=["veronica_passion_up"]):

            $ Veronica_Horniness += 1
            mc "...would you mind staying for a minute?"
            scene w3_5316 with dissolve
            ver "Eh, why...?"
            scene w3_5315 with dissolve
            mc "I kinda like you being there. It turns me on, but don't worry, I'm..."
            scene vd_toiletbj3_a with dissolve
            show vd_toiletbj3 with dissolve
            mc "...almost finished."
            brit "Hkkuk, hhhkkukk-!!!"
            scene w3_5315 with dissolve
            "......"
            "..."
            scene w3_5316 with dissolve
            ver "Fine, you damn freak."
            scene w3_5315 with dissolve
            mc "T-thanks!"
            scene vd_toiletbj3_a with dissolve
            show vd_toiletbj3 with dissolve
            ver "Yeah, no fucking problem."
            mc "A-aah... n-not going to waste your time, so--"
            brit "Hkk, hhhkk-!"
            mc " Olivia is waiting, so--"
            "The oh-so-familiar rush hit me, pushed along by the redhead's unseen eyes and ears."
            brit "Hkk, hhhhhk-!"
            ver "You that close, huh?"
            brit "Hkk, hhhhkh-! Eeguuk, hhkkk-!"
            mc "Y-yeahh...! A-any second...!"
            ver "{b}Good{/b}. Let me hear it."
            mc "Aaahhh-"

            if w3VeroHighness == True:
                ver "Cum for me, {i}your highness{/i}."
            else:
                ver "Cum for me, you big dumb--"

            stop ambient
            stop music
            play ambient "sound effects/gulp3.mp3"
            scene vd_toiletbj4_a with flash
            show vd_toiletbj4
            mc "{b}G--ahhhh!{/b}"
            "She knew just what to say."
            mc "Hnnnnggg-!"
            brit "Hkk, hheeuuhhhh...?"
            "So I let it all out."
            brit "Hnngg, hhhggg..."
            "A nice fat load for this tubby girl's stomach..."
            scene w3_5321 with dissolve
            mc "Drink it down..."
            scene w3_5322 with dissolve
            ver "...ha, God. I'm going."
            scene w3_5323 with dissolve

            if w2ExEndingVeronica == True:
                mc "Thanks, Ronnie."
            else:
                mc "Thanks, Veronica."

            scene w3_5319 with dissolve
            "......"
            scene w3_5320 with dissolve
            "..."

    stop ambient
    $ renpy.music.set_volume(1, 2, channel = "music")
    scene w3_5324 with fade
    mc "...we did a good thing tonight, didn't we?"
    brit "Hehe, hahaa... yeeah..."
    scene w3_5325 with dissolve
    brit "Good job us..."
    scene black with fade

    if not persistent.w3LBBathroomBJ:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3LBBathroomBJ = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "......"
    "..."
    $ renpy.end_replay()
    if mod_week3_veronica_dance_split:
        m_dev "Rewind time"
        jump mod_week3_veronica_dance_split_both
    jump w3June16EndHalf

label w3RosalindNightInLewd:
    if hanaGF == True:
        $ hanaCheat  += 1
        $ hanaTwoTime = True


    play music "music/cello-suite-No-1-G-Major-Prelude.ogg"
    scene rosa_hhj1_a with w19
    show rosa_hhj1
    movie "Am I the meanest?"
    movie "Sho'nuff!"
    mct "(How did it end up this way...?)"
    movie "Am I the prettiest?"
    movie "Sho'nuff!"
    "Well..."
    movie "Am I the baddest mofo low down around this town?"
    movie "Sho'nuff!"
    scene w3_5326 with pixellate
    "Maybe my first inclination was when I caught a glimpse of Rosalind's skin, still damp from an afternoon shower."
    scene rosa_hhj1_a with pixellate
    show rosa_hhj1
    movie "Well who am I?"
    movie "Sho'nuff!"
    scene w3_5327 with pixellate
    "Was that when the thought of how available she was crossed my head?"
    scene rosa_hhj1_a with pixellate
    show rosa_hhj1
    movie "Who am I?"
    movie "Sho'nuff!"
    movie "I can't hear you..."
    scene w3_5328 with pixellate
    "Did I initiate..."
    scene w3_5329 with dissolve
    "...or did she?"
    scene w3_5330 with wiperight
    "The thing about Rosalind was..."
    scene w3_5331 with w21
    "For one reason or another, she was very good at making it difficult to discern whose idea anything was."
    scene rosa_hhj2_a with pixellate
    show rosa_hhj2
    movie "SHO'NUFF!"
    rose "Should I...?"
    mc "Keep watching the movie..."


    if rosalindKilSolution == True:
        "Ian had enough tact not to push his threesome plans on her today, but me..."

        if w3RosalindMassaged == True:
            "I had told her to relax today, yet..."
    elif w3RosalindMassaged == True:
        "I had just told her to think of her stay like a vacation, yet..."
    else:

        pass

    "This kind of situation made me feel like a king."
    "Sure, I could just fold her over and crater her pussy into a busted mess, but this kind of casual attention had its own particular edge."
    mct "(And let's be honest... if she's going to be here for a few days...)"
    mc "Faster."
    scene rosa_hhj3_a with dissolve
    show rosa_hhj3 with dissolve
    "Things will only..."

    if hanaGF == True:
        mct "(Sorry, Hana...)"

    mct "(Yeeeeah...)"
    movie "I thought that maybe it would be a great idea if I got myself a bodyguard. You know, like someone to guard my body? What girl could do worse than to have her own real-life kung fu master?"
    rose "You made it seem like this movie was hilarious..."
    mc "You don't think it is?"
    rose "Uh... well..."
    mc "...I do have a bad habit of talking these things up. But come on, wasn't that the best 80's movie title song of all time?"
    scene rosa_hhj4_a with dissolve
    show rosa_hhj4 with dissolve
    "......"
    "..."
    "She didn't reply, as if other people didn't qualify that sort of thing."
    "........."
    "......"
    "..."
    "{i}Whatever.{/i}"
    mc "Mmmhh..."
    "The movie went on and on..."
    "Rosalind's hand had to be getting tired..."
    "*Shlick, schlicckk...!*"
    "She didn't stop, or complain."
    "She just played her dutiful part."
    scene w3_5332 with dissolve
    rose "I get to pick the next movie, okay?"
    scene w3_5333 with dissolve
    mc "Sure, but..."
    scene w3_5334 with dissolve
    mc "Try not to check out of this one."
    scene rosa_hhj3_a with dissolve
    show rosa_hhj3 with dissolve
    "*Shlick, scchhhhlicck~*"
    mc "...we can watch whatever romantic comedy you want."
    rose "That's sexist."
    "......"
    "..."
    rose "...and {i}Broadcast News{/i} is a classic."
    scene w3_5335 with dissolve
    mc "Fine. We'll watch that next."
    scene w3_5336 with dissolve
    mct "(I hadn't seen it.)"
    scene rosa_hhj4_a with dissolve
    show rosa_hhj4 with dissolve
    "*Shlick, scchhhhlicck~*"
    "........."
    "......"
    "...{i}yeah.{/i}"
    "*Shlick, scchhhhlicck, fwhhhhaap~*"
    "Selfishly one-sided, but..."
    movie "You possess the power of the Glow~"
    "This was a nice night after a long day. The whole vibe even felt cozy and nostalgic..."
    "*Shlick, sshhhliiick*"
    "Although there was the usual squeaking in my guts..."
    scene w3_5337 with dissolve
    "Foul feelings, dripping down from my amygdala and soaking into my fiber as the pressure built in my loins."


    if w2RosalindPhoto == True:
        "So, for a moment, I let my soul marinate."
    else:
        "So, for a moment, I let my soul marinate."


    "...or meditate?"
    "{i}However you put it{/i}."

    if w3RosalindMassaged == True:
        "I thought of all the goodwill I felt earlier in the day, and how flimsy it now felt."

    scene rosa_hhj3_a with dissolve
    show rosa_hhj3 with dissolve
    "All my pretenses seemed so small in face of my looming orgasm, but I knew one thing..."
    "I'd cum, it'd be over, and then we'd watch another movie..."
    mc "Uugghh..."
    mct "(Just hold on...)"
    "........."
    "......"
    "..."
    mc "Uggghh... I'm...!"
    mct "(Just hold on!)"
    scene w3_5338 with dissolve
    "........."
    "......"
    "...!"
    stop music
    play sound "sound effects/spurt.wav"
    scene w3_5339 with flash
    mc "Ghhaaa-!"
    "{i}I'd cum, the black feelings would leave me, and my selfishly one-sided cozy feelings would be secured.{/i}"
    scene w3_5340 with dissolve
    "........."
    scene w3_5341 with dissolve
    "......"
    scene w3_5342 with dissolve
    "..."
    scene w3_5343 with dissolve
    rose "I'll go clean it up."

    if w2RosalindPhoto == True:
        scene w3_5390 with pixellate
        "She'd accept it all...?"
        scene w3_5344 with pixellate
    else:
        scene w3_5344 with dissolve
        "The feelings still lurked, but..."

    menu w3RoseFoulFeelings1:
        "{color=#FF1493}[[Fullest Deal]{/color} No need to get a towel when she's already equipped to deal with it(w3RoseStayMean +=1)."(chg=["rosalind_down2"]) if w2RosalindPhoto == True:
            $ w3RoseStayMean +=1
            $ Rosalind_Affection -= 2
            play music "music/leaving-home.ogg"
            scene w3_5345 with dissolve
            mc "Use your tongue."
            scene w3_5346 with dissolve
            "She was so keen on this, right...?"
            scene w3_5347 with dissolve
            rose "Uh...?"
            scene w3_5345 with dissolve
            mc "Don't dirty a towel. {b}Use your tongue{/b}."
            scene w3_5346 with dissolve
            "It'd be easy to mistake the hard-up mother as having a blank look on her face."
            scene w3_5345 with dissolve
            mc "Lap it up."
            scene w3_5348 with dissolve
            "......"
            "..."
            "Naturally, anyone would pause over such a degrading request."
            scene w3_5349 with dissolve
            rose "Heh, {i}alright{/i}."
            "I didn't think that was quite it."
            scene w3_5350 with dissolve
            "There was a lot turning inside her head, but I was too cum-dumb and drenched in feelings of shit to have any hope of discerning if she was loathing me or coming to a practical acceptance."
            scene w3_5351 with dissolve
            mct "(Maybe both...)"
            scene w3_5352 with dissolve
            "I wanted to say a lot of mean things, but instead I stayed quiet."
            scene w3_5353 with dissolve
            "If she's going to be here a few days, there'd be other opportunities for that."
            scene w3_5354 with dissolve
            "...."
            scene w3_5355 with dissolve
            rose "...all done."
            scene w3_5356 with dissolve
            mc "Good girl."
            scene w3_5357 with dissolve
            rose "...is this what you had in mind when you told me to stay with you?"
            scene w3_5358 with dissolve
            "{i}No. It wasn't.{/i}"
            "Turns out, it didn't matter what I had in mind."
            scene black with fade
            "The rest of the night ended up relatively mundane."
            "......"
            "..."
            play ambient "sound effects/boobjob.wav"
            scene vic_sd_a with pixellate
            show vic_sd
            man "Almost there!"
            vic "Gh-!"
            man "You get to breathe when you drain my balls!"
            vic "Haeeeuch-!"
            stop ambient fadeout 5.0
            "............................................................"
            ".............................."
            "..............."
            scene black with w20
            man "Stupid bitch."
            stop music fadeout 3.0

            if not persistent.w3RoseCouchHJ:
                play sound "sound effects/notification.wav"
                show memoryunlock with dissolve
                $ renpy.pause(3, hard=True)
                $ persistent.w3RoseCouchHJ = True
                hide memoryunlock with dissolve
                $ renpy.pause(0.5, hard=True)
            "........."
            "......"
            "..."
            stop ambient
            hide screen textbox2 with dissolve
            hide screen qmenu with dissolve
            play sound "sound effects/sting-bluesy-vibes.wav"
            scene transitionrosalind05 with blinds
            $ renpy.pause(6, hard=True)
            play music "music/crinoline-dreams.ogg"
            scene w3_5379 with sunshine
            show screen textbox2 with dissolve
            show screen qmenu with dissolve
            mc "Mmmh..."
            mct "(Yesterday was an anomaly...)"
            scene w3_5380 with dissolve
            mc "{i}Heh...{/i}"
            mct "(Back to not having any trouble sleeping.)"
            $ renpy.end_replay()
            jump w3June17Start
        "Ignore what you're thinking.":


            scene w3_5359 with dissolve
            mc "Nah. Let me. I made the mess."
            rose "...?"
            "It was the least I could do..."
            scene w3_5360 with dissolve
            mc "In the meanwhile. Find out where we can watch {i}Broadcast News{/i}."
            scene w3_5361 with dissolve
            "......"
            scene w3_5362 with dissolve
            rose "...okay!"
            scene w3_5363 with dissolve
            "If she's going to be here a few days..."
            "...will I be able to further help myself?"
            scene w3_5364 with dissolve
            rose "......"
            scene w3_5365 with dissolve
            rose "..."
            scene black with fade

            if not persistent.w3RoseCouchHJ:
                play sound "sound effects/notification.wav"
                show memoryunlock with dissolve
                $ renpy.pause(3, hard=True)
                $ persistent.w3RoseCouchHJ = True
                hide memoryunlock with dissolve
                $ renpy.pause(0.5, hard=True)

            "....."
            "..."
            "The rest of the night ended up relatively mundane."
            hide screen textbox2 with dissolve
            hide screen qmenu with dissolve
            play sound "sound effects/sting-bluesy-vibes.wav"
            scene transitionrosalind05 with blinds
            $ renpy.pause(6, hard=True)
            play music "music/crinoline-dreams.ogg"
            scene w3_5379 with sunshine
            show screen textbox2 with dissolve
            show screen qmenu with dissolve
            mc "Mmmh..."
            mct "(Yesterday was an anomaly...)"
            scene w3_5380 with dissolve
            mc "{i}Heh...{/i}"
            mct "(Back to not having any trouble sleeping.)"
            $ renpy.end_replay()
            jump w3June17Start


        "{color=#696969}[[Fullest Deal] No need to get a towel when she's already equipped to deal with it.{/color}" if w2RosalindPhoto == False:
            jump w3RoseFoulFeelings1

label w3RosalindNightInPlatonic:
    "The rest of the night was low-key."
    scene w3_5326 with fade
    "Every so often I {i}felt{/i} her presence."
    scene w3_5366 with dissolve
    "...but the day passed by quickly."
    scene w3_5367 with dissolve
    "And strong woman she was, she settled into a comfortable equilibrium."
    scene w3_5368 with dissolve
    "Or perhaps that is just what I selfishly hoped."
    movie "Am I the baddest mofo low down around this town?"
    movie "Sho'nuff!"
    scene black with fade
    "Yes. A low-key evening, ushering me into a better sleep than the night before."
    "........."
    "......"
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionrosalind05 with blinds
    $ renpy.pause(6, hard=True)
    scene w3_5379 with sunshine
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    play music "music/crinoline-dreams.ogg"
    $ date = "june17day"
    show screen textbox2 with dissolve
    mct "(Yep...)"
    show june17day with squares
    mct "(Back to not having any trouble sleeping.)"
    scene w3_5380 with dissolve
    mc "{i}Heh...{/i}"
    "It only took one day for me to reset."
    jump w3June17Start

label w3June16EndHalf:
    play sound "sound effects/door-openclose.wav"
    scene w3_5369 with circlewipe
    "When I got home, I found Rosalind settled in."
    scene w3_5370 with dissolve
    mc "Oh, hey. Sorry for just disappearing on you like that."
    scene w3_5371 with dissolve
    rose "Don't be. I'm sure a young man like you has a busy life."
    scene w3_5369 with dissolve
    "I didn't know if I wanted to call it \"club business\" or not..."
    scene w3_5372 with dissolve
    mc "...it's been unusual lately."
    scene w3_5373 with dissolve
    "......"
    "..."
    scene w3_5374 with dissolve
    rose "I'll get you a glass of water and I'll heat up some of that stew. How does that sound?"
    scene w3_5375 with dissolve
    "......"
    scene w3_5376 with dissolve
    mc "...sounds brilliant."
    "Preemptive defense against a hangover?"
    scene black with fade
    "God bless her."
    "......"
    "..."
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionveronica06 with blinds
    $ renpy.pause(6, hard=True)
    scene w3_5379 with sunshine
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    play music "music/crinoline-dreams.ogg"
    "I ended up sleeping pretty good that night."
    "I let Rosalind have the bed and surprisingly she didn't fight me about it."
    $ date = "june17day"
    scene w3_5380 with dissolve

    if roseFlag == True:
        "Although, she did suggest we share it..."
        show june17day with squares
        mc "{i}Heh...{/i}"
        "And it also turned out that it only took me one day to reset from being disturbed."
    else:
        mc "{i}Heh...{/i}"
        show june17day with squares
        "Turns out, it only took me one day to reset from being disturbed."
    jump w3June17Start

label w3June16EndFull:
    scene w3_5380 with sunshine
    mc "Uuugghhh..."
    "When I got in, Rosalind was already conked out on the couch, but I got her to move up to my bed."
    scene w3_5379 with dissolve
    play music "music/crinoline-dreams.ogg"
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    $ date = "june17day"
    "Surprisingly, she didn't fight me on it."
    show june17day with squares

    if roseFlag == True:
        "Although, she did suggest we share it..."
    mct "(Wait...)"
    "Despite the heavy drinking..."
    mc "{i}Heh...{/i}"
    "I feel refreshed...?"
    mct "(Fuckin' freak of nature...)"
    jump w3June17Start

label w3June17Start:
    scene w3_5381 with dissolve
    rose "Mhhh, hmmm, mmmh~"
    "Humming, from the kitchen."
    scene w3_5382 with dissolve
    mc "Good morning."
    scene w3_5383 with dissolve
    rose "Oh, good. You're up."
    rose "I'll heat up your breakfast."
    scene w3_5384 with dissolve
    mc "...you've settled in nicely."
    scene w3_5385 with dissolve
    rose "Should you say that when I'm waiting on you?"
    scene w3_5384 with dissolve
    mc "Nope. I should say please and thank you, actually."
    play sound "sound effects/notification.wav"
    scene w3_5386 with dissolve
    "*Beep*"
    scene w3_5387 with fade
    "It was Ian."
    stop music fadeout 5.0

    mct "(True to his word...)"

    if w3VeronicaSex == True:
        mct "(Didn't this madman sleep?)"

    scene w3_5388 with dissolve
    "........."
    "..."
    scene w3_5389 with dissolve
    mc "...fix another plate, will you please, Rose?"
    mc "Ian's coming over."
    scene black with fade
    "He found a way to contact Darius' parents."
    "......"
    "..."
    stop sound
    jump june17StartContinue
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
