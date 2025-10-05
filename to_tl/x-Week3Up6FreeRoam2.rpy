



screen w3ExNavMenuStage2:

    imagemap:
        idle "gui/screens/imagemaps/w3ExNavMenu2_idle.png"
        hover "gui/screens/imagemaps/w3ExNavMenu2_hover.png"
        ground "gui/screens/imagemaps/w3ExNavMenu2_ground.png"

        hotspot (238,301,460,280) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExAOStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        hotspot (49,594,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExMRStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        hotspot (1205,307,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExSRStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        hotspot (734,307,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExHallwayStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        hotspot (529,588,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExPoolStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        hotspot (990,598,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExEHStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        hotspot (1441,594,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExVIPStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        hotspot (10, 22, 180, 180) action [ Play ("menu_click","sound effects/click2.wav") ], Rollback() hovered [ Play ("hover_load", "sound effects/click.wav")]

label w3ExNavMenuStage2:
    call screen w3ExNavMenuStage2 with pixellate

screen w3ExChecklist:
    imagemap:
        idle "gui/screens/imagemaps/eliaschecklist_idle.png"
        hover "gui/screens/imagemaps/eliaschecklist_hover.png"
        ground "gui/screens/imagemaps/eliaschecklist_ground.png"

        hotspot (17,10,100,100) action [ Play ("menu_click","sound effects/click2.wav") ], Rollback() hovered [ Play ("hover_load", "sound effects/click.wav")]

        if w3ExAOHanaLeft == False:
            add "images/misc/checklist/chkaugust-ongoing.png"
        else:
            add "images/misc/checklist/chkaugust-completed.png"

        if w3ExMR2Repeat == False:
            add "images/misc/checklist/chkjoe-ongoing.png"
        else:
            add "images/misc/checklist/chkjoe-completed.png"

        if w3ExKristoffMet == False:
            add "images/misc/checklist/chkjiji-ongoing.png"
        else:
            add "images/misc/checklist/chkjiji-completed.png"

        if w3ExAOHanaLeft == False:
            add "images/misc/checklist/chkhana-ongoing.png"
        else:
            add "images/misc/checklist/chkhana-completed.png"

        add "images/misc/checklist/chkchuck-ongoing.png"

        if w3ExSREmpty == False:
            add "images/misc/checklist/chkfuckrooms-ongoing.png"
        else:
            add "images/misc/checklist/chkfuckrooms-completed.png"

        if w3EHIntroSeen == False:
            add "images/misc/checklist/chkeh-ongoing.png"
        else:
            add "images/misc/checklist/chkeh-completed.png"

        if w3ExMR2Repeat == False:
            add "images/misc/checklist/chkmr-ongoing.png"
        else:
            add "images/misc/checklist/chkmr-completed.png"

        if w3ExKristoffMet == False:
            add "images/misc/checklist/chkpool-ongoing.png"
        else:
            add "images/misc/checklist/chkpool-completed.png"


label w3ExChecklist:
    call screen w3ExChecklist




screen w3ExAO2:
    if w3ExAO2Kimber == False:
        imagemap:
            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            imagebutton auto "gui/screens/imagebuttons/checklist_%s.png" xpos 0.06 action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExChecklist")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            idle "gui/screens/imagemaps/w3ExAO2Initial_idle.png"
            hover "gui/screens/imagemaps/w3ExAO2Initial_hover.png"
            ground "gui/screens/imagemaps/w3ExAO2Initial_ground.png"
            hotspot (340,241,1500,1500) action Jump("w3ExAOKimber")

    elif w3ExAOHanaLeft == False:
        imagemap:
            idle "gui/screens/imagemaps/w3ExAO2_idle.png"
            hover "gui/screens/imagemaps/w3ExAO2_hover.png"
            ground "gui/screens/imagemaps/w3ExAO2_ground.png"
            hotspot (8,50,800,800) action Jump("w3ExAOAllison")
            hotspot (1332,125,800,800) action Jump("w3ExAOAugust")

    else:
        imagemap:
            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            imagebutton auto "gui/screens/imagebuttons/checklist_%s.png" xpos 0.06 action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExChecklist")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            idle "gui/screens/imagemaps/w3ExAO2Solo_idle.png"
            hover "gui/screens/imagemaps/w3ExAO2Solo_hover.png"
            ground "gui/screens/imagemaps/w3ExAO2Solo_ground.png"
            hotspot (1332,125,800,800) action Jump("w3ExAOAugustSolo")

label w3ExAOStage2:
    show black
    if w3ExAO2Kimber == False:
        $ renpy.music.play("music/take-the-lead.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    else:
        $ renpy.music.play("music/as-i-figure.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w3ExAO2 with pixellate

label w3ExAOKimber:
    $ w3ExAO2Kimber = True
    kimber "I--"

    play sound "sound effects/door-open.wav"
    scene w3_12758 with dissolve
    "The moment we entered, {b}bam.{/b} Conversation ceased and it was like a dramatic scene frozen in time."

    if w3ExJacobStage1Repeat == True:
        "Kimber stopped whatever point she was trying to make, a look of consternation shadowing her beautiful complexion."
    else:
        "The woman I saw in the hallway stopped whatever point she was making, a look of consternation shadowing her beautiful complexion."

    aug "That's enough, Kimber. Do not talk business in front of our guest."

    if w3ExJacobStage1Repeat == False:
        mct "(Ah, so that's who it was...)"

    play sound "sound effects/door-close.wav"
    scene w3_12759 with dissolve
    kimber "B-but--"
    scene w3_12760 with dissolve
    aug "I said that's enough! Hana has been {b}very{/b} kind with you, and I've allowed her that as she learns the business, but you're forgetting who {b}{i}I{/i}{/b} am."
    "The mood was plain as day between pimp and prostitute, but Hana had a more complicated expression; a rich mix of frustration, indignation, and a general rather-be-any-other-place-ness."
    scene w3_12761 with dissolve
    aug "Go home. Dalia will be in touch with you later."
    scene w3_12762 with dissolve
    kimber "I'm sorry, it's just--!"
    scene w3_12763 with dissolve
    scene w3_12762 with dissolve
    "August's glanced over at me, finally acknowledging my presence, and issuing a command with a tilt of his head toward the door: {i}see her out.{/i}"
    mct "(Alright...)"
    scene w3_12764 with dissolve
    kimber "--!"
    "Naturally, the tall whore shirked at my touch, having no idea of who I was - a response that undoubtably made me look {b}and{/b} feel like a thug."

    menu:
        "Alright, play the role."(chg=["tough_up", "august_up"]):
            $ August_Friendship +=1
            $ toughness += 1
            scene w3_12766 with dissolve
            mc "Come on."
            scene w3_12765 with dissolve
            kimber "Get your hands off me--"
            scene w3_12766 with dissolve
            mc "You heard Mr. Brynes. Don't be fuckin' stupid."
            scene w3_12767 with dissolve
            kimber "--?!"
            "Something told me she'd respond better to this approach."
        "Quote unquote reason with her."(chg=["hana_up"]):
            $ Hana_Affection +=1
            scene w3_12768 with dissolve
            mc "Better me than Warren."
            scene w3_12769 with dissolve
            "......"
            scene w3_12770 with dissolve
            kimber "...fuck!"

    play sound "sound effects/spit.wav"
    scene black with fade
    aug "Mr. Ford, it's nice to--"
    scene w3_12771 with fade
    mc "...Jesus, are you normally this uncouth?"
    "{i}The bitch spit on my goddamn shoe.{/i}"
    scene w3_12772 with dissolve
    kimber "Who the fuck are you? You look even younger than Daddy's girl!"
    scene w3_12773 with dissolve
    mc "...how long have you worked here?"
    scene w3_12774 with dissolve
    kimber "What?! I don't know, a year?"
    scene w3_12775 with dissolve
    mc "Well, I've only been here a little over a month, but even I know nothing in there was productive. Was it?"
    scene w3_12776 with dissolve
    kimber "You know what? Forget who you are. {b}WHO{/b} does that bitch think she is taking away my hours?!"
    play sound "sound effects/door-close.wav"
    scene w3_12777 with vpunch
    hana "This {b}bitch{/b} is your boss. Why can't you get that through your thick head?!"
    "Hana had followed us out, and judging by how aggro she was, what I {i}didn't see{/i} must have gotten pretty heated..."
    scene w3_12778 with dissolve
    kimber "Bullshit you are! I'm not listening to a kid!"
    scene w3_12780 with dissolve
    hana "We're the same age! Hell, I might even be older!"
    scene w3_12779 with dissolve
    "I had never quite seen her like this. Hana was drawn down to Kimber's level in a rare glimpse of immaturity."
    scene w3_12778 with dissolve
    kimber "Exactly! I'm not getting pimped out by a {b}girl{/b} my age!"
    scene w3_12781 with dissolve
    hana "W-wha...?! This is a {b}gender{/b} thing?!"
    scene w3_12780 with dissolve
    hana "How can you be so transparent and have {i}ZERO{/i} self-awareness?! Newsflash, I've been trying to do you a favor here and cut you a lil' slack, but I'm starting to understand why you've decided to spread your legs for a living!"
    scene w3_12782 with dissolve
    kimber "You fuckin-!"
    scene w3_12783 with dissolve
    mc "Uh..."
    "I did the smart thing here. {b}I kept my fucking mouth shut.{/b}"
    scene w3_12784 with dissolve
    kimber "Look, I {b}need{/b} the money! Book me some clients this week, or are you going to be stupid and lose out on all the money you steal from me!"
    scene w3_12785 with dissolve
    hana "Well! If you need cash, you should've thought about that before you laid out of work in the first place!"
    scene w3_12784 with dissolve
    kimber "I was sick! It's not my fault if a client keeps paying for drinks, is it?!"
    scene w3_12785 with dissolve
    hana "I asked around! You {i}always{/i} party too hard! None of the other girls have this problem, yet they have to pick up your slack!"
    scene w3_12786 with dissolve
    kimber "So wha--"
    hana "--{b}AND{/b} shuffling bookings around just because you don't feel like coming in is more trouble than your boney ass brings in. It's better to just cut you from the schedule."
    scene w3_12787 with dissolve
    "Now my silence was less primal fear and more stunned at how deftly Hana fell into the role of manager."
    "......"
    scene w3_12788 with dissolve
    kimber "...please? {i}I'm sorry{/i}, okay?!"
    mct "(Holy shit...)"
    "Hana changed her tune."
    scene w3_12789 with dissolve
    hana "*Sigh* {b}Look...{/b} we're getting off on the wrong foot and we're down a house girl tonight. I know you usually only do out-calls, but if you fill in, it's a clean slate. That's fair, right?"
    scene w3_12788 with dissolve
    kimber "Uh, I can't tonight... I have to see my boyfriend."
    scene w3_12790 with dissolve
    hana "*You...!*"
    scene w3_12791 with dissolve
    hana "*Ahem* Is that {i}really{/i} the choice you want to make right now? Right when I'm giving you what you're asking for?"
    kimber "Uh... ah..."
    hana "Get your ass into a uniform, you junkie slut."
    scene w3_12792 with dissolve
    kimber "W-whatever. T-thanks."
    scene w3_12793 with dissolve
    "..."
    scene w3_12794 with dissolve
    mc "Huh... didn't know you had that in you."
    scene w3_12795 with dissolve
    hana "{b}God{/b}, I hate that she brought that out of me."
    scene w3_12794 with dissolve
    mc "She must have really gotten under your skin."
    scene w3_12795 with dissolve
    hana "You have {i}no{/i} idea how many voice mails she's left me in the last few hours."

    if hanaGF == True:
        scene w3_12796 with dissolve
        "........."
        "......"
        scene w3_12798 with dissolve
        hana "Ugh, this job..."
        scene w3_12797 with dissolve
        mc "You're taking it pretty seriously. I think you handled that pretty well."
        scene w3_12798 with dissolve
        hana "I was screaming at her like I couldn't control myself."
        scene w3_12797 with dissolve
        mc "I don't know... looks to me like you got through to her..."
        scene w3_12798 with dissolve
        hana "Time will tell... so who's that guy you're with? That the new patron?"
    else:

        scene w3_12799 with dissolve
        hana "Ugh, this job..."
        scene w3_12800 with dissolve
        mc "You're taking it pretty seriously. I think you handled that pretty well."
        scene w3_12799 with dissolve
        hana "I was screaming at her like I couldn't control myself."
        scene w3_12800 with dissolve
        mc "I don't know... looks to me like you got through to her..."
        scene w3_12799 with dissolve
        hana "Time will tell... so who's that guy you're with? That the new patron?"

    scene black with fade
    mc "Ah, yeah... I guess I should introduce you."
    jump w3ExAOStage2


label w3ExAOAllison:
    $ w3ExAOAllisonSeen = True
    $ Allison_Interest +=1
    scene w3_12801 with dissolve
    "When we returned, I noticed Hana eyeing up Allison. The movie star was on stand by, looking pretty, but not much else while the men talked."
    "She looked bored, a drink in her hand, but her mind elsewhere. The evening's battle garb had even robbed her of the refuge of a phone."
    scene w3_12802 with dissolve
    "I filled Hana in on the details. She recognized her from last year's batch of Carnations, but who precisely she was and why she was here {i}now{/i} was in question."
    scene w3_12803 with dissolve
    hana "Oh... {i}really?{/i} Why would she..."
    "I knew what she was getting at as I watched her amber eyes come to the same realization I had earlier."
    scene w3_12804 with dissolve
    "Meanwhile, August and Elias were getting along great, lost in conversation - which was all the fledgling rock star needed to follow where her feet were already pointed."
    scene w3_12805 with dissolve
    hana "Hey! Can I ask you something?"
    scene w3_12806 with dissolve
    allison "......"
    scene w3_12807 with dissolve
    allison "...I remember you. The bartender who scowled all the time."
    scene w3_12808 with dissolve
    hana "I just want to know something."
    scene w3_12809 with dissolve
    allison "...*sigh* sure, they're not paying attention. This will be good."
    hana "Do you work here?"
    scene w3_12810 with dissolve
    allison "Noooo..."
    scene w3_12811 with dissolve
    allison "I'm not a prostitute, if that's what you're asking."
    scene w3_12812 with dissolve
    "That clearly, and understandably, did not compute with Hana. She looked at me as if she herself might be crazy."
    scene w3_12808 with dissolve
    hana "*Whisper* ...but you're here, with {b}that{/b} man."
    scene w3_12807 with dissolve
    allison "I'm his date."
    scene w3_12806 with dissolve
    "Hana was closing in on something I was curious about too, so I helped cut off Allison's retreat."
    scene w3_12813 with dissolve
    mc "And does Mrs. Pulman tell you who to date?"
    scene w3_12814 with dissolve
    "......"
    scene w3_12815 with dissolve
    allison "...it's complicated."
    scene w3_12812 with dissolve
    hana "...?"
    scene w3_12813 with dissolve
    mc "Let's put it another way: you joined the exhibition to boost your career, right?"
    scene w3_12814 with dissolve
    allison "..."
    scene w3_12816 with dissolve
    mc "Hey! I've seen a couple of your movies. You're very talented, but I get that it's a business you need a leg up in. We're just curious, Hana recently got promoted, and--"
    scene w3_12817 with dissolve
    hana "I'd like to know just how fucked up this place is."
    scene w3_12818 with dissolve
    allison "W-wha..? Ha! Look around!"
    scene w3_12819 with dissolve
    hana "Point taken, but I was just wondering. If the club made you, it can also \"unmake\" you too. Is that the deal?"
    scene w3_12820 with dissolve
    "She didn't want to say it, but a tentative nod sufficed."
    scene w3_12821 with dissolve
    "Hana clearly did not like that confirmation, and neither did I."
    "Part of me hoped it was only Allison's rising fame that made her valuable enough to keep around, lest {i}my{/i} Carnations not get their ride off into the sunset."
    scene w3_12822 with dissolve
    "It made ugly sense though. The exhibition raised the girls' value and won them fans. It would be poor business not to reap what you've sown..."
    allison "Are you done with the dumb questions?"
    scene w3_12823 with dissolve
    "Neither of us were, but the pitstop was over. Elias was looking over at us."
    hana "Uh, yeah... {b}thanks.{/b}"
    scene black with fade
    "Moral compunctions aside, we needed to get back to the center of attention."
    jump w3ExAOAugust

label w3ExAOAugust:
    $ w3ExAOHanaLeft = True
    $ w3Stage2Time += 1
    if w3ExAOAllisonSeen == False:
        $ August_Friendship +=1
        $ Elias_Friendship +=1
        scene w3_12824 with dissolve
        "When we returned, we found a more amiable mood. Elias and August had warmed to each other quickly, presently chatting away without even realizing we were here."
        "I noticed Hana curiously eyeing up Allison, but I rejoined the men."
        scene w3_12825 with dissolve
        elias "Back so soon, Bukowski? You didn't throw her out a window, did you?"
        aug "Baha, you would be doing me a favor!"
        scene w3_12826 with dissolve
        mc "Hana came up with an excellent solution, actually. She's quite the little pimp."
        scene w3_12827 with dissolve
        aug "I'll get her to tell me about it later."
        scene w3_12828 with dissolve
        elias "This is nice..."
        scene w3_12829 with dissolve
        aug "Huh, what is?"
        scene w3_12828 with dissolve
        elias "{b}Men{/b}, standing around... a whole night in front of us."
        scene w3_12829 with dissolve
        aug "We're happy to have you, Elias."
        scene w3_12830 with dissolve
        elias "And that's exactly what I'm getting at, because I can tell you actually mean that!"
        scene w3_12831 with dissolve
        aug "You bring the right {i}prestige{/i} to this place. Some of Kathy's recent admissions... {i}leave a lot to be desired.{/}"
        scene w3_12832 with dissolve
        aug "I'm just sorry you had to stumble into some unpleasant business."
        elias "Oh, you don't have to worry about me seeing how the sausage is made. Trust me, I deal with this kind of thing all the time."
    else:
        scene w3_12833 with dissolve
        elias "Ah, there you are, Bukowski. What took so long?"
        mc "We were just chatting with your lovely date."
        hana "Ha, yeah... {size=-15}date...{/size}"
        scene w3_12834 with dissolve
        aug "Thanks for taking care of that kid. Sorry you had to see that, Elias."
        elias "Oh, you don't have to worry about me seeing how the sausage is made. Trust me, I deal with this kind of thing all the time."

    scene w3_12835 with dissolve
    aug "Haha, I'm sure you do, but I promise you... whores are even more entitled than starlets. Lot of them {i}want{/i} you to smack 'em around, else they have a fuckin' existential crisis. It gets tiring."
    scene w3_12836 with dissolve
    hana "Jesus Christ, Dad! Do you even hear yourself?!"
    aug "As you can see, my daughter still has a high opinion of the human race, but she's learning the ropes."
    scene w3_12837 with dissolve
    elias "Oh, this beautiful woman's your daughter?"
    aug "Can you not see the uncanny resemblance? Introduce yourself, sweetheart."
    scene w3_12838 with dissolve
    hana "Hi, I'm Hana."
    aug "I told you about him. Hana, this is Elias Ford."
    scene w3_12839 with dissolve
    hana "Oh..."

    if w3ExAOAllisonSeen == True:
        "Just like with Allison, Hana made the connection."
    else:
        "{i}Oh.{/i} Hana was well aware of his connection with Felicia if her dour expression was anything to go by."

    scene w3_12840 with dissolve
    elias "Don't worry, I {b}don't{/b} see the resemblance."
    scene w3_12841 with dissolve
    aug "Baha! Don't say that when we've only just met!"
    "Just earlier last week she was in a tiff over me interviewing him, but now she was face-to-face with that very man whose marriage she was helping spit on."
    scene w3_12842 with dissolve
    hana "Right, you... you run a modeling agency?"
    elias "Movies and music too, but that's right."
    scene w3_12843 with dissolve
    aug "Music?! You hear that, Hana? He--"
    scene w3_12844 with dissolve
    hana "*Sigh* Don't even suggest it, Dad."
    "{i}Dad,{/i} like a teenager admonishing a parent. Meager as it was, the semi-affectionate inflection stuck in my mind."
    scene w3_12845 with dissolve
    aug "Hana plays the drums in a band--"
    scene w3_12846 with dissolve
    hana "I said don't!"
    scene w3_12847 with dissolve
    aug "........."
    aug "......"
    scene w3_12848 with dissolve
    aug "By the way, I also apologize for not meeting you until now, but the timing was poor this week."
    scene w3_12849 with dissolve
    aug "Drinks with my daughter, you see..."
    elias "That's two apologies, August. You can stuff them."
    elias "There's no offense taken. In a sense, {b}tonight{/b} was our appointment."
    scene w3_12850 with dissolve
    aug "I'm happy you understand... you have a son and daughter, I believe."
    elias "I do... I do indeed..."
    mct "(...holy {i}fuck.{/i} Holy... {b}fuck!{/b})"
    scene w3_12851 with dissolve
    elias "What's this, August? Your daughter's allowance money?"
    scene w3_12852 with dissolve
    "That had to be a million dollars. I had never seen so much money in my life, and judging by Hana's disbelieving side glances... neither had she."
    scene w3_12853 with dissolve
    hana "If it is, this old bastard has been holding out on me..."
    scene w3_12852 with dissolve
    "But rather than be appalled at the obscenity of her father casually handing over enough money to keep Hana's mom well cared for and comfortable for the rest of her life, she looked..."
    scene w3_12854 with dissolve
    "{b}Enthralled.{/b}"
    "It was, after all, the kind of money that made one irrational. Just being in proximity of it put bad ideas in your head. I had little doubt that what was going through Hana's head mirrored my own feelings."
    scene w3_12855 with dissolve
    aug "It's our collective vote of confidence that you'll look after the city. We know you have a lot of mouths to feed."
    scene w3_12856 with dissolve
    elias "That's a lot of weight to put on my shoulders, old man... things are moving fast..."
    scene w3_12855 with dissolve
    aug "You'll carry that weight well. I'm a good judge of character, and I have faith in you."
    scene w3_12857 with dissolve
    aug "Welcome to the club, Elias."

    scene w3_12858 with dissolve
    if hanaGF == True:
        hana "Hey, boyfriend...?"
    else:
        hana "Hey, [mcf]...?"

    scene w3_12859 with dissolve
    mc "Yeah...?"
    scene w3_12858 with dissolve
    hana "I'm going to go..."
    scene w3_12859 with dissolve
    mc "You're leaving me to fend for myself? Why would you do a cruel thing like that?"
    scene w3_12858 with dissolve
    hana "Kathy has a costume she wants me to wear tonight... I should get changed..."
    scene w3_12859 with dissolve
    mc "You're down for that...?"
    scene w3_12860 with dissolve
    hana "I'll let you know after I see it, but..."
    scene w3_12862 with dissolve
    hana "...it wouldn't do for an {i}owner{/i} not to play ball."
    scene w3_12861 with dissolve
    "As she spoke, just like my own, Hana's eyes were on the money."
    scene w3_12863 with dissolve
    mc "Yeah, I get that..."

    if hanaGF == True:
        scene w3_12864 with dissolve
        hana "Besides, could be fun for later..."

        if w3HanaMomMeet == True:
            hana "I mean... mhh... {b}you{/b} didn't cum earlier..."

        scene w3_12865 with dissolve
        mc "Oh... uh... I like the sound of that..."
        scene w3_12864 with dissolve
        hana "Yeah... looking forward to it...."
    else:
        scene w3_12859 with dissolve
        mc "See you later."
        scene w3_12858 with dissolve
        hana "What a night..."
    scene black with fade
    "Hana left, and the men talked for quite some time."
    scene w3_12866 with fade
    "Allison rejoined us at some point, leaving me to stare at a million dollars while rubbing elbows with a movie star."
    scene black with fade
    "Every fiber of my being was telling me {b}I belong here{/b}, and if I didn't {i}want{/i} to be... what was wrong with me?"
    jump w3ExAOStage2

label w3ExAOAugustSolo:
    if w3ExAOAugustSoloRepeat == False:
        $ w3ExAOAugustSoloRepeat = True
        scene w3_12867 with dissolve
        aug "If you get some time to yourself later, drop by and see me, alright?"
    else:

        $ randint = renpy.random.randint(1, 2)
        scene w3_12868 with dissolve
        if randint == 1:
            "I should take Elias elsewhere."
        elif randint == 2:
            "There are more people to introduce Elias to."

    jump w3ExAOStage2




screen w3ExMR2:
    if w3ExMR2Repeat == False:
        imagemap:
            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            imagebutton auto "gui/screens/imagebuttons/checklist_%s.png" xpos 0.06 action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExChecklist")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            idle "gui/screens/imagemaps/w3ExMR2Initial_idle.png"
            hover "gui/screens/imagemaps/w3ExMR2Initial_hover.png"
            ground "gui/screens/imagemaps/w3ExMR2Initial_ground.png"
            hotspot (340,241,1500,1500) action Jump("w3ExShelbyLucy")

    else:
        imagemap:
            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            imagebutton auto "gui/screens/imagebuttons/checklist_%s.png" xpos 0.06 action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExChecklist")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            idle "gui/screens/imagemaps/w3ExMR2_idle.png"
            hover "gui/screens/imagemaps/w3ExMR2_hover.png"
            ground "gui/screens/imagemaps/w3ExMR2_ground.png"
            hotspot (1100,120,800,800) action Jump("w3ExShelbyLucy")


label w3ExMRStage2:
    show black
    $ renpy.music.play("music/jah-jah-bangs.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w3ExMR2 with pixellate

label w3ExShelbyLucy:
    if w3ExMR2Repeat == False:
        $ w3Stage2Time += 1
        $ w3ExMR2Repeat = True
        scene w3_12869 with dissolve
        shel "Hmm...? Who's that?"
        "A quick peek into one of the massage rooms, and I had found one of the men that the old woman directed me to introduce Elias to: Senator Shelby."
        mc "Oh, sorry, sir. I didn't realize anyone was in here. I was showing Mr. Ford ar--"
        scene w3_12870 with dissolve
        shel "{b}Elias?!{/b} No, come in! God, please! All you're doing is interrupting a piss poor massage from a sausage-fingered idiot."
        scene w3_12871 with dissolve
        lucy "Oh, uh... s-should I--"
        scene w3_12872 with dissolve
        shel "I didn't say stop, you nitwit!"
        scene w3_12873 with dissolve
        lucy "Uh, just tell me where it feels good--"
        scene w3_12874 with dissolve
        "Flustered, Lucy unconfidently resumed kneading the old politician's back, making it inevitable that she wouldn't impress."
        scene black with fade
        mc "Mr. Ford, I'd like you to meet Senator Joe Shelby."
        scene w3_12875 with fade
        shel "So, Ford... I've been told to throw my hat in with you."
        scene w3_12876 with dissolve
        elias "You've been told? Is that not your decision to make?"
        "The two men didn't exchange so much as a hello, barreling past all formalities."
        scene w3_12875 with dissolve
        shel "After tonight? {b}No{/b}, it isn't. You're in with us now, so I'll play ball."
        scene w3_12878 with dissolve
        elias "Well... this has all been a bit too good to be true. I thought Kathleen {b}oversold{/b} the perks, but--"
        scene w3_12877 with dissolve
        shel "You'll find ways to pay it forward."
        scene w3_12878 with dissolve
        elias "Naturally..."
        scene w3_12879 with dissolve
        "The room got eerily silent, as the two men looked into the not-quite-fathomless depths of their opposite's eyes. {i}This was the real hello.{/i}"
        "Neither Allison nor I dared to interject, and even Lucy froze in place - forgetting both her duties and even to breathe."
        scene w3_12880 with dissolve
        shel "I didn't know what to make of you, Ford."
        scene w3_12881 with dissolve
        "Finally, the tension was cut, and we all collectively breathed a sigh of relief."
        scene w3_12882 with dissolve
        shel "Alderman Reyes and I used to play baseball together. That was pretty ballsy what you did."
        scene w3_12883 with dissolve
        elias "...I'll delete the footage."
        scene w3_12884 with dissolve
        shel "No, don't. Like I care if that weak idiot got honey potted. I just want you to know you were on the radar months ago, when you started making your moves."
        scene w3_12883 with dissolve
        elias "Reyes came running to daddy, huh?"
        scene w3_12882 with dissolve
        shel "That's right. One way or another, you were going to end up here. The fact you got here {i}independent{/i} of that... the world works in mysterious ways."
        scene w3_12885 with dissolve
        "Elias just looked at the old bastard like he didn't understand, not exactly."
        "Meanwhile, Shelby just smiled, basking in the delicious irony that it was Felicia who ultimately put him here."
        scene w3_12886 with dissolve
        elias "It's great to meet--"
        shel "Jesus Christ, woman, all you're doing is pinching my back!! I thought you said you've given massages before!"
        scene w3_12887 with dissolve
        lucy "I h-have, I've given my husband--"
        scene w3_12888 with dissolve
        shel "Isn't that cute! Now, fuck off and go find me a slut who knows what she's doing!"
        scene w3_12890 with dissolve
        lucy "I, uhh- aum, I can-"
        scene w3_12889 with dissolve
        "If I were in her shoes, I'd {b}gratefully{/b} get the fuck out of here, but for some reason... she looked like she didn't want to leave."
        scene w3_12887 with dissolve
        lucy "I can... I can do {i}other{/i} things..."
        scene w3_12888 with dissolve
        shel "So can every other girl in this place."
        scene w3_12889 with dissolve
        lucy "......"
        scene w3_12891 with dissolve
        "She looked at me, apprehensively, but I just dismissed her with a nod. "
        scene w3_12893 with pixellate
        shel "You can at least be a proper fucking toilet bowl!"
        scene w3_12894 with pixellate
        mct "(Uh...)"
        scene w3_12895 with pixellate
        "...even if she didn't know it, she was getting off lucky."
        shel "How hard is it to rub someone's back? This isn't some back alley parlor. The girls should take classes!"
        scene w3_12896 with dissolve
        mc "Should I leave you two to talk while I find someone for Mr. Shelby?"
        scene w3_12897 with dissolve
        shel "Oh, he speaks! Since you're here, you can give me a massage."
        scene w3_12898 with dissolve
        mc "Uh, I'm not any more of a masseuse than Lucy is, sir."
        scene w3_12899 with dissolve
        shel "Maybe not, but you've got something between your ears at least. Probably know enough not to jab your fingers into my spine. Besides, I wasn't asking."
        scene w3_12900 with dissolve
        mct "(This fucker...!)"
        "Right when I felt the indignation rise in my stomach..."
        scene w3_12901 with dissolve
        elias "Sorry, Bukowski is showing me around before my party, but it's a pleasure to meet you and I {b}am{/i} grateful for your endorsement."
        scene w3_12902 with dissolve
        "Elias swooped in, saving both his time and me from doing something I didn't want to do."
        scene w3_12903 with dissolve
        shel "Alright, then..."
        scene w3_12904 with dissolve
        shel "I guess I'll soak. Hopefully that whore finds someone quick."
        scene w3_12905 with dissolve
        mc "I'll see to it that she does."
        shel "You do that..."
        scene w3_12906 with dissolve
        "Before we left, Elias gave me a reassuring touch and a smile of commiseration that read... {i}what a prick, huh?{/i}"
        "It was a confusingly empathetic gesture from the has-been mogul, but one I strangely appreciated. "
        scene black with fade
        play sound "sound effects/water-splash.wav"
        "..."
    else:
        $ randint = renpy.random.randint(1, 3)
        scene w3_12907 with dissolve
        if randint == 1:
            "Let's leave Shelby to his soak. I don't feel like marinating in the old man's testicle sweat..."
        elif randint == 2:
            "There are better sights to see than an old wrinkly fuck bathing."
        else:
            "Let's show Elias some of the building's {i}other{/i} amenities."

    jump w3ExMRStage2



screen w3ExSR2:
    if w3SRIntroSeen == False:
        imagemap:
            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            imagebutton auto "gui/screens/imagebuttons/checklist_%s.png" xpos 0.06 action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExChecklist")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            idle "gui/screens/imagemaps/w3ExSR2Initial_idle.png"
            hover "gui/screens/imagemaps/w3ExSR2Initial_hover.png"
            ground "gui/screens/imagemaps/w3ExSR2Initial_ground.png"
            hotspot (700,100,2000,2000) action Jump("w3ExSRIntro")

    elif w3ExSREmpty == False:
        imagemap:
            idle "gui/screens/imagemaps/w3ExSR2_idle.png"
            hover "gui/screens/imagemaps/w3ExSR2_hover.png"
            ground "gui/screens/imagemaps/w3ExSR2_ground.png"
            hotspot (1600,112,1200,1200) action Jump("w3ExSRAllison")
            hotspot (21,106,1200,1200) action Jump("w3ExSRElias")

    else:
        imagemap:
            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            imagebutton auto "gui/screens/imagebuttons/checklist_%s.png" xpos 0.06 action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExChecklist")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            idle "gui/screens/imagemaps/w3ExSR2_empty.png"
            hover "gui/screens/imagemaps/w3ExSR2_empty.png"
            ground "gui/screens/imagemaps/w3ExSR2_empty.png"


label w3ExSRStage2:
    show black
    $ renpy.music.play("music/myst-on-the-moor.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w3ExSR2 with pixellate


label w3ExSRIntro:
    $ w3SRIntroSeen = True
    scene w3_12908 with fade
    mc "This is..."
    scene w3_12909 with dissolve
    "I decided to show Elias a few of the more private areas of the building."
    scene w3_12908 with dissolve
    mc "There are regular bedrooms, and quite a few \"thematic ones\"... as you'd expect."
    scene w3_12910 with dissolve
    elias "Red isn't quite my color..."
    mc "Ha, well, you better get used to it."
    scene w3_12911 with dissolve
    allison "Mmmh, what are you doing, mister?"
    scene w3_12912 with dissolve
    "The movie star put a cute lilt behind her question, far and away from her mature appearance. That was something I was realizing about the champion Carnation; she had eyes of ice and a sharp tongue, but she played the coquettish whore well."
    scene w3_12913 with dissolve
    elias "Would something like this be your first choice?"
    scene w3_12914 with dissolve
    allison "You're kidding...♥ No..."
    scene w3_12912 with dissolve
    mct "(He sure has a type...)"
    scene w3_12911 with dissolve
    allison "None of the rooms in {i}this place{/i} would be my first choice."
    scene w3_12912 with dissolve
    "Watching Elias shamelessly kiss the movie star's neck, I thought of Felicia and the similarities between the two."
    scene w3_12913 with dissolve
    elias "Quite so, a woman like you deserves a penthouse, not a cheap funhouse room."
    scene w3_12912 with dissolve
    "And it didn't just come down to the blonde hair either. Not only was Allison an artist in her own right, but her sex appeal..."
    scene w3_12911 with dissolve
    allison "Ah, but that's not going to stop you tonight, is it~"
    scene w3_12915 with dissolve
    "It was equal parts cudgel and a scalpel between the ribs."
    scene w3_12916 with dissolve
    allison "Four Saturdays were quite enough in this place."
    scene w3_12917 with dissolve
    elias "........."
    allison "......"
    scene w3_12918 with dissolve
    elias "...by the way, you wouldn't tell Kathy I called this place cheap, would you?"
    scene w3_12919 with dissolve
    "He was joking, but he looked at me expectantly."

    menu:
        "Your lips are sealed.(Elias Friendship +1)":
            $ Elias_Friendship += 1
            scene w3_12920 with dissolve
            mc "I'll take it to my grave, Mr. Ford."
            mc "Besides, this place is pretty gaudy."
            scene w3_12921 with dissolve
            elias "Haha, good!"
            elias "Thick as thieves, Bukowski!"
        "You can't make that promise.(Allison Interest +1)":

            $ Allison_Interest += 1
            scene w3_12920 with dissolve
            mc "Sorry, sir. I can't make that promise!"
            scene w3_12922 with dissolve
            elias "And why the hell not?!"
            scene w3_12923 with dissolve
            mc "She pays my check. If she asks me how you found the place, I--"
            scene w3_12922 with dissolve
            elias "You wouldn't!"
            scene w3_12924 with dissolve
            "........."
            "......"
            scene w3_12925 with dissolve
            elias "Bah, slave to the almighty dollar!"

    scene w3_12926 with dissolve
    elias "Ah, now that we're not around anyone, I suppose it's about time."
    mc "About time for what?"
    scene w3_12927 with dissolve
    elias "Why... I just landed in Tokyo. Gotta let Felicia know I'm safe."
    scene w3_12928 with dissolve
    mc "Ah--"
    scene w3_12929 with dissolve
    "Momentary panic set in, but if Felicia is expecting a call, there wasn't actually any risk."
    scene w3_12927 with dissolve
    "I could use this chance to talk to Allison or I could hang around Elias to try to pick up bits of his conversation with Felicia."
    jump w3ExSRStage2

label w3ExSRAllison:
    $ w3Stage2Time += 1
    $ Allison_Interest +=2
    $ w3ExAllisonPutInPlace = True
    $ w3ExSREmpty = True
    scene w3_12930 with fade
    "I, of course, elected to bother the stacked movie star that had half her tits out."
    scene w3_12931 with dissolve
    mc "So, uh... 'sup?"
    scene w3_12930 with dissolve
    "I am only a man."
    scene w3_12932 with dissolve
    allison "You couldn't be any more transparent if you tried, but don't get any fuckin' ideas. I'm here with Elias, that's that."
    scene w3_12933 with dissolve
    mc "Hey, I'm not stupid, besides... you're above my pay grade, eh?"
    allison "And don't you forget it."
    scene w3_12934 with dissolve
    mc "You have a high opinion of yourself, but that comes and goes, doesn't it?"
    scene w3_12935 with dissolve
    allison "Nope!! I'm always the brightest thing in the room, even if some people are blind to it."
    scene w3_12936 with dissolve
    mc "You've got to believe that, huh? You know you're the fourth Carnation I've met, but I think I've got it figured out."
    scene w3_12934 with dissolve
    mc "You all either do it out of desperation, greed, or for the thrill."
    scene w3_12935 with dissolve
    allison "No shit, hardly a revelation."
    scene w3_12934 with dissolve
    mc "My point is you're a little more common than you think."
    scene w3_12938 with dissolve
    "I had honestly come to chit-chat, but having her immediately shut me down kinda pissed me off."
    scene w3_12937 with dissolve
    mc "........."
    scene w3_12938 with dissolve
    mc "......"
    scene w3_12939 with dissolve
    allison "...what are you staring at?"
    scene w3_12940 with dissolve
    mc "You're all three. Desperate to be famous, greedy for success, and you {b}won.{/b} That takes a special kind of {b}slut.{/b}"
    scene w3_12941 with dissolve
    allison "Fuck you!"
    scene w3_12942 with dissolve
    mc "I'm not good enough, remember?"
    scene w3_12943 with dissolve
    "This time, Allison looked me up and down, {b}flustered.{/b}"
    scene w3_12944 with dissolve
    allison "Tsk! You're even more annoying than Darius, guess it's a job requirement. What happened to him?"
    scene w3_12945 with dissolve
    mc "Ran out with a girl to live happily ever after."
    scene w3_12946 with dissolve
    allison "Yeah, right..."
    mc "Eh. That's the official story..."
    scene w3_12947 with dissolve
    allison "How'd you get the job?"
    scene w3_12948 with dissolve
    "I thought about telling the truth, that it all came down to knowing a dude, but I wanted to press the advantage I felt I had gotten over her from our previous repartee."
    scene w3_12949 with dissolve
    mc "I'm good at what I do."
    scene w3_12947 with dissolve
    allison "And what do you {i}do?{/i}"
    scene w3_12949 with dissolve

    if toughness >=21:
        mc "Keep bitches like you hungry and in line."
    else:
        mc "Keep women like you hungry and in line."

    scene w3_12950 with dissolve
    "It was utter bullshit, and so out of character, but saying it with conviction gave me an unbelievable thrill."
    scene w3_12951 with dissolve
    "The movie star started to laugh, but faltered. The natural inclination would be that this 20-something-year-old is full of shit, but it was such an audacious thing to say, and my face didn't betray otherwise."
    scene w3_12952 with dissolve
    "What. If."
    "{i}She looked curious.{/i}"
    scene w3_12953 with dissolve
    mc "This place has taught me a lot."
    scene w3_12954 with dissolve
    "Now {i}that{/i} wasn't bullshit."
    scene w3_12955 with dissolve
    mc "How 'bout you...?"
    scene w3_12956 with dissolve
    allison "I suppose I could say the same..."
    scene w3_12957 with dissolve
    mc "Look at that. Seems we exist in the same stratosphere."
    scene w3_12958 with dissolve
    "She looked into my eyes and I felt like I could fuck the whole world. "
    scene w3_12959 with dissolve
    elias "You two look chummy."
    scene w3_12960 with dissolve
    elias "Thanks for keeping her warm for me."
    mc "Of course, Mr. Ford."
    scene w3_12961 with dissolve
    elias "Ha, now! Show me more of this beautiful place!"
    scene black with fade
    "Elias forged ahead, and we followed, with Allison throwing the occasional glance my way."
    jump w3ExSRStage2


label w3ExSRElias:
    $ w3Stage2Time += 1
    $ Elias_Friendship +=1
    $ w3ExSREmpty = True
    scene w3_12962 with fade
    "My sick curiosity got the better of me. The thought of Elias speaking with Felicia, {i}both in the same building{/i}, unbeknownst to each other..."
    "Fuck. {b}Me{/b}."
    "He called, it rang four or five times, and--"
    scene w3_12963 with pixellate
    fel "Oh, sweetie! I was just thinking about you! How was the plane ride?"
    scene w3_12964 with dissolve
    elias "I slept a bit too much. Not going to help the jet lag. What are you up to?"
    scene w3_12963 with dissolve
    fel "I'm reading that new best seller you told me about."
    scene w3_12964 with dissolve
    elias "It's not like you to take my recommendations on literature."
    scene w3_12966 with dissolve
    fel "I have from time to time..."
    scene w3_12965 with dissolve
    elias "I recall you saying my taste in reading was all just boring pompous self-help nonsense."
    scene w3_12966 with dissolve
    fel "It is, but maybe I become a bit more sentimental when we're six thousand miles apart. You know... one time, when you were in Monaco, I slept next to your old clothes."
    fel "That's how much I missed you."
    scene w3_12965 with dissolve
    elias "Who's there?"
    scene w3_12967 with dissolve
    fel "...why do you think someone's with me?"
    scene w3_12965 with dissolve
    elias "Because you're not {i}that{/i} doting when it's just us."
    scene w3_12968 with dissolve
    fel "I'll leave that to your imagination, hun. I'm glad you're back on the ground, safe and sound."
    fel "Even if you don't believe me, I really do miss you when you're gone."
    scene w3_12969 with dissolve
    elias "Yeah, me too... funny how capricious the mind can be. Listen, I've got to--"
    scene w3_12970 with dissolve
    fel "Call me when you finish your business tomorrow morning. I'll tell you what I thought about the book."
    fel "{i}Love you.{/i}"
    play sound "sound effects/phonemenu.wav"
    scene w3_12971 with dissolve
    war "I let you keep your phone because you said you wouldn't make any phone calls."
    scene w3_12972 with dissolve
    fel "First of all, you don't \"let\" me do anything. I do what I want."
    scene w3_12973 with dissolve
    fel "Second... I didn't call anyone. {i}Someone called me.{/i}"
    scene w3_12974 with dissolve
    fel "You want to tell me why, instead of mingling like the last two weeks, you have us sequestered by our lonesome? I wouldn't need my phone if I wasn't so fucking bored! You had me come in hours ago!"
    scene w3_12975 with dissolve
    war "......"
    scene w3_12976 with dissolve
    scene w3_12977 with instantdissolve
    fel "Wh-what--"
    play sound "sound effects/thud-floor.mp3"
    scene w3_12978 with vpunch
    fel "You son of a bitch! I--"
    scene w3_12979 with dissolve
    war "..."
    scene w3_12980 with dissolve
    fel "F-fine... I get it... no more phone... {b}Jesus.{/b} {size=-15}You think you're a big man...{/i}"
    scene w3_12981 with dissolve
    war "I'm glad you understand, {b}Meat.{/b}"
    scene w3_12982 with pixellate
    mc "So... how's your lovely wife?"
    elias "To be honest, I never really know what's going through her head, but that's the case with all women. Right, Bukowski?"
    elias "Knowing her, she's probably fucking some dumbass \"influencer\" or juiced up monkey."
    scene w3_12983 with dissolve
    mc "Oh... you have an... \"understanding\" relationship?"
    elias "I'm a practical man. Learned it from my parents."
    scene w3_12984 with dissolve
    elias "No need to let a flash of desire ruin a good thing, you know what I mean?"
    scene w3_12985 with dissolve
    elias "I mean, look at her..."
    scene w3_12986 with dissolve
    mc "Yeah... good point. It's a world of temptation and you've got free range."
    scene w3_12987 with dissolve
    elias "Haha, I knew you'd understand!"
    mc "...but you could be hypocritical about it. You wouldn't be the first philanderer with double standards."
    scene w3_12988 with dissolve
    elias "I will admit there was a time when I thought otherwise, but I learned a lot about possessiveness from the mother of my children."
    elias "There are simply some people in this world you can't control, and I respect Felicia enough to not attempt to put a one-sided collar on her."
    scene w3_12989 with dissolve
    "There was an odd glint of sadness marring Elias' otherwise distinguished countenance, one that he was quick to--"
    scene w3_12990 with dissolve
    elias "Now, we've got a lot more of this place to see! Let's go!"
    scene black with fade
    "So we continued, Elias particularly more handsy with his date, as if making a point."
    "All I thought of was my own parents' relationship, what was and what could've been."
    jump w3ExSRStage2



screen w3ExEH2:
    if w3EHIntroSeen == False:
        imagemap:
            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            imagebutton auto "gui/screens/imagebuttons/checklist_%s.png" xpos 0.06 action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExChecklist")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            idle "gui/screens/imagemaps/w3ExEH2Initial_idle.png"
            hover "gui/screens/imagemaps/w3ExEH2Initial_hover.png"
            ground "gui/screens/imagemaps/w3ExEH2Initial_ground.png"
            hotspot (888,370,700,700) action Jump("w3ExEH2Talk")
    else:
        imagemap:
            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            imagebutton auto "gui/screens/imagebuttons/checklist_%s.png" xpos 0.06 action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExChecklist")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            idle "gui/screens/imagemaps/w3ExEH2_empty.png"
            hover "gui/screens/imagemaps/w3ExEH2_empty.png"
            ground "gui/screens/imagemaps/w3ExEH2_empty.png"

label w3ExEHStage2:
    show black
    $ renpy.music.play("music/from-russia-with-love.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w3ExEH2 with pixellate


label w3ExEH2Talk:
    $ w3EHIntroSeen = True
    $ w3Stage2Time += 1
    scene w3_12991 with dissolve
    elias "I've heard a lot about these shows..."
    scene w3_12992 with dissolve
    "While showing Elias around, I decided to swing by the exhibition hall. He'd see it soon enough, God help him, but it was right there."
    scene w3_12993 with dissolve
    mc "...uh, did Mrs. Pulman tell you what her shows are like?"
    scene w3_12994 with dissolve
    elias "She's keeping me in suspense."
    scene w3_12993 with dissolve
    mc "Ah, well... they're something..."
    scene w3_12991 with dissolve
    elias "So this is where you were crowned..."
    scene w3_12995 with dissolve
    "The talent agent spoke like Carnation \"Queen\" was a prestigious title, looking toward the stage and imagining the lurid details."
    elias "I do love a woman who uses what she's got to get ahead, but {i}this{/i} takes the cake. Was it close, sweetheart?"
    allison "...was what close?"
    scene w3_12996 with dissolve
    elias "How handily did you beat the other two women?"
    scene w3_12997 with dissolve
    allison "I..."
    scene w3_12998 with dissolve
    allison "I won, didn't I?"
    scene w3_12999 with dissolve
    elias "That's right. You're a winner."
    scene w3_13000 with dissolve
    "Elias looked deep into Allison's eyes, face flushed with arousal."
    scene w3_12999 with dissolve
    elias "{b}Fuck me,{/b} you're beautiful."
    scene w3_13000 with dissolve
    "It was an uncomfortable moment with me playing third wheel, but also fascinating in a sense."
    scene w3_13001 with dissolve
    elias "Now that you're with me and my firm... the sky's the limit."
    scene w3_13002 with dissolve
    allison "I know, baby. I'm in good hands."
    scene w3_13003 with dissolve
    mct "(...what the fuck is he going to do when he sees his {b}wife{/b} up on that stage. Would the slimeball keep that lecherous smile?)"
    scene w3_13001 with dissolve
    elias "How did you beat those whores? Give me an example."
    scene w3_13004 with dissolve
    allison "I..."
    scene w3_13005 with dissolve
    "{i}She didn't want to say.{/i}"

    menu:
        "You're curious too. Encourage her.(Allison Interest -1)":
            $ Allison_Interest -= 1
            scene w3_13006 with dissolve
            mc "I'm actually curious too. I've only sat through half of one of these. How crazy does it get?"

            scene w3_13007 with dissolve
            if w3PromoShockFullSadism == True or w3KatSnare == True:
                "I'd seen one of the events during last year's week three, but a sick part of me was curious about what was in store for {i}my{/i} Carnations."
            else:
                "I'd seen one of the events during last year's week three, but I was admittedly anxious on behalf of {i}my{/i} Carnations."

            scene w3_13008 with dissolve
            allison "That..."
            scene w3_13009 with dissolve
            allison "One week was a treasure hunt."
            scene w3_13010 with dissolve
            elias "Haha, what?"
            scene w3_13011 with dissolve
            allison "We had to do all sorts of things, step-by-step..."
            scene w3_13012 with dissolve
            mc "Like what?"
            scene w3_13013 with dissolve
            "Again, {i}she didn't want to say.{/i}"
            scene w3_13014 with dissolve
            allison "Well..."
            scene w3_13015 with dissolve
            allison "For one clue, we had to use semen we personally \"extracted\" as a key to unlock a door."
            scene w3_13016 with dissolve
            elias "What in the world..."
            scene w3_13015 with dissolve
            allison "For another, we had to... euch... find a clue on one of the patrons' bodies. We didn't know who, either..."
            scene w3_13017 with dissolve
            mc "That doesn't sound so bad."
            scene w3_13015 with dissolve
            allison "After an hour of searching... it was..."
            scene w3_13018 with pixellate
            allison "*Ahem* Where you'd least want to find it..."
            elias "...and you found all the clues?"
            scene w3_13019 with pixellate
            allison "Yeah. I found all the clues..."
            scene w3_13020 with dissolve
            elias "Mmh, I can't wait..."
            scene w3_13021 with dissolve
        "You're here, jump in and give him details from {b}this{/b} exhibition.(Allison Interest +1)":


            $ Allison_Interest += 1
            scene w3_13006 with dissolve
            mc "The first week the Carnations had to figure out how to please me best."
            scene w3_13022 with dissolve
            "I decided to step in, if not to sidestep Allison's recollection, then to remind Elias that I was here as well."
            scene w3_13023 with dissolve
            elias "Oh, yeah...?"
            scene w3_13024 with dissolve
            mc "Yeah... one cradled me like a baby while she jacked me off, one danced, and another--"
            scene w3_13022 with dissolve
            "When I pictured what I did to Felicia, I stopped, a perverse feeling churning in my stomach."
            scene w3_13024 with dissolve
            mc "There's this blonde... a real sex kitten, eager and... {b}happy to be here.{/b} She got on her back and..."
            scene w3_13031 with pixellate
            mc "I face fucked every thought out of her head."
            elias "Ha! That sounds..."
            scene w3_13025 with pixellate
            elias "I wish I could've seen it!"
            mc "Well... there's more to come."
            scene w3_13026 with dissolve
            elias "Mmmh..."

    "Elias' enthusiasm for the lewd details told me one thing... if he doesn't suffer a stroke from utter humiliation, he'll fit right in around here..."

    scene w3_13027 with dissolve
    if w3DuoVickyVisit == True:
        kil "Oh... [mcf]... {i}hey.{/i} What are you doing here? Did Kathy send you to help me set up?"
        "Ian and I exchanged a silent glance. I had been worried about him since he found out about Grace blackmailing my mom, but here he was - looking {i}relatively{/i} normal."

    elif ianVickyTruth == True:
        kil "Oh, hey! What are you doing here? Did Kathy send you to help me set up?"
        "Ian and I exchanged a silent glance. I had been worried about him since he found out about Mom, but here he was - looking {i}relatively{/i} normal."
    else:
        mc "Oh, hey bro! What's up! What are you doing here? Did Kathy send you to help me set up?"
        "Ian and I exchanged a head nod. He seemed in good spirits."

    scene w3_13028 with dissolve
    mc "No, I'm showing..."
    scene w3_13029 with dissolve
    mc "This is Dr. Kohler's nephew, Killian Beaufort. Ian, this is Elias {b}Ford.{/b} I'm showing him around."
    scene w3_13030 with dissolve
    kil "Wait, Elias Fo--"
    "{i}Oh, fuck.{/i} The realization dawned on him; he quickly and thankfully understood."
    scene w3_13032 with dissolve
    kil "Huh... {b}wow.{/b}"
    "It was an expression of disbelief that the old woman would go this far."
    scene w3_13033 with dissolve
    elias "You look familiar..."
    scene w3_13034 with dissolve
    kil "I, uh... I do model photography sometimes. I've worked with your agency."
    scene w3_13035 with dissolve
    elias "Ah, then you probably know my wife!"
    scene w3_13034 with dissolve
    kil "Uh, yeah... we've... {b}met.{/b} Hard to forget a face and body like that."
    scene w3_13035 with dissolve
    elias "Small world. It's nice to meet you, Killian. I'm looking forward to meeting your uncle."
    scene w3_13036 with dissolve
    kil "Don't get your hopes up too high. He's pretty..."
    scene w3_13037 with dissolve
    elias "Don't stop. What were you going to say?"
    kil "You'll see. He doesn't take things too seriously."
    elias "That's hard to believe."
    scene w3_13038 with dissolve
    kil "Well, I've got to get back to work. Boxes of sex toys don't move themselves..."
    elias "Don't let us keep you. Let's go, Bukowski."

    if w3DuoVickyVisit == True:
        scene w3_13041 with dissolve
        kil "Hey, man. Can we talk later? I've got something I want to hypothetically pose to you..."
        scene w3_13040 with dissolve
        "Ian looked oddly serious."
        scene w3_13042 with dissolve
        mc "Of course, yeah... we'll find the time. What's up?"
        scene w3_13041 with dissolve
        kil "I'll tell you later. Come find me if you get a moment alone."
        scene w3_13042 with dissolve
        mc "Will do..."
        scene black with fade
        "It was just for a brief moment, but he looked... intensely pensive."
    else:
        scene w3_13039 with dissolve
        mc "See you around, dude."
        scene black with fade
        "..."

    jump w3ExEHStage2



screen w3ExPool2:
    if w3ExKristoffMet == False:
        imagemap:
            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            imagebutton auto "gui/screens/imagebuttons/checklist_%s.png" xpos 0.06 action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExChecklist")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            idle "gui/screens/imagemaps/w3ExPool2_idle.png"
            hover "gui/screens/imagemaps/w3ExPool2_hover.png"
            ground "gui/screens/imagemaps/w3ExPool2_ground.png"
            hotspot (731,357,750,700) action Jump("w3ExPoolFrank")
            hotspot (422,254,250,500) action Jump("w3ExPoolKristoff")
    else:
        imagemap:
            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            imagebutton auto "gui/screens/imagebuttons/checklist_%s.png" xpos 0.06 action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExChecklist")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            idle "gui/screens/imagemaps/w3ExPool2_empty.png"
            hover "gui/screens/imagemaps/w3ExPool2_empty.png"
            ground "gui/screens/imagemaps/w3ExPool2_empty.png"

label w3ExPoolStage2:
    show black
    $ renpy.music.play("music/too-cool.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w3ExPool2 with pixellate

label w3ExPoolFrank:
    if w3ExPoolFrankRepeat == False:
        $ w3ExPoolFrankRepeat = True
        play ambient "sound effects/swimming.wav"
        scene w3_13043 with fade
        elias "Why would you go to a brothel to exercise?"
        mc "Maybe he wants to limber up before he gets down and dirty?"
        elias "Ha! Right? Some pre-coitus swimming! Doesn't everyone?"
        stop ambient
    else:

        play ambient "sound effects/swimming.wav"
        $ randint = renpy.random.randint(1, 2)
        scene w3_13043 with fade
        if randint == 1:
            "We've got better things to do than watch a flabby old man go back and forth in a pool."
        elif randint == 2:
            mct "(Let's find something else to gawk at, huh?)"
        stop ambient

    jump w3ExPoolStage2

label w3ExPoolKristoff:
    $ w3ExKristoffMet = True
    $ w3Stage2Time += 1
    scene w3_13044 with fade
    mc "Ah, there he is. The man Frank wanted you to meet."
    elias "He looks familiar..."
    mc "Hoarfrost Risk Management."
    scene w3_13045 with dissolve
    elias "Jesus! {i}That{/i} Kristoff?"
    scene w3_13046 with dissolve
    mc "What's the matter?"
    elias "Oh, I don't know. You were a kid when he was front and center of all those congressional hearings during the war - and on top of that, he's got his cock out!"
    scene w3_13047 with dissolve
    "To my surprise, Elias physically recoiled at the prospect of meeting the former soldier of fortune."
    elias "*Sigh* I'll be honest. I... I don't do so great with his {i}type{/i}, Bukowski."
    scene w3_13048 with dissolve
    "Well, that was something. In a rare moment of weakness, Elias looked at me for support."

    menu:
        "Reassure Elias that you have his back.(Elias Interest +1)":
            $ Elias_Friendship +=1
            scene w3_13049 with dissolve
            mc "Lucky for you, you have me to run interference. It's what I'm here for."
            scene w3_13050 with dissolve
            elias "...you think I'm a pussy."
            scene w3_13051 with dissolve
            mc "No, and to be honest, I get it. I've never seen a six-foot-plus 70-year-old with abs. Like what the fuck, huh?"
            scene w3_13052 with dissolve
            elias "Pah! Yeah! Ah... Felicia says it's my three years of growing up at a military academy. At least it's not nuns..."
            elias "You'll lead?"
            scene w3_13053 with dissolve
            mc "Yep. I'll get you started, sir."
        "Pump him up with a little prodding.(Allison Interest +1)":


            $ Allison_Interest += 1
            scene w3_13054 with dissolve
            mc "You've got to be kidding me. Elias Ford is intimidated by an old man? {i}Really?{/i}"
            "I said it as a joke, with the goal of jump-starting his Type A personality up, but--"
            scene w3_13055 with dissolve
            elias "I-- ah... to be honest: {b}yes...?{/b}"
            mct "(Ah, shit... that backfired...)"
            scene w3_13056 with dissolve
            elias "I just find military types to be stuffy as shit. That's all."
            scene w3_13049 with dissolve
            mc "He's got a topless blonde in his arms. No danger of that. Think of your campaign, sir."
            mc "Go talk to him."
            scene w3_13050 with dissolve
            elias "...*sigh* alright, {b}introduce me.{/b}"

    scene black with fade
    "..."
    scene w3_13057 with fade
    "Before I could even get a word out, hell, before we had even begun walking in his direction, the military man extracted himself from leisure and stood tall; his cold, steely gaze utterly inscrutable."
    mc "This is Elias Ford, Mister--"
    scene w3_13058 with dissolve
    jiji "Kristoff Jameson."
    scene w3_13059 with dissolve
    elias "It's very nice to meet you. Frank told me--"
    scene w3_13060 with dissolve
    "With just a handshake, the words were robbed straight from Elias' mouth."
    scene w3_13061 with dissolve
    jiji "For the last two years, your predecessor has been putting the lives of the brave peace officers of this city at risk. You have {i}our{/i} support."
    jiji "If you need any suggestions on how best to retool the precinct armories when it comes time to allocate the city's budget, I'd be happy to educate you on the cutting edge of self-defense and law enforcement technology."
    scene w3_13062 with dissolve
    elias "Yes... I'd appreciate that."
    scene w3_13063 with dissolve
    "The two, with very little words, had come to a simple understanding."
    scene w3_13064 with dissolve
    frank "Oh, good. Seems you've got things set up, Jiji. Wanna hit the Sauna?"
    scene w3_13065 with dissolve
    jiji "Care to join us, Elias?"
    elias "No thanks... I'm... making the rounds."
    jiji "Very well. Welcome to the club."
    scene w3_13066 with dissolve
    elias "Thanks."
    scene w3_13067 with dissolve
    "........."
    "......"
    scene w3_13068 with dissolve
    elias "...how greedy can you get, Bukowski?"
    scene w3_13069 with dissolve
    mc "Is that rhetorical?"
    scene w3_13068 with dissolve
    elias "...on top of military contracts, Hoarfrost supplies armaments to police departments across this country. Morehead Hills is just a drop in a bucket."
    scene w3_13069 with dissolve
    mc "Didn't the city spend millions to modernize the police a few years ago?"
    scene w3_13070 with dissolve
    elias "It did, and I guess Goldie thought whatever he spent must've sufficed. Lucky for me, but a reminder of how tides can change."
    scene w3_13071 with dissolve
    mc "Huh..."
    scene black with fade
    "This was above my pay grade."
    jump w3ExPoolStage2



screen w3ExHallwayStage2:

    if w3Stage2Time == 0:

        imagemap:

            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            imagebutton auto "gui/screens/imagebuttons/checklist_%s.png" xpos 0.06 action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExChecklist")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            idle "gui/screens/imagemaps/w3ExHallway2S1_idle.png"
            hover "gui/screens/imagemaps/w3ExHallway2S1_hover.png"
            ground "gui/screens/imagemaps/w3ExHallway2S1_ground.png"
            hotspot (1050,379,750,700) action Jump("w3ExHallway2Jacob")
            hotspot (35,374,750,700) action Jump("w3ExHallway2KatWarren")

    elif w3Stage2Time == 1:
        imagemap:

            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            imagebutton auto "gui/screens/imagebuttons/checklist_%s.png" xpos 0.06 action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExChecklist")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            idle "gui/screens/imagemaps/w3ExHallway2S2_idle.png"
            hover "gui/screens/imagemaps/w3ExHallway2S2_hover.png"
            ground "gui/screens/imagemaps/w3ExHallway2S2_ground.png"
            hotspot (1050,379,250,500) action Jump("w3ExHallway2Jacob")

            if w3ExMR2Repeat == True and w3ExHallwayLucySeen == False:
                hotspot (1302,454,250,500) action Jump("w3ExHallway2Lucy")


    elif w3Stage2Time == 2:
        imagemap:

            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            imagebutton auto "gui/screens/imagebuttons/checklist_%s.png" xpos 0.06 action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExChecklist")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            idle "gui/screens/imagemaps/w3ExHallway2S3_idle.png"
            hover "gui/screens/imagemaps/w3ExHallway2S3_hover.png"
            ground "gui/screens/imagemaps/w3ExHallway2S3_ground.png"
            hotspot (1050,379,250,500) action Jump("w3ExHallway2Jacob")
            hotspot (488,435,250,500) action Jump("w3ExHallway2Jim")

            if w3ExMR2Repeat == True and w3ExHallwayLucySeen == False:
                hotspot (1302,454,250,500) action Jump("w3ExHallway2Lucy")

    elif w3Stage2Time == 3:

        if w3ExMR2Repeat == True and w3ExHallwayLucySeen == False:

            imagemap:

                imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
                imagebutton auto "gui/screens/imagebuttons/checklist_%s.png" xpos 0.06 action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExChecklist")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
                idle "gui/screens/imagemaps/w3ExHallway2S4Lucy_idle.png"
                hover "gui/screens/imagemaps/w3ExHallway2S4Lucy_hover.png"
                ground "gui/screens/imagemaps/w3ExHallway2S4Lucy_ground.png"
                hotspot (1050,379,250,500) action Jump("w3ExHallway2Jacob")
                hotspot (1503,418,750,700) action Jump("w3ExHallway2Isaac")
                hotspot (603,447,250,500) action Jump("w3ExHallway2WheresLucy")

        else:
            imagemap:
                imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
                imagebutton auto "gui/screens/imagebuttons/checklist_%s.png" xpos 0.06 action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExChecklist")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
                idle "gui/screens/imagemaps/w3ExHallway2S4_idle.png"
                hover "gui/screens/imagemaps/w3ExHallway2S4_hover.png"
                ground "gui/screens/imagemaps/w3ExHallway2S4_ground.png"
                hotspot (1050,379,250,500) action Jump("w3ExHallway2Jacob")
                hotspot (1503,418,750,700) action Jump("w3ExHallway2Isaac")

    elif w3Stage2Time == 4:
        imagemap:

            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            imagebutton auto "gui/screens/imagebuttons/checklist_%s.png" xpos 0.06 action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExChecklist")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            idle "gui/screens/imagemaps/w3ExHallway2S5_idle.png"
            hover "gui/screens/imagemaps/w3ExHallway2S5_hover.png"
            ground "gui/screens/imagemaps/w3ExHallway2S5_ground.png"
            hotspot (299,381,750,700) action Jump("w3ExHallway2Mihir")

            if w3ExMR2Repeat == True and w3ExHallwayLucySeen == False:
                hotspot (1302,454,250,500) action Jump("w3ExHallway2Lucy")
    else:
        imagemap:

            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage2")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            imagebutton auto "gui/screens/imagebuttons/checklist_%s.png" xpos 0.06 action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExChecklist")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            idle "gui/screens/imagemaps/w3ExHallway2S6_idle.png"
            hover "gui/screens/imagemaps/w3ExHallway2S6_hover.png"
            ground "gui/screens/imagemaps/w3ExHallway2S6_ground.png"
            hotspot (640,399,600,700) action Jump("w3ExHallway2Chuck")




label w3ExHallwayStage2:
    show black
    $ renpy.music.play("music/cello-suite-No-1-G-Major-Prelude.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w3ExHallwayStage2 with pixellate


label w3ExHallway2Jacob:

    if w3Stage2Time == 0:
        scene w3_13072 with dissolve
        mct "(I wonder how much he gets paid for just standing around...)"
    elif w3Stage2Time == 1:
        scene w3_13073 with dissolve
        "Jacob waved hello as we passed by."
    elif w3Stage2Time == 2:
        scene w3_13074 with dissolve
        mct "Is it me or is Jacob checking out Serena's ass...?)"
        "Who could blame him?"
    elif w3Stage2Time == 3:
        if w3ExMR2Repeat == True and w3ExHallwayLucySeen == False:
            scene w3_13075 with dissolve
            jacob "...?"
        else:
            scene w3_13076 with dissolve
            mct "(...he's still in that same position.)"

    jump w3ExHallwayStage2

label w3ExHallway2KatWarren:

    if w3ExHallway2KatWarrenRepeat == False:
        $ w3ExHallway2KatWarrenRepeat = True
        scene w3_13077 with dissolve
        kat "...keep a close eye on that slut. Don't let her out of your sight, and keep the monitors off."
        scene w3_13078 with dissolve
        war "You think I'm that stupid?"
        scene w3_13079 with dissolve
        kat "I--"
        scene w3_13080 with dissolve
        war "Don't answer that."
    else:
        scene w3_13077 with dissolve
        mct "(Wonder what that's about?)"

    jump w3ExHallwayStage2


label w3ExHallway2Lucy:
    $ w3ExHallwayLucySeen = True
    scene w3_13081 with dissolve
    "...looks like Lucy ran to Mommy after Shelby's scolding."
    scene w3_12892 with pixellate
    hana "Last year, Mr. Family Values choked Harper until she passed out."
    scene w3_13082 with dissolve
    mct "(Ah, shit...)"
    scene w3_13083 with dissolve
    "What a trooper..."
    jump w3ExHallwayStage2

label w3ExHallway2WheresLucy:
    if w3ExHallway2WheresLucyRepeat == False:
        $ w3ExHallway2WheresLucyRepeat = True
        scene w3_13084 with dissolve
        mct "(I spy with my little eye...)"
        "A prostitute avoiding her problems."
        mct "(Very smooth, girl...)"
    else:
        scene w3_13084 with dissolve
        mct "(I'll just leave her to that.)"

    jump w3ExHallwayStage2

label w3ExHallway2Jim:
    scene w3_13085 with dissolve
    mct "(Looks like they're going somewhere more comfortable.)"
    jump w3ExHallwayStage2


label w3ExHallway2Isaac:
    if w3ExMR2Repeat == True and w3ExHallwayLucySeen == False:
        scene w3_13086 with dissolve
        "He has no idea the whore of his dreams is just around the corner."
        mct "(I'll deal with that later... {i}or not.{/i})"
    else:
        scene w3_13086 with dissolve
        "Looks like Isaac is annoying Eric. He's more patient than I thought."

    jump w3ExHallwayStage2


label w3ExHallway2Mihir:

    if w3ExHallway2MihirRepeat == False:
        $ w3ExHallway2MihirRepeat = True
        scene w3_13087 with dissolve
        "It's a good thing Jacob left his post, what with Mihir's hand nearly up Emma's ass."
    else:
        scene w3_13087 with dissolve
        mct "(...then again, doubt he minds. The job is the job.)"
    jump w3ExHallwayStage2

label w3ExHallway2Chuck:

    scene w3_13088 with fade
    elias "There {b}he{/b} is..."
    "At long last, we found the club's head honcho himself, having caught his chess partner at the door."
    mc "Who, Dr. Kohler?"
    elias "No, Abel Van Doren..."
    "Elias, at odds with the environment, wore a look that appeared dangerously close to childlike wonder and adoration."
    "If I didn't know any better..."
    mc "...you a fan?"
    elias "Introduce me."
    scene black with fade
    "...I'd say he, the man with a movie star in his arms, was star-struck."
    scene w3_13089 with dissolve
    chuck "There he is! The man of the evening!"
    mc "Elias Ford, meet--"
    scene w3_13090 with dissolve
    chuck "We all know who each other are, lad!"
    scene w3_13091 with dissolve
    elias "Thank you for the invitation to paradise, Charles."
    scene w3_13092 with dissolve
    elias "The moment I saw you two... you and Dr. Van Doren..."
    scene w3_13093 with dissolve
    elias "This. Must. Be. The. Place."
    scene w3_13092 with dissolve
    elias "I've been excited to meet you both."
    scene w3_13094 with dissolve
    abel "I feel similarly."
    elias "...you do?"
    abel "Yes, I've been excited to meet you."
    scene w3_13095 with dissolve
    abel "When I was a young boy, I knew your grandfather. He taught me what excellence and poise look like."
    abel "This country simply wouldn't be what it is without your family's legacy, and he carried it remarkably well. You share his blood."
    scene w3_13096 with dissolve
    chuck "Who cares about the past! Elias has made a name for himself through the sweat of his own brow!"
    chuck "I've got so many questions."
    scene w3_13097 with dissolve
    elias "You do?!"
    scene w3_13098 with dissolve
    chuck "What does Elize Sky's pubic hair look like? She shave?"
    scene w3_13099 with dissolve
    elias "And why would I know that?!"
    scene w3_13098 with dissolve
    chuck "Huh? Isn't she part of your agency?"
    scene w3_13099 with dissolve
    elias "Yeah, but--"
    scene w3_13100 with dissolve
    chuck "I'm going to borrow Elias, lad. You don't mind?"
    scene w3_13101 with dissolve
    elias "Where are we going?"
    scene w3_13102 with dissolve
    chuck "To the sauna. I'd like to have a talk with you, alone, mano a mano."
    scene w3_13103 with dissolve
    elias "About what?"
    scene w3_13104 with dissolve
    chuck "Hmm... I don't know? What makes a man? What are your plans for the future? Just bullshit!"
    elias "I'd love that..."
    chuck "Good..."
    scene w3_13105 with dissolve
    chuck "I'll return him in one piece, [mcf]. In the mean time, why don't you go grab a drink or a girl?"
    chuck "I won't tell Kathy you're slacking off if you don't tell her I stole your charge. Deal?"
    scene w3_13106 with dissolve
    mc "I'll come find you later, Mr. Ford."
    elias "You better, Bukowski! I'll miss you!"
    stop music fadeout 10.0
    scene w3_13107 with dissolve
    "........."
    "......"
    scene w3_13108 with dissolve
    allison "*Sigh* I guess I'll get a drink."
    play ambient "sound effects/walk-wood.mp3"
    scene w3_13109 with dissolve
    sophia "That leaves just us."
    stop ambient
    scene w3_13110 with dissolve
    abel "How are you, [mcf]?"
    scene w3_13111 with dissolve
    mc "Ready for a night of... {i}this{/i}, I guess."
    scene w3_13112 with dissolve
    abel "I ran into Dr. Kohler's nephew on the way in. He was quite cross and gave me an earful about our meeting the other day."
    scene w3_13113 with dissolve
    mc "...he did?"
    scene w3_13112 with dissolve
    abel "I was shocked. No one ever talks to me that way. You have a good friend."
    scene w3_13111 with dissolve
    mc "Yeah... he's alright. We don't need to mention it again, not after Sophia dropped by to apologize this morning."
    play music "music/doll-dancing.ogg"
    scene w3_13114 with dissolve
    sophia "...I, what? No, I didn't."
    scene w3_13115 with dissolve
    mc "Huh?! Yeah, you did! You--"
    scene w3_13116 with dissolve
    sophia "I would certainly remember! I..."
    scene w3_13117 with dissolve
    sophia "...I, I think...?"
    scene w3_13118 with dissolve
    "For a brief moment, the leather-clad blonde looked lost and... {i}scared?{/i}"
    mc "Why would I lie about that? Is this another one of your bad jokes?"
    scene w3_13119 with dissolve
    sophia "I... I..."
    scene w3_13120 with dissolve
    play sound "sound effects/finger-snap.wav"
    scene w3_13121 with instantdissolve
    abel "Come, Sophia. We've got some business to attend to."
    scene w3_13122 with dissolve
    sophia "Y-yes, sir..."
    scene w3_13123 with dissolve
    mct "(...{b}ummmmmm{/b}, what the fuck?!)"

    if w3SophApologyPush == True:
        "Was she screwing with me? Acting like she didn't go face down ass up to apologize this morning?"
    else:
        "Was she screwing with me? Acting like she wasn't in the middle of my damn living room?"

    scene w3_13124 with dissolve
    mct "(What is with these goddamn weirdos?!)"
    "She didn't look like she was joking, but I remember plain as--"
    scene w3_13125 with dissolve
    mc "*sigh* Well, whatever."
    "I had freed myself of Elias for the time being. Question is..."
    scene black with fade
    "What should I do with myself?"
    jump w3ExHallwayStage3

    label w3ExVIPStage2:
    scene black with fade
    if w3ExWIPStage2Repeat == False:
        $ w3ExWIPStage2Repeat = True
        "You seem to hear Mrs. Pulman's voice inside your head."
        kat "Remember: VIP room at 8 PM."
        "In the meantime, I should take Elias elsewhere."
    else:
        mct "(Seriously, I don't want to be the one to ruin the old woman's fun...)"
    jump w3ExNavMenuStage2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
