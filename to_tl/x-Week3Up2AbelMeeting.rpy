label june15endrevise:

    scene w3_3384 with curtains
    show screen textbox2 with dissolve
    "When I got back, I should've been more surprised at what I found, but honestly... part of me expected it."
    abel "Oh, good you're here."
    "Abel was sitting comfortably in a chair, a glass of tea in front of him, while Sophia idled in the kitchen."
    scene w3_3385 with dissolve
    abel "I feared you might stand me up like the ugly girl at a winter formal."
    scene w3_3387 with dissolve
    "The old man's nonchalance about breaking into my home was nothing short of infuriating."
    "First it was Sophia fucking with me earlier with her drug, and now..."
    hide screen textbox2 with dissolve

    menu:
        "Hold your tongue(Dialouge/Render Changes only).":
            scene w3_3548 with dissolve
            show screen textbox2 with dissolve
            mc "Good afternoon, Dr. Van Doren. What do I owe the pleasure of your visit?"
            scene w3_3547 with dissolve
            "There was no point in voicing my displeasure; there was only the reality that he was here, and like it or not, my life was now entangled with the whims of men like him."
            scene w3_3549 with dissolve
            abel "I wanted to speak with you {i}outside{/i} the club."
            scene w3_3547 with dissolve
            "A quick inspection of the room told me it was likely just us, although my mind doubled back and second-guessed the conspicuously suited man I had passed at the building's entrance."
            scene w3_3548 with dissolve
            mc "Sophia phrased it differently. She said you wanted to educate me?"
            scene w3_3550 with dissolve
            abel "Did she? Oh, Sophia..."
            abel "For all her wonderful gifts, tact isn't one of them."
            scene w3_3548 with dissolve
            mc "Was she mistaken?"
            scene w3_3549 with dissolve
            abel "There are always nuggets of value to be mined from any conversation."
            scene w3_3548 with dissolve
            mc "Yeah, I see what you mean. {i}Mining{/i}."
            scene w3_3551 with dissolve
            mc "Just like how your choice of words reinforces my impression of you?"
            scene w3_3552 with dissolve
            abel "Show him, Sophia."
            scene w3_3553 with dissolve
            sophia "It's a listening device that broadcasts sound above a specific decibel."
            mc "...are you saying I've been spied on?"
            scene w3_3554 with dissolve
            sophia "I don't think so. This is the only one we found, likely shoddily forgotten after the others had been removed."
            scene w3_3391 with dissolve
            sophia "What's more, the battery likely ran out some time ago. This model can operate for 75 days in standby mode, so I suspect it was a previous tenant who should have had privacy concerns."
            scene w3_3556 with dissolve
            mc "I see..."
            scene w3_3557 with dissolve
            mct "(Darius {i}was{/i} blackmailing the old woman. Her bugging this place {b}would{/b} make sense... still...)"
        "Call him out on it.":

            scene w3_3386 with dissolve
            show screen textbox2 with dissolve
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
            mc "...are you saying I've been spied on?"
            sophia "I don't think so. This is the only one we found, likely forgotten after the others had been shoddily removed."
            scene w3_3391 with dissolve
            sophia "What's more, the battery likely ran out some time ago. This model can operate for 75 days in standby mode, so I suspect it was a previous tenant who had unknown privacy concerns."
            scene w3_3392 with dissolve
            abel "Point is, I only go places that are verified by my staff. Forgive the intrusion."
            scene w3_3556 with dissolve
            mct "(Darius {i}was{/i} blackmailing the old woman. Her bugging this place {b}would{/b} make sense... still...)"
            scene w3_3557 with dissolve


    "Still, this..."
    if w3SophiaPromoFinish == True:
        mc "This bugs me."
        scene w3_3558 with dissolve
        sophia "Pffh-"
        sophia "No pun intended?"
        scene w3_3557 with dissolve
    else:
        "{i}Disturbs me{/i}."

    mc "That's the only one you found?"
    scene w3_3559 with dissolve
    sophia "After an exhaustive search, but it's possible we missed some."
    scene w3_3393 with dissolve
    abel "Don't look so concerned. I highly doubt that device was meant for you - or were you under the illusion you had privacy here?"
    "......"
    "..."
    hide screen textbox2 with dissolve
    menu:
        "Take control of the conversation(w3AbelControl=True).":
            $ w3AbelControl = True
            show screen textbox2 with dissolve
            scene w3_3560 with dissolve
            mc "This has already been educational, sir."
            scene w3_3395 with dissolve
            abel "Why do you say that?"
            scene w3_3561 with dissolve
            mc "The guy I replaced left under unusual circumstances."
            scene w3_3562 with dissolve
            abel "No doubt he did."
            scene w3_3563 with dissolve
            mc "Did you know Darius?"
            scene w3_3562 with dissolve
            abel "No. I'm new to Charles' club, remember?"
            scene w3_3563 with dissolve
            mc "You've already demonstrated your precaution. Are you telling me you didn't look into the club's staff and patrons?"
            scene w3_3562 with dissolve
            abel "Present staff and patrons, sure. I looked into you for example."
            scene w3_3406 with dissolve
            mc "You didn't find anything interesting."
            scene w3_3408 with dissolve
            abel "No, I did {b}not{/b}. You are remarkably unexceptional, if you don't mind me saying."
            scene w3_3406 with dissolve
            mc "No, I don't mind. It's better that way."
            scene w3_3407 with dissolve
            abel "I agree. The people that surround you at work underestimate you because of that. They think you're harmless."
            scene w3_3406 with dissolve
            mc "I AM harmless."
            scene w3_3413 with dissolve
            abel "Someone completely harmless wouldn't be swallowing their annoyance over an old man breaking and entering into their home, demanding their time."
            scene w3_3406 with dissolve
            mc "Thinking before I act was a hard-learned lesson for me as a kid. That's all it is."
            scene w3_3409 with dissolve
            abel "Thinking before you act is one of the few ingredients that you need to thrive in life."
            scene w3_3411 with dissolve
            mc "What are the others?"
            scene w3_3409 with dissolve
            abel "Luck, which you can't control. Another is opportunity, which, to an extent, is something you can."
            scene w3_3408 with dissolve
            abel "But the most important thing, and this speaks to thinking before you act, is to know the difference between caution and hesitation."
            scene w3_3564 with dissolve
            mc "Ha, yeeeeah..."
            mc "{i}\"Fear causes hesitation, and hesitation will cause your worst fears to come true.\"{/i} Something like that?"
            scene w3_3565 with dissolve
            sophia "Who said that, Gandhi?"
            scene w3_3566 with dissolve
            mc "Bodhi."
            scene w3_3567 with dissolve
            sophia "...huh?"
            scene w3_3413 with dissolve
            abel "I'm just saying, [mcf]... if you were so inclined, you're in the kind of position you could levy to your benefit."
            scene w3_3406 with dissolve
            mc "Does that have anything to do with why you're here, sir?"
            scene w3_3412 with dissolve
            abel "It does not. I'm here because I wanted to caution you about your surroundings. You got pulled into this with the promise of money no doubt, dragged all by your friend, and involved in the club's enterprise because of an old man's desire to fulfill his nephew's whims."
            scene w3_3407 with dissolve
            abel "How much do you know about the people around you?"
        "Urge Van Doren to get to the point.":

            scene w3_3394 with dissolve
            show screen textbox2 with dissolve
            mc "Why {i}are{/i} you here?"
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
    abel "No one of consequence ever is, but do you know the specifics."
    scene w3_3406 with dissolve
    mc "Just what I could find on the internet."
    scene w3_3409 with dissolve
    abel "Ah, so nothing at all. It's good I'm here; you thankfully fall within my providence. There are two types of people in this world..."
    scene w3_3410 with dissolve
    mct "(There's probably a lot more than two...)"
    scene w3_3412 with dissolve
    abel "There are those who think nothing of killing a spider in their own home. They simply can't be bothered to do otherwise."
    scene w3_3413 with dissolve
    abel "The other kind of person is the type who takes time to capture and release the spider safely, cognizant that a mere bug doesn't choose to encroach where it doesn't belong."
    scene w3_3406 with dissolve
    mc "Are you saying I don't belong at the club?"
    scene w3_3407 with dissolve

    if w3AbelControl == True:
        abel "I think you are where you chose to be, [mcf]. You availed yourself of luck and opportunity."
    else:
        abel "I think you are where you chose to be, [mcf]."

    scene w3_3406 with dissolve
    mc "Your analogy has me a little confused then."
    scene w3_3409 with dissolve
    abel "You're out of your element, that's all. Not a big deal; people learn quickly. However, the timing is sometimes poor."
    scene w3_3407 with dissolve
    abel "Maybe I'm getting soft in my old age, but you remind me of a boy I once knew. As such, I want you to have a better understanding of your environment."
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
    abel "Now, I'm wondering what I'm even doing here. You have a good head on your shoulders."
    scene w3_3414 with dissolve
    mc "For the record, at the moment, I trust you even less than Dr. Chuck."
    scene w3_3415 with dissolve
    abel "Because of the present circumstances?"
    hide screen textbox2 with dissolve

    menu:
        "Bingo. You think he's shady as fuck(Dialouge/Render Chnages Only).":
            scene w3_3414 with dissolve
            show screen textbox2 with dissolve
            mc "No offense, but pretty much."
            scene w3_3417 with dissolve
            mc "Plus, you're the head of a major pharmaceutical company, cavorting with pimps, refining a sex drug alongside your whore Nazi scientist."
            scene w3_3418 with dissolve
            sophia "Nazi?!"
            mc "No offense Sophia, but being blonde, sharply dressed in black, and testing drugs on people without their consent does conjure up a specific image."
            scene w3_3419 with dissolve
            abel "Ha, honesty! I like that!"
            scene w3_3420 with dissolve
            mc "You claim you're here to be candid? I'll be blunt too."
            scene w3_3421 with dissolve
            sophia "You have no idea who--"
            scene w3_3422 with dissolve
            abel "Pffh, hahaha! Hahahaha! I'm REALLY starting to think I've wasted my time."
            scene w3_3423 with dissolve
            mc "{b}Don't{/b}. Educate me about my environment and the people I work for."
            scene w3_3424 with dissolve
            abel "Okay, let's start with the gangster. You undoubtedly have a vague impression of his character, but you don't know his specific crimes, do you?"
            scene w3_3425 with dissolve
            mc "No, I don't."
            scene w3_3426 with dissolve
        "It's just prudent.":

            scene w3_3568 with dissolve
            show screen textbox2 with dissolve
            mc "It's just a matter of fact. I have strong ties to Dr. Chuck; I grew up around him and he even advised my high school physics club."
            mc "He's not the man I thought I knew, but it's more substantial than..."
            scene w3_3569 with dissolve
            abel "No, I understand."
            mc "Don't get me wrong; you saying I'm out of my element. You took some of your important time to be here. I'm confused, but I'll gladly listen."
            mc "Please educate me about my environment."
            scene w3_3570 with dissolve
            abel "Okay, let's start with the gangster. You undoubtedly have a vague impression of his character, but you don't know his specific crimes, do you?"
            scene w3_3431 with dissolve
            mc "No, I don't."
            scene w3_3430 with dissolve


    abel "It's so easy to get lulled into a sense of security when you're only exposed to a particular side of a person. You may even chat comfortably with him."
    scene w3_3431 with dissolve
    mc "Not too comfortably..."
    scene w3_3430 with dissolve
    abel "You would do well to remember that the man is an extortionist at heart."
    scene w3_3427 with dissolve
    abel "Loan sharking, protection rackets, insurance scams, gambling, prostitution. He's very much destroyed lives - not to mention... he's {b}killed{/b} people."
    scene w3_3429 with dissolve
    mc "...*ahem*, yeah?"
    scene w3_3430 with dissolve
    abel "Well, he's not a convicted murderer. He's a mere person of interest in four disappearances."
    scene w3_3431 with dissolve
    mc "That can mean a lot of things."
    scene w3_3430 with dissolve
    abel "Well whatever it means, he's undoubtedly a factor in a number of suicides. His business remains, as it has long been, one that ruins lives."

    scene w3_3571 with dissolve
    mc "I wasn't... {i}unaware{/i} of that. I mean, well..."
    "......"
    "..."
    scene w3_3431 with dissolve
    mc "I knew he shot porn and he's obviously a pimp, but some of what you've said does paint a more intense picture."
    scene w3_3572 with pixellate
    abel "Men like August who end up making it to a certain age often tend to purport themselves as being principled, but if you cut out the pretense, the only actual standards he upholds are the ones that benefit himself."
    abel "You don't ever want to unknowingly get in that kind of man's way."
    mc "...why would I? I keep my head down."
    abel "Because the difference between family and liability is a thin, flimsy thing to a gangster like him. You should take care not to ever give him even a bad reason."
    scene w3_3431 with pixellate
    mc "I don't plan on it..."
    scene w3_3427 with dissolve
    abel "By the way, have you ever wondered if he knew your mother?"
    scene w3_3432 with dissolve
    mc "What?!"
    mc "That...!"
    scene w3_3433 with dissolve
    "I shouldn't be shocked. The old woman dug up the same info, but..."
    scene w3_3573 with dissolve
    mc "The thought hasn't crossed my mind."
    scene w3_3434 with dissolve
    "...having a patron bring her up, for some nebulous purpose, enraged me to an even more infuriating degree."
    scene w3_3435 with dissolve
    abel "How many videos did she shoot? How big do you think the porn industry of Morehead Hills is?"
    scene w3_3573 with dissolve
    mc "Big enough that I feel comfortable not entertaining that thought."
    scene w3_3435 with dissolve
    abel "It's better not to know, I suppose. August aside, I can tell you who HAS killed people."
    scene w3_3436 with dissolve
    mc "Warren?"
    scene w3_3437 with pixellate
    abel "For one... that man is a menace."
    abel "It takes a lot to get kicked out of the kind of mercenary company that would take a piece of trash like him, but he's pulled it off multiple times - for the same company, no less."
    abel "A by-product of being good at your job, but his \"Sandman\" moniker wasn't given to him because he excelled at fighting. {b}No{/b}, it has more to do with why he's currently a wanted man, living out of your club."
    scene w3_3440 with pixellate
    "......"
    "..."
    mct "(I guess no fucking surprise there, but...)"
    scene w3_3439 with dissolve
    mc "...and what's he wanted for exactly?"
    scene w3_3575 with dissolve
    abel "The man didn't leave his hobby of drugging prostitutes on foreign soil."
    scene w3_3574 with dissolve
    mc "Christ... that... {i}fits{/i} my impression..."
    mc "Speaking of liabilities... {i}he's not?{/i}"
    scene w3_3576 with dissolve
    abel "I said he was good at his job, didn't I?"
    scene w3_3574 with dissolve
    mc "{i}Of watching cameras?{i}"
    scene w3_3575 with dissolve
    abel "His job is to be capable in a pinch and his status as a wanted man makes him more reliable in that aspect."
    scene w3_3577 with dissolve
    mc "His options are limited and you always know where to find him, huh?"
    abel "Precisely."
    scene w3_3439 with dissolve
    mc "What about Jacob? He's not as nice as he seems, right?"
    scene w3_3438 with dissolve
    abel "Why do you say that?"
    scene w3_3439 with dissolve
    mc "I get the feeling he doesn't care for the job, but he's there nonetheless."
    scene w3_3441 with pixellate
    abel "True. Warren's partner is more professional but he's a killer all the same. He got into trouble as a young man in Quebec that saw him flee the country."
    mc "What kind of trouble?"
    abel "A drunken assault. Nothing truly damning on his character in the grand scheme of things, but rather than face the music, he preferred leaving his home country - and what's a more storybook way of escaping your criminal past than joining the foreign legion?"
    mc "That seems pretty drastic."
    abel "Indeed. It's not the easiest route, either. You either have to be a romantic or sufficiently desperate."
    scene w3_3443 with pixellate
    mc "Did he see combat?"
    scene w3_3442 with dissolve
    abel "According to his record, yes. He was recognized for his valor even."
    abel "On paper, he's a commendable man, but after extending his contract a couple of times, he came to the States where he worked for various unsavory sorts."
    scene w3_3443 with dissolve
    mc "...couldn't a man with his experience have landed more legitimate work?"
    scene w3_3444 with dissolve
    abel "That's a good question. There are certainly companies that will overlook and vouch for those with questionable legal status, but that's not the direction he took."
    scene w3_3443 with dissolve
    mc "What kind of jobs did he do?"
    scene w3_3575 with dissolve
    abel "The high-risk kind, the sort you contract out so it doesn't lead back to you."
    scene w3_3574 with dissolve
    mc "Oh..."
    scene w3_3575 with dissolve
    abel "As you know, he now guards a brothel. Maybe he didn't take to his old work, or maybe this is just less risk and more steady pay for him."
    scene w3_3574 with dissolve
    "I certainly understood the pay angle..."
    mc "Since you're naming sins, what about Dr. Kohler?"
    scene w3_3576 with dissolve
    abel "He is the most interesting of the bunch, isn't he?"
    scene w3_3439 with dissolve
    mc "Some of the girls made him sound scary, but he's just the money, right?"
    scene w3_3438 with dissolve
    abel "He's everything you imagine him to be, but worse."
    scene w3_3440 with dissolve
    abel "Charles Kohler made a fortune on war profiteering, bribery, falsification of documents, {b}state-sanctioned smuggling.{/b} He's done a lot for his country."
    scene w3_3432 with dissolve
    mc "{i}State{/i}-sanctioned smuggling?!"
    scene w3_3578 with pixellate
    abel "Yes. As a necessity, weapon manufacturers tend to have strong ties to the various alphabet agencies. Some more than others."
    abel "And your Dr. Chuck is indeed a true American hero and a self-made man - {b}he's also an irredeemable nihilist{/b} of the lowest order, but that's just my personal disdain coming through."
    mc "He worked for the government?"
    abel "He worked for himself."
    mct "(...he always just painted himself as a guy who lucked out that one of his designs worked and got picked up.)"
    scene w3_3444 with pixellate
    abel "Truthfully, a man like Charles doesn't commit any sins that you can specifically point to. The importance and reach of his work affords him quite the umbrella."
    scene w3_3443 with dissolve
    mc "...that really doesn't change anything for me."
    scene w3_3442 with dissolve
    abel "Shouldn't it?"
    scene w3_3443 with dissolve
    mc "Either way he was never the man I remembered, but this helps everything fit."
    scene w3_3442 with dissolve
    abel "Glad to be of some service."
    scene w3_3443 with dissolve
    mc "...can I be frank?"
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
    scene w3_3448 with dissolve
    mc "I'm sure some people would disagree with you on that."
    scene w3_3447 with dissolve
    abel "Comparatively harmless."
    scene w3_3446 with dissolve
    mc "...and all this is meant to caution me about my environment, because of a boy you used to know?"
    scene w3_3449 with dissolve
    abel "You're young; you have your whole life ahead of you. You may even make something of yourself if you keep your head up and your eyes open."
    abel "Success is built upon and sustained by reading the wind and the changing tides. Nothing in this world lasts forever, from vaunted intuitions, to your favorite ice cream shop, and especially criminal enterprises."
    scene w3_3579 with dissolve
    abel "Organizations like yours are prone to shakeups. Not saying anything will happen, but pay attention."
    scene w3_3451 with dissolve
    abel "If you ever find yourself in a bind, give Sophia a call. You should have her personal number now."
    play sound "sound effects/sms-chime.wav"
    scene w3_3452 with dissolve
    "*Boop!"
    scene w3_3453 with dissolve
    mc "What kind of bind would I find myself in?"
    scene w3_3454 with dissolve
    abel "Perhaps the kind that would see your home bugged and surveilled. Do you know who lived here last?"
    scene w3_3453 with dissolve
    mc "I do..."
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
    mc "Wait...!"
    mc "Why are you {i}really{/i} here? This is all too vague and seemingly pointless. I'm having a hard time believing it's out of a sense of altruism."
    scene w3_3461 with dissolve
    abel "I'm not like you, [mcf]. Nor am I like the men who surround you. I think about others all the time; it's a prerequisite of my calling."
    scene w3_3580 with dissolve
    abel "Think about it: what could I {i}possibly{/i} get from a nobody like you?"
    abel "Makes no sense. Absolutely none at all."
    scene w3_3461 with dissolve
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
    mct "(Makes no sense, huh?)"
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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
