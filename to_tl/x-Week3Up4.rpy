label june17StartContinue:

    play music "music/i-knew-a-guy.ogg"
    scene w3_5393 with circlewipe
    mc "...this is his dad's company number, right?"
    scene w3_5394 with dissolve
    mc "It's better than nothing. Did Darius ever talk about his dad?"
    mc "Do you have any idea what kind of man he is?"
    scene w3_5395 with dissolve

    if history_veronica == "I took Veronica out and played wingman for her, hoping some brief fun would be a nice reprieve from her troubles.":
        $ w3VeronicaWingman = True

    if feliciaFlag == True and minaCheat == True and Mina_BiCurious >= 3 and minaBreakOff == False:
        $ w3MinaWantsToWatch = True

    kil "All I know is he's a prick and that Darius did something I wish I could do."
    scene w3_5394 with dissolve
    mc "Get an ocean between him and his family?"
    scene w3_5395 with dissolve
    kil "Exactly, and he went all the way across the Pacific and ended up {b}here{/b} of all places."
    scene w3_5394 with dissolve
    mc "One hell of a trajectory if you think about it..."
    scene w3_5396 with dissolve
    kil "No kidding, he worked for his own money, too. Trekking through state after state..."
    scene w3_5397 with dissolve
    mc "Sounds like some begrudging respect."
    scene w3_5398 with dissolve
    kil "...it's {i}kinda{/i} cool, I guess."
    scene w3_5396 with dissolve
    kil "So, what are you going to do?"
    scene w3_5397 with dissolve
    mc "I don't see the direct approach panning out."
    scene w3_5398 with dissolve
    kil "Just lie. Confirm a dentist's appointment or something."
    scene w3_5397 with dissolve
    mc "I don't think the dentist will cut it either..."
    scene w3_5399 with dissolve
    rose "I'm not sure what you boys are talking about, but..."
    scene w3_5400 with dissolve
    rose "...say you need to speak to Mr. Lee, regarding his son."
    rose "Keep it vague, but make it sound private and important. If they hesitate to put you through, ask him to call you back."
    scene w3_5401 with dissolve
    mc "...and then what?"
    scene w3_5402 with dissolve
    rose "A parent getting a vague message like that? {b}Oh{/b}, he'll call you back."
    scene w3_5403 with dissolve
    mc "......"
    kil "..."
    scene w3_5404 with dissolve
    mck "...not a bad idea."
    scene w3_5405 with dissolve
    kil "The advice of a parent, eh?"
    rose "Um... {i}something{/i} like that. Should I go get some morning air?"
    scene w3_5406 with dissolve
    "Rosalind, as usual, was smart like that. Her offer would otherwise be appreciated, but..."
    scene w3_5407 with dissolve
    mc "There's no need for that."
    kil "You're not going to call?"
    scene w3_5408 with dissolve
    "Despite the voice in my head telling me it wasn't wise, {i}yes.{/i} I would call. It was that simple."
    scene w3_5409 with dissolve
    "There was only one problem, chronologically speaking..."
    mc "It's too early for that. It's like 2 a.m. in Hawaii."
    scene w3_5410 with dissolve
    "......"
    "..."
    stop music
    play sound "sound effects/surprise.wav"
    scene w3_5411 with vpunch
    kil "Son of a {b}BITCH!{/b}"
    scene w3_5412 with dissolve
    mc "Yeah, dude, you could've slept in. Like, what the fuck, it's 8:30 a.m."
    scene w3_5411 with dissolve
    kil "Ack, I got too excited! I thought we'd call..."
    scene w3_5412 with dissolve
    mc "That's two days in a row you got here bumfuck early after a night of drinking. Don't get me wrong, I appreciate it, but how are you not {i}wired?{/i}"
    scene w3_5413 with dissolve
    kil "...benefit of youth? Uh... the hair of the dog?"
    mc "...wait you're not boozed up right now, are you? I hope you didn't pre-game a phone call."
    scene w3_5414 with dissolve
    kil "Is it pre-gaming if you never stopped?"
    "........."
    "......"
    "..."
    scene w3_5415 with dissolve
    kil "I'm kidding! I just drank enough to delay the hangover."
    mc "...bro, go upstairs and sleep. We'll call after you get up."
    scene w3_5416 with dissolve

    if w3VeronicaSex == True:
        kil "How are you not feeling it? You seemed pretty hosed when I caught you with--"
        scene w3_5417 with dissolve
        mc "{size=-10}Shut up!{/size}"
        scene w3_5418 with dissolve
        "{i}It's probably best if Rosalind doesn't know I porked Veronica on my off time...{/i}"
        kil "Ah... right, right, right, right--"
    else:
        kil "What are you, my mom?"
        scene w3_5420 with dissolve
        mc "I'm not reading you a bedtime story if that's what you're angling for."
        scene w3_5421 with dissolve
        "......"
        kil "...not even a--"

    play sound "sound effects/door-bell.wav"
    scene w3_5419 with dissolve
    "*Ding, dong!*"
    kil "Eh, who the hell is...?"
    scene black with fade
    "..."
    play sound "sound effects/door-open.wav"
    hana "Whaddup, boys!"
    play music "music/crinoline-dreams.ogg"
    scene w3_5422 with wipeleft
    kil "Actually, I think I feel my hangover coming on..."
    play sound "sound effects/door-close.wav"
    scene w3_5423 with dissolve
    mc "What are you doing here?"
    scene w3_5424 with dissolve
    hana "I brought donuts."
    scene w3_5425 with dissolve
    kil "Donuts?! You're looking VERY pretty today, Hana--"

    if hanaGF == True:
        scene w3_5426 with dissolve
        mc "Mmhhm..."
        "The casual show of affection was a slight shock to my system, albeit not an unlikable one."
        scene w3_5427 with dissolve
        hana "Good morning, boyfriend."
        hana "How you doin' today?"
        "Hana flashed me a sordid smile, brimming with the knowledge of what we last got up to when she was here."
        scene w3_5428 with dissolve
        mc "The morning's getting brighter."
        kil "{size=-10}You corny mother fucker...{/size}"
        scene w3_5429 with dissolve
        kil "Yoink!"
        kil "I am GLAD to see you, too."

    elif w3HanaDP >= 4:
        scene w3_5427 with dissolve
        hana "How you doin' today?"
        "Hana flashed me a sordid smile, brimming with the knowledge of what we last got up to when she was here."
        scene w3_5428 with dissolve
        mc "The morning's getting brighter."
        kil "{size=-10}You corny mother fucker...{/size}"
        scene w3_5429 with dissolve
        kil "Yoink!"
        kil "I am GLAD to see you, too."
    else:

        scene w3_5430 with dissolve
        hana "How you two doin' today?"
        scene w3_5431 with dissolve
        mc "{b}Good.{/b} We're both good, right?"
        scene w3_5432 with dissolve
        kil "Yoink!"
        kil "{b}Really{/b} good."

    scene w3_5433 with dissolve
    hana "The red velvet one is mine. Don't touch it."
    kil "You got it, boss!"
    scene w3_5490 with dissolve
    hana "Hey, Rose!"
    rose "Ummm, hello..."
    scene w3_5491 with dissolve
    "......"
    "..."
    "She looked like she wanted to say more, but..."
    scene w3_5434 with dissolve
    hana "Hmmm..."
    scene w3_5435 with dissolve
    hana "...your hair looks a little different."
    mc "No, it doesn't. It always looks like this."
    scene w3_5436 with dissolve
    "......"

    if w3HanaDP >= 4:
        scene w3_5437 with dissolve
        hana "...nice try. You're not fooling me, egghead."
        scene w3_5438 with dissolve
        mc "...do you guys have a group chat or something?!"
        scene w3_5439 with dissolve
        hana "I {i}like{/i} it."
        scene w3_5440 with dissolve
        mc "Yeah, right, I just woke up..."
        scene w3_5441 with dissolve
        hana "Mmmhm, and {i}you're cute.{/i}"
        scene w3_5445 with dissolve
        mc "Seriously, what's the occasion, beautiful?"
    else:
        scene w3_5442 with dissolve
        hana "...really?"
        scene w3_5443 with dissolve
        mc "Nah, I got a trim."
        scene w3_5444 with dissolve
        hana "Fuck off, I knew it!"
        scene w3_5445 with dissolve
        mc "Seriously, what's up? Why are you here?"

    scene w3_5446 with dissolve
    hana "August filled me in on some stuff."
    scene w3_5447 with dissolve
    mc "Some stuff...? Do you mean...?"
    scene w3_5446 with dissolve
    hana "{b}Yeah{/b}, and I'm glad to see you're not banged up."
    scene w3_5447 with dissolve
    mc "That explains the donuts. How much did he tell you?"
    scene w3_5448 with dissolve
    "......"
    "..."
    scene w3_5449 with dissolve
    hana "Enough to know I don't like it."
    scene w3_5450 with dissolve
    mc "I don't either, but it is what it is."
    hana "Shut up. {i}\"It is what it is\"{/i}... I hate that macho crap, along with other phrases that mean absolutely nothing."
    scene w3_5451 with dissolve
    mc "I mean, it's getting handled. What else can you do?"

    if hanaGF == True:
        hana "Bring donuts? Check-in on my man? Look Rosalind in the eyes and feel like crap?"
    elif w3HanaDP >= 4:
        hana "Bring donuts? Check-in on you? Look Rosalind in the eyes and feel like crap?"
    else:
        hana "Bring donuts? Look Rosalind in the eyes and feel like crap?"

    scene w3_5452 with dissolve
    mc "Aaaah, you're checking up on her too, huh?"
    scene w3_5453 with dissolve
    hana "It's not like I have anything to say to her... just poking my head in because I feel like I'm floundering."
    scene w3_5452 with dissolve
    mc "It's something we're both going to have to get used to."
    scene w3_5454 with dissolve
    hana "Get used to?! Do you plan on getting into more punch-outs with thugs?"
    scene w3_5455 with dissolve
    mc "Hey... it wasn't a punch out... it was more like--"
    scene w3_5456 with dissolve
    kil "Huh? Blueberry cream cheese pie? Oh, fuck yeah!"
    scene w3_5457 with dissolve
    hana "...he's easily won over."
    scene w3_5458 with dissolve
    mc "Or you just came packing the good shit."
    scene w3_5459 with dissolve
    "......"
    scene w3_5460 with dissolve
    hana "...fill me in on the details, please."
    scene w3_5461 with fade

    if w3RCKnockout == True or w3RCDoubleAssBeat == True or w3RCSuckerPunched == True or w3RCThreatened == True:
        "So, despite my pride, I quickly went over the \"rough\" details of our hallway encounter."
    elif w3RCTussled == True:
        "So, I went into detail about our little tussle in the hallway."
    else:
        "So, I did, explaining the details of our hallway encounter."

    scene w3_5462 with dissolve
    hana "........."
    mc "......"
    scene w3_5463 with dissolve
    hana "...uuugh, don't be so nonchalant about it!"
    mc "It was better for me to be there than not be, right?"
    hana "That's... ah... I fucking hate that's an {i}agreeable{/i} way of looking at it."

    if w3HanaDP >= 4:
        scene w3_5464 with dissolve
        hana "*Sigh* I'm glad Ian was there, at least."
        scene w3_5465 with dissolve
        mc "He had my back."
        scene w3_5466 with dissolve
        hana "Thanks, shitlord."
        scene w3_5467 with dissolve
        kil "Eh, hmmm? For what?"
        scene w3_5466 with dissolve
        hana "For being cool yesterday."
        scene w3_5468 with dissolve
        kil "You're going to have to be more specific. I'm always cool."
        scene w3_5469 with dissolve
        hana "Just go back to stuffing your face."
    else:

        scene w3_5464 with dissolve
        hana "It's good you two were together."
        scene w3_5465 with dissolve
        mc "Yeeeeah, we had each other's back."

    scene w3_5470 with dissolve
    hana "So, what have you two been up to? It's kinda early, isn't it?"
    scene w3_5471 with dissolve
    mc "Playing detective."
    scene w3_5464 with dissolve
    hana "...do I even want to know?"
    scene w3_5472 with dissolve
    "That {i}was{/i} a good question."
    scene w3_5473 with dissolve
    mc "Club stuff. Probably nothing, but I'll tell you about it if it becomes important."
    mc "It's complicated, and it's--"
    scene w3_5474 with dissolve
    rose "Donuts?"
    hana "Oh, uh... you don't have to wait on us, Rose."
    scene w3_5475 with dissolve
    mc "Thank you."
    hana "Aaaah, y-yeahh... seriously, {b}thank you.{/b}"
    rose "Heh, it's not that big of a deal. I just put it on a plate."
    scene w3_5476 with dissolve
    rose "...but my pleasure."
    hana "......"
    scene w3_5477 with dissolve
    mc "...you're less smooth than I give you credit for."
    scene w3_5478 with dissolve
    hana "Shut up. Where were we?"
    scene w3_5479 with dissolve
    mc "I was saying now's not really the time to explain what I've been doing."

    if w3HanaDP >= 4:
        scene w3_5480 with dissolve
        hana "...let's make that time, okay?"
        hana "You listen to my crap, I listen to yours."
        scene w3_5481 with dissolve
        mc "I'd like that."
        scene w3_5480 with dissolve
        hana "{b}Good{/b}, 'cause we're in this together."
    else:
        scene w3_5482 with dissolve
        hana "...alright. But do let me know about it if it's important, 'cause we're in this together."

    scene w3_5483 with dissolve
    hana "You, me, and... Jesus Christ help me, even Ian."
    kil "Why do I keep hearing my name?!"
    scene w3_5484 with dissolve
    mc "Since when have you come around on this prick?"
    scene w3_5485 with dissolve
    kil "Seriously? Are you guys talking about me?"
    scene w3_5486 with dissolve
    hana "Well, none of us are perfect, and I think I realized that there are fewer of {i}us{/i} than them -- those being all the old shit stains..."
    scene w3_5485 with dissolve
    kil "Shit stain? Okay, now I'm definitely sure you're talkin' about me!"
    scene w3_5487 with dissolve
    hana "Pffh--!"
    mc "She thinks you're a shit stain."
    hana "Pffh, haha-!"
    scene w3_5488 with dissolve
    kil "I'm just eating a donut! Leave me alone!"
    scene w3_5489 with dissolve
    rose "Hehe--"
    "It was a weird morning..."
    rose "You three are funny."
    "An odd mish-mash of people."
    scene w3_5492 with cmet
    hana "Hey, can I get Mina's number...?"
    kil "Eh?! Why do you want--"
    "Me, Ian, Hana, and Rose..."
    scene w3_5493 with circlewipe
    hana "[mcf]'s not making you sleep on the couch, is he? 'Cause as his {i}boss{/i} I can order him to let you have the bed."
    "Rosalind didn't seem too out of sorts with this array."
    kil "She's going to pull that card a lot, isn't she?"
    "Hell, I even caught her smiling a couple of times."
    scene w3_5494 with fade
    mc "Get some sleep, dude. We'll make the call after you get up."
    kil "I'm fine, I don't need any--"
    scene w3_5495 with wipeleft
    hana "You should probably get a fold-out or something with how many house guests you have..."
    mc "Heh, yeah, no kidding..."
    "It was a weird, {b}interesting{/b} morning."
    stop music fadeout 3.0
    scene black with w25
    "And the day was about to get more so."
    mc "Looks like I'm needed. You can stay here if you want."
    play sound "sound effects/city-night.wav"
    scene w3_5496 with blinds
    hana "Eh, I'll tag along. I'm supposed to check in with my dad sometime today anyway."
    play music "music/horrible.ogg"
    stop sound fadeout 3.0
    scene w3_5497 with fade
    mc "...you seem to be seeing a lot more of your dad lately. How's that going?"
    hana "Annoyingly. He acts like me accepting the club is the same thing as me accepting him."
    scene w3_5498 with dissolve
    mc "Yet, here you are."
    hana "Maybe it's easier just to say yes?"
    scene w3_5499 with dissolve
    mc "Do you two have a lot to talk about?"
    scene w3_5500 with dissolve
    hana "I don't need to say much; he'll happily talk your ear off if you let him. You only need to throw in an \"uh huh\" occasionally."
    scene w3_5499 with dissolve
    mc "That sounds about right."
    scene w3_5501 with dissolve
    hana "Yeah, you probably know him well enough by now - and Dr. Kohler, you go waaaay back with him, right?"
    scene w3_5499 with dissolve
    mc "In a sense."
    scene w3_5500 with dissolve
    hana "You guys meet one-on-one like this often?"
    scene w3_5502 with dissolve
    mc "Actually, come to think of it... very rarely."
    mc "Growing up, I mostly saw him at school or family events with Ian. And more recently... the only time I can think of is when he dropped by my apartment a couple weeks ago."
    scene w3_5503 with dissolve
    hana "So, this is unusual?"
    scene w3_5504 with dissolve
    mc "......"
    scene w3_5502 with dissolve
    mc "...I 'spose so."
    scene w3_5505 with dissolve
    hana "Any idea what he wants?"
    mc "He wasn't really forthcoming on the phone."
    hana "It could be about Rosalind."
    mc "She's really on your mind."
    scene w3_5506 with dissolve
    hana "Me? She's in your apartment, [mcf]."
    scene w3_5507 with dissolve
    mc "...well, I can't deny seeing her being menaced in person hit a bit differently than the idea of it, but nothing's really changed this week from the last."
    scene w3_5508 with dissolve
    "......"
    scene w3_5509 with dissolve
    hana "...is my dad going to fuck that guy up?"
    scene w3_5510 with dissolve

    if w3RosalindViolentSolution == True:
        mc "He's got to be good for something, right?"
    else:
        mc "The loan shark will wish he was. Dr. Chuck is handling it."

    scene w3_5509 with dissolve
    hana "You're {b}cold{/b}, [mcf]. That doesn't scare you?"
    scene w3_5510 with dissolve
    mc "Honestly, in this particular case? {b}No{/}."
    scene w3_5511 with dissolve
    hana "...it doesn't bother me one bit, either."
    scene w3_5512 with dissolve
    "Hana smiled, but I could see through it. Underneath it was worry."
    "A familiar worry of my own."
    "She wasn't bothered by being indirectly complicit in whatever might happen to Oliver."
    "Instead, she was bothered by the fact that she wasn't bothered."

    if w3HanaDP >= 4:
        scene w3_5513 with dissolve
        hana "...?"
        scene w3_5514 with dissolve
        hana "Mmmh..."
        "........."
        scene w3_5515 with dissolve
        "......"
        "..."
        scene w3_5516 with dissolve
        mc "Just as sweet as ever."
        scene w3_5517 with dissolve
        hana "Lame ass. What would you do if my father saw?"
        scene w3_5516 with dissolve
        mc "Do {b}you{/b} care if he did?"
        scene w3_5517 with dissolve
        hana "Of course not, but I'm asking if you do."

        if hanaGF == True:
            scene w3_5518 with dissolve
            mc "Are we hiding our relationship?"
            hana "...hell no."
            mc "Then I'd do the same thing."
            scene w3_5519 with dissolve
            hana "Really?"
        else:
            scene w3_5518 with dissolve
            mc "He's got no say in what I do to his daughter."
            hana "{i}To{/i} me, huh...?"
            scene w3_5519 with dissolve
            hana "You really wouldn't be nervous?"

        scene w3_5520 with dissolve
        mc "{i}Really{/i}."
        scene w3_5519 with dissolve
        hana "I'll only believe you if you prove it."
        scene w3_5521 with dissolve
        mc "Oh, and should I track down your dad just so I can smooch you?"
        hana "...let's go see if Dr. Chuck is at the bar."
        stop music fadeout 3.0
        scene black with fade
        mc "No rush."
    else:

        scene w3_5522 with dissolve
        mc "Good, you shouldn't be, 'cause the guy's a major prick."
        mc "Think Warren, but with a British accent."
        scene w3_5523 with dissolve
        hana "Oh, {i}God.{/i}"
        mc "Yeah, now you get the picture."
        scene w3_5512 with dissolve
        "......"
        "..."
        scene w3_5511 with dissolve
        hana "Let's go find the old men?"
        stop music fadeout 3.0
        scene black with fade
        mc "Sounds like a plan."

    play music "music/as-i-figure.ogg"
    scene w3_5524 with blinds
    aug "Kids!"
    aug "I wasn't expecting you for another couple of hours, my dear."
    scene w3_5525 with dissolve
    hana "You have [mcf] to thank for that. He got a call from Dr. Chuck and I tagged along."
    aug "Ah... you two are together quite {i}early.{/i}"
    hana "Early to rise, or whatever."
    scene w3_5526 with dissolve
    mc "Good morning, August. Good morning, Mr. Otto."
    scene w3_5527 with dissolve
    otto "He remembers my name!"
    mc "You left an impression, sir."
    scene w3_5528 with dissolve
    otto "He's funny, too."
    aug "He's not joking. That's just his normal face."
    scene w3_5529 with dissolve
    mc "Good morning to you as well, Dalia."
    dal "Good morning, sir."
    scene w3_5530 with dissolve
    otto "Everyone's a fucking sir, huh? You've surrounded yourself with tight asses in your retirement, Augie."
    aug "Ha! The kid can call you whatever he likes."
    scene w3_5531 with dissolve
    hana "Are we butting in on something?"
    scene w3_5532 with dissolve
    otto "Hardly. Your father was just filling me in on some mundane happenings."
    scene w3_5533 with dissolve
    aug "Is that what you call me taking my cholesterol seriously?"
    scene w3_5532 with dissolve
    otto "Luckily, your pretty face has improved the conversation."
    scene w3_5534 with dissolve
    hana "Aha, {size=-10}yeeeeah...{/size}."
    scene w3_5535 with dissolve
    aug "Oh! That was barely a grimace. My daughter's getting better at masking her displeasure over being complimented."
    scene w3_5705 with pixellate
    mct "(No shit, you animals...)"
    aug "Was there something else to report, Dalia? The envelope was nice and fat."
    scene w3_5536 with pixellate
    dal "It's Kimber."
    scene w3_5537 with dissolve
    aug "Don't tell me she's \"sick\" again, or it's coming out of your end, you hear me?"
    scene w3_5536 with dissolve
    dal "...she's requesting tomorrow night off."
    scene w3_5538 with dissolve
    aug "{i}And?{/i} You've had the run of things for a while. You don't need to bring these things to my attention. Just tell her--"
    scene w3_5539 with dissolve
    aug "{b}Actually{/b}, never mind. Hana, dear..."
    hana "...?"
    scene w3_5540 with dissolve
    aug "I want to get your take on this."
    scene w3_5541 with dissolve
    hana "Give her the night off."
    scene w3_5542 with dissolve
    aug "Listen to the circumstances first."
    scene w3_5541 with dissolve
    hana "Doesn't matter. This isn't the kind of job where you should force somebody to work if they're not feeling it."
    scene w3_5543 with dissolve
    otto "Ha! She's got a lot to learn."
    scene w3_5542 with dissolve
    aug "...humor me, alright?"
    scene w3_5544 with dissolve
    hana "..."
    scene w3_5545 with dissolve
    aug "Consider this: Kimber is a bit of an excuse-monger."
    scene w3_5546 with dissolve
    aug "She is habitually late to appointments, and for the last two months, she has requested multiple nights off."
    aug "Now, {b}Kimber{/b} has three bookings tomorrow, set up in advance. If she flakes, rather than canceling, other girls will have to unfairly pick up the load."
    scene w3_5545 with dissolve
    aug "So, let me ask you, should we abide no good lazy whores like Kimber?"
    scene w3_5548 with dissolve
    hana "That's rich, considering we all sit lazily on our asses and profit off them."
    scene w3_5549 with dissolve
    otto "Don't discount the work it takes to keep junkies, debtors, and deadbeats from themselves."
    scene w3_5548 with dissolve
    hana "It sounds like this job isn't for her. Shouldn't you just let her go?"
    scene w3_5550 with dissolve
    aug "Kimber doesn't have better options, I'm afraid. She's lucky this outfit is as low-volume, high-yield as it is."
    scene w3_5548 with dissolve
    hana "So, she doesn't have a choice?"
    scene w3_5551 with dissolve
    otto "She has {i}choices{/i}, but owes me quite a bit of money. This is her best one, even if she doesn't act like it."
    scene w3_5552 with dissolve
    "......"
    scene w3_5545 with dissolve
    aug "...I'm leaving this up to you, truly. Whatever you decide, we'll do."
    scene w3_5547 with dissolve
    hana "...and what's the catch?"
    scene w3_5545 with dissolve
    aug "You'll have to manage the consequences."
    scene w3_5547 with dissolve
    hana "And those are...?"
    scene w3_5546 with dissolve
    aug "Find replacements for her bookings, smooth over any disappointment from our customers, and compensate those who don't want another girl."
    aug "In short, you'll cover what the club loses personally."
    scene w3_5547 with dissolve
    hana "Why are you putting this on me?"
    scene w3_5545 with dissolve
    aug "You know why."
    scene w3_5553 with dissolve
    "Hana clearly didn't appreciate being put on the spot, and her expression told the tale of a woman caught between what she felt was obviously correct and the unpalatable reality of the business."
    "......"
    "..."
    scene w3_5554 with dissolve
    hana "Just give her the night off. Clearly, something's off. Can't you just ask her what's up?"
    scene w3_5555 with dissolve
    aug "Be my guest and do just that. Go see what a filthy, deplorable {b}bitch{/b} she is, listen to her excuses, and give her a whole evening to shoot up."
    scene w3_5556 with dissolve
    hana "Filthy? She's a per--"
    aug "She's a whore, Hana."
    hana "...yeah, like {b}Mom?{/b}"
    scene w3_5557 with dissolve
    aug "Your mother was a {b}star{/b}."
    hana "Tchk! {b}Bullshit!{/b} You got rid of her when she became inconvenient."
    aug "We're not getting into this now."
    scene w3_5558 with dissolve
    hana "Is it {b}TOO{/b} much to ask for some respect and compassion for the women {i}we{/i} bleed dry?"
    scene w3_5559 with dissolve
    aug "There are women here who are worthy of respect and others whose only value is how much you can work them, and you've got to learn that distinction if you want to profit."
    scene w3_5560 with dissolve
    hana "......"
    scene w3_5561 with dissolve
    hana "...that's fair."
    scene w3_5562 with dissolve
    aug "Oh? You don't think I'm being harsh?"
    scene w3_5561 with dissolve
    hana "No, I {b}should{/b} get a taste of the reality around here. Teachable moment, right?"
    scene w3_5563 with dissolve
    aug "My girl's smart."
    hana "Your girl, huh...?"
    scene w3_5564 with dissolve
    hana "...just be open to the possibility that it's a management issue."
    scene w3_5565 with dissolve
    aug "I've been doing this a long time, sweetheart."
    hana "There are other ways to skin a cat..."
    scene w3_5566 with dissolve
    otto "Aptly put!"
    scene w3_5567 with dissolve
    aug "Perhaps..."
    scene w3_5568 with dissolve
    aug "You can go, Dalia. Make sure you get Hana a list of available girls and their schedules."
    dal "Yes, sir."
    scene w3_5569 with dissolve
    "...I didn't envy Hana having to run things, but the mix of anger and frustration on her face made me wish there was something I could do."
    hide screen textbox2 with dissolve

    if w3HanaDP >= 4:
        "Perhaps it would be a pointless gesture, but..."
        hide screen textbox2 with dissolve
        menu:
            "Prove it. (w3HanaClubKiss = True)"(chg=["hana_up2", "august_up"]):
                $ Hana_Affection +=2
                $ August_Friendship += 1
                $ w3HanaClubKiss = True
                jump w3HanaSuckSuckSuck
            "...now's probably not the time, right?"(chg=["hana_down", "hana_anger_up"]):

                $ Hana_Affection -=1
                $ Hana_Anger +=1
                scene w3_5590 with dissolve
                "........."
                "......"
                "..."
                scene w3_5591 with dissolve
                "The moment of opportunity passed, having lived and died inside my skull. Changing my mind now would have just been awkwardly timed."
                scene w3_5592 with dissolve
                aug "...so, are we still on for dinner later?"
                scene w3_5593 with dissolve
                "......"
                hana "...yeah."
                scene w3_5594 with dissolve
                aug "Let's go to my office. I want to show you a new watch that I won in a poker game."
                aug "You might want it."
                scene w3_5595 with dissolve
                otto "Do you have booze stashed in there?"
                aug "It'd be more challenging to find a room in this place that doesn't."
                scene w3_5596 with dissolve
                "......"
                "..."
                "The room quickly cleared out."
                scene w3_5579 with dissolve
                hana "*Sigh* I'm really tempted to let all three bookings go unfilled."
                scene w3_5580 with dissolve
                "It was funny how short of a time it took from when we entered, for Hana to have an emotional tussle, and then for us to be all alone again."
                scene w3_5597 with dissolve
                mc "That wouldn't be smart."
                scene w3_5580 with dissolve
                "Maybe August's quick exit was a rare modicum of tact."
                scene w3_5598 with dissolve
                hana "I know, so I won't, but mother fucker actually views the girls here as dirt. Lucky for me, I didn't come out of some other guy's nut sack, eh?!"
                scene w3_5599 with dissolve
                "......"
                "..."
                scene w3_5598 with dissolve
                hana "I'm going to be a good stooge and make sure I see everything clearly. Anything less is fucking fake, and I won't be delusional."
                scene w3_5600 with dissolve
                mc "You know what I hate the most about this place?"
                hana "What?"
                mc "Fucking finding people. Like goddamn."
                scene w3_5601 with dissolve
                hana "Ha, yeah! Let's go find that belt-buckle asshole."
                scene black with fade
                $ history_hana = "Hana is taking a more proactive role in club activities, alongside obvious consternation."
                $ unread_hana = True
                play sound "sound effects/notification.wav"
                show bioupdate with dissolve
                mc "...I think I'm just going to call him."
                "......"
                "..."
                jump w3FindChuck
    else:
        $ Hana_Anger +=1
        scene w3_5592 with dissolve
        aug "...so, are we still on for dinner?"
        scene w3_5593 with dissolve
        "......"
        hana "...yeah."
        scene w3_5594 with dissolve
        aug "Let's go to my office. I want to show you a new watch that I won in a poker game."
        aug "You might want it."
        scene w3_5595 with dissolve
        otto "Do you have booze stashed in there?"
        aug "It'd be more challenging to find a room in this place that doesn't."
        scene w3_5596 with dissolve
        "......"
        "..."
        "The room quickly cleared out."
        scene w3_5579 with dissolve
        hana "*Sigh* I'm really tempted to let all three bookings go unfilled."
        scene w3_5580 with dissolve
        "It was funny how short of a time it took for us to enter, for Hana to have an emotional tussle, and then for us to be all alone again."
        scene w3_5597 with dissolve
        mc "That wouldn't be smart."
        scene w3_5580 with dissolve
        "Maybe August's quick exit was a rare modicum of tact."
        scene w3_5598 with dissolve
        hana "I know, so I'm not, but mother fucker actually views the girls here as dirt. Lucky for me, I didn't come out of some other guy's nut sack, eh?!"
        scene w3_5599 with dissolve
        "......"
        "..."
        scene w3_5598 with dissolve
        hana "I'm going to be a good stooge and make sure I see everything clearly. Anything less is fucking fake, and I won't be delusional."
        scene w3_5600 with dissolve
        mc "You know what I hate the most about this place?"
        hana "What?"
        mc "Fucking finding people. Like goddamn."
        scene w3_5601 with dissolve
        hana "Ha, yeah! Let's go find that belt-buckle asshole."
        scene black with fade
        $ history_hana = "Hana is taking a more proactive role in club activities, alongside obvious consternation."
        $ unread_hana = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve
        mc "...I think I'm just going to call him."
        "......"
        "..."
        jump w3FindChuck

label w3HanaSuckSuckSuck:

    if _in_replay:
        play music "music/as-i-figure.ogg"
        show transitionhana03 with cmet
        show screen textbox2 with dissolve
        "Goth GF?"
        hide screen textbox2 with dissolve

        menu:
            "Yay.":
                $ hanaGF = True
            "Nay.":
                pass

        show screen textbox2 with dissolve

    scene w3_5570 with dissolve
    show screen textbox2 with dissolve
    mc "Hey..."
    hana "...?"
    scene hanabar_kiss_a with dissolve
    show hanabar_kiss with dissolve
    "...but maybe a kiss could be a sign of solidarity."
    hana "Mmmhhh..."
    "Like she said earlier, we're in this together."
    "I'm sure August and Otto are looking at us right now, but that wasn't important."
    "What was important, what was real right now, was the feeling of electricity on our lips and how soft the world momentarily seemed."
    "She felt it too, as she pulled me into a more showy display, and my taste buds memorized the odd mixture of donuts and chapstick. "
    "............"
    "........."
    "......"
    scene w3_5572 with dissolve
    mc "...does that prove it?"
    scene w3_5571 with dissolve
    "Her eyes said everything she didn't, putting me down the barrel of a smoldering look that compelled me to lurch forward and continue the game."
    scene w3_5572 with dissolve
    mc "Welcome back to Earth."
    scene w3_5573 with dissolve
    "That was an urge I resisted, of course."
    hana "Pffh, you fuckin' idiot."
    scene w3_5574 with dissolve
    aug "...are we still on for dinner later?"
    scene w3_5575 with dissolve
    "......"
    hana "...yeah."
    scene w3_5576 with dissolve
    aug "Let's go to my office. I want to show you a new watch that I won in a poker game."
    aug "You might want it."
    scene w3_5577 with dissolve
    otto "Do you have booze stashed in there?"
    aug "It'd be more challenging to find a room in this place that doesn't."
    scene w3_5578 with dissolve
    "......"
    "..."
    "The room quickly cleared out."
    scene w3_5579 with dissolve
    hana "...I should be used to it."
    scene w3_5580 with dissolve
    "It was funny how short of a time it took for us to enter, for Hana to have an emotional tussle, and then for us to be all alone again."
    scene w3_5579 with dissolve
    hana "Mother fucker actually views the girls here as dirt. Lucky for me, I didn't come out of some other guy's nut sack, eh?"
    scene w3_5580 with dissolve
    "Maybe August's quick exit was a rare modicum of tact."
    scene w3_5581 with dissolve
    hana "That kiss, though...!"
    hana "Pffh, that kiss was...!"
    scene w3_5582 with dissolve
    hana "Mmmh, hmm, hmmmm..."

    if w3HanaCutieCall == True:
        scene w3_5583 with dissolve
        show screen textbox2 with dissolve
        hana "Remember what I said yesterday morning on the phone?"
        scene w3_5584 with dissolve
        mc "Yesterday morning... uh..."
        scene w3_5582 with dissolve
        "{i}Oh.{/i}"
        "{b}Yeah.{/b}"
        "{i}I remember.{/i}"
        scene w3_5583 with dissolve
        hana "Anytime, anywhere, big guy..."
        scene w3_5584 with dissolve
        mc "Wasn't that just for the phone se--"
        scene w3_5583 with dissolve
        hana "It was a {b}promise{/b}, and you won't make me a liar, will you?"
        scene w3_5582 with dissolve
        "........."
        "......"
        scene w3_5585 with dissolve
        mc "...no, we can't have that, can we?"
    else:
        scene w3_5583 with dissolve
        hana "You know, I promised myself I would do something the next time I saw you. No matter the circumstance."
        scene w3_5585 with dissolve
        mc "...and what's that?"
        scene w3_5583 with dissolve
        hana "You didn't finish in my mouth the other night."
        scene w3_5584 with dissolve
        mc "...I didn't?"
        scene w3_5583 with dissolve
        hana "No, and I was quite disappointed by that."
        hana "Don't get me wrong, Sunday was wonderful, but you stopped dicking down my face too soon."
        hana "I meeeean, you barely scuffed my makeup, [mcf], even after I asked you {i}nicely{/i} to {b}really{/b} let me have it."
        scene w3_5585 with dissolve
        mc "I'm very, {i}very{/i} sorry about that."
        scene w3_5583 with dissolve
        hana "How about you make it up to me then?"

    scene w3_5586 with dissolve
    mc "W-wait, we can't just do it in the middle of the bar..."
    hana "Why not, afraid of getting caught with your hand in the cookie jar? Where did all your boldness go?"
    scene w3_5587 with dissolve
    mc "Goddamn it, that must have been some-- just... people walking in aside, don't forget that there are cameras..."
    scene w3_5588 with dissolve
    hana "Not over there."
    mc "Are you sure...? Like, {i}sure{/i}, {b}sure?{/b}"
    scene w3_5589 with dissolve
    hana "Sure enough for you to cram your fat cock down my throat until I'm on the verge of passing out."
    mc "...so about 50/50, then?"
    hana "Ha! Come on!"
    scene black with fade
    hana "Let me prove something to you this time."

    scene w3_5602 with fade
    mc "...and what's that?"
    hana "That I can suck your cock just as enthusiastically as one of the whores that shriveled windbag looks down on."
    scene w3_5603 with dissolve
    "...{i}God bless daddy issues{/i}."
    hana "Now, let's pry a certain something out of your pants, hmmm?"
    scene w3_5604 with dissolve
    hana "There it is!"
    "Without much fuss, Hana freed my better half and ogled it through lust-lidded eyes."
    scene w3_5605 with dissolve
    hana "I've looked forward to this..."
    mc "You're... uh, really into oral, huh?"
    hana "Thanks to this bad boy... I think I might develop a taste for it..."
    scene w3_5606 with dissolve
    hana "Hehe... mmmmhh.... just picturing fighting this {b}monster{/b} drives me crazy. Maybe it's the challenge of it?"

    if hanaGF == True:
        hana "Taking everything your man has, struggling with it, being beaten down by it..."
    else:
        hana "Taking everything your lover has, struggling with it, being beaten down by it..."

    scene w3_5607 with dissolve
    hana "It gives me a special kind of itch, [mcf]. I want to overcome it, and look all the worse for wear for it."
    "As I leered down at Hana's lewd display, my flaccid cock draped over her delicate features, and listening to her lewd words..."
    scene w3_5608 with dissolve
    hana "{b}That's{/b} the reaction I was looking for."
    "{b}I grew hard{/b}."
    scene w3_5609 with dissolve
    hana "FYI, if you don't use this thing to fuck me up, {b}I will{/b}."
    scene w3_5610 with dissolve
    mc "You don't think you're biting off more than you can chew? If I wanted..."
    play sound "sound effects/slap1.wav"
    scene w3_5611 with vpunch
    mc "I could fucking kill you with this thing."
    scene w3_5612 with dissolve
    hana "{b}Goddamn it...{/b}"
    "At the present, neither of us cared about where we were, and I could only hope Hana's estimation of the security system's blind spot was correctly assessed. Because if not..."
    scene w3_5613 with dissolve
    hana "H-haaa...!"
    scene w3_5614 with dissolve
    "There was about to be video evidence of me battering the boss' daughter stupid with cock."
    scene w3_5615 with dissolve
    hana "Spit in my mouth."
    scene w3_5616 with dissolve
    "Hana presented me with the instrument of my demise, a yawning chasm of scorching heat and soft promises, and I didn't hesitate."
    mc "Ah--"
    play sound "sound effects/spit2.wav"
    scene w3_5617 with dissolve
    "Shppeew!"
    "No hesitation."
    scene w3_5618 with dissolve
    mc "Hot damn..."
    "I gave the goth girl exactly what she asked for, high on the dichotomy that the woman who inspired me to kiss her out of tenderness was also a filthy bitch capable of playing my base desires like a fiddle."
    hide screen textbox2 with dissolve
    scene w3_5619 with dissolve
    "There was a brief window, a calmness before the storm, where our eyes met and a feeling of clarity washed over me."
    mct "(I'd sell out the whole fucking world for this blowjob.)"
    scene w3_5620 with dissolve

    if hanaGF == True:
        "Thankfully, that wasn't the toll my lovely girlfriend asked."
    else:
        "Thankfully, that wasn't the toll this devil asked of me."

    "No, all the teasing..."
    scene w3_5621 with dissolve
    "And kissing..."
    "And tentative expeditions down my shaft..."
    stop music fadeout 3.0
    scene w3_5622 with dissolve
    "...were in pursuit of one singular payment to be tendered down her throat at a later time."
    mc "Hana..."
    play music "music/take-the-lead.ogg"
    scene hanabar_bj1_a with dissolve
    "It started ordinarily enough, short and shallow motions, with Hana hollowing out her cheeks and filling in the empty remaining space with dick."
    scene w3_5623 with dissolve
    "But no sooner did her lips glide down my shaft, tight as a bowstring, soon retreating to hold my glans hostage between two pillowy prisons."
    "......"
    "...and there she held it, looking up at me with amber eyes of cock-sucking promise, making sure I was in rigid anticipation of the battle to come."
    "Once satisfied that I existed nowhere else but between her lips..."
    play ambient "sound effects/fel3.wav"
    scene hanabar_bj1_a with dissolve
    show hanabar_bj1 with dissolve
    "...she slid back down my shaft and began the blowjob in earnest."
    "*Chwwup-!*"
    "Every time she took me in, she worked wonders."
    mc "Mmmhh, haa..."
    "The tip of her tongue caught itself in my urethral opening, in just the right way, for just a fraction of a second--"
    mc "--Ga, aahhh!"
    "For that infinitesimal window in time, her wiry tip penetrated me, probing me with a whisk-like motion before..."
    mc "G-gahh, goddamn it... who..."
    "...roughly digging itself out to follow my frenulum down to the root."
    play ambient "sound effects/fel4.wav"
    $ renpy.music.set_volume(.2, 3, channel = "music")
    mc "Who the FUCK taught you that--"
    "*{b}Kwhhup, fwwhhup~{/b}*"
    "In contrast to her pin-prick flourishes, the soft borders of her mouth were divine, and I was -as if I had any choice- content to let the witchy woman guide things."
    "*Chwwip, kwwhhuuuup, wwhhhhupp-!*"
    play ambient "sound effects/kissing2.mp3"
    "...and Hana was content in making a show of it, from the very offset peppering in exaggerated noises that cajoled me into desiring to {i}go deeper{/i} down her suck hole."
    $ renpy.music.set_volume(1, 3, channel = "music")
    "In mere moments, what she desired and what I {i}felt{/i} blended together under a singular unifying banner."
    "*Slurrh, hhhuuur-!*"
    mc "Haaat...!"
    "What's more, every bob was more refined in motion than the last as she grew familiar with the finer points of my shape."
    "*Sluurh, hhhuhuhh-!"
    mc "Fuckk me, that feels so--!"
    stop ambient
    scene hanabar_bj2_a with dissolve
    show hanabar_bj2 with dissolve
    mc "G, a-ah...!"
    "Seeing my reaction, she promptly switched modes to a more protracted assault on my glans."
    mc "Hnnnggg...!"
    "She focused solely on my tip."
    "Bathing it, showering it, {i}learning{/i} it."
    "Her tongue subdued me. That little point, so small, {i}connected us{/i}."
    "It forced me to solely focus on Hana and her ministrations, each flick of her tongue a devotion that fell somewhere between worship and ritual sacrifice."
    mc "Eeeugh... f-fucking--"
    "An ant-like crawling feeling marched all the way to my thighs, fire spreading before my mind was..."
    scene w3_5624 with dissolve
    hana "You really want to know where I picked this up, don't you?"
    scene w3_5625 with dissolve
    "...mercifully distracted by a simple question."
    mc "Not really, I was just running my--"
    play ambient "sound effects/fel3.wav"
    scene hanabar_bj1_a with dissolve
    show hanabar_bj1 with dissolve
    "*Cwhup, ffwwhhhup!*"
    mc "W-waaahh..."
    "My glans, so overwrought with her teasing, {i}melted{/i}."
    "That itchy feeling all but ceased, blotted out by the sudden confines of Hana's clinging throat."
    "*Chwhhup, hhwwwhupp-!*"
    mc "Ah, that's right... suck it... hnnnggg..."
    "And I did the only thing I could do, offering banal encouragement, as if my words had any bearing on Hana's single-minded mission to suck me dry."
    hana "Mmh, mmh...!"
    mc "Suck my fucking dick! A-ah...!"
    hana "Mmmhh, hhhhmmm...!"
    "Her retort was simple yet effective, the thrumming of her throat played in harmony with my own dumb words to further pleasurable ends."
    mc "A-ah--"
    stop ambient
    scene w3_5625 with dissolve
    "And then it stopped and another form of torture took its place."
    "A lonely, cold, longing-filled feeling of absence inflicted on me with a brightly devilish smile."
    scene w3_5624 with dissolve
    hana "I got some pointers from Harper."
    scene w3_5625 with dissolve
    mc "...you're kidding. You didn't actually..."

    if hanaGF == True:
        scene w3_5624 with dissolve
        hana "It's just... I wanted to go the extra mile for my boyfriend."
        scene w3_5625 with dissolve
        mc "...this is more than a mile, girlfriend."
        scene w3_5624 with dissolve
        hana "Oh, come on... your dick's not THAT big..."
        scene w3_5625 with dissolve
        mc "You know what I--"
    else:
        scene w3_5624 with dissolve
        hana "The result speaks for itself, right?"
        scene w3_5625 with dissolve
        "Actually, it left no room for doubt."
        mc "I love a woman who does her homework--"

    play ambient "sound effects/fel5.wav"
    scene hanabar_bj3_a with dissolve
    show hanabar_bj3 with dissolve
    mc "--{b}ha!{/b}"
    "This time, it was for real."
    "*Ghwwhuk-!*"
    "Maybe it was the location, maybe it was redirecting her anger, maybe she genuinely liked the idea of me pouring baby batter down her throat..."
    "*Gwwhhk, hhhhhkk!*"
    "Whatever it may be, there was no more trickery, no more finesse, no more teasing. Hana just launched herself into a proper, earnest, sweat-of-your-brow cock sucking."
    mc "Oh, fuck, Hana..."
    "So I let her know exactly how pleased I was at this turn in direction."
    mct "(Gah! She...)"
    "*Shlhuuk, hhwhhuuk, wshhhuhuk-*"
    mct "(...she looked so FUCKING lewd right now.)"
    "...and she knew it."
    "I wanted so very very badly to destroy her."
    mc "Euuuuughh...!"
    "I wanted to ravage her throat until she was a teary, babbly mess."
    hana "*Cwhup, fwhhhuuup~*"
    "She knew that too."
    "She knew it all."
    "Her technique wasn't perfect."
    hana "*Shhuck, hgffhhhuuk-!*"
    "After all, as enthusiastic as she was, she was a novice."
    mc "Bh, aahhh..."
    "Rather than a smooth trajectory, teeth clumsily grazed flesh and the head of my cock clacked against the back of her throat."
    mc "Ah, Hana..."
    "...but her fervor in playing my cum dump more than made up for it. {i}It felt so {b}FUCKING{/b} good.{/i}"
    $ renpy.music.set_volume(.2, 2, channel = "music")
    mc "H-hana, babe... ah-ahh..."
    "So, so, so {i}good{/i} that my own whorish moans escaped my lips."
    "Hana's message was clear, delivered to me from her throat to my dick."

    if hanaGF == True:
        "{i}I'm yours and don't you forget it.{/i}"
    else:
        "{i}Don't you forget this, loser.{/i}"

    "*GHhhk, hhhhk!*"
    "*Ghh, hhhk, ghhhhhk!*"
    "*Ghh, hhhk, hhjjjjjhhk-!*"
    $ renpy.music.set_volume(1, 0, channel = "music")
    stop ambient
    scene hanabar_bj4_a with dissolve
    show hanabar_bj4 with dissolve
    hana "Ahh, hhaaa.. fuck... {b}holy shit...{/b}"
    "Hana peered up at me, dick drunk and delirious, about to lose it."
    mc "Hana..."
    hana "Your turn, [mcf]. {b}Fuck me up{/b}... a-ah..."
    "She knew what to say to land a critical hit on my base instincts."
    hana "{b}God, I want you!{/b}"

    if hanaGF == True:
        "A look of mania that defied all decency flooded my girlfriend's expression, before..."
    else:
        "A look of mania that defied all decency flooded the goth girl's expression, before..."

    scene w3_5626 with dissolve
    "......"
    scene w3_5627 with dissolve
    hana "Mmmh, hhhhmm...!"
    scene w3_5628 with dissolve
    "..."
    hana "Ha, hahaaa...!"
    scene w3_5629 with dissolve
    "..."
    play sound "sound effects/thud-floor.mp3"
    scene w3_5630 with hpunch
    mc "Ha...!"
    hana "Fuck me up..."
    scene hanabar_bj5_a with dissolve
    show hanabar_bj5 with dissolve
    "The woman in my arms became fever in the flesh."
    hana "Mmmh, mmhhhh...!"
    "Her limbs hooked possessively around me, robbed me of all purchase, and pulled me unflinchingly into the scorching heat of her body."
    mct "(Fuck her up...?)"
    "There she used her mouth and tongue and the contour of her figure to sear her claim of me into my body."
    "{i}Fuck her up?{i}"
    mc "Ghh.. ahhh..."
    "...and the air she drew into her lungs and passed back into me immolated my feeble self-control."
    hana "Mmmh, mmmhhhh..."
    scene w3_5631 with dissolve
    "{b}Fuck her up.{/b}"
    mc "......"
    hana "..."
    scene w3_5632 with dissolve
    "A shared look pushed things along and Hana reached for her blouse..."
    scene w3_5633 with fade
    "..."
    scene w3_5634 with dissolve
    mc "Get on your knees..."
    scene w3_5635 with dissolve
    "Her gaze never left me, nor did the desire in her eyes falter one bit."
    scene w3_5665 with dissolve
    hana "Aaaahhhhh..."
    "Placing her hands behind her back, {b}she wholeheartedly offered me her throat.{/b}"
    scene w3_5666 with dissolve
    mc "Mmmh..."
    "As I peered down at Hana's soon-to-be-cock-stuffed face, kneeling on the brothel floor, a perverse glee gripped me."
    scene w3_5665 with dissolve
    "{i}This was going to be fun.{/i}."

    menu:
        "Ask Hana to name her price. [mod_chat]":
            $ w3HanaBrothelRP = True
            "It's probably not the best time for some roleplay, but..."
            scene w3_5667 with dissolve
            mc "How much?"
            "My query came out as a whisper, as I was cognizant of where I stood, but too horny to let the stupid question go unasked."
            scene w3_5668 with dissolve
            hana "...huh?"
            scene w3_5669 with dissolve
            "I could only hope Hana shared some of my black humor about where our paychecks came from because the thought of the brothel owner's daughter playing a whore..."
            mc "I mean, think about where you are and what you're doing. How much do you want?"
            "...{i}it was too hot{/i}."
            scene w3_5668 with dissolve
            hana "...you joking?"
            scene w3_5669 with dissolve
            mc "I'm serious. Name a price and I'll pay it."
            scene w3_5670 with dissolve
            hana "That--"
            scene w3_5671 with dissolve
            hana "...ha! You fucking asshole!"
            scene w3_5672 with dissolve
            mc "...no go, huh?"
            scene w3_5671 with dissolve
            hana "Well... I {b}did{/b} say I should get a taste of the reality around here."
            scene w3_5672 with dissolve
            "It was amazing how our minds went to the same stupid place. When Hana fully understood what I was asking, a devious glint pierced her sex-fogged eyes."
            scene w3_5673 with dissolve
            mc "So, how much then?"
            scene w3_5672 with dissolve
            "She followed my sick line of thinking and..."
            scene w3_5671 with dissolve
            hana "Oh, I don't know... for a handsome mister like you? Let's say... {b}a hundred dollars?{/b}"
            scene w3_5672 with dissolve
            "...was into it?"
            scene w3_5673 with dissolve
            mc "{b}Deal{/b}, but..."
            scene w3_5674 with dissolve
            mc "...you're going to EARN that money."
        "Take her throat without words.":

            scene w3_5674 with dissolve
            "It was time to let my dick do the talking."

    stop music fadeout 3.0
    scene w3_5675 with dissolve
    "...and so the crown of my cock sank past Hana's parted lips on a languid journey toward her larynx."
    scene w3_5676 with dissolve
    hana "Guuuhhh..."
    "It was a slow descent into Hana's saliva-soaked suck hole, one whose gentleness would be given meaning in the violence that would soon follow."
    scene w3_5677 with dissolve
    if w3HanaBrothelRP == True:
        mc "That's it..."
    "For her part, Hana simply held her mouth open, offering no resistance, her body stiff and her tongue inert in rigid anticipation."
    play ambient "sound effects/kiss2.wav"
    scene hanabar_bj6_a with dissolve
    show hanabar_bj6 with dissolve
    hana "Gh-!"

    if w3HanaBrothelRP == True:
        mc "That's it, {b}bitch.{/b}"

    "Finally, complete and total embrace."

    if w3HanaBrothelRP == True:
        mc "You don't breathe unless I allow it, {b}got it?{/b}"

    "--and here I simply held it, enamored by Hana's submission, inebriated on a feeling of control."
    hana "Mmhhhh..."
    "Seconds passed, and I found that more than just allowing Hana to become accustomed to my size, a feeling of intimacy grew."
    mct "(Yes...!)"
    "A dozen seconds of that, and it felt like we had merged, and that should I pry Hana's lips from my cock, I would be less."
    hana "Ghh, hhuuu-"
    "Two dozen seconds of this waiting game, and I was satisfied that I had imprinted the size, weight, and feeling of my cock into her sex-soaked mind."
    "After half a minute, Hana looked cooked."
    stop ambient
    scene w3_5677 with dissolve
    "So, I withdrew, full of promise that I'd be back... and..."
    play music "music/rifts-for-days.ogg"
    scene hanabar_bj7_a with dissolve
    show hanabar_bj7 with dissolve
    if w3HanaBrothelRP == True:
        mc "There it is!"

    "Man of my word, {b}I was back{/b}."

    if w3HanaBrothelRP == True:
        mc "There it is, cunt!!"

    "In {b}full{/b} control, using Hana's pigtails for their God-given purpose of sliding her beautiful face on and off my bloated cock."
    "{i}Again and again.{/i}"
    scene hanabar_bj8_a with dissolve
    show hanabar_bj8 with dissolve
    "Over and over and over, passing from Hana's pried lips..."
    hana "Huuk-!"
    "To glide with purpose over Hana's tongue..."
    hana "Geeehh-!"
    "...and burrowing my fat dick down the burgeoning cocksucker's tight little throat."
    hana "Guuhh-!"
    "Every cute squeal or sputter signaled my retreat, penis tugging at Hana's windpipe while hastily scraping the roof of her mouth on the way out..."
    hana "Huuumm-!"
    scene hanabar_bj7_a with dissolve
    show hanabar_bj7 with dissolve
    "...only for the voyage down her welcoming throat to begin anew."
    "Naturally, I took it slower at first, feeling out Hana's capabilities."
    "How far could I go before she began to gag?"
    "How hard could I slam the back of her throat without causing her to retreat?"
    "Little by little, I searched for the sweet spot."
    "Hana, so far, kept her composure."
    scene hanabar_bj8_a with dissolve
    show hanabar_bj8 with dissolve
    "The noises that escaped her bulging throat were tame."
    "{i}I knew she wanted more than this.{/i}"
    "I knew {i}I{/i} wanted more than this."
    mct "(...fuck her up?)"
    mc "Ha...."
    "{b}Fuck her up{/b}."
    "I knew it would be rude of me not to consider Hana's heartful and ruinous request, so after being satisfactorily convinced that she could handle it..."
    "It was time to ratchet up the pace."
    scene hanabar_bj9_a with dissolve
    show hanabar_bj9 with dissolve
    if w3HanaBrothelRP == True:
        mc "Fuckin' choke on it!"

    "How far could I take this?"
    "Would she tap out? Would she fight through the discomfort?"
    "How much could she handle?"
    "How much could she endure?"
    hana "Huhh, hhhhhuuu-"
    "Apparently..."
    scene hanabar_bj10_a with dissolve
    show hanabar_bj10 with dissolve
    "*Chwup, fwhhup fwwhhup, theewweeep!*"
    hana "Huuh, hhhmm-"
    "{b}This much{/b}."
    "*{b}Chwwuwp, kwkwwhhup-!!!{/b}"
    hana "Mmhhhuu-♥"
    "Over and over and over again, I drove into her like she was a mere toy."
    hana "Huuuhhhhh-♥♥"
    "Barreling past Hana's gaping lips..."
    hana "HHhhkuk, hhhnuuug-♥♥♥"
    "Digging and gouging the soft muscle of her tongue..."
    hana "Hhhhh-♥♥♥♥"
    "...careening against the back of the goth girl's skull and ramming my cock down her throat. "
    hana "Beellauubh-♥♥♥♥♥"
    scene hanabar_bj11_a with dissolve
    show hanabar_bj11 with dissolve
    "Every gasp and choke signaled that she was still with me."
    "That she was keeping up with this new pace."
    "I could tell it wasn't easy for Hana, but mixed in with her pained expression was one of horny perseverance."
    "That struggle she spoke of in a lusty tone played out in this very moment as she tested her physical mettle against her sexual desire."
    "She wanted a challenge?"

    if w3HanaBrothelRP == True:
        hana "Oh, hhhaaooo-?!"
        mc "*Whisper* ...earn that one hundred bucks, you damn prostitute!"
        hana "Eeeuhh, hhhnggg-"
    else:

        mc "G-gahhh...!"
        "She got one."
        "*Chwwup fwwhhhup, cwwwhup, chwwwwup-!*"
        mc "*Whisper* God d-damn it...!"
        hana "Eeeuhh, hhhnggg-"

    scene hanabar_bj9_a with dissolve
    show hanabar_bj9 with dissolve

    if w3HanaBrothelRP == True:
        mc "{b}This{/b} is what you're best for!"

    "The question was, with how heated I felt, could {i}I{/i} keep up with the challenge?"

    if w3HanaBrothelRP == True:
        mc "Not managing a brothel, but {i}serving{/i} in one."

    "More and more, I was feeling off-kilter. {b}Crazed{/b}."

    if w3HanaBrothelRP == True:
        mc "Fuck you!"

    "The thought of having free rein to fuck Hana's face to my heart's content was enough to put me on edge."

    if w3HanaBrothelRP == True:
        mc "{b}Fuck you!{/b}"

    "*Chwup, ccwwwhhup, thewwweeeep, khhhwwwwup, wwwhhhheeep!*"
    "And the reality?"
    hana "Ghuhhh, hhhk-♥♥♥♥♥♥"
    mct "({b}Fuuuuuuuuuuuuck!{/b})"
    scene hanabar_bj10_a with dissolve
    show hanabar_bj10 with dissolve
    "And what's more, Hana's spasming throat made me want to go even harder."
    "Rougher until she either broke or I ejaculated my entire purpose into her gut."
    mct "(Oh, fuck me...)"
    hana "HHHuuhuhhh, hhhhkhkhkh-!"
    "She was going above and beyond for me today."
    mct "(Oh fuck, oh fuck...!)"
    "The bile in me mixed with something tender."
    hana "Nnggnhg-!"
    "A feeling of appreciation for this remarkable woman."
    hana "HHhheee...♥"
    scene hanabar_bj9_a with dissolve
    show hanabar_bj9 with dissolve
    "She said {i}this{/i} turned her on, but I couldn't help but feel like she was doing something {b}special{/b} for me."
    mct "(God, I should thank her after this.)"
    "I really, really, really, really, really, really should."

    if w3HanaBrothelRP == True:
        mc "*Whisper* Nasty fucking bitch!"
    else:
        mc "*Whisper* God damn it, you're... s-so--"

    mc "...you still with me, babe?"
    hana "Hguh, hggg, hguu...!"
    scene hanabar_bj11_a with dissolve
    show hanabar_bj11 with dissolve
    "{i}Hana looked out of it.{/i}"
    "I would call it unfocused even, if I didn't know all of it was going toward keeping herself alive."
    "Still, she was getting exactly what she asked for."
    "And seeing her like this?"
    mct "(Goddamn it!)"
    "{i}I was close.{/i}."
    mct "(Goddamn it, I--)"
    "Fuck."
    "Her."
    "Up."
    scene hanabar_bj10_a with dissolve
    show hanabar_bj10 with dissolve
    hana "Beelugugh, hhgggk-!"
    "Fuck her up. Fuck her up."
    hana "Beehhk, hhhhkk-!!"
    scene hanabar_bj11b_a with dissolve
    show hanabar_bj11b with dissolve
    "Fuck her up. Fuck her up. Fuck her up."
    hana "Beeehhkk-!!!"
    mct "(FuckherupFuckherupFuckherup!!!!!)"
    "As I drew near, I lost it, praying that Hana would hold up. That some of her would be left over after this."
    "Because by this stage, Hana's mind had fully sublimated into the role of sex toy."
    "The only thing going on between her ears was a face fucking."
    "The complete and total {b}annihilation{/b} of someone's daughter, future wife, future mother..."
    "She wasn't human, but neither was I."
    "{b}God!{/b}"
    "{size=+15}{i}Fucking!{/b}{/size}"
    "{size=+30}{b}DAMN IT!{/b}{/size}"
    scene w3_5678 with dissolve
    aug "That guy is operating in your neck of the woods--"
    scene w3_5679 with dissolve
    mct "(W-whait, wwh, s-shitt--)"
    stop music
    play sound "sound effects/spurt.wav"
    scene w3_5680 with flash
    "--!"
    otto "Yeah, he's a limey prick."
    play sound "sound effects/spurt.wav"
    with flash
    "--!!"
    play ambient "sound effects/gulp3.mp3"
    scene hanabar_bj12_a with dissolve
    show hanabar_bj12 with dissolve
    "Is this how I die?"
    "As August reappeared, and I emptied myself down his daughter's throat, I felt my soul leave my body."
    play sound "sound effects/spurt.wav"
    with flash
    mct "(Fhhhuuuuck... a-ahhh...)"
    "{b}I felt myself cum even harder.{/b}"
    aug "Honestly, it's too rote to find it entertaining."
    mct "(Fhhhuck, I just throat fucked your daughter, you old prick!)"
    otto "Guess the kids got out of here?"
    aug "Seems so. And here I gave them some space."
    mct "(Shit, shit, shit, shit, shit...!)"
    stop ambient
    scene w3_5681 with dissolve
    "Hana was too insensate to register reality right now, but me...?"
    scene w3_5682 with dissolve
    "I pressed Hana deeper into me, hoping to muffle the sounds."
    play music "music/as-i-figure.ogg"
    scene w3_5683 with dissolve
    otto "You like that kid? He seems... sketchy?"
    aug "Jury's still out, but he's attentive."
    scene w3_5684 with dissolve
    otto "Of your daughter?"
    aug "Among other things."
    scene w3_5685 with dissolve
    "Just leave."
    "Please just leave."
    "Please please {b}please{/b} leave."
    scene w3_5686 with dissolve
    "........."
    scene w3_5687 with dissolve
    "......"
    "..."
    scene w3_5688 with dissolve
    "Their footsteps disappeared, but neither of us made a sound."
    "At some point, Hana had come back to her senses and was stiff as a board."
    scene w3_5689 with dissolve
    "......"
    "..."
    scene w3_5690 with dissolve
    mc "Ah--"
    scene w3_5691 with dissolve
    "{b}Fuck.{/b}"
    scene w3_5692 with dissolve
    mc "That was, wow, ahh... how are you--"
    hana "Ghhu... geeeh, hwwwghhh, fhawwwhk..."
    scene w3_5693 with dissolve
    hana "Ha, haa... jhesus... thwought.. w-woahhh..."
    "......"
    "..."
    scene w3_5694 with dissolve
    "For a moment, Hana rambled vacantly, slowly blinking herself to full cognition."
    hana "I was about to fucking croak! That was... ahh... {b}wow.{/b}."
    hana "It's going to take me some days to process these feelings... D-damn..."
    scene w3_5695 with dissolve
    mc "...but let's never do this again, right?"
    hana "...that was your takeaway? Almost getting caught, that was--"
    mc "You're lucky I didn't have a panic attack!"
    scene w3_5696 with dissolve
    hana "Hehehe... haha..."
    scene w3_5697 with dissolve
    "As the tension left our bodies, Hana pulled me into a hug."
    mc "*Whisper* You were wonderful, lover."
    scene w3_5698 with dissolve
    hana "Hmmm...?"
    mc "You worked so hard for me."
    scene w3_5699 with dissolve
    hana "Mmmh... you're welcome."
    mc "...well, was it all you hoped it was?"
    scene w3_5700 with dissolve
    hana "Eh, maybe not so rough next time. "
    hana "Don't get me wrong, that was hot, but... woah. Once is enough."
    hana "I don't want to risk brain damage, you know?"
    scene w3_5701 with dissolve
    "......"
    "..."
    scene w3_5702 with dissolve
    mc "Mmmh..."
    "This was how all of this started..."
    scene w3_5703 with dissolve
    hana "Too bad you gotta go find Chuck."
    $ history_hana = "Hana is taking a more proactive role in club activities, alongside obvious consternation... but there are always ways to blow off stress, aren't there?"
    $ unread_hana = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    scene w3_5704 with dissolve
    mc "...we can take ten minutes to recover. I'm sure he's keeping busy."

    if w3HanaBrothelRP == True:
        scene w3_5703 with dissolve
        hana "Sounds good to me... oh, by the way..."
        scene w3_5704 with dissolve
        mc "Yeah?"
        scene w3_5703 with dissolve
        hana "You owe me a hundred dollars."
        scene black with fade
        stop music fadeout 3.0
        mc "Ah, uhh... do you take credit?"
    else:
        scene black with fade
        stop music fadeout 3.0
        hana "Mmmh... sounds good to me."

    $ renpy.end_replay()

    if not persistent.w3HanaFacefuck:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3HanaFacefuck = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

    "......"
    "..."
    jump w3FindChuck

label w3FindChuck:
    play music "music/the-loner.ogg"
    scene w3_5636 with wiperight
    show screen textbox2 with dissolve
    chuck "[mcf]! Hana!"
    mc "...what are you doing in here?"
    scene w3_5637 with dissolve
    chuck "Watching. Reviewing."
    mc "...watching and reviewing what, exactly?"

    if w3HanaClubKiss == True:
        "Please don't say, \"You throat fucking my friend's daughter\"..."

    scene w3_5638 with dissolve
    chuck "Just some footage from the previous day. I like to keep abreast of some of our patrons' activities."
    scene w3_5639 with dissolve
    hana "Pffh, what? For \"marketing\" purposes?"
    scene w3_5640 with dissolve
    chuck "Entertainment, mostly. Information, sometimes."
    scene w3_5641 with dissolve
    hana "Information, huh? Learn anything interesting?"
    scene w3_5642 with dissolve
    chuck "Well, if you tickle Jim's scrotum with a down feather, he becomes a lot more amenable."
    hana "...you have the STRANGEST hobbies, Dr. Chuck."
    scene w3_5643 with dissolve
    chuck "I'm messing with you, lass."
    hana "...{i}are{/i} you?"
    chuck "Bahaha...! Who knows!"
    scene w3_5644 with dissolve
    mc "Uh, right... so, you wanted to see me...?"
    chuck "That I did, but don't worry! It's not work, and it's not serious!"
    scene w3_5645 with dissolve
    chuck "It's just... mmmhh... I wanted to spend time with you alone today, just you and me."
    scene w3_5646 with dissolve
    mc "...doing what, exactly? What do you have in mind?"
    scene w3_5645 with dissolve
    chuck "Have you ever played squash?"
    scene w3_5646 with dissolve
    mc "I have {i}not{/i}."
    scene w3_5645 with dissolve
    chuck "Good! I'm a novice as well. Why don't we learn the sport together?"
    scene w3_5646 with dissolve
    mc "You want to play squash with me?"
    scene w3_5645 with dissolve
    chuck "I want to do so {b}regularly.{/b} Do you not want to?"
    scene w3_5646 with dissolve
    mc "No, I mean... I didn't say that. It just seems..."
    mct "({i}Random.{/i})"
    scene w3_5647 with dissolve
    chuck "Aw, c'mon. It'll help us get {b}closer{/b}. After that, we can get a bite to eat."
    chuck "What do you say?"
    scene w3_5648 with dissolve
    "Ian has Go, Sophia has Chess, and I'll have {b}squash...{/b}."
    scene w3_5649 with dissolve
    mc "Sure. Could be fun to pick up a new hobby."
    scene w3_5650 with dissolve
    chuck "Great! I had a feeling you might say yes."
    scene w3_5649 with dissolve
    mc "You're a hard man to say no to."
    scene w3_5650 with dissolve
    chuck "Some might even say {i}impossible{/i}."
    scene w3_5651 with dissolve
    hana "...you really like games, don't you?"
    scene w3_5652 with dissolve
    chuck "Hmmm, maybe you and I will have to find one for ourselves someday as well, lass."
    chuck "Your father and I used to play a lot of Scrabble."
    scene w3_5651 with dissolve
    hana "...for real?"
    scene w3_5652 with dissolve
    chuck "Bahaha! You would be surprised! He's quite good at it!"
    scene w3_5653 with dissolve
    hana "...I think I'll get out of your hair."
    chuck "I'd appreciate that, Hana."

    if hanaGF == True and w3HanaClubKiss == True:
        scene w3_5654 with fade
        hana "See you around, tiger."
        mc "Good luck with the whore situation."
        scene w3_5655 with dissolve
        hana "Heh, I'm {i}so{/i} glad I took this new position."
    elif w3HanaDP >= 4 and w3HanaClubKiss == True:
        scene w3_5656 with fade
        hana "See you around, tiger."
        mc "Good luck with the whore situation."
        scene w3_5657 with dissolve
        hana "Heh, I'm {i}so{/i} glad I took this new position."
    elif w3HanaDP >=4 and w3HanaClubKiss == False:
        scene w3_5658 with dissolve
        hana "Talk to you later?"
        mc "Most certainly, and good luck with the whore situation."
        scene w3_5657 with dissolve
        hana "Heh, I'm {i}so{/i} glad I took this new position."
    else:
        scene w3_5658 with dissolve
        hana "See you around, [mcf]. Don't do anything to Rose I wouldn't do, eh?"
        mc "Good luck with the whore situation."
        scene w3_5657 with dissolve
        hana "Yeah, {i}thanks.{/i}"

    scene w3_5659 with dissolve
    "......"
    scene w3_5660 with dissolve
    "..."

    if w3HanaClubKiss == True:
        scene w3_5662 with dissolve
        chuck "You had a close call with August, did you?"
        scene w3_5661 with dissolve
        mc "...you saw that?"
        scene w3_5662 with dissolve
        chuck "I didn't see anything, lad. But I could infer."
        chuck "Thanks for confirming."
        scene w3_5661 with dissolve
        mc "I--"
        scene w3_5663 with dissolve
        chuck "Ha! To be young again, right?"
        scene w3_5664 with dissolve
        mc "...right. Yeah."
        mct "(Fuuuuuuuuuuuuuuck.)"
    else:
        scene w3_5662 with dissolve
        chuck "Beautiful woman, isn't she?"
        scene w3_5661 with dissolve
        mc "...she is."
        scene w3_5662 with dissolve
        chuck "You two came in together."
        scene w3_5661 with dissolve
        mc "...we did."
        scene w3_5663 with dissolve
        chuck "Ah, to be young again."
        scene w3_5664 with dissolve
        "...I was content with letting the old man make his own inferences without adding or subtracting to them."

    scene w3_5662 with dissolve
    chuck "I appreciate you indulging me today. I hope I'm not keeping you from anything."
    scene w3_5661 with dissolve
    mc "Of course not. You're the boss."
    scene w3_5662 with dissolve
    chuck "Don't be so cold, lad."
    stop music fadeout 3.0
    scene black with fade
    chuck "That's an order, because I'm the boss."

label w3AuggyWorries:
    play music "music/night-on-the-docks-sax.ogg"
    scene w3_5706 with w24
    otto "...sounds like you're missing your old life, friend."
    scene w3_5707 with dissolve
    aug "Miss it? I don't know about that, but at least I understood it."
    aug "Chuck and Kathy have always been odd, but as the years go on, I find it more difficult to comprehend what they're thinking."
    scene w3_5706 with dissolve
    otto "Tell me about it."
    scene w3_5708 with dissolve
    aug "Well, for one... Chuck has become increasingly obstinate against making the hard choices."
    aug "For example, even though we could use more hands, he refuses to let me bring more muscle on."
    scene w3_5709 with dissolve
    otto "Lucky for you, you've got me to take care of things discreetly then, eh?"
    scene w3_5710 with dissolve
    aug "Don't act like you're not well-paid for it, asshole. Besides, I don't like having to go behind his back when some asshole creates problems for our low-rent services."
    scene w3_5711 with dissolve
    otto "Why do you even bother with that stuff?"
    scene w3_5712 with dissolve
    aug "What do you mean?"
    scene w3_5711 with dissolve
    otto "I mean that nerd has so much money that this place, even without your platinum clientele, could operate at a loss for the rest of your lifetimes."
    scene w3_5712 with dissolve
    aug "What a stupid question. It's what I do, and Charles is more than happy to take his ample cut of our ventures."
    scene w3_5713 with dissolve
    otto "...but he won't give you more guys?"
    scene w3_5714 with dissolve
    aug "His is a small world, and he likes to keep it that way. He thinks Jacob and Warren are enough to deal with our growing pains."
    aug "The kicker is that when we hit one of those pains, he doesn't--"
    scene w3_5715 with dissolve
    otto "Want to make the hard decisions?"
    aug "He wants everything to have panache. It borders on pathological. Everything is a game and the most obvious solutions are {b}boring{/b}."
    otto "Well, you know how it is... sometimes a majordomo's got to go behind the boss' back to get things done to protect him. "
    scene w3_5716 with dissolve
    aug "He wouldn't see it that way. Every time I go behind his back, I'm playing with fire."
    scene w3_5717 with dissolve
    otto "You two are old friends, aren't you?"
    scene w3_5718 with dissolve
    aug "The oldest I've got."
    scene w3_5719 with dissolve
    otto "I don't fuckin' envy you."
    scene w3_5718 with dissolve
    aug "That's only half of it. There's also Kathy and whatever the fuck she has going on with Abel Van Doren."
    scene w3_5720 with dissolve
    otto "Eh? Now {b}that's{/b} more interesting."
    scene w3_5721 with dissolve
    aug "He's renting the basement of this building, y'know?"
    scene w3_5720 with dissolve
    otto "Can't he buy a whole damn block?"
    scene w3_5721 with dissolve
    aug "Chuck asked me not to stick my nose into it, but I reckon it has to do with the boner drug he's been field-testing with some of our patrons."
    scene w3_5722 with dissolve
    otto "You don't know exactly what's going on? That's gotta be driving you insane."
    scene w3_5723 with dissolve
    aug "He's paying {b}good{/b} money with the assurance of privacy."
    scene w3_5724 with dissolve
    otto "Yeah, but there's the propriety of it. You run this place; you should know what the fuck people are doing."
    otto "I mean, isn't that obvious? Have you gone soft on me?"
    scene w3_5725 with dissolve
    aug "It's Chuck's deal and he tells me it's fine."
    scene w3_5726 with dissolve
    otto "Chuck this, Chuck that... why do you even need that dopey mother fucker? You're the only one adding value to this place."
    scene w3_5727 with dissolve
    aug "Careful, Otto."
    scene w3_5728 with dissolve
    otto "...sorry, it's just you're my old friend too."
    scene w3_5729 with dissolve
    aug "I appreciate it."
    scene w3_5730 with dissolve
    "........."
    "......"
    scene w3_5731 with dissolve
    otto "...you should know what exactly's going on in your own home, August."
    scene w3_5732 with dissolve
    aug "...I know that, but I'm not inclined to push it."
    scene w3_5731 with dissolve
    otto "Why the hell not?"
    scene w3_5732 with dissolve
    aug "My daughter and I have a thing going here.... okay it's not a good thing, but it's better than nothing."
    scene w3_5733 with dissolve
    otto "Old fuck."
    stop music fadeout 3.0
    scene black with fade
    aug "You {i}wish{/i} you looked as young as I do."
    "......"
    "..."

label w3ChuckSquash:
    play music "music/the-loner.ogg"
    scene w3_5734 with blinds
    mc "...{i}he{/i} owns a squash court?"
    chuck "It might surprise you, dull as he is, but Samson has his fingers in {i}many{/i} pies."
    scene w3_5735 with dissolve
    mc "I gather he doesn't {b}spoil{/b} all of them..."
    scene w3_5736 with dissolve
    chuck "Certainly not. He's actually reasonably prudent when it comes to his brand."
    chuck "However, his little shell game with Kathleen is the only bit of color in his otherwise mundane life."
    scene w3_5737 with dissolve
    mc "...you call having a movie career and owning multiple businesses mundane?"
    scene w3_5738 with dissolve
    chuck "Without a doubt, because he's a man who derives his worth from other people."
    chuck "Even if he was the first man to walk on the moon, he measures himself in a mundane way."
    scene w3_5739 with dissolve
    mc "Come on, that's hyperbolic..."
    scene w3_5740 with dissolve
    chuck "It's not! And at your age, just a piece of advice, you should seriously mull over {i}why{/i} you want the things you want."
    scene w3_5741 with dissolve
    mc "Why's that exactly?"
    scene w3_5740 with dissolve
    chuck "{i}You{/i} determine what success is, not the fucks who try to drag you down to their level."
    scene w3_5742 with dissolve
    chuck "The world at large? It only exists up here."
    scene w3_5739 with dissolve
    mc "What good is success if other people don't recognize it?"
    scene w3_5743 with dissolve
    chuck "Let me ask you this. If a small child said you were strong, would you think you could take on Mike Tyson?"
    scene w3_5744 with dissolve
    mc "...you're saying people are easily impressed?"
    scene w3_5745 with dissolve
    chuck "I'm {i}telling{/i} you the only people whose accolades you should lend weight to are those with the same wherewithal."
    chuck "In that sense, I've known bums that measure up better than peers."
    scene w3_5746 with dissolve
    mc "...is that why a rich arms-dealing pervert like you spent your free time advising a public school physics club?"
    chuck "Bahaha! Nah, it's because my nephew refused to go to a private school -- which I couldn't give two shits about. I went to a public school too, mind you, but boy did that drive Gracie mad."
    scene w3_5747 with dissolve
    mc "So you just wanted to be around Ian?"
    scene w3_5748 with dissolve
    chuck "There's more to it than that. Before I'm a \"rich arms-dealing pervert,\" I'm a science-lover."
    scene w3_5749 with dissolve
    chuck "...and being around fresh faces enamored with life's complexity was cathartic in its own way, especially when you're surrounded by so little of that in your professional life."
    chuck "Governmental bureaucrats and stooges, as you can imagine, are lacking in child-like wonder."
    scene w3_5750 with dissolve
    mc "...so what's your own measure of success then, Dr. Chuck?"
    scene w3_5751 with dissolve
    chuck "Right now? {b}Something grand{/b}."
    scene w3_5752 with dissolve
    "......"
    "......"
    chuck "...it's beating someone half my age at hitting a ball at the wall."
    scene w3_5753 with dissolve
    mc "Goddamn it! Why can't I ever get a good read on you?"
    scene w3_5754 with dissolve
    chuck "Maybe you'll get to know me better as we play?"
    scene w3_5755 with dissolve
    mc "You'll have to fill me in on some of the rules, but..."
    scene w3_5756 with dissolve
    hide screen textbox2 with dissolve
    mc "You're on--"
    stop music
    play sound "sound effects/squash.wav"
    scene w3_5757 with dissolve
    scene w3_5758 with vpunch
    "--!"
    jump w3IanRoseConvo

label w3IanRoseConvo:
    play music "music/lobby-time.ogg"
    scene w3_5759 with w20
    kil "Ywwwahhhwwwhh....?"
    scene w3_5760 with dissolve
    show screen textbox2 with dissolve
    kil "How long was I out for?"
    scene w3_5761 with dissolve
    rose "Few hours."
    scene w3_5762 with dissolve
    kil "......"
    scene w3_5763 with dissolve
    kil "...did [mcf] step out?"
    scene w3_5764 with dissolve
    rose "He had to go to the club and Miss Hana went with him."
    rose "Looks like it's just us for a while."

    scene w3_5765 with dissolve
    kil "Yeeeeeuuugh, mmhhh..."
    scene w3_5766 with dissolve
    kil "Yeah, it's just... {i}us{/i}. I hope that doesn't make you uncomfortable."
    scene w3_5767 with dissolve
    rose "Do you want me to make you some food?"
    kil "Not hungry."
    scene w3_5768 with dissolve
    "........."
    "......"
    scene w3_5769 with dissolve
    rose "...and why would being alone with you make me uncomfortable?"
    scene w3_5770 with dissolve
    kil "Because when we first met, you froze up. Shook like a rabbit. Stumbled over your words."
    scene w3_5771 with dissolve
    rose "I remember. You were kind and patient with me then."
    scene w3_5770 with dissolve
    kil "No, I wasn't. You {b}know{/b} I wasn't."
    scene w3_5769 with dissolve
    rose "Let's call it the benefit of hindsight. I have since seen Mrs. Pulman's fangs."
    scene w3_5773 with dissolve
    rose "Compared to that, your brand of chauvinism seems... {i}old-fashioned?{/i}"
    scene w3_5772 with dissolve
    kil "Damn, there ARE some layers to that shit-talk that I am too tired to shift through."
    scene w3_5773 with dissolve
    rose "Shall I make some coffee?"
    scene w3_5772 with dissolve
    kil "Not big on coffee."
    scene w3_5774 with dissolve
    "........."
    scene w3_5775 with dissolve
    "......"
    scene w3_5776 with dissolve
    kil "...and how kind was [mcf]? My uncle used {i}you{/i} to draw him into this business, you know?"
    scene w3_5777 with dissolve
    rose "{i}What{/i} exactly are you asking and why are you asking it?"
    scene w3_5778 with dissolve
    kil "Maybe because in some ways I should thank you, in others..."
    scene w3_5779 with dissolve
    kil "Because you're in his head. The man rushed to check on you over a missed phone call."
    scene w3_5778 with dissolve
    kil "I mean, what sort of mojo are you working on my dude?"
    scene w3_5777 with dissolve
    rose "I'm not \"working\" anything on [mcf]."
    scene w3_5776 with dissolve
    kil "Really? Because he has much to learn about this life, and a sad sack like you is basically the crash course."
    scene w3_5777 with dissolve
    rose "Oh, {b}cram{/b} it."
    scene w3_5780 with dissolve
    kil "See? I'm not so nice."
    scene w3_5781 with dissolve
    rose "I'm a person, you asshole. Not a damn learning experience for your friend."
    scene w3_5782 with dissolve
    kil "Ha! Baha!"
    scene w3_5774 with dissolve
    rose "And what's funny now?"
    scene w3_5783 with dissolve
    kil "You just reminded me of someone else."
    scene w3_5784 with dissolve
    "......"
    "..."
    scene w3_5785 with dissolve
    kil "You didn't answer my question about [mcf]."
    scene w3_5786 with dissolve

    if roseTAapology == True:
        rose "Ask him yourself."
        scene w3_5785 with dissolve
        kil "He'd think I'm weird."
    elif roseTakeAdvantage == True:
        rose "Because it's not worth answering."
        scene w3_5785 with dissolve
        kil "...I read you {b}loud{/b} and clear."
    else:
        rose "He didn't even touch me."
        scene w3_5785 with dissolve
        kil "...really?"

    scene w3_5784 with dissolve
    "........."
    "......"
    scene w3_5785 with dissolve
    kil "I wonder, how many of these awkward pauses can we fit inside of five minutes?"
    scene w3_5787 with dissolve
    rose "Pfff, ha!"
    kil "You like that one, huh?"
    scene w3_5788 with dissolve
    rose "...it's important to you that [mcf] has this job?"
    scene w3_5789 with dissolve
    kil "You don't actually care."
    scene w3_5788 with dissolve
    rose "You're right, but we're talking, and I don't think I will have much luck with this book now that you're up, so..."
    scene w3_5790 with dissolve
    rose "...make me care about it?"
    scene w3_5789 with dissolve
    kil "What's to say? It's good to have a friend."
    scene w3_5790 with dissolve
    rose "You're concerned about him. In a vacuum, it's kinda sweet."
    scene w3_5789 with dissolve
    kil "It's just that if he ends up getting dragged down because of me, I'm responsible for it. That's all I'll say about that."
    scene w3_5791 with dissolve
    "........."
    "......"
    scene w3_5792 with dissolve
    rose "...and THERE is another one. Well, if you don't use your mouth to speak, you can at least use it to chew food."
    scene w3_5793 with dissolve
    kil "You're goddamn relentless, you know that?"
    stop music fadeout 3.0
    scene black with fade
    rose "Maybe I'm just trying to fatten you up so you can't do any harm."
    jump w3ChuckSquash2

label w3ChuckSquash2:
    play sound "sound effects/squash.wav"
    play music "music/training-in-fire.ogg"
    scene w3_5794 with cmet
    chuck "Aaaah.... ha, I should lose some weight!"
    mc "...huh, neither of us is too good at this."
    scene w3_5795 with dissolve
    chuck "That's the fun of it, lad. We're on equal footing."
    mc "That's not flattering, considering the age difference."
    scene w3_5796 with dissolve
    chuck "Candid little shit..."
    chuck "When you drop the act, you sound just like my nephew."
    scene w3_5797 with dissolve
    mc "You {i}could{/i} take it as a compliment - that you're as fit as a man in his early 20s."
    scene w3_5798 with dissolve
    chuck "It's more fun for our game if I don't do that. Besides, I appreciate the candor."
    scene w3_5799 with dissolve
    mc "You do?"
    scene w3_5798 with dissolve
    chuck "Similar to the physics club's wide-eyed optimism, I get so very little ribbing as well."
    scene w3_5799 with dissolve
    mc "I suppose it would behoove me to keep pointing out obvious things, then?"
    scene w3_5796 with dissolve
    chuck "Hit the ball, you fucker."
    play sound "sound effects/squash.wav"
    scene w3_5800 with hpunch
    mct "(Hiya!)"
    scene w3_5801 with dissolve
    chuck "--!"
    scene w3_5802 with dissolve
    chuck "Ha! Good one!"
    mc "Thank you."
    scene w3_5803 with dissolve
    chuck "So, how are you adjusting to the club?"
    mc "...well enough."
    scene w3_5804 with dissolve
    chuck "That drab? I hope your encounter with that gorilla yesterday hasn't soured you."
    scene w3_5805 with dissolve
    mc "...no, that was {i}whatever.{/i}"
    scene w3_5804 with dissolve
    chuck "I didn't think it would, but then again, that {i}was{/i} different from a schoolyard scrap. I would understand if that was sobering."
    scene w3_5807 with dissolve
    "Honestly, maybe that should be a more significant sticking point, but..."
    scene w3_5806 with dissolve
    mc "Well, stuff like that probably isn't going to be a regular occurrence, right?"
    scene w3_5807 with dissolve
    chuck "Most assuredly not."
    scene w3_5808 with dissolve
    "......"
    scene w3_5809 with dissolve
    chuck "...has anything else been bothering you?"
    scene w3_5810 with dissolve
    "His question felt pointed. Like he knew something."
    "--and it wasn't like I had anything to hide, but I certainly had things I didn't want to divulge."
    "However, spending any more time thinking about his basic ass question would just be a huge red flag, so..."
    scene w3_5811 with dissolve
    mc "Are you delaying getting your ass kicked?"
    scene w3_5812 with dissolve
    chuck "...{b}serve{/b}."
    play sound "sound effects/squash.wav"
    scene w3_5813 with vpunch
    mc "--!"
    play sound "sound effects/squash.wav"
    scene w3_5814 with hpunch
    chuck "Heeeet!"
    scene w3_5815 with dissolve
    chuck "...ha, and who's being beat?!"
    scene w3_5816 with fade
    chuck "Going back to my previous question lad, I was only asking because I care about your future."
    scene w3_5817 with dissolve
    mc "You're already helping with that a ton."
    scene w3_5818 with dissolve
    chuck "I'm just giving you money. Money is nothing special."
    scene w3_5816 with dissolve
    chuck "I'd actually like to provide more than that."
    scene w3_5817 with dissolve
    mc "More...?"
    scene w3_5819 with dissolve
    chuck "Indeed. In fact, I'd like for us to become closer."
    scene w3_5817 with dissolve
    mc "What do you mean by closer?"
    scene w3_5818 with dissolve
    chuck "Ha! What does anyone mean by that? Enjoy each other's friendship and pass on what personal wisdom I can."
    scene w3_5817 with dissolve
    mc "Don't you have Ian for that last part?"
    scene w3_5820 with dissolve
    chuck "I do, and I try, but you're part of the family too."
    chuck "I'd like my nephew AND you to grow {i}together{/i}, to not just lead interesting lives, but to {b}cultivate{/b} interesting things in your wake."
    scene w3_5816 with dissolve
    chuck "As for what those interesting things are, you'll just have to show me someday, but the point is... I'd like us to play together like this regularly."
    scene w3_5821 with dissolve
    chuck "...and don't just answer \"you're the boss\". Actually consider what it would mean for us to bond."
    scene w3_5822 with dissolve
    mc "Huh..."
    scene w3_5823 with dissolve
    "Despite his explanation, I still didn't understand what that meant, but I'd be deluding myself if I said a powerful man like him offering something like that with an earnest facade wasn't a headrush."
    "He was far from the man I remembered, but he possessed stature."
    scene w3_5822 with dissolve
    mc "If you ever see the opportunity to give some good advice, I won't turn it down."
    scene w3_5821 with dissolve
    mct "(...but I wouldn't necessarily agree with it, either.)"
    scene w3_5824 with dissolve
    chuck "Coming from you, I'll take that as a yes."
    scene w3_5825 with dissolve
    chuck "Now, let me ask you one thing, [mcf]."
    scene w3_5826 with dissolve
    "......"
    scene w3_5825 with dissolve
    chuck "...are you mundane?"
    scene w3_5827 with dissolve
    "The question itself had a leading effect. It both felt like the obvious answer was {i}yes{/i} and {b}no{/b}."
    "No, because the man posing it defied mundane. And if Samson was mundane, what was I?"
    "Still, {i}being asked that{/i}, made me feel less so..."
    hide screen textbox2 with dissolve

    menu:
        "You're not mundane. How could you be?":
            mc "Right now? I don't feel like I am."
            scene w3_5824 with dissolve
            show screen textbox2 with dissolve
            chuck "Good."
        "You've got room to grow.":
            mc "I've got a lot of life to live first."
            scene w3_5825 with dissolve
            show screen textbox2 with dissolve
            chuck "That answer is very much what I expected from you."
            scene w3_5827 with dissolve
            mc "...is that disappointing?"
            scene w3_5825 with dissolve
            show screen textbox2 with dissolve
            chuck "No, it's playing your cards close to your chest. It is a fine skill, but one you need to learn when not to employ."
        "Be honest: there's nothing special about you.":
            mc "...if I'm going to be honest, it's hard to imagine anything special about me."
            scene w3_5825 with dissolve
            chuck "You won't have to imagine it, lad. You'll only have to give it time."

    scene w3_5828 with dissolve
    chuck "But say... if I gave you two million dollars to give up on being a doctor and become my full-time squash opponent, how would you respond?"
    scene w3_5829 with dissolve
    mc "I'd say that's not a funny joke."
    scene w3_5828 with dissolve
    chuck "And if it wasn't a joke?"
    scene w3_5829 with dissolve
    mc "I'd tell you no."
    scene w3_5828 with dissolve
    chuck "You said that without even thinking about it."
    scene w3_5830 with dissolve

    if id_greed == True:
        mc "The lifetime earning potential of a doctor is greater than two million dollars."
        chuck "Ha!"
    else:
        mc "It's not about the money."

    scene w3_5828 with dissolve
    chuck "And with that, I don't think you're mundane. Which is good, because I'm not losing to some common idiot."
    scene w3_5831 with dissolve
    chuck "Now, let's finish our match and get something to eat."
    stop music fadeout 3.0
    scene black with fade
    "......"
    "..."
    mct "(Wait, was he serious?!)"
    jump w3IanRoseConvo2


label w3IanRoseConvo2:
    play music "music/echo-sclavi.ogg"
    scene w3_5832 with circlewipe
    kil "Christ, when I learned what Dalia went through... I..."
    kil "...didn't do {b}shit{/b}, and that's all there is to say about that, other than maybe I would've digested it better if [mcf] was there."
    kil "He always knew what to do."
    scene w3_5833 with dissolve
    "......"
    "..."
    scene w3_5834 with dissolve
    kil "...I don't know why I'm telling you this. Like seriously, what is this witchcraft?"
    scene w3_5835 with dissolve
    rose "Because you wanted to say it. People are like that."
    rose "You know how you'll fuck anything with a hole? Sometimes that extends to dropping your baggage on people, especially those you don't have any care for."
    scene w3_5836 with dissolve
    kil "...goddamn, Rose. Your gloves are off today."
    scene w3_5837 with dissolve
    rose "Nah, it's just... something I counted on in the past. With some work I did in college."
    scene w3_5838 with dissolve
    kil "......"
    scene w3_5839 with dissolve
    kil "...your old job wasn't whoring, was it?"
    scene w3_5840 with dissolve
    rose "No, why would you conclude that?"
    scene w3_5841 with dissolve
    kil "Yoo-ri, the club's former \"ace\", once told me that people will readily spill their guts to whores because they see them as disposable and unable to judge them."
    scene w3_5842 with dissolve
    rose "Is that your roundabout way of telling me you think I'm--"
    scene w3_5843 with dissolve
    kil "It sounded like a similar observation, is all."
    scene w3_5844 with dissolve
    rose "Well, sorry to burst your bubble, but there are other jobs out there that don't involve selling your body for money."
    scene w3_5845 with dissolve
    kil "...heh, if you zoom out far enough, isn't that technically {i}every{/i} job?"
    scene w3_5844 with dissolve
    rose "...what are you even talking about?"
    scene w3_5845 with dissolve
    kil "Uh, that I'd rather suck dick for a living than be a coal miner?"
    scene w3_5846 with dissolve
    rose "Hehe, {b}fair.{/b}"
    scene w3_5847 with dissolve
    "......"
    "..."
    rose "Should I fetch us some more hot cocoa? I suppose you'll be here until you make that call about your missing friend. "
    scene w3_5848 with dissolve
    kil "...?"
    rose "I hope he's alright."
    scene w3_5849 with dissolve
    kil "...we didn't say anything explicit about that, did we?"
    scene w3_5850 with dissolve
    rose "I was making a guess. The room was easy to read, and when you combine that with your not-great fake dentist plan..."
    rose "I mean, you wanted to find out if he was there, right? Because you don't know where he is?"
    scene w3_5849 with dissolve
    kil "...you made that leap just from that? You guess anything else, Sherlock?"
    scene w3_5848 with dissolve
    rose "Just a confirmation on something I suspected earlier."
    kil "...?"
    scene w3_5851 with dissolve
    rose "That it's none of my business."
    kil "...{i}smart bitch{/i}."
    scene w3_5852 with dissolve
    rose "Still, if it was something you didn't want me to know, you should consider what that Yoo-ri said. You didn't pay me any mind until I spoke up this morning, did you?"
    rose "Imagine what she heard from all those important people you hang around that she probably shouldn't have."
    scene w3_5853 with dissolve
    kil "Heh, no shit... it's probably a gold mine."
    rose "That wasn't my point. I was just saying think about what you say and who you say it around--"
    scene w3_5854 with dissolve
    kil "... oh, that gives me an idea, thanks!"
    rose "Uh... you're welcome?"
    scene w3_5855 with dissolve
    kil "Oh, and the thing about my buddy? It's not exactly a {i}secret{/i} per se, it's just..."
    scene w3_5856 with dissolve
    rose "I don't want to know."
    scene w3_5857 with dissolve
    kil "Yet you're giving me advice about it?"
    scene w3_5858 with dissolve
    rose "You're right. Maybe it's a mom thing I can't turn off?"
    scene w3_5859 with dissolve
    kil "Hmmpfh... you're... {b}solid{/b}, Rose. Actually pretty cool."
    scene w3_5860 with dissolve
    rose "Well, I'm not gas, am I?"
    scene w3_5861 with dissolve
    "........."
    "......"
    scene w3_5862 with dissolve
    rose "...looks like I scored the awkward pause there."
    kil "No, it was funny."
    rose "You didn't even crack a smile."
    kil "Nah, nah... {i}seriously{/i}."
    scene w3_5863 with dissolve
    rose "Hot cocoa or no, jerk?"
    scene w3_5864 with dissolve
    kil "...{i}yes{/i}."
    scene w3_5865 with dissolve
    rose "Very well, Mr. Beaufort."
    kil "...you're doing the mister shit all of a sudden?"
    scene w3_5866 with dissolve
    rose "I just realized I'm being too lippy around you."
    scene w3_5867 with dissolve
    kil "No, you didn't. {b}You knew{/b}."
    stop music fadeout 3.0
    scene black with fade
    kil "And when we're here at [mcf]'s? Just call me Ian."
    "......"
    "..."
    jump w3ChuckLunch

label w3ChuckLunch:
    scene w3_5868 with circlewipe
    "A wise man once said food is tastier when it's free."
    "...I found this to be true."
    play ambient "sound effects/chatter-low.wav"
    scene w3_5869 with dissolve
    mct "(Hmm, yes... the {i}least{/i} I could offer an old man was conversation.)"
    scene w3_5870 with dissolve
    chuck "I hate to sound like a broken record, but are you sure you're adjusting alright?"
    "...{i}did he know something was amiss?{/i}"
    scene w3_5871 with dissolve
    chuck "It's okay not to be 100 percent on board with your new environment. That'd be very normal; it hasn't been very long."
    "Was it just the vibe I was putting out?"
    play music "music/air-on-g.ogg"
    scene w3_5872 with dissolve
    "That was thrice he asked me if anything was bothering me."
    scene w3_5873 with dissolve
    chuck "In fact, it might be more unusual to be {i}completely{/i} acclimatized."
    scene w3_5874 with dissolve
    mc "It'd be crazy not to be, right? What with all the exciting things going on in my life right now."
    scene w3_5873 with dissolve
    chuck "I can hardly imagine how my life would've been for the worse if I had been given access to similar temptations at your age."
    chuck "You'll weather them, though. I have confidence in that."
    scene w3_5872 with dissolve
    "Once again, the affirmation, no matter how unspecific, felt good."
    scene w3_5873 with dissolve
    chuck "So, if you ask me to stop asking you that damn question, then I'll be satisfied."
    scene w3_5875 with dissolve
    "......"
    "..."
    hide screen textbox2 with dissolve

    menu:
        "Mention that Abel dropped by the other day."(chg=["chuck_up"]):
            scene w3_5876 with dissolve
            show screen textbox2 with dissolve
            mc "...Abel Van Doren paid me a visit the other day."
            scene w3_5877 with dissolve
            mc "He let himself in. It was... {i}irksome{/i}."
            scene w3_5878 with dissolve
            "I chose to put it delicately in case ol' Chuck and I weren't on the same page over the impropriety of it."
            scene w3_5879 with dissolve
            chuck "......"
            "...and ol' Chuck carefully gave me a once over, reading between the lines."
            scene w3_5881 with dissolve
            chuck "I bet it was! That asshole has no respect for boundaries."
            scene w3_5880 with dissolve
            chuck "You should see how at home he's made himself at the club - not that I'm complaining. With his lovely apprentice skulking about, there's been ample opportunity to work on my chess game."
            scene w3_5882 with dissolve
            mc "...is your fetish losing to beautiful women? Seriously, what's the deal with that?"
            "I tried to change the topic, but..."
            scene w3_5880 with dissolve
            chuck "Abel's a curious fellow, isn't he? I like him, but I'm afraid he's not my biggest fan."
            scene w3_5882 with dissolve
            mc "You don't get along?"
            scene w3_5883 with dissolve
            chuck "Getting along is for toddlers and those in sexless marriages. {i}I respect him.{/i}"
            scene w3_5884 with dissolve
            mc "Well, I don't really like the idea of a club patron surprising me where I sleep. I know my job is kissing their asses, but I could've had company."
            scene w3_5883 with dissolve
            chuck "I'm sorry if he startled you. I hope it was at least a productive visit."
            scene w3_5885 with dissolve
            mc "Uh..."
            "Even if I could make sense of it, I wasn't sure if I wanted to fill Chuck in on our conversation."
            mc "Well--"
            scene w3_5886 with dissolve
            chuck "I'm not asking for details."
            mc "...you're really not interested? You were dogged about dragging it out of me."
            chuck "I just wanted to hear how you are doing. Whatever you talked about is between you and him."
            scene w3_5887 with dissolve
            chuck "......"
            chuck "...unless there's something you'd LIKE to share with me. My offer to listen to your problems will never expire."
            chuck "It doesn't even have to be a grievance. We can talk about anything you like."
        "Keep your cards close to your chest. (w3ChuckClose = True)"(chg=["chuck_down2"]):

            $ w3ChuckClose = True
            $ Chuck_Friendship -= 1
            scene w3_5876 with dissolve
            show screen textbox2 with dissolve
            mc "Why do you ask? Do I seem... {i}bothered?{/i}"
            scene w3_5875 with dissolve
            chuck "Do you want the honest answer or the extra honest answer?"
            scene w3_5876 with dissolve
            mc "Uh... okay, um... hit me with the extra honest answer?"
            scene w3_5880 with dissolve
            chuck "You always seem bothered. You have the disposition of a rodent."
            scene w3_5882 with dissolve
            mc "And what was the plain honest answer?"
            scene w3_5880 with dissolve
            chuck "That I'm only asking because I want to know how you're doing."
            scene w3_5882 with dissolve
            mc "I will remember to carefully consider that question next time."
            scene w3_5883 with dissolve
            chuck "Sorry."
            scene w3_5884 with dissolve
            mc "Anyway, I'm... {i}good?{/i}"
            scene w3_5883 with dissolve
            chuck "Are you uncertain?"
            scene w3_5884 with dissolve
            "I feigned ambiguity because ambiguity seemed appropriate since I didn't just outright answer his question."
            mc "Yeah, I mean..."

    scene w3_5889 with dissolve
    mc "It's just the usual: am I doing the right things at the right time, in the right way, to achieve what I want to achieve for myself and the people I care about?"
    "That much was true. A happy middle ground between obfuscation and being forthright."
    scene w3_5890 with dissolve
    chuck "All normal questions I can relate to."
    scene w3_5889 with dissolve
    mc "Really? I don't believe you have an ounce of doubt in your body."
    scene w3_5890 with dissolve
    chuck "Once upon a time. I wasn't always old and wealthy, you know - not that either of those cures you of all doubt, but..."
    scene w3_5891 with dissolve
    mc "...it helps?"
    chuck "Baha! Sure as shit does!"
    scene w3_5892 with dissolve
    mc "What were you like when you were my age?"
    scene w3_5893 with dissolve
    chuck "That was so long ago that it's hard to give an accurate answer, even if you don't factor in that we're never the most reliable witnesses to our own character."
    chuck "When I was your age, I had Gracie to worry about and take care of."
    scene w3_5892 with dissolve
    mc "...you raised your sister? How did I not know that?"
    scene w3_5894 with dissolve
    chuck "You may have realized I'm quite a bit older than her. Nineteen years, to be exact."
    chuck "When I was your age, fresh out of college, she would've been just three years old. I can only speculate why my parents waited so long to have another kid, but it left just enough of a gap that I had my wits about me after their accident."
    scene w3_5895 with dissolve
    mc "...?"
    chuck "Drowning. My father tried to save my mother, but she pulled him down."
    scene w3_5896 with dissolve
    chuck "Thankfully, she was too young to remember, but I don't know how many hours my sister spent on the shoreline before another couple found her."
    scene w3_5897 with dissolve
    mc "Holy shit..."
    scene w3_5898 with dissolve
    chuck "So I shaped up. Simple as that."
    scene w3_5899 with dissolve
    chuck "I took my degree and applied for a position in the engineering corps. It was something reliable that offered assurance that Gracie would have an income if anything ever happened to me."
    chuck "Eventually, on the taxpayer's dime, I continued my education. Some years after that, I started my own company, and..."
    scene w3_5900 with dissolve
    chuck "To double back to your original question, I wasn't a very {i}fun{/i} person. Not the chipper fellow in front of you now."
    scene w3_5882 with dissolve
    mc "You had it rougher than I imagined."
    scene w3_5900 with dissolve
    chuck "I've never given you a reason to imagine otherwise. It wasn't easy, but at least I was an adult by the time I had to get it together."
    chuck "It's different from losing a parent at a young age, as you can attest."
    scene w3_5884 with dissolve
    "Even with that purposeful distinction, I felt a new point of connection tethering us."
    scene w3_5879 with dissolve
    mc "You lost both your parents, though. I don't think that can really compare."
    scene w3_5881 with dissolve
    chuck "It was a long time ago. A whole lifetime."
    scene w3_5882 with dissolve
    "......"

    if w3ChuckClose == True:
        $ Chuck_Friendship -= 1
        scene w3_5883 with dissolve
        chuck "I'm just glad Abel's visit didn't put you out of sorts."
        scene w3_5901 with dissolve
        "........."
        "......"
        scene w3_5903 with dissolve
        "..."
        scene w3_5902 with dissolve
        mc "You, uh, ah, ummm-"
        scene w3_5903 with dissolve
        mct "({i}He fucking knows?{/i})"
        scene w3_5902 with dissolve
        mc "I mean, it was {i}weird{/i}. Did Ian mention something to you or--?"
        scene w3_5901 with dissolve
        chuck "Don't worry. He still has your trust."
        chuck "It was Van Doren himself who mentioned he dropped by."
        "Son of a bitch!"
        scene w3_5902 with dissolve
        mc "...and did he happen to fill you in on the why?"
        scene w3_5904 with dissolve
        chuck "No. He left it vague on purpose, most likely to annoy me."
        scene w3_5905 with dissolve
        mc "Well, uh... he succeeded in annoying {i}me{/i} at least. His lack of \"notice\" was unappreciated."
        scene w3_5906 with dissolve
        mc "For example, I could've had company, like my mom, but... wait, why would he visiting me outside the club annoy {b}you{/b}?"
        scene w3_5904 with dissolve
        chuck "Hmm, how can I put it? It was like... finding out your mother had been snooping around your room while you were out?"
        scene w3_5907 with dissolve
        "......"
        mc "...and WHY would he {i}want{/i} to annoy you?"
        chuck "Full of questions, aren't you?"
        scene w3_5908 with dissolve
        mc "'cause I have no idea what his visit was about. I've really been racking my brain over it."
        scene w3_5887 with dissolve
        chuck "Without knowing the contents of your discussion, I'd say it's because he's not a nice man and I don't think he's too fond of me."
        scene w3_5908 with dissolve
        mc "That's it?"
        scene w3_5887 with dissolve
        "That seemed like such a non-reason, but maybe it was just as good as any?"
        chuck "To be honest, I've been going out of my way to mess with him a little bit. Just your typical dick-measuring contest between men, but most of all, I don't think he appreciates me engaging with his lovely assistant on my own terms."
        chuck "Imagine if you presented someone with a beautifully cooked steak dinner, but instead of eating it, they take it home and throw it on their grill."
        scene w3_5908 with dissolve
        mc "That sounds kinda petty."
        scene w3_5887 with dissolve
        chuck "He's a brilliant and entertaining man. Petty is in his repertoire."
        scene w3_5908 with dissolve
        mc "Why wouldn't he sniff around Ian, then?"
        scene w3_5887 with dissolve
        chuck "That's a salient question."
        scene w3_5885 with dissolve
        mc "...well, do you want to know what we talked about?"
        scene w3_5886 with dissolve
        chuck "I don't. That's your business, and I'm not going to give him the pleasure of me prying {i}too{/i} deeply."
        chuck "All I really wanted to know was if he bothered you."
        mc "Uh, so-so?"
        scene w3_5909 with dissolve
        "I wasn't going to mention the stuff about Darius, of course. So, I kept it non-committal."
        scene w3_5910 with dissolve
        chuck "Sorry if he startled you, but you should consider it a compliment."
    else:
        $ Chuck_Friendship += 1
        scene w3_5907 with dissolve
        "........."
        "......"
        "..."
        scene w3_5902 with dissolve
        mc "... so, do you have any idea why Dr. Van Doren would pay me a visit?"
        scene w3_5903 with dissolve
        "That was hanging on my mind, and since I let the cat out of the bag, I might as well search for answers."
        scene w3_5904 with dissolve
        chuck "I suspect he did so to annoy me. A bit of dick-measuring between men."
        chuck "I've been taking an inordinate interest in his prized assistant and maybe he's just doing the same?"
        scene w3_5905 with dissolve
        mc "Why wouldn't he sniff around Ian, then?"
        scene w3_5904 with dissolve
        chuck "That's a salient question. Maybe he thinks you're easier to mess with?"
        scene w3_5906 with dissolve
        mc "And all because you play chess with his assistant?"
        scene w3_5887 with dissolve
        chuck "Look at it this way: he practically throws Sophia at people. It's his way of flexing."
        chuck "He utilizes one of the brightest women in the world as if she was a common whore."
        scene w3_5910 with dissolve
        chuck "But instead of accepting his hospitality, I engage her on my own terms. With my own ends in mind. If I was him, it'd annoy me."
        scene w3_5911 with dissolve
        mc "Sounds petty."
        scene w3_5910 with dissolve
        chuck "It is, but it's how assholes like us pass the time. I'm sorry if he startled you, but you should consider it a compliment in a way."

    scene w3_5911 with dissolve
    mc "...{i}should{/i} I?"
    scene w3_5910 with dissolve
    chuck "I mean, if it's tit-for-tat with Sophia?"
    scene w3_5911 with dissolve
    mc "It's exhausting trying to make sense of why rich people do the things that you do."
    scene w3_5912 with dissolve
    chuck "I'll save you the trouble for next time. It's always about ego. {b}Always{/b}."
    mc "Ha!"
    "For all his red flags, I'd give Dr. Chuck this: he spoke easily and openly with me, with the same candor he purportedly appreciated."
    scene w3_5899 with dissolve
    chuck "...so, how's your prep for the MCATs coming?"
    scene w3_5882 with dissolve
    mc "...these past few weeks? I've probably looked at fewer drills than I should."
    scene w3_5900 with dissolve
    chuck "Oh, that won't do. What's your schedule usually like?"
    scene w3_5913 with fade
    "So, we talked in a way reminiscent of my high school years."
    "How to stay focused, prioritize what you read, and keep things in perspective..."
    "{b}Reassurances{/b} that I was on the right path."
    scene w3_5914 with fade
    mc "But I wonder if making it easier for me will cheapen the result when it's all said and done."
    "It was abnormally normal given our difference in elevation, but it was... {b}welcomed{/b}."
    chuck "Nonsense, money won't study for you or complete your residency. {b}When it's all said and done{/b}, your success will be yours."
    stop ambient fadeout 3.0
    scene w3_5915 with dissolve
    "........."
    "......"
    scene w3_5916 with dissolve
    chuck "...what do you think is the singular most crucial characteristic of a man? What, more than anything else, separates us from the rest of the animals?"
    scene w3_5917 with dissolve
    mc "The {b}single{/b} thing?"
    scene w3_5918 with dissolve
    chuck "Yes, I know it's reductionist, but you'll forgive an old man for simplifying things so he can act like he has it all figured out."
    scene w3_5919 with dissolve
    mc "Hmm..."
    hide screen textbox2 with dissolve

    menu:
        "It's our intelligence.":
            scene w3_5920 with dissolve
            show screen textbox2 with dissolve
            mc "Capacity for language, ability to use tools, organize, and record knowledge to be passed down from generation to generation?"
            scene w3_5921 with dissolve
            chuck "Ha! That is the more obvious answer, and technically more accurate than my thing, but I'm looking for something more {i}spiritual{/i} in nature."
            scene w3_5920 with dissolve
            mc "What is it then?"
            scene w3_5923 with dissolve
            chuck "Control. It's knowing when to restrain yourself and delay gratification."
            chuck "Animals simply do."
        "Is it manners?":
            scene w3_5920 with dissolve
            show screen textbox2 with dissolve
            mc "...is it good manners?"
            scene w3_5922 with dissolve
            chuck "Is that a joke?"
            scene w3_5920 with dissolve
            mc "Have you ever seen a fish say thank you?"
            scene w3_5923 with dissolve
            chuck "It's control. It's knowing when to restrain yourself and deny your base desires."
            chuck "If you or nature would allow it, a fish would eat until its belly bursts open."
        "Empathy?":
            scene w3_5920 with dissolve
            show screen textbox2 with dissolve
            mc "Empathy?"
            scene w3_5922 with dissolve
            chuck "Elephants have empathy."
            scene w3_5920 with dissolve
            mc "What is it then?"
            scene w3_5923 with dissolve
            chuck "Control. It's knowing when to restrain yourself and delay gratification."

    scene w3_5924 with dissolve
    mc "Yet you tell Ian he should be unrestrained and do whatever he wants?"
    scene w3_5925 with dissolve
    chuck "Aye, he should. The key here is whatever {i}he{/i} wants, but do you remember what I said about forging your own way?"
    chuck "If someone proclaims that you can eat as much as you want, who is to blame if you engorge yourself to the point of sickness?"
    scene w3_5926 with dissolve
    mc "Obviously, it's the latter."
    scene w3_5927 with dissolve
    chuck "We are of the same mind, then. Choice gives life meaning, and unfortunately, that also means anyone is free to not live up to their potential."
    chuck "I love my nephew and I {b}will{/b} lay the world at his feet, but I can't pick it up for him."
    scene w3_5928 with dissolve
    mc "I wonder how your sister would feel about that."
    scene w3_5929 with dissolve
    chuck "Oh, I think you know the answer to that, but the point is... {b}control{/b}."
    scene w3_5930 with dissolve
    chuck "I want to leave you with that. Consider the word's relevance in your own life. Consider where you will draw {b}lines.{/b}"
    scene w3_5929 with dissolve
    chuck "If you master yourself, the world becomes a lot simpler -- and makes finally indulging yourself all the more vivid when you do."
    scene w3_5928 with dissolve
    mc "Thank you for the advice."
    scene w3_5929 with dissolve
    chuck "Thank you for listening."
    chuck "I should write fortune cookies, right?"
    stop music
    play ambient "sound effects/chatter-low.wav"
    play sound "sound effects/sms-chime.wav"
    scene w3_5931 with dissolve
    "*Beep*"
    scene w3_5932 with dissolve
    mc "..."
    scene w3_5933 with dissolve
    hide screen textbox2 with dissolve
    call phone_start_hana from _call_phone_start_hana_3
    call message_start ("Hana", "Blah, I don't know if I did the right thing here..") from _call_message_start_32
    call reply_message ("Is this about the Kimber thing?") from _call_reply_message_47
    call message ("Hana", "Yeah, I told her she had to work...") from _call_message_98
    call reply_message ("What changed things?") from _call_reply_message_48
    call phone_end_hana from _call_phone_end_hana_4
    scene w3_5932 with dissolve
    show screen textbox2 with dissolve
    "........."
    "......"
    "...no reply."
    scene w3_5934 with dissolve
    mc "Sorry. Hana."
    scene w3_5935 with dissolve
    chuck "S'alright."
    scene w3_5934 with dissolve
    mc "She's \"acclimatizing\" to having a stake in things."
    scene w3_5935 with dissolve
    chuck "Hmm, maybe we should've included her in this little lunch."
    play sound "sound effects/sms-chime.wav"
    scene w3_5932 with dissolve
    "*Beep*"
    scene w3_5933 with dissolve
    hide screen textbox2 with dissolve
    call phone_start_hana from _call_phone_start_hana_4
    call message_start ("Hana", "I didn't think it was fair to hot potato her clients in another girl's lap, so I went to her apartment to meet face to face.") from _call_message_start_33
    call message ("Hana", "Wanted to see what was up with her. Maybe looking for an excuse...") from _call_message_99
    call reply_message ("How'd that go?") from _call_reply_message_49
    call message ("Hana", "At first she said she wasn't feeling good, but I didn't even push her on it or anything. I guess she could sense I was on her side, because she let slip she was seeing her sugar daddy tonight.") from _call_message_100
    call message ("Hana", "Had all this expensive crap laying around too... I don't know... for a brief second I just kinda stopped feeling and thinking and just blurted out what I felt in my gut.") from _call_message_101
    call reply_message ("Now you feel bad?") from _call_reply_message_50
    call message ("Hana", "Now I feel bad.") from _call_message_102
    call message ("Hana", "I mean all that designer stuff is probably for work, right? And I still don't think you should insist about this kind of work...") from _call_message_103
    call phone_end_hana from _call_phone_end_hana_5
    scene w3_5932 with dissolve
    show screen textbox2 with dissolve
    "Seems she's looking for reassurance..."
    scene w3_5936 with dissolve
    mc "What would August do to a girl who skipped work to meet a guy on company time?"
    scene w3_5935 with dissolve
    chuck "He'd take corrective action."
    scene w3_5936 with dissolve
    mc "Is that what I imagine?"
    scene w3_5935 with dissolve
    chuck "Spare the rod, spoil the child."
    scene w3_5937 with dissolve
    mct "(Goddamn it...)"
    hide screen textbox2 with dissolve

    menu:
        "Tell her she did the right thing because it's unfair to the other girls.":
            scene w3_5933 with dissolve
            show screen textbox2 with dissolve
            mct "(...best keep that detail to herself, lest she hate herself even more.)"
        "She did the right thing, because that's what's best for Kimber. (w3KimberReality = True)"(chg=["hana_anger_up"]):
            scene w3_5933 with dissolve
            $ w3KimberReality = True
            $ Hana_Anger +=1
            show screen textbox2 with dissolve
            mct "(...in a way, it's saving her from herself, right?)"
        "Agree that insisting on this kind of thing is wrong (w3KimberWrong = True)"(chg=["hana_anger_up"]):
            $ w3KimberWrong = True
            $ Hana_Anger +=1
            scene w3_5933 with dissolve
            show screen textbox2 with dissolve
            mct "(...she's right about that last part.)"

    jump w3HanaMinaMeetCute

label w3HanaMinaMeetCute:
    stop ambient
    play sound "sound effects/sms-chime.wav"
    scene w3_5938 with wipeleft
    hana "........."
    play sound "sound effects/sms-chime.wav"
    hana "......"
    play sound "sound effects/sms-chime.wav"
    hana "..."
    scene w3_5939 with dissolve
    mina "Hana, hey!"
    play music "music/ukulele-fun.ogg"
    scene w3_5940 with dissolve
    hana "Oh, uh... hey!"
    mina "I'm not late, am I?"
    scene w3_5941 with dissolve
    hana "We both got here early."
    scene w3_5942 with dissolve
    mina "Awesome! It's good to see you! I was thrilled to hear from you!"
    hana "Um, heh... uh..."
    mina "You've got no idea!"
    scene w3_5943 with dissolve
    "......"
    scene w3_5944 with dissolve
    hana "...I know I was the one who asked you, but I was a little surprised you wanted to get together so soon."
    scene w3_5943 with dissolve
    mina "Well, I hate it when people say they want to connect later."
    mina "Later, later, later... Why not now? No better time than the present. "
    mina "That's how stoked I was to get your call."
    scene w3_5944 with dissolve
    hana "Man. You. Are. A. Peach."
    scene w3_5945 with dissolve
    mina "Heh, {i}peach?{/i}"
    scene w3_5946 with dissolve
    hana "I'm embracing my inner sexist-old-man today."
    hana "{size=-10}In more ways than one...{/size}"
    play sound "sound effects/sms-chime.wav"
    scene w3_5947 with dissolve
    "*Beep!*"
    mina "And how's that working for you?"
    scene w3_5948 with dissolve
    hana "Well, I'm getting a hankering to start a corporate takeover. That and a slice of lemon cake."
    mina "That sounds SO good - AND some tea."

    if w3KimberReality == True or w3KimberWrong == True:
        scene w3_5949 with dissolve
        hana "Tssk! Hmm..."
        mina "Everything okay? That's an intense look to give your phone."
    else:
        scene w3_5950 with dissolve
        hana "Mmmm..."
        mina "Everything okay? That's an intense look to give your phone."

    scene w3_5951 with dissolve
    hana "Sorry. I make it a habit not to check my phone when meeting with people like this, but..."
    hana "Work thing. An {b}annoying{b} work thing."
    scene w3_5952 with dissolve
    mina "Want to talk about it?"
    scene w3_5953 with dissolve
    hana "No offense, but..."
    mina "None taken."
    scene w3_5954 with dissolve
    hana "It's just... I'd rather not think about it right now?"
    scene w3_5955 with dissolve
    mina "{b}None{/b} taken! So...! I was pretty surprised, too!"
    mina "What made you want to get lunch with little ol' me?"
    scene w3_5956 with dissolve
    hana "........."
    hana "......"
    scene w3_5957 with dissolve
    hana "...I wanted to make a friend."
    scene w3_5958 with dissolve
    mina "Really?! You want to be friends?"
    scene w3_5959 with dissolve
    hana "Christ, what am I, in kindergarten?"
    scene w3_5960 with dissolve

    if w3HanaFriendEncourage == True:
        hana "Well, I was recently encouraged to make more friends, so..."
    else:
        hana "Well, it's been brought to my attention that... uh... BY ME... that I..."

    hana "I could use some \"getting to know somebody\" and you leave an--"
    scene w3_5961 with dissolve
    mina "AWESOME~!"
    scene w3_5962 with dissolve
    hana "...i-is it?"
    scene w3_5961 with dissolve
    mina "I was hoping that'd be the case, but you just came out and said it! {b}God{/b}, that's cool!"
    scene w3_5962 with dissolve
    hana "Pffh, you're going to make me blush."
    scene w3_5963 with dissolve
    mina "I'll be honest too, I..."
    scene w3_5964 with dissolve
    mina "I'd love to get to know you better. I've been trying to broaden my horizons and you're the kind of friend I don't think I'd normally make."
    scene w3_5965 with dissolve
    hana "What kind of friends do you usually make?"
    scene w3_5966 with dissolve
    mina "They DON'T ride motorcycles."
    scene w3_5967 with dissolve
    hana "Hehe, you want to go for a ride after this?"
    mina "WOULD I?! WOULD I EVER!"
    scene w3_5968 with dissolve
    hana "Ha! You're uh..."
    mina "Sorry. I can be a lot, I know."
    scene w3_5969 with dissolve
    hana "You kidding? Your excitement is cooler than cool. It's... {i}refreshing{/i}."
    scene w3_5970 with dissolve
    mina "Mmmh... I've had girlfriends who think it's fake as fuck."
    scene w3_5971 with dissolve
    hana "Fuck 'em. You hurtin' anybody?"
    hana "Just jealous bitches who think everyone's gotta be as dull as they are. World's full of 'em."
    scene w3_5972 with dissolve
    mina "Are you speaking from experience?"
    scene w3_5973 with dissolve
    hana "Sure as shit am."
    scene w3_5972 with dissolve
    mina "God, you make cursing sound good."
    scene w3_5973 with dissolve
    hana "You wanna yell some expletives with me?"
    scene w3_5972 with dissolve
    mina "Right here? In the cafe?"
    scene w3_5974 with dissolve
    hana "Yeah!"
    scene w3_5975 with dissolve
    mina "Please don't. I want that lemon cake..."
    scene w3_5976 with dissolve
    hana "Cooler heads prevail."
    scene w3_5977 with dissolve
    mina "Pffft-hehehe!"
    hana "...but yeah. Let's take things slow."
    hana "Order something and see if you don't hate me by the end of it. Alright, peach?"
    mina "Hehehehe..."
    stop music fadeout 3.0
    scene black with fade
    mina "Is that going to be a recurring thing?"
    "......"
    play sound "sound effects/motorcycle-ride.wav"
    "..."
    play music "music/rifts-for-days.ogg"
    scene w3_5978 with cmet
    mina "Woooooooooooaaaaaah! THIS IS AWESOME!"
    hana "You've been saying that for the last three minutes!"
    mina "BECAUSE IT IS! I WANT ONE OF THESE!"
    scene w3_5979 with dissolve
    mina "I feel so..."
    hana "Alive?!"
    mina "Yeah!"
    hana "Excited?!"
    mina "Yeah!"
    scene w3_5980 with dissolve
    hana "Horny?!"
    mina "Yea-- w-wait, wha-?"
    hana "Don't worry! That's normal!"
    hana "You've got 73 horsepower right between your legs!"
    scene w3_5981 with dissolve
    mina "Pffh, ha-hahaa... is that why you own one of these things?"
    hana "All of the above! Now, you probably want to close your mouth."
    mina "Why--"
    scene black with fade
    mina "*Cough, ccough* Haa, hahhhaaaa!"
    hana "{b}Bugs!{/b}"
    "......"
    "..."
    jump w3ThreesCompany

label w3ThreesCompany:
    play music "music/crinoline-dreams.ogg"
    scene w3_5982 with blinds
    mc "Look who's up. You didn't drool all over my sheets, did you?"

    if w3VeronicaSex == True:
        scene w3_5983 with dissolve
        kil "If I did, let's call it payback for the white mess you made on my couch last night."
        rose "Uh... w-what?"
    else:
        scene w3_5984 with dissolve
        kil "Don't worry. It'll dry."

    scene w3_5985 with dissolve
    mc "And what have you two been up to?"
    scene w3_5986 with dissolve
    kil "Rosie's been nose-deep in a book all morning. I looked it up and it's pretty, uh... I mean..."
    kil "It's porn, isn't it?"
    scene w3_5987 with dissolve
    rose "What? It's literature!"
    scene w3_5988 with dissolve
    kil "...is it? What literature has graphic descriptions of eating pussy?"
    scene w3_5989 with dissolve
    rose "Am I really taking flak from {i}you{/i}?"
    scene w3_5988 with dissolve
    kil "I'm not giving you flak... just telling [mcf] what's up."
    kil "Personally? I think reading porn is very modern of you."
    scene w3_5990 with dissolve
    "Rosalind stared daggers into Ian, but he paid it no mind."
    scene w3_5991 with dissolve
    kil "......"
    kil "..."
    scene w3_5992 with dissolve
    mc "I see you busted out the scotch?"
    scene w3_5993 with dissolve
    kil "Shit, man, you were gone awhile. I was starting to get bored."
    kil "Besides, don't worry. I just poured this. I couldn't convince Rosie to have any..."
    scene w3_5994 with dissolve
    mc "You just poured this?"
    kil "What I--"
    scene w3_5995 with dissolve
    kil "--said."
    mc "......"
    scene w3_5996 with dissolve
    mc "...no day drinking, asshole. I'll tell Victoria."
    scene w3_5997 with dissolve
    kil "You wouldn't!"
    scene w3_5998 with dissolve
    mc "Hmmm? Won't I?"
    scene w3_5997 with dissolve
    kil "I'm an adult, I can--"
    scene w3_5998 with dissolve
    mc "You don't think I will?"
    scene w3_5999 with dissolve
    kil "I, uh... I acquiesce and defer to your grand wisdom, brother."
    scene w3_6000 with dissolve
    rose "Pffh, paaah!"
    scene w3_6001 with dissolve
    rose "So, that's the secret to getting him to behave?"
    mc "Always has been. Ever since we were kids."
    scene w3_6002 with dissolve
    rose "Heheheh..."
    kil "And what are you doing?"
    scene w3_6003 with dissolve
    rose "I think I'll have that drink now."
    kil "...ah, you bitch. Twist the knife, why don't you?"
    scene w3_6004 with dissolve
    mc "Funny."
    "It was only a quick swig, but she knocked it back with a flair, like it was much more."
    scene w3_6005 with dissolve
    rose "Who's trying to be funny?"
    "She flashed an unusually naked smile my way. It was a faint hope, but maybe Rosalind was becoming more comfortable in my home?"
    scene w3_6006 with dissolve
    kil "So, time to phone Hawaii? The factory should be open by now."
    scene w3_6007 with dissolve
    mc "Looks like it."
    scene w3_6008 with dissolve
    rose "Should I go pick up some milk? You need some."
    kil "Naaaaaah, just stay. You have it figured out."
    scene w3_6009 with dissolve
    rose "You sure?"
    mc "He's right. We're just trying to locate a friend of Ian's."
    rose "Alright. You're the king of the castle."
    scene w3_6010 with dissolve
    mc "I'm calling."
    play ambient "sound effects/ringing-outbound.mp3"
    scene black with fade
    "*Ring, bbrrrring~*"
    scene w3_6011 with fade
    "*Briiiiing, ring, brrrrring~*"
    "*Briiiiiing, ring~*"
    scene w3_6012 with dissolve
    mc "I don't think--"
    stop ambient
    play sound "sound effects/phonemenu.wav"
    scene w3_6013 with dissolve
    woman "Aloha! Blossom Textiles. I apologize for the wait."
    "A gravelly voice put to rest any hope of no one picking up."
    woman "How can I help you?"
    scene w3_6014 with dissolve
    mc "Please put me in touch with Mr. Lee. It's about his son."
    scene w3_6015 with dissolve
    "......"
    "..."
    "Nothing."
    woman "...his son?"
    scene w3_6014 with dissolve
    mc "Yes, {b}Darius.{/b} It's critical that I speak to Mr. Lee about him."
    scene w3_6015 with dissolve
    "Just like Rosalind had suggested, I put a particular emphasis on my request."
    "......"
    "..."
    scene w3_6014 with dissolve
    mc "...are you--"
    "{i}*Click*{/i}"
    play sound "sound effects/phonemenu.wav"
    scene w3_6016 with dissolve
    mc "......"
    mc "...what the fuck?"
    kil "...eh, what is it?"
    scene w3_6017 with dissolve
    mc "The lady who answered hung up at the first mention of Darius' name."
    "Of all the possibilities, I wasn't expecting {i}that{/i}."
    scene w3_6018 with dissolve
    kil "Maybe the call dropped? Try calling them back."
    scene w3_6019 with dissolve
    mc "Yeah, let's try that..."
    play ambient "sound effects/ringing-outbound.mp3"
    scene w3_6020 with dissolve
    "........."
    "......"
    scene w3_6021 with dissolve
    "..."
    stop ambient
    scene w3_6022 with dissolve
    mc "Nothing."
    kil "{b}What the fuck?{/b}"
    scene w3_6023 with dissolve
    mc "That's what I said! Does any of this make sense to you?"
    kil "Maybe the receptionist is a jilted lover?"
    mc "Be serious."
    kil "Fuck me, I am!"
    scene w3_6024 with dissolve
    "More than underwhelming, this result was {b}frustrating{/b}."
    scene w3_6025 with dissolve
    kil "Maybe we just forget about it?"
    mc "Maybe..."
    scene w3_6024 with dissolve
    "........."
    "......"
    "..."
    scene w3_6026 with dissolve
    mc "Give me that."
    scene w3_6027 with dissolve
    "{i}Maybe{/i} my curiosity would be sated by this honest attempt."
    kil "By the way, who called on you earlier? The old woman, the old man, or our old man?"
    scene w3_6028 with dissolve
    mc "Dr. Chuck wanted to play squash, of all things."
    kil "Ah, damn! It didn't take long for him to rope you into that shit, huh?"
    kil "Squash, though? You pick that?"
    scene w3_6029 with dissolve
    mc "It was his idea."
    kil "Yeah, that makes sense."
    mc "I would've picked checkers or tic-tac-toe."
    kil "Well, he's got his claws in you now. FYI, I've been playing Go with him for years. He won't let you stop."
    scene w3_6030 with dissolve
    mc "It was fun. It reminded me of how I remembered him."
    scene w3_6031 with dissolve
    kil "Wet your whistle, have you?"
    scene w3_6032 with dissolve
    rose "...this is good stuff. Better than what I have at home."
    scene w3_6033 with dissolve
    mct "(...do I have to be concerned about her too now?)"

    if w3VeronicaSex == True:
        mct "(For that matter, I got hosed last night with Veronica. What am {i}I{/i} doing?)"

    scene w3_6034 with dissolve
    kil "Am I {i}really{/i} going to be the one dry here?"
    mc "Could I offer you some water?"
    scene w3_6035 with dissolve
    rose "Someone's got to be the responsible one."
    jump w3MinaKillsAMan


label w3MinaKillsAMan:
    play music "music/happy-clappy.ogg"
    scene w3_6036 with w19
    hana "Holy shit, this is heavy duty! You can shoot this thing?"
    mina "Yup! I shot in competitions."
    scene w3_6037 with dissolve
    hana "........."
    hana "......"
    scene w3_6038 with dissolve
    hana "...do you think you could kill a man with this?"
    scene w3_6039 with dissolve
    mina "What a morbid thing to ask!"
    scene w3_6040 with dissolve
    hana "Oh! Like you haven't thought about it!"
    scene w3_6039 with dissolve
    mina "I haven't!"
    scene w3_6040 with dissolve
    hana "Yes, you have. Don't lie!"
    scene w3_6041 with dissolve
    mina "........."
    mina "......"
    scene w3_6042 with dissolve
    mina "...here, let me see it."
    scene w3_6043 with dissolve
    hana "Okay... what are you--"
    scene w3_6044 with dissolve
    scene w3_6045 with dissolve
    hana "--!"
    scene minashot with dissolve
    show minakillsaman with dissolve
    $ renpy.pause(1.1, hard=True)
    stop music
    "*Flllhhich*"
    scene w3_6046 with dissolve
    mina "The problem would be the draw strength. It's only 30 pounds."
    mina "It's enough to collapse a lung if you nailed someone between the ribs, but not enough to cleanly kill a man unless you land the shot in the jugular or eye."
    scene w3_6047 with dissolve
    hana "HOLY SHIT! HOLY SHIIIIIT!"
    hana "That WAS cool!"
    play music "music/modern-situations.ogg"
    scene w3_6048 with dissolve
    mina "Hehehe, you think? I mean, it wasn't that far of a shot."
    hana "Fuck, if you were any cooler, I'd be pregnant right now."
    scene w3_6049 with dissolve
    mina "Okay, you're making fun of me right now."
    scene w3_6050 with dissolve
    hana "I am one hundred percent sincere."
    scene w3_6051 with dissolve
    mina "...ughh. Was this what I was doing to you? It's kinda embarrassing."
    hana "Well, don't abruptly shoot a mannequin in the throat if you don't want any compliments!"
    scene black with fade
    mina "...huh. I've never thought of it that way."
    jump w3ThreesCompanyToo

label w3ThreesCompanyToo:

    scene w3_6052 with circlewipe
    rose "Pffh, haaa-! Hehehe... stop it!"
    mc "C'mon, it wasn't that funny."
    rose "Well, {i}I'm{/i} laughing!"
    "Not knowing what to do, we sat around, availing ourselves of what was right in front of us."
    scene w3_6053 with dissolve
    rose "No, no, no... ah... it's just--"

    if feliciaFlag == True:
        "Myself, I just drank until I felt a light buzz. I had my evening with Felicia, after all."
    else:
        "Myself, I just drank until I felt a light buzz."

    "Rosalind prudently followed my pace, most likely on guard to avoid getting out of sorts around us."
    scene w3_6054 with dissolve
    mc "You're not the first one to remark that recently. I suppose there must be something to it."
    scene w3_6055 with dissolve
    kil "Oh, fuck you, Mr. Cool."
    "Ian? He stayed committed to the bit of not having anything to drink. God bless him."
    scene w3_6056 with dissolve
    mc "Oh, this is interesting."
    scene w3_6057 with dissolve
    rose "Oh, God. What is?"
    scene w3_6058 with dissolve
    mc "Your porn."
    scene w3_6057 with dissolve
    rose "It's not--"
    scene w3_6058 with dissolve
    mc "--his fingers slide in and out of my {b}quim{/b}, skewering any semblance of rationality I held."
    scene w3_6059 with dissolve
    mc "I mean, who would think to use the word \"quim\"? It's, uh... unsexy?"
    scene w3_6060 with dissolve
    kil "I mean, what the fuck even is a {i}quim?{/i}"
    scene w3_6061 with dissolve
    rose "Vagina! It's a vagina!"
    scene w3_6060 with dissolve
    kil "Why not just use the word pussy then? Or cunt? Or hell, {i}vagina{/i}?"
    scene w3_6058 with dissolve
    mc "Twat would work, but whatever you do, don't use the word \"cunny\" like right--"
    scene w3_6057 with dissolve
    rose "It's about contrast! You're taking something base and making it flowery, it's--"
    scene w3_6062 with dissolve
    mc "Every kiss that dotted my neck fanned the flames of my loins..."
    rose "Uggh, hearing it read aloud is just so-- uh oh, nope! No way! You're not ruining this for me! Stop it!"
    scene w3_6063 with dissolve
    mc "Pffh, no.. no... I'm not... this is {b}good{/b} stuff."
    scene w3_6064 with dissolve
    kil "I just don't understand how any of that is sexy. \"I'm a dirty slut,\" that's sexy, but..."
    scene w3_6065 with dissolve
    rose "It's art! And you've got no appreciation for it!"
    scene w3_6066 with dissolve
    "........."
    "......"
    "..."
    scene w3_6067 with dissolve
    rose "Pffh, haa, haaa... damn it... it is kinda-- it sounds better when you're horny, okay?!"
    kil "So you admit it's porn, then?"
    scene w3_6068 with dissolve
    rose "Mmmhhh... yeah... {b}God...{/b} Pff, hahaha...!"

    if rosalindKilSolution == True:
        scene w3_6069 with dissolve
        kil "That's a few times she's laughed. I think she likes us."
        mc "She probably thinks we're clowns."
        scene w3_6070 with dissolve
        rose "......"
        scene w3_6071 with dissolve
        rose "...well, you two aren't {i}bad{/i} company. It beats downing a bottle of wine by myself at my apartment."
        scene w3_6072 with dissolve
        kil "Oh? We aren't?"
        scene w3_6070 with dissolve
        "The mood abruptly changed, and I could easily read my friend's face."
        scene w3_6072 with dissolve
        kil "You know, Rosie... you're pretty when you laugh."
        scene w3_6070 with dissolve
        "He HAD found the moment to settle the matter of the five thousand dollars."
        scene w3_6073 with dissolve
        rose "......"
        scene w3_6074 with dissolve
        rose "...hmmmm."
        mc "Come on, she's always beautiful."
        scene w3_6075 with dissolve
        rose "Well, you two aren't so bad yourselves..."
        scene w3_6076 with dissolve
        "I'd give my friend this: he picked the moment. He wasn't forcing things."
        scene w3_6077 with dissolve
        kil "Which one of us do you find the most handsome?"
        scene w3_6078 with dissolve
        "It wasn't quite so cold... and despite my initial {i}whatever{/i} over his proposal, I currently wasn't feeling too weird about the prospect..."
        scene w3_6079 with dissolve
        rose "You really shouldn't ask questions that might hurt somebody's feelings."
        scene w3_6080 with dissolve
        "A simple touch to serve as a confirmation."
        rose "Not when we are feeling friendly, and you're both handsome boys."
        scene w3_6081 with dissolve
        "Confirmation that she felt it too: Ian's intention and the mood between the three of us."
        scene w3_6082 with dissolve
        mc "Sounds like she's trying not to hurt your feelings, Ian."

        if hanaGF == True:
            "Hana came to mind, but what could I do? Ian had put up the money, and ostensibly, this was {i}was{/i} club-related. If this was the time he chose..."

        scene w3_6083 with dissolve
        kil "Remember who Lucy picked, bro."
        rose "Heh! You two are..."
        scene w3_6084 with dissolve
        "Rosalind's expression was a difficult read, and there were more layers to it than I could ever hope to unpack from that quagmire of anticipation and transactional matter-of-factness."
        scene w3_6085 with dissolve
        "Similarly, Ian looked at me, trying to feel out if I was okay with this happening. Or, perhaps, was he trying to eyeball a plan of attack?"
        scene w3_6084 with dissolve
        mck "..."
        hide screen textbox2 with dissolve

        menu:
            "Beat him to the punch. Make the move yourself.":
                scene w3_6086 with dissolve
                mc "*Chwup~*"
                rose "Mmmh..."
                mc "Have you ever..."
                scene w3_6087 with dissolve
                rose "Of course not."
                mc "*Chwup*"
                scene w3_6088 with dissolve
                mc "Same. Never, ever..."
                "I kept my voice to a whisper, as if Ian wasn't leering at both of us with an elated smile."
                scene w3_6089 with dissolve
                rose "Mmmhh-"
                mct "(Enjoy the show, weirdo.)"
                scene w3_6090 with dissolve
                mc "Let's enjoy ourselves."
                rose "Good plan..."
            "His money. Let Ian do it.":

                scene w3_6091 with dissolve
                kil "Well, someone's got to do it."
                scene w3_6092 with dissolve
                rose "Heh, you're finally--"
                scene w3_6093 with dissolve
                rose "Mmmh...?!"
                "Roughly, my friend grabbed Rosalind, full of gusto and passion."
                scene w3_6094 with dissolve
                "Along with his tongue being shoved down her throat, so did the malty contents of his mouth."
                rose "Mmh, hhh-"
                scene w3_6095 with dissolve
                kil "Now... If you tell Victoria about {b}this{/b}, I'll have to go into details of what we were doing..."
                scene w3_6096 with dissolve
                mc "Fair point."
                rose "A-ah... geez... your plan is to get a girl drunk, huh?"
                scene w3_6097 with dissolve
                kil "We'll go with that if it makes you feel better."

        scene w3_6098 with dissolve
        show screen textbox2 with dissolve
        rose "I'm... uh... you boys sit tight."
        rose "I'm going to go... uh... {i}freshen up.{/i}"
        scene w3_6099 with dissolve
        kil "Don't take too long."
        stop music fadeout 3.0
        scene w3_6100 with dissolve
        "........."
        scene w3_6101 with dissolve
        "......"
        scene w3_6102 with dissolve
        kil "...damn, bro. We're fucking smooth."
        play ambient "sound effects/ringing-inbound.wav"
        scene w3_6103 with dissolve
        mc "Don't forget you're paying--"
    else:
        scene w3_6070 with dissolve
        rose "....."
        scene w3_6071 with dissolve
        rose "...you two don't make for bad company. It sure beats downing a bottle of wine by myself at my apartment."
        scene w3_6105 with dissolve
        mc "That a regular thing for you?"
        scene w3_6075 with dissolve
        rose "More so recently. Only way I can find time to relax..."
        rose "Maybe I'll order those burgers again tonight."
        scene w3_6105 with dissolve
        mc "Anything you'd like."
        scene w3_6104 with dissolve
        rose "Thanks, [mcf]. And thanks both of you for making me laugh."
        scene w3_6075 with dissolve
        rose "You guys are cute."
        scene w3_6106 with dissolve
        kil "Nah, we're manly as fuck!"
        scene w3_6107 with dissolve
        rose "You sure? You have the hairstyle of someone in a Korean boy band."
        kil "You, uh--"
        scene w3_6108 with dissolve
        mc "{b}Ha!{/b} Bahaha!"
        "Yeah. She seemed comfortable."
        "{b}Good.{/b}"
        scene w3_6100 with dissolve
        rose "I'm going to go take a hot shower."
        mc "Enjoy."
        stop music fadeout 3.0
        scene w3_6109 with dissolve
        "........."
        "......"
        play ambient "sound effects/ringing-inbound.wav"
        scene w3_6110 with dissolve
        kil "...well, that was sad--"

    jump w3DariusCall

label w3DariusCall:
    scene w3_6111 with dissolve
    kil "Uh, who is it? Is it the factory?"
    mc "Unknown number."
    stop ambient
    play sound "sound effects/phonemenu.wav"
    scene w3_6112 with dissolve
    mc "Hello?"
    scene w3_6113 with dissolve
    woman "Who am I speaking to?"
    "It was a woman's voice, different from the receptionist, pointed and clear."
    hide screen textbox2 with dissolve

    menu:
        "[mcf]":
            play music "music/landing.ogg"
            scene w3_6112 with dissolve
            show screen textbox2 with dissolve
            mc "This is [mcf]."
            scene w3_6113 with dissolve
            "A simple question. One I'd been asked and had answered countless times, and thus I blurted out the truth with no thought of subterfuge."
            woman "[mcf], who?"
        "Lie about your name. (w3DariusFakeName = True)":
            $ w3DariusFakeName = True
            play music "music/landing.ogg"
            scene w3_6112 with dissolve
            show screen textbox2 with dissolve
            mc "My name is... {i}Charles.{/i}"
            scene w3_6113 with dissolve
            woman "Charles, who?"

    scene w3_6114 with dissolve
    show unknown-call with dissolve
    mc "Sorry, but {b}who{/b} am {i}I{/i} speaking to?"
    "......"
    woman "...I'm sorry. I'm being rude."
    woman "You called, asking to speak to my husband. My name is Stella Lee."
    mc "You're Darius' mother?"
    stella "I am. Is Darius alright?"
    "Her question was a good sign; it told me she hadn't had cause to look for him and that my call added something unordinary to the equation."
    mc "I'm a friend of his, looking to get back in touch. I was just wondering if you had heard from him any time over the last few months?"
    "...but it was best to be careful with my words, lest I give her a cause for concern."
    mc "You see, he moved out of the city and the number I have for him doesn't seem to be in use anymore."
    stella "...I'm afraid I won't be any help for you there. We haven't spoken in months."
    mc "...if you don't mind me asking, is that unusual?"
    stella "You said you're a friend?"
    mc "And former co-worker."
    stella "Ah, well... I wish it was out of the ordinary, but in the eight years since I last saw him, we've probably only spoken about a dozen times. He didn't leave home on the best of terms."
    "As she chewed over her thoughts, her voice gradually dipped down to a contemplative whisper."
    stella "The few, precious times we've talked since then have been on his terms."
    mc "...and when {i}was{/i} the last time you spoke to him?"
    "She paused in recollection."
    stella "That was six months and two weeks ago."
    mc "Exactly? Wow."
    "According to the timeline, as I knew it, that was {b}BEFORE{/b} he split town."
    stella "I remember because it's a relief every time we do talk. I... {b} miss him.{/b}"

    if w3DariusFakeName == True:
        stella "...the last time you saw him, was he doing alright, Charles?"
    else:
        stella "...the last time you saw him, was he doing alright, [mcf]?"

    stella "Darius wasn't too skinny, was he? He always had trouble putting on weight..."
    mc "Ah, ummmm.... I'm actually here with another friend of his. I'm going to put you on speaker, alright?"
    play sound "sound effects/phonemenu.wav"
    scene w3_6115 with fade
    "*Beep*"
    scene w3_6116 with dissolve
    mc "Hey, Mrs. Lee is wondering how Darius looked the last time you saw him."
    scene w3_6118 with dissolve
    kil "Oh, uh... he was cutting up, laughing."
    scene w3_6117 with dissolve
    mc "Was he looking skinny?"
    scene w3_6119 with dissolve
    kil "Was he...? Nah, he was getting pretty chubby!"
    scene w3_6120 with dissolve
    stella "Was he really?!"
    scene w3_6119 with dissolve
    kil "Oh, yeah. Dude packed it in."
    scene w3_6117 with dissolve
    stella "That's... ah... it's good knowing he has friends worried about him."
    "......"
    scene w3_6121 with dissolve
    "..."
    scene w3_6122 with dissolve
    stella "So he... moved again? Morehead Hills, wasn't it?"
    scene w3_6123 with dissolve
    mc "Yeah. Up and left, with not even a goodbye."
    scene w3_6122 with dissolve
    stella "I think that's the longest he stayed in one place... he must've liked it there."
    scene w3_6123 with dissolve
    mc "...you don't think we have anything to worry about? I mean, he just quit his job without saying anything."
    scene w3_6122 with dissolve
    stella "{b}I'm{/b} going to worry, {i}of course{/i}... but it's what he does."
    scene w3_6124 with dissolve
    "It was hard to imagine that type of relationship with your own son. My stomach lurched at the thought of how my own mother might feel if she hadn't heard from me in months with no idea where I was."
    stella "Can you tell me what kind of life Darius had there?"
    scene w3_6126 with dissolve
    mc "That, uh..."
    scene w3_6125 with dissolve
    "{i}This call wasn't a good idea, was it?{/i}"
    scene w3_6126 with dissolve
    mc "...what kind of life he lived?"
    scene w3_6127 with dissolve
    stella "Please. Anything. Even what his favorite place to eat was."
    scene w3_6128 with dissolve
    kil "He, uh..."
    scene w3_6129 with dissolve
    "Ian tried to paint Darius' mother a picture, leaving out some pertinent details. I think she knew he was being purposely flimsy, but she was so starved for contact with her son that she graciously accepted it."
    "Meanwhile, she shared some things with us. The various places she knew he'd been over the years and little nuggets about his character."
    "{i}The things she missed.{/i} Things that helped further my vague impression of the man. Things that, for better or worse, humanized my predecessor and his predicament."
    "After talking for a few minutes, I had to ask..."
    scene w3_6130 with dissolve
    mc "...how can you tolerate not even knowing what state he's in?"
    scene w3_6131 with dissolve
    stella "Well... what else can I do, other than get used to it?"
    "Sad, but accepting. Like a woman who's already mourned a loss."
    scene w3_6130 with dissolve
    mc "...when you hear from him, would you give me a call, please?"
    scene w3_6131 with dissolve
    stella "Sure. I have your number."
    scene w3_6132 with dissolve
    mc "Thanks. It was nice talking to you, Stella."
    scene w3_6133 with dissolve
    "And that was that. This cleared {b}nothing{/b} up."
    scene w3_6134 with dissolve
    mc "Well, this was a dead end."
    scene w3_6136 with dissolve
    "The two of us looked at each other, disappointed and fully aware that this wasn't a good idea."
    scene w3_6135 with dissolve
    kil "His mother seemed like a nice lady..."
    scene w3_6134 with dissolve
    mc "Do you think she was covering for him?"
    scene w3_6133 with dissolve
    "The thought crossed my mind..."
    mct "(If Darius had fled with blackmailed money, his mother could be covering his tracks...)"
    scene w3_6138 with dissolve
    kil "Anything's possible..."
    scene w3_6137 with dissolve
    mc "What do we do now?"
    scene w3_6138 with dissolve
    kil "We should try to find Isla. If she's still in the city, it means they didn't run off together."
    scene w3_6133 with dissolve
    "There was no uncertainty in his suggestion. {i}This{/i} was what he wanted to do."
    scene w3_6138 with dissolve
    kil "Dalia might know how to contact her, assuming you still want to look into this."
    scene w3_6134 with dissolve
    mc "...do you?"
    scene w3_6135 with dissolve
    kil "His mother seemed like a nice lady. That's all I'm saying."
    stop music fadeout 3.0
    scene w3_6136 with dissolve
    "......"
    "..."
    "Like when we were kids, we didn't need to say anything else. We were on the same page."
    "If our wildest imaginations turned out to be true, we were in for a moral reckoning and for possibly learning some uncomfortable truths about ourselves."

    hide screen textbox2 with dissolve

    if rosalindKilSolution == True:
        jump w3TalkingAboutCeasar

    elif feliciaFlag == True:
        play music "music/crinoline-dreams.ogg"
        scene w3_6139 with dissolve
        kil "You have any plans for today?"
        scene w3_6140 with dissolve
        "However, not one to endure an uncomfortable silence, my friend switched gears."
        scene w3_6141 with dissolve
        mc "Some art thing with Felicia."
        scene w3_6142 with dissolve
        kil "You're seeing her socially?"
        scene w3_6143 with dissolve
        mc "I hadn't really put it in old man terms like that, but it would seem so, huh? Are you going to tell me that's a bad idea?"
        scene w3_6144 with dissolve
        kil "Shit, man. I was the one who set you up with her in the first place. I'm not worried about that crazy bitch playing you like the other girls."
        scene w3_6143 with dissolve
        mc "Awww, you're worried about the others? That's nice."
        scene w3_6144 with dissolve
        kil "I mean, if you ran off with some hooker, it'll be my fault. What will I tell Victoria?"
        scene w3_6143 with dissolve
        mc "Ha! In some ways, you're more of a nervous nelly than I am ."
        scene w3_6145 with dissolve
        kil "I've seen you worry that an e-mail didn't actually send!"
        mc "It was an important e-mail."
        kil "You checked the receipts three times!"
        scene w3_6146 with dissolve
        mc "...enough about me. What are you going to get up to?"
        scene w3_6142 with dissolve
        kil "Uh... I don't know. I'm due for a nap and I think I should spend some quality time alone for once."
        scene w3_6147 with dissolve
        mc "What's got you sayin' that??"
        scene w3_6148 with dissolve
        kil "I should probably rethink all that \"coked up\" behavior of Darius that I wrote off."
        scene w3_6147 with dissolve
        mc "Don't wallow too deep, my dude."
        scene w3_6148 with dissolve
        kil "No worries. Who do you think I am? You?"
        scene w3_6149 with dissolve
        mct "(Hmm... I should probably shoot Felicia a text and see what's up)"
        scene w3_6147 with dissolve
        mc "I'm just saying you need to start taking better care of yourself, dude. More sleep and less drinking."
        scene w3_6150 with fade
        rose "Hey, if I made some peanut butter cookies, would you boys eat some? I'm getting a craving."
        scene w3_6151 with dissolve
        kil "What kind of question is that? Hell yeah."
        scene w3_6150 with dissolve
        mc "Heh. You don't stop, do you?"
        scene black with fade
        stop music fadeout 3.0
        "......"
        "..."
        jump w3FeliciaMeet1
    else:

        play music "music/crinoline-dreams.ogg"
        scene w3_6139 with dissolve
        kil "You have any plans for today?"
        scene w3_6140 with dissolve
        "However, not one to endure an uncomfortable silence, my friend switched gears."
        scene w3_6141 with dissolve
        mc "Nah. Think I'm just going to stay in. What about you?"
        scene w3_6142 with dissolve
        kil "Uh... I don't know. I'm due for a nap and I think I should spend some quality time alone for once."
        scene w3_6147 with dissolve
        mc "What's got you sayin that??"
        scene w3_6148 with dissolve
        kil "I should probably rethink all that \"coked up\" behavior of Darius that I wrote off."
        scene w3_6147 with dissolve
        mc "Talking to his mother got to you, huh?"
        scene w3_6148 with dissolve
        kil "I think your anxiousness is rubbing off on me."
        scene w3_6147 with dissolve
        mc "Don't wallow too deep, my dude."
        scene w3_6148 with dissolve
        kil "No worries. Who do you think I am? You?"
        scene w3_6147 with dissolve
        mc "I'm just saying you need to start taking better care of yourself, dude. More sleep and less drinking."
        scene w3_6150 with fade
        rose "Hey, if I made some peanut butter cookies, would you boys eat some? I'm getting a craving."
        scene w3_6151 with dissolve
        kil "What kind of question is that? Hell yeah."
        scene w3_6150 with dissolve
        mc "Heh. You don't stop, do you?"
        scene black with fade
        stop music fadeout 3.0
        "......"
        "..."

        if w3VeroBarDate == True:
            jump w3June17MiddayMontage
        else:
            jump w3June17End

label w3TalkingAboutCeasar:
    $ w3MCThreesomeCherryPopped = True
    scene w3_6152 with dissolve
    "However, my friend's mind clearly {i}turned{/i} to the {b}other{/b} thing."
    scene w3_6153 with dissolve
    kil "Enough anxious shit. Let's focus on now, eh?"
    scene w3_6154 with dissolve
    mc "You're {i}way{/i} too into this."
    scene w3_6155 with dissolve
    kil "I'm the {i}right{/i} amount into demolishing a {b}big-tittied{/b} MILF with his bro. Shall we go see how Rosie is faring?"
    scene w3_6154 with dissolve
    mc "She said to sit tight."
    scene w3_6153 with dissolve
    kil "How can I when I feel like it's Christmas morning?"
    scene w3_6156 with dissolve
    rose "Time to open your present, boys."
    mc "Hmmm?"
    play music "music/too-cool.ogg"
    scene w3_6157 with wipeleft:
        subpixel True
        yalign 1.0
        xalign 0.6
        linear 5 yalign 0.15
    rose "{i}GOD{/i} that sounded better in my head... heh..."
    "Lo' and behold, Rosalind had crept down the stairs and stood before us clad in black lace, ready to do battle."
    scene w3_6158 with dissolve
    kil "Ho, ho, ho--"
    "My friend let out an impressed whistle, while an unnecessary question formed on my lips."
    mc "You packed that?"
    scene w3_6159 with dissolve
    rose "I thought it might come in use..."
    scene w3_6160 with dissolve
    kil "You're oooooone smart cookie, Rosie."
    kil "I couldn't have picked something better myself..."
    scene w3_6161 with dissolve
    rose "Uh, thanks, I think... I'm glad you like it?"
    scene w3_6162 with dissolve
    kil "Oh, we {i}love{/i} it, don't we?"
    scene w3_6163 with dissolve
    mc "No disagreement here."
    "Sheer as it was, it didn't just leave nothing to the imagination."
    "The accentuated hipline and bust were so damn eye-pleasingly vulgar that it made my balls {i}ache{/i} from anticipation alone."
    scene w3_6164 with dissolve
    rose "Hnnggg..."
    "Meanwhile, Ian's fingertips casually grazed Rosalind's concealed nipple, eliciting a shudder from the teat-weak brunette."
    scene w3_6165 with dissolve
    kil "You thought about {i}this{/i} while getting ready, didn't you?"
    scene w3_6166 with dissolve
    rose "Well... I mean... {i}duh?{/i}"
    scene w3_6165 with dissolve
    kil "The thought of two young men not being able to keep their hands off you... like you're the center of the fucking universe..."
    scene w3_6166 with dissolve
    rose "Well, uh..."
    scene w3_6167 with dissolve
    mc "Duh?"
    "Working in tandem was new to me, but I did what came naturally. While it {i}was{/i} Ian's show..."
    scene w3_6168 with dissolve
    "I wasn't going to sit on the sidelines."
    scene w3_6169 with dissolve
    rose "Maybe... and now..."
    "The flustered look on her face made it evident, but the unsubtle way she pushed out her chest made it clear."
    rose "Seems you boys have me {b}cornered{/b}, huh?"
    "{i}She wasn't feeling cold about this.{/i}"
    scene w3_6170 with dissolve
    kil "Yeah, {b}we do{/}. And you're going to do EVERYTHING we say. {b}Got it{/b}?"
    scene w3_6171 with dissolve
    "Rosalind confirmed with a faint, jittery nod."
    scene w3_6170 with dissolve
    kil "Don't just nod. Let's be clear on it..."
    scene w3_6172 with dissolve
    rose "...I'll do anything either [mcf] or you ask me to, Ian."
    scene w3_6170 with dissolve
    kil "...and do you know why you'll play the perfect {i}cumdump{/i} for us?"
    scene w3_6172 with dissolve
    rose "...because you gave me money?"
    scene w3_6173 with dissolve
    kil "Nah! Wrong! It's because if you do everything we ask, [mcf] and I... well..."
    scene w3_6174 with dissolve
    kil "We're going to redefine what you think \"getting fucked\" means."
    kil "You see... next time you shag some boring old prick, {i}you'll think of us.{/i} The next time you crack open one of those books? {b}Us{/}."
    kil "So, you'll do everything [mcf] and I ask you to, yeah?"
    scene w3_6175 with dissolve
    rose "That, uh--"
    "Rose's voice caught in her throat as her eyes darted between Ian and I."
    scene w3_6176 with dissolve
    rose "If you manage to pull it off... that might be pretty {i}okay{/i}."
    scene w3_6177 with dissolve
    "Ian leveled a conspiratorial smile my way, and I felt... weird. Outnumbering a woman felt... {i}good.{/i}"
    scene w3_6178 with dissolve
    mc "Just okay, Rose?"
    scene w3_6179 with dissolve
    mct "(When in Rome...)"
    scene w3_6180 with dissolve
    rose "...what's wrong with okay?"
    "Thankfully, it only took a measly glance for Ian to pick up where I was going with this."
    hide screen textbox2 with dissolve
    scene w3_6181 with dissolve
    "As I stood pressed chest-to-chest with the busty mother, Ian swept in and sandwiched her between us."
    scene w3_6182 with dissolve
    mc "I mean, we're about to give you the best sexual experience of your life and all you've got for us is a {i}pretty{/i} okay?"
    "Pressed body-to-body-to-body, groin-to-groin-to-groin, I built on my friend's bravado."
    "And as the outline of our bulges pushed into the nearly bare flesh of her thighs and ass..."
    scene rosa_3s01_a with dissolve
    show rosa_3s01 with dissolve
    rose "*Gulp* Ahh...."
    "Everything became hot all of a sudden."
    rose "Why..."
    "Was it me?"
    "Was it Ian?"
    "Was it Rose herself?"
    rose "Aahh... heheh..."
    "Whoever it may have been, it only took one person before our individual neediness became shared."
    rose "Fuck, I actually believe you boys..."
    "Hands and crotch and thighs and legs mashed into each other as if trying to impossibly join together."
    scene w3_6183 with dissolve
    rose "I could do a {b}firm{/b} okay. But, if I may be so bold, um..."
    scene w3_6184 with dissolve
    "Her submission came out thin, husky, and heavy with anticipation."
    scene w3_6183 with dissolve
    rose "...what are you waiting for?"
    scene w3_6185 with dissolve
    kil "Ha! How's an old bitch like you so cute?"

    scene w3_6186 with dissolve

    if w3AliceOffer == True:
        "Unlike Alice, Rosalind showed no qualms in admitting her desire."
    else:
        "Rosalind showed no qualms in admitting her desire."

    scene w3_6185 with dissolve
    kil "And what would you have us do?"
    scene w3_6187 with dissolve
    rose "{i}Get undressed.{/i}"
    scene w3_6188 with dissolve
    mc "...and then what?"
    scene w3_6187 with dissolve
    rose "And then... well..."
    stop music fadeout 3.0
    scene black with fade
    "......"
    "..."
    play ambient "sound effects/fel4.wav"
    rose "Eehh? Hmm? *Chwup, sshhluwwwwup!*"
    mc "Aaaah... watch the foot, please! Those things are like daggers!"
    play music "music/six-days-of-heat-pt2.ogg"
    scene rosa_3s02_a with wipedown
    show rosa_3s02 with dissolve
    "Quickly, we found ourselves upstairs, limbs tangled and mouths preoccupied."
    "It was awkward at first, three people bidding for position, but we soon found our roles buried between each other's thighs."
    kil "Ah, hot damn-"
    "Rosalind wasted no time wrapping her bronze-painted lips around my friend's cock."
    rose "*Plhhah, chwwup!*"
    "The busty brunette bobbed her head up and down at a pleasant pace, steadily stimulating my friend's glans."
    hide screen textbox2 with dissolve
    scene rosa_3s03_a with dissolve
    show rosa_3s03 with dissolve
    kil "Fuckin' A, I've been looking forward to this."
    "There was something different in Ian's tone. Despite the crass way he put it..."
    kil "You better not disappoint {i}either{/i} of us, Rosie."
    rose "Mmh, uhummm...!"
    kil "So, uh... ahh... {b}work hard{/b}, eh?"
    "It lacked the usual edge he had when dealing with whores."
    rose "Mmh, mmhhh..."
    "Instead, between every arrested word was arousal, and whose inflection read more like an emphatic plea."
    kil "Don't forget who owns your cow ass!"
    mct "(--or {b}maybe{/b} not.)"
    rose "Eeauhhmm...♥"
    "And meanwhile, with a tight grip on my hair..."
    scene rosa_3s05_a with dissolve
    show rosa_3s05 with dissolve
    rose "Yeeuhh...♥"
    "Rosalind \"Fuckin' A'd\" my own diligent efforts at exploring her insides."
    kil "Ah, fuckin' bitch..."
    "Just like she was, I took it nice, easy, and steady, folding my tongue and prying her open on a mission to loosen up her soon-to-be cock-stuffed hole for entry."
    kil "{size=+10}Keep doing what you're doing down there, bro!{/size}"
    mct "(I can hear you just fine, moron...)"
    "Still, my friend's egging on inspired in me something {i}novel.{/i}"
    rose "Mhhh...♥♥ *Chwup, fwhhhup-*"
    "Each pleasant plap of Rosalind's cock-sucking lips that got passed down to my ears acted as encouragement."
    kil "She's getting more into it!"
    "Part of me envisioned, as if I was the engine of it all, spurring Rosalind's lust and driving her deeper down Ian's cock--"
    scene rosa_3s04_a with dissolve
    show rosa_3s04 with dissolve
    rose "Ahhhmm... *schlick, schluck-!"
    "--the three of us working in precise concert like the movement of a wristwatch."
    kil "Ha! Shit, I, uh..."
    mct "(Yeah...)"
    kil "...I don't know what to do with my hands!"
    "{i}There was something to that, I thought.{/i}"
    rose "Mhh, shhh- *Cwhup, kwhhup!*"
    "Something that might only exist while I was buried nose deep in Rosalind's quim."
    "Something that would likely go back to just being weird once the cum oozing from Rosalind's orifices turned cold."
    mct "(...{i}no homo.{/i})"
    kil "Ha, guess I'll just keep running my mouth then!"
    scene rosa_3s02_a with dissolve
    show rosa_3s02 with dissolve
    "And, naturally, Rosalind and I left the idle playboy to his own musings."
    rose "Ehhuhh... *Swhhup, chwwup-♥*"
    "Instead, we toiled away: Rosalind working my friend's frenulum and making sure he got his money's worth, while I prepped for my own gratification."
    "Maybe for a minute, before-"
    kil "Ah, fuck, man...!"
    stop ambient
    $ renpy.music.set_volume(0.1, 0, channel = "music")
    scene w3_6189 with fade
    kil "A-ah... let's switch it up, huh?"
    scene w3_6190 with dissolve
    kil "What do you think?"
    "Lost in my own devices, it took a moment for the question to register."
    mct "(What did I think?)"
    "As I peered up at my friend from this awkward angle, making eye contact with him through the valley of Rosalind's prodigious bounty..."
    "{i}What did I think?{/i}"
    scene black with fade
    "I thought one thing."
    scene w3_6191 with fade
    rose "B-boys... t-there isn't really any need--"
    scene w3_6192 with dissolve
    mc "You don't want us to?"
    scene w3_6191 with dissolve
    rose "Well, I..."
    scene w3_6193 with dissolve
    rose "......"
    scene w3_6194 with dissolve
    rose "..."
    scene w3_6195 with dissolve
    rose "O-ohh...!"
    "My thumb lazily flittered across her clitoral hood with a light touch."
    rose "I- I, uh... I didn't say that did I?"
    scene w3_6196 with dissolve
    rose "H-hello!"
    "And just as slowly, I sank two of my digits into Rosalind's welcoming hole. "
    scene w3_6197 with dissolve
    kil "What's the problem then?"
    scene w3_6198 with dissolve
    mc "I've learned from the past couple of days that she doesn't like sitting on her hands."
    rose "Mmmhh...♥ It's not that boys... it's just--"
    scene rosa_3s06_a with dissolve
    show rosa_3s06 with dissolve
    rose "Ah, haaa...♥ "
    "Having waited for just the right moment, I began my delicate strumming."
    rose "I-isn't it {i}boring{/i} for you two if I'm not doing anything?"
    "Rosalind's insides gripped me readily, burning the edges of my fingernails with hot sticky need."
    kil "Aw, the prostitute is thinking of {i}our{/i} fun right now. That's sweet..."
    rose "...heh, aren't I nice? Ahaaa..."
    kil "Well, don't worry, Rosie. It's fun watching you moan."
    rose "{i}Of course{/i} it is... {b}why wouldn't it be?{/b} Hnnngg--"
    "Her feigned exasperation might've been convincing if it wasn't for..."
    mc "She's feeling it, dude."
    scene rosa_3s09_a with dissolve
    show rosa_3s09 with dissolve
    "Quickly, Rosalind's pleasure point revealed itself and fattened against the base of my thumb."
    kil "No shit, she is."
    rose "Ah... hhuuuuhh... y-you boys..."
    kil "Prattling on about {i}our{/i} fun, yet what she really wants is to just go ahead and get stuffed?"
    rose "Eyeee..."
    mc "Kinda shameless, if you ask me."
    rose "No more than you--"
    scene w3_6199 with vpunch
    rose "Oh, hhmmm-♥♥"
    kil "I didn't know you played an instrument."
    "A jolt of pleasure rendered whatever point she was about to make ineffective and moot."
    scene w3_6200 with dissolve
    rose "Ghh, h-huhh...♥ Yheeur..."
    kil "Listen~ to~ that~ teapot~ hum~"
    scene rosa_3s06_a with dissolve
    show rosa_3s06 with dissolve
    rose "A-hh, ohh fuggg...♥"
    "Being back-against-the-wall, with two strapping men bearing down on her was {i}really{/i} getting to her..."
    kil "{b}Dirty bitch.{/b}"
    "The way her cunt tried to milk my fingers pretty much confirmed it."
    mc "--his fingers slide in and out of my {b}quim{/b}, skewering any semblance of rationality I held."
    kil "Ha! Nice! Like in one of her porn--"
    rose "Mmmhh, they're not porn--! "
    scene w3_6200 with dissolve
    rose "S-stupids...♥ J-just...♥"
    "As she was berated on both sides, glibly chided and ganged up on, Rosalind once more offered her chest."
    scene w3_6201 with dissolve
    rose "Shut up and put those mouths to better use."
    $ renpy.music.set_volume(1, 0, channel = "music")
    scene rosa_3s07_a with dissolve
    show rosa_3s07 with dissolve
    "{i}She got it{/i}."
    "Like starving wolves, we dove into the panting woman's chest, salivating and eager."
    rose "Mmmhhh...♥ Oh-♥♥"
    "Oh yeah, {b}She got it{/b}."
    rose "G-god...♥"
    "{i}Licking, and sucking, poking, and rubbing...{/i}"
    rose "Fhuuooow...♥ H-ha...♥♥"
    "Rosalind immediately fell under a spell."
    rose "Good {b}boys...!{/b}"
    "She called out incoherently, drunk on pleasure, yet fully aware that she was weaponizing her motherly charms."
    scene rosa_3s08_a with dissolve
    show rosa_3s08 with dissolve
    rose "Oh... ohhh...♥ D-damn it, you two...!"
    "She {b}pointedly{/b} moaned into our ears."
    rose "Hnnggg...♥"
    "...or maybe no thought at all was given to that sweet encouragement."
    rose "Bhhhoyss...♥ A-ahhh...♥♥"
    scene rosa_3s07_a with dissolve
    show rosa_3s07 with dissolve
    "Either way, under a joint assault, the awkwardness of \"sitting on her hands\" evaporated into lewd fuck sounds."
    rose "Haa, haaat-♥♥"
    "Her chest heaved and her breath was cleaved in pleasure."
    rose "Ah, hhhh- shhhoot...!"
    mct "(Ha! That's...!)"
    scene w3_6203 with pixellate
    mc "Is the coast clear?"
    scene w3_6204 with dissolve
    kil "No Alice in sight!"
    scene w3_6203 with dissolve
    mc "Good, keep lookout. I'll grab the goods."
    scene w3_6204 with dissolve
    kil "I think it's in her closet..."
    scene w3_6203 with dissolve
    mc "If we get caught, it was my idea, okay?"
    scene w3_6204 with dissolve
    kil "No way! We go down together!"
    scene w3_6203 with dissolve
    mc "Just listen to what I say! She can't punish me!"
    scene rosa_3s07_a with pixellate
    show rosa_3s07 with dissolve
    "That's fuckin' {b}team work!{/b}"
    rose "Ahh, hhha, haat! Oh- ohh-♥"
    mct "(Our mission to get Ian's games back...)"
    rose "Ohh, umm... b-boys.... gahhh...!"
    "This was as strange a mix of emotions as I'd ever felt, the delirious sounds of Rosalind's pending release mingling with a sudden rush of nostalgia."
    scene rosa_3s09_a with dissolve
    show rosa_3s09 with dissolve
    rose "B-boys... I don't think I... I can't control it...!"
    mct "(Can't control it...?)"
    "Her warning didn't phase either of us."
    mct "(Is that what they mean when they say two heads are better than one?)"
    rose "N-no, s-seriously-!"
    "Things were about to get wet. We both knew it, and her growing concern over her incontinence didn't warrant pause."
    scene rosa_3s07_a with dissolve
    show rosa_3s07 with dissolve
    rose "Haaa, haaaa...♥ {size=+15}Haaaaat-♥♥♥♥♥{/size}"
    "No, it spurred us on."
    rose "Ah, f-fine then!"
    "I could tell."
    rose "Dddd-dhon't say I dh-didn't warn yhouuuuh..."
    "We could tell."
    "She was on the precipice, and--"
    scene w3_6205 with vpunch
    rose "Oh, ohh-"
    rose "Oh, hhhooo-"
    scene w3_6206 with dissolve
    rose "Euguuuugghh--"
    stop music
    play sound "sound effects/spurt.wav"
    scene w3_6207 with flash
    rose "Hwwwwaaaaahhhhhhhhhh-♥"
    "{i}She blew.{/i}"
    play sound "sound effects/spurt.wav"
    scene w3_6208 with flash
    "{b}Team work.{/b}"
    kil "Holy shit, she's still going."

    if w3VeronicaSex == True:
        mc "...I think {b}now{/b} we're even on the couch thing."
    else:
        mc "No kidding..."

    "Rosalind gushed like a fountain, making a mess of my sheets."
    scene w3_6209 with dissolve
    rose "A- ahhh... eeugughh..."
    kil "Is it over?"
    mc "Yeah, I think it's--"
    play sound "sound effects/spurt.wav"
    scene w3_6210 with flash
    rose "Geh, eeuugghhh..."
    mc "...over."
    scene black with fade
    kil "Damn, dude you're a fucking maestro!"
    "......"
    "..."
    play music "music/too-cool.ogg"
    scene w3_6211 with dissolve
    rose " I don't think, uh... ahh... heheh..."
    "Eventually, the signs of intelligence resurfaced in Rosalind's blue eyes."
    scene w3_6212 with dissolve
    rose "...oh, g-gimme a second, would you?"
    "And so, {b}for a second{/b}, we smugly basked in our combined handiwork while Rosalind collected herself in a puddle of her own urine."
    "........."
    scene w3_6213 with dissolve
    rose "You boys are off to a good start with that promise..."
    scene w3_6214 with dissolve
    mc "We'll take some credit, but that was A LOT of you..."
    "{i}Literally and figuratively speaking.{/i}"
    scene w3_6215 with dissolve
    rose "Hehe.. heh... yeah, heh, I'd say..."
    rose "Oh, and for the record, I gave fair warning so I'm not cleaning any of that up."
    scene w3_6216 with dissolve
    mck "Pft-!"
    rose "Hehehehe..."
    "As we shared a brief laugh, things felt a little cozy, but..."
    scene w3_6217 with dissolve
    "...as the silence grew, with cocks standing free and Rosalind laying exposed, our minds returned to more dirty expectations."
    scene w3_6218 with dissolve
    rose "Come on, boys..."
    "Rosalind spread her legs invitingly, showing an initiative far beyond the cold submission she puts on for the club."
    scene w3_6219 with dissolve
    kil "Wider, you fuckin' slut."
    scene w3_6220 with dissolve
    "......"
    scene black with fade
    "..."
    mc "Shouldn't you go first? You're the one who-"
    scene w3_6221 with wiperight
    kil "Be my guest, bro."
    scene w3_6222 with dissolve
    "As my friend smiled like an idiot, Rosalind squirmed beneath me in hushed anticipation."
    scene w3_6221 with dissolve
    kil "But before you get cracking..."
    scene w3_6223 with dissolve
    kil "Beg for my friend to fuck you, bitch."
    scene w3_6225 with dissolve
    "The motherly woman paused, eyes turned upward at the two men looming over her with dicks at the ready, as if conjuring the right emotion."
    scene w3_6226 with dissolve
    rose "{i}Please{/i}, {size=+15}{b}please{/b}{/size} give me your strong, young cock."
    scene w3_6227 with dissolve
    "...and delivered an appropriately patronizing declaration doused in {i}just{/i} enough feeling that it made my dick twitch in excitement."
    scene w2_8149 with pixellate
    show screen camcorder
    mc "You are one hell of an actress, Rosie..."
    rose "This isn't a performance, [mcf]..."
    hide screen camcorder
    scene w3_6226 with pixellate
    rose "Put it in, and you'll see just how much I mean it..."
    scene w3_6227 with dissolve
    "The expression she hit me with was irrefutable."
    scene w3_6226 with dissolve
    rose "{i}Please.{/i}"
    stop music fadeout 3.0
    scene w3_6227 with dissolve
    "She may have been bought and paid for like a prostitute, but she was speaking as a woman."

    menu:
        "Indulge her.":
            scene w3_6228 with dissolve
            rose "Ah, h-here we go..."
            scene w3_6229 with dissolve
            "The moment I slipped inside, Rosalind's inner walls stuck to my dick like glue, refusing retreat."
            rose "Deeper, [mcf]...♥"
            scene w3_6231 with hpunch
            "The way she spoke that single word, the way she paired it with my name--"
            play music "music/drum-bass.ogg"
            scene rosa_3s10_a with dissolve
            show rosa_3s10 with dissolve
            rose "--eeughddeeeep~♥ H-hehh...!"
            "--filled me with the explosive urge to drive forward into Rosalind's hold, in an effort to skewer both Rosalind and her words."
            rose "Ohh- your d-dick, ha...♥"
            "And so, Rosalind cried out, possessed by the moment; belting a tune perfectly suited for a woman eager to be ravaged by young cock."
            kil "Fuck, yeah!"
            "Again and again, I made Rosalind's cunt my home, bottoming out and kissing the deepest parts of her with ball-slapping fervor."
            kil "Give it to her, dude!"
        "Tease her."(chg=["rosalind_passion_up"]):

            $ Rosalind_Libido += 1
            scene w3_6228 with dissolve
            mc "You sell yourself to two young men and then you say something like that?"
            scene w3_6229 with dissolve
            "While I spoke, I let my cock languish at her entrance, pushing and prodding..."
            mc "Yet, I fully believe you. I believe you so much it..."
            scene w3_6230 with dissolve
            scene w3_6229 with dissolve
            rose "Hhhaaa...♥"
            mc "It turns me on."
            "Inching slowly up, with promise of penetration..."
            scene w3_6230 with dissolve
            scene w3_6229 with dissolve
            rose "Fhh... hnnn...♥"
            mc "Your husband must not have cut it in the bedroom, huh?"
            rose "He, hahh... don't go there..."
            "Rosalind took it in stride, perhaps refusing to be thrown off balance by someone she saw as a kid."
            mc "You should really thank my friend for turning you into a prostitute, because--"
            play music "music/drum-bass.ogg"
            scene rosa_3s10_a with dissolve
            show rosa_3s10 with dissolve
            rose "--eeeuaahh!"
            "After an agonizing delay, I pushed deep into Rosalind's hold, skewering her in support of my claims."
            mc "...you now have a good excuse for eating dick, don't you?!"
            "Again and again, I made Rosalind's cunt my home, bottoming out and kissing the deepest parts of her with ball-slapping fervor."
            kil "Fuck, yeah! Give it to her, dude!"


    "She took my cock in stride, devouring every inch of me, sucking me in as if it weren't even enough."
    "From her physique down to her receptiveness, Rosalind had a body built for fucking, and it was making sure that was {b}amply{/b} understood."
    kil "Fuck this bitch!"
    scene rosa_3s12_a with dissolve
    show rosa_3s12 with dissolve
    "Her wide hips veered feverishly into mine and her heavy chest boiled over in need, rising and falling, haphazardly sucking down air to fuel the debauchery."
    rose "Eh, aahh...! [mcf]!"
    "Her fat tits rewarded each and every thrust by flailing about {size=+10}STUPIDLY.{/size}"
    rose "This is... eeeeaahhhhh...♥♥"
    "And every time I freed myself from Rosalind's grasp, a fresh coat of sexual effluvia clung to the already slurry mix, making re-hilting myself in the motherly woman's fuckhole not only an inevitability, but..."
    rose "Euuggh, o-ohhhh...♥♥♥"
    "...bidding me to fuck her harder."
    kil "You've got two daddies tonight, you got it, bitch?!"
    scene rosa_3s10_a with dissolve
    show rosa_3s10 with dissolve
    "Rose's body said all it needed to say, and it didn't talk, it screamed."
    "{i}Fuck me, fuck me, fuck me...{/i}"
    kil "I said: {b}{size=+10}DO. YOU. FUCKIN'. GOT. IT. BITCH?!{/b}{/size}"
    "The idiot bellowed out, and I felt a swell of..."
    rose "Y-yeeeaehh....?! Y-yes!"
    "...solidarity?"
    kil "Who's your fuckin' daddy?!"
    "Kinship?"
    rose "Y-you two...!"
    "{i}Harmony?{/i}"
    kil "{b}{size=+10}SPEAK THE FUCK UP!{/b}{/size}"
    rose "{b}{size=+15}YOU TWO!{/b}{/size} Oh, fhhhuu--"
    mc "Ha! Oh, god...!"
    kil "Huh? What's so funny?"
    mct "(Damn, this was absurd!)"
    "We were more alike than I ever cared to admit, huh?"
    rose "Eeuuggghh...♥"
    "...and having a hype man while you go cervix-deep in a woman?"
    mc "A-ah... you're... god, you're fuckin stupid!"
    "{i}Not too shabby.{/i}"
    rose "Ha, haaaat...♥♥ You two a-are...♥♥"
    "His excitement was contagious."
    rose "OO, DhhaaaaAAAhhd...♥♥♥"
    kil "Listen to her! She fucking loves it!"
    rose "Euuhhh, oohhh...!"
    kil "How does my friend's dick taste, Rosie?"
    rose "W-what? Asking 'cause you... h-heh... w-wanna try? A-aahhh...?!"
    kil "You--"
    scene w3_6232 with dissolve
    rose "Pfft! C-crap...!"
    scene w3_6233 with dissolve
    mc "Bahaha! You set her up for that one!"
    scene w3_6232 with dissolve
    rose "Aah, h-hhaaa... I s-shouldn't laugh when I'm getting...! A, a-ah... t-to answer y-your question..."
    scene w3_6234 with dissolve
    rose "It feels f-fucking... a-ah...[mcf]'s fucking me..."
    scene w3_6235 with dissolve
    rose "{size=+5}Yyyyeeaaahh...♥{/size}"
    with flash
    mct "(S-shit!)"
    "Rosalind's cunt gripped my shaft so hard that I saw white."
    rose "For r-real...? Ah- haahaha...♥"
    scene rosa_3s12_a with dissolve
    show rosa_3s12 with dissolve
    kil "Damn dude, she's about to squeeze my dick off!"
    "...that was about all she was doing, actually, otherwise too distracted to do anything with it."
    kil "Did she just cum again?"
    "For his sake, I thought about redirecting her energy, but..."
    kil "Fuck, what a natural!"
    "He had the same dumb look present on his face as when we started, so caught up in the scenario that he didn't seem to mind the lack of attention."
    rose "Hehehe, ah... c-crap..."
    "And all the while we bantered, Rosalind quivered and shook as a cascade of little orgasms overwhelmed her senses."
    scene rosa_3s11_a with dissolve
    show rosa_3s11 with dissolve
    kil "Fuck, this is BEAUTIFUL!"
    rose "{size=+10}Ghh, haa, h-haaaaat!{/size}"
    with flash
    "One after another, threatening to extract a climax of my own from me."
    rose "Uh... s-sometimes I surprise myself...? Heh, hehh...♥"
    kil "I mean shit, we haven't even actually double-teamed you yet-"
    with flash
    rose "{size=+15}Oeeeeii, ha!{/size}"
    "Another one."
    kil "You know, I thought this last week, but if this Carnation thing doesn't work out..."
    with flash
    rose "{size=+20}D-damn...!{/size}"
    "And another."
    kil "We could start our own porn studio, and Rosie could star!"
    scene rosa_3s10_a with dissolve
    show rosa_3s10 with dissolve
    mc "S-shit, dude... with the way she's cumming-"
    with flash
    rose "{size=+25}OOoaauughhhhh-♥♥{/size}"
    kil "Holy shit, keep fuckin' thrustin', dude!"
    rose "Ghh, w-wahh...♥ G-ghwwod~"
    kil "I wanna see if we can break ol' Rosie!"
    mc "Haaah...! Eeeugh!"
    "The hold Rosalind had on me reached a delirious pitch."

    menu:
        "As Ian yammered, you feel a growing fondness for this woman."(chg=["rosalind_up"]):

            $ Rosalind_Affection +=1
            scene rosa_3s12_a with dissolve
            show rosa_3s12 with dissolve
            mc "D-damn it, Rose... you're amazing, you know that--"
            with flash
            rose "{size=+30}Geeeuuuuahhh-♥♥♥{/size}"
            "Pushing into her at this speed was a laborious undertaking, but my body refused to yield."
            mc "I m-mean... she's unbelievable, right?"
            kil "No, {i}shit.{/i} Someone should name a boat!"
            rose "F-fuck mee... k-keeep...♥"
            mc "Ride it out, Rose."
            rose "Whhyy.... ahhhh...♥"
            mc "Don't fight it!"
            rose "Ewwwooohhh, wWhhHooohhhhh...♥"
            mc "Enjoy it!"
            rose "EAaahhagin...???"
            mc "Cum!"
            rose "Aghhaaian...♥"
            mc "Cum on my cock!"
            rose "Ewwhm, aghhaaian, agghggaaain...♥"
            mc "Cum your fuckin' heart out--"
        "In your delirium, Ian's idea didn't sound so bad."(chg=["rosalind_passion_up"]):

            $ Rosalind_Libido += 1
            scene rosa_3s12_a with dissolve
            show rosa_3s12 with dissolve
            mc "Y-you know? I think--"
            with flash
            rose "{size=+30}Geeeuuuuahhh-♥♥♥{/size}"
            "Pushing into her at this speed was a laborious undertaking, but my body refused to yield."
            mc "I think you might be onto something with that porn shit!"
            "With all the blood in my body pooling in my cock, I was easily pulled into Ian's lunacy."
            mc "How's that sound? You want to be our personal prostitute?"
            rose "Eeehhh, yyheewwah... rrhhighhttt..."
            mc "Would you like that, Rose?"
            rose "Ahhnyy... annoyingg... fhhuuck..."
            mc "Would you like to be an on-camera cumdump?"
            rose "Shhttupihh... nhhho thahhhnks...."
            mc "You sure?"
            rose "Ayy, yyeehhhh.... shhowwt uhwwhp..."
            mc "Just think about it. You could get railed like this every week!"
            rose "Gghh... eeeughhh... ahggghain..?"
            kil "Some might even call it a dream job!"
            rose "Aghhaaian...♥"
            mc "Come on, just think--"


    $ renpy.music.set_volume(.2, 0, channel = "music")
    scene w3_6236 with dissolve
    play sound "sound effects/spurt.wav"
    with flash
    rose "{size=+40}Eeeuaah...♥♥♥ O-oh, c-crud!{/size}"
    "She squeezed down hard once more on my end, piercing the room with a cacophonous cry, as an unexpected jet stream of jizz fired into her greedy womb."
    kil "A-ahh... d-damn dude, she's...!"
    play sound "sound effects/spurt.wav"
    with flash
    scene w3_6237 with dissolve
    mc "S-shit!"
    "Rope after rope splattered her insides, mixing together with her discharge, and jettisoned itself from where we were connected."
    rose "Ahh...♥ Ah, nooh..♥♥. W-woah..♥♥♥"
    scene black with fade
    "......"
    "......"
    rose "...ehuuhh... eeuughhh...?! *Gwhhurk, hhwhhuwrk!*"
    $ renpy.music.set_volume(.5, 0, channel = "music")
    scene rosa_3s13_a with cmet
    show rosa_3s13 with dissolve
    mc "Ah, crap, sorry dude... I... came {b}inside.{/b} I don't know what the proper etiquette for these situations is."
    "Rosalind was just full of \"pleasant plaps\" today, as Ian delivered backshot after thunderous backshot to the MILF's gloriously ample ass."
    kil "Pfff, \"etiquette\"? The etiquette is you just don't think about the other dude's mess."
    mc "Uh..."
    rose "Ghhhuk... ghhhhhuukk...♥"
    "To the reasonable part of my brain, that sounded {b}gross{/b}, yet..."
    rose "Mmhyeehhahh...! Eehh...! *Gwhhurk, hhwhhuwrk!"
    mc "I'll defer to your wisdom, brother."
    "Who was I to argue?"
    rose "Ghh, hhhhkkk, mmmmhhh...!"
    "I hadn't even rested and yet I was still rock hard, as every thrust of my friend's cock caused Rosalind to sputter on my own."
    kil "Ah, but goddamn it, man. I think I'm in love!"
    scene w3_6238 with pixellate
    rose "Let's try both of you now..."
    kil "She actually said that!"
    play ambient "sound effects/fel2.wav"
    scene rosa_3s14_a with pixellate
    show rosa_3s14 with dissolve
    kil "{size=+10}I THINK I'M IN LOVE!{/size}"
    mc "Yeah, {i}right!{/i}"
    rose "Ghh, hhhhmm... eeuugghh... *Gurk!*"
    mc "Should make for a cute story to tell the grandkids!"
    "Half sensate as Rosalind was, she handled my size well, as I pushed past her uvula and tickled the back of the motherly cock sucker's throat."
    mc "Ughhhh... this is...!"
    "The energy of Ian's every thrust passed on his pleasure to me, and the sensation of Rosalind moaning into my groin...."
    mct "({i}I think I'm in love.{/i})"
    scene rosa_3s13_a with dissolve
    show rosa_3s13 with dissolve
    "*{size=+15}PlapPlapPlapPlapPlapPlapPlapPlapPlapPlap!*{/size}"
    kil "Oh, fuck yeah!"
    "*PlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlap!*"
    kil "My buddy's a tough act to follow, but GODDAMN IT! I'm crushing it!"
    rose "Hmmmhhh...♥♥♥"
    kil "You think so too, don't you slut?"
    rose "Mmhh, nnohhyhheee...♥"
    "As if affirming Ian's words, Rosalind let out a series of lackadaisical moans into my groin."
    rose "Ghh, yhheee, ooommmhhh...♥♥"
    "And again, I couldn't argue..."
    rose "Eyyuguhh... hywaahh... *Gruekkk!*"
    "Every well-timed shot of my friend's was delivered to perfection. {i}He was positively glowing.{/i}"
    "........."
    "......"
    mct "(...goddamn it, why am I appraising his forward thrusts?!)"
    mc "Ha! S-shit! I hope this is worth the money, Ian."
    rose "Mmmh, mmmhhh... *Chwwup, gwwrk-!*"
    kil "Oh, we're just getting started, but..."
    scene w3_6239 with dissolve
    play sound "sound effects/slap3.wav"
    scene w3_6240 with hpunch
    rose "GGhhh...♥"
    scene w3_6241 with dissolve
    kil "{b}Abso-fucking-lutely!{/b}"
    scene rosa_3s13_a with dissolve
    show rosa_3s13 with dissolve
    mc "D-damn, that felt...!"
    rose "Mmhh, aahh--"
    "Ian's blow passed pleasurably into my bones, adding an additional rush of pleasure into the mix."
    mc "Ah, that feels--"
    rose "Mhhhuuu...♥"
    kil "You fat ass cow!"
    "Picking up on that pleasure, Ian delivered another thunderous smack to Rosie's ample rear."
    rose "Mmhh, hhuu- *Gwhurrk, hhnnggwwuuk-!*"
    "It was perhaps the most moving \"I've got you, bro.\" that I had ever experienced."
    rose "Eeuuhhhh... *Whhurrrk-!*"
    scene w3_6239 with dissolve
    play sound "sound effects/slap3.wav"
    scene w3_6240 with hpunch
    kil "{size=+10}Who the fuck do you think you are?!!{/size}"
    rose "Ahhh, haaaaa--ghnnnuiuurrrk-!!!"
    scene w3_6239 with dissolve
    play sound "sound effects/slap3.wav"
    scene w3_6240 with hpunch
    kil "I pay you five grand and you cum endlessly on my friend's cock?!"
    scene rosa_3s13_a with dissolve
    show rosa_3s13 with dissolve
    "*{size=+15}PlapPlapPlapPlapPlapPlapPlapPlapPlapPlap!*{/size}"
    kil "You get off before EITHER of us?"
    kil "Y'know, you're a lousy prostitute, but...!"
    scene rosa_3s14_a with dissolve
    show rosa_3s14 with dissolve
    kil "...a {b}wonderful{/b} woman."
    "As we spit-roasted this wonderful woman, a funny thought from earlier crossed my mind..."
    mc "... ah, heh... you know what's weird?"
    kil "...eh? What?"
    mc "The time we stole your games back from Alice popped into my mind earlier."
    kil "Oh, yeah! She called up Vicky and got her permission to give you the same punishment as me!"
    "*PlapPlapPlapPlapPlapPlapPlapPlapPlapPlap!*"
    kil "What did you say? She can't punish both of us?"
    scene w3_6239 with dissolve
    play sound "sound effects/slap3.wav"
    scene w3_6240 with hpunch
    mc "H-heh... ah..."
    scene rosa_3s13_a with dissolve
    show rosa_3s13 with dissolve
    "{i}Goddamn it Rosalind's throat felt good{/i}."
    mc "...{i}something like that.{/i} We spent a whole Saturday cleaning the house."
    "*PlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlap!*"
    mc "First time I cursed you for being rich. {b}Big-ass-house-having-mansion-fuck!{/b}"
    kil "Fuck off! You sure came over an awful lot!"
    "*PlapPlapPlapPlapPlapPlapPlapPlapPlapPlap!*"
    mc "Heh, I guess we did have the run of the place, huh?"
    "*PlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlap!*"
    kil "It made for some kick-ass forts!"
    kil "While we're at it, can I be honest about something?"
    mc "Fuck. Sure. Yeah. What better time is there to have a heart-to-heart?"
    kil "You know those two or three years when we started to drop out of touch?"
    mc "What about--"
    rose "Mmhh, hhhaaa...♥♥♥"
    kil "I, uh... o-oh, fuck. I think she just came again."
    rose "Eeuuwwh, hhooo... *gurk, fhwwuck-!*"
    kil "Um, what was I... ah, yeah... uh.... actually, uh... h-hold on--"
    play sound "sound effects/spurt.wav"
    scene w3_6242 with flash
    kil "Gah!"
    "My friend put a pin in his thoughts, to cum inside Rosalind's reupholstered insides."
    stop ambient
    play sound "sound effects/spurt.wav"
    scene w3_6243 with flash
    kil "YOU BEAUTIFUL BIG-ASS BITCH!"
    play sound "sound effects/spurt.wav"
    with flash
    rose "{size=+15}Eeeeeeuuuuuuuuuuuuuuuah...♥♥♥{/size}"
    stop music fadeout 3.0
    scene black with fade
    "Rosalind's cry of ecstasy reverberated through my very being."
    "......"
    kil "...I'm just really glad we're back, man. Falling out of touch sucked."
    play music "music/the-gentleman.ogg"
    scene rosa_3s15_a with circlewipe
    show rosa_3s15 with dissolve
    "A few minutes later, we got back on track."
    kil "I was fuckin' miserable and I didn't even realize it until a few weeks ago."
    "I hadn't stopped fucking her face in the meantime, but Ian rejoined me."
    rose "Ghh, uhhhh...♥"
    kil "Don't get me wrong, my version of miserable kicks ass, but it was missing something."
    rose "Ghhrk, hhrrrrk-!"
    mc "We've had this conversation before."
    scene rosa_3s16_a with dissolve
    show rosa_3s16 with dissolve
    "...and now we were having it, making eye contact, while going balls deep in both ends of a mother of one."
    kil "I know, but... I'm just really, {i}really{/i} glad."
    rose "Grrk, hhhhhk, hhnnng...!"
    kil "--and I know me being gung-ho about doing this with you is fucking weird, but.."
    kil "I'm a fucked up dude, okay?"
    mc "Come on, dude it's--"
    scene rosa_3s15_a with dissolve
    show rosa_3s15 with dissolve
    "Self-consciousness froze the words in my throat, but..."

    menu:
        "Get it out! You're actually glad you reconnected too."(chg=["killian_up3"]):
            $ Killian_Bromance +=3
            mc "It's not like I don't owe a lot of who I am to you."
            "...the swelling warmth in me melted and freed them from my mouth."
            rose "Ghh, hhhhhh!"
            mc "In a good way."
            kil "Yeah, right..."
            mc "I probably wouldn't have had any friends growing up, and your timing was... {b}good{/b}."
            rose "Wwaah, hhaaa, hhhhhaaa!!"
            mc "After the accident, I mean."
            mc "Plus, I kinda liked playing protector, y'know?"
            rose "Wwaaah, hhmhmm, hhwwwah, yyeeahh!!!"
            mc "I've never admitted that to myself because it sounds messed up."
        "Nah, he's right, this is weird.":

            mc "Ah... forget about it. I don't know what I was going to say."
            "I left them there. "
            rose "Ghh, hhhhhh!"
            rose "Wwaah, hhaaa, hhhhhaaa!!"
            rose "Wwaaah, hhmhmm, hhwwwah, yyeeahh!!!"
            kil "It's alright, dude. I know you don't do sentimental shit. Instead..."


    scene w3_6244 with dissolve
    kil "........."
    kil "......"
    kil "..."
    scene rosa_3s15_a with dissolve
    show rosa_3s15 with dissolve
    mc "Why are you looking at me like that? It's weird."
    "I knew that look..."
    rose "Gurrk, hhrrrk-!"
    kil "Come on."
    rose "Mmmhh, hhweeuuughh-"
    scene rosa_3s16_a with dissolve
    show rosa_3s16 with dissolve
    mc "Is now the time for that?"
    kil "I can't think of a better one!"
    rose "Bleeeeaah, uhhhh.. eeeeeahhh..."
    mc "It's not like we just won a gym dodgeball game or anything..."
    scene w3_6245 with dissolve
    kil "You really going to leave me hanging, bro?"
    scene w3_6246 with dissolve
    rose "{size=-10}Mmmhh, eeeuuhhhhhh...{/size}"
    "It was like {i}not{/i} rubbing a dog's belly when he rolls over."

    menu:
        "Don't leave him hanging!":
            pass
        "Give him five!":
            pass
        "Give him some skin!":
            pass
        "Seriously, are you a monster? You have no choice here.":
            pass

    play sound "sound effects/slap4.wav"
    scene w3_6247 with vpunch
    kil "Fuck yeah!"
    play sound "sound effects/slap4.wav"
    scene w3_6248 with hpunch
    "The sound of two men's hands triumphantly meeting palm-to-palm rang out through the loft, superseding Rosalind's whorish moans."
    play sound "sound effects/slap4.wav"
    scene w3_6247 with vpunch
    mct "(Just can't not do it..)"
    scene rosa_3s15_a with fade
    show rosa_3s15 with dissolve

    if feliciaFlag == True:
        kil "So, you have any plans for today?"
        mc "Some art thing with Felicia."
        kil "You're seeing her socially?"
        mc "No, I'm not seeing her \"socially\", it's..."
        "As if I could forget, Rosalind was currently playing the role of Chinese finger."
        rose "{size=-15}Ghh, rrrk, euuuaoooh...{/size}"
        "Still, I doubt she's processing much of what she hears at this point..."
        mc "Something like that. What are you going to get up to?"
    else:
        kil "You have any plans for today?"
        mc "Nah. Think I'm just going to stay in. What about you?"

    kil "Uh... I don't know. Between {b}this{/b} and the past few nights, I think I'm due for a nap."
    mc "Sounds like a good idea to me. Take care of yourself!"
    rose "Ghhrrk, hhhnnhg... mmmmhhh...♥"
    kil "Yeah, y-yeah, plus I should..."
    rose "{size=+15}Eeuuuuuuuooohhmmhmhhhhh...♥♥♥{/size}"
    kil "...I *ahem* s-should probably rethink all that \"coked up\" behavior of Darius that I wrote off."
    mc "D-don't wallow too deep.."
    "I could feel my nuts begin to tighten."
    kil "N-no worries. Who do you think I am? Y-you?"
    mct "(Hmm... I should probably shoot Felicia a text and see what's up)"
    scene w3_6249 with dissolve
    mc "I'm just saying... ah... you--"
    play sound "sound effects/spurt.wav"
    scene w3_6250 with flash
    mc "Hnnngg...!"
    "This time, I was compelled to mess up Rosalind's beautiful outside."
    scene w3_6251 with dissolve
    kil "Hehe, nice one!"
    mc "...you need to start taking better care of yourself, dude. More sleep and less drinking."
    kil "Y-yeah, probably..."
    stop music fadeout 3.0
    scene black with fade
    kil "After I cum on this bitch's fat tits."
    "*PlapPlapPlapPlapPlapPlapPlapPlapPlapPlap!*"
    rose "{size=+15}Mmhhhhhaaaaaa!{/size}"
    "*PlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlapPlap!*"
    play music "music/crinoline-dreams.ogg"
    scene w3_6252 with circlewipe

    if feliciaFlag == True:
        mct "(I should text Felicia...)"
        "It probably wasn't the best idea to do this when I still had a long day ahead of me, but this was fun."
    else:
        mct "(...well, that was {i}fun,{/i})"

    scene w3_6253 with dissolve
    "............"
    "......"
    "...maybe too much fun.."
    kil "Goddamn it, I'm beat..."
    mc "Go home and get some sleep. Like you planned."
    kil "Yeah... I should."
    rose "Ghh, huuu, zzzzzh, heee..."
    "For a moment, we both listened to Rosalind steadily breathe, admiring our handiwork."
    "......"
    "..."
    kil "Not as beat as her, though. Is she snoring?"
    play ambient "sound effects/ringing-inbound.wav"
    scene w3_6254 with dissolve
    "*Brrring, rrrriiing-!*"
    rose "Oh!"
    scene w3_6255 with dissolve
    rose "S-shit, it's that time?!"
    rose "That's probably Nora!"
    scene w3_6256 with dissolve
    "........."
    "......"
    scene w3_6257 with dissolve
    kil "...is she the fucking Terminator?"
    stop ambient fadeout 3.0
    scene black with fade
    mc "Quite possibly..."
    kil "{b}Heh.{/b} {i}Fucking{/i} Terminator."

    $ renpy.end_replay()

    if not persistent.w3RoseThreesome:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3RoseThreesome = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

    "........."
    "......"
    "..."

    if feliciaFlag == True:
        jump w3FeliciaMeet1
    elif feliciaFlag == False and w3VeroBarDate == True:
        show screen textbox2 with dissolve
        jump w3June17MiddayMontage
    else:
        jump w3June17End

label w3FeliciaMeet1:
    stop music
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionfelicia06 with blinds
    $ renpy.pause(6, hard=True)
    scene w3_6258 with blinds
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    play ambient "sound effects/city-night.wav"
    "A few hours after Ian left, details were honed and a time was set up."
    scene w3_6259 with dissolve
    mct "(She's got 15 minutes on the clock.)"
    scene w3_6260 with dissolve
    "But rather than twiddling my thumbs inside, I planted my ass on the curb and mused if the wife shared her husband's uncanny punctuality."
    "......"
    scene w3_6261 with dissolve
    "..."

    if feliciaSugarBaby == True:
        mct "(I'm supposed to play the role of a sugar baby, huh...?)"

        if hanaGF == True and hanaCheat == 0:
            "The problem with that is my arrangement with Felicia predates the one I made with Hana."

            if rosalindKilSolution == True:
                "Tag teaming Rosalind aside to get her out of trouble with a loan shark, {i}this{/i} extracurricular definitely qualifies as cheating on Hana."
            else:
                "This extracurricular definitely qualifies as \"outside the club\"..."

            jump w3FeliciaCheatMenu

            if rosalindFelSolution == True:
                "Of course, lest I forget, my time has already been bought with Felicia's settlement of Rosalind's interest."
                mct "(Welp, I put myself in this position...)"

        elif hanaGF == True and hanaCheat >= 1:
            "It's not like I haven't already violated my arrangement with Hana, but it also doesn't need to become a pattern."

            if rosalindKilSolution == True:
                "Tag teaming Rosalind aside to get her out of trouble with a loan shark, {i}this{/i} extracurricular definitely qualifies as cheating on Hana."
            else:
                "And this extracurricular definitely qualifies as \"outside the club\"..."

            if rosalindFelSolution == True:
                "Of course, lest I forget, my time has already been bought with Felicia's settlement of Rosalind's interest."
                mct "(Welp, I put myself in this position...)"
            scene w3_6263 with dissolve
            jump w3FeliciaCheatMenu
        else:

            mct "(I still think it's absurd, but it could be fun.)"
            "{i}A lot of fun.{/i}"
            scene w3_6262 with dissolve
            mc "Heh..."
            jump w3FeliciaMeet2
    else:


        mct "(She wanted to pay me for my time, but I insisted otherwise...)"

        if hanaGF == True and hanaCheat == 0:
            "The problem is we scheduled this before I started going out with Hana."
            "Now, things don't have to necessarily get physical tonight, but I do run the risk of violating my new girlfriend's trust."

            if rosalindKilSolution == True:
                mct "(Tag teaming Rosalind with my best friend to settle the interest on her debt aside, of course...)"
            scene w3_6263 with dissolve
            jump w3FeliciaCheatMenu


        elif hanaGF == True and hanaCheat >= 1:
            "The problem is we scheduled this before I started going out with Hana, and while it wouldn't be the first time I reneged on our freshly made promise, it also doesn't need to become a pattern."
            "Things don't necessarily have to get physical tonight, but knowing Felicia..."
            scene w3_6263 with dissolve
            jump w3FeliciaCheatMenu
        else:

            scene w3_6262 with dissolve
            "{i}She's so stupid...{/i}"
            jump w3FeliciaMeet2


    menu w3FeliciaCheatMenu:

        "I'll be straight with Felicia. We can have fun tonight, but it has to be platonic. (w3FeliciaPlatonic = True)" if feliciaSugarBaby == False:
            $ w3FeliciaPlatonic = True
            mct "(She's going to think I'm stupid...)"
            jump w3FeliciaMeet2

        "I'll be upfront with Felicia. We can go out tonight, but the sugar mama thing is no longer happening. (w3FeliciaPlatonic = True)" if feliciaSugarBaby == True:
            $ w3FeliciaPlatonic = True
            mct "(Hopefully she won't be too angry. It's for a good reason, right?)"
            jump w3FeliciaMeet2

        "A deal is a deal, and this helped out Rosalind." if rosalindFelSolution == True:
            mct "(...Hana would appreciate that, right?)"
            "{i}Yeah, right...{/i}"
            jump w3FeliciaMeet2
        "It's not like Hana will know.":
            mct "(...but why did I even make that promise in the first place, then?)"
            jump w3FeliciaMeet2

label w3FeliciaMeet2:

    scene w3_6264 with dissolve
    "Twelve minutes."

    if w3VeroBarDate == True:
        play ambient2 "sound effects/ringing-inbound.wav"
        scene w3_6265 with dissolve
        "*Ring, ring...*"
        scene w3_6266 with dissolve
        mct "(Hmmm...?)"
        scene w3_6267 with dissolve
        if w2ExEndingVeronica == True:
            "It was Ronnie."
        else:
            "It was Veronica."

        if w3VeronicaSex == True and hanaGF == True:
            mct "(Speaking of cheating on Hana...)"
            mct "(...wait, she's calling {i}me?!{/i})"
        else:
            mct "(She's calling {i}me?!{/i})"
        stop ambient2
        play sound "sound effects/phonemenu.wav"
        scene w3_6268 with dissolve
        mc "Hello?"
        scene w3_6269 with dissolve
        ver "[mcf], I... uh..."
        "{i}Something must be wrong.{/i}"
        jump w3VeroCheckingIn
    else:
        scene w3_6263 with dissolve
        "And so time dwindled down and my butt fell asleep."
        "Ten, five..."
        scene black with fade
        "Three, two..."
        play sound "sound effects/car-beep.wav"
        jump w3FeliciaMeet3


label w3VeroCheckingIn:
    stop ambient
    play music "music/timeless.ogg"
    scene w3_6270 with wipeleft
    ver "Umm... how's... {i}how's it going?{/i}"
    scene w3_6271 with dissolve
    mct "Is everything okay?!"
    scene w3_6272 with dissolve
    ver "........."
    ver "......"
    scene w3_6273 with dissolve
    ver "...I'm calling to talk!"
    scene w3_6274 with dissolve
    mc "To me? To [mcf] [mcl]?"
    scene w3_6275 with dissolve
    ver "Yes! That's what... that's... {b}you fucking asshole!{/b} A client canceled on me and I'm bored!"
    scene w3_6276 with dissolve
    mc "...you're bored?"
    scene w3_6277 with dissolve
    ver "And I, uh.. I just wanted to, umm..."

    if feliciaFlag == True:
        scene w3_6278 with dissolve
        mc "Good timing. You've got me all to yourself for ten whole minutes."
        scene w3_6279 with dissolve
        ver "Don't phrase it like that."
        scene w3_6278 with dissolve
    else:
        scene w3_8034 with dissolve
        mc "Okay, let's talk, and..."

    if w3VeronicaSex == True:
        mc "I'm good, by the way. In fact, I'm doing even better now that I've heard from you."
        scene w3_6280 with dissolve
        ver "...you are?"
        scene w3_6281 with dissolve
        mc "I was worried that once you sobered up, you might think I'm an idiot who only cares about his cock."
        scene w3_6282 with dissolve
        ver "What? Because you got horny? Because we fucked? I'm not going to give you shit for that, I was right there with you."
        ver "We're good, [mcf]. You're a sincere man."
        scene w3_6281 with dissolve
        "For some reason the word \"man\", coming from Veronica's lips, filled me with undue happiness."

        if w2ExEndingVeronica == True:
            mc "Consider me relieved. How are you, Ronnie?"
        else:
            mc "Consider me relieved. How are you, Veronica?"

        scene w3_6280 with dissolve
        ver "About the same as yesterday, but a little less stressed and a lot more sore."
        scene w3_6281 with dissolve
        mc "From working out?"
        scene w3_6282 with dissolve
        ver "No. From our little romp. It's not every day I take eight inches."
        scene w3_6283 with dissolve
        mc "Could've fooled me."
        ver "Fuck yeah, I could."
        scene w3_6284 with dissolve
        ver "Did you have any trouble getting home last night? You were pretty hosed."
        mc "Not as hosed as you."
        scene w3_6285 with dissolve
        ver "Wrong~ I can hold my liquor better than you, string bean."
        scene w3_6286 with dissolve
        mc "How would you know? You were drunk!"

    elif w3VeronicaWingman == True:
        mc "Say, I must've really wowed with how cool and cordial I am."
        scene w3_6280 with dissolve
        ver "Shut up."
        scene w3_6281 with dissolve
        mc "You called me to tell me to shut up?"
        scene w3_6282 with dissolve
        ver "Answer my question: how the fuck are you?"
        scene w3_6283 with dissolve
        mc "I'm good. How about you?"
        mc "Did you and Olivia find your way out of the night safe and sound?"
        scene w3_6284 with dissolve
        ver "Hehe, what are you asking, exactly?"
        mc "Did you have a nice, warm night?"
        ver "Well..."
        scene vero_ot_a with pixellate
        show vero_ot with dissolve
        olivia "Ghhhhhhaaaaaaaaaaaaah...♥♥♥"
        mc "Was it a home run?"
        ver "I hate using sports metaphors. It's degrading."
        olivia "Yeahhuuhh... S-stacy... euuhhh... why did you..."
        mc "My bad."
        ver "Yeah..."
        scene w3_6287 with pixellate
        ver "Let's just say the bases were loaded and I knocked it out of the damn park."
        scene w3_6288 with dissolve
        mc "Ha!"
        $ renpy.end_replay()

        if not persistent.w3VeronicaStory:
            play sound "sound effects/notification.wav"
            show memoryunlock with dissolve
            $ renpy.pause(3, hard=True)
            $ persistent.w3VeronicaStory = True
            hide memoryunlock with dissolve
            $ renpy.pause(0.5, hard=True)
    else:

        mc "Did you get home, alright? When we parted, you were pretty hosed."
        scene w3_6280 with dissolve
        ver "So were you."
        scene w3_6281 with dissolve
        mc "Yeah, I can hardly remember what we talked about."
        scene w3_6282 with dissolve
        ver "{b}Good.{/b} Drunken soul-searching is..."
        scene w3_6283 with dissolve
        ver "I'm just going to remember the dancing. You really put on the moves."
        scene w3_6284 with dissolve
        mc "So did you..."

    scene w3_6289 with dissolve
    ver "Ask me something, [mcf]."
    scene w3_6290 with dissolve
    mc "Because you're bored?"
    scene w3_6289 with dissolve
    ver "Because I'm bored."
    scene w3_6290 with dissolve
    mc "How much does a shot put weigh?"
    scene w3_6291 with dissolve
    ver "That's your question?"
    scene w3_6286 with dissolve
    mc "Sorry. How much does a {i}woman's{/i} shot put weigh?"
    scene w3_6285 with dissolve
    ver "8.82 pounds."
    scene w3_6286 with dissolve
    mc "That doesn't seem so heavy."
    scene w3_6285 with dissolve
    ver "You try lobbing one 20 meters."
    scene w3_6286 with dissolve
    mc "No, thank you."
    scene w3_6291 with dissolve

    if feliciaFlag == True:
        ver "You said I had ten minutes. Am I keeping you from something?"
        scene w3_6290 with dissolve
        mc "Quite the opposite. You're keeping me from being {b}bored{/b}."
        mc "I'm sitting on the curb, waiting for a ride. You've got great timing."
    else:

        ver "By the way, am I keeping {i}you{/i} from something?"
        scene w3_6290 with dissolve
        mc "Nah, I'm just sitting at home. We can talk as much as you like."

    mc "Do you still get paid if a client cancels?"
    scene w3_6289 with dissolve
    ver "There's a 50 percent cancellation fee, waivable at my discretion."
    scene w3_6290 with dissolve
    mc "Did you waive it?"
    scene w3_6292 with dissolve
    ver "Fuck no! Time is money and I've got more of one than the other right now."
    stop music fadeout 3.0
    scene black with fade
    $ history_veronica = "To my surprise, a lonely Veronica gave me a call. A small gesture that made me feel... good?"
    $ unread_veronica = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "We talked."
    "It was a simple, yet seemingly insurmountable thing."

    if feliciaFlag == True:
        play sound "sound effects/car-beep.wav"
        "We talked for 23 minutes. It turned out Felicia wasn't as time-savvy as Elias Ford."
        jump w3FeliciaMeet3
    else:
        "We talked for an hour, until Veronica's next client."
        $ date = "june17day"
        jump w3June17End

label w3FeliciaMeet3:
    scene w3_6293 with circlewipe
    fel "Hiya, stud."
    scene w3_6294 with dissolve
    "Finally, standing like a golden goddess against the backdrop of a dirty city street, there was Felicia."
    play music "music/soft-feeling.ogg"
    scene w3_6295 with dissolve
    fel "Your carriage awaits."
    scene w3_6296 with dissolve
    "With nary a blemish or a hair out of place, she looked..."
    hide screen textbox2 with dissolve

    menu:
        "Greet Felicia, emphatically.":
            scene w3_6297 with dissolve
            show screen textbox2 with dissolve
            mc "Holy {b}fuck{/b}, you look {i}great.{/i}"
            scene w3_6298 with dissolve
            "(There's something about the way her tanline peeks out from her dress that's {i}just..{/i})"
            scene w3_6299 with dissolve
            fel "Down, boy."
            scene w3_6298 with dissolve
            mct "(Yeah...)"
            scene w3_6301 with dissolve
            mc "No, {b}really{/}, you do. But I know you know that, because--"
            scene w3_6299 with dissolve
            fel "Are you going to say, 'when do you not?'?"
            scene w3_6300 with dissolve
            mc "I wasn't going to make it a question."
            scene w3_6299 with dissolve
            fel "Cute."
            scene w3_6300 with dissolve
            mc "So, art thing, huh?"
            scene w3_6302 with dissolve
            fel "The term is exhibition."

        "Play it cool with a familiar touch. (if w3FeliciaPlatonic = False)" if w3FeliciaPlatonic == False:
            scene w3_6297 with dissolve
            show screen textbox2 with dissolve
            mc "Hello, Felicia. You..."
            scene w3_6303 with dissolve
            "*Chwup!*"
            mc "You look {i}impeccable{/i} this evening."
            scene w3_6299 with dissolve
            fel "My plan went perfectly then."
            fel "You look good too, [mcf]."
            scene w3_6300 with dissolve
            mc "I'm underdressed.."
            scene w3_6299 with dissolve
            fel "We'll be fixing that soon."
            scene w3_6301 with dissolve
            mc "It wouldn't do to look schlubby for an art thing, now would it?"
            scene w3_6302 with dissolve
            fel "That \"thing\" is called an exhibition."
        "Act casual.":
            scene w3_6297 with dissolve
            show screen textbox2 with dissolve
            mc "Was traffic bad?"
            scene w3_6299 with dissolve
            fel "There was an accident. I had to take a detour to get here. {i}Sorry.{/i}"
            scene w3_6300 with dissolve
            mc "No big deal, not your fault. Plus..."
            scene w3_6304 with dissolve
            mc "It's a nice cool evening for summer, isn't it? Nice weather for the art thing you have planned."
            scene w3_6302 with dissolve
            fel "It's called an exhibition."

    scene w3_6305 with dissolve
    mc "It seems I can't get away from that word."
    scene w3_6306 with dissolve
    fel "Heh, no, we can't..."
    scene w3_6307 with dissolve
    mc "Who's the artist?"
    scene w3_6308 with dissolve
    fel "A young woman I'm a big fan of. Denise Cosgrove."
    scene w3_6309 with dissolve
    fel "You wouldn't have heard of her, but..."
    "Felicia briefly trailed off, as if rolling the weight of the moment back and forth in her mind."
    scene w3_6310 with dissolve
    fel "Tonight's her first solo show. It means a lot, and I want to be there."
    scene w3_6305 with dissolve
    mc "Are you two friends? You sound really proud of her."
    scene w3_6310 with dissolve
    fel "Never met, actually."
    scene w3_6305 with dissolve
    mc "Tonight will be the first time then?"
    scene w3_6310 with dissolve
    fel "Maybe. I don't know if I'll speak to her."
    scene w3_6305 with dissolve
    mc "Why not? Don't artists love to meet their fans?"
    scene w3_6311 with dissolve
    fel "......"
    scene w3_6312 with dissolve
    fel "...is that on my account?"
    scene w3_6313 with dissolve
    "It didn't take a social savant to note Felicia curiously dodged the question..."
    scene w3_6314 with dissolve
    mc "Sorry to say, but it's because my mom thought I looked like a dork."
    scene w3_6315 with dissolve
    fel "...are you trying to make me feel like I'm robbing the cradle?"
    mc "...no?"
    scene w3_6316 with dissolve
    fel "Too bad. You would've got credit for it."

    if feliciaSugarBaby == True:
        fel "Would've been the perfect vibe for a sugar baby."
        scene w3_6317 with dissolve
        mc "I'm being graded?"
        scene w3_6316 with dissolve
        fel "I told you tonight was a test run, didn't I?"
    else:
        scene w3_6317 with dissolve
        mc "I'm being graded?"
        scene w3_6316 with dissolve
        fel "You would be, if you didn't refuse my money."
        fel "Which is a {b}shame.{/b} Money makes for good foreplay."

    if w3FeliciaPlatonic == True:
        scene w3_6318 with dissolve
        mc "Actually, about that..."
        mct "(Before the evening actually begins, I need to establish expectations.)"
        fel "Mmmh, I don't like that look, [mcf]. Too serious..."
        scene w3_6319 with dissolve
        hide screen textbox2 with dissolve

        menu:
            "Stick to your guns. Tonight's needs to be platonic." if feliciaSugarBaby == False:
                show screen textbox2 with dissolve
                mc "About that, I really *AM* just going as your friend tonight, Felicia. {b}Full stop.{/b}"
                scene w3_6321 with dissolve
                fel "{i}Friend?{/i} Full stop? Like no sex?"
                fel "{i}You{/i} are taking sex off the table?"
                scene w3_6322 with dissolve
                "She looked understandably confused by my proclamation."
                mc "I'm... seeing someone."
                scene w3_6323 with dissolve
                "........."
                "......"
                scene w3_6324 with dissolve
                fel "...pfhh, {i}what?!{/i} {i}You're{/i} seeing someone?"
                fel "{b}You{/b}, as in the you who plays sexual organ grinder monkey for his day job, is making a point of being monogamous?"
                scene w3_6325 with dissolve
                fel "Or did you quit your job when I wasn't looking?"

                if w3FeliciaMeanShock == True:
                    fel "If you did, I wish you did that a few days ago. Would've spared me the indignity of shocking the {b}shit{/b} out of me."

                scene w3_6326 with dissolve
                mc "No, {i}I didn't quit.{/i} It's Hana."
                scene w3_6325 with dissolve
                fel "Hana, huh?"
                scene w3_6326 with dissolve
                mc "Yeah, outside and inside of the club are two separate--"
                scene w3_6329 with dissolve
                fel "{b}Huh!{/b} Well..."
                scene w3_6328 with dissolve
                "Her appraisal of that idea was plain as day as the lines on her face."
                scene w3_6329 with dissolve
                fel "That is, uh... that seems like a keg of gunpowder waiting to explode, but live AND learn."
                scene w3_6319 with dissolve
                "{i}She looked at me like I was a naive child.{/i}"
                mc "...so... with THAT in mind, do you still want to go out with me tonight?"
                scene w3_6330 with dissolve
                fel "......"

                if minaFlag == True and minaCheat == True:
                    scene w3_6327 with dissolve
                    fel "...what about Mina? After going through the wringer with Ian, {b}don't be indelicate with her when you let her know.{/b}"
                    scene w3_6326 with dissolve

                    if w3MinaHotelFucked == True:
                        mct "(Right, yeah... {i}when I let her know.{/i})"
                        mc "You don't have anything to worry about..."
                        mct "(Because naturally if I'm breaking it off with Felicia, I will break it off with Mina, too...)"
                    elif minaBreakOff == True:
                        mc "Don't worry. She already knows."

                    scene w3_6327 with dissolve
                    fel "Good."
                    scene w3_6330 with dissolve
                    "......"
                    mc "...so, we going to have a nice night out or what?"
                    scene w3_6331 with dissolve
                    fel "Well... I can't go to this thing alone and I {i}really{/i} want to go. Anything extra would've been just icing."
                else:
                    scene w3_6331 with dissolve
                    fel "...I do. I can't go to this thing alone and I {i}really{/i} want to go. Anything extra was just icing."

                scene w3_6319 with dissolve
                mc "I was hoping you'd say that."
                jump w3PlatonicJumpingPoint

            "Stick to your guns. Your arrangement can no longer happen. (if rosalindFelSolution = True)"(chg=["felicia_down3"]) if feliciaSugarBaby == True:

                if rosalindFelSolution == True:
                    $ Felicia_Affection -= 3

                show screen textbox2 with dissolve
                mc "That can't happen anymore, I'm sorry."
                scene w3_6322 with dissolve
                "She looked understandably confused by my proclamation."
                scene w3_6321 with dissolve
                fel "You're sorry...?"
                scene w3_6322 with dissolve
                "........."
                scene w3_6323 with dissolve
                "......"
                scene w3_6324 with dissolve
                fel "...pfhh, {i}what?!{/i} {i}You're{/i} seeing someone?"
                fel "{b}You{/b}, as in the you who plays sexual organ grinder monkey for his day job, is making a point of being monogamous?"
                scene w3_6325 with dissolve
                fel "Or did you quit your job when I wasn't looking?"

                if w3FeliciaMeanShock == True:
                    fel "If you did, I wish you did that a few days ago. Would've spared me the indignity of shocking the {b}shit{/b} out of me."

                scene w3_6326 with dissolve
                mc "No, {i}I didn't quit.{/i} It's Hana."
                scene w3_6325 with dissolve
                fel "Hana, huh?"
                scene w3_6326 with dissolve
                mc "Yeah, outside and inside of the club are two separate--"
                scene w3_6329 with dissolve
                fel "{b}Huh!{/b} Well..."
                scene w3_6328 with dissolve
                "Her appraisal of that idea was plain as day as the lines on her face."
                scene w3_6329 with dissolve
                fel "That is, uh... that seems like a keg of gunpowder waiting to explode, but live and learn."
                scene w3_6319 with dissolve
                "Rather than being pissed, she looked at me almost sympathetically. {i}As if I was a naive child.{/i}"

                if rosalindFelSolution == True:
                    mc "I'll get you your five grand back. It'll take a little bit for me to come up with, but--"
                    scene w3_6321 with dissolve
                    fel "My five grand...? Oh, {i}yeah{/i}."
                    scene w3_6331 with dissolve
                    fel "Rosalind's thing -- don't bother."
                    scene w3_6330 with dissolve
                    mc "...but it's a good chunk of change."
                    scene w3_6325 with dissolve
                    fel "Heh. Do you know what the difference between a sugar baby and a whore is, [mcf]?"
                    scene w3_6319 with dissolve
                    mc "One offers more tangible companionship?"
                    scene w3_6325 with dissolve
                    fel "No. You give the sugar baby money with the {b}hope{/b} of something happening. It's up to them if they want to do what's needed to keep that relationship up."
                    scene w3_6329 with dissolve
                    fel "As far as I'm concerned, that's just the breaks."
                    scene w3_6328 with dissolve
                    mc "That sounds... {i}arbitrary.{/i}"
                    scene w3_6320 with dissolve
                    fel "Maybe, but the point is, it's just five grand and it helped out Rosie. Don't worry about it."

                    if minaFlag == True and minaCheat == True:
                        scene w3_6321 with dissolve
                        fel "...I'm actually more worried about Mina. After going through the wringer with Ian, {b}don't be indelicate with her when you let her know.{/b}"
                        scene w3_6322 with dissolve

                        if w3MinaHotelFucked == True:
                            mct "(Right, yeah... {i}when I let her know.{/i})"
                            mc "You don't have anything to worry about..."
                            mct "(Because naturally if I'm breaking it off with Felicia, I will have to break it off with Mina, too...)"
                        elif minaBreakOff == True:
                            mc "Don't worry. She already knows."

                        scene w3_6320 with dissolve
                        fel "Good."
                        scene w3_6319 with dissolve

                elif minaFlag == True and minaCheat == True:
                    scene w3_6327 with dissolve
                    fel "...but, what about Mina? After going through the wringer with Ian, {b}don't be indelicate with her when you let her know.{/b}"
                    scene w3_6326 with dissolve

                    if w3MinaHotelFucked == True:
                        mct "(Right, yeah... {i}when I let her know.{/i})"
                        mc "You don't have anything to worry about..."
                        mct "(Because naturally if I'm breaking it off with Felicia, I will have to break it off with Mina, too...)"
                    elif minaBreakOff == True:
                        mc "Don't worry. She already knows."

                        scene w3_6320 with dissolve
                        fel "Good."
                        scene w3_6319 with dissolve
                else:

                    pass

                mc "...so, do you still want to go out with me tonight or...?"
                scene w3_6331 with dissolve
                fel "Well... uh... for the record, I'm not happy about it, but..."
                scene w3_6330 with dissolve
                "She weighed her options."
                scene w3_6321 with dissolve
                fel "I can't go to this thing alone and I {i}really{/i} want to go."
                jump w3PlatonicJumpingPoint
            "On second thought... (hanaTwoTime = True, hanacheat +1, w3FeliciaPlatonic = False)":

                $ hanaTwoTime = True
                $ hanaCheat +=1
                $ w3FeliciaPlatonic = False
                show screen textbox2 with dissolve
                "Such a short-lived resolution..."
                jump w3FullOnJumpingPoint
    else:
        jump w3FullOnJumpingPoint


label w3PlatonicJumpingPoint:
    scene w3_6332 with dissolve
    mct "(She really must be a big fan...)"
    scene w3_6333 with dissolve
    mc "So, how is tonight going to play?"
    scene w3_6334 with dissolve
    fel "First, we need to get you a nice suit."
    scene w3_6333 with dissolve
    mc "You're still keen on dressing me up? I can just go back up and change."
    scene w3_6335 with dissolve
    fel "Awww, don't rob me of that pleasure, stud. I'm sure you have something ill-fitted from your high school graduation, but I'm thinking something a bit more..."
    fel "{i}Me.{/i} Let's not put a hamper on all my designs. Pretty please?"
    scene w3_6336 with dissolve
    "I wanted to say something in return, but aside from my monkey clothes for the club, which I had no inclination to wear any place else..."
    scene w3_6333 with dissolve
    mc "Sure, you can dress me up like an accessory, but I'll pay for it. Deal?"
    scene w3_6332 with dissolve
    mct "(She wasn't wrong.)"
    scene w3_6337 with dissolve
    fel "Just remember, when you see the bill, there's no shame about changing your mind about that."
    scene w3_6338 with dissolve
    mc "You play smarmy really well when you want to, Felicia."
    scene w3_6334 with dissolve
    fel "Don't I?"
    scene w3_6339 with dissolve
    fel "I might be jumping the gun, but I think you'd look good in something {i}complimentary{/i}.."
    scene w3_6333 with dissolve
    mc "What time's the show?"
    scene w3_6334 with dissolve
    fel "7 PM, but it's outside the city. The drive will eat up most of the time."
    scene w3_6335 with dissolve
    fel "The plan was to eat afterward. You feeling peckish or can you wait?"
    scene w3_6340 with dissolve
    mc "I can work up an appetite. Shall we go, then?"
    scene w3_6341 with dissolve
    fel "Careful with your phrasing, Mr. Platonic Ideal."
    scene black with fade
    stop music fadeout 3.0
    "........."
    "......"
    "..."
    jump w3FeliciaClothing

label w3FullOnJumpingPoint:

    if feliciaSugarBaby == True:
        scene w3_6342 with dissolve
        mc "Should I just act how I'd want you to if the roles were reversed?"
        scene w3_6343 with dissolve
        fel "You think I'd need to pay money for a horn dog? I could pull one of those off the streets."
        scene w3_6344 with dissolve
        mc "Then what am I being graded on, exactly?"
        scene w3_6343 with dissolve
        fel "Something more... {b}polished.{/b} {i}Fastidious?{/i}"
        scene w3_6345 with dissolve
        fel "You'll need to be a lot of things."
        fel "A companion, {b}a man{/b}, funny, serious, attentive, {i}inattentive.{/i}"
        scene w3_6343 with dissolve
        fel "Whatever suits the mood and needs of the moment."
        scene w3_6344 with dissolve
        mc "Sounds like a tall order..."
        scene w3_6343 with dissolve
        fel "You can handle it, stud."
        scene w3_6346 with dissolve
        fel "If anything, I might be the one out of my element."
    else:

        scene w3_6347 with dissolve
        mc "Personally? I prefer skin-on-skin."
        scene w3_6348 with dissolve
        fel "Do you now?"
        scene w3_6349 with dissolve
        fel "So, you're going to play gentleman tonight?"
        scene w3_6350 with dissolve
        mc "I can try, but no promises. I'm going to be out of my element."
        scene w3_6351 with dissolve
        fel "You'll do fine, stud."
        fel "You'll do fine..."
        fel "You might even be surprised at the variety of types that will be there."
        scene w3_6352 with dissolve
        fel "If anything, I might be the one out of her element."

    scene w3_6353 with dissolve
    mc "That's doubtful..."
    scene w3_6354 with dissolve
    fel "Well, we'll see."
    scene w3_6355 with dissolve
    mc "So what's the itinerary for the night, Mrs. Ford?"
    fel "First things first, we need to get you a suit."
    fel "Something suitable for a young man playing companion to a beautiful socialite."
    scene w3_6356 with dissolve
    mc "I can go back upstairs and get dressed."
    scene w3_6357 with dissolve
    fel "You'll do no. Such. Thing."
    scene w3_6358 with dissolve
    fel "Believe it or not, I've been looking forward to dressing you up, so that's non-negotiable."
    scene w3_6359 with dissolve
    fel "I can't wait to see you in a tailored suit. I'm thinking something {i}complimentary{/i}..."
    scene w3_6356 with dissolve

    if feliciaSugarBaby == True:
        mc "Sure, I'll happily play accessory. What time's the show?"
    else:
        mc "Sure, you can dress me up like an accessory, but I'll pay for it."
        scene w3_6360 with dissolve
        fel "Can't you just consider it a gift for spending an evening with me?"
        scene w3_6356 with dissolve
        mc "{b}I want to.{/b} What time's the show?"

    scene w3_6358 with dissolve
    fel "7 PM, but it's outside the city. The drive will eat up most of the time."
    scene w3_6361 with dissolve
    fel "The plan was to eat afterward. You feeling peckish or can you wait?"
    scene w3_6362 with dissolve
    mc "I can work up an appetite."
    scene w3_6361 with dissolve
    fel "Yeah... I'm sure we'll find ways."
    scene w3_6363 with dissolve

    if feliciaSugarBaby == True:
        fel "Shall we go, boy toy?"
    else:
        fel "Shall we go, stud?"

    scene w3_6364 with dissolve
    mc "Want me to drive?"
    stop music fadeout 3.0
    scene black with fade
    mc "...is what I would say, if I had a license."
    "......"
    "..."
    jump w3FeliciaClothing

label w3FeliciaClothing:
    play music "music/together-with-you.ogg"
    scene w3_6365 with blinds
    mc "Tell me more about this artist."
    scene w3_6366 with dissolve
    fel "What do you want to know?"
    scene w3_6367 with dissolve
    mc "Whatever you think I should know. So I can both get the most out of it and not seem like an uncultured idiot."
    scene w3_6368 with dissolve
    fel "You don't have to pretend like you \"get it\" tonight. At the end of the day, you're just looking at pictures."
    scene w3_6369 with dissolve
    mc "Sure, but the way you looked when you mentioned her earlier has me curious about her."
    scene w3_6370 with dissolve
    fel "Oh, yeah? And what's your read on that?"
    scene w3_6371 with dissolve
    mc "Warm and anxious. It reminded me of a nervous mother or sister or something."
    scene w3_6372 with dissolve
    fel "It's just, uh..."
    scene w3_6373 with dissolve
    "......"
    scene w3_6372 with dissolve
    fel "...her work speaks to me. I'm just hoping the best for a talented woman.."
    scene w3_6374 with dissolve
    mc "...how do I look?"
    scene w3_6375 with dissolve
    "After stuffing myself into layers..."
    scene w3_6376 with dissolve
    mc " It's a bit much, isn't it?"
    scene w3_6375 with dissolve
    fel "Ooooh, [mcf]. You look..."
    scene w3_6376 with dissolve
    mc "Like I'm taking you to prom?"
    scene w3_6377 with dissolve
    fel "I was going to say dashing."
    scene w3_6378 with dissolve
    fel "Dashing, smart, and--"
    scene w3_6379 with dissolve
    mc "Like I'm going after an international gold smuggler?"
    scene w3_6380 with dissolve
    fel "Shut up and take my compliments."
    scene w3_6381 with dissolve

    if feliciaSugarBaby == True and w3FeliciaPlatonic == False:
        mc "Yes, Ma'am."
    else:
        mc "Don't want to. I feel silly."
    scene w3_6382 with dissolve
    fel "...well, you're not wrong on one front."
    scene w3_6383 with dissolve
    mc "What's that?"
    scene w3_6384 with dissolve
    fel "This is WAY overdressed for tonight."
    scene w3_6385 with dissolve
    mc "Then why did you have me try this on?!"
    scene w3_6384 with dissolve
    fel "I wanted to see how you'd look in it."
    scene w3_6386 with dissolve
    mc "You bonafide sadist..."
    scene w3_6387 with dissolve
    fel "Let's try something more... {i}breezy{/i}."
    clerk "What do you have in mind, Mrs. Ford?"
    scene w3_6388 with dissolve
    fel "Let's try that and..."
    fel "Do you have that in his size?"
    clerk "I'll check."
    fel "Please do."
    scene w3_6389 with dissolve
    mc "You're not going to have me try on a dozen outfits are you?"
    scene w3_6390 with dissolve
    fel "Would you tire of me modeling for you?"
    scene w3_6391 with dissolve
    mc "Unlikely."
    scene w3_6392 with dissolve
    "Felicia smiled. {i}Sadistically{/i}."
    scene w3_6393 with dissolve

    if feliciaSugarBaby == True and w3FeliciaPlatonic == False:
        mc "Alright, have your fun."
    else:
        mc "I'll give you six outfits."

    scene w3_6394 with dissolve
    fel "Aww, don't worry. I won't need that many to get you looking like a million bucks."
    scene w3_6395 with dissolve
    "......"
    scene w3_6396 with dissolve
    mc "...and what does Denise's work say when it speaks?"
    scene w3_6397 with dissolve
    fel "Oh, back on that?"
    scene w3_6398 with dissolve
    fel "Well..."
    scene w3_6399 with dissolve
    fel "In my opinion, the best art makes you feel connected. Like you're staring into a mirror and seeing a usually unseen part of yourself bled into a canvas."
    mc "An unseen part...?"
    scene w3_6400 with dissolve
    fel "...y'know, like your {b}gooch{/b} or something!"
    scene w3_6401 with dissolve
    "I took a moment and considered what she meant."
    scene w3_6402 with dissolve
    mc "My Mom has this whole spiel about movie magic. That the beautiful thing about movies is how communal they are."
    scene w3_6403 with dissolve
    mc "That even if you have no one to watch them with, you're viewing a whole group's imagination put out into the world - across borders {i}and{/i} time."
    mc "Said she gets a high thinking about how some haphazard, hasty production from 40 years ago can still resonate with a lady who doesn't speak a lick of Italian."
    mc "{i}Connection{/i}. I get it."
    scene w3_6404 with dissolve
    "......"
    scene w3_6405 with dissolve
    fel "...to answer your question, her work tells me I'm small."
    fel "{i}Makes me believe it too{/i}. That's a new one for me."
    scene w3_6406 with dissolve
    mc "She must be something."
    scene w3_6405 with dissolve
    fel "I'm probably overselling it..."

    if w3FeliciaPlatonic == True:
        scene w3_6418 with dissolve
        clerk "I've found the requested shirt and left it in the dressing room, sir."
        scene w3_6419 with dissolve
        fel "Go change. I have a feeling you're going to look good in gold."
    else:

        scene w3_6407 with dissolve
        "Felicia quickly got {i}cute{/i}..."
        hide screen textbox2 with dissolve

        menu:
            "Don't let her retreat. Make her being earnest into a good thing."(chg=["felicia_up"]):
                $ Felicia_Affection += 1
                scene w3_6408 with dissolve
                show screen textbox2 with dissolve
                mc "Oh, no. Don't backtrack."
                mc "I might not see what you see, but just knowing how it makes you feel is enough to make it {i}fascinating.{/i}"
                scene w3_6409 with dissolve
                mc "Connection, right? From the canvas, to you... from you, to me."
                mc "Tonight's a shared experience. Otherwise, you'd be going alone."
                scene w3_6410 with dissolve
                "........."
                "......"
                scene w3_6411 with dissolve
                fel "...points in your favor."
                scene w3_6412 with dissolve

                if feliciaSugarBaby == True:
                    mc "I'm not vying for--"
                    scene w3_6411 with dissolve
                    fel "You got 'em, deal with 'em."
                else:
                    mc "But I'm not--"
                    scene w3_6411 with dissolve
                    fel "Sorry. You're getting points whether you like it or not."
                    fel "That's the way the world works."

                hide screen textbox2 with dissolve
                scene w3_6410 with dissolve

                menu:
                    "Go for more points. ( kissAttempt = True)":
                        $ kissAttempt = True
                        scene w3_6413 with dissolve
                        show screen textbox2 with dissolve
                        mct "(God, I'm getting full of myself...)"
                        scene w3_6414 with dissolve
                        fel "Mmmhh..."
                        scene w3_6415 with dissolve
                        fel "Don't just kiss me when you feel like it."
                        scene w3_6416 with dissolve
                        mc "You said \"mmmhh\", though."
                        scene w3_6415 with dissolve
                        fel "Even still."
                        scene w3_6417 with dissolve
                        fel "I don't mind the initiative, but there's a time and place."
                        mc "Noted."
                    "Nah. Too public.":

                        show screen textbox2 with dissolve
            "Get physical. Take a stab at being dashing. (kissAttempt = True)":

                $ kissAttempt = True
                scene w3_6413 with dissolve
                show screen textbox2 with dissolve
                "So, I just as quickly pulled Felicia closer and..."
                scene w3_6420 with dissolve
                fel "Don't just kiss me when you feel like it."
                scene w3_6421 with dissolve
                mc "Sorry, it's the suit. Makes me want to kiss you and take over the world. In that order."
                scene w3_6422 with dissolve
                fel "We both know what made you try..."
                scene w3_6417 with dissolve
                fel "Now, I don't mind the initiative, but there's a time and place."
                mc "Noted."
            "Leave it at that.":

                show screen textbox2 with dissolve
                "..."

        scene w3_6418 with dissolve
        clerk "I've found the requested shirt and left it in the dressing room, sir."
        scene w3_6419 with dissolve
        fel "Go change. I have a feeling you're going to look good in gold."

    scene black with fade
    "......"
    "..."
    scene w3_6423 with fade
    fel "Hmmm... {b}nope{/b}."
    scene w3_6424 with dissolve
    "Felicia inspected me closely, wearing her dissatisfaction plainly."
    scene w3_6423 with dissolve
    fel "{b}Too{/b} breezy."
    scene w3_6425 with dissolve
    mc "I feel like a bad rug salesman."
    scene w3_6423 with dissolve
    fel "It's not that bad, stud."
    scene w3_6426 with dissolve
    fel "You {i}could{/i} make it work. What you wear is 75 percent attitude, anyway."
    scene w3_6427 with dissolve
    mc "Oh? And what would it take to get you on this shag carpet today, Miss?"
    scene w3_6428 with dissolve
    fel "Hey. I've heard worse lines, delivered better."
    scene w3_6429 with dissolve
    mc "...and they worked?"
    scene w3_6430 with dissolve
    fel "Maybe. How confidently a man can say stupid, embarrassing things {i}is{/i} {b}something{/b} of a measure."
    scene w3_6428 with dissolve
    fel "I'm curious. If you saw me sitting alone in a bar, would you approach me?"
    scene w3_6429 with dissolve
    mc "Are you asking if I would embarrass myself?"
    scene w3_6428 with dissolve
    fel "I'm asking if you would come up to me. That's all."
    scene w3_6429 with dissolve
    mc "Unlikely."
    scene w3_6428 with dissolve
    fel "And why's that?"
    scene w3_6429 with dissolve
    mc "If you were alone, better men would have tried."
    scene w3_6431 with dissolve
    fel "Is that the you from a few weeks ago or the current you saying that?"
    scene w3_6432 with dissolve
    mc "Are you trying to trip me up?"
    scene w3_6433 with dissolve
    fel "Never, ever. It's just something I've noticed. It's subtle, but you've got a different vibe from the kid that Ian introduced me to."
    fel "It's in the way you stand. The words you choose."
    scene w3_6434 with dissolve
    fel "{i}It's in your eyes{/i}..."
    fel "It's like an absent-minded, apathetic sort of confidence that you don't credit yourself with."
    scene w3_6435 with dissolve
    mct "(...was she trying to build me up?)"
    scene w3_6434 with dissolve
    fel "Better men would have tried? And if everyone had that thought, I'd be lonely."
    scene w3_6436 with dissolve
    fel "{b}Hell,{/b} maybe you'd be the first. That would count for something."
    scene w3_6438 with dissolve

    if w3FeliciaPlatonic == True:
        mc "Are you telling me to keep my head high tonight?"
    else:
        mc "And here we are, though. Life's been working out in my favor."

    scene w3_6439 with dissolve
    fel "Hypothetically... what would you say to me?"
    scene w3_6437 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Could I buy you a drink?":
            scene w3_6441 with dissolve
            show screen textbox2 with dissolve
            mc "I'd ask if I could buy you a drink."
            scene w3_6442 with dissolve
            fel "That's it?"
            scene w3_6443 with dissolve
            mc "Why complicate it? No need to bend over backward trying to come up with something creative or interesting."
            mc "You'd take a look at me and decide for yourself. Que sera sera."
            scene w3_6442 with dissolve
            fel "Whatever will be will be."
            scene w3_6441 with dissolve
            mc "Would you say yes?"
            scene w3_6442 with dissolve
            fel "I don't know. Some college-age boy asking that?"
            fel "It's the kind of thing you can only truly know in the moment."
        "You'd ask if she's waiting on someone.":

            scene w3_6441 with dissolve
            show screen textbox2 with dissolve
            mc "I'd ask if you were waiting on someone."
            scene w3_6442 with dissolve
            fel "A cautious approach..."
            scene w3_6443 with dissolve
            mc "Straight to the point. Why waste anyone's time?"
            scene w3_6442 with dissolve
            fel "That's another way of looking at it, sure."
            scene w3_6441 with dissolve
            mc "And what would you say?"
            scene w3_6442 with dissolve
            fel "I don't know. It's the kind of thing you can only truly know in the moment."

    scene w3_6443 with dissolve
    mc "Then why the hypothetical?"
    scene w3_6442 with dissolve

    if w3FeliciaPlatonic == True:
        fel "I just wanted to know how you'd do it. We never had that step, yet you're my date tonight - even if you are spoken for."
    else:
        fel "I just wanted to know how you'd do it. We never had that step, yet you're my date tonight."

    scene w3_6444 with dissolve
    mc "...do you really think I've changed over the past few weeks?"
    fel "Absolutely, but do you trust my judge of character?"
    mc "It's hard to believe. It's such a short amount of time."
    scene w3_6445 with dissolve
    fel "It takes a billion years to make a diamond naturally, but it only takes one or two weeks to grow one in a lab."
    scene w3_6446 with dissolve
    mc "I feel the same."
    scene w3_6445 with dissolve
    fel "And you never notice yourself putting on the pounds until you're well and fully plump."
    scene w3_6447 with dissolve
    mc "You got a retort for everything?"
    fel "Sure do, stud. Now..."
    scene w3_6448 with dissolve
    fel "Go try the other one on. That's the one you'll be wearing tonight."
    scene w3_6449 with dissolve
    mc "You haven't seen it yet."
    scene w3_6450 with dissolve
    fel "I don't need to. It's got you written all over it."
    stop music fadeout 3.0
    scene black with fade
    "It turned out the third time was the charm."
    jump w3ArtExhibition


label w3ArtExhibition:

    play music "music/speak-the-truth.ogg"
    scene fapan1 with cmet
    show fa_ex1
    $ renpy.pause(1.1, hard=True)
    "A ride out of the city later, we stood in the exhibition venue."
    "A quaint little courtyard pavilion rented out by a neighboring inn."
    mc "To be honest, I was expecting something a bit more... {i}elaborate{/i}?"
    scene fapan2 with dissolve
    show fa_ex2
    $ renpy.pause(1.1, hard=True)
    fel "There's often a disconnect between the people who make the art, the people who peddle it, and the people opening the purse strings."
    mc "So this is something of a middle ground between caviar hors d'oeuvres and a warehouse with dirty needles strewn about?"
    fel "It's a venue suited for the artist. Denise has... {b}trouble{/b} with crowds and confined spaces."
    mc "I see..."
    scene w3_6451 with dissolve
    mc "So, what do you do at these things?"
    scene w3_6452 with dissolve
    fel "Mingle and look at paintings, what else?"
    scene w3_6451 with dissolve
    mc "Which one of those are we starting with?"
    scene w3_6452 with dissolve
    fel "I could do without the first, but it is unfortunately unavoidable."
    scene w3_6451 with dissolve
    mc "That surprises me. This seems like the kind of thing you would like socializing at."
    scene w3_6453 with dissolve
    fel "You'd be mistaken..."
    scene w3_6454 with dissolve
    "Were my eyes deceiving me? There was a tinge of trepidation tugging at the lines of Felicia's beautiful face."
    hide screen textbox2 with dissolve


    menu:
        "Ask why that is.":
            scene w3_6455 with dissolve
            show screen textbox2 with dissolve
            mc "That's a novel look on your face."
            scene w3_6456 with dissolve
            fel "Well, it's not that I mind people being fake as shit; {i}I'm fake as shit{/i}. I'm comfortable with that."
            scene w3_6455 with dissolve
            mc "Why do you look a little uncomfortable then?"
            scene w3_6456 with dissolve
            fel "Because things like this come at the expense of those who are not."
        "Place your hand on the small of Felicia's back."(chg=["felicia_up"]):


            $ Felicia_Affection +=1
            "Uncomfortable social situations had a tried and true remedy."
            show screen textbox2 with dissolve
            scene w3_6457 with dissolve
            mc "Lucky for you, I'm here playing buffer."
            scene w3_6458 with dissolve
            fel "Yeah? You'll stay close then?"
            "--an antidote Felicia was willing to pay for."
            scene w3_6459 with dissolve
            mc "I'll do you one better. I won't let a single snooty remark pass by without derision."
            scene w3_6458 with dissolve
            fel "Quick on the uptake, ain'tcha?"


    scene w3_6460 with dissolve
    "..."
    scene w3_6461 with dissolve
    "And for a moment, Felicia and I stood there, as if staking the place out."
    scene w3_6462 with dissolve
    mc "Do you know many of these people?"
    scene w3_6463 with dissolve
    fel "Too many. Mostly from things like this."
    scene w3_6462 with dissolve
    mc "Need I be concerned about how we come across?"
    scene w3_6463 with dissolve

    if w3FeliciaPlatonic == True:
        fel "There's a degree of separation between these people and my husband. We're good."
    else:
        fel "Unless you're planning on fucking me in front of the fountain, no. There's a degree of separation between these people and my husband."
        fel "Just act like you're in polite society."

    mc "Got it."

    if feliciaSugarBaby == True and w3FeliciaPlatonic == False:
        fel "Points for mindfulness."
    else:
        fel "It's good you're mindful of that."

    scene w3_6462 with dissolve
    mc "Well, it wasn't a real question. I doubt you would bring me to something that would blow up in your face."
    scene w3_6463 with dissolve
    fel "Who knows about that. If I was so cautious, I wouldn't be at the club now, would I?"
    fel "I'm more stupid than I let on."
    scene w3_6462 with dissolve
    mc "Ditto. Saaaaame."
    scene w3_6464 with dissolve
    mcfel "......"
    scene w3_6465 with dissolve
    fel "I've got to go say hello."
    mc "...?"
    scene w3_6466 with dissolve
    "I followed where Felicia was looking, to a man who was smiling expectantly."
    fel "Come on."
    mc "Who's he?"
    fel "Raymond Saint-Clair. He's a friend."
    scene w3_6467 with dissolve
    mc "Like a {i}friend{/i} friend?"
    fel "Just **a** friend. He's the one who set this up."
    mc "Saint-Clair, eh? Was he born for this?"
    scene w3_6468 with dissolve
    fel "Hardly. His real surname is Cockburn."
    mc "No, it's not."
    fel "Yes, {b}it is{/b}. Try not to laugh, stud."
    mc "How do you expect me to look him in the eye and--"
    scene w3_6469 with dissolve
    ray "Felicia, dear! Hey!"
    fel "Raaaaaymond!"
    scene w3_6470 with dissolve
    ray "Muaah!"
    ray "I knew you would show! You said you weren't, but I-"
    scene w3_6471 with dissolve
    fel "...{b}knew!{/b} No surprise there. What is it you like to say? People are...?"
    ray "{b}My subject{/b}. I'm a purveyor of man."
    scene w3_6472 with dissolve
    mct "(Oh, god...)"
    "I did my best not to laugh. I had enough \"purveyors\" of man in my life thanks to the club."
    scene w3_6473 with dissolve
    ray "And who is this drink of water, Felish?"
    fel "My date tonight, Ray. This is [mcf]."
    scene w3_6474 with dissolve
    ray "How do you do, young man?"
    mc "Uh..."
    scene w3_6475 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Kiss it...? (w3RayKiss = True)"(chg=["felicia_up"]):
            $ w3RayKiss = True
            $ Felicia_Affection += 1
            "It seemed like the thing to do...?"
            scene w3_6476 with dissolve
            show screen textbox2 with dissolve
            mc "Hello."
            ray "Oooh! That's weird!"
            scene w3_6477 with dissolve
            ray "He's a different sort, isn't he?"
            scene w3_6478 with dissolve
            "......"
            "...why did he offer his hand like that then?!"
            scene w3_6479 with dissolve
            fel "You have no idea."
        "Shake his hand.":

            scene w3_6480 with dissolve
            show screen textbox2 with dissolve
            mc "Nice to meet you, Raymond."
            "It was an awkward sort of handshake. I didn't say \"charmed\" and he didn't curtsy."


    scene w3_6481 with dissolve
    ray "Are you familiar with Denise's work?"
    scene w3_6482 with dissolve
    mc "I'm not really an art per--"
    scene w3_6483 with dissolve
    fel "He's here as my date tonight, and to look. {b}Not buy.{/b}"
    fel "No need to sell him. Speaking of, how is our girl tonight?"
    scene w3_6484 with dissolve
    ray "Mmmh... {i}hard to say.{/i} She's done a round or two with the guests, but she's made herself annoyingly sparse."
    ray "I mean, I'm relying on that \"wallflower\" thing as her hook, but that only works if she stands around awkwardly where people can see her."
    scene w3_6485 with dissolve
    mct "(...?!)"
    "I felt Felicia's nails dig into my skin, and I immediately marveled at how a woman could possess a herculean grip."
    fel "...is that so? Huh!"
    scene w3_6486 with dissolve
    "All unbeknownst to Raymond, as Felicia looked him dead in the eye, completely unperturbed."
    scene w3_6487 with dissolve
    fel "Well, I'm sure her work speaks for itself."
    scene w3_6488 with dissolve
    ray "Don't get me wrong, she {i}is{/i} talented and I'm glad you pointed me in her direction, but you know how it is. Talent is abound, and {i}stories{/i} are what sell."
    ray "Her {b}face{/b} is the story."
    scene w3_6489 with dissolve
    "Again, Felicia squeezed, letting me and me alone know her frustration."
    hide screen textbox2 with dissolve

    menu:
        "Keep your mouth shut and look pretty.":
            scene w3_6490 with dissolve
            "Eh. I don't know shit about art."
            scene w3_6495 with dissolve
            fel "{i}Other{/i} than that, how are people taking to the work? Positive things, I hope..."
        "Interject."(chg=["felicia_up"]):

            $ Felicia_Affection +=1
            scene w3_6491 with dissolve
            mc "Forgive me, I'm a novice when it comes to this stuff, but..."
            "I briefly looked at Felicia, and was encouraged by her curious gaze."
            scene w3_6492 with dissolve
            mc "There's more to tonight than just selling paintings, isn't there? Like, say..."
            "I recalled Felicia's own words."
            mc "The public connecting with art?"
            scene w3_6493 with dissolve
            ray "..."
            scene w3_6494 with dissolve
            ray "Of course! Of course! I'm just speaking from the business point of view, of course!"
            ray "Sometimes that hat gets stuck on too tight."
            scene w3_6495 with dissolve
            fel "...other than that, how are people taking to the work? Positive things, I hope..."

    scene w3_6496 with dissolve
    ray "Elizabeth Averell is here tonight."
    scene w3_6497 with dissolve
    fel "{b}Huh...{/b} this is a small thing. It {i}normally{/i} wouldn't get traction in the papers."
    fel "Slow month, maybe?"
    scene w3_6498 with dissolve
    ray "I may have had a hand in that. I let slip that Felicia Ford discovered a new artist--"
    scene w3_6499 with dissolve
    fel "You idiot!"
    fel "You... you... BLATHERING idiot! You {b}know{/b} I embarrassed that harpy at the Marie-Thompson event! "
    scene w3_6500 with dissolve
    ray "All press is good press, Felish. One way or another, they'll be talking about your girl. That's a good thing in the long run..."
    ray "Besides, Liza wouldn't let her personal feelings-"
    scene w3_6501 with dissolve
    "He stopped himself."
    scene w3_6502 with dissolve
    ray "Oh, who am I kidding? Maybe it's not too late to apologize."
    scene w3_6503 with dissolve
    "Felicia's expression read like she was about to close the distance and smack him, but her feet remained firmly planted in place."

    menu:
        "Put a comforting hand on her back."(chg=["felicia_up"]):
            $ Felicia_Affection += 1
            scene w3_6504 with dissolve
            "Just a small reminder she wasn't beset on all sides."
            scene w3_6505 with dissolve
            fel "Ugh... fuck you and your business, but..."
            "She took a moment."
            fel "I know you're just doing your job."
        "Ask who the woman is.":

            scene w3_6506 with dissolve
            mc "Who is Elizabeth Averell?"
            "Contextually, it was a good guess she was a critic, but a momentary distraction felt needed..."
            scene w3_6507 with dissolve
            fel "She writes hit pieces for the Morehead Times."
            scene w3_6508 with dissolve
            ray "Come on, she reviews art."
            scene w3_6507 with dissolve
            fel "She's a talentless hack that hides her lack of value behind glib commentary."
            scene w3_6508 with dissolve
            ray "Careful Felish, she might just hear you..."
            scene w3_6509 with dissolve
            fel "*Sigh* Ah, fuck you, Ray..."
        "She's a big girl. She doesn't need coddling.":

            scene w3_6510 with dissolve
            "......"
            "..."
            scene w3_6511 with dissolve
            fel "Fuck you, Raaaaaay."
            ray "Not sorry."
            fel "Yeah... no shit."

    scene w3_6512 with dissolve
    "Despite Felicia's displeasure, the two were comfortable enough with each other to speak plainly."
    ray "And who knows? Don't be grim. Denise is great. Maybe she'll be more kind than usual?"
    fel "Who ARE you kidding?"
    scene w3_6513 with dissolve
    ray "Tonight's a stepping stone. Denise will have dozens of shows by the time she's old and grey and Liza will just be a drop in the bucket."
    scene w3_6514 with dissolve
    fel "Without a doubt..."
    scene w3_6515 with dissolve
    ray "Want me to give you the rundown?"
    scene w3_6516 with dissolve
    fel "Do you think you talking in my ear is the way I want to first take in tonight's new work?"
    scene w3_6517 with dissolve
    ray "Hell no."
    scene w3_6516 with dissolve
    fel "Besides, it's too crowded. We're going to mingle a bit."
    scene w3_6517 with dissolve
    ray "You mean you're going to go smoke where you shouldn't, like a teenage girl?"
    scene w3_6516 with dissolve
    fel "You a narc?"
    scene w3_6518 with dissolve
    ray "Then I should get back out there. The hat's been off for too long."
    scene w3_6519 with dissolve
    mc "Interesting guy..."

    if w3RayKiss == True:
        scene w3_6520 with dissolve
        fel "Yeah, I'd say. You gave him a kiss!"
        scene w3_6521 with dissolve
        mc "I didn't know what to do!"

    scene w3_6520 with dissolve
    fel "Well, you're not wrong. He has his ups and downs, but he takes risks on young artists. I'm thankful for that."
    stop music fadeout 3.0
    scene w3_6522 with dissolve
    fel "Still, every time I speak to him, I'm reminded of why I gave slobbering on rich knobs a college try."
    mc "He said you pointed him in Denise's direction?"
    play music "music/georges-lament.ogg"
    scene w3_6523 with dissolve
    fel "I mentioned her once or twice. Or three times. {i}Low key.{/i}"
    mc "...but you're not friends with her?"
    fel "Again, never spoken."
    scene w3_6524 with dissolve
    mc "He must trust your eye for talent."
    fel "Art is a social construct, for better and worse - and, wouldn't you know it, I'm a valued customer."
    mc "Your expertise extends further than that, right? You won a national award for a painting!"
    scene w3_6525 with dissolve
    fel "Eh, join the club. That was more than 15 years ago."
    fel "All he needed to do was look to realize the girl has talent."
    scene w3_6526 with dissolve
    mc "......"
    scene w3_6527 with dissolve
    mc "...I'm curious about your own work now."
    scene w3_6528 with dissolve
    fel "Work is overly generous. There's only the one \"out there\", stud.."
    scene w3_6527 with dissolve
    mc "What was your winning painting of?"
    scene w3_6529 with dissolve
    fel "You can see it yourself if you want. There's a photo of it on the Future Artists of America's website."
    fel "Just {i}please{/i} don't pull out your phone to check. Wait until tomorrow, when I'm not sitting next to you."
    scene w3_6531 with dissolve
    mc "What? To save you the embarrassment?"
    scene w3_6529 with dissolve
    fel "Not because of the painting, mind you. Every year's winner includes a submitted essay."
    scene w3_6530 with dissolve
    mct "(Now I'm even more curious...)"
    scene w3_6531 with dissolve
    mc "No shit? What did you write about?"
    scene w3_6529 with dissolve
    fel "A bunch of words that amount to teenage rambling."
    scene w3_6527 with dissolve
    mc "It's hard to imagine what you were like as a young girl..."
    scene w3_6532 with dissolve
    fel "You should have a decent picture by now, [mcf]. Especially after Kat's show."
    fel "Fill in the blanks with your imagination. That's more fun than the reality of it."
    scene w3_6533 with dissolve
    mc "You sure you want that? Because my imagination includes rhinestone cloth--."
    scene w3_6534 with dissolve
    fel "Well, here it comes."
    fel "{size=-10}Brace for impact, Felicia.{/size}"
    $ renpy.music.set_volume(.1, 1, channel = "music")
    scene w3_6535 with dissolve
    "With barely any time to speak, another person showed up."
    woman "Mrs. Ford! I haven't seen you at one of Ray's showings in months! Not since our {i}spirited{/i} debate."
    scene w3_6536 with dissolve
    "The critic, I presumed."
    liza "I've missed your bohemian takes on certain matters."
    scene w3_6537 with dissolve
    fel "I should apologize for last time. I went overboard. You know how I am."
    scene w3_6538 with dissolve
    "To my surprise, Felicia mustered up an expression of contriteness."
    scene w3_6537 with dissolve
    fel "...what is it that you said? What I lack in education is made up in enthusiasm?"
    scene w3_6538 with dissolve
    "There was no \"but\" or backhanded element to it, either."
    scene w3_6537 with dissolve
    fel "Sometimes I mistake being loud as being correct."
    scene w3_6538 with dissolve
    "Just a sublimation of ego."
    scene w3_6539 with dissolve
    liza "Water under the bridge. You're a passionate woman, it's hardly anything to apologize for."
    scene w3_6540 with dissolve
    fel "...how are you enjoying tonight?"
    scene w3_6541 with dissolve
    liza "The night's been on the... {i}mundane{/i} side."
    scene w3_6543 with dissolve
    fel "What do you mean?"
    scene w3_6541 with dissolve
    liza "The technique is all over the place, not to mention the wasted brush stroke a plenty."
    "...yet she mentioned it."
    scene w3_6542 with dissolve
    liza "I was hoping to speak to the artist about it, but she seems to have better things to do. Usually artists hover over their work."
    scene w3_6541 with dissolve
    liza "It shows that they care..."
    scene w3_6543 with dissolve
    fel "Maybe she prefers to let the work speak for itself?"
    scene w3_6542 with dissolve
    liza "She should reconsider that approach, because all I'm hearing is obvious and uninspired."
    "To my further surprise, Felicia didn't bite back. She held her tongue, like the professional adulator she was."
    scene w3_6543 with dissolve
    fel "Maybe if you give it time, you'll find some other meaning."
    scene w3_6541 with dissolve
    liza "{b}Perhaps{/b}."
    scene w3_6544 with dissolve
    "........."
    "......"
    "..."
    scene w3_6545 with dissolve
    liza "Oh, Amanda's here. I got to go say hi."
    fel "It was nice seeing you, Liza."
    scene w3_6546 with dissolve
    liza "I agree."
    scene w3_6547 with dissolve
    "..."
    $ renpy.music.set_volume(1, 3, channel = "music")
    scene w3_6548 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Insult the critic.":
            scene w3_6549 with dissolve
            show screen textbox2 with dissolve
            mc "Seems like a cunt."
            scene w3_6550 with dissolve
            fel "If that was all she was, she'd be a dime-a-dozen."
        "Remark on their history.":

            scene w3_6549 with dissolve
            show screen textbox2 with dissolve
            mc "Did I just meet your adversary?"
            scene w3_6550 with dissolve
            fel "More like a thorn. I forget she even exists until I feel the prick."
            scene w3_6549 with dissolve
            mc "There's a joke in there somewhere..."


    if w3FeliciaPlatonic == True:
        scene w3_6551 with dissolve
        fel "I think I need a smoke."
        scene w3_6552 with dissolve
        mc "Sure, but where?"
        scene w3_6553 with dissolve
        fel "Good question... somewhere out of sight..."
        scene w3_6554 with dissolve
        mc "Raymond guessed it, huh?"
    else:

        scene w3_6555 with dissolve
        fel "Come on, I need a smoke."
        scene w3_6556 with dissolve
        mc "Sure, but where?"
        scene w3_6557 with dissolve
        fel "Somewhere... {b}private{/b}. Where no one will give us the stink eye for doing something we shouldn't."
        "I knew that look..."
        mc "Funny. {i}Us{/i}, when I'm not the one who'll be smoking..."

    scene black with fade
    fel "Hmmm... this shoul--"
    scene w3_6558 with cmet
    "Our pinpointed hideaway wasn't so hidden away, but we didn't move on."
    fel "Ah..."
    "Instead, Felicia stood in the doorway, awkwardly transfixed on the back of the unexpected occupant."
    "Clearly underway with a bit of sleuthing or calculating..."
    "The question was: was this someone she knew or was that what she was actively trying to figure out?"
    scene w3_6559 with dissolve
    mc "...Felicia?"
    scene w3_6560 with dissolve
    woman "Oh! Uh..."
    scene w3_6561 with dissolve
    "My whisper might as well have been a bark, judging by the way the woman immediately tensed up and stood on guard."
    "Yet still, not one of us - Felicia, myself, or this stranger - course corrected away from the blaring silence."
    "Not for a little while at least."
    scene w3_6562 with dissolve
    "......"
    scene w3_6563 with dissolve
    "..."
    scene w3_6564 with dissolve
    woman "Excuse me..."
    scene w3_6565 with dissolve
    "Felicia's soft expression instantly narrowed down the answer to my question."
    scene w3_6566 with dissolve
    fel "S-sorry. Go ahead."
    "And the way Felicia girlishly stammered clued me into the stranger's identity."
    scene w3_6567 with dissolve
    woman "It's alright..."
    scene w3_6568 with dissolve
    "A brief, clumsy exchange that concluded just as soon as it started."
    scene w3_6569 with dissolve
    mct "(Huh...)"
    scene black with fade
    fel "...come on."
    scene w3_6570 with dissolve
    mc "So, that was Denise?"
    scene w3_6571 with dissolve
    fel "It was."
    scene w3_6572 with dissolve
    mc "I guess we blew up her hiding spot."
    scene w3_6573 with dissolve
    fel "Heh. We must have."
    scene w3_6572 with dissolve
    mc "You didn't say anything to her."
    scene w3_6574 with dissolve
    fel "Untrue. I apologized for being in the way."
    scene w3_6575 with dissolve
    mc "I guess I expected a few more words than that, considering how invested you are in tonight."
    mc "I mean, you should at least introduce yourself, right?"
    scene w3_6576 with dissolve
    "I returned to our earlier exchange in the dressing room."
    fel "I'm not going to do that."
    "--except this time, her \"I'm not sure\" took a more definite spin."
    scene w3_6577 with dissolve
    mc "No...?"
    scene w3_6578 with dissolve
    fel "I barely understand it myself."
    scene w3_6579 with dissolve
    mc "I doubt that."
    scene w3_6580 with dissolve
    fel "What would I say?"
    scene w3_6581 with dissolve
    mc "I love your work could be a good place to start."
    scene w3_6582 with dissolve
    fel "Those would be meaningless words from yet another fake, rich old woman selfishly suckling at something more {b}alive.{/b}"
    scene w3_6583 with dissolve
    "She said all that without a hint of self-loathing or disgrace, but rather as if it was a self-evident truth."
    scene w3_6582 with dissolve
    fel "She's flooded with 'em. I'd just be a bother."
    scene w3_6584 with dissolve
    "This seemed an unusual pain point for Felicia, a far cry from her effortlessly employed social graces."
    scene w3_6583 with dissolve
    mct "(...was she feeling {i}shy{/i}?)"
    hide screen textbox2 with dissolve

    menu:
        "Use a bit of verbal judo.":
            scene w3_6585 with dissolve
            show screen textbox2 with dissolve
            mc "...or maybe she'll think \"Hey, cool. I made something that connected with someone.\" That's the entire point of showing your art publicly, isn't it?"
        "Tease her, bluntly.":

            scene w3_6580 with dissolve
            show screen textbox2 with dissolve
            mc "Ha! You're acting like a shy little fan girl, afraid of looking lame!"

    scene w3_6587 with dissolve
    fel "The thing is, enjoying something from afar can be enough. Sometimes more is... {i}inadequate.{/i}"
    scene w3_6579 with dissolve
    mc "{i}Inadequate?{/i} How so?"
    scene w3_6580 with dissolve
    fel "It's... {i}never{/i} as good as you hope. What you imagine you'll get out of it is... {i}rarely{/i} matched by reality."
    scene w3_6581 with dissolve
    mc "Is this a \"don't meet your heroes\" sort of thing?"
    scene w3_6587 with dissolve
    fel "Hero feels like too strong of a word, but maybe that's what it is."
    scene w3_6579 with dissolve
    mc "Sometimes reality can surprise you in a positive way too, can't it?"
    scene w3_6587 with dissolve
    fel "Sure..."
    scene w3_6579 with dissolve
    mc "What is it that you admire about this woman? Her skill?"
    scene w3_6587 with dissolve
    fel "The road not taken."
    scene w3_6585 with dissolve
    mc "...I don't follow."
    scene w3_6582 with dissolve
    fel "She just... {i}fascinates{/i} me, on a personal level."
    scene w3_6588 with dissolve
    "........."
    "......"
    scene w3_6589 with dissolve
    "...the conversation dissipated like the smoke rising out the end of her cigarette."
    scene w3_6590 with dissolve
    "Absent the draw of conversation, shoulder-to-shoulder, I felt more aesthetic."
    scene w3_6591 with dissolve
    "The shadow cast by the evening's dying light subdued Felicia's golden tresses and transformed her perfectly tanned skin into a canvas for the candle's glow."
    scene w3_6592 with dissolve
    "With every puff, it was as if the end of her very fingers was combusting and smoking the sky itself."
    scene w3_6590 with dissolve
    "For just a fleeting moment, between an inclination and an urge, I wanted to do something {b}stupid.{/b}"
    hide screen textbox2 with dissolve

    menu:
        "Ask to take a draw."(chg=["felicia_up"]):
            $ Felicia_Affection += 1
            mc "...can I try that?"
            scene w3_6593 with dissolve
            show screen textbox2 with dissolve
            "Felicia answered my question by looking at me dumbly, as if not understanding what those four words meant in this specific context."
            scene w3_6594 with dissolve
            fel "...you want to {i}smoke?{/i}"
            scene w3_6593 with dissolve
            mc "{b}Yeah.{/b}"
            scene w3_6595 with dissolve
            fel "No!"
            scene w3_6596 with dissolve
            "She was {b}emphatic.{/b}"
            scene w3_6595 with dissolve
            fel "I'm not going to be responsible for you picking up this filthy habit!"
            scene w3_6596 with dissolve
            mc "I'm not stupid, Felicia. I don't plan on making it a recurring thing, I just want to... {i}try it once.{/i}"
            scene w3_6597 with dissolve
            "I stopped short of proclaiming it was \"for the vibes\", to avoid running counterpoint to my claim of intelligence."
            mc "Y'know, just to say that I have..."
            scene w3_6598 with dissolve
            fel "I mean... I can't stop you. I'm not your mother."
            scene w3_6597 with dissolve
            mc "Can we share that one...?"
            scene w3_6599 with dissolve
            fel "What's this, are you trying to turn this into a moment? Points for vision, at least."
            scene w3_6600 with dissolve
            mc "I don't want to waste one. {b}That's all.{/b}"
            scene w3_6601 with dissolve
            mct "(What was I doing...?)"
            "It smelled bad."
            scene w3_6602 with dissolve
            "It tasted bitter."
            "Different from the cigar I tried in the sauna, but still wholly unappetizing."
            scene w3_6603 with dissolve
            "The smoke burned my lungs in a similar way too-"
            scene w3_6604 with dissolve
            mc "*Cough* Ahehhm, eehhh."
            fel "See? Bad idea, stud."
            mc "If you tell me it's a bad idea it must be."
            scene w3_6605 with dissolve
            "Yeah... this was disgusting..."
            scene w3_6606 with dissolve
            if feliciaSugarBaby == True and w3FeliciaPlatonic == False:
                fel "Mama knows best."
                scene w3_6607 with dissolve
                mc "You like trying that on for size?"
            else:
                fel "Right? Do as I say, not as I do."
                scene w3_6607 with dissolve
                mc "You said you weren't my mother."
                scene w3_6606 with dissolve
                fel "Should I make you smoke a whole pack until you're sick?"
            scene w3_6608 with dissolve
            mc "I would've figured you smoked menthols."
            fel "Don't insult me."
            "......"
            "..."
            jump w3FeliciaDuoSmoke
        "No way. Push aside the impulse.":

            jump w3FeliciaSmoke


label w3FeliciaDuoSmoke:
    scene w3_6609 with fade
    "A couple of minutes passed, and while the act remained unpleasant, there was something about the warmth and proximity with Felicia that felt {i}right.{/i}"
    "The awkward gaps of time where words failed or an idea floundered, were hidden behind puffs of smoke, ensconced by peering eyes and the sensual act of sharing a smoke."
    scene w3_6610 with dissolve
    fel "You ever get a blowjob with a menthol drop?"
    scene w3_6611 with dissolve
    mc "Of course, I haven't. {b}Most people{/b} haven't."
    mc "Like the overwhelming majority haven't."
    scene w3_6610 with dissolve
    fel "That's a shame."
    scene w3_6611 with dissolve
    mc "...I bet it feels good?"
    scene w3_6610 with dissolve
    fel "It can take some getting used to -- finding the right amount, I mean."
    scene w3_6612 with dissolve
    fel "If we're talking cream, the same application has different effects on men and women, but..."
    scene w3_6610 with dissolve
    fel "{b}Yeah.{/b} You should try it sometime."

    if w3FeliciaPlatonic == True:
        "Was that her way of ribbing me over the asinine \"no sex\" proclamation?"
        scene w3_6611 with dissolve
        mc "Is that in your top 10 tips for spicing up your sex life, Ms. Cosmopolitan?"
        scene w3_6610 with dissolve
        fel "Shut up."
    else:
        scene w3_6611 with dissolve
        mc "{i}Yeah.{/i} We should..."

    scene w3_6609 with dissolve
    "......"
    scene w3_6613 with dissolve
    "..."
    scene w3_6614 with dissolve
    fel "So, do you normally make impulsively bad decisions to impress a girl?"
    scene w3_6615 with dissolve
    mc "Well, let me ask you the only question that matters: do I look cool right now?"
    scene w3_6614 with dissolve
    fel "No."
    scene w3_6616 with dissolve
    mc "What if I hold it like this?"
    scene w3_6617 with dissolve
    fel "Wait, hold on. {b}Stop{/b}."
    scene w3_6618 with dissolve
    "......"
    "..."
    scene w3_6617 with dissolve
    fel "My God. If anyone sees you hold it like {b}that{/b}, you'll be in danger of them wanting to sleep with you."
    scene w3_6619 with dissolve
    mc "I thought so. I must wield this power responsibly."
    "......"
    scene w3_6620 with dissolve
    fel "...you're corny."
    mc "And don't forget lame."
    scene w3_6621 with dissolve
    "......"
    scene w3_6622 with dissolve
    "..."
    scene w3_6623 with dissolve
    mc "Ffffeeee~"
    "A playful billow of smoke tickled my nose and aggravated my nostrils."
    scene w3_6624 with dissolve
    mc "*Cough* Ahemm..."
    scene w3_6625 with dissolve
    fel "You look quite handsome tonight, [mcf]."
    scene w3_6626 with dissolve
    mc "You had a hand in it. Got it in three tries."
    scene w3_6625 with dissolve
    fel "We'll call it a joint effort."
    scene w3_6627 with dissolve
    mc "*Ahem* Ahh, y-yeah--"
    fel "Give me that."
    scene w3_6628 with dissolve
    fel "I take it back. I may not be your mother, but I am your date."
    fel "It doesn't suit your charms."
    scene w3_6629 with dissolve
    mc "The absent-minded, apathetic charms?"
    scene w3_6628 with dissolve
    fel "No. Your boyish ones."
    scene w3_6630 with dissolve
    "......"
    "..."
    jump w3FelSmokeEnding

label w3FeliciaSmoke:
    scene w3_6608 with dissolve
    "{i}As if.{/i}"
    "I'm going to be a doctor for fuck's sake."
    mc "You should quit."
    scene w3_6612 with dissolve
    fel "No, thanks. It's one of my three pleasures in this world."
    scene w3_6611 with dissolve
    mc "What's the other two?"
    scene w3_6610 with dissolve
    fel "Take a guess."
    scene w3_6611 with dissolve
    mc "Fucking, painting, and smoking?"
    scene w3_6612 with dissolve
    fel "Now, aren't I a complicated woman?"
    scene w3_6611 with dissolve
    mc "You're good at obfuscating it, at least. Ms. Hierarchy of Needs."
    scene w3_6610 with dissolve
    fel "Ah, you remembered my bullshit?"
    scene w3_6629 with dissolve
    mc "You left an impression and you know it, Felicia."
    mc "Not many women rattle off like that while jerking a cock in a public park."
    scene w3_6630 with dissolve
    mct "(That would make for some fine wedding vows...)"
    scene w3_6628 with dissolve
    fel "Impressions are my bread n' butter..."
    scene w3_6630 with dissolve
    "That look was a critical hit..."
    "......"
    "..."

    if w3FeliciaPlatonic == True:
        "Was that her way of ribbing me over the asinine \"no sex\" proclamation?"

    jump w3FelSmokeEnding


label w3FelSmokeEnding:
    scene w3_6631 with dissolve
    fel "So, Stud, what's your idea of a satisfying date?"
    mc "Where's that coming from?"
    fel "Well, you found the courage to ask me out at the bar, didn't you? That's the natural progression here."
    scene w3_6632 with dissolve
    mc "You're asking what my \"dream\" date is?"
    scene w3_6633 with dissolve
    fel "I'm wondering what you'd call a really good one. What's the shape of it? What's the feel?"
    scene w3_6632 with dissolve
    mc "I'm not really a discerning dater, Felicia. You could even say I'm easy to please."
    scene w3_6634 with dissolve
    fel "Eugh. Even if that is true, you shouldn't let the person taking you out know it."
    scene w3_6635 with dissolve
    mc "No?"
    scene w3_6634 with dissolve
    fel "{b}No.{/} For one, you shouldn't make it {i}too{/i} easy for the other person."
    scene w3_6635 with dissolve
    mc "Yeah, right..."
    scene w3_6638 with dissolve
    fel "Because it gets them used to not having to consider your wants and needs."
    scene w3_6636 with dissolve
    mc "The thing is, I'm a guy. Typically I'd be on the other side of things..."
    scene w3_6638 with dissolve
    fel "It works both ways, Stud. Even if you're in the driver's seat."
    scene w3_6633 with dissolve
    fel "Having wants and being clear on them not only sets expectations, it establishes respect."
    scene w3_6632 with dissolve
    mc "...you like lecturing about life, don't you?"
    scene w3_6637 with dissolve
    fel "To your point, I'm not usually on this side of things either. I'm having... {i}fun.{/i}"
    scene w3_6632 with dissolve
    mc "...good."
    scene w3_6633 with dissolve
    fel "...but there is a practical dimension to the question."

    if w3FeliciaPlatonic == False and feliciaSugarBaby == True:
        fel "After all, there might be more of these in the future..."
    elif w3FeliciaPlatonic == False and feliciaSugarBaby == False:
        fel "After all, there could be a next time for this..."
    else:
        fel "The night's just beginning, is it?"

    scene w3_6639 with dissolve
    "Felicia's eyes pushed me for an answer to her question."
    "What was it again? The shape and feel of a good date?"
    hide screen textbox2 with dissolve

    menu:
        "You prefer staying in.":
            scene w3_6636 with dissolve
            show screen textbox2 with dissolve
            mc "It might be boring, but I prefer something cozy over flashy."
            scene w3_6638 with dissolve
            fel "You're a stay-at-home kinda guy, huh? Curl up on the couch with a movie?"
            scene w3_6635 with dissolve
            mc "Would admitting that mean I'm making it too easy?"
            scene w3_6638 with dissolve
            fel "Not exactly. A cabin vacation might be fun, right?"
            scene w3_6632 with dissolve
            mc "Yeah... I could see myself enjoying something like that. That's a good one."
            scene w3_6637 with dissolve
            fel "See? You can be easygoing and manifest it in a directed way."
        "The thought of having a night out has been growing on you.":

            scene w3_6636 with dissolve
            show screen textbox2 with dissolve
            mc "You know, normally I prefer staying in, but I don't know..."
            mc "I'm starting to get a taste for stuff like this. Moving about has its appeal."
            scene w3_6637 with dissolve
            fel "Pfft, yeah? That's not specific."
            scene w3_6632 with dissolve
            mc "Alright, {i}specific{/i}. A good dinner. Some place loud that makes it easy not to think too hard. Some place quiet afterwards, after the ice has thawed, to get closer to the other person."
            mc "Something like that, I guess?"
            scene w3_6634 with dissolve
            fel "Hmm..."
            "......"
            fel "...still not specific, but I'll take it."
            scene w3_6632 with dissolve
            mc "I appreciate your magnanimity."

    scene w3_6639 with dissolve
    "......"
    scene w3_6640 with dissolve
    mc "...so, are we going to hide for the rest of the night?"
    scene w3_6641 with dissolve
    fel "We'll make a daring jailbreak soon enough. In a few more minutes."
    scene w3_6642 with dissolve
    fel "...not yet, though."
    scene w3_6643 with dissolve
    "Some time passed, without a word passing between us."
    "Just the two of us, comfortably basking in the summer shade, while the cigarette resting between Felicia's fingers slowly dwindled alongside the evening's light."
    "......"
    "..."
    stop music fadeout 3.0
    scene black with fade
    mc "I gotta go to the bathroom."
    fel "I'll be here, Stud."
    jump w3LucyMeet

label w3LucyMeet:
    play music "music/sonatina-in-c-minor.ogg"
    scene w3_6644 with blinds
    "One empty bladder later...."
    "On the way back, I found myself scanning the courtyard."
    scene w3_6645 with dissolve
    mct "(Looks like it's cleared out quite a bit...)"
    "I should fetch Felicia."
    scene w3_6646 with dissolve
    "......"
    mct "(...wait, is that?)"
    mct "(No way...)"
    scene w3_6647 with dissolve
    "It {b}was{/b} her."
    mct "(Why is Lucy here?!)"
    "Had she noticed me...?"
    "She sat alone at the fountain's edge, conspicuously looking at nothing at all, as if she was avoiding acknowledging me."
    scene w3_6648 with dissolve
    "However, a furtive glance gave her away."
    "The moment we caught each other's gaze, she returned my look of shock with what could only be described as an \"oh shit\" face."
    scene w3_6649 with dissolve
    "Yet, realizing she was gawking, she quickly changed tune, getting up and plastering a weak smile on her face."
    scene w3_6650 with dissolve
    lucy "Uh... hi."
    scene w3_6651 with dissolve
    mc "It's a small world, huh?"
    scene w3_6650 with dissolve
    lucy "Y-yeah... isn't it?"
    scene w3_6652 with dissolve
    "Lucy looked visibly uncomfortable to be meeting face-to-face, but that wasn't all that surprising considering our connection."
    "{b}What did surprise me though was...{/b}"
    scene w3_6653 with dissolve
    mct "(Hot damn.)"
    "The raven-haired teacher's tits were spilling out her top and the split in her skirt was so daring that it was fit for a..."
    hide screen textbox2 with dissolve
    scene w3_6654 with dissolve
    mc "What are you doing here?"
    scene w3_6655 with dissolve
    "Well, {i}her other job.{/i}"
    scene w3_6656 with dissolve
    lucy "I'm... on... a... {b}date.{/b}"
    scene w3_6657 with dissolve
    mc "Oh, with your husband?"
    scene w3_6658 with dissolve
    lucy "......"
    scene w3_6659 with dissolve
    lucy "...{i}nooooooo.{/i}"
    scene w3_6660 with dissolve
    mc "Aha..."
    "She was {b}working.{/b}"
    scene w3_6658 with dissolve
    "......"
    "..."
    scene w3_6657 with dissolve
    mc "You and I have never spoken one-on-one, have we?"
    scene w3_6655 with dissolve
    "The silence was so suffocating that I spewed, in a bid to break it, the first dumb observation that crossed my frontal lobe."
    scene w3_6656 with dissolve
    lucy "I don't believe we have, no..."
    scene w3_6661 with dissolve
    "Outside of the club, and on a weekday no less..."
    scene w3_6658 with dissolve
    mct "(August has the teacher fully whored out...)"
    scene w3_6660 with dissolve
    mc "Kinda funny we've never had the chance, considering how often--"
    scene w3_6658 with dissolve
    "Lucy's nervousness tripled, as if our little conversation might betray her moonlighting to the world of decent folk. Or, perhaps..."
    scene w3_6657 with dissolve
    mc "Are you alright?"
    scene w3_6655 with dissolve
    "Then again, it was quite the coincidence to run into her with a customer..."
    scene w3_6656 with dissolve
    lucy "I'm with.. mmmmmh, I'm... uh..."
    scene w3_6661 with dissolve
    "...but maybe not an inordinate one?"
    scene black with dissolve
    m_dev "Just a moment my master wanted me to explain something to you."
    m_dev "Lucy (arrow up image) will represent \"Lucy's Affability\" points."
    m_dev "Lucy (flame image} will represent \"Lucy's Pressure\" points."
    m_dev "It's recommanded to get atleast 4 of either which you choose determines the scenes you get."
    m_dev "{m_note} Recommended to stick to one \"path\"."
    m_dev "So choose accordingly, For example for a more \"caring/understanding\" scene pick Affability"
    m_dev "Anyways enough talk lets continue with game!"
    scene w3_6661 with dissolve
    menu:
        "Give her a touch. (w3LucyTouch = True)"(chg=["lucy_up"]):
            $ w3LucyTouch = True
            $ w3LucyAffability += 1
            scene w3_6662 with dissolve
            "The moment I touched Lucy's arm, she flinched a little, but I pushed through."
            mc "We're just a man and a woman chatting at an art exhibition, Lucy."
            "...as it'd be more awkward if I recoiled back as well."
            mc "No one's paying attention to us."
            scene w3_6663 with dissolve
            lucy "Ah, heh... s-sorry... I..."
            lucy "This is my first night out like this. Running into you has thrown me through a loop. Heh..."
            scene w3_6664 with dissolve
            mc "No, no... I get it. What are the odds?"
            scene w3_6663 with dissolve
            lucy "Yeah... what are the odds..."
        "Ask her about your suspicion directly (w3CoincidenceAsk = True)"(chg=["lucy_passion_up"]):

            $ w3CoincidenceAsk = True
            $ w3LucyPressure += 1
            scene w3_6660 with dissolve
            mc "This might sound like a weird question, Lucy, but... running into each other like this is a coincidence, right?"
            scene w3_6659 with dissolve
            lucy "I, ummm... gah, w-what else would it be?"
            scene w3_6658 with dissolve
            "The newbie harlot's fluster didn't soothe my suspicion, but I didn't know what I expected asking a question like that."
            scene w3_6660 with dissolve
            mc "Sorry. I don't know. Thought maybe it was..."
            scene w3_6658 with dissolve
            "I stopped short of saying {i}Felicia related.{/i}"
            scene w3_6657 with dissolve
            mc "Nevermind."
            scene w3_6655 with dissolve
            lucy "......"

    scene w3_6665 with dissolve
    lucy "...to answer your question, I'm here with Mr. Waylon."
    scene w3_6666 with dissolve
    mct "(Eric Waylon...?)"
    "The asshole CEO who has had an eye on Felicia the last couple of weeks..."
    mct "({i}What *ARE* the odds...{/i})"
    scene w3_6667 with dissolve
    mc "I'm surprised you're not glued to his side then. That's the point of bringing a beautiful woman to a public event like this, right?"
    scene w3_6668 with dissolve
    lucy "He..."
    lucy "He's weird about attention."
    "I summarily scanned the courtyard, looking for the Aubade Group's auspicious CEO."
    scene w3_6669 with dissolve
    mc "Yeah...?"
    mct "({b}There{/b} he was.)"
    "Chatting up some man I did *not* recognize."
    scene w3_6670 with dissolve
    lucy "Yeah... weird and... {b}picky{/b}."
    scene w3_6671 with dissolve
    mc "I... {i}think{/i} I know what you mean."
    scene w3_6672 with dissolve
    lucy "...good, because I shouldn't say anything bad about him, should I? Heh..."
    scene w3_6673 with dissolve
    "As nervous as she was, the wry smile on her was still a smile, and it made her even more fetching than she was inside of the club."
    menu w3LucyMenu1:
        "Tell her she looks good tonight."(chg=["lucy_down"]) if w3LucyConvoPoint == 0:
            $ w3LucyConvoPoint +=1
            $ w3LucyAffability -= 1
            scene w3_6674 with dissolve
            "......"
            scene w3_6675 with dissolve
            mc "...nice dress, by the way."
            lucy "Uh, thanks... I..."
            scene w3_6676 with dissolve
            lucy "I'm not really used to wearing stuff like this. Especially not in public."
            scene w3_6678 with dissolve
            mc "Well, you wear it well. Have some confidence."
            scene w3_6676 with dissolve
            lucy "That's the problem. If I do... I think I will have lost it. Heh."
            scene w3_6677 with dissolve
            "Another nervous chuckle."
            scene w3_6676 with dissolve
            lucy "I mean, it's uh... Mr. Waylon insisted I wear this. {i}Then he ditches me{/i}..."
            scene w3_6685 with dissolve
            lucy "Oh, I feel like I could die right now..."


        "Ask how she's doing."(chg=["lucy_up"]) if w3LucyHowUDoin == False:
            $ w3LucyHowUDoin = True
            $ w3LucyConvoPoint +=1
            $ w3LucyAffability += 1
            scene w3_6680 with dissolve
            mc "Are you getting used to things at the club?"
            "I asked what was fresh on my mind, having been asked this very question myself today."
            scene w3_6670 with dissolve
            lucy "No. {b}Thank god.{/b}"
            scene w3_6680 with dissolve
            mc "Yet you signed up for it."
            scene w3_6672 with dissolve
            lucy "Can't put the cat back in the box..."

        "Ask if Harper and she are still going strong."(chg=["lucy_passion_up"]) if w2ExLezSeen == True and w3LucyLezTease == False:
            $ w3LucyLezTease = True
            $ w3LucyConvoPoint +=1
            $ w3LucyPressure += 1
            scene w3_6680 with dissolve
            mc "Harper still teaching you the ropes?"
            scene w3_6670 with dissolve
            lucy "Uh.... {i}yeah?{/}."
            scene w3_6671 with dissolve
            mc "Heh. Weird question, I know."
            scene w3_6670 with dissolve
            lucy "It's an awkward one, considering..."
            mc "Yep. {b}Considering{/b}."
            scene w3_6671 with dissolve
            mc "You two make a cute couple."
            scene w3_6681 with dissolve
            lucy "S-shut up!"
            scene w3_6682 with dissolve
            mct "(Ha! Turns out you {i}can{/i} make a whore blush.)"
            scene w3_6683 with dissolve
            mc "Sorry!"
            scene w3_6681 with dissolve
            lucy "You're not!"
            scene w3_6682 with dissolve
            mct "(...{i}nope.{/i})"
            scene w3_6684 with dissolve
            lucy "...you haven't said anything to anyone about that, right?"

            if w3KathleenLezTold == True:
                mc "I have... {i}not{/i}."
                "That was a lie, but it's not like I would say {b}yes.{/b}"
            else:
                mc "Absolutely not. I have no reason to."

            scene w3_6685 with dissolve
            lucy "G-good..."

        "Ask if Eric is treating her alright tonight."(chg=["lucy_up"]) if w3LucyEricAsk == False:
            $ w3LucyEricAsk = True
            $ w3LucyConvoPoint +=1
            $ w3LucyAffability += 1
            scene w3_6680 with dissolve
            mc "Other than weird and picky, have things been good with Mr. Waylon tonight?"
            scene w3_6686 with dissolve
            "What was I? Putting on my managerial hat?"
            scene w3_6685 with dissolve
            lucy "That..."
            scene w3_6686 with dissolve
            "{i}It felt like something I could ask.{/i} It beat silence."
            scene w3_6685 with dissolve
            lucy "I'm not sure. I haven't really been with him much, which is fine with me, but..."
            lucy "I just hope that doesn't reflect poorly on my performance."
            scene w3_6687 with dissolve
            mc "I doubt he'll be writing a report."
            scene w3_6686 with dissolve
            mct "({i}...probably?{/i})"
            "{b}Probably.{/b}"
            scene w3_6670 with dissolve
            lucy "S-sure..."

    if w3LucyConvoPoint == 1:
        scene w3_6679 with dissolve
        jump w3LucyMenu1
    else:
        pass

    scene w3_6688 with dissolve
    lucy "......"
    mc "...first night out like {i}this{/i} for you, then?"
    lucy "Uh huh... you can probably tell..."
    scene w3_6690 with dissolve
    mc "Not going to lie, it's pretty obvious."
    scene w3_6663 with dissolve
    lucy "Heh, I'm so... {b}frazzled{/b}, afraid that someone might... {i}you know--{/i}"
    scene w3_6689 with dissolve

    menu w3LucyMenu2:
        "You do know, but she doesn't have to worry."(chg=["lucy_up"]):
            $ w3LucyAffability += 1
            scene w3_6690 with dissolve
            mc "No one's going to recognize you, Lucy. Put that fear to rest."
            scene w3_6691 with dissolve
            lucy "What makes you sure about that?"
            scene w3_6690 with dissolve
            mc "How often do you run into people you know at the grocery store?"
            scene w3_6693 with dissolve
            lucy "Not often..."
            scene w3_6694 with dissolve
            mc "You think you're going to run into any at a small artist's exhibition?"
            scene w3_6692 with dissolve
            "...but, {i}I did.{/i}"
            scene w3_6693 with dissolve
            lucy "You're probably right."
            scene w3_6690 with dissolve
            mc "I {b}am{/b} right. Say it."
            scene w3_6663 with dissolve
            lucy "You're right."
            scene w3_6664 with dissolve
            mc "Good girl."
            scene w3_6695 with dissolve
            "And my head keeps growing..."
        "If anyone did see her... {b}Clark Kent.{/b}"(chg=["lucy_down"]):

            $ w3LucyAffability -= 1
            scene w3_6690 with dissolve
            mc "No one's going to recognize you, Lucy."
            scene w3_6691 with dissolve
            lucy "What makes you sure about that?"
            scene w3_6690 with dissolve
            mc "Clark Kent."
            scene w3_6691 with dissolve
            lucy "H-huh? What's that mean?"
            scene w3_6690 with dissolve
            mc "You see, no one expects Superman to have a secret identity."
            scene w3_6691 with dissolve
            lucy "And...?"
            scene w3_6690 with dissolve
            mc "And none of your kid's parents will expect Lucy Long the teacher to be at an art exhibition dressed like a prostitute."
            scene w3_6696 with dissolve
            "She looked at me like I was either stupid or an asshole."
            scene w3_6693 with dissolve
            lucy "...uh. What you said may have seemed encouraging in your head, Mr. [mcl], but there are MULTIPLE points of failure in your reassurance."
            scene w3_6694 with dissolve
            mc "...was it the comic book metaphor?"
            scene w3_6693 with dissolve
            lucy "That was the least of it..."
            scene w3_6692 with dissolve
            mct "(Nice job, [mcf].)"
        "Unfortunately, that's the risk she's taking."(chg=["lucy_passion_up"]):

            $ w3LucyPressure += 1
            scene w3_6690 with dissolve
            mc "That's the risk, ain't it?"
            scene w3_6692 with dissolve
            lucy "......"
            lucy "..."
            scene w3_6694 with dissolve
            mc "I mean, that's how bad you want to get your kid in that school, right?"
            scene w3_6693 with dissolve
            lucy "Y-yeah..."
            scene w3_6692 with dissolve
            "I could've said something sympathetic, but I didn't have any for her self-created predicament."

    scene w3_6688 with dissolve
    "......"
    "...one more break in silence and the writing was on the wall.."
    scene w3_6697 with dissolve
    lucy "Well, uh... I..."

    menu w3LucyMenu3:
        "Excuse yourself, but tell Lucy you're available if she needs you."(chg=["lucy_up", "lucy_passion_down"]):

            $ w3LucyAffability += 1
            $ w3LucyPressure -= 1
            scene w3_6698 with dissolve
            mc "I'll get out of your hair."
            scene w3_6699 with dissolve
            lucy "It's not like that, it's just--"
            scene w3_6700 with dissolve
            mc "I get it, but if you need anything, let me know."
            mc "I'll give you my number."
            scene w3_6701 with dissolve
            lucy "...heh, what could I possibly need?"
            scene w3_6702 with dissolve
            mc "I don't know, but I'm pretty sure if things ever get out of hand, I can smooth things over."
            scene w3_6701 with dissolve
            lucy "...okay."
            scene black with fade
            lucy "Here's my phone--"
        "Simply say goodbye.":

            scene w3_6698 with dissolve
            mc "Goodbye, Lucy."
            scene black with fade
            lucy "...bye."
            "On that point, we were on the same wavelength."

        "Before you go, you just have to ask again..."(chg=["lucy_passion_up2"]) if w3CoincidenceAsk == True:
            $ w3LucyPressure += 2
            $ w3CoincidenceAskTwice = True
            scene w3_6703 with dissolve
            mc "Just to be sure, Waylon isn't creeping on Felicia tonight, right?"
            scene w3_6705 with dissolve
            lucy "I, um-- I'm not... errr... I don't know anything about that."
            lucy "I'm just... I'm just here doing what I've been asked to do - at Mr. Waylon's behest."
            scene w3_6707 with dissolve
            mc "Got it. Sorry for asking twice."
            scene w3_6706 with dissolve
            "It is probably just a coincidence..."
            scene w3_6707 with dissolve
            mc "I'll see you around, Lucy. Good luck with Waylon."

        "Last shot to ask that question at the back of your mind."(chg=["lucy_passion_up"]) if w3CoincidenceAsk == False:
            $ w3LucyPressure += 1
            $ w3CoincidenceAskTwice = True
            scene w3_6703 with dissolve
            mc "Before I go back to my date, I do have a question."
            scene w3_6704 with dissolve
            lucy "W-what is it?"
            scene w3_6703 with dissolve
            mc "Us running into each other is a coincidence, right?"
            scene w3_6706 with dissolve
            "........."
            "......"
            scene w3_6705 with dissolve
            lucy "...what else would it be?"
            scene w3_6707 with dissolve
            mc "I don't know. You're not keeping an eye on Felicia for Mrs. Pulman are you?"
            scene w3_6705 with dissolve
            lucy "N-no... uh... I'm just here at Mr. Waylon's behest."
            scene w3_6707 with dissolve
            mc "Got it. Just thought I'd ask."
            scene w3_6706 with dissolve
            "It is probably just a coincidence..."
            scene w3_6707 with dissolve
            mc "I'll see you around, Lucy. Good luck with Waylon."
            scene black with fade
            lucy "Thanks..."


    "......"
    "..."
    scene w3_6708 with fade
    mct "(Well, that was interesting...)"
    "I watched Lucy shuffle off while considering my options."
    scene w3_6709 with dissolve
    "I should probably go back to Felicia. She'll start to wonder where I wandered off to."
    "--and it's not like I wanted to say hello to Eric Waylon, but part of me couldn't shake the weirdness of running into someone like him at a small thing like this."

    menu:
        "{mod_green}MOD OPTIONS{/mod_green}: Do both (can lead to Blackmail and Lucy confront scenes)"(chg=["maid"]):
            m_dev "Hey me again! If you actually want to see both scenes pick the options with my face."
            $ mod_week3_bl_lucy = True
            $ w3EricTalked = True
            $ w3LucyConfront = True
            jump mod_ch4up4_bl_lucy
        "Go back to Felicia. (can lead to w3LizaBlackMail = True)":

            jump w3LizaBlackmail
        "As always, the nagging feeling wins. (can lead to w3LucyConfront = True)":

            $ w3EricTalked = True
            jump w3EricTalk


label w3EricTalk:

    scene w3_6710 with dissolve
    "Curiosity prevails."
    "My body immediately plodded toward our club's {i}esteemed{/i} patron."
    scene w3_6711 with dissolve
    mct "(And after all, it'd be rude not to acknowledge him, wouldn't it?)"
    mct "(Something, something {i}my job...{/i})"
    scene w3_6712 with wipeleft
    "The moment Eric Waylon saw me approach, a funny expression crossed his face."
    scene w3_6713 with dissolve
    "One of vague and cloudy recognition, attempting to recollect where he knew me from and if he should even give a shit."
    menu:
        "Save him the trouble. Greet him.":
            scene w3_6714 with dissolve
            show screen textbox2
            mc "Good afternoon, Mr. Waylon. Last time I saw you was with Mr. Garcia, wasn't it?"
            scene w3_6715 with dissolve
            "His eyes immediately gained focus as recognition took hold."
            scene w3_6716 with dissolve
            eric "Right, {b}right{/b}. You're the gopher. Sorry, what was your--"
            mc "[mcf] [mcl], sir."
            scene w3_6717 with dissolve
            "{i}Asshole.{/i}"
            scene w3_6718 with dissolve
            eric "[mcf]. Right."
        "This will be interesting. Wait for him to say something.":

            scene w3_6715 with dissolve
            show screen textbox2
            "The gears turned, and just when I thought he was about to ask-"
            scene w3_6716 with dissolve
            eric "You're the club gopher."
            mc "Yes, sir. [mcf]."
            scene w3_6718 with dissolve
            eric "Why are you just standing there gawking, [mcf]?"
            scene w3_6719 with dissolve
            mc "My apologies."
            scene w3_6717 with dissolve
            "{i}Asshole.{/i}"

    scene w3_6719 with dissolve
    mc "How are you doing, sir?"
    scene w3_6718 with dissolve
    eric "You can spare the chit-chat. It's not like we're friends."
    scene w3_6720 with dissolve
    "........."
    scene w3_6721 with dissolve
    "......"
    scene w3_6722 with dissolve
    mc "...I'm very surprised to run into you like this."
    scene w3_6721 with dissolve
    "Alright. {i}Pretenses dropped{/i}."
    scene w3_6722 with dissolve
    mc "So, you're into paintings?"
    scene w3_6723 with dissolve
    eric "That's not a {i}you're{/i} into paintings, I hope."
    scene w3_6724 with dissolve
    mc "No. Just a straight-up question."
    scene w3_6723 with dissolve
    eric "Good, because can't I be?"
    scene w3_6726 with dissolve
    eric "Mihir sounded incredulous when I told him I was looking to learn about art."
    scene w3_6725 with dissolve
    mc "Oh..."
    "The relatively polite and pleasant dean of Allerton University."
    scene w3_6727 with dissolve
    mc "Is that how you heard about tonight?"
    "As a baseless presumption, something like this did fit his disposition."
    scene w3_6723 with dissolve
    eric "It sounds like you're interrogating me, [mcf]."
    scene w3_6724 with dissolve
    mc "Sorry. I'm just..."
    scene w3_6727 with dissolve
    mc "...making conversation?"
    mct "(Besides, wouldn't he have a person who did things like that for him?)"
    scene w3_6728 with dissolve
    eric "{i}Sorry.{/i}"
    eric "Let me ask you something, [mcf]."
    scene w3_6729 with dissolve
    mc "Anything, sir."
    scene w3_6730 with dissolve
    eric "Why do I find you so immediately irritating tonight?"
    scene w3_6731 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Is it because he finds everyone irritating?":
            scene w3_6732 with dissolve
            show screen textbox2 with dissolve
            mc "I'd wager you find most people irritating, Mr. Waylon."
            scene w3_6733 with dissolve
            eric "It's because you come up to me and act like we know each other."
            scene w3_6732 with dissolve
            mc "In a sense, you and I have a closer connection than anyone else here."
            scene w3_6734 with dissolve
            eric "...perhaps you're right about that."
            scene w3_6735 with dissolve
            mc "You don't want to be seen talking to some kid?"
        "Tell him it's probably because you have a stupid face.":


            scene w3_6732 with dissolve
            show screen textbox2 with dissolve
            mc "Is it cause I have a stupid face?"
            scene w3_6736 with dissolve
            eric "...pffh, ha! No, that's not it."
            "A little deadpan delivery and Eric Waylon looked... bemused?"
            scene w3_6735 with dissolve

    mc "I'll get out of your hair if you want."
    scene w3_6737 with dissolve
    play sound "sound effects/slap2.wav"
    scene w3_6738 with hpunch
    eric "Oh, fuck you. Relax. I'm just busting your balls."
    "The investment banker swatted me like we were two man-children in a frat."
    scene w3_6739 with dissolve
    mc "I--"
    "I caught myself from apologizing once more."
    mc "Yeah, fuck you too."
    scene w3_6740 with dissolve
    eric "I could ask you the same thing by the way. What the hell are you doing here?"
    eric "{i}You don't strike me as the type.{/i}"
    scene w3_6741 with dissolve
    "He passed along his peer's alleged incredulousness to me."
    scene w3_6740 with dissolve
    eric "Are you here on {i}business?{/i}"
    scene w3_6741 with dissolve
    "...did he not know Felicia was here? Was this really just a chance encounter?"
    mct "(Fuck, maybe the old man's home invasion just has me paranoid...)"
    scene w3_6742 with dissolve
    mc "I'm actually on a date."
    "No point in lying. I kept it vague, but he was likely to run into Felicia pretty soon anyway - with me at her side."
    scene w3_6743 with dissolve
    eric "Ah."
    scene w3_6744 with dissolve
    "He'll draw his own conclusions, then."
    scene w3_6743 with dissolve
    eric "That makes sense."
    scene w3_6746 with dissolve
    eric "Tale as old as time. Men getting dragged to stupid shit to get laid."
    eric "Ha! I guess that's partly true of myself tonight as well."
    scene w3_6748 with dissolve
    mc "...that so?"
    scene w3_6747 with dissolve
    "Considering his company was a prostitute, that struck me as a particularly odd thing to say."
    scene w3_6748 with dissolve
    mc "I saw one of the girls earlier."
    scene w3_6749 with dissolve
    eric "I said partly! I'm here tonight because I got laid."
    scene w3_6743 with dissolve
    eric "Answering your earlier question, I let slip to that full-figured whore of Isaak's a few days ago that I was becoming interested in art. Then she sprung this on me yesterday."
    scene w3_6745 with dissolve
    mc "...it was Lucy's idea?"
    scene w3_6750 with dissolve
    eric "The paintings suck, nothing I'm interested in, but I do get to watch that bitch squirm with her tits out."
    "{i}It was Lucy's idea?!{/i}"

    if w3CoincidenceAskTwice == True:
        mct "(...and she lied to me about this being his idea.)"

    scene w3_6751 with dissolve
    mct "(That's interesting...)"
    scene w3_6752 with dissolve
    mc "A teacher should be cultured, huh?"
    scene w3_6753 with dissolve
    eric "*Scoff* Cultured. {i}Fuckin' slut.{/i}"
    scene w3_6754 with dissolve
    "......"
    "..."
    scene w3_6755 with dissolve
    mc "Are you going to be here long, Mr. Waylon?"
    scene w3_6734 with dissolve
    eric "I'll be leaving soon."
    scene w3_6757 with dissolve
    "That was, in a small way, a relief. That means I could potentially avoid an awkward run-in between him and Felicia if I wanted."
    scene w3_6756 with dissolve
    eric "I would leave now, but I want to watch Lucy wilt a little while longer."
    scene w3_6757 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "You want to get to the bottom of this. Excuse yourself, go find Lucy Long. (w3LucyConfront = True)":
            $ w3LucyConfront = True
            scene w3_6735 with dissolve
            show screen textbox2 with dissolve
            mc "I should go find my friend."
            scene w3_6756 with dissolve
            eric "Oh, you're done grilling me?"
            scene w3_6735 with dissolve
            mc "Aye, I'm done grilling you, sir. But do you mind if I talk to Lucy real quick?"
            scene w3_6756 with dissolve
            eric "Knock yourself out."
            scene w3_6758 with dissolve
            mc "Thank you. I hope you have a good evening, Mr. Waylon."
            scene black with fade
            "......"
            "..."
            jump w3LucyConfront
        "...just go back to Felicia. Who cares. This shit is tiring. (w3FeliciaIdle = True)":

            $ w3FeliciaIdle = True
            scene w3_6735 with dissolve
            show screen textbox2 with dissolve
            mc "I should go find my friend."
            scene w3_6756 with dissolve
            eric "Oh, you're done grilling me?"
            scene w3_6735 with dissolve
            mc "Aye, I'm done grilling you."
            scene w3_6758 with dissolve
            mc "I hope you have a good evening, Mr. Waylon."
            scene w3_6759 with dissolve
            ray "Yeah, she's like that. Sorry."
            scene w3_6760 with dissolve
            denise "It's alright, Ray. I know it's a part of this thing, right?"
            scene w3_6759 with dissolve
            ray "I know you know, girl."
            scene w3_6760 with dissolve
            denise "Still..."
            scene w3_6761 with dissolve
            ray "Just don't let it eat away at you."
            scene black with fade
            "......"
            "..."
            jump w3FeliciaConnectingInterlude

label w3LizaBlackmail:
    scene w3_6762 with dissolve
    "Felicia was waiting, and I have had enough of listening to my gut for one week."
    "It wasn't hard to resist, either."
    scene w3_6763 with dissolve
    mct "(Felicia's company is more preferable to that silver-haired dickhead, anyway.)"
    scene w3_6764 with dissolve
    "...but even still, out of every guest here, I couldn't help but think that Lucy was trying to shirk from my gaze in particular."
    "......"
    "..."
    scene w3_6765 with dissolve
    liza "It's quite quaint how fixated your work seems to be. Where other artists would've moved on, your preoccupation with the same {i}basic{/i} themes speaks to a singular-mindedness that I'm sure we can all wish to return to."
    "As I pondered the state of Lucy, the conversation playing out in front of the teacher immediately drew my attention."
    scene w3_6766 with dissolve
    denise "..."
    ray "..."
    "The blonde critic's voice alone carried across the courtyard, as if trying to be heard."
    scene w3_6767 with dissolve
    liza "Still, I do wonder who it's for..."
    denise "..."
    liza "Yes, but that's so matter of fact. Almost child-like. Undifficult."
    scene w3_6766 with dissolve
    denise "..."
    ray "..."
    scene w3_6765 with dissolve
    liza "Surely you're trying to say more?"
    denise "..."
    scene w3_6767 with dissolve
    liza "Well, it {i}is{/i} an interesting choice to only exhibit 5 rudimentary works. On one hand, using the form of the event to inform the subject is OVERDONE, but..."
    denise "..."
    scene w3_6768 with dissolve
    liza "Let me finish! Don't cut me off!"
    ray "..."
    scene w3_6769 with dissolve
    "Only catching one side of things, I could still tell it was a whole lot of bullshit."
    "Liza would talk loudly."
    "Raymond would try to run interference for Denise's sake."
    scene w3_6770 with dissolve
    "Denise would oscillate between making a point and then conceding it, looking smaller each time."
    "Then Liza would talk even more loudly over the two."
    scene w3_6771 with dissolve
    "I knew the type. She was a bully, only she dressed up those tendencies under the guise of civilized discourse."
    scene w3_6772 with dissolve
    "Which {b}irked{/b} more than if she had simply pushed somebody to the ground and tousled their hair."
    mct "(Well, whatever--)"
    scene w3_6773 with dissolve
    mct "(What is she...?)"
    scene w3_6774 with dissolve
    "Oh. {i}Drugs{/i}."
    "Following one high with another, are you?"
    hide screen textbox2 with dissolve

    menu:
        "That figures.":
            scene w3_6775 with dissolve
            show screen textbox2 with dissolve
            "I watched the critic powder her nose, all quick-like, with only a nominal effort in concealing it."
            scene w3_6776 with dissolve
            "......"
            "..."
            scene w3_6777 with dissolve
            mct "({b}Nasty cunt.{/b})"
            scene w3_6778 with dissolve
            "An ugliness colored my mind, my mood had been soured, and I wasn't feeling particularly kind right now."
        "Your hand moves without thought. (w3LizaBlackMail = True)":

            $ w3LizaBlackMail = True
            scene w3_6775 with dissolve
            show screen textbox2 with dissolve
            "I had no plan to use this, but..."
            play sound "sound effects/camera-phone-shutter.wav"
            scene w3_6781 with flash
            "My phone found its way into my hand, and a series of snapshots of the critic powdering her nose found its way into my possession."
            "Perhaps I should be concerned about how easily that impulse overwrote my brain, but I wasn't feeling kind right now."
            scene w3_6776 with dissolve
            "......"
            "...maybe Felicia could use this to get her girl a glowing review?"
            scene w3_6777 with dissolve
            "......"
            "...nah. She'd probably despise that?"
            scene w3_6778 with dissolve
            mct "(I'll just delete this later...)"

    scene w3_6779 with dissolve
    mct "(Well, {b}whatever{/b}.)"
    scene w3_6780 with dissolve
    "{b}Now{/b} I should return to Felicia--"
    hide screen textbox2 with dissolve

    menu:
        "But before that...":
            scene w3_6782 with dissolve
            show screen textbox2 with dissolve
            mc "The work on display tonight is beautiful."
            scene w3_6783 with dissolve
            denise "Oh, uh... thank you."
            scene w3_6784 with dissolve
            ray "See? Don't pay attention to that bitch."
            denise "..."
            scene black with fade
            "I was fine with those being the only words I said to her."
            denise "Heh. At least she's paying attention to me, right?"
            stop music fadeout 3.0
            scene black with fade
            ray "Right on, girl."
            "......"
            "..."
        "The blonde bombshell is waiting.":
            show screen textbox2 with dissolve
            ray "Don't let that bitch get to you, Denny."
            denise "It comes with the territory, right? Still..."
            ray "Yeah, I know, girl. {b}I know{/b}."
            stop music fadeout 3.0
            scene black with fade
            ray "Try not to let it eat away at you."
            "......"
            "..."

    jump w3FeliciaConnectingInterlude


label w3FeliciaConnectingInterlude:

    play music "music/georges-lament.ogg"
    scene w3_6785 with wipeleft
    if w3FeliciaIdle == True:
        fel "There you are. I was starting to think you got lost."
    else:
        fel "There you are, just when I was starting to get bored."

    mc "Sorry to keep you waiting."
    scene w3_6786 with dissolve
    fel "How did it look out there?"
    mc "It's clearing out some."
    scene w3_6787 with dissolve
    fel "{b}Good.{/b} Enough for me to comfortably gawk without feeling rushed?"
    mc "Hmmm... I'd say so?"
    scene w3_6788 with dissolve
    fel "Shall we go see, then?"
    scene w3_6789 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Warn her about Waylon. (w3FeliciaEricWarn = True)"(chg=["felicia_up2"]):
            $ w3FeliciaEricWarn = True
            $ Felicia_Affection +=2
            scene w3_6790 with dissolve
            show screen textbox2 with dissolve
            if w3FeliciaIdle == True:
                mc "Before we do that, I should probably tell you, I didn't get lost. I got pulled into some mingling of my own."
            else:
                mc "Before we do that, I should probably tell you... I got pulled into some mingling of my own."

            scene w3_6788 with dissolve
            fel "You did? {b}Interesting...{/b}"
            scene w3_6790 with dissolve
            mc "One of the club's patrons is here."
            scene w3_6788 with dissolve
            fel "Small world."
            scene w3_6790 with dissolve
            mc "That's exactly what I said."
            scene w3_6788 with dissolve
            fel "Who is it?"
            scene w3_6790 with dissolve
            mc "Eric Waylon."
            scene w3_6791 with dissolve
            fel "{i}Him?{/i}"
            scene w3_6792 with dissolve
            "Felicia, of course, recognized the name as one of the \"backers\" in her corner."
            fel "......"
            scene w3_6793 with dissolve
            fel "...it's not like I haven't seen some of those men out in the wild before, but at a socially inconsequential event like this? He must really like me..."
            scene w3_6792 with dissolve

            if w3EricTalked == True:
                mct "(That thought also crossed my mind, but...)"
                "The fact it was Lucy's idea cast aspersions on the creep factor."
            else:
                mc "That thought also crossed my mind."
                "The looming question, however, was how did he find out about tonight?"

            scene w3_6794 with dissolve
            mc "Did you tell anyone where you were going tonight?"
            scene w3_6791 with dissolve
            fel "{b}No{/b}. Not a soul..."
            scene w3_6790 with dissolve


            if w3FeliciaIdle == True:
                mc "Well, he said he'll be leaving soon. Wanna keep hiding out for another ten minutes or so? Avoid an awkward encounter?"
            else:
                mc "Maybe we can wait him out? Avoid an awkward encounter for you?"

            scene w3_6795 with dissolve
            fel "Aww, stud. Looking out for me?"
            scene w3_6796 with dissolve
            mc "Well, he is an unpleasant man."

            if w3FeliciaIdle == True:
                "As I was reminded..."

            scene w3_6797 with dissolve
            fel "Ha! Don't forget who I'm married to."
            scene w3_6798 with dissolve
            mc "You make a very strong point."
            scene w3_6799 with dissolve
            fel "I know how to redirect unpleasant men, {b}and{/b}..."
            fel "It's not really awkward if I know it's coming?"
            scene w3_6800 with dissolve
            "She sounded slightly unsure of that last part."

            hide screen textbox2 with dissolve
            if w3FeliciaPlatonic == False:
                scene w3_6801 with dissolve
                fel "Thanks for the warning."
                scene w3_6802 with dissolve
                "Boy, did she love those kinds of looks."
                scene w3_6803 with dissolve
                mc "...shall we go back outside, then?"
                scene w3_6802 with dissolve
                "A combustible look - well-honed, precise, and deadly - effective in igniting one's worldly imagination."
                scene w3_6801 with dissolve
                fel "{b}Let's{/b}. And once we see tonight's work, we can..."
                scene w3_6804 with dissolve
                "A pause, and a well-timed hand on my chest, as if opening a door to spark a backdraft."
                scene w3_6805 with dissolve
                fel "...we can get out of here and do something more {b}fun.{/b} Something {i}both{/i} our speeds."
                scene w3_6806 with dissolve
                "......"
                "..."

                menu:
                    "(Fake out) She has something on her face.":
                        scene w3_6807 with dissolve
                        mc "Wait. You've got something on your face."
                        fel "...?"
                        scene w3_6808 with dissolve
                        fel "What, like dirt?"
                        mc "Nope, not dirt. It's..."
                        scene w3_6809 with dissolve
                        "{i}Boop.{/i}."
                        mc "Your nose."
                        scene w3_6810 with dissolve
                        "......"
                        scene w3_6811 with dissolve
                        fel "...{b}stupid.{/b}"
                    "Kiss her. That's the look, right? (kissAttempt2 = True)":

                        $ kissAttempt2 = True
                        scene w3_6812 with dissolve
                        "An amorous look, inviting a--"
                        scene w3_6813 with dissolve

                        if kissAttempt == True:
                            "Again I was denied. Evidently, not the time or place."
                            scene w3_6814 with dissolve
                            fel "What did I tell you about doing that willy nilly?"
                            scene w3_6815 with dissolve
                            mc "...you're fucking with me, aren't you?"
                        else:
                            "I was denied."
                            scene w3_6814 with dissolve
                            fel "Don't just kiss me when you feel like it."
                            scene w3_6815 with dissolve
                            mc "I guess I misread your look..."
                            scene w3_6814 with dissolve
                            fel "No, you didn't."
                    "Tell her to lead the way.":

                        scene w3_6816 with dissolve
                        mc "Sounds like a plan."
                        scene w3_6805 with dissolve
                        fel "Good..."
            else:

                scene w3_6817 with dissolve
                fel "{i}Let's.{/i} Once we see tonight's work, we can get out of here. Get some grub."
                scene w3_6818 with dissolve
                mc "Sounds like a plan.."
        "Leave it as a surprise.":

            "Explaining the situation didn't seem worth the effort. She'll get the picture, just as I did, when she sees Eric Waylon's scowling face."
            scene w3_6790 with dissolve
            mc "Shall we go back out there?"
            scene w3_6789 with dissolve
            "Ultimately, I knew she could handle that asshole, but...I was curious about what kind of expression she'd make when she's surprised."

            if w3FeliciaPlatonic == False:
                scene w3_6819 with dissolve
                fel "{i}Let's.{/i} Once we see tonight's work, we can get out of here and do something more... {b}fun.{/b}"
                scene w3_6820 with dissolve
                mc "Sounds like a plan."
            else:
                scene w3_6788 with dissolve
                fel "{i}Let's.{/i} Once we see tonight's work, we can grab some grub."
                scene w3_6790 with dissolve
                mc "That sounds like a plan."
    stop music fadeout 3.0
    show screen textbox2 with dissolve
    scene black with fade
    fel "Let's go."
    "......"
    "..."
    jump w3FeliciaPaintingViewing

label w3LucyConfront:
    scene w3_6821 with fade
    "The way I saw it, I had two approaches."
    "One, I could be direct."

    if w3CoincidenceAskTwice == True:
        "Tell her I knew Mr. Waylon was here at {i}her{/i} behest and ask her why she lied about it."
        "The thing is, it's not likely she did it out of maliciousness or to fuck with me. I'm sure, in some way, this was about the exhibition and Lucy was simply on marching order."
    elif w3CoincidenceAsk == True:
        "Tell her I knew it was her idea to come here tonight and ask her why she implied otherwise."
        "The thing is, it's not likely she did it out of maliciousness or to fuck with me. I'm sure, in some way, this was about the exhibition and Lucy was simply on marching order."
    else:
        "Ask her straight up - {i}why{/i} would she bring a client to a place like this?"
        "A good bet was that she was operating under marching orders from above, and that this in some way had to do with the exhibition."

    "The other way, I could attempt to finesse it out of Lucy."
    "Avoid pressuring her, tip-toe around the issue, and try to ferret out enough information to arrive at a sensible conclusion."
    scene w3_6822 with dissolve
    "As I considered what I'd say, once more, I caught Lucy's attention."
    "A weak smile created even more distance, but I could tell she knew I wanted to talk."
    scene w3_6821 with dissolve
    mct "(Unlike her...)"
    "No matter how I decided to play it--"
    scene w3_6823 with dissolve
    ray "[mcf]!"
    "Ah, crap."
    scene w3_6824 with dissolve
    mc "You remembered my name!"
    ray "Part of my skill set! Impressive, I know!"
    scene w3_6825 with dissolve
    mct "(Ah, double crap!)"
    "{i}Lucy seized the opportunity to escape.{/i}"
    ray "And where has our ray of sunshine wandered off to?"
    mc "Uh... Felicia? she's--"
    scene w3_6826 with dissolve
    "My attention wandered to the small girl next to him, the one Felicia was intent on not meeting."
    "A shy, small thing that fearless Felicia was exceedingly self-conscious of."
    mc "...she's {i}around.{/i}"
    scene w3_6827 with dissolve
    ray "You haven't had the chance to meet tonight's artist, have you?"
    denise "H-hello."
    scene w3_6828 with dissolve
    mc "...Hello, Denise. I bet it's pretty cool to have all these people here to look at something you made."
    denise "Eh... some of that is Ray's doing."
    ray "Don't be modest!"
    scene w3_6829 with dissolve
    ray "Anyway, great! Now you've said hello to [mcf], so..."
    ray "You got a lot more of those to do. Let's go see how Mr. Kieślowski is doing."
    scene w3_6830 with dissolve
    denise "B-bye [mcf]!"
    ray "Just don't stand too close to him. He's a bit grabby, men AND women."
    denise "Um, h-huh, wha--"
    mc "Nice meeting you..."
    scene w3_6831 with dissolve
    "Like that, she was whisked away, to perform her duties."
    "......"
    scene w3_6832 with dissolve
    "..."
    scene w3_6833 with dissolve
    fel "There you are. I was getting worried you might've drowned yourself in the urinal or something."
    scene w3_6834 with dissolve
    mc "...you don't have a high opinion of me, do you?"
    scene w3_6835 with dissolve
    fel "Nonsense. Anyone who can get me to cum is {b}at least{/b} decent stock."
    scene w3_6836 with dissolve
    mc "You--"
    scene w3_6837 with dissolve
    mc "{b}Hah.{/b} You missed your girl, by the way."
    scene w3_6838 with dissolve
    fel "I know. I walked slow."
    fel "Cute, isn't she?"
    scene w3_6839 with dissolve
    mc "Looks like it cleared up over there."
    fel "So it has."
    scene w3_6840 with dissolve
    mc "Shall we?"

    if w3FeliciaPlatonic == False:
        scene w3_6841 with dissolve
        fel "{b}Let's.{/b} Once we see tonight's work, we can get out of here and do something more... {b}fun.{/b}"
    else:
        scene w3_6842 with dissolve
        fel "{b}Let's.{/b} Once we see tonight's work, we can grab some grub."

    stop music fadeout 3.0
    scene black with fade
    "......"
    "..."
    jump w3FeliciaPaintingViewing

label w3FeliciaPaintingViewing:
    play music "music/a-nice-dream.ogg"
    scene w3_6843 with curtains
    mc "...so, what is it about this girl that you find so \"personally\" fascinating?"
    scene w3_6844 with dissolve
    fel "We're back to that?"
    scene w3_6843 with dissolve
    mc "{i}The road not taken.{/i} You didn't expand on that."
    scene w3_6844 with dissolve
    fel "It's... {i}stupid.{/i}"
    scene w3_6843 with dissolve
    mc "To me, good art is whatever looks cool or realistic. I'm a total pleb like that, but it would be fascinating to know what makes this..."
    scene w3_6845 with dissolve
    mc "...click for {i}Felicia.{/i}"
    scene w3_6846 with dissolve
    fel "Despite it being an obvious and {b}fair{/b} question, why do I feel put on the spot?"
    scene w3_6847 with dissolve
    mc "Is it about content? Technique? Something you'd pick up on that I wouldn't?"
    scene w3_6846 with dissolve
    fel "It's nothing that {i}sterile{/i}. It's just... I relate to it on an {i}experiential{/i} level?"
    scene w3_6847 with dissolve
    mc "You see yourself in the work?"
    scene w3_6846 with dissolve
    fel "Some of it, and mostly...."
    scene w3_6848 with dissolve
    "Felicia took some seconds to mold feelings into words."
    scene w3_6849 with dissolve
    fel "I see myself in the artist."
    scene w3_6850 with dissolve
    "Felicia peered intently at the painting in front of us, taking in the melancholic orange hue while I waited to see if she wanted to expand on her admission."
    "......"
    "..."
    scene w3_6851 with dissolve
    fel "It was like.. five or six years ago? That's when she won the same competition I did in my teens."
    scene w3_6852 with dissolve
    fel "That in itself isn't anything special; they do it every year."
    scene w3_6853 with dissolve
    mc "What made her special, then?"
    scene w3_6854 with dissolve
    fel "Her essay. It lacked the... \"safe\" elements that are typically submitted."
    fel "It pretty much voiced every reason I decided to keep art as something I privately enjoyed."
    scene w3_6853 with dissolve
    mc "She must be some writer for it to have you stalking her."
    scene w3_6855 with dissolve
    fel "I'm not--!"
    mc "Kidding! What sort of reasons?"
    scene w3_6856 with dissolve
    fel "Eh. The usual stuff..."
    fel "Losing sight of why you enjoy something, what future was there in it, what's to gain from exposing yourself, how it might make you half-hearted..."
    scene w3_6857 with dissolve
    fel "Those kinds of things."
    scene w3_6858 with dissolve
    mc "Doubt?"
    scene w3_6857 with dissolve
    fel "If you want to wrap it all up in one word like that, {b}yeah{/b}. Doubt."
    scene w3_6860 with dissolve
    "......"
    scene w3_6858 with dissolve
    mc "...so, you got a girl crush on a kindred spirit."
    scene w3_6859 with dissolve
    "........."
    "......"
    scene w3_6857 with dissolve
    fel "...I got a girl crush on a kindred spirit, yeah."
    fel "That wasn't when she won me over as a fan, though. I actually went on with my busy life, thinking I forgot about her, until..."
    scene w3_6860 with dissolve
    "........."
    "......"
    scene w3_6861 with dissolve
    fel "...makes me want to scream, too."
    scene w3_6862 with dissolve
    fel "It was a few years later that I saw a painting with her name on it, in the outer reaches of an open community showing."
    mc "What was it of?"
    scene w3_6863 with dissolve
    fel "A clown of all things, dwarfed by a deep chasm in the foreground."
    scene w3_6864 with dissolve
    mc "That's... weird."
    scene w3_6863 with dissolve
    fel "The thing is, she stuck with it."
    fel "She stuck with it, all alone, and unlike me. In spite of the kind of things I felt, along with much-much-more than I could comprehend...."
    scene w3_6866 with dissolve
    fel "She gave it a {b}go.{/b}"
    scene w3_6865 with dissolve
    mct "(The road not taken...)"
    scene w3_6863 with dissolve
    fel "Eventually, I realized I deeply admired her."
    scene w3_6864 with dissolve
    mc "Do you wish you stuck with it?"
    scene w3_6863 with dissolve
    fel "Honestly? Not really - and her work has helped me understand that about myself. I'm grateful for that."
    scene w3_6867 with dissolve
    fel "At first, I was simply curious. Where did she find the motivation? Would she keep with it?"
    scene w3_6868 with dissolve
    fel "And over time, as her works developed, I learned just how similar we are AND just how we diverge."
    mc "Connection..."
    scene w3_6869 with dissolve
    fel "{b}Connection{/b}"
    fel "For me art is a way to express myself inwardly. A comfort I privately draw on to touch a time and a place long gone, whenever I feel like I'm forgetting something."
    scene w3_6870 with dissolve
    fel "For her..."
    scene w3_6871 with dissolve
    fel "...it's outward expression."
    scene w3_6872 with dissolve
    mc "Same medium, but completely opposite purpose."
    scene w3_6871 with dissolve
    fel "Not completely. Hobby or not, with only yourself or the world at large, it's about feeling heard..."
    scene w3_6873 with dissolve
    fel "I really don't regret giving up my chance at an art career, I just hope..."
    fel "I hope Denise gets everything she wants out of it."
    scene w3_6874 with dissolve
    mc "What about you? Was tonight everything you were hoping for?"
    scene w3_6875 with dissolve
    fel "{b}Yeah{/b}. I'm so fucking proud of her, [mcf]."
    scene w3_6876 with dissolve
    "Felicia swelled, like a doting mother, with a conviction whose touch extended beyond the syllables of her words."
    scene w3_6877 with dissolve
    "......"
    "..."
    scene w3_6878 with dissolve
    "For a couple minutes, Felicia appraised the work, getting a handle on her thoughts while I likewise did the same."
    "I finally got my head around what tonight exactly meant to her, and why she offered to pay me just so she didn't partake in it alone."
    scene w3_6879 with dissolve
    "......"
    "..."
    play music "music/sonatina-in-c-minor.ogg"
    scene w3_6880 with dissolve
    eric "Look who it is!"

    if w3FeliciaEricWarn == True:
        scene w3_6881 with dissolve
        "It was as if our esteemed patron picked the {b}perfect{/b} time to put his stink on the moment."
        scene w3_6882 with dissolve
        eric "Mrs. Ford! I'm surprised to run into you like this."

        if w3EricTalked == True:
            scene w3_6883 with dissolve
            eric "So that's who the gopher's date was. Enjoying the perks, kid?"

        scene w3_6884 with dissolve
        "......"
        "..."
        scene w3_6885 with dissolve
        fel "Mr. Waylon."
        scene w3_6884 with dissolve
        "She spoke before turning around, as if uncannily suggesting she had eyes in the back of her head."
        scene w3_6886 with dissolve
        fel "{i}Indeed.{/i} What a surprise."
        scene w3_6890 with dissolve
        "Then the two simply acknowledged each other, Mr. Waylon leering and looking down on Felicia, while Felicia looked utterly unperturbed - almost as if she was looking straight through him, like he didn't have any substance at all."
        "Just like she had suggested, in light of my warning, she had steeled herself for this eventuality."
        scene w3_6891 with dissolve
        eric "You look beautiful tonight. Contrasts wonderfully with your weekend attire."
        scene w3_6892 with dissolve
        fel "It seems we have a common interest."
        scene w3_6891 with dissolve
        eric "My life coach tells me I should get more culture in my life."
    else:

        $ Felicia_Confidence -= 1
        scene w3_6887 with dissolve
        "It was as if our esteemed patron picked the {b}perfect{/b} time to put his stink on the moment."
        scene w3_6888 with dissolve
        eric "Mrs. Ford! I'm surprised to run into you like this."
        scene w3_6887 with dissolve
        "Felicia's expression immediately conveyed her shock."
        scene w3_6889 with dissolve
        "She had likely placed it as a club-affiliated voice, but had yet to pinpoint its specific owner."
        "......"
        "..."
        scene w3_6886 with dissolve
        fel "...M-Mr. Waylon."
        scene w3_6893 with dissolve
        "She briefly fumbled over her words, not expecting to be ambushed tonight and here of all places, during her moment of personal contemplation."
        scene w3_6894 with dissolve
        eric "You look beautiful tonight. Contrasts wonderfully with your weekend attire."
        scene w3_6896 with dissolve
        fel "Uh..."
        scene w3_6895 with dissolve
        "She was also likely running through the same possibilities I had."
        scene w3_6896 with dissolve
        fel "...what are you doing here?"
        scene w3_6895 with dissolve
        "The same suspicions of being fucked with, and asking herself what were the odds."
        scene w3_6894 with dissolve
        eric "My life coach tells me I should get more culture in my life."
        scene w3_6890 with dissolve
        "...but true to character, Felicia quickly found her social footing, and composed herself with a befitting demeanor."

    scene w3_6892 with dissolve
    fel "And how's that working out for you?"
    scene w3_6891 with dissolve
    eric "I'm still waiting on a revelation."
    scene w3_6892 with dissolve
    fel "Have you tried yoga?"
    scene w3_6897 with dissolve
    eric "You know, I kinda feel bad for your husband..."
    scene w3_6898 with dissolve
    "Eric moved forward and equipped himself with a more hushed tone."
    scene w3_6897 with dissolve
    eric "The club is one thing, but now you're gallivanting at large with a brat?"
    scene w3_6899 with dissolve
    fel "Well, Mr. Waylon, you're married too. You know the score."
    scene w3_6897 with dissolve
    eric "It's not the same game, Mrs. Ford."
    scene w3_6898 with dissolve
    "......"
    "..."
    scene w3_6897 with dissolve
    eric "Would you and [mcf] like to go back to my penthouse?"
    eric "The four of us could have some fun together."
    scene w3_6900 with dissolve
    fel "That will spoil this Saturday for you, Waylon."
    scene w3_6897 with dissolve
    eric "See you this Saturday."
    scene w3_6898 with dissolve
    mct "(...was that it?)"
    scene w3_6901 with dissolve
    fel "Have a good night."

    if w3EricTalked == True:
        "If I didn't know Lucy was the one who directed him here, the conversation was so brief and undogged that I would've said this had to be a coincidence."
    else:
        "The conversation was so brief and undogged that this really had to just be a coincidence."

    scene w3_6902 with dissolve
    lucy "{i}...wants to talk.{/i}"
    "And if Kat intended the random encounter to be disconcerting, to remind Felicia she was flying close to the sun, it lacked any punch."
    scene w3_6903 with dissolve
    eric "...hello? Yes, yes. I'm here. Right--"
    eric "In fact--"
    scene w3_6904 with dissolve
    "........."
    "......"
    scene w3_6905 with dissolve
    mc "...you handled that well."
    scene w3_6906 with dissolve
    fel "'Bound to happen, and something I need to get used to."
    scene w3_6905 with dissolve
    mc "You know, if you win the competition and become a member, most of the patrons won't respect you - {i}just like that.{/i}"
    scene w3_6906 with dissolve
    fel "At best, I'll be a novelty."
    scene w3_6905 with dissolve
    mc "...then why do you want to be a member?"
    scene w3_6906 with dissolve
    fel "Because I like throwing myself off the deep end. Besides, people like novelty. It sells."
    scene w3_6907 with dissolve
    mc "...but it wears off. That's its defining characteristic."
    scene w3_6908 with dissolve
    fel "Hand over hand, one rung of the ladder at a time, stud."
    scene w3_6909 with dissolve

    if w3LucyConfront == True:
        mct "(Hmm...)"
        "As Waylon spoke on the phone, the one that Lucy handed him, my mind naturally went back to where I was 20 minutes ago."
        mct "(What the fuck are they up to...?)"
        "...and I wondered who he was talking to."
    else:

        mct "(Hmm...)"
        "It was odd that Lucy had handed Eric Waylon the phone."
        mct "(I wonder who he's talking to.)"

    scene w3_6905 with dissolve
    mc "I hope that didn't spoil your mood."
    scene w3_6906 with dissolve
    fel "Too good of a moment to be spoiled by something like--"
    scene w3_6910 with dissolve
    denise "I k-know! Just-- thank you--"
    scene w3_6911 with dissolve
    "Felicia's championed artist became another sudden point of interest, as a frantic energy overtook her shyness."
    scene w3_6912 with dissolve
    denise "Why do you keep, th-the s-same thing-- over and--"
    scene w3_6913 with dissolve
    "She mouthed the words {i}you're not a very nice person{/b}."
    scene w3_6914 with dissolve
    "...before scurrying away and leaving the critic with a bemused smirk on her face."
    mct "(What a fuckin' cunt...)"
    scene w3_6915 with dissolve
    mc "Looks like your girl had enough of that bitch's shit."
    scene w3_6916 with dissolve
    fel "..."
    "It was a quiet, seething anger that coursed through the blonde's veins."
    "........."
    scene w3_6917 with dissolve
    "......"
    scene w3_6918 with dissolve
    mc "...she'll be alright. There will be a lot of critics in her career."
    scene w3_6919 with dissolve
    fel "That is true..."
    scene w3_6918 with dissolve
    mc "It's not your fault."
    scene w3_6919 with dissolve
    fel "I understand, but..."
    scene w3_6917 with dissolve
    "......"
    scene w3_6920 with dissolve
    mc "...but?"
    scene w3_6921 with dissolve
    fel "But I don't care."
    scene w3_6916 with dissolve
    "......"
    scene w3_6915 with dissolve
    mc "...are you considering drowning her in the fountain right now?"
    scene w3_6921 with dissolve
    fel "That would be..."
    scene w3_6922 with pixellate
    "......"
    mc "...that would be insane?"
    fel "...too {i}public{/i}."
    scene w3_6923 with pixellate
    "That sounded like an unconvincing, flimsy impediment."
    scene w3_6924 with dissolve
    fel "Then again, my husband has good lawyers..."
    scene w3_6923 with dissolve
    "All things considered, we had achieved what we had set out to do here. That was, look at some paintings..."
    scene w3_6917 with dissolve
    "I could suggest we get out of here, to find something else to put her mind at rest, but that would mean leaving the exhibition on a sour note."
    "However, I could tell Felicia desperately wished she could do something..."
    hide screen textbox2 with dissolve

    menu w3FelDateDeniseDecision:
        "Suggest she go talk to Denise (while you go talk to Lucy.) (w3FeliciaDeniseConvinced = True)"(chg=["felicia_passion_up"]) if w3LucyConfront == True:
            $ Felicia_Confidence += 1
            $ w3FeliciaDeniseConvinced = True
            scene w3_6925 with dissolve
            show screen textbox2 with dissolve
            mc "You do know that if you don't say hello tonight, you're a creepy stalker, right?"
            scene w3_6926 with dissolve
            fel "...you're saying I should go talk to her?"
            scene w3_6925 with dissolve
            mc "It's better than staring daggers into that bitch's back."
            scene w3_6926 with dissolve
            fel "I... I don't have anything to say."
            scene w3_6925 with dissolve
            mc "I'm pretty sure you're like her biggest fan. You could start with that."
            scene w3_6919 with dissolve
            fel "A David Hasselhoff poster helped usher me into womanhood. Should I meet him too?"
            scene w3_6920 with dissolve
            mc "...I don't think he's here tonight."
            scene w3_6927 with dissolve
            "......"
            scene w3_6928 with dissolve
            mc "...Seriously, you just told me how alike you two are. Do you really not have anything to say?"
            jump w3FelDeniseTalkPersuade

        "Suggest she go talk to Denise. (w3FeliciaDeniseConvinced = True)"(chg=["felicia_passion_up"]) if w3LucyConfront == False:
            $ Felicia_Confidence += 1
            $ w3FeliciaDeniseConvinced = True
            scene w3_6925 with dissolve
            show screen textbox2 with dissolve
            mc "You do know that if you don't say hello tonight, you're a creepy stalker, right?"
            scene w3_6926 with dissolve
            fel "...you're saying I should go talk to her?"
            scene w3_6925 with dissolve
            mc "It's better than staring daggers into that bitch's back."
            scene w3_6926 with dissolve
            fel "I... I don't have anything to say."
            scene w3_6925 with dissolve
            mc "I'm pretty sure you're like her biggest fan. You could start with that."
            scene w3_6919 with dissolve
            fel "A David Hasslehoff poster helped usher me into womanhood. Should I meet him too?"
            scene w3_6920 with dissolve
            mc "...I don't think he's here tonight."
            scene w3_6927 with dissolve
            "......"
            scene w3_6928 with dissolve
            mc "...seriously, you just told me how alike you two are. Do you really not have anything to say?"
            jump w3FelDeniseTalkPersuade
        "{color=#FF1493}[[Blackmail]{/color} You DO have those photos... (if w3LizaBlackMail = True)"(chg=["maid"]) if mod_week3_bl_lucy == True:
            jump mod_ch4up4_bl_lucy_menu
        "{color=#FF1493}[[Blackmail]{/color} You DO have those photos... (if w3LizaBlackMail = True)" if w3LizaBlackMail == True and not mod_week3_bl_lucy:
            label mod_ch4up4_bl_lucy_menu:
            show screen textbox2 with dissolve
            "I don't know what possessed me, it's not like I cared if Denise got a shitty review on the back page of some barely-read paper..."
            scene w3_6929 with dissolve
            mct "(...besides, that's a crime, right? Even if it's something small like this?)"
            "That's what I thought, but the word \"crime\" felt so quaint. Inconsequential."
            scene w3_6930 with dissolve
            mc "Hey, Felicia?"
            "Maybe I just wanted to do Felicia a favor, maybe the thought gave me a rush..."
            fel "Hmmm...?"
            scene w3_6931 with dissolve
            "......"
            "..."
            mc "I'm spitballing here."
            scene w3_6932 with dissolve
            fel "......"
            fel "..."
            mc "Would other people seeing that image be undesirable for her?"
            fel "[mcf], you..."
            "She looked surprised."
            scene w3_6933 with dissolve
            fel "This is something my husband would think of."
            "She looked surprised, but I couldn't tell if she thought that was a grim observation or not."
            mc "Bad idea?"
            scene w3_6932 with dissolve
            fel "......"
            fel "...it's not like she'd get fired over it, but it'd be embarrassing."
            scene w3_6934 with dissolve
            mc "Embarrassing enough to convince her to write a good review?"
            fel "[mcf], I don't--"
            "She stopped, and considered."
            scene w3_6935 with dissolve
            "{i}Really considered.{/i}"
            "Undoubtedly shifting through her feelings, the potential consequences, and the morality of my supposition."
            scene w3_6936 with dissolve
            fel "{b}No.{/b} I'd be compromising her integrity without her knowledge. Even if she doesn't know about it, getting a good review through coercion is worse than getting a bad one you don't deserve."
            scene w3_6937 with dissolve
            "The pragmatic woman proved surprisingly impractical on the subject."
            hide screen textbox2 with dissolve

            menu:
                "You respect it."(chg=["felicia_passion_up"]):
                    $ Felicia_Confidence += 1
                    scene w3_6938 with dissolve
                    show screen textbox2 with dissolve
                    mc "Like I said, was just a random thought. I took that without even thinking earlier..."
                    "Good on you for having scruples."
                    scene w3_6935 with dissolve
                    fel "......"
                    scene w3_6939 with dissolve
                    fel "..."
                    hide screen textbox2 with dissolve

                    menu:
                        "Suggest she go talk to Denise. (w3FeliciaDeniseConvinced = True)"(chg=["felicia_passion_up"]):
                            $ Felicia_Confidence += 1
                            $ w3FeliciaDeniseConvinced = True
                            scene w3_6925 with dissolve
                            show screen textbox2 with dissolve
                            mc "Well then, there's always another way you could improve Denise's night."
                            scene w3_6926 with dissolve
                            fel "...and what's that?"
                            scene w3_6925 with dissolve
                            mc "Just go talk to her, idiot. You said you two were alike. You really don't have anything to say to her?"
                            jump w3FelDeniseTalkPersuade
                        "Suggest you leave, then."(chg=["felicia_passion_down"]):

                            $ Felicia_Confidence -= 1
                            scene w3_6940 with dissolve
                            show screen textbox2 with dissolve
                            mc "Let's get out of here. Tonight seems like a success, and like Ray said, no such thing as bad press."
                            scene w3_6941 with dissolve
                            fel "......"
                            scene w3_6942 with dissolve
                            fel "Y-yeah. Let's shift gears."
                            jump w3ArtExhibitionOutro

                "You CAN think of an alternative... (w3ActuallyBlackmail = True)"(chg=["maid"]) if mod_week3_bl_lucy == True:
                    jump mod_ch4up4_bl_lucy_menu_2
                "You CAN think of an alternative... (w3ActuallyBlackmail = True)" if mod_week3_bl_lucy == False:
                    label mod_ch4up4_bl_lucy_menu_2:
                    $ w3ActuallyBlackmail = True
                    scene w3_6943 with dissolve
                    show screen textbox2 with dissolve
                    mc "If that's your hangup, does it even have to be a good review?"
                    mc "If she wouldn't have been here if you weren't a fan, then, just convincing her not to write one altogether would be nothing gained and nothing lost."
                    scene w3_6944 with dissolve
                    fel "......"
                    scene w3_6945 with dissolve
                    fel "...I don't know if she'll listen to me. Hell, it might make--"
                    scene w3_6943 with dissolve
                    mc "I'll do it."
                    scene w3_6945 with dissolve
                    fel "...you'll blackmail someone on my behalf?"
                    scene w3_6943 with dissolve
                    mc "Why not? I'm not going to think of it that way, though."
                    mc "Seems like too big of a word for this."
                    scene w3_6927 with dissolve
                    "......"
                    "..."
                    hide screen textbox2 with dissolve
                    menu:
                        "In the meanwhile: suggest she go talk to Denise. (w3FeliciaDeniseConvinced = True)"(chg=["felicia_passion_up", "maid"]):
                            $ Felicia_Confidence += 1
                            $ w3FeliciaDeniseConvinced = True
                            scene w3_6928 with dissolve
                            show screen textbox2 with dissolve
                            mc "And while I do that, why don't you go do something only you can do."
                            scene w3_6926 with dissolve
                            fel "...and what's that?"
                            scene w3_6925 with dissolve
                            mc "Just go talk to her. Do you really not have anything to say to her that would help her feel better about freaking out?"
                            jump w3FelDeniseTalkPersuade
                        "Suggest she go to the bathroom."(chg=["felicia_passion_down"]):

                            $ Felicia_Confidence -= 1
                            scene w3_6946 with dissolve
                            show screen textbox2 with dissolve
                            mc "In the meantime, stay out of sight. Go to the bathroom or something."
                            fel "...?"
                            mc "I doubt she even remembers seeing me with you."
                            scene w3_6942 with dissolve
                            fel "Yeah... {i}okay.{/i}"
                            jump w3LizaBlackmailMontage
        "Suggest you get out of here."(chg=["felicia_passion_down"]):

            $ Felicia_Confidence -= 1
            scene w3_6940 with dissolve
            show screen textbox2 with dissolve
            mc "Let's get out of here. Find some dinner. Tonight seems like a success."
            scene w3_6941 with dissolve
            fel "......"
            scene w3_6942 with dissolve
            fel "That sounds good to me.."
            jump w3ArtExhibitionOutro

        "{color=#696969}[[Blackmail] You do have those photos...{/color}" if w3LizaBlackMail == False:
            jump w3FelDateDeniseDecision

label w3FelDeniseTalkPersuade:
    scene w3_6947 with pixellate
    fel "It'd just be awkward and forced. She'll want me to go away."
    mc "...or she might not. I'm not saying go dispense sagely wisdom. Just tell her you think she's cool and take it from there."
    mc "People like hearing that kinda shit. Why are you so apprehensive about introducing yourself to a girl?"
    scene w3_6948 with pixellate
    mct "(You fuck on stage...)"
    scene w3_6949 with dissolve
    mc "Do you think she's better than you?"
    scene w3_6948 with dissolve
    fel "..."
    scene w3_6950 with dissolve
    mc "I mean, you have a unique perspective, Felicia. You've been in her shoes and you're good at dealing with other people's opinions."
    scene w3_6951 with dissolve
    fel "Yeah, and I jumped out those shoes the first chance I got. I got nothing worth--"
    scene w3_6952 with dissolve
    "She stopped, slinking back into her thoughts."
    scene w3_6950 with dissolve
    mc "It's just a suggestion. I think you have a good shot at helping her feel better, you know... since she just shouted at an influential critic at her first big event."
    scene w3_6952 with dissolve
    fel "........."
    fel "......"
    scene w3_6953 with dissolve
    fel "...fuck, I should go talk to her."
    scene w3_6952 with dissolve
    "{i}Bullseye.{/i} She said it almost as a whisper."
    stop music fadeout 3.0
    scene w3_6954 with dissolve

    if w3ActuallyBlackmail == True:
        mc "Go, and I'll talk to Liza about the importance of journalistic integrity."
        fel "Alright, then. I have a good guess of where she ran off to..."
    else:
        mc "Go. I'll be around. You want help finding her?"
        fel "No, thanks. I have a guess as to where she ran off to..."

    scene black with fade
    "......"
    "..."
    if w3ActuallyBlackmail == True:
        scene w3_6955 with dissolve
        "I had no idea how long Felicia's conversation would take, but..."
        scene w3_6956 with dissolve
        "I was going to be quick about this."
    elif w3LucyConfront == True:
        scene w3_6957 with dissolve
        "I had no idea how long Felicia's conversations would take, but her absence presented an opportunity."
        scene w3_6958 with dissolve
        "I could finally talk to Lucy."
    else:
        mct "(Well... who knows how long this might take.)"
        "......"
        "..."
        mct "(I guess I'll try the punch...)"

    jump w3FeliciaDeniseTalk

label w3FeliciaDeniseTalk:
    play music "music/a-nice-dream.ogg"
    scene w3_6959 with wipeleft
    fel "Umm... {i}hey{/i}."
    scene w3_6960 with dissolve
    denise "......"
    denise "...h-hello."
    scene w3_6961 with dissolve
    fel "Am I interrupting anything? I can leave you be, I just..."
    fel "My name is Felicia Barnes and I'm... I'm a big fan of yours. I've admired your work for a long time, in fact."
    scene w3_6962 with dissolve
    denise "I, uh... I know who you are."
    fel "...y-you do?"
    scene w3_6963 with dissolve
    denise "Well... I didn't know your name, but you bought the first painting I ever sold. R-right?"
    scene w3_6964 with dissolve
    fel "...how did you know that?"
    scene w3_6963 with dissolve
    denise "You were the only one who spared it a passing glance during that show. Actually, uh... you looked at it for a while."
    denise "Like a {i}awhile{/i} awhile."
    scene w3_6965 with dissolve
    fel "{b}Oh.{/b} That makes sense."
    denise "...but even if you didn't, I'd probably remember you. You, uh... you stick out."
    scene w3_6966 with dissolve
    fel "......"
    denise "I-in a good way."
    scene w3_6967 with dissolve
    fel "I tried to be anonymous. I'm not really sure why..."
    scene w3_6968 with dissolve
    denise "I get that, I... I stick out too."
    scene w3_6967 with dissolve
    fel "How's the show going?"
    scene w3_6968 with dissolve
    denise "About... {i}as expected.{/i}"
    scene w3_6967 with dissolve
    fel "Tell me about it."
    scene w3_6969 with dissolve
    denise "I haven't gotten used to some aspects of it, but..."
    scene w3_6970 with dissolve
    "........."
    "......"
    scene w3_6969 with dissolve
    denise "...I'm trying to, but it's touch and go."
    scene w3_6971 with dissolve
    fel "You know, I debated against even introducing myself to you tonight?"
    scene w3_6972 with dissolve
    denise "...how come?"
    scene w3_6971 with dissolve
    fel "I was feeling... {i}shy.{/i}"
    scene w3_6972 with dissolve
    denise "That's hard to believe."
    scene w3_6971 with dissolve
    fel "Actually, I'm only talking to you because a {b}friend{/b} of mine told me I was being stupid. Which, he had a point...."
    scene w3_6973 with dissolve
    "........."
    "......"
    fel "...I've been following your career for a while. Ever since you won the FAA award."
    scene w3_6974 with dissolve
    denise "Oh, that was just--"
    scene w3_6975 with dissolve
    fel "An especially beautiful entry - and I - and I just wanted to tell you..."
    fel "...you're an inspiration to me."
    scene w3_6976 with dissolve
    denise "Oh, uh... {i}thank you.{/i}."
    scene w3_6977 with dissolve
    "........."
    scene w3_6978 with dissolve
    "......"
    scene w3_6979 with dissolve
    denise "...m-me?!"
    scene w3_6980 with dissolve
    fel "Yeah. {b}You{/b}."
    fel "Art is a very personal subject for me too. I think it's amazing you pushed past what you said in your essa--."
    scene w3_6979 with dissolve
    denise "Wait... that's what inspired you?"
    scene w3_6981 with dissolve
    denise "......"
    scene w3_6982 with dissolve
    denise "...you w-wanna take a walk with me?"
    scene black with fade
    fel "Sure. I-if you don't mind me intruding on you trying to get away..."
    $ mod_var = False
    if mod_week3_bl_lucy == True:
        if w3ActuallyBlackmail and w3LucyConfront:
            $ mod_var = True
            jump w3LizaBlackmailTalk
        elif w3ActuallyBlackmail == True:
            jump w3LizaBlackmailTalk
        elif w3LucyConfront == True:
            jump w3LucyActuallyConfront
        else:
            jump w3EdwinIdleMontage

    elif w3ActuallyBlackmail == True:
        jump w3LizaBlackmailTalk
    elif w3LucyConfront == True:
        jump w3LucyActuallyConfront
    else:
        jump w3EdwinIdleMontage

label w3LizaBlackmailMontage:
    scene w3_6955 with dissolve
    "While Felicia made herself scant, I found Elizabeth Averell and pulled her aside."
    scene w3_6956 with dissolve
    "She looked at me dubiously but complied. We found ourselves off to the side and..."
    jump w3LizaBlackmailTalk

label w3LizaBlackmailTalk:
    play music "music/leaving-home.ogg"
    scene w3_6983 with wiperight
    mc "Well... this is awkward."
    scene w3_6985 with dissolve
    "This was my best attempt at a stern and steady expression, one to mask the foul mixture of excitement and unease brewing in my gut."
    scene w3_6984 with dissolve
    "I had taken the picture so offhandedly, I had mentioned it so casually to Felicia, but the reality was much more {b}heightened.{/b}"
    scene w3_6985 with dissolve
    "The look of gradual understanding and disbelief, as she glanced from the phone to me, back to the phone, and back again to me..."
    scene w3_6986 with dissolve
    liza "...fuck you. No one will care."
    mc "...no?"
    liza "{b}No{/b}."
    scene w3_6987 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Call her bluff.":
            scene w3_6990 with dissolve
            show screen textbox2 with dissolve
            mc "Fair enough. We can test that hypothesis. Goodbye--"
            scene w3_6991 with dissolve
            liza "Fuck you! You little creep! T-taking pictures of strangers!"
            scene w3_6992 with dissolve
            mc "Don't touch me, you fucking {b}skank.{/b}"
            liza "S-sorry!"
            "I said it sharply, and the edge in my voice pierced the critic's skin."
        "Double down.":

            scene w3_6988 with dissolve
            show screen textbox2 with dissolve
            mc "You don't think anyone will care that you're snorting drugs at a show you're reviewing? Will you even remember what you saw tonight?"
            scene w3_6989 with dissolve
            liza "Fuck you! It's nootropic!"
            scene w3_6988 with dissolve
            mc "Now there's a good word for a skanky, pretentious bitch."
            "I felt I was channeling a bit of Felicia with that line, although the sadism coursing through my veins was definitely my own."
            scene w3_6989 with dissolve
            liza "You fuckin-"
            scene w3_6988 with dissolve
            mc "Is \"fuck\" all you can say?"
            scene w3_6993 with dissolve
            liza "..."

    scene w3_6994 with dissolve
    "I could tell she wasn't used to anyone speaking to her like this."
    scene w3_6995 with dissolve
    liza "W-what you're doing is way worse than what's in that photo, you know that, right?!"
    scene w3_6996 with dissolve
    mc "Oh, definitely, but so what?"
    scene w3_6997 with dissolve
    liza "You-"
    hide screen textbox2 with dissolve

    menu:
        "Cut her off, rudely."(chg=["tough_up"]):
            $ toughness += 1
            scene w3_6998 with dissolve
            show screen textbox2 with dissolve
            mc "Shut your goddamn mouth."
            "Again, I spoke unfiltered, keeping in control of the conversation and relishing the flustered look on the socialite's face all the while."
            scene w3_6999 with dissolve
            liza "I, uh-"
            "The woman sputtered, before gulping down a glob of spit pooling from her words."
            scene w3_7000 with dissolve
            mc "......"
            mc "..."
            "I waited to see if she'd continue, but she seemed gobsmacked and pacified by rudeness."
        "Let her finish.":

            scene w3_7001 with dissolve
            show screen textbox2 with dissolve
            liza "You have any idea who I am?"
            scene w3_7002 with dissolve
            mc "Your name is Elizabeth Averell, you write for the Herald, and you're a self-important bitch."
            scene w3_7003 with dissolve
            "......"
            "..."

    scene w3_7004 with dissolve
    mc "You make a good point; it's not the worst thing in the world, no, but I'm not asking for a million dollars either."
    scene w3_7005 with dissolve
    liza "What ARE you asking for?"
    scene w3_7006 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Use body language to drive the point home."(chg=["tough_up"]):
            $ toughness += 1
            scene w3_7007 with dissolve
            show screen textbox2 with dissolve
            "One small step was all it took to invade the woman's personal space."
            scene w3_7008 with dissolve
            mc "I'm glad you asked, Liz."
            scene w3_7009 with dissolve
            "In this context, a small step would feel harrowing."
            scene w3_7008 with dissolve
            mc "All you need to do is..."
            scene w3_7009 with dissolve
            "She instinctually sized me up and down, and her expression told me that this one little step was akin to stepping on her.."
            scene w3_7010 with dissolve
            mc "...forget you came here tonight."
            scene w3_7011 with dissolve
            liza "W-wha? H-huh?"
            scene w3_7012 with dissolve
            mc "Go home."
            scene w3_7005 with dissolve
            liza "That's it...?"
            scene w3_7004 with dissolve
            mc "Yeah. {b}That's it.{/b}"
        "Say it simply.":

            scene w3_7004 with dissolve
            show screen textbox2 with dissolve
            mc "Forget what you came here to do tonight."
            scene w3_7005 with dissolve
            liza "Excuse me? What does that mean?"
            scene w3_7004 with dissolve
            mc "Just go home."

    mc "Don't write anything about tonight, good or otherwise."
    scene w3_6995 with dissolve
    liza "Why would you-- Who put you up to--"
    scene w3_6996 with dissolve
    mc "No one did. I've seen you a couple times tonight, and make no mistake, you're a bully."
    mc "Besides, we both know you didn't come here with objective intentions tonight, don't we?"
    scene w3_6995 with dissolve
    liza "...that's {i}all{/i} you want?"
    scene w3_6994 with dissolve
    "The way she emphasized her question confirmed what I suspected: journalistic integrity wasn't a concern for her."
    scene w3_7013 with dissolve
    mc "You think I should ask for more?"
    scene w3_7001 with dissolve
    liza "Fuck you!"
    scene w3_6997 with dissolve
    "She reminded me of a little, yappy poodle."
    scene w3_7002 with dissolve
    mc "...yes or no, Mrs. Averell?"
    scene w3_7000 with dissolve
    liza "......"
    scene w3_7005 with dissolve
    liza "...fine! I don't think my editor would've ran it anyway. Not at the height of summer."
    scene w3_7004 with dissolve
    mc "That was simple."
    scene w3_7014 with dissolve
    mc "Goodbye, Mrs--"
    scene w3_7015 with dissolve
    liza "Well, this is a first for me."
    mc "...{i}yeah.{/i} Same?"
    scene w3_7016 with dissolve
    liza "......"
    scene w3_7017 with dissolve
    liza "...it's {b}Miss{/b} Alverell, by the way."
    mct "(Crazy bitch...)"
    if mod_var:
        jump w3LucyActuallyConfront
    elif w3FeliciaDeniseConvinced == True:
        jump w3FeliciaDeniseEnding
    else:
        jump w3ArtExhibitionOutro

label w3EdwinIdleMontage:
    scene w3_7030 with fade
    "............"
    "........."
    "......"
    scene w3_7031 with dissolve
    "...nice weather. I bet Felicia's hitting it--"
    jump w3FeliciaDeniseEnding


label w3LucyActuallyConfront:
    play music "music/doll-dancing.ogg"
    scene w3_7032 with dissolve
    lucy "Can this wait until later, I really should get back to--"
    mc "Not to worry. Mr. Waylon seems pretty occupied right now, plus he gave me his permission to borrow some of your time earlier."
    scene w3_7033 with dissolve
    lucy "...he did?"
    mc "His generosity knows no bounds."
    scene w3_7037 with dissolve
    lucy "......"
    scene w3_7034 with dissolve
    lucy "...uh, so... what did you want to speak about?"
    scene w3_7035 with dissolve
    "Once more, I considered how I might play this."
    scene w3_7036 with dissolve
    mc "He mentioned something curious. He said it was your idea to come here for a date tonight."
    scene w3_7035 with dissolve
    "And I decided to start with a direct statement to test the waters and see how that fared."
    scene w3_7034 with dissolve
    lucy "Y-yeah... I saw a flyer for -- and-- ummm... you see, he said he was interested in art and--"
    scene w3_7036 with dissolve
    mc "--and you took some initiative for a cherished client?"
    scene w3_7037 with dissolve
    "If she was trying to keep this under wraps..."
    scene w3_7038 with dissolve
    lucy "That was the idea, yes... I don't get why you're--"
    scene w3_7037 with dissolve
    mct "(Man, she was awful at this.)"

    if w3CoincidenceAskTwice == True:
        scene w3_7039 with dissolve
        mc "It just struck me as odd, because... well... you said it was his idea."
        scene w3_7038 with dissolve
        lucy "I misspoke."
        scene w3_7037 with dissolve
        "She said it flat and quickly, with no further explanation, as if changing tactics."
        scene w3_7039 with dissolve
    else:
        scene w3_7039 with dissolve
        mc "It's just..."

    mc "I have a feeling that there's more to it than that. Am I mistaken?"
    scene w3_7040 with dissolve
    "A clear unease permeated the teacher-turned-whore's body language and I got the sense that talking to me was placing her in a difficult spot."
    hide screen textbox2 with dissolve

    menu:
        "Open up and reassure her you're not trying to get her in trouble."(chg=["tough_down","lucy_up"]):
            $ toughness -= 1

            if w3LucyTouch == True:
                $ w3LucyAffability += 2
                scene w3_7042 with dissolve
                "Unlike last time, I refrained from adding a touch."
                mc "Relax, Lucy."
                "Instead, I took a step back, to give Lucy a feeling of space."
            else:
                $ w3LucyAffability += 1
                scene w3_7041 with dissolve
                mc "Relax, Lu--"
                "The moment I reached out to touch her, I knew I made a mistake. "
                scene w3_7042 with dissolve
                "So I immediately pivoted, backing up in hope of giving Lucy a feeling of space."

            mc "I'm not trying to trip you up."
            scene w3_7043 with dissolve
            lucy "..."
            scene w3_7044 with dissolve
            mc "Just kinda in the dark here."

            if kat_polite == True:
                mc "Mrs. Pulman has you under marching orders, right?"
            else:
                mc "The old woman has you under marching orders, correct?"

            scene w3_7045 with dissolve
            lucy "..."
            scene w3_7046 with dissolve
            mc "If it's a yes, how 'bout you don't answer me."
            scene w3_7045 with dissolve
            lucy "............"
            lucy "........."
            lucy "......"
            scene w3_7047 with dissolve
            lucy "...n-no."
            scene w3_7048 with dissolve
            mc "Heh. Not quite, huh?"
            mct "(I thought I had her.)"
            scene w3_7050 with dissolve

            if w3LucyAffability >= 3:
                lucy "I'm just, just here as Mr. Waylon's date, [mcf]."
                scene w3_7049 with dissolve
                "The switch to [mcf] from Mr. [mcl] was notable."
            else:
                lucy "I'm just playing arm candy, Mr. [mcl]."
                scene w3_7049 with dissolve


            mc "Yet, we both know there's something more to it. What's the harm in admitting that?"
            scene w3_7052 with dissolve
            lucy "I haven't the faintest idea what ANY of you are up to."
            scene w3_7051 with dissolve
            mct "(That was fair...)"
            "Me, Eric, or Kathleen were more similar to each other than she was."
            "I could try to shift that perception some, or I could attempt to leverage the difference in power to my advantage."
        "Close off the space and play into her trepidation."(chg=["lucy_passion_up","tough_up"]):


            $ w3LucyPressure += 1
            $ toughness += 1

            scene w3_7054 with dissolve
            mc "Okay, Lucy... different question..."
            scene w3_7053 with dissolve
            "I probably looked like a creep right now, and perhaps it was owed to our individual positions at the club, but I felt emboldened."
            scene w3_7054 with dissolve
            mc "What is it about my first question that makes you look like you wanna run away?"
            scene w3_7055 with dissolve
            "Like this was a natural thing for me to do."
            scene w3_7056 with dissolve
            lucy "I--"
            scene w3_7057 with dissolve
            mc "Before you start: are you going to lie to me?"
            scene w3_7056 with dissolve
            lucy "Uh--"
            scene w3_7054 with dissolve
            mc "I'm not asking you to tell me what you're doing here, but at least admit this is more than a coincidence."
            scene w3_7057 with dissolve
            mc "We both know it is; what's the point in insisting otherwise?"
            scene w3_7055 with dissolve
            lucy "..."
            scene w3_7057 with dissolve

            if kat_polite == True:
                mc "I'll say it more directly: Mrs. Pulman has you up to something, right?"
            else:
                mc "I'll say it more directly: the old woman has you up to something, right?"

            scene w3_7058 with dissolve
            lucy "......"
            scene w3_7059 with dissolve

            if w3LucyAffability >= 3:
                lucy "...I'm just, just here as Mr. Waylon's date, [mcf]."
                scene w3_7058 with dissolve
                "The switch to [mcf] from Mr. [mcl] was notable."
            else:
                lucy "...I'm just playing arm candy, Mr. [mcl]."
                scene w3_7058 with dissolve

            "I wasn't even getting that out of her."
            scene w3_7060 with dissolve
            mc "You're tough to crack."
            scene w3_7050 with dissolve
            lucy "I haven't the faintest idea what ANY of you are up to."
            scene w3_7049 with dissolve
            mct "(That was...)"
            scene w3_7051 with dissolve
            "...fair."
            "Me, Eric, or Kathleen were more similar to each other than she was."
            "I could switch gears and try to alter that perception, or I could use that power-gap to my advantage."

    "How should I proceed?"

    menu:
        "Appeal to a feeling of commiseration."(chg=["lucy_up"]):
            $ w3LucyAffability += 1
            jump w3LucyCommiserate
        "Insinuate that you two should have a good relationship. (w3LucyRelationshipOffer = True)"(chg=["lucy_passion_up"]):

            $ w3LucyPressure += 1
            $ w3LucyRelationshipOffer = True
            jump w3LucyProQuo


label w3LucyCommiserate:
    if _in_replay:
        play music "music/doll-dancing.ogg"

    "You get more flies with honey than with vinegar."
    scene w3_7061 with dissolve

    if kat_polite == True:
        mc "*Sigh* I get it. It's in a different way, but Mrs. Pulman jerks me around too."
    else:
        mc "*Sigh* I get it. It's in a different way, but Kathleen jerks me around too."

    mc "You're doing this to get your son into a good school, and I'm trying to pay for college. We're not {i}too{/i} different in that regard."
    scene w3_7062 with dissolve
    mc "So, yeah... again, {i}I get it.{/i}, coloring inside the lines."
    scene w3_7063 with dissolve
    "That was perhaps a strategy I should consider adopting as well. After all, if I wasn't told about it, I probably don't need to know."
    scene w3_7062 with dissolve
    mc "She won't know we talked, but should I just drop it, Luce?"
    scene w3_7063 with dissolve
    lucy "......"

    if w3LucyAffability >= 4:
        $ w3FeliciaKatCall = True
        scene w3_7064 with dissolve
        lucy "*Sigh* Ah, {b}euuugh...{/b}"
        scene w3_7065 with dissolve
        "Lucy promptly traded her forlorn look for an exasperated one."
        scene w3_7066 with dissolve
        lucy "You know, I expected to {b}fuck{/b}, but Mrs. Pulman is so {i}extra.{/i}"
        scene w3_7067 with dissolve
        mc "Uh huh. We've met."
        scene w3_7068 with dissolve
        lucy "I mean, having sex is one thing, but Mrs. Pulman's OTHER demands... I'm not built for this kind of thing. I'm a straightforward woman."
        scene w3_7066 with dissolve
        lucy "That's why I was okay with the club's arrangement. It seemed simple. {b}Mostly{/b}."
        scene w3_7065 with dissolve
        mct "(Huh...)"
        "Hearing the frustrated woman paint her relationship to the club in such a cold transactional light, while rather obvious if you thought about it, added an almost uncanny quality to Lucy's character."
        scene w3_7069 with dissolve
        lucy "Either way I'm in over my head, but at least dumb rutting doesn't require living out a fourth-rate John le Carré novel!"
        scene w3_7070 with dissolve
        lucy "......."
        scene w3_7071 with dissolve
        lucy "...um, sorry. Didn't mean to get that excited."
        mc "It's alright. The life we've chosen is new and frustrating, but it's the length you'll go to for your kid."
        scene w3_7072 with dissolve
        mct "(I'm being transparent, right...?)"
        scene w3_7073 with dissolve
        lucy "Yeah..."
        scene w3_7072 with dissolve
        "...but if she noticed, she didn't take umbrage with it. Perhaps any solidarity is better than none?"

        if w2ExLezSeen == True:
            "The raven-haired beauty's expression read scattered and susceptible, and knowing what I knew about her and Harper, I was aware of how pliable she was to a friendly touch."
        else:

            "The raven-haired beauty's expression read scattered and susceptible, perhaps even pliable to a friendly touch..."

        "Of course, I had already pierced a hole in her resolve. If I asked again, she would likely admit the truth - no need to go the extra mile."

        menu:
            "Get her to come close.":
                "...unless I wanted to."
                play music "music/i-knew-a-guy.ogg"
                scene w3_7074 with dissolve
                mc "Give me your hand."
                lucy "...?"
                scene w3_7075 with dissolve
                lucy "What are you...?"
                mc "Take it."
                scene w3_7076 with dissolve
                mc "We both entered this environment at the exact same time, pretty much."
                scene w3_7077 with dissolve
                lucy "I remember..."
                mct "(Yeah, that time when the old woman made me choose whose face I wanted to shoot my load on...)"
                scene w3_7076 with dissolve
                mc "You picked Ian during the trial due to him being more handsome-"
                scene w3_7078 with dissolve
                lucy "You're not, uh--"
                scene w3_7079 with dissolve
                mc "I'm not mad. I respect that mentality."
                scene w3_7080 with dissolve
                mc "It's just making the best of the situation."
                scene w3_7081 with dissolve
                lucy "..."
                scene w3_7082 with dissolve
                mc "I'm not going to insult you by saying you and I are in the same boat, but I do want you to get through this, get what you want, and put it all behind you."
                "I was so, SO transparent, yet..."
                scene w3_7083 with dissolve
                lucy "T-thanks."
                scene w3_7084 with dissolve
                "She willfully ignored that."
                scene w3_7085 with dissolve
                mc "What are you doing here tonight, Lucy?"
                scene w3_7086 with dissolve
                lucy "Mrs. Pulman wanted me to confirm if Felicia was here tonight or not..."
                scene w3_7085 with dissolve
                mc "Did she get her confirmation?"
                scene w3_7087 with dissolve
                lucy "That was her talking to Mr. Waylon on the phone..."
                scene w3_7086 with dissolve
                lucy "She's the one who had me suggest coming here tonight to him."
                scene w3_7085 with dissolve
                mc "So he's not {b}knowingly{/b} here because of Felicia?"
                scene w3_7086 with dissolve
                lucy "...no. He was really surprised to see her, actually."
                scene w3_7088 with dissolve
                mct "(More or less what I had expected, but this was confirmation - curious to note, whatever she's doing, it wasn't something she saw fit to include me in...)"
                scene w3_7082 with dissolve
                mc "Thank you, beautiful. And any idea why she wanted confirmation?"
                scene w3_7089 with dissolve
                lucy "N-no... you being here surprised her, though. When she learned you were here, she instructed me to report on you too... like how you were behaving... that sort of thing..."
                scene w3_7090 with dissolve
                lucy "I'm sorry, it's just--"
                mc "Do what she asks, Luce. Tell her I browbeat you, okay? No need for you to disappoint her."
                scene w3_7091 with dissolve
                lucy "R-really?"
                mc "Just don't tell her you admitted everything. Score some points with her, but say I guessed it."
                scene w3_7083 with dissolve
                lucy "Well, if you insist... heh..."
                scene w3_7092 with dissolve
                mc "Thank you for indulging my curiosity."

                if w3LucyAffability >= 5:
                    scene w3_7093 with dissolve
                    "My eyes set down the onyx-tinged path of Lucy's own peering orbs and got momentarily drawn into their confines."
                    scene w3_7094 with dissolve
                    lucy "Harper and I... {i}she's nice{/i}."
                    scene w3_7093 with dissolve
                    mc "Yeah?"
                    scene w3_7094 with dissolve
                    lucy "You seem nice, too."
                    scene w3_7093 with dissolve
                    "..."
                    scene w3_7095 with dissolve
                    "Trapped as I was, I watched something between an urge and idea take form within those dark pools."
                    scene fa_lucykiss_a with dissolve
                    show fa_lucykiss with dissolve
                    "Somehow, even though she was the one who pressed her painted lips into mine, she tricked me into feeling like it was all my doing."
                    lucy "Mmmhhh..."
                    "For a brief instant, all jitters subsided, as I grabbed and she pushed her body into mine."
                    "........."
                    "......"

                    if w3FeliciaPlatonic == True:
                        scene w3_7097 with dissolve
                        mc "...uh, I've... I've got a girlfriend..."

                    scene w3_7098 with dissolve
                    lucy "...Mr. Waylon's gonna fuck me hard tonight, and that's fine.... but I'm going to think about that handful of seconds."
                    scene w3_7099 with dissolve
                    lucy "Keep me in mind."

                    scene w3_7100 with dissolve
                    mc "Have a good night, for real this time - and good luck."
                    "The implication was clear, and I began to wonder, between Harper and her, who roped who into their sapphic tryst."
                    scene w3_7101 with dissolve
                    lucy "Yeah, uh... have a good night - for real this time."
                    scene black with fade
                    stop music fadeout 3.0
                    $ renpy.end_replay()

                    if not persistent.w3LucyAffable:
                        play sound "sound effects/notification.wav"
                        show memoryunlock with dissolve
                        $ renpy.pause(3, hard=True)
                        $ persistent.w3LucyAffable = True
                        hide memoryunlock with dissolve
                        $ renpy.pause(0.5, hard=True)

                    "At the very least, it was yet another reminder of Ian's warning about how slippery the club's cast could be."
                    $ history_lucy = "Through a little understanding, I got Lucy to confess that she was spying on Felicia for club business. No surprise there, but it's good to get confirmation."
                    $ unread_lucy = True
                    play sound "sound effects/notification.wav"
                    show bioupdate with dissolve
                    "......"
                    "..."
                    jump w3FeliciaKathleenCall
                else:

                    scene w3_7102 with fade
                    mc "Have a good night, for real this time - and good luck."
                    scene w3_7103 with dissolve
                    "......"
                    scene w3_7104 with dissolve
                    lucy "...y-you too."
                    scene black with fade
                    stop music fadeout 3.0
                    $ history_lucy = "Through a little understanding, I got Lucy to confess that she was spying on Felicia for club business. No surprise there, but it's good to get confirmation."
                    $ unread_lucy = True
                    play sound "sound effects/notification.wav"
                    show bioupdate with dissolve
                    "And that was that. A lot of effort circling the drain and I still don't know what's fully going on, but it's something - plus I felt like I won Lucy over somewhat."
                    mct "(Not too shabby...)"
                    "Besides, if Lucy tells Kat what I asked her to...."
                    jump w3FeliciaKathleenCall
            "Ask about the spy-novel shit she eluded to.":



                scene w3_7107 with dissolve
                if kat_polite == True:
                    mc "Tell me about the mission Mrs. Pulman has you doing."
                else:
                    mc "Tell me about that John le Carré shit the old woman has you doing."

                scene w3_7072 with dissolve
                lucy "......"
                scene w3_7073 with dissolve
                lucy "...I was... I was told to confirm whether or not Mrs. Ford was here tonight, and then let Mrs. Pulman know."
                scene w3_7107 with dissolve
                mc "Does she know?"
                scene w3_7106 with dissolve
                lucy "That was her talking to Mr. Waylon. She's the one who had me suggest coming here tonight to him."
                scene w3_7107 with dissolve
                mc "So, he wasn't here specifically for Felicia?"
                scene w3_7106 with dissolve
                lucy "No... he was genuinely surprised to discover she was here."
                scene w3_7108 with dissolve
                mct "(More or less what I had expected, but this was confirmation - curious to note, whatever she's doing, it wasn't something she saw fit to include me in...)"
                scene w3_7107 with dissolve
                mc "...Thank you. You don't have any inkling why Mrs. Pulman wanted to know if Felicia was here tonight?"
                scene w3_7106 with dissolve
                lucy "No, but it seems she didn't expect you to be with her. When she heard that, she told me to report on you too... just how you're behaving, what you were doing..."
                scene w3_7109 with dissolve
                lucy "S-sorry. She told me to keep tight-lipped with Mr. Waylon, and well... anyone else... she was emphatic about it."
                mc "Don't worry about it. Actually, do what she expects. Let her know I browbeat you, okay?"
                scene w3_7106 with dissolve
                lucy "You want me to tell her I spilled my--"
                scene w3_7107 with dissolve
                mc "Leave that part out. Just mention to her that I pestered you, and pretty much guessed."
                scene w3_7110 with dissolve
                lucy "A-alright..."
                scene w3_7111 with dissolve
                mc "Thanks for indulging my curiosity."
                lucy "I can go...?"
                scene w3_7112 with dissolve
                mc "Have a good night, for real this time."
                lucy "Y-you too."
                scene w3_7113 with dissolve
                "And that was that. A lot of effort circling the drain and I still don't know what's fully going on, but it's something - plus I felt like I won Lucy over somewhat."
                scene black with fade
                stop music fadeout 3.0
                $ history_lucy = "Through a little understanding, I got Lucy to confess that she was spying on Felicia for club business. No surprise there, but it's good to get confirmation."
                $ unread_lucy = True
                play sound "sound effects/notification.wav"
                show bioupdate with dissolve
                mct "(Not too shabby...)"
                "Besides, if Lucy tells Kat what I asked her to...."
                jump w3FeliciaKathleenCall
    else:


        scene w3_7073 with dissolve
        lucy "P-please."
        scene w3_7072 with dissolve
        "{i}A gamble that didn't pay off.{/i}"
        "Still, that was good enough for me, and a confirmation in a way."
        scene w3_7109 with dissolve
        mc "Sorry for the hassle. Have a good night."
        lucy "I can go...?"
        mc "It's a free country."
        scene w3_7072 with dissolve
        "......"
        scene w3_7114 with dissolve
        lucy "...t-thanks."
        scene w3_7113 with dissolve
        "That could've gone better."
        scene black with fade
        stop music fadeout 3.0
        $ history_lucy = "I have only my gut feeling in the negative that running into Lucy at the art exhibition {i}wasn't{/i} a coincidence."
        $ unread_lucy = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve
        "......"
        "..."
        jump w3FeliciaDeniseEnding

label w3LucyProQuo:
    scene w3_7116 with dissolve
    mc "...shouldn't we be friends, Luce?"
    scene w3_7115 with dissolve
    lucy "I'm not looking to make friends."

    if w2ExLezSeen == True:
        scene w3_7061 with dissolve
        mc "You and Harper seem like friends."
        scene w3_7115 with dissolve
        lucy "That--"

    scene w3_7116 with dissolve
    if kat_polite == True:
        mc "How long does Mrs. Pulman have you on the hook?"
    else:
        mc "How long does Kathleen have you on the hook?"

    scene w3_7115 with dissolve
    lucy "A y-year..."
    scene w3_7117 with dissolve
    mc "Pfweeeeew!"
    "I whistled in fake amazement, like a tried and true {b}prick.{/b}"
    scene w3_7107 with dissolve
    mc "Long enough for the end to be in sight, but still a... {i}crushing{/i} time-frame."
    scene w3_7108 with dissolve
    "...then I waited, letting the implication hang in the air, unspoken."
    scene w3_7107 with dissolve
    mc "I'm good at keeping secrets, and I have a completely unwarranted amount of pull at the club."
    scene w3_7105 with dissolve
    mct "(Big head, big head, big head...)"
    scene w3_7107 with dissolve
    mc "See what I'm saying? I think we should be friends."
    scene w3_7106 with dissolve
    lucy "...friends, huh?"
    scene w3_7072 with dissolve
    "Lucy's focus retreated elsewhere as she mulled over the size, shape, and specifications of that tenuous word."
    scene w3_7107 with dissolve

    if w2ExLezSeen == True:
        mc "Do you think you'll last a year with just the one?"
    else:
        mc "Do you think you'll last a year without making any?"

    scene w3_7118 with dissolve
    "Her expression narrowed and I could tell the first thing that came to mind was a strong \"yes\", but she curiously refrained from voicing her willful inclination."
    scene w3_7106 with dissolve
    lucy "I don't... uh..."
    scene w3_7105 with dissolve
    "...because ultimately, Lucy was a pragmatic woman who had recklessly embraced a transactional world."
    scene w3_7064 with dissolve
    lucy "*Sigh* This is...!"
    scene w3_7065 with dissolve
    "Yet, for the first time since this conversation started, outwardly frustrated, she let a sliver of personality infect her words."
    scene w3_7066 with dissolve
    lucy "This is all SO damn EXTRA."
    scene w3_7065 with dissolve
    "I could use that as an opening, or..."

    menu:
        "Appeal to her pragmatism and use the mention of her son to give her a push.":
            scene w3_7121 with dissolve
            mc "I admire your pragmatism, Lucy. {b}I really do.{/b}"
            scene w3_7120 with dissolve
            mc "Despite your son - and stop me if I'm wrong here - despite him being shortsighted and ungrateful..."
            scene w3_7119 with dissolve
            "She didn't stop me."
            scene w3_7121 with dissolve
            mc "Despite being a brat..."
            scene w3_7119 with dissolve
            "Again, she didn't seem to disagree with my wild assessment."
            scene w3_7061 with dissolve
            mc "Despite that, like a good mother, you seized an opportunity to provide the best for him. I respect that, and I think you'll find that I'm the only person at the club who does."
            scene w3_7063 with dissolve
            mct "(God, I'm so painfully transparent...)"
            scene w3_7062 with dissolve
            mc "All I'm hoping for is that the sympathy can go both ways. I'm in the dark here. I'm just trying to figure out if I'm being messed with tonight."
            scene w3_7124 with dissolve
            lucy "That... uh..."

            if w3LucyPressure >= 4 or w3LucyAffability >=4:
                scene w3_7126 with dissolve
                lucy "{b}You{/b} are not being messed with..."
                scene w3_7125 with dissolve
                mc "No...?"
                jump w3LucyQPQSuccess
        "Pull the teacher close and remind her of the type of transaction she's dealing in. (w3LucyGrope = True)"(chg=["tough_up"]):
            $ w3LucyGrope = True
            $ toughness += 1
            stop music fadeout 3.0
            jump w3LucyGrabby
        "Change track. Encourage her to unload her frustrations.":
            scene w3_7120 with dissolve
            mc "Hey, you can vent if you want. I get it."
            scene w3_7121 with dissolve
            mc "You're in over your head and wondering if this is all worth it."
            scene w3_7122 with dissolve
            lucy "You don't need to tell me how I feel."
            scene w3_7120 with dissolve
            mc "Then how about {i}you{/i} tell me how {b}you{/b} feel?"
            scene w3_7066 with dissolve
            lucy "I feel--"
            scene w3_7125 with dissolve
            "She started, but stopped. Restraint prevailing."
            scene w3_7124 with dissolve
            lucy "...d-did Mrs. Pulman put you up to this?"
            scene w3_7123 with dissolve
            "That admission was something of a confirmation of its own, but..."
            scene w3_7116 with dissolve
            mc "I wouldn't put it past her, but no. I'm seriously in the dark."
            scene w3_7061 with dissolve
            mc "For all I know, she's using you to keep tabs on me. Do you understand why I'm being hard-nosed about this? As two people under her thumb, we should... {i}really{/i} help each other out."
            scene w3_7062 with dissolve
            mc "{b}Friends{/b}."
            scene w3_7063 with dissolve
            lucy "......"

            if w3LucyPressure >= 4 or  w3LucyAffability >=4:
                $ w3FeliciaKatCall = True
                scene w3_7068 with dissolve
                lucy "*Sigh* ...having sex is one thing, but Mrs. Pulman's OTHER demands... I'm not equipped for this kind of thing. I'm a straightforward woman. "
                lucy "That's why I was okay with the club's arrangement. It seemed simple. {b}Mostly{/b}."
                scene w3_7069 with dissolve
                lucy "I mean, I know I'm in over my head, but that's life. However, I signed up for dumb rutting, not to act out a fourth-rate John le Carré novel!"
                scene w3_7121 with dissolve
                mc "And what's the plot of that novel, Lucy?"
                scene w3_7073 with dissolve
                lucy "That--"
                jump w3LucyQPQSuccess
            else:
                jump w3LucyQPQFailure


label w3LucyQPQSuccess:
    scene w3_7106 with dissolve
    lucy "...I was told to confirm whether or not Mrs. Ford was here tonight, and then let Mrs. Pulman know."
    scene w3_7107 with dissolve
    mc "Does she know?"
    scene w3_7106 with dissolve
    lucy "That was her talking to Mr. Waylon. She's the one who had me suggest coming here tonight to him."
    scene w3_7107 with dissolve
    mc "So, he wasn't here specifically for Felicia?"
    scene w3_7106 with dissolve
    lucy "No... he was genuinely surprised to discover she was here."
    scene w3_7107 with dissolve
    mc "You wouldn't have any inkling why Mrs. Pulman wanted to know if Felicia was here tonight, would you?"
    scene w3_7106 with dissolve
    lucy "No, but it seems she didn't expect you to be with her. When she heard that, she told me to report on you too... just how you're behaving, what you were doing..."
    scene w3_7109 with dissolve
    lucy "S-sorry. She told me to keep tight-lipped with Mr. Waylon, and well... anyone else... she was emphatic about it."
    mc "Don't worry about it. Actually, do what she expects. Let her know I browbeat you, okay?"
    scene w3_7106 with dissolve
    lucy "You want me to tell her I spilled my--"
    scene w3_7107 with dissolve
    mc "Leave that part out. Just mention to her I pestered you, and pretty much guessed."
    scene w3_7110 with dissolve
    lucy "A-alright..."
    scene w3_7116 with dissolve
    mc "Thanks for indulging my curiosity."
    scene w3_7115 with dissolve
    lucy "Y-yeah..."
    scene w3_7116 with dissolve
    mc "If you ever have a problem, come to me and we'll see what I can do."
    scene w3_7115 with dissolve
    lucy "Like what?"
    scene w3_7116 with dissolve
    mc "I dunno. We've both been at the club the same amount of time, but I think I might be able to help you get around certain things..."
    scene w3_7110 with dissolve
    lucy "...with your unwarranted sway?"
    scene w3_7107 with dissolve
    mc "Who knows, but I'm saying I won't forget you filling me in about this."
    scene w3_7111 with dissolve
    lucy "...alright."
    mc "Have a good night, for real this time - and good luck."
    lucy "I can go...?"
    scene w3_7112 with dissolve
    "I nodded, as if it was up to me to give her permission."
    lucy "T-thanks... uh... you too."
    scene black with fade
    stop music fadeout 3.0
    $ history_lucy = "I got Lucy to confess that she was spying on Felicia for club business. No surprise there, but it's good to get confirmation."
    $ unread_lucy = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    lucy "Have a good night as well."
    "And that was that. A lot of effort circling the drain and I still don't know what's fully going on, but it's something - plus I felt like I won Lucy over somewhat."
    mct "(Not too shabby...)"
    "Besides, if Lucy tells Kat what I asked her to...."
    jump w3FeliciaKathleenCall

label w3LucyQPQFailure:
    scene w3_7126 with dissolve
    lucy "...I should get back to Mr. Waylon."
    scene w3_7125 with dissolve
    "It seems I was unconvincing."
    mc "It's not like I can't keep you here."
    scene w3_7110 with dissolve
    lucy "...no?"
    scene w3_7107 with dissolve
    mc "It's a free country."
    scene w3_7108 with dissolve
    lucy "......"
    lucy "..."
    scene w3_7107 with dissolve
    mc "Have a good night, Lucy."
    scene w3_7114 with dissolve
    lucy "Uh, you... you too."
    scene w3_7113 with dissolve
    "That could've gone better, if I played my cards right."
    scene black with fade
    stop music fadeout 3.0
    $ history_lucy = "I have only my gut feeling in the negative that running into Lucy at the art exhibition {i}wasn't{/i} a coincidence."
    $ unread_lucy = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "......"
    "..."
    jump w3FeliciaDeniseEnding

label w3LucyGrabby:
    scene w3_7144 with dissolve
    mc "Extra, yeah..."
    "Maybe I suddenly recalled all the rich bitch mothers I endured during my tenure as a tutor..."
    lucy "W-what are you..."
    play music "music/leaving-home.ogg"
    scene w3_7145 with dissolve
    "Maybe it's because her motivations were in the same breath familiar and enigmatic to me."
    scene w3_7146 with dissolve
    mc "It's a lot to take in."
    scene w3_7147 with dissolve
    lucy "I--"
    scene w3_7145 with dissolve

    if w1GonzoReward == True:
        "But ultimately, I was emboldened by her position as a whore and our past physical intimacy."
    else:
        "But ultimately, I was emboldened by her status as a whore."

    scene w3_7148 with dissolve
    mc "The old woman likes to jerk me around too..."
    "Contrary to the comforting affectation in my voice, as a sickness took hold in my gut, I placed a hand on Lucy's thigh."
    scene w3_7149 with dissolve
    "Never in my life would I have expected to be this skeezy, but it again came so effortlessly."
    scene w3_7150 with dissolve
    lucy "...s-she does?"
    scene w3_7149 with dissolve
    mct "(You simply can't take stock of a man's character if he lives in an immutable bubble...)"
    scene w3_7151 with dissolve
    mc "All the time. I think she likes to fuck with everyone. Is she giving you a hard time, tonight?"
    scene w3_7152 with dissolve
    "She didn't answer, clearly preoccupied with the hand creeping up her thigh."
    scene w3_7153 with dissolve
    mc "Worried about Mr. Waylon?"
    scene w3_7154 with dissolve
    lucy "I'm worried about everyone's attention!"
    scene w3_7153 with dissolve
    mc "No one's looking..."
    scene w3_7154 with dissolve
    lucy "You don't know that... your eyes are glued to my chest..."
    scene w3_7152 with dissolve
    mct "(Well, she has a point there...)"
    scene w3_7155 with dissolve
    mc "No one's looking."
    scene w3_7154 with dissolve
    lucy "...not yet."
    scene w3_7153 with dissolve
    mc "...Is that the only aspect of this you're concerned about? Not that I'm touching you, not that you're being touched, but... {i}that someone might see me touching you?{/i}"
    scene w3_7154 with dissolve
    lucy "It's... {i}the top of the list.{/i}"
    scene w3_7155 with dissolve
    mc "Makes sense."
    scene w3_7156 with dissolve
    lucy "Do-"
    "As I grew bold and terrible, my fingers sank into Lucy's fleshy chest and still no one was paying attention to us."
    lucy "...d-does it? Why don't you explain it to me then, because I don't get it? Why am I not telling you to fuck off right now?"
    scene fa_lucyrub1_a with dissolve
    show fa_lucyrub1 with dissolve
    lucy "A-ahh..!"
    mc "Well, you sold your pussy for an entire year to a group of rich assholes just so you could get your son into a \"good\" school."
    mc "That being your driving motivation, {b}I do not doubt{/b}, but it is a decision that arrives by having a few screws loose.."
    mc "I just wonder... is it overwhelming vanity? Do you have a warped sense of values? Or, perhaps..."
    "I trailed off, watching Lucy's face closely for signs of anticipation, and when she finally asked--"
    lucy "Or perhaps w-what?"
    mc "Do you possibly find this {i}acceptable{/i} on some level? Exciting, even?"
    scene w3_7157 with dissolve
    lucy "Don't be ridiculous. You think I enjoy being ogled and molested by that lumpy sack of shit, Isaak?"
    scene w3_7158 with dissolve
    "Before her very mouth, her glare refuted my words."
    scene w3_7159 with dissolve
    mc "Well, maybe I'm off base..."
    "Slowly, in a heavy and hot tone, I spoke directly to Lucy's brain."
    scene w3_7160 with dissolve
    mc "The thing is, I've tutored brats with mothers like you."
    scene fa_lucyrub2_a with dissolve
    show fa_lucyrub2 with dissolve
    lucy "W-whhaa...♥"
    mc "You don't lack self-esteem - at least, not outwardly."
    lucy "Hnnn, uhh...."
    mc "Your children are an extension of yourself, so debasing yourself for their sake would be cutting off your nose to spite your face."
    mc "The only way I can understand it is if you don't see this as debasing yourself. Instead, maybe it's... {i}an excuse?{/i}"
    lucy "I've w-worked hard--"

    if toughness >= 20:
        mc "Have you, you little slut?"
    else:
        mc "Have you, beautiful?"

    "I cut her off, in an attempt to deprive her of any conversational footing."
    mc "I'm not judging you. I can see it being cathartic..."
    mc "Giving up control..."
    lucy "Ahh... ohh...♥"
    mc "Playing the motherly martyr, and all the while..."
    lucy "That--"
    mc "...getting a taste of a more sordid life outside your private schools and gated communities."
    lucy "You are--"
    mc "I'm wrong? Like I said, I could be off base here."
    lucy "H-huhhh... you are... y-you're wrong..."
    mc "{b}Personally{/i}, I think you're bored and unfulfilled."
    lucy "E-eeuuuah..."
    mc "Personally, I think all that shit in your daily life you sold your soul for isn't cutting it, and that has slowly been sinking in."
    lucy "Y-you're wrong... I--"
    mc "Well, maybe I'm projecting. Tell me to stop and I will."
    lucy "Hnnn... ahh..."
    "I waited a moment, but no \"stop\" came from her lips."
    mc "A year is a long time, Lucy. {b}We should be friends.{/b}"
    mc "Friends tell each other stuff. Friends don't go on to blather to the boss what they've been told."
    mc "And if there's ever any hiccups, which there just has to be over the course of a year, they have each other's backs."
    lucy "H-harper's speech was more convincing..."

    if w2ExLezSeen == True:
        scene w3_7161 with dissolve
        mct "(What does Harper have to do with...? Ah, no matter.)"

    scene w3_7162 with dissolve
    mc "...but is mine convincing enough?"
    scene w3_7161 with dissolve
    lucy "........."
    lucy "......"

    if w3LucyPressure >= 4:
        scene w3_7163 with dissolve
        lucy "...I was told to confirm whether or not Mrs. Ford was here tonight, and then let Mrs. Pulman know."
        scene w3_7164 with dissolve
        mc "'atta, girl - and does the old woman know?"
        scene w3_7166 with dissolve
        lucy "...t-that was her talking to Mr. Waylon."
        scene w3_7167 with dissolve
        mc "Is he also confirming?"
        scene w3_7163 with dissolve
        lucy "N-no... he's in the dark. Mrs. Pulman had me suggest coming tonight. He was surprised to discover she was here."
        scene w3_7164 with dissolve
        mc "You wouldn't have any inkling why Mrs. Pulman wanted to know if Felicia was here tonight, would you?"
        scene w3_7163 with dissolve
        lucy "No, but it seems she didn't expect you to be with her either. When she heard that, she told me to report on you too... just how you're behaving, what you were doing..."
        scene w3_7166 with dissolve
        lucy "S-sorry. She told me to keep tight-lipped with Mr. Waylon, and well... anyone else... she was emphatic about it."
        scene w3_7167 with dissolve
        mc "That's alright. In fact, tell her I came up to you and pretty much figured it out."
        mc "Don't tell her that you blathered, understand?"
        scene w3_7166 with dissolve
        lucy "Y-yes, sir."
        scene w3_7165 with dissolve
        $ history_lucy = "After getting hands on, I got Lucy to admit that our meeting during Felicia's date {i}wasn't{/i} a coincidence. The old woman has plans."
        $ unread_lucy = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve
        "Lucy had changed her tone somewhat, having accepted my purported influence, and falling into obedience mode."
        "Her puppy dog eyes agitated something in me."
        "It filled me with the desire to poke and prod, and to do something {b}stupid{/b}."

        menu w3LucyGropeMenu:
            "Ignore it. Dismiss her and wait for Felicia.":
                scene w3_7167 with dissolve
                mc "If you ever have a problem, come to me and we'll see what I can do."
                scene w3_7163 with dissolve
                lucy "...don't think I won't."
                scene w3_7164 with dissolve
                mc "I know you will. Have a good night, Lucy."
                scene black with fade
                "And that was that. A lot of effort circling the drain, while letting out a side of me I was coming around to liking, and I still don't know what's fully going on, but... I got {i}something.{/i} "
                mct "(Not too shabby...)"
                "Besides, if Lucy tells Kat what I asked her to...."
                jump w3FeliciaKathleenCall


            "{color=#FF1493}[[Mischievous]{/color} Push it even further. (w3LucySupergrope = True)" if toughness >=15:
                jump w3LucyFeverishRub

            "{color=#696969}[[Mischievous] Push it even further. {/color}" if toughness <=14:
                jump w3LucyGropeMenu
    else:
        scene w3_7168 with dissolve
        lucy "...no. It's not. Not in this case."
        mc "...can't say I didn't try."
        scene w3_7169 with dissolve
        lucy "Mrs. Pulman told me to keep my mouth shut about this bullshit she has me doing. I'll give you that much, but if you truly relate, you can understand what that means."
        lucy "I'd rather not piss her off."
        scene w3_7171 with dissolve
        mc "It doesn't have to get back to--"
        scene w3_7169 with dissolve
        lucy "Not risking it."
        scene w3_7170 with dissolve
        "She has had enough and this time she was firm."
        scene w3_7171 with dissolve
        mc "Alright, I do sympathize."
        scene w3_7172 with dissolve
        mc "Sorry for taking up your time."
        scene w3_7170 with dissolve
        lucy "......"
        scene black with fade
        lucy "...I sympathize too."
        "At least I concretely know the old woman is working an angle tonight. I would have to subsist entirely on that information."
        jump w3FeliciaDeniseEnding


label w3LucyFeverishRub:
    $ w3LucySupergrope = True
    scene w3_7174 with dissolve
    "Truly, I had lost my mind."
    lucy "What are you--"
    scene fa_lucyrub3_a with dissolve
    show fa_lucyrub3 with dissolve
    mc "Thanks for being honest with me."
    lucy "O-oh..!"
    mc "If you ever have a problem, come to me."
    lucy "Y-yeah... you-- euughh.."
    mc "We'll see what I can do."
    mct "(What had come over me?)"
    lucy "{b}Wwhha, h-haaa...!!{/b} S-someone might s-see..."

    if toughness >=22:
        mc "...but best keep it down then, you filthy bitch."
    else:
        mc "...but best keep it down then."

    lucy "*Gulp* Hnnngg..."
    "When I first grabbed her, I thought I had a plan."
    "I thought I could squeeze some info out of her - or some {b}nonsense{/b} like that."
    lucy "Hnnn...♥"
    "...but, in turn, I was just priming my urges and flaunting a position that had fallen in my lap."
    mct "({b}This is fucking insane.{/b})"
    "Whatever bullshit that was rattling around in my head, that blew past my filter and exposed my ugliness to the teacher, temporarily left me as I kept a firm eye on what was in front of us."
    mct "(If we got caught, kicked out, or even had the police called on us...)"
    "One, there was no explaining this to Felicia - hell, there was no explaining it to myself, because {b}two{/}..."
    "This would look AWFUL to a medical board. For as silly and stupid as I thought Lucy's motivations were, I was equally susceptible to the same folly."
    "Yet, Lucy was too good of a morsel. So, lips sealed and eyes peeled, I fervently rubbed at the growing need between Lucy's thighs as if I was trying to erase it from existence."
    lucy "Haa...."
    "...riding high on a feeling of control over this woman."
    scene fa_lucyrub4_a with dissolve
    show fa_lucyrub4 with dissolve
    lucy "......"
    lucy "..."
    "Lucy, likewise, tried to endure quietly, a deeply scarlet blush revealing itself through the fingers on her covered face."
    mc "Should I stop...?"
    "I don't know if I was asking for my sake or hers, but..."
    lucy "*Gulp.* Ahhhee..."
    "...her answer, as I had instinctually known would be the case, didn't come at all."
    mct "(Fuckin' A...)"
    "Her response came from the slight way her hips moved, running counter to my palm, in a paltry bid to enhance her pitiful pleasure."
    mct "(Oh, I've got your number, Luce...)"
    lucy "H-haa...♥ T-this... t-this... this is c-crazy..."

    if toughness >=25:
        mc "You fucking love it, cunt..."
    else:
        mc "You're lovin' it..."

    lucy "Eh, hhaa...♥"

    "So I just rubbed."
    "Rubbed."
    "Rubbed, rubbed, rubbed."
    "Not long - not long at all, really..."
    "...but--"
    scene fa_lucyrub5_a with dissolve
    show fa_lucyrub5 with dissolve
    lucy "--!"
    "............"
    "........."
    "......"
    scene w3_7175 with dissolve
    "The madness was blissfully concluded when I felt her thighs release my hand and the strength leave Lucy's legs."
    "A completely vacant look clouded over Lucy's face, and for a few mere seconds, a brief respite for the night's anxiety."
    scene w3_7176 with dissolve
    "No longer worried about getting caught, I was transfixed by the English teacher's dull expression for an equally brief amount of time."
    "......"
    "..."
    "She didn't even acknowledge her own climax."
    scene w3_7177 with dissolve
    lucy "I should get back to Mr. Waylon..."
    scene w3_7178 with dissolve

    if not persistent.w3LucyQPQ:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3LucyQPQ = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

    mct "(Fuck, that's hot.)"

    menu w3LucySpitMenu:

        "{color=#FF1493}[[Asshole]{/color} Send her on her way with a little bit of yourself." if toughness >=25:
            "I had been staring at her sumptuous tits all night, wanting to see them messed up and soiled."
            "An impossibility, given the situation, but..."
            play sound "sound effects/spit.wav"
            scene w3_7179 with dissolve
            mc "*spit*"
            scene w3_7180 with dissolve
            mc "Get the fuck out of here."
            scene w3_7181 with dissolve
            "{b}A consolation{/b}, and one last sadistic flourish as I took gratification in watching a big glob of spit eek into the magnificent valley below."
            play sound "sound effects/slap4.wav"
            scene w3_7182 with dissolve
            scene w3_7183 with hpunch
            mc "Get!"
            stop music fadeout 3.0
            scene black with fade
            mct "(God it feels good to be a prick...)"
            $ renpy.end_replay()
            "......"
            "..."
            jump w3FeliciaKathleenCall
        "Ignore it. Dismiss her and wait for Felicia.":

            scene w3_7184 with dissolve
            mc "If you ever have a problem, come to me and we'll see what I can do."
            scene w3_7185 with dissolve
            lucy "...don't think I won't."
            scene w3_7184 with dissolve
            mc "I know you will. Have a good night, Lucy."
            stop music fadeout 3.0
            scene black with fade
            "And that was that. A lot of effort circling the drain, while letting out a side of me I was coming around to liking, and I still don't know what's fully going on, but... I got {i}something.{/i} "
            mct "(Not too shabby...)"
            $ renpy.end_replay()
            "Besides, if Lucy tells Kat what I asked her to...."
            jump w3FeliciaKathleenCall


        "{color=#696969}[[Mischievous]Send her on her way with a little bit of yourself.{/color}" if toughness <=24:
            jump w3LucySpitMenu


label w3FeliciaKathleenCall:
    $ w3KathleenFeliciaReveal = True
    stop music fadeout 3.0
    play ambient "sound effects/ringing-inbound.wav"
    "*Ring, ring~*"
    "Right on cue..."
    stop ambient
    play sound "music/Moonlight-Sonata.ogg"
    scene w3_7018 with circlewipe
    show screen textbox2 with dissolve
    kat "Mr. [mcl]. You could've saved me a whole lot of trouble!"
    scene w3_7019 with dissolve
    mc "Sorry I pried so hard."
    scene w3_7018 with dissolve
    kat "Oh, no need! I wasn't keeping it a secret from you. I had no idea Mrs. Ford was comfortable enough with you to invite you to social outings. God, that woman is outrageous!"
    scene w3_7019 with dissolve
    mc "So, what's going on tonight?"
    scene w3_7021 with dissolve
    kat "I wanted to learn just how much this particular artist meant to Mrs. Ford, that's all - and, with that affirmative, acquire some {i}material{/i} for this weekend."
    scene w3_7020 with dissolve
    mc "You're buying a painting?"
    scene w3_7021 with dissolve
    kat "Eric is. He {i}has{/i} been looking to invest."
    scene w3_7020 with dissolve
    mct "(Ah, crap...)"
    mc "Why did you keep Mr. Waylon in the dark?"
    "I don't think Felicia will appreciate the club getting its mitts on one of her beloved artist's works."
    scene w3_7022 with dissolve
    kat "Oh! You weaseled that out of Lucy, did you?"
    scene w3_7020 with dissolve
    mc "..."
    scene w3_7021 with dissolve
    kat "It kept the ostentation to the minimum. I suspected he'd be more giddy and {i}pointed{/i} if assigned the role of hunting dog."
    scene w3_7022 with dissolve
    kat "Felicia's a shrewd girl and he'd tip the hand. If I knew YOU had an in, you could've saved me two degrees of delegation."
    scene w3_7021 with dissolve
    kat "I'll tell you this: I'm very impressed, not only by your ability to ingratiate yourself with the Carnations, but also your shrewdness. However, it goes without saying..."
    scene w3_7023 with dissolve
    kat "Mum's the word; Felicia shouldn't know about this. It'd ruin the surprise."
    scene w3_7024 with dissolve
    mc "...surprise, got it."
    mc "How... fun."
    scene w3_7025 with dissolve
    kat "How fun, indeed! Now!"
    kat "I should go. I've got a roast in the oven."
    scene w3_7024 with dissolve
    mc "...do you really?"
    scene w3_7026 with dissolve
    kat "[mcf]... what a dreadful insinuation."
    scene w3_7028 with dissolve

    if kat_polite == True:
        mc "Have a nice night, Mrs. Pulman."
    else:
        mc "Have a nice night, boss."

    scene w3_7027 with dissolve
    kat "Tata~"
    play sound "sound effects/phonemenu.wav"
    stop music
    scene w3_7029 with dissolve
    mct "(Sheesh, she sounded exceedingly jubilant during that whole call.)"
    "......"
    "..."
    "I don't know how I felt about that, it would probably be better if I didn't know."
    scene black with fade
    "I wouldn't have the irony hanging over my head, at least."
    jump w3FeliciaDeniseEnding

label w3FeliciaDeniseEnding:
    play music "music/a-nice-dream.ogg"
    scene w3_7127 with circlewipe
    denise "Oh, dear. I've barely given you a chance to speak."
    fel "That's alright. I love hearing you talk about your interests."
    denise "...heh. When you put it that way, I'm even more embarrassed."
    scene w3_7128 with dissolve
    fel "I while away the days, on stuff not worth mentioning."
    denise "I doubt that... the not worth mentioning part, I mean."
    scene w3_7129 with dissolve
    fel "I don't know. I used to feel more involved, but a lot of it has become dull recently."
    fel "I... occasionally try my hand at painting."
    scene w3_7130 with dissolve
    denise "Really?! That makes sense, since you're-"
    scene w3_7131 with dissolve
    fel "It's for fun."
    scene w3_7132 with dissolve
    denise "......"
    scene w3_7133 with dissolve
    denise "...I've found no better stress reliever."
    scene w3_7134 with dissolve
    denise "Of course, sometimes I find painting to be the source of that stress, but when it pops..."
    denise "Pow! What a relief! Heh..."
    scene w3_7135 with dissolve
    denise "Sorry for getting excited."
    fel "You remind me of another friend of mine who also excessively apologizes."
    scene w3_7136 with dissolve
    denise "...the one you're with tonight?"
    scene w3_7137 with dissolve
    fel "No. Not him."
    scene w3_7138 with dissolve
    fel "The one in question is more blonde."
    denise "Heheh... are you callin' me blonde?"
    scene w3_7139 with dissolve
    denise "I'm not usually like this. It's just..."
    denise "It's gratifying to know there's someone out there who appreciates the \"doing\" side of the craft."
    scene w3_7141 with dissolve
    fel "Oh, come on. You have other fans."
    scene w3_7140 with dissolve
    denise "I get a lot of {i}you're so brave{/i} and {i}your perseverance is...{/i}"
    scene w3_7139 with dissolve
    denise "I know they mean well, but it's nice to know someone sees past that."
    denise "So, what I'm trying to say is..."
    scene w3_7142 with dissolve
    denise "Please come to the next one. I-if there is a next one that--"
    fel "I won't fucking miss it."
    scene w3_7143 with dissolve
    denise "Uh... Raymond looks like he just witnessed a miracle."
    scene black with fade
    "......"
    "..."
    jump w3ArtExhibitionOutro

label w3ArtExhibitionOutro:
    $ date = "june17day"
    play music "music/ocean-view.ogg"
    hide screen textbox2
    scene fa_drive1_a with w19
    show fa_drive1 with dissolve
    "After wrapping up at the exhibition, the sun had fallen past the city's edge and the night was full of promise."
    show june17night with squares

    if w3FeliciaDeniseConvinced == True:
        fel "She's so much shorter than I thought she'd be."
        "As we blasted past mile marker after mile marker, Felicia was over the moon, inundating me with her time with Denise."
        scene fa_drive2_a with dissolve
        show fa_drive2 with dissolve
        mc "Huh? Is there something about her art that made you think she was tall?"
        "Inwardly, I marveled at how a brief interaction had rendered the demure Felicia into a blathering, over-excited schoolgirl."
        fel "I don't know I just figured--"
        "For a woman with as many facets as Felicia, finding yet another side of her made me crack a smile."
        mct "(She's cute...)"
        fel "Anyway, and then we went for a walk."
        scene fa_drive1_a with dissolve
        show fa_drive1 with dissolve

        if w3KathleenFeliciaReveal == True:
            "And while she explained {b}everything{/b} to me, teeming with earnest, the call with Kathleen sat in the corner of my mind, taking a fat shit."
            "Part of me wanted to give Felicia a heads up, to tell her that Mrs. Pulman had come into possession of one of her idol's esteemed works, for what was surely an unsavory purpose."
            "Yet, she was explicit regarding my silence and I truly believed that her well-honed sadistic senses would see through any faux-surprise on Felicia's part..."
            "...and honestly would spilling the beans even lessen the blow? Would it even be a big deal to Felicia?"
            "My gut says yes, but then again, {b}her girl got paid.{/}"
            mct "(I could see her looking at it like that...)"

        elif w3LucyConfront == True:
            "So, I sat quietly, engaged with Felicia's tale and watching whole stretches of road disappear."
            "I was slightly concerned that whatever the old woman was up to tonight would mar this memory, but that was a future concern."
            "That was what I told myself."
        else:

            "So, I sat quietly, engaged with Felicia's tale and watching whole stretches of road disappear."
            "At the back of my mind, there was Eric and Lucy, but..."
            "It was none of my business. At least, not yet."
            "And if it had anything to do with Felicia or the club..."
            mct "(...this is what she signed up for?)"
            "That was what I told myself."


        scene fa_drive3_a with dissolve
        show fa_drive3 with dissolve
        "Minutes passed, and then maybe a dozen. She ventured enthusiastically into the fine details of what I knew nothing about, explaining some of the signature characteristics of Denise's works and harping on things like texture, form, and space."
        mc "You should be an art critic."
        fel "Shut up!"
        "Minutes turned into a dozen, and after she had run out of things to talk about, a silence fell over the car..."
        scene fa_drive3b_a with dissolve
        show fa_drive3b with dissolve
        "So casual, yet perhaps the single most intimate moment I had ever shared with Felicia - {i}and I have been inside her!{/i}"
        fel "......"
        "A simple, human gesture."
        fel "..."
        "An affectionate, platonic sentiment removed from the club paradigm, extended as naturally as breathing."
        "I hadn't done anything, {b}nothing at all{/b}, but I suppose my mere presence had been of use to the feisty blonde."
    else:

        fel "You sure you don't want to drive?"
        "As we put each mile marker behind us, Felicia and I made small talk."
        mc "Yeah, I'm sure..."
        scene fa_drive2_a with dissolve
        show fa_drive2 with dissolve
        "Undoubtedly in a bid to upend the evening's pissy conclusion."
        fel "You'd be a lot cooler if you drove. A man should drive, y'know?"
        mc "Thank you for your professional opinion."

        if w3ActuallyBlackmail == True:
            "At the very least, we probably spared her girl a bad review. That was a little something."

        "Nevertheless, Felicia looked her usual self. In control, and building a certain sultry vibe that she had kept to a minimum during \"business\" hours."
        fel "Seriously. It's not like I'd tell on you."
        fel "I'll pull over and we can swap."
        "Ever so often, she'd send an obvious glance my way or shift in a way to tell me something was brewing inside her skull."
        mc "Yeah, and if I swiped a parked car, what would you do?"
        fel "Well, I'd suggest not crashing into things?"
        mc "Brilliant."
        mc "Do I need to remind you that you're the would-be sugar mama here?"
        scene fa_drive3_a with dissolve
        show fa_drive3 with dissolve

        if w3FeliciaPlatonic == True:
            "Not that any of those looks mattered. My body was off limits tonight, right?"
            fel "Mama likes a man who's in control."
            "{/i}...right?{/i}"
        else:
            fel "Mama likes a man who's in control."

        "And while the conversation briefly receded, and the pavement hypnotized my wandering mind, a nagging feeling seized me."

        if w3LucyConfront == True:
            "What was the old woman up to tonight? It had to be about something."
            "If not me, then Felicia, but..."
            "If I needed to know, I'd need to know..."
            "That was what I told myself at least."
        else:

            "Eric and Lucy."
            "Whatever that was, it was none of my business. At least, not yet."
            "And if it had anything to do with Felicia or the club..."
            mct "(...this is what she signed up for?)"
            "That was what I told myself."

    scene fa_drive2_a with dissolve
    show fa_drive2 with dissolve
    "......"
    "..."
    mc "So... where to next? What are you in the mood for?"
    fel "Uh... how about sex on the beach?"
    mc "I mean food-wise."
    fel "You have any suggestions?"
    mc "It's your evening. I'm down for {b}whatever{/b}."
    scene fa_drive1_a with dissolve
    show fa_drive1 with dissolve
    fel "Don't put it all on me, stud. It's {i}our{/i} evening."
    mc "Well... uh... we're dressed for something fffah--?"
    fel "{b}PASS{/b} on fancy. Nothing stuffy, nothing where the waiter is checking to see if there's a hair out of place on my bleached asshole - not in the mood."
    mc "Okay, okay... no culinary-related colon inspections. Something light, then?"
    fel "Something {i}satisfying.{/i}"
    mc "...a big fucking burger, then?"
    fel "........."
    fel "......"
    fel "...a {b}big{/b} fucking burger it is."
    scene fa_drive3_a with dissolve
    show fa_drive3 with dissolve

    if w3RosalindMassaged == True:
        "...and thanks to Rosalind--"
        mc "I happen to know a good place."
    else:
        mc "Know any good places?"
        fel "In this city? About half a dozen."
        "..."

    fel "It's locked in. No changing our minds."
    fel "Points for settling that quickly."
    mc "...and how am I scoring, overall?"

    if w3FeliciaDeniseConvinced == True:
        fel "Well..."
        "For a flickering moment, Felicia's eyes wandered off the road and over to me."
        fel "You pushed me out of my comfort zone tonight. Otherwise I wouldn't have--"
        fel "I mean, y-yeah... you're scoring {b}high.{/b}"
        "I caught something lingering in them, before Felicia's eyes closed back in on the road."

        if w3ActuallyBlackmail == True:
            fel "Plus, you blackmailed a woman for my sake tonight. That's something too."
            mc "I... just suggested she play nice. I hate bullies."
            fel "Uh, huh... sure you do..."
            mc "Come on, and what are you implying?"
            fel "Just that you should be honest with yourself."

    elif w3ActuallyBlackmail == True:
        fel "Well..."
        "For a flickering moment, Felicia's eyes wandered off the road and over to me."
        fel "...you blackmailed a woman for my sake tonight. That's something."
        mc "I... just suggested she play nice. I hate bullies."
        fel "Uh, huh... sure you do..."
        mc "Come on, and what are you implying?"
        fel "Just that you should be honest with yourself."
    else:
        fel "Not bad, but let's see if you stick the landing."

    if w3FeliciaPlatonic == True and w3FeliciaDeniseConvinced == True or w3FeliciaPlatonic == False and w3FeliciaDeniseConvinced == True and w3MinaWantsToWatch == False:
        scene w3_7186 with dissolve
        "And so, Felicia stepped on the gas, yellow missile hurtling through the darkness with us as its payload."
        "We grabbed some burgers, and next stop..."
        jump w3FeliciaRooftopRendezvous

    elif w3FeliciaPlatonic == False and w3MinaWantsToWatch == True:
        scene fa_drive1_a with dissolve
        show fa_drive1 with dissolve
        "........."
        "......"
        fel "...I wonder if Mina's eaten yet."
        mc "You want to invite her to join us...?"
        scene fa_drive2_a with dissolve
        show fa_drive2 with dissolve
        fel "Well, she mentioned the three of us should hang out the other day..."
        "Considering my knowledge of Mina's list, the possibility of this being an opportunity crossed my mind."
        fel "...and I thought it might be... {i}nice{/i} to show her that there are some people out there who listen, remember, and think about her."
        mc "You've got a real soft spot for that girl."
        fel "Don't you? {i}Girls talk you know.{/i}"
        mc "...uh, yeah... I am but made of flesh and blood."
        fel "Anyway, it's okay if you don't want to. You and I have certain {i}bodily{/i} expectations of each other and picking up a third wheel might get in the way of that."

        menu:
            "The more the merrier."(chg=["mina_up2","mina_bi_up"]):
                $ Mina_Affection += 2
                $ Mina_BiCurious += 1
                mc "Sure, yeah. Let's invite her to eat with us."
                fel "Ha! I had a feeling you'd agree!"
                mc "You put it elegantly."
                mct "({i}Two hot blondes{/i}...)"
                scene w3_7186 with dissolve
                "And so, Felicia stepped on the gas, yellow missile hurdling through the darkness with us as its payload."
                "We grabbed some burgers and..."
                scene black with fade
                stop music fadeout 3.0
                "...set course for a night I'd never forget."
                "......"
                "..."
                jump w3FeliciaMinaThrowdownStart
            "You'd really just like to spend some romantic time alone with Felicia tonight."(chg=["felicia_up2","felicia_passion_up"]):

                $ Felicia_Affection += 2
                $ Felicia_Confidence += 1
                mc "Don't get me wrong, knowing what I know about Mina, it's a {b}tempting{/b} prospect, but..."
                "Felicia's gaze wandered back over to me, as if she was genuinely hanging onto that \"but\"..."
                mc "...but I would love to spend some one-on-one time with {i}just{/i} you and get to know you better."
                scene w3_7187 with dissolve
                fel "...s-seriously?"
                scene w3_7188 with dissolve
                mc "I mean I like Mina, but how often are you and I really going to see each other like--"
                scene w3_7189 with dissolve
                fel "{b}Okay.{/b} That's..."
                scene w3_7190 with dissolve
                mc "Stupid?"
                scene w3_7191 with dissolve
                fel "That's all you have to say."
                scene w3_7192 with dissolve
                "......"
                "..."
                scene w3_7186 with dissolve
                "And so, Felicia stepped on the gas, yellow missile hurdling through the darkness with us as its payload."
                "We grabbed the burgers, and--"
                jump w3FeliciaRooftopRendezvous

    elif w3FeliciaPlatonic == True and w3FeliciaDeniseConvinced == False:
        scene w3_7186 with dissolve
        "And so, Felicia stepped on the gas, yellow missile hurdling through the darkness with us as its payload."
        "We grabbed some burgers and--"
        jump w3FeliciaPrematureEnding




label w3FeliciaRooftopRendezvous:
    play music "music/jazz-piano-bar.ogg"
    scene w3_7193 with w19
    show screen textbox2 with dissolve
    fel "Oooh, ho, hoooo... THAT hit the spot."

    if prAfterParty == False:
        "I watched Felicia devour that thing, even more so than on the night we first met."
        scene w3_7194 with dissolve
        fel "...that's a curious expression from {i}my{/i} dour boy. What's bouncing around up there?"
        mc "I'm just recalling the first night we met."
        fel "Oh, yeah?"
        mc "You had a burger then, too."
        scene w3_7193 with dissolve
        fel "Maybe there's something about you that makes women want to fill themselves up with {b}meat{/b}."
        mc "Har har."
    else:
        mc "Enjoying it?"
        scene w3_7194 with dissolve
        fel "Oh, [mcf]. You can't tell when a woman has a satisfied look on her face?"

    scene w3_7196 with dissolve
    mc "I'm not complaining, I actually do prefer this, but I kiiiinda expected you to wine and dine me after you pitched me on this \"date\" and talked about \"taking\" me around."
    scene w3_7195 with dissolve
    fel "I thought about doing that. Showing someone the finer things in life, especially when they're not used to them, DOES sound fun..."
    scene w3_7196 with dissolve
    mc "...but?"
    scene w3_7200 with dissolve
    fel "..but I got to thinking, I would feel less guilty about playing chicken with my aging metabolism if I had someone else pigging out beside me."
    scene w3_7202 with dissolve
    mc "Oh, is that it?"
    scene w3_7197 with dissolve
    fel "It's just that the {i}finer{/i} things in life look different depending on what side of the fence you sit, and what I've learned over the years is what really elevates a night is the quality of the company."
    scene w3_7198 with dissolve
    mc "You're cheesier than you look, Felicia."
    scene w3_7195 with dissolve
    fel "I'm realizing that about myself. You know, every now and then, I recall a date I went on during my heyday."
    scene w3_7197 with dissolve
    fel "The man I spent the evening with was handsome and loaded, but none of that is in my recollection. What {b}sticks{/b} out through the haziness of memory is..."
    fel "...Sebastian was {b}very{/b} funny. A bit of a dick in the typical ways you might expect, but not quite typical."
    scene w3_7199 with dissolve
    "Oh, yeah. I knew what she meant. I *was* in the middle of a crash course of what she meant by {i}typical.{/i}"
    scene w3_7195 with dissolve
    fel "He geeked out about his playing card collection of all things. Not his watch collection, but cheap little cards, and it wasn't in the \"I don't think of you as a person, so I'm just going to listen to myself talk\" way. He was just unabashedly sharing about himself."
    fel "And as vain as I seemed, he still tried to loop my own insipid interests into the conversation - and for that evening, I didn't feel so stupid about them. "
    scene w3_7196 with dissolve
    mc "Is he the one that got away?"
    scene w3_7195 with dissolve
    fel "As if. We weren't compatible at all. I only saw him the once."
    scene w3_7196 with dissolve
    mc "...but?"
    scene w3_7195 with dissolve
    fel "...but here I am mentioning it 12 years later as if it is more noteworthy than any ride on a private jet."
    scene w3_7197 with dissolve
    fel "Actually kinda sad when you think about it, but my point was that the \"finer\" things have their place and {b}this{/b} was the perfect accompaniment to my good mood."
    scene w3_7201 with dissolve
    mc "......"
    stop music fadeout 3.0
    scene w3_7202 with dissolve
    mc "...it was a good burger."
    scene w3_7200 with dissolve
    fel "It was a {b}damn{/b} good burger."
    scene w3_7203 with dissolve
    mc "What now, though? We're cozy, and you're dressed like you're about to spend a night watching movies..."
    mc "I'm assuming we're gonna hang here? What are we going to do?"
    play music "music/ethereal-rest.ogg"
    hide screen textbox2 with dissolve
    scene w3_7204 with dissolve

    if w3FeliciaPlatonic == True:
        fel "Yeah... quite the conundrum. We got cozy and {b}you{/b} have a girlfriend."
        mc "I wasn't suggesting--"
        fel "I know, but it is kinda absurd. Still, I didn't want the night to end prematurely."
        mct "(...that so?)"
    else:
        fel "Oh, I'm sure you'll come up with something."

    scene w3_7205 with dissolve
    mc "...working on anything?"
    fel "Are you asking about the canvases?"
    scene w3_7207 with dissolve
    mc "Yeah. Last time I was here, you had something going."
    scene w3_7206 with dissolve
    fel "I finished it."
    scene w3_7207 with dissolve
    mc "How did it turn out? Were you happy with it?"
    scene w3_7206 with dissolve
    fel "Not really, but I rarely am."
    scene w3_7208 with dissolve
    mc "What do you do with them? You don't throw them out, right?"
    fel "I put them in storage."
    scene w3_7209 with dissolve
    mc "And how many do you have stored? A warehouse worth, I bet."
    fel "Not that many. Since I've gotten married, I only paint a few a year."
    scene w3_7210 with dissolve
    mc "Does it take a lot of energy?"
    scene w3_7211 with dissolve
    fel "Sometimes it's easier than not."
    scene w3_7212 with dissolve
    fel "It's funny. I go months without thinking about this stuff, and even longer talking about it - by design, but today..."
    fel "It's all we've talked about."
    scene w3_7213 with dissolve
    mc "Today was a special occasion. I'm glad I could go with you."
    scene w3_7214 with dissolve
    fel "It's funny. I just wanted to get my weed that day."
    fel "It wouldn't have even occurred to me otherwise to saddle you with the job of playing arm warmer."
    scene w3_7215 with dissolve
    fel "The sugar mama stuff was one hell of a pretense, huh?"
    scene w3_7216 with dissolve
    mc "Wait, it wasn't because of my charms and good looks?"
    scene w3_7217 with dissolve
    fel "If all I wanted was a friend to go with me, I could've just asked Mina..."
    scene w3_7218 with dissolve
    fel "You know, she doesn't even know I used to paint?"
    scene w3_7219 with dissolve
    mc "...really? It's an important side of you; you should share it with her. I can already see it now..."
    scene w3_7220 with dissolve
    mc "{i}That's so cooooooooool{/i}, wow!"
    fel "She'd die if she saw you mock her like that."
    scene w3_7221 with dissolve
    mc "Eh, it's cuter when she does it."
    scene w3_7222 with dissolve
    fel "It's strange. I don't know why I haven't shared that with her..."
    scene w3_7223 with dissolve
    mc "Force of habit from not thinking about it for months, maybe?"
    scene w3_7222 with dissolve
    fel "Maybe."
    scene w3_7224 with dissolve
    "........."
    "......"
    scene w3_7225 with dissolve
    fel "....."
    scene w3_7226 with dissolve
    fel "...straighten out your posture for me, would you?"
    mc "Why--"
    scene w3_7227 with dissolve
    fel "Come on, indulge me!"
    scene w3_7228 with dissolve
    mc "...eheh, like this?"
    fel "Pull your shoulder away from your ears."
    scene w3_7229 with dissolve
    mc "{i}Away{/i} from my ears? How the hell do you do that?"
    fel "About like that."
    scene w3_7230 with dissolve
    "Felicia scrutinized my posture so closely that I was starting to develop a keen feeling of exhibitionism."
    scene w3_7231 with dissolve
    fel "...you're probably not aware of it, but you have {b}remarkable{/b} control over your body language."
    fel "Even when you're uneasy, like the first time you were on the club's stage, you don't really show it."
    scene w3_7232 with dissolve
    mc "...I'll have to take your word for it?"
    scene w3_7233 with dissolve
    fel "Yet, on the whole, you gravitate to body language that puts people at ease. You don't shy away, but you also tend to minimize the space you take up."
    fel "It's an interesting balance; firm and inconspicuous as a rock."
    scene w3_7232 with dissolve
    mc "Is that why you have me standing like this?"
    scene w3_7233 with dissolve
    fel "I just wanted to see what you'd look like as a boulder."
    scene w3_7232 with dissolve
    mc "And?"
    scene w3_7234 with dissolve
    fel "And you don't want to come off as some small dicked alpha-wannabe chode, y'know? And that's a real possibility when you start trying to regulate your subconscious behavior, but..."
    scene w3_7235 with dissolve
    fel "You look attractive with your chest puffed out. I think you should try to project more outward confidence when you stand."
    scene w3_7236 with dissolve
    mc "...why are you so hung up on teaching me how to be the best me tonight?"
    scene w3_7235 with dissolve
    fel "Honestly? It turns me on a little."
    scene w3_7236 with dissolve
    mc "TED talking people turns you on?"
    scene w3_7237 with dissolve
    fel "Some women like projects, but honestly? There's something about having a guiding hand on a man's masculinity that I find..."
    scene w3_7238 with dissolve
    mc "Yeah, okay. I get it. It's like the companion piece to {i}a hot-for-teacher{/i} thing."
    scene w3_7237 with dissolve
    fel "Just saying... certain women appreciate a {b}tacit{/b} reminder that the man they trust could overpower them if he wanted to."
    scene w3_7239 with dissolve
    mc "Is that why they put the pickle jar lids on so tight?"
    scene w3_7240 with dissolve
    fel "...would you mind modeling for me, [mcf]?"
    fel "I haven't had anyone to stand in as a reference in a very long time, and tonight..."
    scene w3_7241 with dissolve
    fel "...tonight is picturesque."
    scene w3_7242 with dissolve
    mc "When did you decide we were going to do this?"
    scene w3_7243 with dissolve
    fel "Earlier tonight at the exhibition. I got an itch."
    scene w3_7244 with dissolve
    mc "You have me completely at your disposal tonight, open to doing whatever you want, and that's what you pick?"
    fel "Please don't say no."
    mc "Well, I'm not very good at standing still--"
    scene w3_7245 with dissolve
    fel "Yeah, okay, it's stupid--"
    mc "...but I'll try."
    scene w3_7246 with dissolve
    fel "Ah-! C-cool... ahem..."
    scene w3_7247 with dissolve
    "......"
    "..."
    scene w3_7248 with dissolve
    fel "Please stand over there. I... want to check the lighting."
    scene w3_7249 with dissolve
    mc "......"
    scene w3_7250 with dissolve
    mc "...what should I do? Do I strike a pose?"
    fel "No, just sit down. Get comfortable."
    fel "I want to capture you at your most natural."
    scene w3_7251 with dissolve
    mc "Alright. Just be sure to get my good side."
    scene black with fade
    "........."
    "......"
    mct "(...that was the part where she was supposed to say \"all you have are good sides\".)"
    scene w3_7252 with dissolve
    mc "...can I ask you something that's been on my mind since last week?"
    scene w3_7253 with dissolve
    fel "Spill it."
    scene w3_7252 with dissolve
    mc "Last time we were here... you told me the club represented an opportunity independent of your husband, yet you clearly know people."
    scene w3_7254 with dissolve
    mc "I even bet those people like you independent of your husband. You don't need the club to make your own money, do you?"
    mc "It doesn't make a lick of sense to me."
    scene w3_7255 with dissolve
    fel "I suspect {i}any{/i} answer I could give you won't satisfy you, but..."
    fel "It's a matter of heuristics..."
    scene w3_7254 with dissolve
    mc "...heuristics? You're kidding?"
    scene w3_7256 with dissolve
    fel "Does it sound better when you dress it up with a fancy word? Or does it sound even more absurd?"
    mc "Yeah, uh... I asked this last time, but how does being a member give you a leg to stand on? Connect the dots for me."
    mc "What's the road to financial independence?"
    scene w3_7255 with dissolve
    fel "I would prefer satisfying other things than your curiosity, [mcf]."
    scene w3_7254 with dissolve
    mc "Come on, pleeeeease? I'm indulging you here."
    scene w3_7257 with dissolve
    fel "Oh, fine... I..."
    scene w3_7258 with dissolve
    fel "I have my way."
    scene w3_7259 with dissolve
    mc "...?"
    scene w3_7258 with dissolve
    fel "I know... {i}things.{/i}"
    scene w3_7259 with dissolve
    mc "You know things?"
    "What kind of answer was that?"
    scene w3_7260 with dissolve
    fel "...and I'd like to make sure I'm in a secure position to exploit them."
    scene w3_7261 with dissolve
    mc "What sort of things do you--"
    scene w3_7262 with dissolve
    fel "If I told you, I'd have to kill you."
    scene w3_7261 with dissolve
    "......"
    scene w3_7259 with dissolve
    "..."
    scene w3_7263 with dissolve
    mc "You live an interesting life, Mrs. Ford."
    scene w3_7264 with dissolve
    fel "{i}Miss Barnes{/i} is fine tonight, Mr. [mcl]."
    scene w3_7263 with dissolve
    mc "You live an interesting life, Miss Barnes."
    scene w3_7265 with dissolve
    fel "You do too, [mcf]. You're right in front of me, smack dab in the midst of many things, rubbing shoulders with the city's elite at 22."
    fel "You aren't doing bad for yourself. Imagine where you'll be in ten or fifteen years. I bet you'll be trading in the old wife for a new one by then."
    scene w3_7266 with dissolve
    mc "It's hard to picture that."
    scene w3_7265 with dissolve
    fel "Do you plan on being a lifelong bachelor like Dr. Kohler?"
    scene w3_7266 with dissolve
    mc "No, never mind that. I mean it's hard to picture what kind of person I will be in ten to fifteen years."
    scene w3_7264 with dissolve
    fel "You won't recognize yourself. Not necessarily in a bad way, either. It's just a... {i}given{/i}."
    scene w3_7263 with dissolve
    mc "Is that so?"
    scene w3_7255 with dissolve
    fel "If you want to look at it pessimistically, maybe it's because humans are bad at reading the room of life."
    scene w3_7252 with dissolve
    mc "And optimistically?"
    scene w3_7253 with dissolve
    fel "It could be because life takes us all in wildly different, unexpected ways to keep things interesting."
    scene w3_7252 with dissolve
    mc "Some would call that scary."
    scene w3_7267 with dissolve
    fel "Tsk! Pessimism it is, then."
    scene w3_7256 with dissolve
    mc "I do know one thing, though..."
    fel "What's that?"
    hide screen textbox2 with dissolve
    scene w3_7261 with dissolve

    menu:
        "You don't think you'll meet another woman like her. (w3FeliciaHeavyCompliment = True)"(chg=["felicia_up"]):
            $ Felicia_Affection +=1
            $ w3FeliciaHeavyCompliment = True
            show screen textbox2 with dissolve
            mc "I don't think I'll have another encounter with any woman like you, Felicia."
            scene w3_7260 with dissolve
            fel "Flatterer."
            scene w3_7261 with dissolve
            mc "I'm serious."
            scene w3_7258 with dissolve
            fel "There's a lot of gold digging hoes out there, [mcf]."
            scene w3_7259 with dissolve
            mc "...and I've met the most interesting of them all already. Seriously, like you said, I'm 22!"
            scene w3_7261 with dissolve
            mc "Where do I go from here? And even if they came close to your vivaciousness, appetites, and intellect..."
            scene w3_7268 with dissolve
            fel "...?"
            mc "...you'll have the benefit of time and being the first in my memory."
            scene w3_7269 with dissolve
            fel "Shuuuut up. Vivacious?"
            fel "You sound like an old man trying to sweet-talk a young girl."
            scene w3_7270 with dissolve
            mc "Well, even if some of it is just the naivety of youth, you can imagine where I'm coming from. I'm barely not a kid, and you're... {b}you{/b}."
            mc "You've been on this side of things before, right? "
        "You'll have put distance between you and the Club by then.":

            show screen textbox2 with dissolve
            mc "My club days will be long behind me then."
            scene w3_7260 with dissolve
            fel "...why would you ever want to quit?"
            scene w3_7271 with dissolve
            mc "...is that a serious question? I'll pay for college, but after that, I just want to live a normal life."
            scene w3_7272 with dissolve
            mc "Can't believe I'm saying this, but one of the perks of being a doctor will be {i}not{/i} tussling with loan sharks and gangsters."
            scene w3_7271 with dissolve
            mc "What? Do you want to be 50 and still sadly chasing after your kicks?"
            scene w3_7273 with dissolve
            fel "......"
            scene w3_7274 with dissolve
            fel "...there will always be something new to chase, I think. That's just the kind of person I am."
            scene w3_7271 with dissolve
            mc "Is that so...?"
        "(Joke) Any personal crises probably won't lead you to getting dicked down on stage."(chg=["felicia_down"]):

            $ Felicia_Affection -= 1
            show screen textbox2 with dissolve
            mc "I won't be getting dicked down on stage in the midst of a personal crisis."
            scene w3_7275 with dissolve
            "........."
            scene w3_7271 with dissolve
            "......"
            scene w3_7272 with dissolve
            mc "...I'm joking?"
            scene w3_7257 with dissolve
            fel "*Sigh* I know..."
            scene w3_7259 with dissolve
            "........."
            "......"
            scene w3_7260 with dissolve
            fel "...don't know it until you try it, stud."
            scene w3_7261 with dissolve
            mc "Is that so...?"

    scene w3_7276 with dissolve
    "........."
    "......"
    scene w3_7277 with dissolve
    mc "Can I see?"
    fel "Nothing to see. I've barely gotten started."
    scene w3_7278 with dissolve
    mc "Right, yeah..."
    scene w3_7276 with dissolve
    "........."
    "......"
    scene w3_7279 with dissolve
    fel "...thanks for agreeing to this, [mcf]."
    scene w3_7280 with dissolve
    mc "Eh. Sitting here just means I don't have to work too hard to accommodate you."
    mc "Win-win--"
    scene w3_7281 with dissolve
    fel "Hey, don't move!"
    mc "Oh, uh, my bad..."
    scene w3_7282 with dissolve
    "I would later learn I had underestimated the backbone required to sit in a relatively unchanging pose for a couple of hours, nor the fortitude needed to keep a conversation going while your ass was falling asleep."
    "Still, it was enjoyable to watch Felicia work, half-hidden behind a canvas, as her face twisted in all manner of curious, frustrated, and ultimately {b}adorable{/b} expressions."
    scene w3_7283 with dissolve
    "Eventually, the conversation waned and--"
    stop music fadeout 3.0
    scene black with fade
    "........."
    "......"

label w3FeliciaRomanceRising:

    play music "music/helium.ogg"
    scene w3_7284 with dissolve
    "I felt the spread of human warmth seep into my body."
    scene w3_7285 with dissolve
    mc "...uh... ah, crap. I'm a bad model, huh?"
    scene w3_7286 with dissolve
    fel "Quite the contrary. It wasn't an issue."
    scene w3_7287 with dissolve
    mc "Did you finish?"
    fel "I decided to take a break. You looked so serene that it rubbed off on me."
    scene w3_7288 with dissolve
    mc "I've been told I have that effect on people."
    fel "Narcolepsy?"
    scene w3_7289 with dissolve
    mc "Heh, ah..."
    mc "So... is the painting far along enough for me to look at it now??"
    scene w3_7290 with dissolve
    fel "Absolutely not."
    scene w3_7291 with dissolve
    mc "Oh, come on. I wanna take a look--"
    fel "I said no!"
    scene w3_7292 with dissolve
    fel "It's...! Uh..."
    scene w3_7293 with dissolve
    fel "It's not finished. So, don't look yet."
    scene w3_7294 with dissolve
    mc "{i}Felicia Barnes.{/i} Are you... {i}embarrassed?{/i}"

    if w3FeliciaPlatonic == True:
        scene w3_7295 with dissolve
        fel "......"
        scene w3_7296 with dissolve
        fel "...it seems I am. So, that's what that feels like."
        fel "Pffh- heh..."
        jump w3FeliciaDatePlatonicEnd
    else:
        scene w3_7293 with dissolve
        fel "No, it's just... uh..."

    scene w3_7297 with fade
    "In between breaths, Felicia wrapped herself around me like a sloth clinging to a tree branch."
    scene w3_7298 with dissolve
    fel "...the night's getting cold, and I don't want you going anywhere?"
    scene w3_7299 with dissolve
    fel "........."
    mc "......"
    scene w3_7300 with dissolve
    "......"
    "...Felicia had the right idea about the snuggling."
    "The heat from her body was an {b}undeniably{/b} better alternative to walking around sans big-breasted blonde clinging to your side."
    "Accepting my fate, I sank deeper into the outdoor sofa, soaking in the feeling and peering up at the stars."
    scene w3_7301 with dissolve
    fel "Besides, it's seven years' bad luck to look at an unfinished painting without permission."
    scene w3_7302 with dissolve
    "Every so often, Felicia would reaffirm her grip on my bicep, keeping me firmly rooting in place as if I was in danger of floating off into the night sky."
    scene w3_7303 with dissolve
    mc "That's not a thing."
    scene w3_7302 with dissolve
    "While doing so, alongside every squeeze, Felicia offered me something cute to digest."
    scene w3_7301 with dissolve
    fel "...do you really want to risk it?"
    scene w3_7305 with dissolve
    "Sometimes her repositioning would be followed by a girlishly sweet coo, a novelty contrasted against her typical svelte and seductive mannerisms."
    scene w3_7304 with dissolve
    "Another time, I caught her taking a deep whiff of my shirt's fabric, curiously picking apart notes of detergent and B.O."
    "Mostly, I became familiar with just how much this girl {i}fidgeted{/i} absent any occupying thought."
    scene w3_7300 with dissolve
    "The scene beneath the starlit sky was no less befitting two lovers, and I think Felicia was keenly playing on that vibe."

    if feliciaSugarBaby == True:
        mct "(...was this the kind of thing she's willing to pay for?)"
    else:
        mct "(...was this what she was trying to pay for?)"

    scene w3_7305 with dissolve
    "Not that I was complaining. The way she affectionately stroked my arm, alongside every other adorable gesture, was a total headrush."
    scene w3_7300 with dissolve
    "Having an older woman like Felicia preciously clinging to you would do that to your average man."
    scene w3_7308 with pixellate
    chuck "--I don't think you're mundane either. Which is good, because I'm not losing to some common idiot."
    mct "(...or was I so average?)"
    "The company of beautiful women has fallen into my lap so easily and so often recently that I kinda feel like it's a matter of fact."
    "Or rather..."
    scene w3_7306 with pixellate
    mct "(I deserve this...)"
    "......"
    "..."
    scene w3_7307 with dissolve
    mct "(Gah, I'm a dumbass. Why am I thinking about an old man in this situation?)"
    "Not when--"
    scene w3_7309 with dissolve
    "The mood {i}flipped.{/i}"
    scene w3_7310 with dissolve
    fel "...back on Earth, stud?"
    scene w3_7309 with dissolve
    "Lo' and behold, pulled from my thoughts, I discovered myself peered at by a potent set of upcast eyes."
    scene w3_7311 with dissolve
    mc "Don't get jealous. I wasn't anywhere that didn't involve you."
    scene w3_7309 with dissolve
    "...but instead of the usual azure jewels, I found a pair of tiny black holes, pulling me toward an inescapable horizon."
    scene w3_7312 with dissolve
    fel "..."
    scene black with fade
    "Flesh-and-blood Felicia became inevitability itself."
    scene w3_7313 with fade
    mc "........."
    scene w3_7314 with dissolve
    fel "......"
    scene w3_7313 with dissolve
    "Coiled in anticipation, Felicia examined the lines of my face."
    scene w3_7315 with dissolve
    mc "Did you climb on my lap just to stare?"
    scene w3_7316 with dissolve
    fel "I'm thinking about the way you rearranged my insides in my husband's office last week."
    scene w3_7314 with dissolve
    "There was a soft haziness to the air, and alongside her words, I grew hard under Felicia's scrutiny."
    scene w3_7316 with dissolve
    fel "Mmmh... the train is right on time. That's what I was waiting for."
    scene w3_7317 with dissolve
    mc "...sure you're not waiting to be kissed?"
    scene w3_7318 with dissolve
    fel "I don't like kissing..."
    scene w3_7319 with dissolve
    mc "Everyone likes to be kissed."
    scene w3_7318 with dissolve
    fel "Not meeee..."
    scene w3_7319 with dissolve
    mc "Do you kiss your husband?"
    scene w3_7320 with dissolve
    fel "I do, and that is {i}precisely{/i} my point, [mcf]."
    scene w3_7321 with dissolve
    mc "Do you lay your head on his shoulder?"
    scene w3_7320 with dissolve
    fel "What a stupid question..."
    scene w3_7317 with dissolve
    mc "Read the room, idiot. You're the one who set it."
    scene w3_7322 with dissolve
    mc "I'm kissing you, Felicia."
    scene w3_7323 with dissolve
    fel "..."
    play ambient "sound effects/kissing1.mp3"
    hide screen textbox2 with dissolve
    scene fa_makeout1_a with dissolve
    show fa_makeout1 with dissolve
    "It didn't take much convincing for the blonde to bring her lips to mine, confirming my suspicion that Felicia wanted to be kissed."
    "It was an odd line in the sand to draw, but I'd wager her half-hearted discernment was meant to leave the onus on me."
    "Sure, we had kissed before, but it was never a point of focus. {i}Or contention{/i}."
    "For a woman who had built her life around knowing and targeting what she wanted, this peculiarity in her personality presented as a delicacy."
    fel "Mmmmhh..."
    "And soon, I was hopped up on the intoxicating rush of Felicia's tongue slipping into my mouth, and the waxy texture of her amber-painted lips being pried apart by mine."
    fel "Haaat- *Cwhup, ffwwhhup~*"
    "-- and no surprise Felicia was a better kisser than I."
    "The kiss itself, like much of Felicia's personality, was a contradiction."
    "A mixture of instinct and control, selfish and giving."
    "Her tongue followed mine to a T. {i}Cornering, corralling, and coaxing it into where she wanted it to go.{/i}"
    "So for now, the blonde set the pace and I followed her tender inclinations."
    "Using the tips of my fingers, I caressed the small of Felicia's back, drawing an affectionate trail down her spine."
    "The occasional tickled breathy coo told me she was aware of my idle act; even preoccupied, she was keenly sensing where I touched her body."
    fel "Mmmhh...!"
    "Every pass of my fingernail over the goosebumps that dotted her back pulled us closer, and Felicia's tongue deeper down my throat."
    fel "Haa, haaaa...! *Chwup, fwhhup, khwwwup-*"
    "Her hips began to rock, and soon--"
    play ambient "sound effects/kissing2.mp3"
    scene fa_makeout2_a with dissolve
    show fa_makeout2 with dissolve
    fel "--!"
    "And soon, tenderness turned to passion."
    "I held her close, but that didn't satisfy her."
    "She wanted more."
    "She wanted to be closer."
    fel "Haa, hhaaa!"
    "And to that end, Felicia relaxed, pleasantly pressing her chest into mine, allowing herself to {i}melt.{/i}"
    fel "Mmhh, www[mcf]aaaah...!"
    "All pretense and compartmentalization, as befitting the hedonist blonde, took a backseat to bodily friction."
    "Everything she might've said was conveyed in the way she moved her hips, and in the way the sofa's arm dug roughly into my back."
    fel "Mmmh, mmhhhhh--"
    "In return, I pulled her into me."
    "I grabbed and squeezed, holding onto her dearly."
    "{b}Greedily{/b}."
    "{i}Possessively.{/i}"
    "My hand caressed no more, instead finding firm placement on Felicia's buttocks, spreading and teasing."
    "All the while, internally delighting in the thrill of wantonly clinging to a rich man's wife."
    "{i}Breathing became an occasional thing.{/i}"
    "So locked together, whatever air miraculously found its way into our lungs, was exhaled through the other."
    "I was beginning to feel light. Almost drunk."
    mc "Vhhhuuu..!"
    "A light pounding in my head preoccupied my senses."
    fel "MMmmhhh[mcf]hhhh-!"
    stop ambient
    scene w3_7324 with dissolve
    mc "--!"
    "When we finally did break, the rush of air was exquisite."
    scene w3_7325 with dissolve
    fel "...s-satisfied?"
    scene w3_7326 with dissolve

    menu:
        "You are.":
            scene w3_7327 with dissolve
            mc "...I'm satisfied that you like kissing me."
            scene w3_7328 with dissolve
            fel "Everyone likes to kiss, [mcf]. Don't you know that?"
            scene w3_7329 with dissolve
            "Before I had a chance to retort--"
            fel "*Chwup*"
            scene w3_7330 with dissolve
            mc "Mheh!"
            "It was my nose that got booped."
            scene w3_7326 with dissolve
            fel "Mmmmhh..."
            "...but that moment of brevity was soon overwhelmed by the itchiness and heat growing between our legs."
            scene w3_7328 with dissolve
            fel "Come on..."
            scene w3_7331 with dissolve
            "--!"
            mc "You got it..."
        "...is she?":

            scene w3_7327 with dissolve
            mc "That depends. Are you?"
            scene w3_7328 with dissolve
            fel "That's my sauce for success, stud. I'm {i}never{/i} satisfied."
            scene w3_7326 with dissolve

            menu:
                "Good, because you're just getting started.":
                    scene w3_7327 with dissolve
                    mc "I'll take that as a challenge, Miss Barnes."
                    scene w3_7328 with dissolve
                    fel "Good. I intended it to be."
                    fel "Come on..."
                    scene w3_7331 with dissolve
                    "--!"
                    mc "You got it..."
                "Is that so? {b}Death by kisses.{/b}":

                    scene w3_7332 with dissolve
                    mc "That's kinda sad."
                    fel "I--"
                    play ambient "sound effects/kissing1.mp3"
                    scene fa_makeout3_a with dissolve
                    show fa_makeout3 with dissolve
                    "Kiss after kiss marked Felicia's beautiful face."
                    fel "Hheeuuh..."
                    "A bit of tenderness, slicing like a knife."
                    "Spot after spot, no rhyme or reason, in an effort to bring chills to the bombshell in my arms."
                    mc "Mmhh... *chwup* How... *Fwhhup-* How about..."
                    "The sound of which faded high into the city's backdrop, unbeknownst to everyone below what a little {i}kiss slut{/i} Felicia was."
                    mc "How about... *Chwup* How does... *Chwwwwup-* {i}temporarily{/i}... *Chwwup--*"
                    fel "Eeah♥"
                    mc "--work for *Chup-* for you...?"
                    fel "Ghood...Essounds... hehe..."
                    "*Chwup, fwhhup-!"
                    fel "Soundhhlhiike-"
                    "*Cwhup, fhwup, khhwwwuuup!*"
                    fel "Mmmhh...."
                    stop ambient
                    scene w3_7333 with dissolve
                    fel "That's--"
                    scene w3_7334 with dissolve
                    mc "Yeah?"
                    scene w3_7333 with dissolve
                    fel "...that's a promise you best keep."
                    scene w3_7328 with dissolve
                    fel "Come on..."
                    scene w3_7331 with dissolve
                    "--!"
                    mc "You got it..."
        "Not quite...":

            scene w3_7327 with dissolve
            mc "...not until I blow a load in your guts."
            scene w3_7326 with dissolve
            fel "........."
            scene w3_7335 with dissolve
            fel "......"
            scene w3_7328 with dissolve
            fel "...what are you waiting for?"
            fel "Come on..."
            scene w3_7331 with dissolve
            "--!"
            mc "First things first..."

    scene w3_7336 with dissolve
    "Felicia kept tight-lipped, simply staring up at me with an anticipatory glint in her eye."
    scene w3_7337 with dissolve
    "The cool night was about to get cooler, but I didn't anticipate that being much of a problem."
    scene black with fade
    "Button by button, her eyes remained fixed."
    scene w3_7338 with curtains
    fel "Hmm..."
    scene w3_7339 with dissolve
    "In fact, her touch was searing to my bare skin."
    fel "You're not so bad at the \"looming over\" thing."
    scene w3_7340 with dissolve
    mc "How many points did that score me?"
    "Felicia didn't answer me, instead her favorable appraisal showed in the way she ran her fingers across my abdomen."
    scene w3_7341 with dissolve
    "Her nails sailed across my umbilicus muscle.."
    fel "Hmm..."
    scene w3_7342 with dissolve
    "Took a detour around my external obliques..."
    mc "Ha..."
    scene w3_7343 with dissolve
    "Up to the serratus anterior..."
    fel "Ticklish?"
    scene w3_7344 with dissolve
    "Circled back to the linea alba.."
    mc "Not really..."
    scene w3_7345 with dissolve
    "...until they found their place on my rectus abdominis."
    fel "That's good, because you've got a lot of real estate..."
    scene w3_7346 with dissolve
    mct "(That's a curious way of phrasing it...)"
    scene w3_7347 with dissolve
    "That aside, {i}let's get this aside.{/i}"
    scene w3_7348 with dissolve
    "--in a swift, rough motion."
    scene w3_7349 with dissolve
    fel "A-ah..."
    scene w3_7350 with dissolve
    fel "Mmmh..."
    scene w3_7351 with dissolve
    fel "Your hand feels good on my skin..."
    scene w3_7352 with dissolve
    "Felicia's torso shuddered from a feather-like caress..."
    fel "H-haa...♥"
    scene w3_7353 with dissolve
    fel "O-oh..!"
    mct "(With vigor this time...)"
    scene w3_7354 with dissolve
    "On top of Felicia like this, having her pinned down, I had an inclination..."

    menu:
        "...to stroke her cheek.":
            scene fa_cheekrub_a with dissolve
            show fa_cheekrub with dissolve
            "{i}She had nowhere to escape.{/i}"
            "I let my hand linger across the landscape of Felicia's face."
            mct "(Her cheeks...)"
            mct "(Her lips...)"
            mct "(Her chin...)"
            "I blatantly took measure of Felicia's beauty head-on, peering possessively down at Felicia as if she was a piece of valuable art."
            "......"
            scene w3_7355 with dissolve
            "..."
            scene w3_7356 with dissolve
            "{i}Glomped{/i}, denying my retreat."
            "As if to ask: {i}where do you think you're going?{/i}"
            scene w3_7357 with dissolve
            "........."
            "......"
            "..."
            scene w3_7358 with dissolve
            "Finally, {b}freed.{/b}"
            scene w3_7359 with dissolve
            "Of her own volition, on Felicia's terms."
        "...to roughly touch her by the throat. [mod_chat]":

            $ w3FeliciaChoke = True
            scene fa_choke_a with dissolve
            show fa_choke with dissolve
            "My hand naturally found its way toward Felicia's throat..."
            mct "(...she said something about a reminder that I could overpower her, didn't she?)"
            fel "Euuuh..."
            "{b}And closed{/b}."
            "She didn't say a word, and neither did I."
            "I squeezed, but Felicia took it in stride."
            "She shut her eyes and inhaled like she was submerging herself in water."
            "For a moment, we shared in an indelible feeling."
            "The kind that sank down into your gut, snagged on your insides."
            "For as long as my fingers were around the blonde's throat, I felt buoyant. {i}Lighter than air{/i}."
            "Perhaps, to this degree, Felicia's indulgent tendencies were rubbing off on me."
            fel "A-hahh-!"
            fel "Mmmh, hhhmmm...!"
            "........."
            "......"
            scene w3_7361 with dissolve
            fel "--!"
            "A tap on the wrist, and Felicia let me know to relent."
            scene w3_7362 with dissolve
            fel "...ahahh."
            "An exaggerated {i}gulp{/i} cut the tension."

    scene w3_7360 with dissolve
    fel "Mmmmh... heh... you let that \"looming\" comment go to your head."
    fel "Careful, though. It's not wise to corner an old cat..."
    scene w3_7359 with dissolve
    "A playful smirk revealed itself on Felicia's face."
    mc "Oh, yeah...?"
    scene w3_7360 with dissolve
    fel "Mhmm..."
    scene w3_7363 with dissolve
    fel "...claws!"
    mc "H-ha!"
    scene w3_7364 with dissolve
    "{i}Ticklish.{/i}"
    "Pressing her advantage, Felicia deftly maneuvered around me."
    scene w3_7365 with dissolve
    mc "Heh.. ha... what are you--"
    "The sudden change in position and Felicia's burst of energy left me flabbergasted."
    scene w3_7366 with dissolve
    "--but the sight of Felicia's ass exposed made me want to give chase."
    scene w3_7367 with dissolve
    fel "Back away!"
    mc "What are you going to do with that--"
    scene w3_7368 with dissolve
    mc "-g-gah?!"
    scene w3_7369 with dissolve
    "Wielding the brush like a dagger, Felicia drew blood."
    fel "Back away! {b}Slowly!{/b}"
    scene w3_7370 with dissolve
    mc "Alright, alright..."
    "Seems Felicia was feeling {i}very{/i} playful."
    scene w3_7371 with dissolve
    mc "Uh... how can I create some distance if you're following me?"
    fel "Oh, I don't want distance, stud."
    scene w3_7372 with dissolve
    mc "...what do you want?"
    scene w3_7373 with dissolve
    fel "Lots of things."
    scene w3_7372 with dissolve
    mc "Start with one."
    scene w3_7373 with dissolve
    fel "Number one? {b}Sit down.{/b}"
    scene w3_7372 with dissolve
    mc "I--"
    scene w3_7374 with dissolve
    mc "Aaah, o-okay, okay..."
    "I stopped short of saying \"you might put my eye out\", as that..."
    scene w3_7375 with dissolve
    "{i}That would've been lame as fuck.{/i}"
    mc "Okay, I'm sitting!"
    scene w3_7376 with dissolve
    "........."
    "......"
    scene w3_7377 with dissolve
    mc "...what are you leering at?"
    scene w3_7378 with dissolve
    fel "It's just... you're {i}missing{/i} something."
    scene w3_7377 with dissolve
    mc "I'm afraid to ask what..."
    scene w3_7379 with dissolve
    fel "You're unbalanced. May I?"
    scene w3_7380 with dissolve
    mc "Are you asking this time?"
    scene w3_7379 with dissolve
    fel "Sit still..."
    scene w3_7381 with dissolve
    "A quick, light dab and I felt the cold pigment sink into my cheek."
    scene w3_7382 with dissolve
    fel "Now, that's better."
    scene w3_7383 with dissolve
    mc "All you did was splotch paint on me."
    scene w3_7384 with dissolve
    fel "Untrue. I've put my mark on you."
    scene w3_7385 with dissolve
    fel "I've given you my signature..."
    scene w3_7386 with dissolve
    mc "...what's number two of your demands?"
    scene w3_7387 with dissolve
    fel "The second...?"
    scene w3_7388 with dissolve
    mc "You're still armed, and first was for me to sit down. What's the second?"
    scene w3_7389 with dissolve
    "........."
    "......"
    scene w3_7390 with dissolve
    fel "...the second is to lose the pants."
    scene w3_7391 with dissolve
    mct "(I can agree with that one--)"
    scene w3_7392 with dissolve
    fel "Stop."
    mc "...?"
    scene w3_7393 with dissolve
    fel "I've got them."
    "As silly as this was..."
    scene w3_7394 with dissolve
    mct "(...this was oddly sexy?)"
    "Then again..."
    mct "(...what's odd about a woman on her knees with her tits out?)"
    scene w3_7395 with dissolve
    fel "May I?"
    mc "Are you asking this--"
    scene black with fade
    fel "Nope."
    "..."
    scene w3_7396 with fade
    mc "You're not going to paint my junk are you?"
    scene w3_7397 with dissolve
    fel "Well, now that you mention it..."
    scene w3_7398 with dissolve
    mc "......"
    scene w3_7399 with dissolve
    fel "...I'm kidding."
    scene w3_7400 with dissolve
    fel "I'm actually feeling a bit {b}undergunned{/b} now..."
    mc "So... Miss Barnes... what's your third demand?"
    scene w3_7401 with dissolve
    fel "Third, huh? Pheeeeew!"
    fel "You {b}are{/b} accommodating. Hmmm..."
    scene w3_7402 with dissolve
    "I witnessed Felicia go someplace else for the moment, reaching into her perverted toolbox and weighing her options."
    scene w3_7403 with dissolve
    "After a while, she resurfaced, donning an immaculately devilish smile."
    scene w3_7404 with dissolve
    fel "Let's pick back up where we left off."
    mc "And where was that exactly?"
    scene w3_7405 with dissolve
    fel "Back when we were horizontal. That had you going."
    mc "That had a lot to do with you..."
    scene black with fade

    if w3FeliciaChoke == True:
        fel "Oh, yeah? Is choking typically part of your foreplay repertoire?"
        mc "Not really..."
        fel "Uh huh. And I said you were more confident than the boy I first met, didn't I?"
    else:
        fel "So it did, but... mmmh..."

    scene w3_7406 with dissolve
    fel "I think I want to lay back and watch you figure out what to do with yourself."
    scene w3_7408 with dissolve
    mc "Are you telling me to have my way with you?"
    scene w3_7406 with dissolve
    fel "Something like that, but I prefer thinking of it as having a front-row seat to my own sex appeal."
    fel "Treat me like a whore. Get rough with me."
    scene w3_7407 with dissolve
    "Standing as she was, chest jutting out in purpose, the answer to that question lingered on the tip of my tongue."
    scene w3_7409 with dissolve

    if w3FeliciaMeanShock == True:
        fel "Luckily there's no cattle prod up here."
        mc "That's not funny."
        fel "I wasn't joking."
    else:
        fel "Show me more about yourself."
        mc "I don't think it would be all that illuminating."
        fel "I disagree."

    scene w3_7410 with dissolve
    "Once again, it seemed to me she was keen on shifting the initiative in spite of herself."
    "Maybe it's because she's used to playing ancillary to powerful men?"
    "Maybe it was her way of preemptively taking control of the situation?"
    mct "(Or maybe she really did just want to lazily lay back and let me thrill her?)"
    "Still, and this could all be in my head, but judging from the way she initiated on the couch and her playful pivot with the paintbrush, I think she was preening for something different than the usual {i}rough and filthy.{/i}. The thing was..."
    mct "(Those are my magic words, although it may lead to something {i}ugly{/i}...)"

    menu:
        "Do as suggested. Indulge your id. [mod_chat]":
            $ w3FeliciaLoseControl = True
            stop music fadeout 3.0
            scene w3_7411 with dissolve
            mc "Well, you don't leave me any choice, armed as you are..."
            scene w3_7412 with dissolve
            fel "No, I don't..."
            fel "Have at it, stud."
            play music "music/wanderlust.ogg"
            scene black with fade
            "...turns out, nothing kills the romantic tension like flopping your cock on a woman's chest."
            scene w3_7414 with w24
            fel "Heh, heh... so that's what you have in mind? Gonna warm your nice, hard dick between my tits?"
            scene w3_7413 with dissolve
            mct "(Can't dispute the view, though...)"
            scene w3_7414 with dissolve
            fel "Well, whatever the case... {i}make some noise{/i} while you're up there."
            scene w3_7415 with dissolve
            mc "There won't be much ambiguity in how much you get me going, Felicia."
            scene w3_7414 with dissolve
            fel "Yeah..."
            scene w3_7416 with dissolve
            "Her eyes drifted and lingered on the cock in front of her nose."
            fel "You're right about that..."
            "Gradually..."
            scene w3_7417 with dissolve
            fel "A-ahh... heh..."
            "I shifted my posture, dragging my length across the pliant, sun-kissed flesh of Felicia's chest and wedging it between Felicia's bust."
            scene w3_7418 with dissolve
            fel "That..."
            "All the while, Felicia kept an eye on the prize."
            scene w3_7419 with dissolve
            fel "That fits quite nicely. Like it was made to go there..."
            fel "A stupendous cock matched for my perfect tits."
            scene w3_7420 with dissolve
            mc "Have you ever met a cock you didn't like?"
            scene w3_7421 with dissolve
            fel "I believe there's no such thing as a bad cock, only those who aren't worthy of having one."
            fel "Are you just going to stare at me?"
            scene w3_7420 with dissolve
            mc "If I want to? Sure."
            scene w3_7421 with dissolve
            fel "Euugh... that's bor--"
            scene w3_7422 with vpunch
            fel "-oohringg-?! E-eh"
            "I tested the waters with a pinch."
            mc "You're the one keen on changing the mood all of a sudden."
            scene w3_7423 with dissolve
            fel "Hnng, haa... eheh... it got bigger."
            mc "It did. And..."
            scene w3_7424 with vpunch
            fel "Ha-haaat...?!"
            "{i}Another.{/i}"
            "Why did Felicia's flippant attitude irk me?"
            fel "Hnnngg....!"
            mc "Losers like me have a simple psychology."
            scene w3_7425 with dissolve
            fel "Mmmeeeh... heh... you gotta kill that shame crap, [mcf]. It's {i}dull.{/i}"
            scene w3_7426 with dissolve
            mc "..."
            scene w3_7425 with dissolve
            fel "What's with that look?"
            scene w3_7426 with dissolve
            mc "I guess I'm just feeling fond of you."
            scene w3_7427 with dissolve
            fel "I'm {i}well{/i} aware of that..."
            scene fa_titfuck1_a with dissolve
            show fa_titfuck1 with dissolve
            fel "Aheh...!"
            "With my cock smothered by Felicia's sweaty breasts, I rocked my hips."
            fel "That's right..."
            "Now, I didn't intend to finish here. Not like this."
            fel "{b}Fuck my tits, stud.{/b}"
            "Even with her telling me to have fun, and even with how great her tits were, there were greener pastures."
            fel "What else are they for?"
            "I would however, for a time, greedily soak in the sensation of using the trophy wife's bosom like it was my own personal sex toy."
            fel "A set like these, on a frame like mine? I hit the genetic lottery."
            "And looking down at Felicia like this, her dirty talk pulling me along, I felt... {i}better than her.{/i}"
            fel "It's like God set me up for success..."
            mc "Ah, s-shut up..."
            "That dull response was the best I could muster as I watched my cock disappear into a valley of flesh."
            fel "Mmmhm, and why should I?"
            "With every pass, I timed my squeezes oh-so-right so the crown of my penis struggled to break through."
            fel "Am I talking too much for your liking?"
            "So, upon reentry, the corona and neck of my glans caught torturously on the firm give of Felicia's breasts."
            fel "Heh... a pair of tits shouldn't squawk, huh?"
            "Each pass through these glorious mounds sent a tingle up my spine and exposed me to Felicia's words."
            mc "You were cute tonight... you were so invested.... a-ah..."
            "{i}What was I even saying?{/i}"
            mc "You painted me..."
            "{i}Seriously, why did the change in attitude irk me?{/i}"
            mc "It's been a nice night..."
            "I felt an immense frustration with that disconnect."
            fel "Is fucking my tits not nice?"
            "--like we had connected, but now Felicia was steering us off a cliff and watching me like a lab rat."
            mc "Seriously... just shut up for a second."
            "What was even more frustrating..."
            fel "Only if you tell me what's going on in your head right now..."
            "...was that I didn't want to ever remove myself from Felicia's fleshy grasp."
            mc "I'm starting to think of you as--"
            fel "An object? {b}Go ahead.{/b}"
            "She loved doing this."
            fel "Isn't that what I've done with you tonight?"
            "{i}Prodding and muddling.{/i}"
            fel "Use your presence to make myself feel more secure?"
            "Mixing me up and pushing my buttons..."
            fel "Just fuck me like a dirty whore. I know you want to, or..."
            "{i}Taking control and worming her way into my skull.{/i}"
            fel "Are you having trouble reconciling that with liking me?"
            mc "That--"
            stop music
            scene w3_7469 with dissolve
            play sound "sound effects/slap3.wav"
            scene w3_7470 with hpunch
            fel "Gaah-!"
            scene w3_7471 with dissolve
            mc "{b}You fuckin'...!{/b}"
            scene w3_7472 with dissolve
            "Her devilish smile was louder than words."

            if w2FeliciaDegrade == True:
                "That frivolous side of her pissed me off. {i}Just as it had in her husband's office.{/i}"
            else:
                "{i}That frivolous side of her pissed me off.{/i}"

            "No other words left my throat; no, they were drowned out by the bile rising up from my stomach."
            scene w3_7473 with dissolve
            fel "You don't have to reconcile it."
            scene w3_7474 with dissolve
            "This woman might just be the scariest thing on the face of the earth."
            scene w3_7473 with dissolve
            fel "...just embrace the absurdity."
            scene w3_7474 with dissolve
            "While Kathleen was blatant and honest, Felicia..."
            scene w3_7476 with dissolve
            mc "...you want to pull me down to your level?"
            play music "music/hypnosis.ogg"
            scene pr0003 with pixellate
            mc "Fine! You're not shit, bitch!"
            mc "You think you are, but there's a dozen whores at the club I could be doing this with."
            mc "Hell, if I wanted to..."
            scene fa_titfuck2b_a with pixellate
            show fa_titfuck2b with dissolve
            mc " ...maybe, I should've gone home with Lucy tonight!"
            fel "Euuah, a-aahh...?!"
            mc "It's all the same, right?"
            fel "Euguggh?!"
            mc "Or maybe you're right! Maybe I AM fond of you, you smug whore!"
            scene fa_titfuck2_a with w19
            show fa_titfuck2 with dissolve
            "I swam headfirst into a riptide of contempt, delighting in the way it robbed me of air."
            fel "Eeeuuuugughhh-♥"
            mc "{b}Fuck, something about you just PISSES me off!{/b}"
            "I felt exalted."
            mc "...and why do I fucking love that?"
            fel "Euuhhh... I don't know... because you want me to judge you and I'm not? Ahhh...♥"
            "{i}She was probably right on the money.{/i}"
            "She probably rarely wasn't."
            mc "Oh, fuck you and your stupid perfect tits!"
            "A relief washed over me."
            fel "Euuugghhh, hhnnnn, haaat...♥"
            "Like I had opened a lid too tightly sealed."
            fel "Hmmm, haaah, s-shit...♥"
            "Alongside my catharsis, Felicia's moans fell deaf on the city around us."
            scene w3_7428 with dissolve
            mc "*Agem, aahhh... heuughh..."
            fel "Is this what you wanted?"
            scene w3_7429 with dissolve
            mc "Don't fucking look at me!"
            scene w3_7477 with dissolve
            mc "Where do you want it?!"
            fel "My ah--"
            play music "music/addict.ogg"
            scene w3_7478 with hpunch
            fel "Eaahs-{b}ooohh?!{/b}"
            mc "As if I didn't already know, you carnivorous bitch!"
            scene fa_bf06_a with dissolve
            show fa_bf06 with dissolve
            "Slipping into Felicia was a trifling thing."
            fel "Y-yes!"
            "I had no more entered her as she had pierced herself on my cock."
            fel "Ahh...♥"
            "Her guts swallowed me with enthusiasm, sucking me in, daring me to even attempt to leave."
            mc "Take it!"
            "As if that was ever in the cards."
            mc "{size=+10}Take my fucking cock!{/size}"
            "Neither of us would be satisfied until I left Felicia's asshole well-used and gaping."
            mc "Take it in your fuckin' ass! "
            "If I didn't, I wouldn't ever go back to {i}normal{/i}."
            fel "Ghh, hhhk-♥"
            "With my hand on her throat, I leveraged myself and pounded {b}hard{/b}."
            mc "{b}Scatter-brained slut!{/b}"
            "Clap after thunderous clap rang out, as I battered my thighs against Felicia's softest bits."
            fel "Ghh, hhhkk...♥ S-show me...!"
            "Sexual effluvia painted my balls sticky with every flap, all generously sourced and flowing freely from Felicia's untouched cunt."
            fel "S-shhow, hhk! Show...! S-show me more!"
            mc "More?!"
            fel "{b}M-more!{/b} {i}Harder{/i}."
            mc "You want more?! You greedy--"
            fel "Hhhh, {b}m-more!{/b}"
            mc "No one fucks you like this, huh? Is that it?!"
            fel "Euughh, hhk! Hnnggk...! N-no o-one..!"
            "The sound of her words passing through my grip?"
            fel "No one fucks me like {b}this{/b}."
            "{i}Delightful.{/i}"
            fel "N-no one...! {b}No one!{/b}"
            fel "{b}Fhhuuuuuuuuck--{/b}"
            mc "Goddamn it, you--"
            scene fa_bf07_a with dissolve
            show fa_bf07 with dissolve
            "Unceremoniously, {i}Felicia came.{/i}"
            mc "G-greedy fuck pig!"
            fel "Euuhhh, hahaaaa...♥♥♥♥ M-more!"
            mct "({i}She wants more?!{/i})"
            fel "Hkkk, hhkkk!"
            scene fa_bf08_a with flash
            show fa_bf08 with dissolve
            "So I tightened down, taking control of her airways."
            mc "Fuckin' trailer trash!"
            scene fa_bf07_a with dissolve
            show fa_bf07 with dissolve
            fel "Euuhhk-!"
            mc "How 'bout you fuckin' show me?!"
            fel "Euhhh-!"
            "Not the brightest of dirty talk, but..."
            scene fa_bf08_a with flash
            show fa_bf08 with dissolve
            mc "Show me how you earn your keep!!"
            "My creativity was understandably hampered right now, sold only for the pure intensity of the moment."
            fel "Ehhhuuk! Hkkk♥♥♥♥♥"
            "Again, like it was her only function in life, Felicia climaxed."
            fel "Eieeeeeahhh...♥"
            "Again, her pleasure-wracked cries filtered out from my fingertips."
            scene fa_bf07_a with dissolve
            show fa_bf07 with dissolve
            fel "Euuhuhhk!"
            "Again, I squeezed tighter, delving fully into the lunacy."
            mc "Cum your dignity out, bitch!"
            fel "Euuughhk, hhhhhgk!"
            mc "Splatter it all over my cock!"
            fel "Ghhk, hhkk-♥"
            mc "Yeah, I'm nothing I pretend to be!"
            scene fa_bf08_a with flash
            show fa_bf08 with dissolve
            fel "Hhhhg...♥"
            mc "{b}Who{/b} the fuck is?!"
            fel "Hhhk, hhhkkeeuug...♥"
            "In this moment, I felt like a collection of urges, driven by an ill-suited ego."
            scene fa_bf07_a with dissolve
            show fa_bf07 with dissolve
            "--and that wasn't so bad!"
            mc "Beg for my cum!"
            fel "Hkkkhh-♥"
            mc "Beg for it!"
            fel "Hgggk, hhhggggg-♥"
            mc "Beg for it-♥"
            stop music
            play sound "sound effects/spurt.wav"
            scene w3_7479 with flash
            mc "Ghhh, hhhk--"
            "The death of the nonsense I was spewing was immediate, expelled forth into Felicia's gut."
            fel "Euuggh...♥"
            play sound "sound effects/spurt.wav"
            scene w3_7480 with flash
            "My contempt faded away just as easily as it had been conjured."
            fel "Euughhh..."
            play sound "sound effects/spurt.wav"
            scene w3_7481 with flash
            fel "Euuggh... oohhhh...."
            "It all seemed like a transitory moment that had slipped through my fingers."
            scene black with fade
            mc "Heeh... oh... wow..."
            scene w3_7466 with w12
            "Equal parts relief and frustration, cut with a bit of numbness from overwrought pleasure."
            "And in my vulnerable haze, Felicia held me tight."
            "Nothing was said, but she spoke to me."
            "It's okay to rip open and throw around your baggage sometimes."
            "It might even be needed."
            "-- or maybe that was wishful thinking."
            "As I ruminated on the wordless revelation, the blonde picked her moment to become the center of my world once more."
            play music "music/ethereal-rest.ogg"
            scene w3_7467 with dissolve
            fel "Heh, oh... ehe... that was {b}intense.{/i} {i}Life's a hoot.{/i} Heh..."
            mct "(...hoot?)"
            scene w3_7466 with dissolve
            "She hadn't been toying with me."
            scene w3_7468 with dissolve
            mc "You're chaos, Felicia."
            scene w3_7466 with dissolve
            "This was just how she related. I knew that from the start."
            scene w3_7467 with dissolve
            fel "And, you're right here with me, stud. It's beautiful the way two people can come together and things {b}happen.{/b}"
            fel "God, it makes me want to paint!"
            scene w3_7468 with dissolve
            mc "Sorry. Not moving yet."
            scene w3_7467 with dissolve
            fel "Aw, the candle is burning!"
            scene black with fade
            "Where did that energy come from?"

            $ renpy.end_replay()

            if not persistent.w3FeliciaSoloPath:
                play sound "sound effects/notification.wav"
                show memoryunlock with dissolve
                $ renpy.pause(3, hard=True)
                $ persistent.w3FeliciaSoloPath = True
                hide memoryunlock with dissolve
                $ renpy.pause(0.5, hard=True)


            "..."
            jump w3FeliciaPaintingReveal
        "You're feeling romantic, actually... [mod_chat]"(chg=["felicia_passion_up"]):

            $ Felicia_Confidence += 1
            $ w3FeliciaRomanceFocus = True

            scene w3_7411 with dissolve
            mc "I've got a better idea."
            scene w3_7430 with dissolve
            mc "...I'd also like to pick up where we left off."
            fel "Heh, and...?"
            scene w3_7431 with dissolve
            mc "The {i}holding you close{/i} part, I mean."
            scene w3_7432 with dissolve
            fel "..."
            scene w3_7433 with dissolve
            mc "Isn't that more in line with what you intended tonight?"
            scene w3_7434 with dissolve
            fel "..."
            mc "Besides, I don't need any hoops to enjoy my time with you."
            scene w3_7435 with dissolve
            fel "{i}Well... {i}you've been so accommodating{/i} with me, I guess I can return the favor and skip the foreplay."
            scene w3_7436 with dissolve
            mc "Yeah... that's it. The train can't wait to leave the station."
            scene w3_7437 with dissolve
            fel "Men are {i}so{/i} over-eager."
            scene w3_7436 with dissolve
            mc "Absolutely. No nuance, really..."
            stop music fadeout 3.0
            scene black with fade
            "..."
            play music "music/wanderlust.ogg"
            scene w3_7438 with dissolve
            fel "...go ahead. Stick it in."
            scene w3_7439 with dissolve
            mc "Not yet."
            scene w3_7440 with dissolve
            "Taking Felicia from behind, I wrapped my arms around her and I let my rod linger longingly around the blonde's honeypot. Not to tease, not to build anticipation, but rather..."
            scene w3_7441 with dissolve
            mc "*Cwhup~*"
            scene w3_7442 with dissolve
            "...to control the mood and to stop it from backsliding into Felicia's typical brand of debauchery."
            scene w3_7441 with dissolve
            mc "*Chwup, chwup~*"
            scene w3_7442 with dissolve
            "This was my chance to offer her a taste of something different, and maybe, have her remember me for it."
            scene w3_7443 with dissolve
            mc "*Chwhup, fwhup, kwwwu~*"
            "And why would I want to do that?"
            scene w3_7444 with dissolve
            fel "Hnnngg... you've made your point."
            scene w3_7442 with dissolve
            mct "(...ego?)"
            "{i}I wasn't sure.{/i}"
            scene w3_7445 with dissolve
            mc "I'm not making a point, Felicia. I'm..."
            scene w3_7446 with dissolve
            mc "I'm enjoying the moment."
            fel "Hee, haaa..."
            scene w3_7447 with dissolve
            mc "That's your philosophy, isn't it?"
            mc "When will I ever get a chance to hold {i}Felicia Barnes{/i} close to my chest like this again?"
            scene w3_7448 with dissolve
            fel "...I'm immune to that kind of talk."
            scene w3_7449 with dissolve
            mc "*Chwup~*"
            scene w3_7450 with dissolve
            mc "...okay? I'm not trying to convince you of anything. I'm simply..."
            scene w3_7449 with dissolve
            mc "*Cwhup, chwwup~*"
            scene w3_7450 with dissolve
            mc "...telling you what I'm doing - and even if you invited me here tonight because you see me as someone disposable..."
            scene w3_7448 with dissolve
            fel "I--"
            scene w3_7447 with dissolve
            mc "I'll cherish the glimpse I've gotten of who you are. The world is {i}colorful{/i}, isn't it?"
            scene w3_7448 with dissolve
            fel "...put it in, [mcf]."
            scene w3_7450 with dissolve
            mc "Okay..."
            scene w3_7451 with dissolve
            "I aligned myself with Felicia, and..."
            fel "Mmmhh..."
            scene w3_7452 with dissolve
            "...the head of my cock disappeared. {i}Welcomed utterly{/i}."
            fel "Deeper..."
            "Slowly, I advanced inside her."
            scene w3_7453 with dissolve
            fel "Ha.. haaa..."
            "My attention held captive by the way Felicia's back tensed up as I held her flush against me."
            "......"
            "..."
            scene w3_7454 with dissolve
            fel "You make different colors by combining those colors that already exist."
            scene w3_7455 with dissolve
            mc "...what's that?"
            scene w3_7454 with dissolve
            fel "It's just a thing my old art teacher was fond of saying."
            scene w3_7456 with dissolve
            fel "The world is colorful..."
            scene fa_bf02_a with dissolve
            show fa_bf02 with dissolve
            "Painfully, I fought Felicia's searingly sweet hold on me and pulled myself back."
            fel "Aah-"
            "It was only for a second, but the absence of Felicia became too much to bear, so I drove myself back into her embrace."
            fel "--!"
            "And again."
            scene fa_bf01_a with dissolve
            show fa_bf01 with dissolve
            "And again. And again."
            "Our coitus was a familiar exercise in longing, but in spite of the brain's boiling haze, I felt oddly calm."
            "And not just calm, but a methodical, meditative-like clarity."
            mct "(Control the mood...)"
            "That was the mantra that replayed in my head."
            "I didn't want to rush to my impending orgasm or throw myself into an abyss, but like I professed to Felicia, I was enjoying the moment."
            "I savored every thrust like it was a stroke of a pen, focusing on every thrust like I was connecting lines of calligraphy to create something greater than words on a page."
            "I luxuriated in the way Felicia's cunt accepted every inch of me."
            fel "...g-go faster."
            mc "Not yet..."
            scene fa_bf02_a with dissolve
            show fa_bf02 with dissolve
            mct "(Control the mood.)"
            "Like each individual drum stroke in a solo."
            fel "Go faster..."
            mct "(Control the mood.)"
            mc "Not yet... do you feel how hard I am inside you?"
            fel "H-how would I not..."
            scene w3_7457 with dissolve
            "*Chwuip~*"
            scene w3_7458 with dissolve
            fel "Hnngg~ D-don't-"
            scene fa_bf01_a with dissolve
            show fa_bf01 with dissolve
            mc "Sensitive?"
            fel "*Gulp* You're... you're {i}hard{/i}."
            mct "(Control the mood.)"
            fel "Y-yeah... I feel it...♥"
            "An increasingly difficult proposition, as Felicia played into my mutterings..."
            fel "H-hell, I..."
            "...and a feeling of domineering her through pleasure peskily nipped at my heels."
            fel "I feel your heartbeat, aheh--"
            mct "(Control the mood, [mcf].)"
            fel "-oh!"
            scene fa_bf02_a with dissolve
            show fa_bf02 with dissolve
            "An even more difficult thing to do as a wave of pleasure overtook me and Felicia's sex wrestled to keep me from extracting myself from her."
            mc "You're a jewel, Felicia."
            "...so I tried switching it up. By focusing on her instead of what was brewing in my nuts."
            mc "A living, breathing, uniquely {i}you{/i} jewel."
            fel "Heeuu... y-you're supposed to say things like \"you're a whore\", idiot."
            scene fa_bf01_a with dissolve
            show fa_bf01 with dissolve
            mc "That's, h-heh, that's the thing--"
            fel "A jewel is a commodity."
            mc "... y-yeah, but you've got vibrantly different shades and that's what I love about you."
            fel "You love the way I let you fuck me-♥"
            "Felicia, of course, deflected."
            mct "(Control the mood.)"
            mc "I love how unabashed you are."
            "The muscles in Felicia's arms went taut, as she hugged herself harder."
            mc "I love how you keep looking ahead."
            mc "I love the way you cared {i}deeply{/i} about a stranger's success tonight."
            "I felt her torso pull away from our entangled hold."
            fel "Hnnn, haaa... that's..."
            "...a physical retreat?"
            scene fa_bf02_a with dissolve
            show fa_bf02 with dissolve
            fel "There are so many strangers I don't give a damn about-♥"
            mc "Heh, I'll s-say this... I don't love the way you don't embrace the good things about yourself."
            fel "Hee, heeugugh...♥"
            mc "--b-but then again..."
            scene fa_bf03_a with dissolve
            show fa_bf03 with dissolve
            "Carefully, I upped the tempo, plowing into Felicia with a controlled {i}oompfh{/i}, and keeping in mind my mantra."
            fel "H-haa, haa... y-yes!"
            mc "...b-but then again, that inability kinda makes you {b}cute{/b}, too."
            fel "A-aah, aahhhh...♥ [mcf], if there's one thing I'm not--"
            mc "Don't argue with me!"
            "Hammering away from below, I took possession of her."
            fel "Ah, heeuugghh-♥ Ohhhhhkay-ehhu-♥"
            scene fa_bf04_a with dissolve
            show fa_bf04 with dissolve
            mc "I'm looking at you, Felicia."
            fel "Eeeuuhh-♥"
            mc "You see?"
            fel "Eeeuuhuhh-♥"
            "With a perpetual, unyielding focus on the blonde, I staked an imaginary, transitory claim."
            fel "Wh-whhoo else WOOUULD you be looking at-- [mcf]-♥?"
            mc "H-hehhh, ha!"
            "And just like her, her response was one of conceit and bluster."
            fel "T-there's only us and a sky full of stars."
            "A trait that, perhaps annoying other times..."
            fel "Of course, you're looking at me."
            scene fa_bf03_a with dissolve
            show fa_bf03 with dissolve
            "...was one that I intimately adored right now."
            mc "Eheh... I'm just spewing crap, huh?"
            "I backpedaled, confident in the knowledge that Felicia's other mouth was telling a different story."
            fel "W-well...♥ if saying sappy shit is what you're into... uh..."
            "Felicia wasn't just pushing back into me with the precision of a practiced woman."
            fel "Mmhhh... I'll get used to it."
            "No, there was an unevenness to it."
            mc "Hnnnggg... heh... v-very kind..."
            "A frantic, implicit acceptance of my adulatory pillow talk."
            mc "Very generous..."
            "I pushed in, and so did she, making sure the tip of my cock kissed the far reaches of her cunt."
            fel "Aa, oohhhh...♥ F-fuck, I love how deep you hit-♥"
            mct "({i}Control the mood.{/i})"
            "I tried to focus on every thrust, but my mind was beginning to get foggy."
            mct "({i}Control the mood.{/i})"
            "Felicia tickled the part of my brain that compelled me to ravage."
            mct "({i}Control the mood.{/i})"
            fel "Hnngg...♥ "
            fel "Heeh-♥ O-ohhh..."
            scene fa_bf04_a with dissolve
            show fa_bf04 with dissolve
            fel "♥♥♥♥♥♥♥♥♥♥♥♥"
            fel "♥♥♥♥♥♥♥♥♥"
            fel "♥♥♥♥♥♥"
            fel "-♥♥♥ H-hey, [mcf]?"
            "As Felicia found the words, her cunt grabbed me unlike before."
            fel "C-could you... uh...?"
            "She was taking control of me."
            fel "Kiss me while you cum inside me."
            "My mantra of control fell to the wayside, and she and I both knew..."
            scene fa_bf05_a with fade
            show fa_bf05
            fel "--!"
            "The end, and its roughly sweet delight, was in sight."
            fel "Mmmhhh...♥"
            "Felicia bucked even harder, both heads finally in sync."
            "There was no difference between what her sex or her mouth was doing. It was a singular, indistinguishable act."
            fel "Hhh--♥ Ahhshhh[mcf]ssshhh...♥♥"
            "Everything, in this moment, compressed."
            "The animal fervor behind my thrusts, the layers of unspoken want and guesses, all of it was folded into a single action."
            fel "Hhhhhngg, hhhhhgheeuuu...♥♥♥♥"
            "My lips consumed Felicia, and her tongue dragged me down with her, hurtling both of us toward the precipice."
            fel "Mmmh~♥♥♥♥ Eeuuguhh...♥♥♥"
            "Her moans grew louder."
            fel "Mmhh, hheeeuutt...♥♥♥♥"
            "Her pussy refused escape."
            fel "Eeeuuguhh, mmmhh...♥♥♥♥♥"
            "Her orgasm didn't impede her ardor."
            fel "Mhh, hhh-♥"
            "It didn't slack her intensity."
            fel "Aahh, [mcf]eeeuuhhh...!"
            "Her eagerness was unabated, as she put every iota of herself into getting me to the finish line."
            fel "[mcf]eeuugh, [mcf]eeehhh...!"
            "And as the itch grew in my groin, as the pressure in my balls built, my brain did not scream {i}cum{/i}."
            "*Chwup, fwhhup~*"
            "All of my thoughts were preoccupied by this single, lonesome victory."
            fel "Mmmh, hhhhhh...♥"
            "It whispered to me {i}do not let go--{/i}"
            stop music
            play sound "sound effects/spurt.wav"
            scene w3_7459 with flash
            "This woman, this moment, {i}this feeling...{/i}"
            "As I flooded her insides with my cum, this feeling would seed a memory that would last a lifetime."
            fel "Ah, hhaaa-♥"
            scene w3_7460 with dissolve
            "The memory of the moment that I learned just how transcendental a kiss could be."
            play sound "sound effects/spurt.wav"
            with flash
            "........."
            play sound "sound effects/spurt.wav"
            with flash
            "......"
            play sound "sound effects/spurt.wav"
            with flash
            scene w3_7461 with dissolve
            "..."
            fel "......"
            play music "music/helium.ogg"
            scene w3_7462 with dissolve
            mc "...hey, guess what?"
            scene w3_7463 with dissolve
            fel "No post-coital guessing games, please..."
            scene w3_7462 with dissolve
            mc "Heh... just saying..."
            scene w3_7464 with dissolve
            "........."
            "......"
            scene w3_7462 with dissolve
            mc "...I nutted and I'm still looking at you."
            scene w3_7465 with dissolve
            fel "Pfft... you're such a kid."
            mc "I surprise myself sometimes..."
            scene w3_7466 with dissolve
            "......"
            "..."
            scene w3_7467 with dissolve
            fel "You're not the only one surprised. You read me like a book."
            scene w3_7468 with dissolve
            mc "I suppose it's like you said. We have a {i}certain{/i} compatibility."
            scene w3_7467 with dissolve
            fel "Maybe..."
            fel "Still, I think you could find a rich, old widow for yourself and make bank."
            scene w3_7468 with dissolve
            mc "Is that your professional evaluation?"
            scene w3_7467 with dissolve
            fel "That's my evaluation as a woman."
            scene w3_7466 with dissolve
            "Without further communication, I held Felicia close."
            "I hoped I offered her something a little different."
            scene black with fade
            $ history_felicia = "A simple ending to a night with a complicated woman and two people brought closer together. It was a delusion worth buying into for a few hours."
            $ unread_felicia = True
            play sound "sound effects/notification.wav"
            show bioupdate with dissolve

            "Something that I had enjoyed myself."

            $ renpy.end_replay()

            if not persistent.w3FeliciaSoloPath:
                play sound "sound effects/notification.wav"
                show memoryunlock with dissolve
                $ renpy.pause(3, hard=True)
                $ persistent.w3FeliciaSoloPath = True
                hide memoryunlock with dissolve
                $ renpy.pause(0.5, hard=True)


            "..."
            jump w3FeliciaPaintingReveal


label w3FeliciaPaintingReveal:

    scene w3_7482 with blinds
    show screen textbox2 with dissolve
    fel "...so, uh, yeah, that's--"
    mc "That's me."
    fel "..."
    scene w3_7483 with dissolve
    mc "I don't look like that--"
    fel "I'm... I'm not good when it comes to portr--"
    scene w3_7484 with dissolve
    mc "No, I mean... {b}it looks great{/b}."
    fel "Oh..."
    scene w3_7485 with dissolve
    "......"
    scene w3_7486 with dissolve
    mc "...it is missing something though."
    scene w3_7487 with dissolve
    fel "Heh, I suppose it is..."
    scene w3_7488 with dissolve
    fel "Why don't you do the honors?"
    scene w3_7489 with dissolve
    mc "I'll ruin it."
    scene w3_7490 with dissolve
    fel "You'll make it even more valuable."
    scene w3_7489 with dissolve
    mc "Pssh... no, it won't be."
    scene w3_7490 with dissolve
    fel "It will be to me."
    scene w3_7491 with dissolve
    "She said it so absolutely that it was hard to argue with."
    scene w3_7492 with dissolve
    fel "Truth is... I'm not used to feeling socially anxious, or even... {i}invested{/i} in something outside, well..."
    scene w3_7493 with dissolve
    fel "...when I thought about tonight's showing... I couldn't breathe for some reason. It's such a tiny thing, but--"
    scene w3_7494 with dissolve
    "......"
    scene w3_7488 with dissolve
    fel "...point is, you'll be my co-artist for this piece."
    scene w3_7495 with dissolve
    mc "......"
    scene w3_7496 with dissolve
    mc "I'm honored to be your collaborator."
    "{i}...{i}art is connection.{/i}"
    scene w3_7497 with dissolve
    mc "...that's the word for that, right?"
    fel "Sounds pretentious, but..."
    scene w3_7498 with dissolve
    "........."
    "......"
    scene w3_7499 with dissolve
    mc "...how's that?"
    scene w3_7500 with dissolve
    fel "It's perfect, Mr. Collaborator."
    scene w3_7501 with dissolve
    play sound "sound effects/notification.wav"
    $ Felicia_Relations = "Collaborator"
    show relationfel with dissolve
    "The rest of the night was spent on the smallest of talk that had ever felt... {b}big{/b}."
    "She told me more about the art academy she attended, the friends she made there, and about the town of Wheatley."
    "Her words on her birthplace remained one of derision, yet... it was softer than it had been the night of the second exhibition."
    "She told me more about how she bounced around after coming to the city, not knowing anyone."
    "The details of which, as someone who was taking a shortcut for my own education, made me feel {i}small{/i}."
    fel "...what were you really like growing up?"
    mc "You sure you don't just want to kick me out of your place now that you've had your fun with me?"
    fel "...shut up."
    mc "I was... eugh... I was the kind of kid preoccupied with how I came off to others."
    fel "That makes sense."
    scene black with fade
    "It was a quiet conclusion to a modest night with a woman larger than life."
    "......"
    "..."
    jump w3June17End

label w3FeliciaMinaThrowdownStart:
    stop music
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionfelmina01 with blinds
    $ renpy.pause(6, hard=True)
    play ambient "sound effects/city-night.wav"
    scene w3_7502 with blinds
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    "{i}Felicia's penthouse.{/i}"
    "A stunning view."
    scene w3_7503 with dissolve
    "A belly full of burgers."
    "Heated pool."
    scene w3_7504 with dissolve
    mc "Mmmhh..."
    mct "(When I'm a doctor, I'm definitely buying a pool...)"
    "The only thing missing...."
    scene w3_7505 with dissolve
    "My blonde companions."
    mct "(What's keeping them? I've been soaking for five minutes.)"
    scene w3_7504 with dissolve
    "When Mina arrived..."
    stop ambient
    play music "music/happy-whistling-ukulele.ogg"
    scene w3_7506 with pixellate
    mina "Felicia!"
    "She flittered in like a hurricane."
    scene w3_7507 with dissolve
    mina "Hey! Hey! Hey!"
    "And as usual, she was the brightest thing against the city night."
    scene w3_7508 with dissolve
    mina "Thanks for inviting me!"
    scene w3_7509 with fade
    mina "[mcf]!"
    scene w3_7510 with hpunch
    mc "Heh, hey..."
    scene w3_7511 with dissolve
    mina "It's just the three of us? You sure you want me here?"
    mina "Feels like I might intrude on something?"
    scene w3_7512 with dissolve
    fel "You didn't expect my call?"
    scene w3_7513 with dissolve
    mina "No...?"
    scene w3_7512 with dissolve
    fel "{i}Interesting...{/i} why did you come up town so quick if you worried about playing third wheel?"
    scene w3_7513 with dissolve
    mina "I was excited to be included. It didn't occur to me."
    scene w3_7514 with dissolve
    fel "God, you're precious."
    scene w3_7515 with dissolve
    fel "When have you known me to invite anyone anywhere out of politeness? I want you here."
    scene w3_7516 with dissolve
    mc "Same here."
    scene w3_7517 with dissolve
    mina "Heh, heh..."
    mct "(There's that puppy dog look.)"
    scene w3_7504 with pixellate
    mc "..."
    "Mina had beamed, pleased to be included {i}and{/i} the center of attention."
    scene w3_7505 with dissolve
    mct "(...seriously how long does it take to change into a swimsuit?)"
    "I mean..."
    scene w3_7518 with pixellate
    mc "...you're fucking with me."
    fel "No, really. Elias only wears speedos."
    scene w3_7519 with dissolve
    mc "You're fucking with me!"
    fel "I mean, you can go commando if you want... neither of us would mind~ {i}we've both seen it.{/i}"
    mc "That--"
    scene w3_7520 with pixellate
    "........."
    "......"
    "...in retrospect, this gaudy thing I'm wearing felt {i}more embarrassing than hanging dong.{/i} I don't know why I--"
    scene w3_7521 with pixellate
    mina "Aw, come on I waaaant to see it. Please? Please?"
    mct "(Right. {b}That's why{/b}.)"
    scene w3_7522 with dissolve
    fel "Hehe, *ahem*... you can borrow one of my swimsuits too, Mina. We're about the same size..."
    scene w3_7523 with pixellate
    mc "Mhhh..."
    "The sounds of the city were so relaxing..."
    mct "(When I'm a doctor, I {i}definitely{/i} need a multi-million dollar penthouse above the city.)"
    scene w3_7524 with dissolve
    "........."
    scene w3_7525 with dissolve
    "......"
    stop music fadeout 3.0
    scene black with fade
    mct "(...yeah, that's in the cards. {b}Dumbass{/b})"
    play sound "sound effects/water-splash3.wav"
    mina "--much?"
    "It wasn't much longer until the sound of water breaking pulled me from my inane contemplation."
    stop sound
    play music "music/dont-fret.ogg"
    scene w3_7526 with w12
    fel "Yeah, I know. It's a little tight, but it's what I have on hand."
    scene w3_7527 with dissolve
    mina "Why do I not believe you? A bitch like you has a million swimsuits!"
    scene w3_7526 with dissolve
    fel "Sure, but... uh... they're all at our summer home?"
    scene w3_7528 with dissolve
    mc "Hey, girls..."
    scene w3_7529 with dissolve
    mina "Hey!"
    "Mina snapped back with a Pavlovian-like enthusiasm."
    fel "Besides, you look A-M-A-Z-I-N-G. Right, [mcf]?"
    hide screen textbox2 with dissolve
    scene w3_7530 with dissolve
    "The answer to that question..."
    scene w3_7531 with dissolve
    "...was an unflinching yes."
    "As for Mina's complaint about tightness?"
    scene w3_7532 with dissolve
    "An indubitable yes."
    "The squeeze of the polyester fabric {i}improved upon perfection{/i}, sculpting her already shapely breasts and accentuating their glory."
    scene w3_7533 with dissolve
    mina "..."
    scene w3_7534 with wipeleft
    "And Felicia?"
    play sound "sound effects/water-splash2.wav"
    scene w3_7535 with dissolve
    "Hers was classy and sexy rolled into one; not so much {i}squeezing{/i} as it conformed to her curves."
    fel "Mmmh... Say something, stud."
    stop sound
    scene w3_7536 with wiperight
    "Felicia's smirk revealed her game."
    "Between my speedo and the tit bonanza, she was not even trying to hide her duplicity."
    scene w3_7537 with dissolve
    mc "It goes without saying that Mina looks... {i}yeah{/i}."
    scene w3_7538 with dissolve
    fel "There you have it. The best compliments are served poorly articulated."
    scene w3_7537 with dissolve
    mc "{i}Both{/i} you girls look like a slice of heaven."
    scene w3_7538 with dissolve
    fel "And spoken like a dirty old man."
    scene w3_7539 with dissolve
    mina "If I make a sudden turn, everything's gonna spill out!"
    scene w3_7540 with dissolve
    fel "So? We've all seen them."
    mina " Haaat..."
    scene w3_7541 with dissolve
    "The two of them made quite the pair, and the three of us..."
    mct "(Goddamn it, I'm using up all my good fortune this month.)"
    scene w3_7542 with dissolve
    mina "Sorry for taking so long. Felicia filled me in on--"
    scene w3_7543 with dissolve
    fel "I see you managed to keep yourself amused in our absence. Aren't you supposed to wait 30 minutes after you eat before swimming?"
    scene w3_7544 with dissolve
    mc "Danger's my middle name."
    scene w3_7545 with dissolve
    fel "Mmmhh... nothing's better for idle thoughts, is there?"
    scene w3_7546 with dissolve
    mc "...speaking of those, when's your husband due back again?"
    scene w3_7547 with dissolve
    fel "Couple of days."
    scene w3_7546 with dissolve
    mc "Oh, I should be gone by then."
    scene w3_7548 with dissolve
    "I followed Felicia's example, sinking more completely into the warm water."
    scene w3_7549 with dissolve
    mc "Probably..."
    scene w3_7550 with dissolve
    mina "Oh, yeah, that's... uh..."
    scene w3_7551 with dissolve
    fel "That's what?"
    "A vague look of consternation briefly blanketed Mina's expression, as if suddenly reminded of something."
    scene w3_7552 with dissolve
    mina "{i}Nothing.{/i}"
    scene w3_7551 with dissolve
    fel "No way! You're not feeling bad for Elias, are you?"
    scene w3_7552 with dissolve
    mina "Not... not exactly? I hate that guy. I just realized, I suppose I'm complicit in--"
    scene w3_7553 with dissolve
    fel "Hush! You're sinless. In fact, you being here is going to keep me honest, isn't it?"
    fel "Just three friends... eating some burgers... taking a dip... {i}whatever.{/i}"
    scene w3_7554 with dissolve
    "........."
    "......"
    scene w3_7555 with dissolve
    "...gradually, Mina's perplexity eased up."
    scene w3_7556 with dissolve
    mina "Well, you seemed really happy when talking about earlier."
    scene w3_7557 with dissolve
    mc "She was stoked for her friend. It was adorable."
    scene w3_7558 with dissolve

    if w3FeliciaDeniseConvinced == True:
        fel "She's not my friend, just--"
        fel "Actually... yeah. {i}Friend{/i}, heh..."
        scene w3_7559 with dissolve
        mina "D'aaaaw!"
    else:
        fel "She's not my friend, just--"
        scene w3_7560 with dissolve
        mc "Yeah, yeah... you're a fan."
        mina "Eh...?"
        scene w3_7561 with dissolve
        mc "Point of contention tonight."
        mina "Ooookay..."

    scene w3_7562 with dissolve
    fel "Enough about me! What have you been up to today, peach?"
    scene w3_7563 with dissolve
    mina "Meeeeee? Well...?"
    scene w3_7564 with dissolve
    fel "Moping?"
    mina "Nope!"
    fel "Sulking?"
    mina "Nope!"
    fel "Cursing things?"
    mina "No! I hung out with Hana!"
    scene w3_7565 with dissolve

    if hanaGF == True:
        mc "...really? And what did you two do?"
        scene w3_7566 with dissolve
        mina "Oh, this and that. It was fun."
        "Clearly \"this and that\" didn't involve conversations about me..."
        scene w3_7567 with dissolve
        fel "Huh..."
        "{i}Hopefully.{/i}"
    else:
        mc "Oh, nice. That's great. What did you two do?"
        scene w3_7566 with dissolve
        mina "Oh, this and that. It was fun."
        scene w3_7567 with dissolve
        fel "Huh..."

    scene w3_7568 with dissolve
    mina "You two would get along great! You both kick ass!"
    scene w3_7569 with dissolve
    "Felicia just smiled in response, the irony heavy on her lips."
    scene w3_7570 with dissolve
    fel "We would, huh?"
    scene w3_7569 with dissolve
    "........."
    "......"
    scene w3_7571 with dissolve
    mc "...so, I know the plan for the evening isn't just to get waterlogged."
    "{i}So I veered it back to the present.{/i}"
    scene w3_7572 with dissolve
    fel "And damage our flawless skin?"
    scene w3_7573 with dissolve
    mina "...o-oh?"
    "Felicia brought herself closer with the subtlety of a sledgehammer."
    scene w3_7574 with dissolve
    fel "It was a good excuse to change out of those stuffy clothes."
    mina "Like you need an excuse, you ho."
    scene w3_7575 with dissolve
    mc "I'm not complaining. Felicia had us in matching outfits tonight."
    scene w3_7576 with dissolve
    mina "I {b}noticed!{/b} You actually let Felicia pick your clothes?"
    scene w3_7575 with dissolve
    mc "Your tone makes it sound emasculating."
    scene w3_7576 with dissolve
    mina "No! I'm just... {i}surprised?{/i} Matching outfits!"
    mina "Ian never--"
    scene w3_7577 with dissolve
    fel "Leave that man's name off your lips, dear. {i}Certainly don't use him as a template.{/i}"
    scene w3_7575 with dissolve
    mc "I can't say I didn't feel a bit lap dog-like."
    scene w3_7578 with dissolve
    fel "You don't think important men have people who pick their clothes?"
    scene w3_7579 with dissolve
    mc "Do you dress your husband?"
    scene w3_7578 with dissolve
    fel "Absolutely. He's got no sense for it, and it's cheaper than paying someone to do it."
    scene w3_7579 with dissolve
    mc "Rich people pay people to dress them?"
    scene w3_7580 with dissolve
    mina "They're called personal stylists."
    scene w3_7579 with dissolve
    mc "What's so hard about picking out a black suit?"
    scene w3_7581 with dissolve
    fel "You'd be surprised..."
    fel "Coconut butter...? New shampoo?"
    scene w3_7582 with dissolve
    "Felicia put her face conspicuously close."
    scene w3_7583 with dissolve
    mina "Uh... face cream... do you like it?"
    scene w3_7584 with dissolve
    fel "You usually smell like strawberries."
    scene w3_7585 with dissolve
    mina "I've been feeling like changing some things up..."
    mc "...is there an anonymous support group for rich idiots?"
    scene w3_7586 with dissolve
    fel "Support makes a man, [mcf]."
    scene w3_7308 with pixellate
    chuck "...are you mundane?"
    "My earlier conversation with Dr. Chuck came to mind."
    "I wondered how much help he's had to get where he is..."
    "How much help Abel Van Doren has had."
    "{i}How much help did I need?{/i}"
    scene w3_7587 with pixellate
    mina "Oh! That's right!"
    mina "I haven't had a good look at [mcf]!"
    scene w3_7588 with dissolve
    mc "What do--"
    mina "Your speedo!"
    mc "You can see it through the water."
    scene w3_7589 with dissolve
    mina "I want a good look at it! Model it for me."
    mc "Later. The outside's cold and the pool's warm--."
    mina "Aaaaw! Pleeeease?"
    scene w3_7590 with dissolve
    "........."
    "......"
    scene w3_7591 with dissolve
    "...Mina's \"please\" was a coercive and powerful weapon."
    mc "Alright..."
    play sound "sound effects/water-splash2.wav"
    scene black with fade
    mc "Take a picture, it'll last longer."
    fel "Pfffthaha...! You look-!"
    stop sound
    scene w3_7592 with curtains
    mina "...{b}good!{/b}"
    "I've always found the best way to stave off the feeling of embarrassment was to go for the gusto."
    mc "Yeah, right!"
    "Be bold."
    scene w3_7593 with dissolve
    mina "No, really... you..."
    "{i}Own it.{/i}"
    mina "May I?"
    scene w3_7594 with dissolve
    mc "You don't have to ask for permission to touch me."
    scene w3_7595 with dissolve
    mina "You've got nice thighs..."
    mc "I'm... uh..."
    scene w3_7596 with dissolve
    mina "...and calves."
    mc "Well, I'm no Dr. Frank-N-Furter."
    scene w3_7597 with dissolve
    fel "I've got a pair of fishnets that would fit him. Want to see it?"
    mina "{i}Would I?!{/i}"
    mc "That's enough dress up for me today, ladies..."
    scene w3_7598 with dissolve
    mina "..."
    "Mina's eyes drifted back to me, and she momentarily checked out of the conversation."
    mc "It's a gaudy, black-and-gold floral--"
    scene w3_7599 with dissolve
    mina "You pull it off."
    fel "See, [mcf]?"
    scene w3_7600 with dissolve
    fel "I told him he should have more confidence in himself."
    mc "...I'm going to go get a drink. You want something?"
    fel "He's escaping."
    scene w3_7601 with dissolve
    mina "Hehe, he is!"
    fel "Is he blushing?"
    mina "I can't tell!"
    stop music fadeout 3.0
    scene black with fade
    "I made my escape."
    play ambient "sound effects/city-night.wav"
    scene w3_7602 with fade
    mc "Eh? Why are these back here?"
    scene w3_7603 with dissolve
    mina "Oh, God. {b}Those.{/b}"
    scene w3_7604 with dissolve
    "The sight of the handcuffs brought a troubled, funny look to the younger blonde's face."
    scene w3_7605 with dissolve
    fel "You never know when they'll come in handy."
    scene w3_7606 with dissolve
    mc "Got it. It's a sex thing."
    scene w3_7605 with dissolve
    fel "That or I'm running a prison out of one of my closets."
    scene w3_7607 with dissolve
    fel "Remember when Elias caught you--"
    mina "You don't have to remind me..."
    scene w3_7608 with dissolve
    fel "Pour us ALL a drink, will 'ya stud?"
    mc "What do you want?"
    fel "Bartender's choice."
    scene w3_7609 with dissolve
    mina "Oh, that reminds me! Hana told me she bartended at your work!"
    scene w3_7610 with dissolve
    mc "Uh huh, yeah... she does a lot of things. She's a very {i}handy{/i} girl."
    scene w3_7609 with dissolve
    mina "That'd be fun!"
    scene w3_7611 with dissolve
    fel "You don't even like to drink, Mina."
    mina "Pouring them might be fun, though! I bet she meets all kinds of interesting people."
    stop ambient fadeout 3.0
    scene black with fade
    mc "Oh, yeah. {i}Definitely{/i}"
    fel "It's a lot of drunk assholes flirting with you is what it is."
    mina "Yeah! And?!! You'd be like an unofficial therapist! It'd be so cool!"
    play music "music/the-gentleman.ogg"
    scene w3_7612 with circlewipe
    mct "(That zeal for life is enviable...)"
    "......"
    "..."
    scene w3_7613 with dissolve
    mina "...aaaaah, enough about that, okay?"
    "The three of us simply put on some music and sat down."
    scene w3_7614 with dissolve
    fel "I'll stop... {i}for now{/i}, but let's ask [mcf] the same question."
    scene w3_7615 with dissolve
    mc "What's the weirdest thing I have in my home? Uh..."
    scene w3_7616 with dissolve

    if w2ExEndingKathleen == True:
        mct "(Leaving out the assortment of goodies Kathleen left me...)"
    else:
        mct "(Hmmm...)"

    scene w3_7615 with dissolve
    mc "I guess it's just a lone ping pong paddle that the previous owner left."
    scene w3_7617 with dissolve
    mina "Why's that weird?"
    scene w3_7618 with dissolve
    mc "It was in the nightstand. Alone. Next to the bed."
    scene w3_7619 with dissolve
    fel "Probably a sex thing."
    scene w3_7620 with dissolve
    mc "I actually used it as an impromptu weapon one time when I heard a noise downstairs and thought someone broke in."
    scene w3_7621 with dissolve
    fel "That's about as smart as Mina handcuffing herself to my pool."
    mina "I said enough!"
    scene w3_7619 with dissolve
    fel "And had someone broken in?"
    scene w3_7615 with dissolve
    mc "That's a story best left for {i}another{/i} night."
    scene w3_7616 with dissolve
    "{i}One that Mina wasn't privy to.{/i}"
    scene w3_7622 with dissolve
    fel "You two are tight-lipped!"
    scene w3_7623 with dissolve
    mc "Oh, I'm sure you have your ways of extracting tawdry details from the both of us."
    scene w3_7624 with dissolve
    "......"
    scene w3_7625 with dissolve
    "..."
    scene w3_7626 with dissolve
    "The homemaker and I, for a moment, got caught in each other's slipstreams."
    "I hadn't intended for my offhanded remark to be loaded, but Felicia flashed a dirty smile in return, and where I ended up looking wasn't her eyes."
    scene w3_7627 with dissolve
    fel "Thanks again for tonight. I might've torn that bitch's head off if you weren't there playing counterbalance."
    scene w3_7628 with dissolve
    mina "...who are you talking about?"
    fel "Huh?"
    mina "Who's the bitch?"
    scene w3_7629 with dissolve
    "For a mere instance, Mina looked temporarily withdrawn."
    scene w3_7630 with dissolve
    fel "Oh, just a blood sworn enemy of mine who we ran into at the art exhibition tonight."
    mina "I see..."
    fel "I just told you the good parts earlier."
    scene w3_7631 with dissolve
    "Felicia, catching wind of {i}something{/i}, kept it purposefully vague."
    mina "I'm glad you didn't get arrested..."
    scene w3_7632 with dissolve
    fel "Feeling left out, {i}kitten?{/i}"
    mina "That's a new one..."
    fel "It's a fitting pet name."
    scene w3_7633 with dissolve
    fel "{i}Stud{/i}, kitten, and me in the middle."
    "The emphasis she put on my portion sounded heavy and deliberate."
    scene w3_7634 with dissolve
    mina "...you're teasing me."
    fel "Come sit between us."
    mina "{i}You're teasing me.{/i}"
    scene w3_7635 with dissolve
    fel "I'd be making fun of myself if that's the case. {i}I sympathize.{/i}"
    fel "If you're between us, all our eyes will be on each other."
    scene w3_7636 with dissolve
    mina "Why would I want--"
    scene w3_7635 with dissolve
    fel "Don't play stupid, kitten. There's a time and a place for that, but not between you and me."
    scene w3_7637 with dissolve
    mina "..."
    scene w3_7638 with dissolve
    "Leave it to Felicia to set the mood."
    scene w3_7639 with cmet
    mina "......"
    scene w3_7640 with dissolve
    mina "...I've got a question, you ho."
    fel "...?"
    mina "When did you start to feel {i}solid{/i}."
    scene w3_7641 with dissolve
    fel "It's a work in progress."
    mina "...-r-really?"
    scene w3_7642 with dissolve
    fel "Everything is. You don't water a plant once and forget about it."
    scene w3_7643 with dissolve
    "Part of me wanted to crack a joke about a \"sagely slut\", but the positively maternal expression on Felicia's face put a stop to that."
    scene w3_7644 with dissolve
    mina "...it's not like I want all the attention on me."
    "Plus, it didn't feel like a platitude coming from her. {b}Hell{/b}, it even resonated with my own experience."
    scene w3_7645 with dissolve
    fel "Really? Because I do."
    scene w3_7646 with dissolve
    mina "Gosh... I got the worst fuckin' role models..."
    scene w3_7647 with dissolve
    "Mina looked back at me, and with a smile, I made sure that my attention fell squarely on her for the time being."
    mct "(Not that it was hard...)"
    scene w3_7648 with dissolve
    fel "Did you really forget what you asked me the other morning?"
    scene w3_7649 with dissolve
    mina "A...ha... heh... I was only half serious..."
    scene w3_7650 with dissolve
    fel "I'll play it off as a joke if that's what you want..."
    scene w3_7651 with dissolve
    mc "What did she ask?"
    scene w3_7652 with dissolve
    mina "......"
    scene w3_7653 with dissolve
    mina "...I was only {i}half joking{/i}, too."
    scene w3_7654 with dissolve
    fel "Green light, then?"
    scene w3_7655 with dissolve
    mina "......"
    scene w3_7656 with dissolve
    mina "...could I have another drink, please?"
    scene w3_7657 with dissolve
    mc "Sure. The same thing?"
    mina "I'll take a whiskey this time. Straight."
    mc "Thanks for keeping it simple."
    scene black with fade
    "......"
    "..."
    play sound "sound effects/handcuffs.wav"
    "A whiskey and trying to explain what the fuck a Goblin album was later--"
    stop sound
    scene w3_7658 with circlewipe
    mina "Too tight?"
    mc "Why am I the one modeling tonight?"
    scene w3_7659 with dissolve
    fel "Because we outnumber you, and you're looking like a cross between a grown-up Theodore Cleaver and a Chippendales dancer."
    scene w3_7660 with dissolve
    mc "...you could have just stopped after your first point."
    scene w3_7661 with dissolve
    fel "Do a spin."
    scene w3_7662 with dissolve
    "This was so stupid, but..."
    scene w3_7663 with dissolve
    "I was, for about two beautiful bouncy sets of reasons, in a generous and malleable mood."
    mina "I should take a picture."
    scene w3_7664 with dissolve
    mct "(It's too late to ask if these are sanitized...)"
    mina "It'll last longer..."
    scene w3_7665 with dissolve
    fel "Nothing's sexier than a good sport."

label w3FeliciaMinaFun:
    if _in_replay:
        play music "music/the-gentleman.ogg"
        show screen textbox2

    scene w3_7666 with dissolve
    mc "...you two having fun?"
    scene w3_7667 with dissolve
    minafel "{b}Yes.{/b}"
    scene w3_7668 with dissolve
    fel "You wear them well."
    scene w3_7666 with dissolve
    mc "Either of you would look even better. Anyway, so, take them off?"
    scene w3_7669 with dissolve
    "......"
    "...the two shared a transparent, duplicitous look."
    scene w3_7666 with dissolve
    mc "I'm not getting out of these that easily, am I?"
    scene w3_7667 with dissolve
    minafel "Nope!"
    scene w3_7666 with dissolve
    mc "I halfway expected that. What's the price?"
    scene w3_7670 with dissolve
    fel "Oh, about four to five honest answers should do it."
    mc "I guess I'm at the mercy of your questions..."
    scene w3_7671 with dissolve
    fel "Which one of us do you find more attractive?"
    mina "Don't ask him that!"
    fel "Sure, Mina has the advantage of age, but I'm--"
    scene w3_7672 with dissolve
    mc "That's like comparing a sunset to a sunrise. Where do you even begin to judge?"
    scene w3_7673 with dissolve
    fel "......"
    scene w3_7674 with dissolve
    fel "...good enough for you?"
    mc "It's what you're getting out of me..."
    scene w3_7675 with dissolve
    mina "I think it was an excellent answer."
    scene w3_7676 with dissolve
    fel "It was the only correct one. I don't know if I should take off or give points for the cringy imagery, though."
    scene w3_7677 with dissolve
    mc "Are we still doing the point thing...?"
    scene w3_7678 with dissolve
    fel "...{b}no{/b}. It's all analog now."
    scene w3_7679 with dissolve
    "........."
    scene w3_7680 with dissolve
    "......"
    fel "... and what are you feeling right now? What's going on in your mind?"
    scene w3_7681 with dissolve
    mc "The lyrics of a Louis Armstrong song."
    scene w3_7682 with dissolve
    fel "Take a seat, kitten. Anywhere you want..."
    scene black with fade
    fel "I've got mine picked out..."
    "After some awkward poking and prodding and guiding..."
    scene w3_7683 with fade
    "...with the imminent risk of my hands going numb, the older blonde straddled me."
    scene w3_7684 with dissolve
    mc "And the world's getting even more wonderful..."
    scene w3_7685 with dissolve
    "With Mina's eyes upon us this time, Felicia pulled me into her orbit."
    "My sexual desire swelled, and my focus fell entirely on her body."
    "The closeness of us."
    scene w3_7686 with dissolve
    "My attention shifted from her piercing blue eyes and down to her shiny wet lips."
    "--and from her smirk, I traipsed over to her neck."
    scene w3_7687 with dissolve
    "Backlit as she was, the apartment's dim lighting accentuated its allure."
    "I thought maybe it was time to give Felicia a taste, but as I teetered on that precipice between urge and action, Felicia brought Mina into our world."
    scene w3_7688 with dissolve
    fel "...take note, kitten. Where's his attention?"
    scene w3_7689 with dissolve
    mina "On your lips..."
    scene w3_7690 with dissolve
    fel "Thereabouts. As an actress, I'm sure I don't have to tell you this, but there's the magic."
    fel "The first point of contact in life, in business, and in seduction..."
    "It wasn't the first time Felicia levied this kind of pull my way..."
    scene w3_7691 with dissolve
    fel "Mmmhh..."
    "{i}It was only my hands that were tied.{/i}"
    scene fm_nekiss_a with dissolve
    show fm_nekiss with dissolve
    fel "A-aah..."
    "This was, truly, a preferable mode of action to watching Felicia squawk like a know-it-all."
    mc "*Chwup, fhwup~*"
    "And part of me wanted to show Mina that it wasn't solely Felicia's prowess fueling the moment."
    "{i}I was here too, damn it.{/i}"
    scene w3_7692 with dissolve
    mc "You know... you never told me what Mina asked."
    scene w3_7693 with dissolve
    fel "Read between the lines, stud."
    scene w3_7694 with dissolve
    "I already had, of course, but part of me wanted to tease it out."
    scene w3_7695 with dissolve
    "So I shot Mina a look that, in my imagination only, conveyed a command."
    scene w3_7696 with dissolve
    "........."
    "......"
    scene w3_7697 with dissolve
    mct "(...yeah, no. That didn't work.)"
    scene w3_7698 with dissolve
    "{i}Back on Felicia's trajectory it is.{/i}"
    mc "Mmmhh..."
    "Restrained as I was, with little leeway, I could only melt into the blonde's kiss."
    "{i}Count the seconds and endure the swelling urge to suck in air.{/i}"
    scene w3_7699 with dissolve
    "{b}Feel{/b} Mina's eyes scrutinize every small, discernable movement to our coupling."
    "Even without seeing her, her interest was known to me, hanging heavy in the air..."
    scene w3_7700 with dissolve
    fel "Mmmhh..."
    "--cloying, even."
    scene w3_7701 with dissolve
    "Mina's watchful gaze had a different feel than that of the club's patrons."
    scene w3_7702 with dissolve
    mc "*Chwup, fwhhup~*"
    "Like a cool gust of wind making the hair on my neck stand up on a humid day."
    scene w3_7703 with dissolve
    mc "Uncuff me already..."
    "Without the use of my hands, my only avenue to deprive Felicia of her little modesty was my mouth."
    scene w3_7704 with dissolve
    fel "Mmmh..."
    "...and I wasn't above ripping off her bikini with my teeth."
    scene w3_7705 with dissolve
    fel "Kitten..."
    scene w3_7706 with dissolve
    "Felicia ignored my request and fired two seductive syllables in the other direction."
    scene w3_7705 with dissolve
    fel "...what are you doing over there?"
    scene w3_7707 with dissolve
    mina "You told me to sit where I wanted."
    scene w3_7705 with dissolve
    fel "Scoot closer..."
    scene w3_7706 with dissolve
    mina "......"
    scene w3_7708 with dissolve
    mina "..."
    scene w3_7709 with dissolve
    mc "A-ahh..."
    "This time it was a double assault on MY neck and nipple."
    fel "*Cwhup, fwhhup*"
    scene w3_7710 with dissolve
    "And the shivers cascaded all the way to my toes."
    mc "A-ahh..."
    scene w3_7711 with dissolve
    fel "...any requests?"
    mina "Uh..."
    scene w3_7712 with dissolve
    mina "...j-just do it naturally?"
    scene w3_7713 with dissolve
    "There was a thick awkwardness inherent to this situation. One that Felicia and I were acclimated to, but Mina..."
    "Mina didn't verbalize it, but the uneasy way she pulled away was indication enough that she was feeling skittish. She had such lofty sexual goals, but..."
    scene w3_7714 with dissolve
    fel "Aw, beautiful..."
    fel "...head's spinning, isn't it?"
    scene w3_7715 with dissolve
    mina "D-don't tease me. Just... do what you're doing."
    mina "Pretend I'm not here?"
    scene w3_7714 with dissolve
    fel "Mmmhh, but you are here, kitten."
    scene w3_7716 with dissolve
    mina "..."
    scene w3_7717 with dissolve
    "..............."
    scene w3_7718 with dissolve
    "............"
    scene w3_7719 with dissolve
    "........."
    scene w3_7718 with dissolve
    "......"
    scene w3_7719 with dissolve
    "...I couldn't hear a single damn thing they were saying."
    "Like seriously, they weren't that far away, yet..."
    scene w3_7718 with dissolve
    mct "(That's a fuckin' skill.)"
    scene w3_7719 with dissolve
    "Now I was the one feeling awkward."
    scene w3_7720 with dissolve
    "Hands behind my back, dick half hard in a gaudy speedo while my blonde companions had a sidebar."
    "........."
    "......"
    scene w3_7721 with dissolve
    mina "Uh, I'll be right back, [mcf]."
    scene w3_7722 with dissolve
    "--and then she rushed off."
    scene w3_7723 with dissolve
    mc "...what's she doing?"
    scene w3_7724 with dissolve
    fel "A bit of a reset. I told her to go take a moment."
    scene w3_7725 with dissolve
    mc "Okay..."
    scene w3_7726 with dissolve
    fel "You'll be rewarded for your patience and understanding, stud."
    fel "All three of us will have a good time tonight. That's my goddamn mission."
    scene w3_7727 with dissolve
    mc "...so, uncuff me?"
    scene w3_7726 with dissolve
    fel "I'm going to go talk to Mina."
    fel "Peak into my bedroom in like five minutes."
    scene w3_7727 with dissolve
    mc "Sure, just uncuff me first."
    scene w3_7728 with dissolve
    fel "You won't regret it."
    mc "Wait uncuff--"
    stop music fadeout 3.0
    scene black with fade
    "Also, what room is her bedroom?!"
    mct "(Ah, fuck.)"
    "I really should have seen this coming."
    play music "music/jazz-piano-bar.ogg"
    scene w3_7729 with w24
    fel "Hey, girl."
    fel "Penny for your thoughts?"
    scene w3_7730 with dissolve
    mina "You'll want a refund."
    scene w3_7731 with dissolve
    fel "Try me."
    scene w3_7732 with fade
    "......"
    "..."
    scene w3_7733 with dissolve
    fel "I guess it was more of a yellow light, huh?"
    scene w3_7734 with dissolve
    mina "{b}God{/b} I'm stupid!"
    mina "When I heard you two were going to... well... uh... I thought I could do {i}casual{/i} too."
    mina "I'm {b}trying{/b} to do casual, but..."
    scene w3_7735 with dissolve
    fel "...it's a difficult thing."
    scene w3_7736 with dissolve
    mina "......"
    scene w3_7737 with dissolve
    mina "...watching you kiss [mcf]... I started to think of that video of Ian and those two women..."
    mina "It's ALL I could think about, actually... I got sick to my stomach."
    scene w3_7738 with dissolve
    fel "......"
    scene w3_7739 with dissolve
    fel "...I know I encouraged you to act on your impulses, but... Christ, {i}that was just a few days ago{/i}."
    scene w3_7740 with dissolve
    mina "..."
    scene w3_7741 with dissolve
    fel "Are you feeling jealous?"
    scene w3_7742 with dissolve
    mina "..."
    scene w3_7741 with dissolve
    fel "That's nothing to be ashamed of. Jealousy is normal. It's something that I've wrestled with myself, time and time again."
    scene w3_7743 with dissolve
    mina "Really? {b}You?{/b}"
    fel "Yeah, {b}me.{/b} Society doesn't wire {i}any of us{/i} for casual."
    fel "Especially for me, even. You know how greedy I can be..."
    scene w3_7744 with dissolve
    mina "Heh..."
    scene w3_7745 with dissolve
    fel "You've only slept with like, what? Two people?"
    scene w3_7746 with dissolve
    mina "You KNOW it's only two people..."
    scene w3_7747 with dissolve
    fel "Point is, the second one is handcuffed in my living room."
    scene w3_7748 with dissolve
    fel "What you're feeling is natural. Don't ignore it; {b}stare it down{/b}. Try to understand it."
    scene w3_7749 with dissolve
    fel "Why you feel what you feel isn't something you're going to unravel in a single night. You're going to have to peck away at it, over time."
    hide screen textbox2 with dissolve
    scene w3_7750 with dissolve
    fel "You know the saying... crack a few eggs, make an omelet..."
    scene w3_7751 with dissolve
    fel "........."
    mina "......"
    scene w3_7752 with dissolve
    fel "...you might even discover you don't like omelets, and that's cool too. The night is just starting and we're not going to rush anything."
    mina "Felicia..."
    scene w3_7753 with dissolve
    fel "You're safe with me dear."
    mina "Felicia... you're... I don't deserve a friend like you..."
    stop music
    fel "{b}Hush{/b}."
    scene w3_7754 with dissolve
    mina "W-what are you doing..."
    fel "You know what I'm doing..."
    play music "music/ob1.ogg"
    scene w3_7755 with dissolve
    mina "I'm just here to watch..."
    fel "There will be plenty of that. Do you find me attractive, {i}kitten{/i}?"
    scene w3_7756 with dissolve
    mina "......"
    scene w3_7757 with dissolve
    mina "...y-yeah. You're beautiful."
    scene w3_7758 with dissolve
    fel "I wasn't asking if you thought I was beautiful. I'm asking what your body is telling you to do right now."
    scene w3_7757 with dissolve
    mina "I, uh... well... y-you don't like women, do you?"
    scene w3_7758 with dissolve
    fel "I'm {i}liking{/i} the way you're blushing right now."
    scene fm_lez01_a with dissolve
    show fm_lez01 with dissolve
    mina "A-ah... w-where do you think you're touching me, s-slut..."
    fel "You trust me, don't you?"
    mina "Eeehh..."
    fel "I mean... [mcf] is one thing. He's a guy. Even at his best, he's... well..."
    mina "I trust you... you're... ah..."
    fel "Mmmmhh...?"
    mina "...you're practically the only friend I have in the world."
    fel "Is it kinda funny that I can say the same? I mean, I have \"friends\", but..."
    mina "A-ahh-♥"
    fel "No one really relies on or looks up to me, y'know?"
    mina "Haaat..."
    fel "Elias has the kids on a rotating set of nannies. You could barely call me their mother ..."
    mina "Hnnggg..."
    fel "Heheh... I just {b}knew{/b} how fat your ass would look in {i}this{/i} swimsuit..."
    mina "F-fat?! A-ahh..."
    fel "You don't think you've got a fat ass?"
    mina "It's not t-too fat, is it?"
    fel "It's {i}obscene{/i}, kitten. Any number of men, would--"
    mina "Ahh, w-whhaa... s-shut up!"
    fel "When you fucked [mcf] the other day, did he--"
    scene w3_7759 with dissolve
    play sound "sound effects/slap1.wav"
    scene w3_7760
    fel "--eh?"
    scene fm_lez01_a with dissolve
    show fm_lez01 with dissolve
    mina "Mmmhhh... y-you're teasin' me..."
    fel "This time? Ehh..."
    mina "A-aahh..."
    scene fm_lez02_a with fade
    show fm_lez02
    fel "You are right on the money, beautiful. {b}I am{/b}."
    mina "Hnnngg... o-ohh..."
    fel "Did he grab your breasts from behind like this?"
    mina "Hnnn... w-wait..."
    fel "Right before he split you open with that fuckin' log of his?"
    mina "Ghha...♥"
    fel "{i}You don't want me to wait.{/i}"
    mina "A-ahh...♥"
    fel "{i}God{/i}, you are {b}wet.{/b} You sure you're not the one who likes girls?"
    mina "T-that...!"
    fel "I wouldn't blame you, kitten."
    mina "That's not, I'm j-just...!"
    fel "I mean.... we're soft, cute... {i}and more likely to know our way around a clit.{/i}"
    mina "Aeeeuhhh, I'm just-♥"
    fel "Just a little curious...?"
    mina "A-aah... y-yeah... I g-guess...?"
    fel "Mmmmh, I've been there, kitten."
    mina "R-really?"
    fel "I don't need to ask you how you're finding it. I mean, who's the ho, now?"
    mina "W-whaa..."
    fel "{i}Bitch.{/i} You're dirtying my swimsuit."
    mina "G-gahh...♥"
    fel "A pretty expensive one, too."
    mina "Oouuuhhh...♥"
    fel "...has your curiosity been sated, dear?"
    mina "S-sated...? Ahh..."
    fel "As in, are you satisfied with just this?"
    mina "I, t-this is..."
    fel "...not enough?"
    mina "I-it's, ahh... it's... n-not...?"
    fel "You sound uncertain, dear..."
    mina "Euuugghh..."
    fel "{i}Women really need to be more vocal with their desires in the bedroom,{/i} don't you think?"
    mina "Eeugughhh..."
    fel "Especially women like us."
    mina "W-women like us...?"
    fel "{i}Hungry, carnivorous {b}bitches.{/b}"
    mina "A-aaah... I'm--"
    scene w3_7761 with dissolve
    "......"
    "..."
    scene w3_7762 with dissolve
    mina "H-hey, F-felish?"
    scene w3_7761 with dissolve
    fel "Say it."
    scene w3_7762 with dissolve
    mina "P-put your finger in..."
    scene w3_7761 with dissolve
    "......"
    scene w3_7762 with dissolve
    mina "P-please...?"
    scene w3_7763 with dissolve
    fel "Yeah, yeah, yeah~"
    mina "Haaa, hhhnnggg...♥"
    scene fm_lez03_a with dissolve
    show fm_lez03 with dissolve
    fel "Heh, thank you for asking so nicely dear!"
    mina "Eeuuugghhhh-♥"
    fel "By the end of the night, you're going to appreciate me a lot more. I'll teach your cunt just how magnanimous Felicia Ford can be."
    mina "Ah, F-felish....♥"
    fel "Hey! Sounds like you're getting there."
    mina "Hhnnyeee...♥"
    "*Schlick, fhhhlick, {b}shhliiiiiick!{/b}*"
    mina "Hhhnnngggg..."
    fel "Sing for me, beautiful."
    mina "Eutt--♥"
    fel "Sing~"
    mina "Haaat...♥♥♥"
    fel "Mmmhh, but when I'm done with you..."
    scene black with fade
    fel "...I'm going to make you do more than just {b}purr{/b}, kitten."
    stop music fadeout 3.0
    "......"
    "..."
    play music "music/sneaky-snitch.ogg"
    scene w3_7764 with fade
    "How long had it been?"
    mct "(Two minutes...?)"
    scene w3_7765 with dissolve
    "{i}No.{/i}"
    mct "(...three minutes?)"
    "To be honest, I was getting kind of pissed just sitting there."
    scene w3_7766 with dissolve
    "{i}The kind of pissed you can only get when your balls ached.{/i}"
    scene w3_7767 with dissolve
    mct "({b}Fuck it!{/b})"
    "I was nowhere near as concerned about punctuality as Felicia's husband."
    scene w3_7768 with dissolve
    mct "(...which one is her fucking bedroom again?)"
    "......"
    "..."
    "{i}You won't regret it.{/i}"
    scene w3_7769 with dissolve
    mina "Kkkhh, n-not there.."
    "Felicia's promise was proven true as traces of Mina's muffled moans penetrated the bedroom door."
    scene w3_7770 with dissolve
    fel "Sorry! I'll have every part of you, kitten."
    scene w3_7771 with fade
    mc "........."
    mc "......"
    mct "(...those bitches are having fun without me!)"
    play music "music/a-kiss-for-amanda.ogg"
    play ambient "sound effects/kissing1.mp3"
    scene fm_lez04_a with cmet
    show fm_lez04
    "...part of me felt left out, but another was in awe."
    "It's funny how certain sights can make even the most material of individuals {i}spiritual{/i}."
    "The beauty of nature."
    "Niagara Falls."
    "The Grand Canyon."
    "The Isle of Skye."
    "The sight playing out before me was such a phenomenon. An incidental thing of beauty that inspired reverence."
    mct "(Goddamn, put this shit on the roof of the Sistine Chapel...)"
    fel "*Chwwup, ffwhhup...!*"
    mina "Mmmhhh...♥"
    mct "(Glory, glory, hallelujah..)"
    "A perverse thrill tickled my gut."
    scene fm_lez04b_a with dissolve
    show fm_lez04b with dissolve
    fel "*Schwwup, chwwup, khhwwwuup~*"
    mina "Haaaa...o-ohhhh... y-you s-slut... t-talkin..."
    "It was Felicia's invitation that had placed me amidst these intimate proceedings."
    mina "T-talkin' 'b-bout meh-meee l-liking g-girls..."
    "She probably expects me to interject, but I stood firm at the door, leering in under a spell of girl love."
    fel "{b}*Shhhwup, sshmmmack-*{/b}"
    scene fm_lez04_a with dissolve
    show fm_lez04 with dissolve
    "Absorbing the sounds of blonde-on-blonde violence, parsing every little moan and lewd **POP** as if it was to be savored."
    mct "(His truth is marching on...)"
    mina "W-when you're so g-good at that..."
    fel "{b}*Shhhwup, sshmmmack-*{/b}"
    mina "R-really, {i}really{/i}, g-good--"
    fel "*Schwwup, chwwup, khhwwwuup~*"
    mina "Reallyreallyreally ghhoood at thaaaat~"
    fel "{b}*Shhhwup, sshmmmack-*{/b}"
    "Mina channeled her nervous energy into inane mutterings that Felicia paid no heed to."
    fel "*Schwwup, chwwup, khhwwwuup~*"
    "Instead, her attack on the younger blonde's perfectly puffy nipples continued unabated."
    mina "Haaa...♥"
    scene fm_lez05_a with dissolve
    show fm_lez05 with dissolve
    "...and not getting any sort of rise from Felicia, with only her pleasure to contend with, words fell away completely."
    "I imagined her focus turned within."
    "{i}The thrill of it.{/i}"
    "The taboo, confusion..."
    mina "Eeuuuhhh...♥"
    "I had no idea if Mina was genuinely bi-sexual, or even gay, but those moans were unmistakably approving."
    mina "Feeeelish...♥"
    "Her good friend was teaching her a new kind of pleasure."
    mina "F-felishh...♥"
    "There was a tenderness in the way she called out her friend's name. One that could only be found in insensate abandon."
    mina "Hhhnhnhhh...♥"
    "...but every time Mina cried out freely, my previous frustration returned."
    mina "Ghh...♥♥"
    "I was reminded of my ass on the fancy leather couch, left out in the cold."
    "{i}I remembered how I was just sitting out there, alone. {i}Unattended{/i}."
    "Selfishness surged in me. The most frustrating part?"
    mina "Feeeeeeliciaaaaa-♥"
    scene w3_7772 with dissolve
    "Mina was calling out Felicia's name instead of mine!"
    stop ambient

    menu:
        "Enough is enough: {i}interject.{/i} [mod_chat]":
            $ w3FeliciaThreesomeControl = True
            jump w3FeliciaMinaTakeControl
        "Stow your frustration. You want to see them go further."(chg=["mina_bi_up2"]):
            $ Mina_BiCurious += 2
            jump w3FeliciaMinaVoyeur


label w3FeliciaMinaVoyeur:
    scene w3_7773 with dissolve
    "...well, if her intent was for me to intrude?"
    mct "(She'll just have to wait...)"
    scene fm_lez06_a with dissolve
    show fm_lez06 with dissolve
    "{i}I wanted to see just how far the older blonde would push Mina.{/i}"
    "So I watched, Felicia's wet lips working a spell on both of us."
    mina "A-aahh...♥ Oh, {b}God{/b{!}."
    "I observed, frustration abated by Mina's delirious expression."
    mina "F-fel... F-feeel... oh, hhhh-"
    "I surveyed, as Mina teetered on the brink of oblivion."
    stop music
    scene w3_7774 with flash
    mina "O-oh, aahhhh-♥"
    "And I was there when a sudden, shrill cry signifying her {i}plunge{/i} cut through my perverted soul."
    scene w3_7776 with dissolve
    "........."
    play ambient "sound effects/kissing1.mp3"
    scene fm_lez07_a with dissolve
    show fm_lez07 with dissolve
    "...and then passion took hold and Felicia drew a mollified Mina into a kiss."
    mina "Mmmhh..."
    "A gesture of security."
    fel "*Chwup~!*"
    "Kinship."
    "{i}Affection{/i}."
    mina "Mmhhw, *chwup*, hhn...♥"
    "From my voyeuristic eyes to my bowels, the intimacy of the moment provided a {i}charge{/i}."
    "............"
    "........."
    "......"
    "..."
    stop ambient
    scene w3_7777 with dissolve
    mina "Aaa--?"
    "Felicia broke her hold, and Mina's dopey expression faded into one of hazy perturbment."
    scene w3_7778 with dissolve
    fel "......"
    scene w3_7779 with dissolve
    fel "..."
    play music "music/sneaky-snitch.ogg"
    scene w3_7780 with dissolve
    "{i}Felicia looked straight at me.{/i}"
    mc "........."
    mc "......"
    mc "..."
    "The jig was up. I was exposed."
    stop music fadeout 7.0
    scene w3_7781 with dissolve
    mina "...e-ehh? Hnnggg... Feeeeeliciaa...."
    "A cry of the utmost, {i}greedy{/i} frustration."
    scene w3_7782 with dissolve
    fel "I know that look. {i}It's not enough.{/i}"
    scene w3_7783 with dissolve
    mina "Haat... y-you started it!"
    fel "Don't you think you're getting ahead of yourself?"
    play music "music/blue-mood.ogg"
    scene fm_lez08_a with fade
    mina "Hnngg...! I k-now... I'm just here to watch..."
    "........."
    "......"
    show fm_lez08 with dissolve
    "{i}...Mina took the initiative.{/i}"
    mina "Y-you should go get [mcf]..."
    "As she spoke, all the sexual tension in Mina's body boiled over, and she shook like an anxiety-ridden poodle."
    fel "A-ahh, heh...♥"
    "And like the practiced hedonist she was, Felicia followed suit."
    fel "Mmmhh... you know.. heh... I have the {b}sneaking{/b} feeling [mcf] wouldn't mind us getting revved up without him."
    mina "A-aahh...♥"
    fel "I'm sure {i}if he was here{/i}, he might even find it {b}hot.{/b}"
    mina "Ngggg..."
    fel "You and I will both have to work hard to make it up to him though."
    mina "H-haaa!"
    fel "God! F-fuck... ah... you {i}really{/i} like the sound of that, huh?"
    mina "So do you, you fuckin' ho!"
    fel "A-aahh...!"
    "{i}That anxiety turned to aggression.{/i}"
    mina "If w-we're so alike, m-move your hips more!"
    fel "Haa...♥ H-have it your way, brat!"
    mina "Heeeuugh...♥"
    "Both blondes moaned without restraint."
    minafel "Yeeeeeahhh...!"
    scene fm_lez08b_a with dissolve
    show fm_lez08b with dissolve
    "Grunting and crying out in unison."
    "As I watched them writhe, I tried to be patient."
    mina "Mmmhhh...!"
    "I tried to play the good little voyeur."
    fel " M-more!"
    "As I watched Felicia's own greediness show its face, part of me delighted in the denial."
    mina "Feelhhh...♥"
    "{i}In the twisted anticipation of it all.{/i}"
    mct "(The things I'd do to the both of them...)"
    "Patience fueled my perversion, but only a small part of me. The overwhelming part of me?"
    mct "(God, I wish I could jerk off right now!)"
    scene w3_7784 with dissolve
    mc "A-ahem... you... got the keys to these things?"
    scene w3_7785 with dissolve
    "With the sound of my voice, the writhing stopped."
    scene w3_7786 with dissolve
    mina "[mcf].. eheh.. u-uh... h-hey, unm..."
    scene w3_7785 with dissolve
    "The writhing stopped and shame {i}instantly{/i} spread across Mina's perfect face."
    scene w3_7787 with dissolve
    "........."
    "......"
    scene w3_7788 with dissolve
    mina "...uh, d-did you find that hot?"
    scene w3_7787 with dissolve
    "Mina's face turned crimson, adding to my arousal."
    scene w3_7789 with dissolve
    mc "I'm about to fucking die here, girls..."
    scene w3_7790 with dissolve
    fel "I don't think I'd be able to explain a corpse..."
    scene w3_7791 with dissolve
    fel "...I guess someone better take care of that then."
    scene w3_7792 with dissolve
    mina "I..."
    scene w3_7793 with dissolve
    fel "That was rhetorical. {i}You watch.{/i}"
    "Slowly, Felicia eeked toward me, and..."
    play ambient "sound effects/fel4.wav"
    scene black with fade
    mc "Uncuff me first?"
    fel "*Chwup- A-ahh... heh... do you really want me to get up right now?"
    mc "...on second thought, just {b}suck my dick.{/b}"

    if feliciaDaddy == True:
        fel "Sure thing, {i}daddy{/i}."
    else:
        fel "{i}Those{/i} are the magic words."


    scene fm_ts01_a with fade
    show fm_ts01 with dissolve
    "I'd say this..."
    fel "*Cwhup, fwhhup~♥"
    "Felicia's annoying glibness?"
    mc "A-ahh...♥"
    "...while a poison, was remedied beautifully by her knob polishing, even at this awkward angle."
    "........."
    "......"
    "...or maybe {b}especially{/b} at this awkward angle."
    "The sight from above, of Felicia's golden scalp bobbing up and down, while Mina attentively watched..."
    mc "O-ohh... ah..."
    "...it filled me with a sense of primacy that outweighed my restraints..."
    fel "*Cwhup, fwhhup-♥"
    mc "Ehh... how's the view, {i}kitten?{/i}"
    mina "Oh, not you too..."
    mc "Heh... just wanted to--"
    fel "*Cwhup, fwhup, chwwupp-♥"
    mc "-try it on for size."
    mina "Uh, huh... yeah... {i}s-stud{/i}."
    fel "Mmhhh, mmhhh...♥"
    mc "She likes an audience, y'know..."
    mina "A-ah... yeah... {i}I know...{/i}"
    fel "Mmmh, euuch... *Chwup-♥*"
    mc "It's a bit more intense than a kiss, right? Ah... uhh..."
    "I recalled earlier."
    mc "...y-you alright?"
    "She wasn't going to run off again, was she? I'd die of blue balls if she did..."
    mina "Y-yeah... I'm, uhh..."
    stop ambient fadeout 3.0
    scene w3_7794 with dissolve
    "........."
    scene w3_7795 with dissolve
    "......"
    scene w3_7796 with dissolve
    mina "...{i}fuck{/i}."
    scene w3_7797 with dissolve
    "Arousal was plain as day on Mina's lovely face."
    mc "Good, because I like you watching too..."
    scene w3_7798 with dissolve
    mina "That, uh..."
    scene w3_7797 with dissolve
    fel "Euuch, hhnnk- *Fwhhup-♥"
    scene w3_7798 with dissolve
    mina "...that's a safe {i}nooooooo {b}crap.{/b}{/i}"
    scene fm_ts01_a with dissolve
    show fm_ts01 with dissolve
    "I had been exceedingly lucky lately, but this..."
    mc "A-ahh-"
    "Even a young, inexperienced woman like Mina had this pegged as the luckiest day of my life."
    mc "Heh, y-yeah..."
    fel "Euuch, *chwup-*"
    mc "...nooooooo {b}crap{/b}. Hhha-"
    fel "Mmmhh.... hhmmmm...♥"
    "Felicia purred contentedly alongside our inane banner."
    mc "You know what else Felicia would like? She'd {b}love{/b} to hear what you're feeling right now."
    mina "I'm... feeling... uh..."
    fel "*Cwhup, fwhhup-♥ Euugghh...!"
    mina "...this is the first time I've seen it from this perspective outside of the video. Heh."
    fel "*Cwhhup, fwhhhuhp~* Mmhmhh..."
    mina "L-lotta firsts, actually... how much did you see of me and Fel--"
    mc "Aha... q-quite a bit."
    fel "*CWhhup-♥"
    scene w3_7799 with dissolve
    mina "Oh, uhh... I hope you're not feeling--"
    scene w3_7800 with dissolve
    mc "{b}It's cool.{/b}"
    scene w3_7801 with dissolve
    mina "O-ohh..."
    scene w3_7802 with dissolve
    "...she looked kinda disappointed?"
    mc "You looked lovely. {b}You were glowing.{/b}"
    scene w3_7803 with dissolve
    mina "O-ohhh..."
    scene fm_ts01_a with dissolve
    show fm_ts01 with dissolve
    "While we talked, Felicia worked my little head with a slow, agonizing purpose."
    mc "Hnnnhh..."
    "Every fiber of my being wanted to grab and impale her deeper, but alas..."
    mct "(God damn it...)"
    mina "...y-you look frustrated? Doesn't it feel good?"
    mc "Well, uhh..."
    mc "She's playing with her food."
    mina "Oh..."
    scene w3_7804 with dissolve
    mina "Hey, Felicia, ummm..."
    scene w3_7805 with dissolve
    "As she processed what I was feeling, Mina looked {i}hilariously{/i} concerned."
    scene w3_7804 with dissolve
    mina "S-speed up, some?"
    scene w3_7805 with dissolve
    "{i}God, she was cute.{/i}"
    scene w3_7804 with dissolve
    mina "{b}Feeelicia{/b}, c-come on!"
    scene w3_7805 with dissolve
    "Even as a passive observer, she was taking an active interest in my pleasure."
    scene fm_ts01b_a with dissolve
    show fm_ts01b with dissolve
    mc "Ha! Hahaha!"
    mina "W-what?"
    mc "You're fucking adorable, you know that?"
    mina "O-oh..."
    "{i}Oh, again.{/i}"
    "...and the older blonde? What could she do but acquiesce that cuteness as well."
    fel "Euuchh, hhmmm... *Cwhup-♥"
    "She did indeed speed up."
    fel "*Chwwup-♥"
    "Seems neither of us were immune to Mina's charms."
    fel "Euche- *Cwhhiip-♥*"
    "{i}That much was obvious by the way they were going at it before.{/i}"
    fel "*Cwhup, fwhhup-*"
    "...and the way Mina was peering up at me, tits out?"
    fel "Mmhhh... *cwhhhup-♥*"
    "...with a serene and filthy look on her face?"
    "{b}Fuuuuuuuuuuck.{/b}"
    "Felicia had picked up the pace, but I was still unsatisfied."
    mina "[mcf]..."
    "I wanted violent, unrestrained rutting."
    mc "Ghhhh..."
    "{i}Greed{/i} filled me, and I wanted much more than what I was getting."
    mina "You look so... aheh... {i}oh, fuck.{/i}"
    "Again with the cutesy 'fucks'."
    stop music
    scene w3_7806 with vpunch
    mc "O-okay that's enough!"
    scene w3_7807 with dissolve
    fel "...?"
    scene w3_7808 with dissolve
    fel "Chwup* Hmmm....?"
    mc "Get these cuffs off me!"
    play music "music/rockville.ogg"
    scene w3_7809 with dissolve
    "I knew, for a fact, she was already warmed up."
    scene black with fade
    mina "...what, what should I do?"
    mc "Just--"
    jump w3FeliciaMinaMuffDiving


label w3FeliciaMinaTakeControl:
    scene w3_7828 with dissolve
    mc "Hey, Girls...?"
    scene fm_lez06_a with dissolve
    show fm_lez06 with dissolve
    mc "*Ahem* Girls...?"
    mina "A-aahh...♥ Oh, {b}God{/b{!}."
    "My voice didn't quite reach them. They were off in their own little world at the moment."
    mina "Hhnnng-- hhaaaa...♥"
    "{i}Not that I could blame them, but...{/i}"
    scene w3_7810 with dissolve
    stop music
    play sound "sound effects/record-scratch.wav"
    with vpunch
    mc "Hey, horny bitches!!"
    mina "I--"
    "........."
    scene w3_7811 with dissolve
    "......"
    "..."
    scene w3_7812 with dissolve
    fel "There you are."
    mina "I w-was about to, uhh... euhhh..."
    play music "music/dont-fret.ogg"
    scene w3_7813 with dissolve
    "Felicia was, naturally, much more composed than her friend."
    scene w3_7814 with dissolve
    fel "...has it been five minutes already?"
    scene w3_7815 with dissolve
    mc "Beats me."
    scene w3_7813 with dissolve
    mina "Uhh..."
    scene w3_7816 with dissolve
    "It took Mina quite a few blinks to see through the pleasurable murk clouding her consciousness."
    scene w3_7817 with dissolve
    mina "[mcf], I, uhh... h-how long were you--"
    scene w3_7818 with dissolve
    mc "Long enough to hear you cry Felicia's name. {i}A whole bunch.{/i}"
    scene w3_7817 with dissolve
    mina "Oh, heh... umm..."
    scene w3_7816 with dissolve
    "...and quite a few more blinks for her brain to finally fire back up and default to shame."
    scene w3_7817 with dissolve
    mina "I, uhh- um... eheh... I hope you're not jealous..."
    scene w3_7816 with dissolve
    "{i}She almost sounded hopeful.{/i}"
    scene w3_7818 with dissolve
    mc "You left me on the couch, all by myself. Jealousy wouldn't be the word for it..."
    scene w3_7819 with dissolve
    fel "What? Spying on two hot blondes getting it on isn't a good pittance?"
    scene w3_7820 with dissolve
    "...no, the {i}phrase{/i} for it would be horny out of my gourd and looking to fuck."
    scene w3_7821 with dissolve
    mc "I want more than a pittance."
    scene w3_7819 with dissolve
    fel "Heheh, seems we're {i}all{/i} greedy, greedy tonight."
    scene w3_7821 with dissolve
    mc "Get these cuffs off me."
    scene w3_7822 with dissolve
    fel "...and then what? You gonna punish us?"
    mina "P-punish...? U-us?"
    scene w3_7821 with dissolve
    mc "First things first..."
    scene black with fade
    play sound "sound effects/handcuffs.wav"
    "I felt the world at my feet."
    stop sound
    mc "{b}You.{/b} Come here!"
    mina "Uhhh..."
    scene w3_7823 with fade
    mina "What are you...?"
    scene w3_7824 with dissolve
    "Through an eye roll, Felicia obliged my request to bend over. I suppose she wanted to see where I was taking this."
    scene w3_7825 with dissolve
    mc "I interrupted just as things were about to get {i}good{/i}, didn't I?"
    scene w3_7823 with dissolve
    mina "Ummm... ah--"
    scene w3_7825 with dissolve
    mc "You know exactly what I mean. You were..."
    scene w3_7826 with dissolve
    mc "...you were about to {i}peak{/i}."
    mina "Aaaah...♥"
    scene w3_7827 with dissolve
    "It was amazing just how submissive Mina was."
    scene w3_7829 with vpunch
    mina "Ehh..."
    "Felicia had her primed. All I needed to do to make her eyes roll back was to tease a nipple."
    scene fm_ts02_a with dissolve
    show fm_ts02 with dissolve
    mc "Must be... {i}frustrating{/i}."
    mina "O-ohhh...♥"
    mc "Must be really, {i}really{/i} frustrating..."
    mina "Euuhhh... k-kinda...?"
    mc "You didn't get to cum."
    mina "That's... uh... that's okay. I'm just here to watch."
    mc "Let's pretend for a moment that's true, that we're not already well beyond that..."
    mina "Aeuuh... y-yeah?"
    mc "Would you be satisfied with that?"
    "Mina didn't even have to think about it. She was nodding to the contrary before I had even finished my last syllable."
    scene w3_7830 with dissolve
    fel "Hey, I'm getting--"
    scene w3_7831 with dissolve
    mc "Bitches who leave their guests blue balled and handcuffed so they can lez out don't get to complain!"
    scene w3_7832 with dissolve
    fel "Uhhh..."
    "I said it, as convincingly as I could muster."
    "......"
    "..."
    scene w3_7833 with dissolve
    "The world was indeed at my feet, and God help me, I was going to act like I was entitled to it."
    scene w3_7834 with dissolve
    mc "Whose lips do you prefer wrapped around your tits?"
    scene w3_7835 with dissolve
    mina "{b}Y-you are jealous!{/b}"
    "Again, jealousy wasn't the word for it."
    scene w3_7836 with dissolve
    mc "Kiss me."
    scene w3_7837 with dissolve
    "...was it competitiveness?"
    scene fm_ts03_a with fade
    show fm_ts03
    "God help the young blonde, as malleable as she was, caught between two perverts like us."
    mina "Mmmhhh...♥"
    mct "(She does smell like coconut...)"
    "Felicia got her started, but I was taking Mina back."
    mina "Mmhh, *cwhuhp-*"
    "And what of Felicia, face down and ass up just over Mina's shoulder?"
    mina "Eehhh... *Cwhup*"
    "She was right where she belonged."
    mina "*Cwhup, fwhhup!*"
    "{i}All was right with the world.{/i}"
    "........."
    "......"
    "..."
    scene w3_7838 with dissolve
    mina "Eugghhhh... [mcf]... I want to..."
    scene w3_7839 with dissolve
    mc "On the bed."
    stop music fadeout 3.0
    scene black with fade
    "It's funny how certain sights can make even the most material of individuals {i}spiritual{/i}."
    scene w3_7840 with dissolve
    "The Great Barrier Reef."
    "Yellowstone."
    "The Amalfi Coast."
    scene w3_7841 with dissolve
    "{i}This shit, man.{/i}"
    "........."
    "......"
    "..."
    play music "music/happy-clappy.ogg"
    scene w3_7842 with dissolve
    play sound "sound effects/slap3.wav"
    scene w3_7843 with vpunch
    minafel "O-aah..?!"
    scene w3_7842 with dissolve
    "Two blondes with beautiful, bouncy asses lined up like a set of bongos begging to be played."
    scene w3_7844 with dissolve
    play sound "sound effects/slap4.wav"
    scene w3_7845 with hpunch
    mina "G-gahh-♥"
    mc "Bitch!"
    scene w3_7844 with dissolve
    "The unassailable majesty of the moment begged the question."
    play sound "sound effects/slap4.wav"
    scene w3_7846 with hpunch
    fel "O-eeuuhh!"
    mc "Fuckin' beautiful!"
    scene w3_7844 with dissolve
    mct "(...how the hell am I going to satisfy {i}two{/i} women?)"
    "......"
    mct "(...eh, I just won't think about it.)"
    scene w3_7842 with dissolve
    play sound "sound effects/slap3.wav"
    scene w3_7843 with vpunch
    minafel "Gee-ahh..?!"
    scene w3_7847 with dissolve
    mc "Sorry, feelin' like a kid in a candy store right now."
    "{i}Hopefully it'll work out.{/i}"
    stop music
    play sound "sound effects/surprise.wav"
    scene w3_7848 with vpunch
    mina "Euugghh...?!"
    "Plowing on without restraint, a manic energy took hold, and I slipped my fingers into whatever holes they could fit."
    play sound "sound effects/surprise.wav"
    scene w3_7849 with vpunch
    fel "W-whoa, {b}s-shit!{/b}"
    play music "music/higher-octane.ogg"
    scene fm_ts04_a with flash
    show fm_ts04
    mina "Gg---ahh..? {i}A-asss...?!?{/i}"
    "{i}Go for the gusto!{/i}"
    mc "Thanks for indulging me, girls!"
    mina "W-whooaaa...!"
    mc "Goddamn it, it feels g-good to be alive!"
    fel "H-haa! I thought you were upset!"
    mc "You kidding?!"
    fel "You--"
    scene fm_ts04b_a with dissolve
    show fm_ts04b with dissolve
    "*Schlick, fwhhhip-!*"
    fel "You f-fucker!"
    mina "O-ohhh, s-shiiit--"
    mc "Ha! You fuckin' kidding?"
    mina "EEuuhhhh...?! Ww---aaahhh...♥"
    scene fm_ts04_a with dissolve
    show fm_ts04 with dissolve
    mc "Listen to her fuckin' wail!"
    mina "Aaah, hhhnngggg...♥"
    "Hard and fast, {i}violent{/i}, with no concern for tempo."
    mc "Lined up like a pair of bitches."
    "No nuance, no play, just overwhelming stimulation."
    scene w3_7850 with dissolve
    play sound "sound effects/slap3.wav"
    scene w3_7851 with hpunch
    "{b}*Fwwwap!*{/b}"
    minafel "G-aahh-!"
    scene w3_7852 with dissolve
    mc "How could I be upset about any of it?!"
    mina "W-what the--"
    scene w3_7853 with dissolve
    play sound "sound effects/slap4.wav"
    scene w3_7854 with hpunch
    "{b}*Fwhhaap-!*{/b}"
    mina "Oooh-hhh-♥"
    scene w3_7855 with dissolve
    mc "Howl like a fucking dog, you bitch!"
    mina "Aaaaaaahhh-♥"
    scene fm_ts04b_a with dissolve
    show fm_ts04b with dissolve
    mc "Dirty fucking whores!"
    minafel "Ehhuhuuhh...?!"
    mct "(...she did say being treated like this was on her list, right?)"
    minafel "Eguuuuhhh...!"
    mct "(...y-yeah... that's a good excuse as any for doing what I feel like, right?)"
    scene w3_7856 with dissolve
    scene w3_7857 with dissolve
    play sound "sound effects/slap4.wav"
    scene w3_7858 with vpunch
    mc "Golddigging bitch!"
    fel "S-shit...!"
    mct "(...and Felicia is getting swept along with the inclination.)"
    scene fm_ts04_a with dissolve
    show fm_ts04 with dissolve
    minafel "Eeuuhhhh...♥"
    "The pair cried out in unison and it was a beautiful symphony."
    minafel "Eeuugughhh...♥"
    mc "Howl!"
    minafel "Euughhh...?!♥♥♥"
    mc "Howl!"
    fel "Whhe--"
    scene w3_7850 with dissolve
    play sound "sound effects/slap3.wav"
    scene w3_7851 with vpunch
    mc "Howl!"
    mina "Uh, w-weee--"
    scene fm_ts04b_a with dissolve
    show fm_ts04b with dissolve
    mc "Dirty cunts!!"
    minafel "Whhuugg--♥"
    mc "Ha! Haha!"
    mct "(Oh, fuck it's beautiful... {b}GODDAMN IT!{/b})"
    minafel "Euugghh...!"
    "{i}These two, wonderful, sisterly sluts.{/i}"
    scene fm_ts04_a with dissolve
    show fm_ts04 with dissolve
    minafel "Eugughhh..."
    mc "Moan for me!"
    minafel "Eegguhhh...♥"
    mct "(I wouldn't have a problem dying after this...)"
    mc "{b}Howl!{/b}"
    minafel "Ehhuhhooo...♥♥"
    mina "Oh, fuck I'm going to-"
    scene w3_7853 with dissolve
    play sound "sound effects/slap4.wav"
    stop music
    scene w3_7859 with hpunch
    mc "Cum, puppy!!"
    mina "{b}Geyyyeeehhhhhhhhhhhh....!{/b}"
    "I pushed Mina out of the goddamn window and into an orgasm with one last spank."
    scene w3_7860 with dissolve
    mina "Ohohhhh, d-damnieeehhttt....! A-aahh, ohhh... f-fuck..."
    play music "music/anacaptainslogue.ogg"
    scene fm_ts05_a with fade
    show fm_ts05
    mina "O-hhh, ohhh fuck... what the..."
    mc "{i}I've got you.{/i}"
    "Quickly I scooped Mina up, taking ownership of her, as every wrinkle in her brain was smoothed over in a fit of pleasure."
    mina "Euheehh...! W-wwaahh...!"
    mc "{i}You're alright.{/i}"
    mina "Nnhheeeyyy, awhhh...."
    mc "Just ride it out, beautiful."
    mina "W-whatt theee..."
    mc "{i}I've got you.{/i}"
    mina "Eeuugghh... wwhhaa, that was..."
    mc "{i}Take your time coming down.{/i}"
    stop ambient fadeout 3.0
    scene w3_7861 with dissolve
    mina "Haaahaaa... [mcf]... I don't know if..."
    scene w3_7862 with dissolve
    "........."
    "......"
    stop music fadeout 3.0
    scene w3_7876 with pixellate
    mct "(Heh...)"
    "I had Veronica to thank for showing me how effective this approach could be."
    scene w3_7862 with pixellate
    "Of course, it probably had more to do with Mina's receptiveness than anything on my end."
    scene w3_7863 with dissolve
    mina "...I don't know if I liked that?"
    scene w3_7864 with dissolve
    mct "(Felicia on the other hand...)"
    scene w3_7865 with dissolve
    fel "I'd say the result speaks for itself."
    scene w3_7864 with dissolve
    "Getting one out of the two to climax wasn't so bad."
    mina "Heh, y-yeah... w-wow..."
    scene w3_7866 with dissolve
    fel "Well, you seemed to have fun. Did that make up for leaving you all by your lonesome?"
    scene w3_7867 with dissolve
    mc "Oh, {i}I'm just getting started.{/i}"
    scene w3_7868 with dissolve
    fel "...do you actually think you can handle the both of us?"
    scene w3_7867 with dissolve
    mc "What are you, {b}blind?{/b}"
    play music "music/rockville.ogg"
    scene w3_7869 with dissolve
    mina "E-eehh...?"
    mc "I didn't even have to use {i}this.{/i}"
    scene w3_7870 with dissolve
    fel "My, my, you're getting confident..."
    scene w3_7871 with dissolve
    mc "Tell Felicia who made you cum."
    mina "Ummmmmmm..."
    "Mina momentarily didn't seem like she parsed the question."
    scene w3_7872 with dissolve
    mina "Y-you did..."
    scene w3_7873 with dissolve
    mc "You're goddamn right I did - and after I fuck Felicia, {i}and make her cum...{/i}"
    scene fm_ts06_a with dissolve
    show fm_ts06 with dissolve
    mc "...you better saddle up for round two."
    mina "Hhhgeehh..."
    mc "And do you want to know how the night ends?"
    mina "E-ehh...?"
    mc "You're both going to reward my hard work by drinking my cum and not spilling a single. {i}Fucking{/i}. {b}Drop.{/b}"
    "To be honest..."
    mc "Sound good?"
    mc "Yeah, that's right..."
    "...to be honest, as I enjoyed Mina's lewd affirmation of my bullshit, this situation felt beyond me."
    scene w3_7874 with dissolve
    mc "Seems Mina likes that plan. How 'bout you, Felicia?"
    scene w3_7875 with dissolve
    "I didn't feel like myself, but lest it slip away..."
    scene w3_7877 with dissolve
    fel "I think..."
    scene w3_7875 with dissolve
    "...all I could do, so to speak, was act like I belonged."
    scene w3_7877 with dissolve
    fel "...I think you should put your money where your mouth is."
    scene w3_7878 with dissolve
    mc "Is that opposed to you putting your mouth where the money is?"
    scene w3_7879 with dissolve
    mina "Pffhhh-!"
    scene w3_7880 with dissolve
    fel "...just get the fuck over here, stud! You're getting annoying!"
    mc "What? You told me to be confident."
    scene w3_7881 with dissolve
    fel "Yeah, and I'm creating a monster - and you too, {i}puppy{/i}."
    scene w3_7882 with dissolve
    mina "H-huh?"
    scene w3_7881 with dissolve
    fel "You ain't just staring slack-jawed, alright? No time to pick up your brains. Get over here!"
    scene black with fade
    mina "...w-wait a moment. W-what was that accent just now?"
    "...and, after some scrambling--"
    jump w3FeliciaMinaMuffDiving

label w3FeliciaMinaMuffDiving:
    scene w3_7883 with fade
    fel "...I'm starting to think this is how you like me best."
    scene w3_7884 with dissolve
    mina "Hehe, well, {i}you do have a fat ass.{/i}"
    scene w3_7885 with dissolve
    fel "...excuse me?"
    mina "I mean, w-we both do!"
    scene fm_ts07_a with dissolve
    show fm_ts07 with dissolve
    mc "She's not wrong..."
    "Growing impatient, I began teasing Felicia."
    fel "A-ah... I prefer the term {i}perfectly plump.{/i}"
    mina "Of course you do, you narcissistic ho."
    fel "Mmmh, oh f-fuck..."
    mc "You watching, Mina?"
    mina "Uh, huh, what else would I--"
    mc "Keep your eyes peeled~ I want you to take a gander at what your best friend looks like when she's {i}thoroughly{/i} fucked."
    scene w3_7886 with dissolve
    mina "I..."
    scene w3_7887 with dissolve
    "There was anticipation within her pause."
    scene w3_7886 with dissolve
    mina "I won't look away..."
    scene w3_7887 with dissolve

    if w3FeliciaThreesomeControl == True:
        mc "Good, because what you're about to see is what you looked like five minutes ago."
        scene w3_7888 with dissolve
        "........."
        "......"
        scene w3_7889 with dissolve
        mina "...s-show me, [mcf]."
    else:
        scene w3_7890 with dissolve
        mina "...you'd like that, right?"
        scene w3_7891 with dissolve
        fel "There's nothing more that I want right now than for you to see this part of me, {i}kitten{/i}."
        scene w3_7892 with dissolve
        "........."
        "......"
        scene w3_7890 with dissolve
        mina "...s-show me, {i}please.{/i}"
        scene w3_7892 with dissolve
        "{i}Neither of us could resist Mina's charms.{/i}"

    scene fm_ts08_a with dissolve
    show fm_ts08 with dissolve
    fel "A-aahhh, h-here--"
    "...and with a roll of my hips, I pushed forward."
    fel "-it goes!"
    "There was no need to take it slow with Felicia."
    fel "Mmhmhhh...♥"
    "She devoured my length, effortlessly, all the way to the hilt."
    fel "See this shit, kitten? Aeeuuggh-♥"

    if w3FeliciaThreesomeControl == True:
        fel "Not that I need to tell you, but this bastard is a real animal!"
        "Felicia's words only encouraged me to fuck her harder."
        scene w3_7893 with dissolve
        play sound "sound effects/slap4.wav"
        scene w3_7894 with hpunch
        fel "-nnhnhhhh!"
        mc "You would know one, bitch!"
        scene fm_ts08_a with dissolve
        show fm_ts08 with dissolve
        fel "Eeugghh, hehe...♥ I knew that was coming... hehe..."
    else:

        fel "The man you're crushing on is a goddamn animal!"
        "Felicia's words only encouraged to fuck her harder."
        mc "It takes one to know one."
        fel "Mmmmhhhh...♥"

    "Mina, from the moment I pried Felicia's pussy open, was transfixed on the scene."
    fel "Heeeh...♥ God, {i}look at me{/i}, kitten."

    if w3FeliciaThreesomeControl == True:
        "Any compunction the young nympho had about our ménage à trois had been finger fucked out of her."
    else:
        "Any compunction the young nympho had about our ménage à trois had been coaxed out of her by Felicia."

    scene fm_ts08b_a with dissolve
    show fm_ts08b with dissolve
    mina "Huh...."
    "She read every minute change in the older blonde's expression like it would be on the quiz."
    mina "You look..."
    "Every time I pulled back, she scrutinized the lines of longing on Felicia's face."
    fel "S-say it... t-tell me..."
    "Every time I skewered the older slut with my dick, Mina's eyes went wide processing her friend's animal glee."
    mina "You look {i}so{/i} lewd, yet..."
    fel "Y-yet...?"
    mina "...you look {i}so{/i} beautiful."
    fel "W-whatt..? Ha! Hnggg..."
    "Mina's compliment took her fellow blonde off guard."
    fel "T-that's what you're thinking? In this situation, a-ahh...?"
    mina "You're glowing..."
    mc "That's because she's in her element!"
    fel "Ahh, hhhaaa...♥"
    mc "You'll make her cum from just watching."
    mina "...{i}I-I will?{/i}"
    mc "Yeah, {i}you.{/i}"
    scene fm_ts08c_a with dissolve
    show fm_ts08c with dissolve
    fel "Aahhh, eehhh-♥"
    mc "You're getting her off, {i}kitten{/i}."
    fel "Ooo-hhhh, ohhh...♥"
    mina "...I'm just sitting here."
    mc "No shit, it's probably doing a better job than I am! A-ah--"
    "{i}Shit! Felicia was so fucking tight right now.{/i}"
    mc "You might think you have an idea, but having someone she loves and respects watch her?"
    fel "S-shut up, [mcf]!"
    mc "I bet it takes it to the next level!"
    mina "Oh God, she's so cute..."
    "{i}It was funny how that last part was what she seemed to be denying...{/i}"
    mc "She's clinging to me like a glue trap! {i}Dirty fucking slut!{/i}"
    fel "Ohh, hhnn...♥ Oh, fuck!"
    scene fm_ts08b_a with dissolve
    show fm_ts08b with dissolve
    "As usual, pointing out her depravity proved to be {i}honey{/i} to the horny blonde."
    mina "...does that mean I'm getting you off too?"
    mc "What do you think?"
    mina "Ohhhh... uh... {i}heh{/i}..."
    "{i}Mina seemed particularly thrilled by that angle.{/i}"
    fel "Hhhhhh... he's s-so fucking hard, k-kitten."
    scene fm_ts08_a with dissolve
    show fm_ts08 with dissolve


    if w3FeliciaThreesomeControl == True:
        mc "So don't even THINK of fucking blinking, got it?"
        "And with that missive, I fell into a rhythm."
        "A thunderous, abject rut of a rhythm with the sole goal of delivering Felicia to the same oblivion Mina had just experienced."
        fel "Ahh-aah!"
        mct "(Turn this bitch into mush!)"
    else:

        mc "Don't even dream of blinking, beautiful!"
        fel "Haaaa...♥"
        "And with that missive, I fell into a rhythm."
        "A thunderous, abject rut of a rhythm with the sole goal of throwing Felicia head first into oblivion."

    "No more thought of Mina's gaze."
    fel "Oh, d-damn it!"
    "Only of the sensation of my nuts slapping against Felicia's clit, of the nigh inescapable squeeze of her cunt."
    fel "Oh, fuck!"
    "Of her expletive-ridden moans, and the firm give of her sculpted {i}perfectly plump{/i} ass."
    fel "Haa, hhaaa-♥"
    "For the gold-digging wife to sing the tune I wanted, those were the only things I could allow myself to be enslaved by."
    fel "Ohhh, ffuuuuuucckk, [mcf]-♥"
    scene w3_7893 with dissolve
    play sound "sound effects/slap4.wav"
    scene w3_7894 with hpunch
    mc "A-aahh! S-shake your ass more!"
    scene fm_ts08c_a with dissolve
    show fm_ts08c with dissolve
    "If I wanted to turn Felicia into mush, then all I had was instinct."
    "A weak demand."
    fel "A-aaahh...♥"
    "A {i}pointless{/i} demand."
    fel "Ahh, w-whatever you want!"
    "Felicia was in her element, and the fervent way she bucked back into me left {b}no{/b} room for improvement, but still..."
    mc "You want to cum?! Work for it!"
    "...but still I reprimanded her."
    scene w3_7893 with dissolve
    play sound "sound effects/slap4.wav"
    scene w3_7894 with hpunch
    mc "Shake your fucking hips! Show Mina what you really are!"
    scene fm_ts08_a with dissolve
    show fm_ts08 with dissolve
    fel "F-ffuccckk... o-okay!"
    "...and she lustily deferred to my vanity."
    fel "F-fuucuccckk--"
    scene w3_7893 with dissolve
    play sound "sound effects/slap4.wav"
    scene w3_7894 with hpunch
    mc "Fuckin' move it!"
    scene fm_ts08_a with dissolve
    show fm_ts08 with dissolve
    fel "A-ahhh...♥ S-shi--"
    "The sickness in my soul churned."
    mc "Show me..."
    scene w3_7893 with dissolve
    play sound "sound effects/slap4.wav"
    scene w3_7894 with hpunch
    mc "Show why I shouldn't be fucking Mina right now instead!"
    scene fm_ts08_a with dissolve
    show fm_ts08 with dissolve
    fel "Ahh... ahhh- o-ohhh--"
    mc "Or should I just switch?!"
    "{i}I may have been getting lost in a fantasy of my own making...{/i}"
    scene w3_7895 with dissolve
    mc "Maybe I'll handcuff you and just let you {b}stew!{/b}"
    scene w3_7896 with dissolve
    mina "H-holy shit... w-woah..."
    scene w3_7897 with dissolve
    "........."
    "......"
    scene fm_ts08d_a with dissolve
    show fm_ts08d with dissolve
    mct "(...oh, fuck. When did she...?)"
    "Mina threw a wrench in my plans and drew my focus back on her."
    mina "A-aahh...♥"
    "Somewhere during my stupor, the budding slut had provocatively spread her legs and proffered a clear view of her honeypot."
    mina "O-ohhh...♥ W-what am I doing?"
    "Her hands traveled her sex without shame."
    mina "O-oh, h-hell... l-look at me, too, g-guys... a-ahh..."
    fel "F-fuck that's hot...!"
    "Felicia's heart and body were in complete alignment, as the stimulus before her eyes sent her into milking-my-cock overdrive."
    mina "D-do me n-neeeeeeext, eh? [mcf]... Felicia... Haaaa...♥"
    "And as absent-minded as she seemed, Mina chose her words carefully."
    mina "I w-want Felicia to watch m-me.. t-tooooooOOOOooo...♥"
    "Targeting both of us with language that would spur on our desires."
    mc "Oh, God, you're a fuckin' natural..."
    mina "Hehe, why... do you guys keep saying that... hmmm...?"
    "The cutesy, clumsy way she tripped over her words ceased, as if being possessed by a spirit of beguilement."
    fel "O-ohhh, hhhaaa...♥ {b}FUCK!{/b}. P-play with yourself for me, kitten."
    fel "M-masturbate to me! O-ohhh...♥"
    scene fm_ts08c_a with dissolve
    show fm_ts08c with dissolve
    "{i}Felicia was REALLY into this dynamic...{/i}"
    mina "I'm dirty, I'm so fucking... a-ahhh...♥"
    fel "Fuck yes, you are! FUCK YES, YOU ARE."
    "She was really, REALLY into this dynamic."
    mina "Aa, hhnhnn-♥ Ohh-♥ T-this is insane! I'm out of my mind, but oh, you two--!"
    scene w3_7898 with dissolve
    play sound "sound effects/slap4.wav"
    scene w3_7899 with hpunch
    mc "Come on!"
    scene fm_ts08c_a with dissolve
    show fm_ts08c with dissolve
    mina "O-oahhhh, eeeuuggghhh..."
    fel "Euugghhh... y-you act so pure..."
    mina "O-ohhh...♥♥♥"
    fel "Y-you went to your rich bitch school-"
    mina "Mmmhhh...♥ God I wish the archery team could see this--! S-spank her again, [mcf]--"
    scene w3_7898 with dissolve
    play sound "sound effects/slap4.wav"
    scene w3_7899 with hpunch
    mc "GAH! YOU {b}PRIM AND PROPER BITCHES{/b} ARE GOING TO KILL ME!"
    scene fm_ts08d_a with dissolve
    show fm_ts08d with dissolve
    mina "A-aahh, hhhaaaa-♥"
    fel "Hnntt.... hhhgggg...! Y-you want this dick?!"
    mina "Y-yeahh.... Oh, God, I {i}need{/i} it."
    mct "(Euuuggghhh, fuuuuuuuck...)"
    mina "I need dick!"
    fel "Too bad! Ha...♥ Play with yourself and wait your turn!"
    "{i}This chorus was getting to me, but I hadn't even tasted Mina yet...{/i}"
    mina "A-ahh.... oh, Felicia... o-oh, [mcf]...♥ F-fuck you both for making me crazy like this..."
    scene fm_ts08e_a with dissolve
    show fm_ts08e with dissolve
    "So began the race to get Felicia off before the older blonde's quivering box got me off."
    fel "This is ALL you, kitten. {b}Own it!{/b}"
    mina "Eh... hehhh--"
    fel "SAY IT! THIS IS YOU!"
    mina "Euuugghh...?"
    fel "This! Is! You!"
    mina "A-aaahh...♥ This is all me!"
    "Like a shepherd, Felicia herded Mina toward {i}her own{/i} truth."
    fel "Say it louder!"
    scene fm_ts08d_a with dissolve
    show fm_ts08d with dissolve
    mina "T-this is all me! I like dick... hnggg...♥ I like... watching you g-get fucked..!"
    fel "Is that it?!"
    "{i}Felicia was losing it.{/i}"
    mina "I l-like being watched masturbating--"
    "{i}Mina was losing it.{/i}"
    mina "I l-like men... and I l-like..."
    mc "Oh, you bitches!"
    "{b}I was losing it.{/b}"
    mc "You're FUCKING killing me here, Mina!"
    fel "What else?!"
    mina "I l-like g-girls?!"
    scene fm_ts08e_a with dissolve
    show fm_ts08e with dissolve
    "It was truly a feedback loop of depravity."
    fel "O-ohh, oh fuck, d-do you now? Ha, heeh... no need to make any life decisions right now... j-just fucking watch me... a-ahh..."
    "Fortunately, before their dirty admissions brought me to climax..."
    fel "Oh, o-ohh, aauuuhhh...!"
    "{i}Felicia was there.{/i}"
    fel "W-watch me...!"
    scene w3_7900 with flash
    fel "A--oohhh, ooohhhhhhhooo!"
    "Felicia came, and with it, was my own blinding bliss that threatened to jeopardize my laid plans of {i}not{/i} making a mess inside her."
    scene w3_7901 with flash
    fel "Euuggghhhhh....♥♥♥♥"
    "Felicia swallowed me completely, forcefully pressing herself back in a bid to get the most dick as possible, and keeping it there."
    scene w3_7902 with vpunch
    mc "O-ohhhh... hnnggg...!"
    "All I could do was hold tight, balls aching and white-knuckling Felicia's womanly shape, as we both rode out her orgasm together."
    fel "O-ohh, hhaaaaaaa....♥♥♥♥♥ You s-seee... t-this..."
    scene w3_7903 with dissolve
    mina "........."
    mina "......"
    mina "..."
    "Mina, mesmerized by the fireworks, froze up."
    scene w3_7904 with dissolve
    fel "Aaa--ahh, ohhhhh...♥ Aaaa--aaahh...♥ Heh, hehe... {b}thiiiiis{/b} was the BEST--"
    "Mina stared at her friend's debasement in utter amazement, and I swelled with primal confidence."
    fel "This... this... was a good idea. W-whose was it again? Heheh..."
    scene w3_7905 with dissolve
    "........."
    "......"
    scene w3_7906 with dissolve
    mina "...I didn't look like that, did I?"

    if w3FeliciaThreesomeControl == True:
        scene w3_7907 with dissolve
        fel "E-hehhh..."
        mc "Get a good fucking look at this disheveled bitch."
        scene fm_ts09_a with dissolve
        show fm_ts09 with dissolve
        mc "Burn it into your eye sockets."
        fel "Heheh...♥"
        mc "{b}That's{/b} Felicia Ford for you, in the flesh."
        mina "Oh..."
        mc "That beautiful, confident woman you know?"
        fel "O-oh, s-shit..."
        mct "(...did she just come again?)"
        mc "This is what she looks like when she's been {b}thoroughly fucked.{/b}"
        mina "W-wow..."
        mc "Thank me for the dick, you sloppy bitch."
        "The same energy from earlier manifested itself, and I said whatever I wanted, as if it was the complete truth."
        fel "Hmmm...♥"
        "...but instead, Felicia just smiled, insubordinate and contented."
        scene w3_7908 with dissolve
        scene w3_7909 with dissolve
        mc "Eh. Get Mina ready for me."
        "I barked an order, as if Felicia was a club whore."
        fel "Ehehhh..."
        mc "{b}Lick.{/b}"
        scene w3_7910 with dissolve
        "...in this, she obeyed."
        mina "[mcf], you're..."
        scene w3_7911 with dissolve
        "{i}She did as I asked.{/i}"
        mina "O-ohhh...?!"
        scene black with fade
        mc "It's your turn now, {i}kitten{/i}."
        "..."
        jump w3FeliciaMinaSwitch
    else:

        scene w3_7912 with dissolve
        mc "Yeah, you kinda did."
        scene w3_7913 with dissolve
        "........."
        "......"
        scene w3_7914 with dissolve
        mina "...d-did not."
        scene w3_7913 with dissolve
        "......"
        "..."
        scene w3_7915 with dissolve
        mc "Pfft-"
        mina "Hahaha... we've lost our minds."
        scene w3_7916 with dissolve
        mc "So, you like girls, huh?"
        mina "Uh, um.... I don't... I'm not sure?"
        scene w3_7917 with dissolve
        mc "Get her ready for me, will you?"
        fel "H-hehe... s-sure thing... a-hhh..."
        scene w3_7918 with dissolve
        mina "I wasn't, uhh... people just say things...."
        mc "Yeah, people say all kinds of things in the heat of passion."
        scene w3_7919 with dissolve
        mina "O-ohhh...♥"
        mc "I'm going to choose to take it as a challenge though."
        scene w3_7910 with dissolve
        mina "U-uhhh... {i}w-what?{/i} A-ah..."
        mc "No pressure, Felicia, but I think Mina's identity might hang in the balance on your oral skills."
        scene w3_7920 with dissolve
        mina "GOD YOU TWO ARE STUPID!"
        scene black with fade
        mc "Mmmmh, good girls..."
        "......"
        "..."
        jump w3FeliciaMinaSwitch

label w3FeliciaMinaSwitch:
    scene w3_7921 with fade
    mina "Hnngggg... w-what's with this position?"
    scene w3_7922 with dissolve
    fel "It lets you see just how deep [mcf] is penetrating you."
    scene w3_7921 with dissolve
    mina "S-sure, I get that, but why are you holding me?"
    scene w3_7923 with dissolve
    fel "*Whisper* {i}Because I want to see how deep he fucks you.{/i}"
    scene w3_7924 with dissolve
    mina "O-oh, yeah... that makes sense..."
    scene w3_7925 with dissolve
    mc "Well, well, well... you recovered quickly..."
    "Felicia was in fighting form."

    if w3FeliciaThreesomeControl == True:
        scene w3_7927 with dissolve
        fel "Mmmh, what? Do you think your dick is Mike Tyson?"
        scene w3_7925 with dissolve
        mc "That's not what you sounded like five minutes ago..."
        scene w3_7926 with dissolve
        fel "{i}Thank you for the cock{/i}, [mcf]."
    else:
        scene w3_7926 with dissolve
        fel "It's not my first time, stud"

    fel "Now, go ahead. Give our darling what she craves."
    scene w3_7928 with dissolve
    mina "Heh, heh--"
    scene black with fade
    "{i}Mina fit me like a glove{/i}."
    scene fm_ts10_a with dissolve
    show fm_ts10 with dissolve
    "And, like Felicia, she was past the need for taking it slow."
    mina "Hnnggg...♥"
    "The moment I slipped in, Mina's insides seized me, and I was reminded of the need that Felicia had failed to extract from me."
    mina "[mcf]....!"
    "A need that propelled me forward into the younger blonde."
    mina "Oooh, euughhh..."
    "Felicia, meanwhile, loomed over the blonde, pressing down from above on her womb."
    fel "...you like, kitten?"
    "Something that proved to be a unique sensation for both of us, like playing with the safety up on a bowling lane."
    scene fm_ts10b_a with dissolve
    show fm_ts10b with dissolve
    mina "It feels w-weird!"
    mc "That's a neat, simple trick..."
    mina "Mmmhhh...♥"
    fel "Just relax, let go, and enjoy the sensation..."
    "Felicia adopted a more nurturing tone divorced from the previous insanity and aimed it squarely at the younger woman in her arms."
    mina "It feels weird, but it feels good at the same time..."
    scene fm_ts10_a with dissolve
    show fm_ts10 with dissolve
    "That dichotomy, the one of the screaming whore from five minutes ago and the sweetly guiding influence of now, twisted up my insides."
    mina "Eheh... you said I'm in good hands, right?"
    "The bulk of my being wanted to wretch Felicia back into the former persona, but chasing that flash of need, was a serenity."
    fel "You're lucky to call on our {i}experience.{/i}"
    mina "O-ohhh...♥"
    fel "You're going to get fucked up, kitten. That's the honest truth."
    mina "A--aahh, oohhh... F-felicia...♥"
    fel "But while you're still cognizant of more than just your cunt..."
    mina "Euugghhh..."
    fel "Know this..."
    mina "A-ahhhh... w-what?"
    fel "You're our whole world right now."
    mina "Mmmhhh...♥ Y-yeah...?"
    fel "You're all that matters."
    mina "Meeuhhh... y-yeah... what do you two take me for..."
    scene w3_7929 with dissolve
    scene w3_7930 with dissolve
    scene w3_7931 with instantdissolve
    mina "Euuuuuughhh...?!"
    "Felicia put a little bit more weight on where I was gouging."
    scene fm_ts10b_a with dissolve
    show fm_ts10b with dissolve
    fel "What were you saying, {i}kitten?{/i}"
    mina "Holy, I just blanked! O-ohh...♥"
    mina "Oh, o-ohhh...♥ What a--"
    fel "I know, right? First taste of dick tonight, yet you've already been put through the wringer..."
    mina "A-aahhhh...♥"
    "Every time Felicia spoke, the already trivial task of pushing into the younger blonde became even easier."
    scene w3_7929 with dissolve
    scene w3_7930 with dissolve
    scene w3_7931 with instantdissolve
    fel "Too hard?"
    mina "N-no! I... {i}love it.{/i} Hnnggg...♥ F-fuck....!"
    scene fm_ts10_a with dissolve
    show fm_ts10 with dissolve
    mina "Fuck, shit, ooo-♥"
    "Mina's overwrought emotions bubbled to the surface and expletive upon expletive fell from Mina's lips, but none of them had barbs."
    mina "Y-you b-bitch!"
    fel "Listen to her! So overwhelmed!"
    "But as I watched Mina quickly get shackled by the throes of carnal pleasure..."
    mc "I think our princess is ready to be devoured, Felicia."
    "My greediness grew."
    mina "P-princess...? A-ahhh..."
    mc "Push down a little harder, {i}please.{/i}"
    fel "Since you said please..."
    mina "W-wait is this the {i}fucked up{/i} part you were alluding--"
    mina "Aeeeuuuuughhhttoooo...♥"
    "True to theory, the result was divine."
    mina "Whhattdddhhaafhhhuuck...♥"
    "The pressure from above was the tightest squeeze yet, and what was previously {i}plowing{/i} became better described as sawing."
    mina "Eugughhh...♥ F-feels like I'm going to pee!"
    scene fm_ts10b_a with dissolve
    show fm_ts10b with dissolve
    "It was a battle to get through, and the rim of my engorged crown gouged Mina's insides in a crudely delirious way."
    fel "You're not going to! Probably!"
    mc "Fuck!"
    mina "[mcf]-"
    mc "Fuck! {b}Fuck!! FUCK!!!{/b}"
    "It truly felt like Mina's insides were being molded to the contours of my penis."
    fel "How's that feel, kitten?"
    mina "Eugughhh...♥ I don't know!"
    fel "Should we change track?"
    mina "N-no! K-keep fucking me!"

    if w3FeliciaThreesomeControl == True:
        fel "Then ask [mcf] to make you cum again! All nice, and submissive like, okay?"
    else:

        fel "Then ask [mcf] to make you cum! All nice, and submissive like, okay?"

    mina "You ask him, you-!"
    scene w3_7929 with dissolve
    scene w3_7930 with dissolve
    scene w3_7931 with instantdissolve
    "{i}Harder.{/i}"
    mina "Oooeuubbhhihiittccch..."
    fel "Lip service is important in these situations!"
    scene fm_ts10b_a with dissolve
    show fm_ts10b with dissolve
    fel "Ask him while you still have some sense left in that near-empty head of yours."
    mina "M-make me cum, please. [mcf]. Aaaaaahh...♥"
    fel "Ask him without sounding like your brains are scrambled eggs!"
    mina "M-make me-"
    scene w3_7929 with dissolve
    scene w3_7930 with dissolve
    scene w3_7931 with instantdissolve
    mina "A-aahhh...!"
    fel "Say it properly, kitten."
    scene fm_ts10_a with dissolve
    show fm_ts10 with dissolve
    mina "Euuughhh...!"
    mina "Make me cum, [mcf]. {i}I want to cum.{/i}"
    mina "C-cum, cch-ummm, ch-chhhummm...! Mhakemeeeh...!"
    mc "Fuck, you're breaking her...!"
    mina "Eugughhh.. o-ooooooouuhuhhhhhhhh...♥"
    fel "You sure that's not your doing, you big dicked bastard??"
    mina "Bwwweeahhhhh...♥"
    fel "No thoughts, kitten. {i}Only dick!{/i}"
    mina "Dhiicck... dhiicccck...♥"
    "Insensate, Mina parroted back whatever odd word pierced through the noise."
    mina "Euugghhh... g-guyss... it's happenin' so-soooo quick!"
    fel "Say, what's your name?"
    mina "Euuhhh... w-what?"
    fel "What's the name your mother gave you?"
    mina "Umm, uhhhhmmm..."
    fel "Yep... {i}forget even that.{/i}"
    scene fm_ts10b_a with dissolve
    show fm_ts10b with dissolve
    "Mina wasn't so much {i}pure{/i}, as she was a searing hot piece of iron."
    fel "Get lost, {i}kitten.{/i}"
    "Easily bent. Moldable. Primed for the imperfections to be hammered out."
    mina "Ghhuuyuysss...!"
    "And in a rare moment of clarity, while I dumbly plugged away at this babbling bitch of a blonde, I realized we were equal in one respect."
    mina "Yhhhoutwhhoo... yuouhuhhtwhhhoo...♥"
    "Try as I might to have control over this situation, I was just as lost as she was, infected by Felicia's enthusiasm."
    fel "There you go!"
    mina "I'm--"
    scene w3_7929 with dissolve
    scene w3_7930 with dissolve
    scene w3_7932 with instantdissolve
    mina "O-ooooookayyyyy...! A-aaahhh...!"
    with flash
    "{i}A short and hard one took Mina from us{/i}, and I was swallowed up by the sweetly shrill cacophony of Mina's orgasm."
    scene fm_ts10c_a with dissolve
    show fm_ts10c with dissolve
    "............"
    "........."
    "......"
    "..."
    mina "Euhhhh..."
    "In the end, I felt frustrated. I wanted to cum, yet I didn't move my hips."
    "I just took in the sight of Mina writhing beneath me."
    scene w3_7933 with dissolve
    "........."
    scene w3_7934 with dissolve
    "......"
    scene w3_7935 with dissolve
    fel "...nice work, stud. A+ effort."
    scene w3_7936 with dissolve
    "Felicia kept that same, motherly affectation she wielded like a blade with Mina."
    scene w3_7935 with dissolve
    fel "Why don't you finish? Or you don't want it to be over?"
    scene w3_7937 with dissolve
    mc "..."
    "Naturally, I wanted this to never stop."
    scene w3_7938 with dissolve
    fel "Should I finish you...?"
    scene w3_7937 with dissolve
    "Again, I didn't answer, only stared back in a daze."
    scene w3_7939 with dissolve
    fel "I know that look."
    stop music fadeout 3.0
    scene black with fade
    "...but if it had to end, there was only one option in my mind."
    jump w3FeliciaMinaBJ

label w3FeliciaMinaBJ:
    play music "music/epic-battle-speech.ogg"
    scene w3_7940 with fade
    "Two beautiful women sat obediently at my feet, the cap of a night that had thrown my karmic balance into the gutter."
    "Two sets of expansive eyes, wet with arousal."
    "Felicia's as sharp as ever."
    scene w3_7941 with dissolve
    "Mina's a bit more dulled by the night's proceedings, but hunger no less abated..."
    scene w3_7942 with dissolve
    mc "{b}No.{/}"
    "Felicia reached with initiative, but I wanted to take in this sight as if it were a quickly fading sunset."
    scene w3_7943 with dissolve
    "............"
    "........."
    scene w3_7944 with dissolve
    "......"
    scene w3_7945 with dissolve
    "...at least, that was my intention, but--"
    scene w3_7946 with dissolve
    "Oh, how did my balls {i}ache{/i}."
    "I had no concrete plan."
    scene w3_7947 with dissolve
    "My genitals ebbed and flowed between the two."
    "Rubbing, covering faces..."
    scene w3_7948 with dissolve
    "Winding up on the insides of cheeks..."
    "The pair indulged me in a raw, meandering manner."
    scene fm_ts11_a with dissolve
    show fm_ts11 with dissolve
    "It was as formless of an act of sexual expression as I had ever experienced."
    mc "Ahhh... {i}girls...{/i}"
    "I had intended to loom over the pair, to poke and exacerbate my male ego, but both my blondes burned too bright for that."
    minafel "Cwup, ffwhhup~*"
    "So bright that edges of where one of us began and the other ended {i}bled{/i}."
    minafel "*Chwup, fwhhhhuppp~*"
    "Every little kiss they dotted my prick with brought us closer to a homogenized form, until..."
    scene w3_7949 with dissolve
    mc "W-where do you think..."
    fel "Relax, I'm going to make you feel amazing."
    mina "Me too..."
    play music "music/hypnosis.ogg"
    scene fm_ts12_a with vpunch
    show fm_ts12
    mc "Eh...?!"
    "{i}I was being devoured.{/i}"
    mc "That's--"
    "Mina assumed a more {i}normalized{/i} position, while Felicia had begun teasing parts of me that I had yet unventured."
    with vpunch
    mc "Hnnnggg...!"
    "The girls, through their attentive efforts, were telling me it was {b}my{/b} turn to moan."
    with vpunch
    mc "Oh, oohhhh...!"
    "And the dichotomy between those two competing sensations, Mina in my front and Felicia in my back, veered beyond the borders of my sexual understanding."
    "Mina's servile devotion was an act of warm familiarity, a lover-like embrace save for the inundation of sloppy fuck sounds."
    "At the opposing end, the sensation of Felicia's tongue creeping into my most underused orifice was {i}alien{/i}."
    "The soft, wet, snake-like invader pushed past my pucker slowly, coaxing it to dilate."
    play ambient "sound effects/fel5.wav"
    scene fm_ts12b_a with dissolve
    show fm_ts12b with dissolve
    mc "Oh, what the fuck..."
    "And as I invaded the back of the actress' throat, Felicia's tongue successfully found purchase. Not {i}so{/i} deep..."
    mc "Ah...!"
    "...but deep enough for me to know she was back there."
    "It wasn't quite how I imagined it; {i}not that I imagined it.{/i}"
    "Her tongue didn't feel hot, but rather... {i}cool{/i}."
    mc "Uuugh..."
    stop ambient
    scene fm_ts12_a with dissolve
    show fm_ts12 with dissolve
    "Or maybe it wasn't so much the appendage itself, but the accumulating saliva transferring from her tongue to my pink parts?"
    "Either way, an {b}odd{/b}, almost implacable feeling."
    "Something firm, like a finger or sex toy, I understood. But a tongue?"
    "Yet, it felt good, in a different way."
    "Before this, I would've imagined the appeal was the thrill of debasement..."
    play ambient "sound effects/fel2.wav"
    scene fm_ts12b_a with dissolve
    show fm_ts12b with dissolve
    mc "Holy shit..."
    "...but that wiry fucker set alight all the overly concentrated nerve endings of my asshole."
    fel "Mmmh, hmmm, hmm~!"
    mina "*Cwhhup-♥*"
    "Conversely, Mina wasn't going to be outdone. What she lacked in experience was more than made up for in determination."
    "My hand sat firmly atop her head, but she was in the driver's seat; I was too otherwise overwhelmed by the double-pronged attack to offer guidance."
    mc "Euugghhhh..."
    stop ambient
    scene fm_ts12_a with dissolve
    show fm_ts12 with dissolve
    "My entirety, my id and my ego, was sandwiched between two blondes and being minced into paste."
    mc "A-ahh... M-mina!"
    "{i}Locked and pressure cooked.{/i}"
    mc "F-felicia...!"
    "{b}Boiling{/b}, with no escape other than down the younger blonde's throat."
    mc "Oh, oh, o-oh god!"
    "A shrill cry slipped out as I headed to that sweet escape."
    mc "Ah, hhnngg...! I'm ahhh..."
    "So why bother?"
    mc "Ooooooh! Hnnnhg...♥"
    "Just... {b}enjoy!{/b}"
    stop music
    play sound "sound effects/spurt.wav"
    scene w3_7950 with flash
    mina "MMmhhh-!"
    "Mina's cheeks puffed up fatter than a squirrel during the winter, as I unleashed a torrent of white sickness into her all-consuming mouth."
    play sound "sound effects/spurt.wav"
    scene fm_ts13_a with flash
    show fm_ts13
    play ambient "sound effects/gulp3.mp3"
    mc "G-gahhh...!"
    "Rope after rope, some finding its way into her tummy."
    "Some clung defiantly to her cheeks..."
    "Some of it spilled from her mouth."
    stop ambient
    scene w3_7951 with dissolve
    fel "C'mere!"
    mina "Mh...?!"
    play music "music/ode-to-joy.ogg"
    play ambient "sound effects/fel3.wav"
    scene fm_ts14_a with dissolve
    show fm_ts14 with dissolve
    "True to self, Felicia's commitment to a performance, came in a {i}me-personally{/i} aggrandizing flourish."
    ".................."
    "..............."
    "............"
    "........."
    "......"
    "...the world was a beautiful place of peace and harmony."
    stop ambient fadeout 3.0
    scene black with fade
    $ history_felicia = "I must have built up some tremendous karma in a past life, as... well... {i}yeah.{/i} I will see this when I close my eyes."
    $ unread_felicia = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "That was my concluding thought to the best night of my life."

    $ renpy.end_replay()

    if not persistent.w3FeliciaMinaThreesome:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3FeliciaMinaThreesome = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

    ".................."
    "..............."
    "............"
    "........."
    stop music fadeout 5.0
    "......"
    "..."
    show screen textbox2 with dissolve
    jump w3June17End

label w3FeliciaDatePlatonicEnd:
    scene w3_7952 with dissolve
    "........"
    "......"
    "..."
    scene w3_7953 with dissolve
    mc "I was serious about not fooling around."
    scene w3_7954 with dissolve
    fel "I know, [mcf]."
    scene w3_7953 with dissolve
    mc "I was more telling myself..."
    scene w3_7955 with dissolve
    "{i}Boop{/i}."
    scene w3_7956 with dissolve
    fel "The man protests too much."
    scene w3_7952 with dissolve
    "......"
    "..."
    scene w3_7957 with dissolve
    fel "We gain the strength of the temptation we resist."
    scene w3_7958 with dissolve
    mc "That'a a funny thing for you to say."
    scene w3_7952 with dissolve
    "..."
    scene w3_7959 with dissolve
    fel "Tonight's been fun."
    scene w3_7960 with dissolve
    mc "Has it?"
    scene w3_7959 with dissolve
    fel "Not in the way I imagined, but... {i}yeah.{/i}"
    scene w3_7960 with dissolve
    mc "What was your winning essay about?"
    scene w3_7961 with dissolve
    "........."
    "......"
    scene w3_7962 with dissolve
    fel "...I'm going to start painting again. Continue napping if you want."
    scene w3_7963 with dissolve
    "As the night and our time together wrapped up, I had thought."
    "With a brush in her hand, Felicia never looked more stunning."
    $ history_felicia = "Even though the night ended without a bang, as I intended, I still had a lovely date with my favorite gold digger."
    $ unread_felicia = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "............"
    "..."
    show screen textbox2 with dissolve
    jump w3June17End


label w3FeliciaPrematureEnding:
    scene black with fade
    $ history_felicia = "I fulfilled my function as Felicia's date, serving as a buffer against awkwardness. As planned, the night ended without a bang, although Felicia could've been in better spirits."
    $ unread_felicia = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "That was our night."
    "I stuck to my guns about keeping it platonic, and Felicia never quite shook her irritation over the critic."
    "It probably wasn't the night she imagined, but she thanked me all the same. I had served my function as a {i}present body{/i} well enough."
    jump w3June17End

label w3June17End:
    play music "music/Moonlight-Sonata.ogg"
    scene w3_7964 with fade
    kat "I'm glad you accepted our invitation."
    man "I would've taken the card as a joke, but I've heard talk of this place."
    kat "{i}Whispers{/i}, I hope."
    man "Oh, of course."
    scene w3_7966 with dissolve
    kat "Well, that's unsurprising. A lot of our members should be familiar faces to a man of your influence. That card stuff..."
    scene w3_7965 with dissolve
    man "...a bit of panache?"
    scene w3_7966 with dissolve
    kat "{i}Precisely.{/i}"
    scene w3_7965 with dissolve
    man "I know a thing or two about that with my line of work."
    scene w3_7967 with dissolve
    kat "The invitation by card is August's flair. Did Dalia introduce you to him yet?"
    scene w3_7965 with dissolve
    man "No, uh... the tour was {i}short-lived.{/i}"
    scene w3_7969 with dissolve
    kat "She's good, isn't she?"
    scene w3_7968 with dissolve
    man "Oh, ohh... {i}she's good.{/i}"
    scene w3_7970 with dissolve
    kat "You'll find this place is all about flair."
    kat "I'm sorry that I'm the only one introducing myself tonight."
    scene w3_7968 with dissolve
    man "I wasn't expecting a welcome wagon. Charles Kohler is no doubt a busy man."
    scene w3_7971 with dissolve
    kat "Oh, he... {i}is.{/i}"
    scene w3_7972 with blinds
    kat "{b}Very busy.{/b}"
    chuck "Shall I pour you another drink?"
    scene w3_7973 with dissolve
    sophia "I believe {i}one{/i} is within the bounds of politeness."
    scene w3_7972 with dissolve
    chuck "Thank you for another night of indulgence."
    scene w3_7974 with dissolve
    sophia "Mmmhhm."
    scene w3_7975 with dissolve
    chuck "This is where you usually remind me what a busy woman you are."
    scene w3_7976 with dissolve
    sophia "What exactly do you do with {i}your{/i} time, Dr. Kohler?"
    scene w3_7977 with dissolve
    chuck "I'm an open book."
    scene w3_7976 with dissolve
    sophia "If that was true, your golf instructor would've ran the moment you fell off the bookshelf."
    scene w3_7975 with dissolve
    chuck "You know about her?"
    scene w3_7978 with dissolve
    sophia "Yes, and your bowling teacher, as well as your shuffleboard coach. It's funny how all your recreational learning comes from women."
    scene w3_7979 with dissolve
    chuck "They weren't laughing."
    scene w3_7980 with dissolve
    sophia "......"
    scene w3_7981 with dissolve
    sophia "...you're disgusting."
    scene w3_7982 with dissolve
    chuck "Like you have any leverage to hurl stones at me. I just have the decency not to dress it up."
    scene w3_7983 with dissolve
    sophia "You presume too much about Dr. Van Doren."
    chuck "That struck a nerve, did it? He's just as frivolous as I am, is he not?"
    scene w3_7984 with dissolve
    chuck "How else would you explain poking around my hen house? Like you don't have a secret lab to conduct your experiments in. Or is paying young men {i}innocuous{/i} house calls a hobby of his?"
    scene w3_7985 with dissolve
    sophia "You welcomed us with open arms, Dr. Kohler."
    scene w3_7986 with dissolve
    chuck "That I did, lass. Because it's not every day you get to see that old Kraken of yours unfurl his shadowy tendrils."
    chuck "It's especially funny that {i}your{/i} brainwash juice, or whatever the fuck you're cooking up, has him not only cavorting with whores but new money assholes like me."
    scene w3_7987 with dissolve
    sophia "...are we a joke to you?"
    scene w3_7988 with dissolve
    chuck "A friend of mine at Langley had a saying that I took a real shining to."
    chuck "{i}Life's a joke, so be the punchline.{/i}"
    scene w3_7987 with dissolve
    sophia "Was he very funny?"
    scene w3_7988 with dissolve
    chuck "Not at all. In fact, save for you, he was the unfunniest person I'd ever had the displeasure of meeting."
    scene w3_7989 with dissolve
    sophia "...do you really think you'll be able to beat me? Even if you had years?"
    chuck "I don't know. They all thought that, but you're a different breed from some hick semi-pro golfer from Oklahoma."
    scene w3_7990 with dissolve
    chuck "Plus, I don't think you'll break like they did. And it's not like I can do any lasting damage, right?"
    chuck "You're too valuable of a commodity."
    scene w3_7991 with dissolve
    sophia "........."
    scene w3_7992 with dissolve
    sophia "......"
    scene w3_7993 with dissolve
    sophia "...good night, Dr. Kohler."
    chuck "Good night, Dr. Lundgren."
    scene w3_7994 with blinds
    kat "You'll meet him soon enough. You're actually joining us at an exciting time."
    scene w3_7995 with dissolve
    man "You don't need to sell me, Kathy. You've already got my money."
    scene w3_7996 with dissolve
    kat "And in many different ways, I suppose."
    scene w3_7997 with dissolve
    man "I'm not sure I follow."
    scene w3_7994 with dissolve
    kat "Oh, that explanation is better saved for your grand welcome this weekend - the operative word being {b}grand{/b}."
    scene w3_7998 with dissolve
    man "Now, you have my curiosity. Does everyone get one of those?"
    scene w3_7994 with dissolve
    kat "Would you believe me if I said no?"
    scene w3_7995 with dissolve
    man "Yes, but then I'd remember the kind of place I'm in."
    scene w3_7998 with dissolve
    man "So, I've met you - and Charles has his reputation - but tell me about the other one with the panache?"
    scene w3_7996 with dissolve
    kat "Oh, August? He's..."

    scene w3_7999 with blinds
    aug "Tough day, my dear?"
    scene w3_8000 with dissolve
    hana "It was... {i}so-so{/i}."
    scene w3_7999 with dissolve
    aug "Oh? And here I was hoping dealing with Kimber would tank your whole evening."
    scene w3_8001 with dissolve
    "........."
    "......"
    scene w3_8002 with dissolve
    hana "...it would have, but I saw a friend."
    scene w3_8003 with dissolve
    aug "Well, if {i}so-so{/i} gets you accepting more of my drinks, then maybe I should give this friend a job."
    scene w3_8004 with dissolve
    hana "Don't even joke about that..."
    scene w3_8005 with dissolve
    "......"
    scene w3_8006 with dissolve
    "..."
    scene w3_8007 with dissolve
    aug "I won't patronize you by telling you that you made the right choice today."
    scene w3_8006 with dissolve
    hana "Shouldn't you? I made the choice you wanted me to make."
    scene w3_8007 with dissolve
    aug "{b}You did{/b}, but I didn't push you to make a {i}right{/i} choice."
    scene w3_8008 with dissolve
    hana "... and what would you know about that, {i}father?{/i}"
    scene w3_8009 with dissolve
    aug "I've seen \"right\" sink and {b}shorten{/b} men's longevity, just as I've seen the \"right\" choice keep men afloat."
    scene w3_8010 with dissolve
    hana "Blah, blah no right and wrong?"
    scene w3_8011 with dissolve
    aug "Oh, no. That's a delusion that you can drown in."
    scene w3_8009 with dissolve
    aug "Make no mistake; when the choice is both \"smart\" and \"right\", that's the one you go with. Otherwise..."
    scene w3_8012 with dissolve
    hana "...don't be stupid?"
    scene w3_8013 with dissolve
    aug "Don't. Be. Stupid. Smart should always win out over right."
    scene w3_8014 with dissolve
    hana "........."
    scene w3_8015 with dissolve
    "......"
    scene w3_8016 with dissolve
    hana "...that's such bullshit."
    scene w3_8017 with dissolve
    "........."
    "......"
    scene w3_8018 with dissolve
    aug "...what's with that look, sweetheart?"
    scene w3_8019 with dissolve
    hana "...I was just thinking it's exhausting being angry at you."
    scene w3_8018 with dissolve
    aug "Does that mean you're going to try the alternative?"
    scene w3_8020 with dissolve
    hana "Oh, I'll give it a spin for five minutes. Or until that bottle runs out."
    scene w3_8021 with dissolve
    aug "I'll pour slowly, then."
    scene w3_7994 with blinds
    kat "...he's a {i}dear.{/i} Surprisingly sentimental."
    scene w3_7995 with dissolve
    man "...is that so?"
    scene w3_7994 with dissolve
    kat "He told me he knew your father."
    scene w3_7995 with dissolve
    man "Was he--"
    scene w3_7996 with dissolve
    kat "{i}No.{/i} You'll have to ask him for specifics, though."
    scene w3_7998 with dissolve
    man "{i}Well{/i}, I'm intrigued."
    scene w3_7994 with dissolve
    kat "You'll find that there's more to our establishment than just the girls."
    scene w3_8022 with dissolve
    kat "By the way, speaking of which... we're always on the lookout for fresh faces."
    scene w3_8023 with dissolve
    man "And it just so happens that's my expertise?"
    scene w3_8024 with dissolve
    kat "Would it amuse you to know that Alison Smith was in the previous year's contest?"
    scene w3_8023 with dissolve
    man "{b}No shit!{/b}"
    scene w3_8024 with dissolve
    kat "{i}No shit.{/i}"
    scene w3_8023 with dissolve
    man "What about this year? Anyone I would know? Or {i}will{/i} know?"
    scene w3_8025 with dissolve
    kat "In that respect? I believe you will be thoroughly {i}floored{/i}."
    scene w3_8026 with dissolve
    kat "Welcome to the club, Mr. Ford."
    scene w3_8027 with dissolve
    elias "You have the mark of a good steward, Kathy."
    scene black with fade
    "......"
    "..."
    stop music
    jump June18Start


label w3June17MiddayMontage:
    "The rest of the day was spent on bullshit."
    scene w3_8028 with fade
    "Rosalind kept to herself mostly."
    "Read a book, even."
    scene w3_8029 with dissolve
    "{i}I studied.{/i}"
    "An oddly harmonious, peaceful afternoon."

    if rosalindKilSolution == True:
        "{i}Especially after what we did...{/i}"

    scene w3_8030 with dissolve
    "......"
    "..."
    play ambient "sound effects/ringing-inbound.wav"
    scene w3_8031 with dissolve
    "*Ring, ring*"
    mc "Hmm... Veronica...?"
    scene w3_8032 with dissolve
    "..."
    scene w3_8033 with dissolve
    mct "(No harm in answering in...)"
    stop ambient
    play sound "sound effects/phonemenu.wav"
    scene w3_8034 with dissolve
    mc "He--"
    jump w3VeroCheckingIn
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
