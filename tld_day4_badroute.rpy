label tld_day4bad:

# (Previous positions)
# show logan normal at Position(xpos = 0.75) with dissolve
# show remy normal flip at left with dissolve

if kol_tld_wtpchosen == True:
    Lg normal "All three of us are going to the water treatment plant so that we can start with our repairs, since we only did some rough scouting yesterday."

else:
    Lg normal"All three of us are going to factory so that we can start with our repairs, since we only did some rough scouting yesterday."

Lg "Any objections?"
Ry normal flip "I'm all set."
c "None."
Lg "In that case, we’ll begin immediately."
Ry look flip "Can’t we just wait for a while? I still need to get my bearings."
Lg serious "You had all morning to get your bearings, Remy."
Lg "It’s best that we don’t waste any more time than is necessary."
Ry "I understand."
Lg normal "Now, let’s get going, shall we?"

hide logan with dissolve
hide remy with dissolve

m "The three of us left my house, with Remy being the last to exit."

$ renpy.pause (1.0)
scene city at Pan ((0, 360), (0, 0), 5.0) with dissolve
$ renpy.pause (7.0)

scene kolcitycentre at Pan ((0,180),(0,180), 3.0) with dissolve
$ renpy.pause (2.0)

m "We went through the streets in silence, causing me to wonder what Logan was scheming this time. I looked at Remy, but he didn’t seem like he wanted to talk. Eventually, Logan broke the silence."

show logan normal at Position(xpos = 0.75) with dissolve
show remy normal flip at left with dissolve

Lg "We won’t need to make a stop at my place, as I already made some preparations."
Lg "Luckily I had a spare wheelbarrow to haul all those extra electronics around."
c "Since when did you have a wheelbarrow?"
c "Last I checked, you weren’t really the gardening type."
Lg smiling "That question can be easily answered!"
Lg serious "I’m not."
Lg normal "So I simply {i}barrowed{/i} it from one of the military camps."

menu:
    "I didn’t think that you were the type to steal.":
        $ renpy.pause (0.5)

        Lg serious "Well, desperate times call for desperate measures."
        Lg "And besides, who will use this anyway?"
        Lg normal "As far as I’m concerned, this entire city is free real estate."

    "Couldn’t you at least have asked permission first?":
        $ renpy.pause (0.5)

        Lg serious "{i}From who?{/i}"
        Lg "The person who it belonged to?"
        Lg "The {i}authorities{/i}?"
        Lg "Let’s be honest here [player_name]. Nobody is going to miss a wheelbarrow."
        c "Still, it isn’t right to steal anything, even if nobody will be using it"
        Lg "Fine, will it make you feel better if I returned it later?"
        c "It would."

        $ renpy.pause (0.5)

        Lg "That was a rhetorical question, [player_name]."

    "How unusual of you to make a pun.":
        $ renpy.pause (0.5)

        Lg "Hey, I just had to, alright?"
        Lg "I know that I hate puns with every fibre of my being, but even {i}I{/i} had to take that opportunity."
        c "Just be careful with any given opportunity. We wouldn’t want to start {i}soiling{/i} the mood now, would we?"
        $ renpy.pause (1.5)
        Lg serious "..."
        Lg "Damn it, [player_name]."



$ renpy.pause (0.5)

if kol_tld_wtpchosen == True:
    m "We continued to walk in the middle of the roads for some time. Eventually, we reached the water treatment plant."

    $ renpy.pause (2.0)
    scene kolwtpout at Pan((0,0),(0,60),4.0) with dissolve
    $ renpy.pause (2.0)

else:
    m "We continued to walk in the middle of the roads for some time. Eventually, we reached the factory."

    $ renpy.pause (2.0)
    scene kolfactoryout at Pan((0,0),(0,60),4.0) with dissolve
    $ renpy.pause (2.0)

m "Unsurprisingly, it looked exactly the same since we left it."

show logan normal at Position(xpos = 0.75) with dissolve
show remy normal flip at left with dissolve

Lg "Alright, we’re here."
Lg serious "We have a lot of work to do, so let’s make this quick."
Lg "I devised a plan last night based on what we found here yesterday."

if kol_tld_wtpchosen == True:
    Lg "I checked the building materials you found. All I can say is that it won’t be enough to fully repair the plant."
    Lg "However, they should cover most of the basic damage, and maybe some of the more severe degradation as well."
    c "Did you find anything that could help us repair the water purifiers?"
    Lg "Sadly, no."
    Lg "Like I said, however, I think that they only need some power and a few minor repairs to get up and running again"
    Ry "I assume that you’ll be going to the purifiers to try to get them up and running, correct?"
    Lg normal "You assumed correctly."
    Lg serious "As for you two, I recommend that you and [player_name] prescribe a healthy dose of repairs to a nearby ruined building." #Sounds a bit strange, but whatever
    Lg "I brought some spare tools that may be useful, as well as moving all the supplies closer to the entrance for your convenience."
    c "Got it. Good luck, Logan."
    Lg "No need for luck, [player_name]. Only effort and time."

    stop music fadeout (2.0)
    $ renpy.pause (1.0)
    scene kolwtp3 at Pan ((0, 0), (0, 127), 4.0) with dissolve
    $ renpy.pause (3.0)
    play music "mx/surge_kol.ogg" fadein 1.0

    m "Me and Remy entered the water treatment plant, weary of any other accidents that might happen this time. After looking for a while, we found all the tools that Logan left us, as well as all the supplies that I found."

    show remy normal with dissolve

    Ry smile "Looks like Logan already sorted everything for us."
    c "How nice of him."
    Ry normal "It does make me wonder, though. When did Logan have the time to do all of this?"
    Ry look "Surely he doesn’t prepare everything {i}that{/i} early in the morning."

    menu:
        "Oh, but he does.":
            $ renpy.pause (0.5)

            c "Here’s a neat piece of trivia for you. He does, in fact, prepare everything that early in the morning."
            c "And he’s been doing it ever since I first met him."
            Ry "I don’t think that I could ever wake up that early, let alone already start working."
            Ry normal "Even when I was working under the council, I didn’t have to wake up nearly as early as Logan seems to do."
            c "Well, Logan is a special kind of person that just loves to give sleep the middle finger."
            Ry look "The... middle finger?"
            c "Let’s just say that it’s a very rude gesture."
            Ry "I see..."


        "Maybe we should ask him?":
            $ renpy.pause (0.5)

            Ry shy "I don’t think that’s such a good idea."
            c "Why not?"
            Ry "Well..."
            Ry "He would probably rant about “How all this is necessary for the survival of the city!”, or “I’m just trying to keep this city afloat!”..."
            Ry normal "None of which I’m particularly eager to sit through."
            c "That’s a surprisingly accurate impression of Logan."
            Ry smile "Thank you, [player_name]."


        "I wonder as well sometimes.":
            $ renpy.pause (0.5)

            Ry "Wait, you do?"
            c "Of course. For as long as I’ve known him, Logan always tended to keep to himself."
            c "Especially when it comes to bad habits like his sleeping schedule."
            c "To be honest, it’s a miracle how I ever found that out."
            Ry shy "Well, how {i}did{/i} you find out?"
            c "In a nutshell: I heard many things, saw fewer, and witnessed less."
            Ry "I’m a bit confused as to what you said. Could you maybe clarify that?"
            c "I heard some rumours about Logan once and tried to investigate, which ended up with me finding out that his sleep schedule is next to non-existent."
            Ry normal "Ah, that makes more sense now."
            c "You’re welcome."


    $ renpy.pause (0.5)

    c "In any case, we should probably get to work. I’ll start with mixing the cement."
    c "Do you think that you’ll be able to get some water for me?"
    Ry normal "I can try. That is, if you have an idea as to where I can get some water."
    c "There’s an area with water tanks just outside one of the fire exits that you can get some clean water from."
    c "Luckily, Logan has already provided us with suitable buckets for perfect water scooping, so you could just use those."
    c "The water tanks shouldn’t be hard to miss, as it’s close to some of the only greenery in the entire city."
    Ry "Alright. I might be gone for a while, as carrying water without spilling it may be a bit too tricky for me. I will try to be quick, though."

    hide remy with easeoutleft

    m "Remy carried two buckets in his mouth and left the room. I waited for some time until he came back, slowly putting the filled water buckets on the floor."

    show remy normal flip with easeinleft
    show remy normal with dissolve

    Ry "I’m back, [player_name]. Hopefully I didn’t take too long."
    c "Not at all, Remy. Now we can finally start with the repairs."
    c "Out of curiosity, have you ever done something like this before?"
    Ry "I can’t say that I have."
    c "Looks like you’ll get to experience something new, then."

    hide remy with dissolve

    m "I explained to Remy how to mix the cement so that it can be used for reconstruction. I also explained how you should use the cement with the bricks to patch the walls."

    show remy shy with dissolve

    Ry "I... think that I understand."
    Ry "Should I mix the cement, or try and repair the broken walls?"
    Ry "It seems that you have far more experience in construction than me, so I’d like to hear your opinion."

    menu:
        "Mixing the cement will be the better choice.":
            $ renpy.pause (0.5)

            Ry "How so?"
            c "Well, I figured that spreading the cement on the bricks and placing them together might be a bit too precise for you."
            c "Mixing the cement only takes someone adding water to the powder and mixing."
            Ry normal "You do have a point there. Even if my hands were more dexterous, they’re far too big to be able to effectively patch the holes."
            c "Do you think that you’ll be comfortable with all this?"
            Ry "Well, I don’t have much of a choice, really. I’ll just have to try and help in any way I can."
            c "I understand."
            c "Oh, and for the reference:"
            c "I do {i}not{/i} have experience with construction work. I have a degree in biology, {i}not{/i} engineering."
            c "All I did was pick up a few things back while I was trying to keep myself afloat."
            Ry shy "My apologies, then. I just assumed that you would know a lot about things like this."
            c "Don’t worry about it, Remy. Now, let’s get started, shall we?"
            Ry normal "Now, let’s get started, shall we?"

            hide remy with dissolve

            m "I then prepared to mix the cement for Remy while he patiently waited for me. Afterwards, Remy started to fix the holes, albeit at a fairly slow pace. As he approached the end of his first huge hole, however, I could see that he struggled to push the last few bricks in."
            c "Here. Let me help you."
            Ry shy "Thank you, [player_name]."
            m "I placed the final bricks in, making sure that the cement is spread evenly among the gaps."
            c "There we go. That’s one huge hole finished."

            $ renpy.pause (0.5)

            c "Now for the rest..."


        "Patching the holes is probably the easier task.":
            $ renpy.pause (0.5)

            Ry "How so?"
            c "Well, since we don’t have a cement mixer with us, we’ll have to do everything by hand."
            c "I figured that you might have a bit of a hard time trying to get everything consistent enough, so having you patch up the holes seems like the better choice."
            Ry normal "Well, I guess you’re right. It would be a bit tricky for me to try and get everything mixed enough."
            c "Do you think that you’ll be comfortable with all this?"
            Ry "Well, I don’t have much of a choice, really. I’ll just have to try and help in any way I can."
            c "I understand."
            c "Oh, and for the reference:"
            c "I do {i}not{/i} have experience with construction work. I have a degree in biology, {i}not{/i} engineering."
            c "All I did was pick up a few things back while I was trying to keep myself afloat."
            Ry shy "My apologies, then. I just assumed that you would know a lot about things like this."
            c "Don’t worry about it, Remy. Now, let’s get started, shall we?"
            Ry normal "Now, let’s get started, shall we?"

            hide remy with dissolve

            m "I waited a bit for Remy to start mixing the cement before I started. At first I could see him struggling, but he soon adapted, mixing the cement at a fairly even and fast pace."
            m "At least, for a dragon like Remy."
            m "I attempted to spread the cement evenly on the bricks. However my attempts weren’t without some complications, as some chunks of powder still remained after the mixing."
            c "Maybe you should try mixing like this."
            Ry shy "Yeah, that looks a bit better. Thanks."
            m "Afterwards, the cement was consistent enough for constant use. Soon, the entire wall was repaired."

            show remy shy with dissolve

            Ry "I don’t think that I can feel my arms anymore."
            c "Don’t worry, Remy. You did a great job."
            c "Now for the rest..."



    $ renpy.pause (0.5)
    stop music fadeout (2.0)
    play sound "fx/explosion.ogg"
    $ renpy.pause (2.5)

    m "Suddenly, I heard a large explosion from deeper within the building, as well as the sound of something collapsing. This was also followed by some loud swearing."
    Ry "Should we-{w=0.5}{nw}"
    c "Yeah, we should. Let’s go."

    $ renpy.pause (1.0)
    scene kolwtp4 at Pan ((0, 20), (0, 142), 5.0) with dissolve
    $ renpy.pause (3.0)

    m "Me and Remy proceeded to go to the source of the noise, looking to see what part of the plant collapsed this time. Eventually, we found Logan, who looked extremely distraught."

    show logan surprised flip at Position(xpos=0.25) with dissolve
    show remy look at right with dissolve

    Lg "This damned building will be my sarcophagus one day, I swear it."
    Ry look "What happened to you? You look like you’ve seen a ghost."
    Lg "I might as well be a ghost, Remy."
    Lg serious flip "Another part of the building collapsed, but this time, on one of the purifiers."
    Lg "And the worst part: The generator I used caused this, since the purifier I had been working on, turns out, {i}couldn't{/i} handle the power supply."
    Lg "It’s a real shame, as well. Can’t even retrieve the parts or salvage the purifier and generator for scraps."
    Lg "Heck, I probably don’t even have enough parts left to fully repair all the purifiers, let alone everything else in this damned city, since the rubble has also crashed onto a nearby heap of spare parts."
    Lg "I guess that I could try and salvage some, but I doubt anything would be working now."
    Lg "Fate truly does have a sick, demented mind."

    menu:
        "At least you’re safe.":
            $ renpy.pause (0.5)

            Lg "What does it even matter, though?"
            Lg "It’s either that I died here under the rubble, or die later when we run out of clean water."
            c "Don’t think like that when there is still some hope left. After all, you still have some spare parts left, as well as the other purifiers."
            c "Sure, we may only have two generators left, but it's till manageable."
            Lg "Not if there aren’t any usable parts left that are compatible with the purifiers. Or if the last generators also blow up."
            Lg "Just more monotonous work for later, I guess."


        "You should have been more careful.":
            $ renpy.pause (0.5)

            Lg "Not sure how I could have been more careful if a literal generator exploded in front of me and almost caused me to be crushed under a heap of debris."
            Lg normal flip "Oh, I know! I simply could have worked outside where nothing could have collapsed!"
            Lg "All I needed to do was to carry the several purifiers that weighed literal tonnes and worked in an area where dust might interfere with the electronics!" #The sass is real here
            Lg "How foolish of me!"
            c "No need to be sarcastic, Logan. I’m just trying to help."
            Lg serious flip "And I’m just trying to point out the flaws in your logic."


        "Any ideas as to how you could fix this?":
            $ renpy.pause (0.5)

            Lg "Here’s the short answer: I do not."
            Lg "And I’m pretty sure that I won’t have any idea for quite some time."


    Ry "Is there anything we could do to help you out now?"
    Lg thinking flip "Not that I could think of. I’ll have to try and think about what our next plans are."
    Lg serious flip "Regardless, I think that you two should continue with y-{w=0.75}{nw}"

    $ renpy.pause (0.5)
    play sound "fx/wind_kol.wav"

    m "An abnormally large gust of wind interrupted Logan. Logan started to look extremely frustrated and confused at the same time."
    Lg "What is it this time?"
    Ry shy "I... don’t have any idea. I could go and check outside, if you want."
    Lg "Screw it, I’m going with you. Might as well see how much the universe hates me now."
    c "Should I-{w=0.45}{nw}"
    Lg "You don’t even need to ask."

    $ renpy.pause (0.5)
    scene kolwtpoutstorm at Pan ((0, 0), (0, 80), 2.5) with dissolve
    $ renpy.pause (2.0)

    m "The three of us went outside to the water treatment plant grounds to see what was causing the sudden intense wind. That question was soon answered when we looked at the skies, however."
    m "A storm was approaching."

    show koldarkclouds at Pan ((580,608), (0,0), 12.0) with fade
    $ renpy.pause (10.0)
    hide koldarkclouds with fade

    play music "mx/ashes_kol.ogg" fadein 1.0

    show logan surprised flip at Position(xpos=0.25) with dissolve
    show remy look at right with dissolve

    Lg "You can’t be serious."
    c "Wait. Why is there a storm here? {i}How{/i} could there be a storm here?"
    Lg "HOW THE HECK SHOULD I KNOW?!" with Shake ((0, 0, 0, 0), 3, dist=20)
    Lg "Nothing here makes even any sense anymore!"
    Lg serious flip "Last I checked, storms, especially of {i}that{/i} size, didn’t just casually wander into the desert unnoticed!"
    Lg "Damn it all! I don’t think that this building would survive the winds or rain. Even more hard work just wasted!" with Shake ((0, 0, 0, 0), 2, dist=10)
    m "Despite Logan’s ranting, he appeared to be deep in thought. Soon, however, he did what he always did best."
    m "He came up with a plan."
    Lg thinking flip "The rain caused by this storm will definitely damage a lot of infrastructure here in the city, considering that most buildings here are very much {i}not{/i} waterproof."
    Lg "To try and fix all of them at this time is a fool’s errand, so here’s what we’re gonna do:"
    Lg serious flip "I’ll be off trying to minimize the potential damage to the purifiers and anything else that may endanger them."
    Lg "Remy, can you fly close to the storm to give an approximation of the potential damage we’re facing?"
    Ry shy "I think so. I never fly when a storm is this close, but I should be able to make an educated guess on where the storm is heading, as well as the potential damages the rain and wind might cause."
    Lg "Considering that we don’t have a weather specialist, you’ll have to do."
    Lg "That leaves only you left, [player_name]."
    Lg "Despite the huge pit we landed in right now, there’s some opportunity to be had."
    Lg "I want you to open the valves for the water tanks so that any spare water that may flow will end up in them."
    Lg "If this place is going to get flooded, then you best be sure that clean water would be essential."
    Lg "Just make sure to not open the valves that already contain purified water, though. Don’t want excess muck to mix with that oh so precious disease-free water."
    c "Got it. Anything else?"
    Lg "Nothing. Let's go!" with Shake ((0, 0, 0, 0), 1.5, dist=13)

    hide logan with dissolve
    hide remy with dissolve
    play sound "fx/takeoff.ogg"
    $ renpy.pause (1.5)

    m "Remy quickly took off to the skies, while Logan went back inside. I rushed to the area that had the water tanks."

    $ renpy.pause (0.5)
    scene kolwatertank at Pan ((0, 0), (5, 80), 2.5) with dissolve
    $ renpy.pause (2.0)

    m "I could see that there were entire sections with water tanks, with each their own individual pumps."
    m "Upon looking around, I eventually saw a wall with numerous valves, each being coloured to indicate what tank they were connected to."
    c "(Here goes nothing...)"
    m "I mustered all the strength I could and turned the valves, with each one somehow being tighter than the next."

    $ renpy.pause (1.0)

    c "(Come on, budge!)"

    play sound "fx/wheels.ogg"

    m "With enough effort, however, the valves that opened the pipes to the empty and partially clean water tanks were open. I then opened the corresponding valves on the water tanks themselves so that water could actually flow inside them."
    m "After some time, all the water tanks were now ready to receive rain water."
    c "(How did Remy even get the water for the cement in the first place when all of the valves are so tight?)"

    $ renpy.pause (4.0)
    scene kolwtp3 at Pan ((0, 0), (0, 127), 4.0) with dissolve
    $ renpy.pause (3.0)

    m "I rushed back inside the water treatment plant to report to Logan about the success of my task."
    m "However, when I found him, he was already busy talking to Remy."

    show logan normal flip at Position(xpos=0.25) with dissolve
    show remy normal at right with dissolve

    Lg "I’ll admit, that’s quite the relief."
    Lg serious flip "Still, nothing to be relaxed about, but that should give us the hope we need."
    Ry shy "Do take note that I could be wrong. After all, this is just an educated guess."
    Lg normal flip "An educated guess is way better than nothing, and I’m thankful for that."
    c "I assume that Remy has some good news, right?"

    $ renpy.pause (1.0)

    Ry "Oh, hello [player_name]. I didn't see you come in."

    $ renpy.pause (1.0)

    Ry smile "Yes, I do have some good news."
    Ry normal "It looks like the storm will just barely hit us, with the heaviest blows not even reaching our city."
    Ry "If I had to guess, we should still be safe."
    Ry look "For the most part."
    Lg serious flip "Even then, we can’t let our guard down, especially with that ever looming threat of raiders potentially coming here."

    $ renpy.pause (0.5)
    stop music fadeout (15.0)

    Lg normal flip "In any case, I can see that you two are exhausted."
    Lg "Take the rest of the evening off to try and waterproof anything that you can."
    c "I don’t think that there really is much to waterproof at my house, except for maybe some broken appliances."
    Lg thinking flip "Lucky you, then."
    Lg serious flip "I’ll just stay here and continue to minimize the potential damage. You can never be too sure, after all."
    c "But shouldn’t you-{w=0.65}{nw}"
    Lg "No, [player_name]. This is far more important." #DAmn, Logan really does like shutting the MC down, doesn't he?
    Lg "And no, I won’t accept your help now. Spend the last few minutes or however much we have left before the storm hits on yourselves."
    Ry look "And what about you? Where are you going before the storm hits?"
    Lg "I’ll either stay here or try to go home in the rain and wind."
    Lg normal flip "Now, are you just going to waste your precious time by standing here?"
    c "Thanks, Logan."
    Lg "Don’t mention it."
    Lg serious flip "Seriously."

    scene black with fade
    $ renpy.pause (6.0)


    jump tld_day4end





else:
    Lg "I checked the food stash you found, [player_name]. It should last us about a month."
    Lg thinking "Maybe more, if we start rationing when our current food supplies run out."
    c "And what about the machines?"
    Lg serious "I looked at your PDA some more and found the blueprints for the machines in the factory."
    Lg "It’s going to be a lot of hard work and frustration, but I believe that I {i}could{/i} get it to a state where it {i}would{/i} maybe function again."
    c "That’s a lot of promises."
    Lg normal "Well, not much that I could deliver when all the advanced electronics are fried a la solar flare."
    Ry look flip "But you could still fix it, right?"
    Lg serious "I'll try. That's all I can say."
    Ry normal flip "I see. In any case, how could me and [player_name] start working?"
    Lg "There should be some tools in a storage room nearby that you could use to start salvaging some usable parts for building materials."
    Lg normal "Do try to decommission the less valuable facilities, though. If anything useful breaks, then we’re screwed, to put it lightly."
    c "Seems easy enough."
    Lg serious "Everything seems easy enough at first."
    Lg "Now, I’ll be off to try and rewire some machines. Come and get me when you need anything."

    show logan normal flip with dissolve
    hide logan with easeoutright
    $ renpy.pause (1.5)

    Ry "I’ll be off getting the tools, then. Where should I get you, [player_name]?"
    c "I think that I’ll just wait for you here."
    Ry shy flip "Alright then."

    hide remy with dissolve

    m "Remy went around the factory in search of the storage room while I waited for him at the entrance."
    m "Remy soon reappeared carrying a large toolbox, as well as a sledgehammer in his mouth. As he set the tools down, I could hear him giving a sigh of relief."

    show remy normal with dissolve

    Ry smile "Whew, that was uncomfortable to carry."
    Ry normal "I didn’t think that a sledgehammer could be so heavy."

    menu:
        "Well, it {i}is{/i} a sledgehammer, after all.":
            $ renpy.pause (0.5)

            Ry "Well, you do have a point. It’s just that it’s quite hard having to carry something heavy like that while making sure not to trip over something."
            Ry shy "Especially while already carrying something else."
            c "Like the books at the library?"
            Ry look "..."
            c "I’m sorry. I shouldn’t have brought that up."
            Ry "It's fine."


        "At least you managed to get all the tools.":
            $ renpy.pause (0.5)

            Ry "Well, not really. I only got the things that I thought would be necessary."
            c "For someone who doesn’t know a lot about construction, you sure did make a good guess on which tools would be necessary, though."
            Ry smile "I guess I did."


        "Maybe I should have helped you, then.":
            $ renpy.pause (0.5)

            Ry "Oh, there was no need."
            Ry smile "I mean, I {i}did{/i} manage to get the tools, didn’t I?"
            c "But you didn’t look comfortable at all while carrying them."
            Ry shy "I guess you got me there. I don’t think I’m suited at carrying a bunch of things all at once."
            Ry look "My job was more than enough evidence of that."



    $ renpy.pause (0.5)

    Ry normal "In any case, let’s get started."
    stop music fadeout (2.0)

    $ renpy.pause (1.0)
    scene kolfactory3 at Pan ((0, 0), (0, 127), 4.0) with dissolve
    $ renpy.pause (3.0)
    play music "mx/surge_kol.ogg" fadein 1.0

    m "We entered the facility with the tools, seeing that, just like the exterior, nothing has changed since our last visit. I expected to see some piles of electronics that Logan had apparently brought with him, but couldn’t see any."
    c "(Guess that Logan took all those parts with him to the central facility, then.)"

    $ renpy.pause (1.0)
    scene kolfactory4 at Pan ((0, 0), (0, 0), 4.0) with dissolve
    $ renpy.pause (2.0)

    m "We wandered around, looking for anything that could be salvaged."
    Ry normal "[player_name]! Over here!"
    c "Found something?"

    show remy normal with dissolve

    Ry "Yeah. It seems like the wall over here can be broken down for some spare pieces of concrete. As an extra bonus, it doesn’t seem to support anything, so tearing it down is safe."
    c "Good work spotting that. Now, stand back while I swing the sledgehammer, please."

    hide remy with dissolve

    m "I took the sledgehammer and swung it at the centre of the wall with all my might. The wall soon fell over, leaving a few concrete bricks left standing that were already loose from the wall, as well as a large heap of concrete chunks."
    c "(That was easier than I thought it would be. Guess these walls were worse off than I thought.)"

    show remy normal with dissolve

    c "That should do it. Most of these pieces seem to be usable in some way."
    c "These should be good for repairing a few holes in the walls near the entrance, don’t you think?"
    Ry smile "Well, they are certainly more useful now than they were a while ago."
    c "I very much agree."
    Ry normal "Should we leave these pieces here for now, or should we try to carry them someplace else?"
    c "I think that we should take it closer to the entrance so that we don’t constantly have to carry them around."
    c "If we are able to sort any additional resources into separate piles, we shouldn’t have to waste more time transporting and gathering them."
    Ry "I guess you do have a point."

    $ renpy.pause (1.0)
    scene kolfactory3 at Pan ((0, 0), (0, 0), 2.5) with dissolve
    $ renpy.pause (2.0)

    m "Me and Remy spent the next several minutes sorting and carrying the chunks of concrete that we could use to repair the factory."
    c "Good job, Remy. It looks like you have a real knack for sorting things."
    Ry smile "Thank you, [player_name]. Looks like all that experience with carrying books and scrolls finally paid off."

    show remy normal with dissolve

    $ renpy.pause (1.0)
    m "We exchanged a quick glance before returning to our work."
    $ renpy.pause (0.5)

    c "Do you have any recommendations as to what we should do next?"
    Ry "I would suggest getting some scrap metal, but I think that it would be a bit of a hassle picking some scraps up and trying to pry others from whatever parts we can."
    c "How about we salvage soom wood, instead?"
    Ry "I suppose we could. I did see a bunch of crates and shelves in some of the storage rooms, as well as a few planks randomly laying about."
    c "Off to the storage rooms, then!"

    $ renpy.pause (1.0)
    scene kolfactory4 at Pan ((0, 0), (0, 0), 4.0) with dissolve
    $ renpy.pause (2.0)

    m "We went to the storage rooms to see whether any wood could be used for construction. Luckily, we found a bunch of empty crates, as well as a few stray planks. In the end, we were able to gather a surprising amount of wood."

    $ renpy.pause (1.0)
    scene kolfactory3 at Pan ((0, 0), (0, 0), 2.5) with dissolve
    $ renpy.pause (2.0)

    m "Me and Remy went back to where we had the pile of concrete bricks while carrying the wood. Sadly, I couldn’t carry them for too long before needing a break."
    c "Wait, Remy."

    show remy look with dissolve

    c "I really need a small break. I don’t think that I’m suited to carry this much stuff for so long."
    Ry normal "Good idea. All this work has made me a bit tired."
    Ry smile "{i}Wooden{/i} you agree?"

    menu:
        "That’s a good one.":
            $ renpy.pause (0.5)

            Ry "Thanks. I have been practicing a bit recently."
            Ry normal "After all, there has to be something that I can do to keep the morale high."
            Ry smile "Even if a certain somebody doesn’t like it that much."
            c "Well, I’d say you’re doing a great job so far."
            Ry "I’ll be sure to keep up the good work, then."


        "That’s two puns today. Want to make it {i}tree{/i}?": #Pun wars are the best types of wars you could get tbh
            $ renpy.pause (0.5)

            Ry normal "Well, I guess you just did."
            Ry smile "I wonder {i}four{/i} how long you could keep up, though."
            c "My, you're quite good. I’ll have to use every {i}five{/i}r of my being to continue our little game."
            Ry "Well, maybe we’ll be able to get it to ten if you can go on. Then it would be a great {i}six-s{/i}!"
            c "Let’s just hope that I can keep this going. I wouldn’t want to {i}seven{/i} our progress so far by suddenly hitting a blank."
            Ry "I don’t think that that was your best joke so far, but I do appreci{i}eight{/i} it nonetheless."
            c "Yeah, that joke was a bit too asi{i}nine{/i}."
            Ry "At least you were {i}ten{/i}acious through the entire ordeal."
            c "And looks like we did it. I’ll admit, that was pretty fun."
            Ry normal "I agree. You have quite some skill when it comes to puns."
            c "Not as good as you, though. You were amazing at coming up with puns like those."
            Ry shy "Practice does come a long way, after all."


        "Now isn’t the time for puns.":
            $ renpy.pause (0.5)

            Ry look "I’m sorry, [player_name]. I shouldn’t have gotten distracted from our work right now."
            Ry "Especially when there’s so much at stake."
            Ry "I’ll just pretend that it never happened."



    $ renpy.pause (1.0)

    Ry normal "Now, let’s get back to work. Are you ready, [player_name]?"
    c "As ready as I can be. Let’s just hope that all this carrying around won’t cause me some sore muscles in the morning."

    hide remy with dissolve

    m "We started to carry the wood again, albeit at a much slower pace than before. Eventually, we did reach the area where we decided all the spare materials should go, even if my body started to ache a bit."

    show remy normal with dissolve
    $ renpy.pause (3.5)

    c "There we go."
    c "Hopefully that should be all the things we need to carry, for now. I honestly don’t know how much more physical labour I can do today."
    Ry look "I understand how you feel, [player_name]."
    Ry "Back at the library, I used to carry so many boxes filled with artifacts when I’m not researching anything for the council."
    Ry shy "Some of which weren’t very light, as you may imagine."
    c "Well, I do think that you'd be able to do a better job here than at the library, as you don’t need to be as careful here."
    c "Emphasis on {i}as{/i}."
    Ry "Thanks, [player_name]."
    Ry normal "Now that you mentioned working here, I wonder how Logan is doing."
    c "If I had to guess, he’s probably busy with-{w=0.70}{nw}"

    $ renpy.pause (0.5)
    stop music fadeout (2.0)
    play sound "fx/explosion.ogg"
    $ renpy.pause (2.5)

    m "Suddenly, I could hear a loud explosion coming from the central facility, followed by some intense swearing."
    c "...exploding electronics."
    Ry look "We should go help him, then. That sounded really bad."
    c "Yeah. Let’s go."

    $ renpy.pause (1.0)
    scene kolfactory1 at Pan ((0, 20), (0, 142), 5.0) with dissolve
    $ renpy.pause (3.0)

    m "We rushed to the main facility and looked for Logan, only to find him surrounded by broken pieces of metal. When he turned to face us, I could see that he was in a state of disbelief."

    show logan surprised flip at Position(xpos = 0.25) with dissolve
    show remy look at right with dissolve

    Lg "Oh, it’s you two."
    Ry "Is everything alright, Logan? We heard an explosion and we figured that you might be in danger."
    Lg serious flip "Well, I’m alright as of now."
    Lg "But we won’t be soon enough."
    c "What are you talking about?"
    Lg "One of the generators didn’t respond so well with the condition of the machines."
    Lg "Despite everything I did that bypassed faulty pieces and to replace others, the generator simply couldn’t handle it."
    Lg "In short, we now only have a single usable generator left."
    Ry sad "Only one? I thought that we had three in total."
    Lg "I put aside one to see how they functioned so that I could try and make my generators more efficient, remember?"
    Lg "Until then, there’s nothing we can do to power the factory. All we can do now, however, is to try and fix the infrastructure."
    Lg "Anything else is far beyond my current skill level, impressive as it may be."

    menu:
        "At least you tried.":
            $ renpy.pause (0.5)

            Lg "Trying isn’t going to get us anywhere in this city, [player_name]. You should know that by now."
            Lg "Only results will."
            Lg "And as you can clearly see, the results here are a failure."


        "Well, it brought us this far.":

            c "Your skill has already brought us extremely far, Logan."
            c "Without you, we probably wouldn’t even have considered repairing the factory."
            c "What’s stopping you now from only getting more and more successful and restoring this place to its former glory?"
            Lg "..."
            Lg "Resources."
            Lg "Remember, all the spare parts I have that still work aren’t exactly limitless."
            Lg "I need to strategize what would be the best course of action so that I don’t needlessly waste what I have left."


        "So, what now?":
            $ renpy.pause (0.5)

            Lg "You {i}did{/i} listen to what I just said, didn’t you?"
            Lg "We’re going to repair the infrastructure until we find a way to power the machines without causing any explosions."


    Lg normal flip "Regardless, thanks to those fruit snacks you found, we could keep going for just a while longer after our main supplies run out."
    Lg serious flip "Let’s just hope that I can find a way to get this place up and running before then."
    Ry normal " I wish you the best of luck then, Logan."
    Lg "I think that I’ll be needing a lot more than luck here, Remy."
    Lg "In any case, we should be going back to work. Did you start repairing anything yet?"
    c "Not yet."
    c "We did gather a few concrete bricks, a lot of concrete chunks and some wood, though."
    Lg "Not the most suitable items for repair, but it will have to do. Guess we'll j-{w=0.75}{nw}"

    $ renpy.pause (0.5)
    play sound "fx/wind_kol.wav"

    m "Logan was about to say something else, but got interrupted by an abnormally large gust of wind."
    Lg "The heck?"
    Lg "Why is it this windy all of a sudden?"
    c "Should I go outside and check?"
    Lg "I think that I’ll have to go with you on this one. You coming along, Remy?"
    Ry "I’d be happy to."

    $ renpy.pause (0.5)
    scene kolfactoryoutstorm at Pan ((0, 0), (0, 80), 2.5) with dissolve
    $ renpy.pause (2.0)

    m "The three of us left the factory to see what was happening on the outside. Our questions were soon answered when we looked up to the skies."
    m "A storm was approaching."

    show koldarkclouds at Pan ((580,608), (0,0), 12.0) with fade
    $ renpy.pause (10.0)
    hide koldarkclouds with fade

    play music "mx/ashes_kol.ogg" fadein 1.0

    show logan surprised flip at Position(xpos=0.25) with dissolve
    show remy look at right with dissolve

    Lg "Is that a damn storm?!"
    Lg "What?! {w}{i}How?!{/i} {w}This doesn’t make any sense!"
    Lg "WE ARE IN THE DESERT! WE SHOULDN’T BE ABLE TO GET STORMS, ESPECIALLY OF THAT SIZE!" with Shake ((0, 0, 0, 0), 5, dist=35)
    c "Calm down, Logan. We’ll be able to manage this."
    Lg serious flip "Oh? Do tell me how. I doubt that most of these buildings are able to handle heavy rain, let alone the flash flood that those clouds would probably bring."
    c "Maybe it won’t hit us as bad as you think it will."
    c "Remy, do you think that you’ll be able to fly to the storm and determine its route?"
    Ry shy "I think so. I never fly when a storm is this close, but I should be able to make an educated guess on where the storm is heading."
    c "That will be good enough."
    Ry "Alright. I'll be back."

    hide remy with dissolve
    play sound "fx/takeoff.ogg"
    $ renpy.pause (1.0)

    m "Remy took a few steps back before flying straight into the darkened sky."
    Lg "Alright, I have an important task for you, [player_name]."
    Lg "This facility isn’t waterproof enough for the electronics to stay here. The humidity alone would probably mess the electronics up."
    Lg "I’ll be needing you to take all the electronics I brought here back to my place as fast as you can. It’s probably the only place nearby where it would probably still function after the storm is over."
    Lg "Sadly, you’ll need to take the wheelbarrow, as nothing else here would be able to carry all of the electronics quick enough."
    c "I’m not sure that I’ll be able to-{w=0.75}{nw}"
    Lg "Shut it, [player_name]! The more you talk, the more time we waste." with Shake ((0, 0, 0, 0), 2, dist=10)
    Lg "I’ll stay here and wait for Remy. In the meantime, I’ll try to waterproof this place as much as possible."
    Lg "Now go, damn it!" with Shake ((0, 0, 0, 0), 1.5, dist=13)

    hide logan with dissolve

    m "I rushed back inside to grab the remaining spare parts that Logan used to try and fix the machines with."

    scene black with fade
    $ renpy.pause (1.0)

    m "Luckily, there were only a few things scattered around the floor, while most of it was already in the wheelbarrow."
    m "I took the wheelbarrow with me and ran outside the factory grounds as fast as I could, being extra careful not to drop anything."

    play sound "fx/wheelbarrow_kol.wav"
    $ renpy.pause (1.0)
    scene kolcitycentrestorm at Pan ((0,180),(0,180),3.0) with fade
    $ renpy.pause (1.0)

    m "A while later, I saw that Remy was flying in the sky on his way to Logan."

    $ renpy.pause (1.0)
    scene kolloganoutstorm at Pan ((0, 0), (0, 250), 5.0) with dissolve
    $ renpy.pause (1.0)

    m "Eventually, I reached Logan’s house with more than enough time to spare, as the storm didn’t seem to fully arrive at his house yet, unlike most of the city."

    $ renpy.pause (1.0)
    scene kolloganhousestorm at Pan ((0, 220), (0,360), 3.0) with dissolveslow
    $ renpy.pause (1.0)
    stop music fadeout (15.0)

    m "I entered the house, feeling exhausted after pushing the wheelbarrow so far."
    c "(That was way harder than I thought it would be. At least it's over now.)"
    m "I sat down on Logan’s couch to try and gather myself. Much to my surprise, however, Remy appeared at the entrance just as I settled down."

    show remy normal with easeinright
    $ renpy.pause (1.0)

    c "Remy! I didn’t expect you to come here after me!"
    Ry smile "Well, I just couldn’t leave you all alone, now could I?"
    c "Trust me, you can. I have handled far worse on my own."
    c "But enough of that. What's the news on the storm?"
    Ry normal "It looks like the storm will just barely hit us. It’s likely that we’ll receive some heavy rain, sure, but we should be mostly safe."
    Ry look "Emphasis on {i}mostly{/i}."
    c "I see. What was Logan’s response, then?"
    Ry normal "By the looks of it, I’d say that he was relieved."
    Ry "Of course, I could still see that he was really stressed, but I think that the news helped to somewhat calm his nerves."
    Ry look "Or so I think. It’s hard to read Logan’s emotions."

    menu:
        "I’ll have to agree with you.":

            c "Well, you’re right. I’ve known him for quite some time, and even I struggle to tell his emotions apart."
            Ry normal "I’m glad to not be the only one, then."


        "You just need to get to know him more.":
            $ renpy.pause (0.5)

            Ry normal "How long have you known him?"
            c "Quite a long time, actually. If I remember correctly, then I’d probably say a few months after I graduated from college."
            Ry look "In that case, there isn’t any hope for me on that front, then."
            Ry normal "Oh well."


        "Maybe he’s just good at hiding them?":

            c "I think that Logan might just have a skill for hiding his emotions from everybody, or, at the very least, make them hard to read."
            Ry look "That doesn’t sound particularly healthy for your mental wellbeing."
            c "Well, it’s just the kind of person he is."
            Ry normal "Maybe I shouldn’t worry about it too much, then."



    $ renpy.pause (0.5)

    c "Well, what will Logan do now?"
    Ry "He said that he’ll try to waterproof everything as much as he can before it starts to rain."
    Ry "Afterwards, he’ll try to keep a lookout for any raiders that might use the storm as cover."
    Ry "He also said that we should take the evening off to try and fix anything at our place if need be."
    c "Leave it to Logan to keep guard for raiders..."
    c "He really doesn’t know what a break is, does he?"
    Ry "Maybe he just doesn’t want to take them. Still, if it’s his choice to do the things he wants to do, then we shouldn’t judge him."
    Ry look "Now, about the part where we should see if we can waterproof our house..."
    c "I don’t think that the cracks in the walls would affect us too much, so we’re probably good."
    Ry "Are you sure about that, [player_name]?"
    c "Pretty sure. The cracks don’t go all the way through, so rain shouldn’t get in unless something happened that I wasn’t aware of."
    Ry normal "In that case, let’s go home before it starts to rain."
    c "Sounds like a good plan to me."

    scene black with fade
    $ renpy.pause (6.0)


    jump tld_day4end
