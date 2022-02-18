label tld_day4good:

# (Previous positions)
# show logan normal at Position(xpos = 0.75) with dissolve
# show remy normal flip -at left with dissolve

Lg "I’ve talked with those people you let in the city earlier this morning."
Lg serious "We’re quite lucky in terms of skilled workers."
Lg "We have a doctor, two engineers, a proper electrician and a maintenance guy."

if kol_tld_wtpchosen == True:
    Lg "Since we already did some rough scouting work at the water treatment plant, I believe that we could theoretically get the systems running again."

else:
    Lg "Since we already did some rough scouting work at the factory, I believe that we could theoretically get the systems running again."

Lg "At least, enough until we figure out what to do later."
Ry "What about all the interiors that still needed to be repaired?"
Ry "After all, you just can’t start to operate something while something else is already falling apart."
Lg "Already thought about that."
Lg "I managed to get most of the people to start working as we speak."
Lg thinking "Last I checked, the outer walls were being repaired."
c "Should we go to check up on their progress, then?"
Lg normal "Is the sky blue?" #Another one of my favourite lines!
c "Noted."

hide logan with dissolve
hide remy with dissolve

m "I finished with the last pieces of my food and went outside with Logan and Remy."

$ renpy.pause (1.0)
scene city at Pan ((0, 360), (0, 0), 5.0) with dissolve
$ renpy.pause (7.0)

scene kolcitycentre at Pan ((0,180),(0,180), 3.0) with dissolve
$ renpy.pause (2.0)
m "Looking back at Remy, I could see that he didn’t look like his usual self. Whether that was from Logan waking him up earlier than he was used to, or something else entirely, I couldn’t tell."

if kol_tld_wtpchosen == True:

    $ renpy.pause (2.0)
    scene kolwtpout at Pan((0,0),(0,60),4.0) with dissolve
    $ renpy.pause (2.0)

    m "We eventually arrived at the water treatment plant after several minutes of Logan theorizing about several different possibilities of repairs."

    show logan normal flip at Position(xpos = 0.25) with dissolve
    show remy normal at right with dissolve

    Lg serious flip "Damn, they're quick."
    Lg "It’s almost as if they're secretly the old construction robots we had back in the day in disguise."
    c "But you said that they were repairing the outside walls the last time you checked, correct?"
    Lg "Yeah."
    Lg normal flip "And as you can see, that’s almost finished."
    Ry smile "That’s honestly quite impressive."
    Ry normal "Do you know if any progress has been made on the interiors yet?"
    Lg thinking flip "Well, since you asked, we might as well check on that."

    stop music fadeout (2.0)
    $ renpy.pause (1.0)
    scene kolwtp3 at Pan ((0, 0), (0, 127), 4.0) with dissolve
    $ renpy.pause (3.0)
    play music "mx/believe_kol.ogg" fadein 1.5

    m "We went inside, expecting it to still be in a state of disarray. However, it seemed that there were already many people inside, with several of them washing the walls and sweeping the floors."
    #From here on out it's a different route, so just copy paste the above section for later

    m "We walked further inside to the water purifiers, only to be greeted by someone who I presumed was the maintenance guy. A few words were exchanged with Logan, as if the both of them were coming to a sort of conclusion."

    show logan smiling at Position(xpos = 0.75) with dissolve
    show remy normal flip at left with dissolve

    Lg "Guess we’re in luck."
    Lg "The guy actually has an idea of what to do. Turns out, the purifiers we have are the exact same model they had in the city before they were destroyed."
    Lg "We should be able to get them up and running far sooner than I expected."
    Ry smile flip "That’s great! I’m glad that the extra help turned out useful in the end."

    show logan serious with dissolve
    $ renpy.pause (1.0)
    m "Logan grumbled something under his breath."
    $ renpy.pause (1.0)

    c "So, is there anything that we could help with?"
    c "I mean, I don’t think that just standing here would help the water treatment plant get repaired."
    Lg thinking "Hmmm..."
    Lg normal "You could help to repair the ceiling of the facility with the resources you found the other day, since I don’t think that anybody has started on that yet."
    Lg "Maybe you could also check on the progress that all the others have already made."
    Lg thinking "As for Remy, I’m not entirely sure. I don’t think that he’d be able to do something complicated like reconstruction."
    Ry normal flip "Well, you are correct. I’m not nearly as dexterous as anybody here, so I can’t really do any complex physical labour without struggling."
    Ry "I can, however, carry some building materials, if that would be helpful."
    Lg normal "I suppose that would suffice."
    Lg "Well, I’ll call for you as soon as I’m ready to test the purifiers out."
    Lg "Oh, and the materials you found are just outside near the back door, if you’re wondering. I also added a few extra things like nails and some tools, just in case you need it."
    c "Thanks. Good luck, Logan."
    Lg "In this day and age, you’re going to need a lot more than luck, [player_name]."
    Lg serious "A lot more."

    $ renpy.pause (1.0)
    scene kolwtpout at Pan ((0, 0), (0, 0), 2.0) with dissolve
    $ renpy.pause (2.0)

    m "We left the facility to get the resources for the repairs, but soon ran into Martin already carrying a great deal of building materials."

    show martin normal with dissolve

    Mt happy "Oh, you’re here! I guess you two are here to repair the roof, correct?"
    c "Yeah. Logan asked us to work on it while he’s busy with the water purifiers. What made you decide to help out, though?"
    Mt normal "I figured that repairing needed to be top priority now, considering that an entire section had collapsed, as well as the already numerous tiny skylights that are an ever present reminder of how worn down this roof is."
    c "I see. Well, it looks like that the three of us will be working together, then."
    c "Remy will help to transport some materials while me and you can start actually repairing the roof."
    Mt "Sounds like a good enough plan for me."
    Mt serious "To be honest, I really don’t know why I thought that it would be a good idea to do this alone, considering that I’m not strong enough to constantly carry everything back and forth."
    Mt normal "Do you think that I should get some extra tools? I do happen to have a few..."

    $ renpy.pause (1.0)

    Mt "Exotic tools that could make our life a bit easier back at my place."
    c "Wait, why do you have spare tools?"
    Mt happy "Well, you do need to repair some equipment every once in a while when you and an entire group are refugees from a dying city."
    c "I guess that I could see that."
    c "In any case, I don’t think that it would be necessary."
    c "For now, at least."
    Mt normal "Ah, gotcha. Well, I guess I’ll see you on the roof, then."

    hide martin with dissolve

    m "Martin slowly put all the materials that he carried down on the ground, went around the building and grabbed a ladder that leaned on the walls."
    m "I could see him slowly struggling to climb the ladder, as if he was afraid that he might slip and fall." #Clumsy boi

    show remy normal flip at left with dissolve

    Ry "Should I start to bring the materials for you and Martin?"
    c "Yeah. Just remember to bring a small amount over time."
    c "Too much could cause the roof to collapse even further due to the extra weight."
    c "This also means that you’d probably have to stay on the ground."
    Ry "I understand."
    Ry smile flip "Well, you can call me if you need anything."
    c "Will do, Remy."

    hide remy with dissolve

    $ renpy.pause (1.0)
    scene kolwtproof at Pan ((0, 0), (0, 65), 3.0) with dissolve
    $ renpy.pause (2.0)

    m "I climbed onto the roof using the same ladder that Martin had used. Upon reaching the top, I looked around, enjoying the view I now had of a great chunk of the city. I didn’t look long, however, before Martin interrupted me."

    show martin serious with dissolve

    Mt "I don’t think that we should waste time looking around and start repairing as soon as we can."
    c "Fine, we’ll start."
    c "Where should we begin?"
    Mt normal "That part over there should be a fairly decent place to start."
    c "Alright, then. Let me call for Remy."

    hide martin with dissolve

    m "I asked Remy if he could bring me the materials needed to start. After watching him slowly pick up the materials Martin carried, he flew up at a steady pace and dropped the materials next to me."

    play sound "fx/box2.wav"
    $ renpy.pause (1.0)

    show martin normal with dissolve

    Mt happy "Well, that’s an interesting way of transporting stuff."
    c "Just don’t expect too much from it, that’s all."
    Mt normal "A reasonable conclusion."

    $ renpy.pause (2.0)
    play sound "fx/repairhammer_kol.wav"
    $ renpy.pause (2.0)

    c "I know that this is a sudden question, but why are you always wearing that cloak wherever you go?"
    c "It seems that it would just get in the way while you work."
    Mt "Well, let’s just say that the cloak keeps me from getting sunburnt while also protecting me from the sandy wind."
    c "I see."
    c "How are you adapting to the city so far?"
    Mt happy "It’s pretty great, actually!"
    Mt normal "Sure, there is a lot of work that needs to be done here, but that’s to be expected."
    Mt "At least everybody else and I are safe, to a certain degree."
    Mt serious "I will admit, though. The last few weeks have been really rough on everybody."
    Mt "Everyday we were on the edge of giving up and surrendering ourselves to the desert."
    Mt "If you and Logan didn’t allow us in the city, then I don’t think that we would have been able to continue surviving."
    c "Well, Logan was really close to outright rejecting you in the first place. It took some convincing to try and change his mind."
    Mt "Honestly, I wouldn’t have expected anything else from him. He does seem like somebody that would risk life and limb to protect what’s dear to him."
    Mt "Even if it means threatening the lives of so many innocent people."
    Mt "But enough procrastination for now."
    Mt normal "Can you hand me some ceiling tiles and cement from over there?"
    Mt "Oh, and the electric drill as well."
    c "Here you go."

    hide martin with dissolve

    m "I handed around half of the current bricks I had to Martin, as well as some cement and the drill he wanted."
    c "(Wait, how does this thing even still work? Did Logan tamper with it by any chance?)"
    $ renpy.pause (3.0)
    c "(Ah, a solar powered battery. Logan {i}definitely{/i} tampered with this beforehand.)"
    $ renpy.pause (2.5)
    m "We started to work on the roof by fixing the small holes with the ceiling tiles that we had, with the cement helping to reattach the loose bricks on the edges. "

    play sound "fx/repairdrill_kol.wav" #Wait, why would you need a drill when you're working with cement and ceiling tiles? Hmmmm... Poor plotting I see....
    $ renpy.pause (1.0)

    m "After a while, however, Martin seemed to get more and more frustrated."

    show martin serious with dissolve

    Mt "This is getting far too annoying for me. I don’t think I’ll be able to go on like this."
    Mt "I’m going to need a certain specialised tool of mine if I want to be able to stabilise this section of the roof."
    c "Well, there are other parts of the roof that need working on, you know."
    Mt "I guess you do have a point. The thing is, only the most unstable parts remain, so both of us will need to work on the same part to prevent it from collapsing."
    c "Alright. I’d say that we start with that section over there."
    Mt "Too dangerous. We’re going to have to stabilize the inside first by adding supports before moving to that section."
    c "So you’d rather want to work on that huge hole over there that collapsed recently?"

    $ renpy.pause (2.0)

    Mt "Fine. I’ll check the interior first before we make any further moves."
    Mt normal "I’ll be right back."

    hide martin with dissolve

    m "Martin went down the ladder while I patiently waited."
    $ renpy.pause (3.5)
    m "Some time passed before I heard Remy call out to me."

    Ry look "[player_name]! I think you need to come and see this!"
    c "What’s wrong, Remy?"
    Ry "Look over there. Can you see it?"
    m "Remy pointed to the sky with his claw."
    $ renpy.pause (1.0)
    c "Sorry Remy. I can’t see a thing, even from up here."
    Ry "I’ll fill you in on the details, then."
    Ry "But first, I’m going to need to fly a bit to see whether my suspicions are justified."
    Ry "After all, I really don’t want to create a sense of panic by spreading rumours and false news."
    c "Take your time."
    m "I decided that I should climb down from the roof while Remy took off to the skies. I could see that he flew for quite some distance, but returned soon afterwards."

    $ renpy.pause (1.0)
    scene kolwtpout at Pan ((0, 0), (0, 0), 2.0) with dissolve
    $ renpy.pause (2.0)

    show remy look with dissolve

    Ry "It seems that my suspicions were correct after all."
    Ry sad "A huge storm is approaching."
    c "A storm? Are you sure about that, Remy?"
    Ry "As sure as day."
    c "Then let me check something quickly..."
    m "I took my PDA out and searched for something that could give me more information on why and how a storm could possibly form here."

    $ renpy.pause (2.0)

    m "Nothing appeared."
    c "(Looks like there isn’t any information about weather patterns on this thing. Why am I surprised?)"
    Ry look "Did you learn anything?"
    c "Nothing that could help me determine why or how a storm could be here."
    c "The concept of a huge storm in the middle of this desert is pretty much unheard of."
    c "The last time a storm hit was probably..."

    $ renpy.pause (3.0)

    c "Huh. I don't think that I can even try to make an accurate guess."
    Ry "I’d imagine that it just makes this all the more surreal for you."
    c "Yeah. In any case, can you try to make an estimate on when the storm will arrive? After all, since you had a better view in the sky, you should be able to give a somewhat accurate estimation."

    $ renpy.pause (1.0)

    Ry "I'd say most likely around tonight at the earliest."
    c "Then we should immediately tell Logan so that we could plan ahead."

    play sound "fx/steps/rough_gravel.wav"

    m "I started walking to the entrance, wondering why Martin was taking so long to return."
    c "Let’s go. I think that the amount of repairs me and Martin did will suffice for now."
    Ry normal "Well, it should keep most of the rain out."
    Ry look "Or so I hope."

    stop sound
    $ renpy.pause (1.0)
    scene kolwtp3 at Pan ((0, 0), (0, 127), 4.0) with dissolve
    $ renpy.pause (3.0)

    m "We entered the water treatment plant with a feeling of dread brewing inside of me, as the roof hadn’t been repaired to an extent where it would sufficiently protect the interior from rain."
    m "As we walked through the hallways, we ran into Logan with a somewhat excited smile on his face."

    show remy normal flip at left with dissolve
    show logan normal at Position(xpos = 0.75) with easeinright

    Lg smiling "Well, looks like fate decided that I shouldn’t have to worry about finding you two."
    Lg "I literally just went to come and get the both of you, but it looks like you two already came on your own accord."
    Lg "Say, how are the repairs going?"
    c "Well, most of it has been repaired, but there are still a few gaps left, as well as the larger holes that collapsed."
    Lg normal "Good enough, I suppose."
    Lg "Now, are you coming with me to see if the purifiers are operational or not?"
    Ry look flip "Actually, there’s something we need to tell you first."
    Lg "I’m pretty sure it can wait." #Ah, Logan just casually being a self-absorbed prick. Classic.
    Lg "Now, let’s go and see if these things will turn on."
    c "But won’t you need a generator to power the purifiers?"
    Lg "I already sent somebody to get one from my house for me. All that needs to be done is the testing."

    show logan normal flip with dissolve
    hide logan normal flip with easeoutright

    m "Logan was already walking before he finished that sentence. Me and Remy had to run so that we would be able to catch up."

    $ renpy.pause (1.0)
    scene kolwtp4 at Pan ((0, 20), (0, 142), 5.0) with dissolve
    $ renpy.pause (3.0)

    m "As the three of us entered the room containing the water purifiers, we were greeted by the maintenance guy I saw earlier. He and Logan exchanged some words, with both of them showing signs of excitement."

    show remy normal at right with dissolve
    show logan normal flip at Position(xpos = 0.25) with dissolve

    Lg smiling flip "Looks like everything is in place now. Thanks to those functioning parts, the maintenance guy wasn’t {i}just{/i} able to help me repair it, but to improve the purifiers as well."
    Lg "In other words, less energy will now be used to power these."
    c "That’s honestly amazing. I do presume that it wasn’t easy to do, though."
    Lg normal flip "You bet it wasn’t. The easy part was getting the purifiers working again. To actually make them more energy efficient, however, is not something that I’m capable of."
    Lg "Now, let’s turn these things on, shall we?"

    show logan normal at Position(xpos = 0.25) with dissolve #Very inefficient, I know.
    $ renpy.pause (1.0)

    m "Logan went to the generator next to a control panel for one of the purifiers and turned it on."

    play sound "fx/highvoltzap_kol.wav"
    $ renpy.pause (3.0)

    m "A loud buzzing followed, with loud noises from various moving parts filling the room."
    $ renpy.pause (1.0)

    stop sound

    show logan smiling flip at Position(xpos = 0.25) with dissolve

    Lg "Success!" with Shake ((0, 0, 0, 0), 3, dist=10)
    Lg "And would you look at that! Almost no electricity is used in powering all these machines!"
    Lg "Now all we need to do is finish the pumps and repair the main pipes, and this city will have clean water once again."
    Ry smile "I didn’t think that you’d be able to pull all this off, even with the help of someone else."
    Ry "Congratulations!"
    Lg "Why, thank you! It certainly is ever so wonderful to bask in the glory of success!" #Now he's really an egotistic prick...
    m "I saw in the corner of my eye that the maintenance guy had an annoyed expression."

    menu:
        "Well, maybe you should share some of that glory with those who helped you.":
            $ renpy.pause (0.5)

            Lg normal flip "Ah, you’re right. Where on earth are my manners?"
            Lg "Thank you, Remy, and thank you, [player_name], for helping me to repair this plant to its former glory."
            c "I was more referring to the maintenance guy."
            Lg serious flip "Oh."
            m "Logan started to talk loudly to the maintenance guy on the other end of the room."
            Lg "Alright. Thank you too, for putting the extra effort in so that these machines can run in a far better state than they originally could!" with Shake ((0, 0, 0, 0), 8, dist=5)
            Lg "Happy now, [player_name]?"
            m "I saw a somewhat satisfied smile appear on the maintenance guy’s face as he left the room."
            c "Happy enough."
            Lg normal flip "Good."


        "Yeah, it feels really nice.":
            $ renpy.pause (0.5)

            Lg "See? Sometimes it feels great to be a success!"
            Lg normal flip "All those hours of frustration finally paid off."


        "Are you really going to have an inflated ego now, of all places?":
            $ renpy.pause (0.5)

            Lg normal flip "I wouldn’t say that I have an inflated ego." #Yeah, you do. I literally wrote you to have an inflated ego here dammit!
            Lg "Just an adrenaline rush from knowing that you did something very important."
            c "I do understand that, Logan, but don’t you think you’re overreacting a bit?"
            Lg serious flip "Oh, [player_name]."
            Lg normal flip "You have no idea what I’m like when I’m {i}actually{/i} overreacting." #Is that a threat?


    $ renpy.pause (1.5)

    Lg "Now, if I remember correctly, Remy wanted to tell me something, correct?"
    Ry look "Yes. There is a storm approaching, and the chances are good that it will hit us pretty hard."
    Lg thinking flip "A storm?"
    Lg "In this place?"
    Lg "At this time of year?"

    $ renpy.pause (1.5)

    Lg serious flip "Sorry, but I’m not so sure I believe you there." #WHY ARE YOU SO DAMN STUBBORN?! Oh wait, I created you...
    Lg "You do know that we live in a {i}desert{/i}, right? You know, one of the driest climates you could possibly get on Earth?"
    c "I know that it’s strange, but you have to believe him."
    c "Sadly, I can’t confirm anything, as my PDA had no information that I could use to identify the strange change in weather, but I did start to feel the air getting more humid before I came to see you."
    c "At least a bit, if that's worth anything."
    Lg "Well, if that’s the case, then it would be the first time a storm hit here in years."
    Lg "Mind if you can show me any signs of the storm approaching?"
    Ry shy "I don’t think that I even need to show you. Dark clouds are already visible on the horizon, and I can already start to hear some strong winds blowing."
    m "Me and Logan looked through one of the windows outside. I could spot some dark clouds approaching, as if all the rain in the desert these past few years had been gathering up in those few clouds."

    stop music fadeout (3.5)

    show koldarkclouds at Pan ((580,608), (0,0), 12.0) with fade
    $ renpy.pause (10.0)
    hide koldarkclouds with fade

    play music "mx/fervor_kol.ogg" fadein 1.0 #Yes, this has background wind. It's for the extra E F F E C T.

    Lg "Damn it!" with Shake ((0, 0, 0, 0), 2.5, dist=30)
    Lg "Alright, let me think..."

    show logan thinking flip with dissolve
    $ renpy.pause (4.5)
    show logan serious flip with dissolve

    Lg "Okay. We need to warn everybody that didn’t come to help repair the water treatment plant, and fast. Tell them to reinforce their houses and to waterproof their possessions."
    Lg "If luck is on our side, then the city {i}shouldn’t{/i} be completely flooded when this is all over."
    c "I’ll go and find Martin. After all, he was supposed to be back quite some time ago."
    Lg thinking flip "If I recall, he said that he went somewhere to retrieve something that he needed to make an estimation on some supports for the roof."
    Lg serious flip "Well, you should just go and see if you can find him. Chances are, everybody else will listen to him more than me, so finding him is a necessity."
    Ry look "I’ll go with you, [player_name]. If I see any developments in the storm in the skies, then I’ll let you know as soon as possible."
    Lg "Good. [player_name], take the motorcycle I originally used to get here. It will save you some much necessary time."
    c "Alright. Where will we meet again after I’m done?"
    Lg "Right here."
    Lg "Now go!" with Shake ((0, 0, 0, 0), 2, dist=10)

    $ renpy.pause (0.5)
    scene kolwtpoutstorm at Pan ((0, 0), (0, 0), 2.0) with dissolve
    $ renpy.pause (2.0)

    m "I rushed outside the building, with Remy following right behind me."
    m "After a bit of searching, I found the motorcycle that Logan was referring to hidden in a small corner near one of the secondary exits."

    show remy look with dissolve

    c "Remy, if you see Martin at some point, let me know immediately."
    Ry "And if I somehow find him before you do, then I’ll let him know of the storm."
    c "Deal. Good luck, and stay safe."
    Ry normal "You too, [player_name]."

    hide remy with dissolve
    play sound "fx/motorcycleaccelerate_kol.wav"
    $ renpy.pause (2.0)

    m "I climbed on the motorcycle and started the engine. Soon, I drove around, hoping to see where Martin was."

    scene kolcitystorm at Pan ((0, 360), (0, 360), 0.0) with fade
    $ renpy.pause (1.0)
    m "I rode the motorcycle through the streets of the city, hoping to find Martin before the storm got any worse."
    $ renpy.pause (2.0)

    jump tld_martinencounter





    label tld_wtpend:

    $ renpy.pause (0.5)
    scene kolwtpoutstorm at Pan ((0, 0), (0, 60), 2.5) with fade
    $ renpy.pause (2.0)

    stop sounds

    m "After a few minutes of driving, I reached the water treatment plant. Luckily, it hadn’t started to rain yet, although I could guess that it wouldn’t be long anymore before it does."
    c "(Looks like I made it in time.)"

    play sound "fx/landing.ogg"
    $ renpy.pause (1.0)

    m "Remy soon landed after with a mildly distraught face."

    show remy look with dissolvemed

    Ry "I don’t know if you felt it, but the winds just changed direction. It looks like the storm will hit us earlier than expected."
    Ry sad "If I had to guess, I’d say in about half an hour."
    c "So, a few hours earlier than scheduled."
    c "Damn it. We’ll have to make this quick, then."

    $ renpy.pause (1.0)
    scene kolwtp3 at Pan ((0, 0), (0, 127), 4.0) with dissolve
    $ renpy.pause (3.0)

    m "We entered the building, only to find that Logan was already waiting for us. "

    show logan serious at Position(xpos = 0.75) with dissolve
    show remy normal flip at left with dissolve

    m "He appeared extremely worried, but when he saw us approaching, he seemed to lighten up."
    m "At least partially."

    Lg "Ah, you’re back."
    Lg "Were you able to find Martin?"
    c "Yes, we were."
    c "Even better, however, was the fact that Martin seemed to know a few things about the weather."
    c "According to him, we should be able to avoid the storm’s heaviest blow."
    c "In short, we should still be mostly safe."
    Lg "And how do you know that he’s correct?" #Scepticism is good
    Lg "For all I know, he could just be saying that to avoid mass panic."
    Lg "I’ve seen far too many cases like that in my life."
    c "I can only guess here, as he didn’t elaborate much."
    c "He seems to know a lot about weather and storms in general, though."
    Ry "During my flight, I could also see the clouds starting to shift in the winds. I wanted to let [player_name] know, but Martin already beat me to it."
    Ry look flip "Problem is, the rain should hit way earlier than I originally estimated."
    Lg "The time being in...?"
    Ry sad flip "Around half an hour."

    hide logan with dissolve
    m "Logan turned around and walked in a small circle, presumably deep in thought about what would be the best move to make. After a few minutes, he stopped and turned back towards me and Remy."

    show logan serious at Position(xpos = 0.75) with dissolve
    $ renpy.pause (2.5)

    Lg "*sigh*"
    Lg "I’ll set out some instructions for the workers still here to go home as soon as they’re finished with whatever they’re busy with."
    Lg "Since this place hasn’t crumbled yet, it’s best to leave any additional repairs for later. The roof not being fully patched up does concern me a bit, but I’m hoping that nothing too bad happens."
    Lg "I just hope that whatever you and Martin did is sufficient enough to protect most of the necessary equipment."
    Lg normal "You two can go home now. I think that the both of you earned some rest."
    Ry look flip "But what about you? Won’t you just get soaked in the rain when you go home?"
    Lg "I’ll manage somehow."
    Lg thinking "It does make me wonder, though. Do your scales protect you from getting wet, or do you get soaked like the rest of us?"
    Ry normal flip "Our scales do make us partially waterproof, but that can differ between species."
    Ry "For me, if I get really wet, I can just shake myself dry."
    Lg "That’s nice."
    Lg normal "Well, it’s best that you two leave while there’s still light outside. See you whenever this storm ends, I guess."
    c "See you, Logan."
    Ry "Goodbye, Logan. Do stay safe."

    scene black with fade
    stop music fadeout (2.0)
    $ renpy.pause (2.0)

    m "Me and Remy left the water treatment plant while Logan still lingered around the grounds. Surprisingly, the entire sky has now gotten dark, with only a few rays of sunshine penetrating the clouds."

    jump tld_day4end



else:

    $ renpy.pause (2.0)
    scene kolfactoryout at Pan((0,0),(0,60),4.0) with dissolve
    $ renpy.pause (2.0)

    m "We eventually arrived at the factory after several minutes of Logan theorizing about several different possibilities of repairs."

    show logan normal flip at Position(xpos = 0.25) with dissolve
    show remy normal at right with dissolve

    Lg serious flip "Damn, they're quick."
    Lg "It’s almost as if they are the old construction robots we had back in the day in disguise."
    c "But you said that they were repairing the outside walls the last time you checked, correct?"
    Lg "Yeah."
    Lg normal flip "And as you can see, that’s almost finished."
    Ry smile "That’s honestly quite impressive."
    Ry normal "Do you know if any progress has been made on the interiors yet?"
    Lg thinking flip "Well, since you asked, we might as well check on that."

    stop music fadeout (2.0)
    $ renpy.pause (1.0)
    scene kolfactory3 at Pan ((0, 0), (0, 127), 4.0) with dissolve
    $ renpy.pause (3.0)

    play music "mx/believe_kol.ogg" fadein 1.5
    m "We went inside, expecting it to still be in a state of disarray. However, it seemed that there were already many people inside, with several of them washing the walls and sweeping the floors."

    $ renpy.pause (1.0)
    scene kolfactory1 at Pan ((0, 0), (0, 127), 4.0) with dissolve
    $ renpy.pause (3.0)

    m "In the central facility, however, only a single human was present to inspect the old machinery. Logan went towards them and exchanged a few words. When he returned, however, I could see some signs of irritation on his face."

    show logan serious flip at Position(xpos = 0.25) with dissolve
    show remy normal at right with dissolve

    Lg "Guess I shouldn’t have had my hopes that high."
    Ry look "I imagine that the feedback wasn’t that positive."
    Lg "You’d be right with that."
    Lg "Luckily, nothing that isn’t a dealbreaker. Just a major annoyance."
    c "So, that person you were talking to couldn’t try and come up with any solutions?"
    Lg "Nope. Turns out that I could probably do a far better job repairing the electronics myself than with the help of anybody else, despite said electronics being more fried than your average food selection at an old carnival." #Yet another golden line
    Lg thinking flip "At least they aren’t {i}entirely{/i} clueless."
    Lg normal flip "I’ll just have them remove the rust and the old electronics later while I try and figure something out."
    c "Well, at least you {i}have{/i} extra help. That is something worth on it’s own, after all. Just imagine how many more sleepless nights you’d have to pull in order to get something of this scale working again."
    Lg serious flip "I hate admitting that somebody is right and I’m wrong, but..."
    Lg "You’re right. I’m wrong."
    Lg "Even if the extra help is pretty basic, it’s help that we didn’t have before. I really shouldn’t have pointed a gun at them if their help is what’s necessary to get this city up and running again." #Oh? Logan feels regret? How interesting...
    c "It’s a pleasure helping you acknowledge the truth."
    Lg "Don't push it."
    m "Suddenly, Martin entered the room with a strange metal object in his hand."

    show martin normal at Position(xpos = 0.90) with easeinright

    Mt "Well, I found the part you were lo-{w=0.75}{nw}"

    m "His face then shifted to an expression of surprise."
    Mt shocked "Oh! [player_name] and Remy are here!"
    Mt normal "I just came here to deliver a part to Logan, that’s all."
    Lg normal flip "That’s quicker than I expected. You bunch really do know how to work efficiently, don’t you?"
    Mt "Well, you need to learn how to work quickly if you want to survive in these times."
    Mt "But enough rambling. Here’s the part you wanted."

    $ renpy.pause (3.0)

    Lg thinking flip "Now, let’s see if it’s..."

    play sound "fx/magnetzap_kol.wav"
    $ renpy.pause (4.0)

    Lg smiling flip "Yep. Magnetic and still responsive."
    Lg thinking flip "And it seems that it should fit right about here, although I’m not sure what effect that might have on the adjacent parts that are more resistant to the effects of electromagnetic induction."
    Lg "Hmmmmm..."
    c "Is there anything we can help with?"
    Lg normal flip "Yeah. Could somebody go and get the guy that I chased away a few minutes ago?"
    Mt "On it."

    show martin normal flip at Position(xpos = 1.20) with ease

    Lg "Good. As for you two, I recommend that you check up on the progress around the factory a bit more."
    Lg serious flip "No need to offend you, but the untrained shouldn’t be anywhere {i}near{/i} things like this, especially if {i}I’m{/i} the one that is going to try and replace a bunch of tech."
    c "I figured as much. At least {i}try{/i} to not zap something this time."
    Lg smiling flip "I’ll only stop when this thing is either repaired or I’m dead."
    Lg "Besides, zapping stuff via magnets is the best part."
    Lg "That’s why I studied electromagnetism in the first place!"

    $ renpy.pause (1.0)
    scene kolfactory3 at Pan ((0, 0), (0, 0), 2.0) with dissolve
    $ renpy.pause (3.0)

    m "Me and Remy left the central facility to check up on the progress that all the workers had made on the factory. After many good words and several progress reports, we decided to take a small break outside to get some fresh air."

    $ renpy.pause (3.0)
    scene kolfactoryout at Pan((0,0),(0,0),2.0) with fade
    $ renpy.pause (2.0)

    m "I sat on an old bench nearby, while Remy comfortably sat next to me on the floor."

    show remy normal with dissolve

    c "Are you sure that you’re comfortable, Remy? Rocky sand isn’t exactly the best place to sit and get comfortable."
    Ry smile "There’s no need to worry. My scales are able to make almost any place comfortable enough for me to sit down."
    c "Almost?"
    Ry normal "Well, obviously you can’t just decide to lay down in some thorny bushes or sharp edges at a cliffside."
    Ry "Although, there are species like earth dragons that are able to, due to them having far harder scales than your average dragon."
    Ry "But they have other problems to compensate for their hardened scales."
    c "Like having trouble with stairs, for example?"
    Ry look "What makes you think that?"
    c "Oh, no particular reason, that’s all."
    Ry "That sounds far too specific of a scenario to have no reason, though."
    Ry smile "I’ll just have to try and figure your reason out later, then!"

    $ renpy.pause (3.0)

    Ry look "Wait..."
    m "Remy looked up at the sky and pointed to something far in the distance."
    Ry "Do you see that, [player_name]?"
    c "I’m sorry, but I don’t think that I do. What is it?"
    Ry "Please wait for a bit while I confirm my suspicions. I wouldn’t want to create panic by spreading false news."

    hide remy with dissolve
    play sound "fx/takeoff.ogg"

    $ renpy.pause (1.0)
    m "Remy took off into the sky, but came back soon afterwards."

    stop sound

    $ renpy.pause (2.0)
    play sound "fx/landing.ogg"

    show remy sad with dissolve

    Ry "And it seems that I was right."
    Ry "It seems that a huge storm is approaching."
    c "A storm? Are you sure about that, Remy?"
    Ry "As sure as day."
    c "Then let me check something quickly."
    m "I took my PDA out and searched for something that could give me more information on how and why a storm could possibly form here."

    $ renpy.pause (2.0)

    m "Nothing appeared."
    c "(Looks like there isn’t any information about weather patterns on this thing. Why am I surprised?)"
    Ry look "Did you learn anything?"
    c "Nothing that could help me determine why or how a storm could be here."
    c "The concept of a huge storm in the middle of this desert is pretty much unheard of."
    c "The last time a storm hit was probably..."

    $ renpy.pause (3.0)

    c "Huh. I don't think that I can even try to make an accurate guess."
    Ry "I’d imagine that it just makes this all the more surreal for you."
    c "Yeah. In any case, can you try to make an estimate on when the storm will arrive? After all, since you had a better view in the sky, you should be able to give a somewhat accurate estimation."

    $ renpy.pause (1.0)

    Ry "I'd say most likely around tonight at the earliest."
    c "Then I should probably let Logan know when our break is over."
    Ry "I think that we should let him know immediately so that we can start to prepare."
    c "You’re right. We probably would be better off if we let him know right now."

    $ renpy.pause (1.0)
    scene kolfactory3 at Pan ((0, 0), (0, 127), 4.0) with dissolve
    $ renpy.pause (3.0)

    m "We went back inside the factory on our way to the central facility, only to be immediately met with Martin."

    show remy normal flip at left with dissolve
    show martin normal at Position(xpos = 0.75) with dissolve

    Mt "There you are! Logan told me to go and look for you."
    Mt serious "He says that he needs a generator to test the machines, as well as your PDA, as it might contain something that he could use."
    Ry "I’ll go get the generator from Logan’s house. I should be back soon."

    hide remy with dissolve

    m "Remy quickly left the factory grounds and flew off to Logan’s house to get one of the generators we left for him to test his electronics with."

    c "I know that this is a sudden question, but why are you always wearing that cloak wherever you go?"
    c "It seems that it would just get in the way while you work."
    Mt "Well, let’s just say that the cloak keeps me from getting sunburnt while also protecting me from the sandy wind."
    c "I see."
    c "How are you adapting to the city so far?"
    Mt happy "It’s pretty great, actually!"
    Mt normal "Sure, there is a lot of work that needs to be done here, but that’s to be expected."
    Mt "At least everybody else and I are safe, to a certain degree."
    Mt serious "I will admit, though. The last few weeks have been really rough on everybody."
    Mt "Everyday we were on the edge of giving up and surrendering ourselves to the desert."
    Mt "If you and Logan didn’t allow us in the city, then I don’t think that we would have been able to continue surviving."
    c "Well, Logan was really close to outright rejecting you in the first place. It took some convincing to try and change his mind."
    Mt "Honestly, I wouldn’t have expected anything else from him. He does seem like somebody that would risk life and limb to protect what’s dear to him."
    Mt "Even if it means threatening the lives of so many innocent people."
    Mt normal "But enough gossiping. You should probably be on your way to Logan now."
    Mt "In any case, do you see any chance that we could hang out later?"
    c "I’ll try, but I can’t promise anything yet."
    Mt happy "Roger that."
    Mt normal "Well, best that I’d be going now. Wouldn’t want to keep you from doing your work now, would we?"
    Mt "Cheers!"

    show martin normal flip with dissolve
    hide martin normal with easeoutright

    $ renpy.pause (1.0)
    scene kolfactory1 at Pan ((0, 0), (0, 0), 3.0) with fade
    $ renpy.pause (3.0)

    m "I found Logan talking to who I presumed to be one of the engineers in Martin’s group. When I approached them, Logan immediately stopped talking and gave me his full attention while the engineer left the room, presumably to give us some privacy."

    show logan normal with dissolve

    Lg "Ah, you’re back. Did you bring the things I asked for?"
    c "Here’s the PDA. Remy will soon be back with a generator from your place."
    Lg smiling "Excellent."
    Lg normal "Now, while we wait, I might as well discuss what’s going on."
    Lg "Despite the obvious lack of use, the machines {i}should{/i} still be operational at a fundamental degree."
    Lg "The PDA should hopefully have a handy instruction manual that I could use to try and get the machines up and running again after I have replaced the electronics."
    Lg serious "The problem is, we can’t really test the machines to see if they function the way they are supposed to, due to a distinct lack of fresh produce."
    Lg thinking "However, if we manage to get the systems online, we should be able to grow crops in the old greenhouse upstairs. Luckily, Martin carried some spare seeds with him which we could use, because for some reason he was carrying those."
    Lg normal "For now, however, we can only really see if the machines actually turn on."
    c "It seems that you already have most of this all figured out."
    Lg smiling "Of course I have." #Again with the ego dammit!
    Lg normal "Now, could you do me a favour and hold this real quick?"
    c "Sure."

    hide logan with dissolve

    m "Logan then proceeded to spend several minutes rearranging some wires that he had misplaced, as well as switching a few parts around."

    show logan normal with dissolve

    Lg "That should do it."
    Lg thinking "Now, what does the magical PDA of almost all human knowledge say..."
    m "Logan searched through the PDA to find anything he could use for these machines in particular. At the same time, Remy appeared from one of the entrances."

    show logan normal at Position(xpos = 0.75) with ease
    show remy normal flip at left with easeinleft

    Ry smile flip "Here’s the generator you asked for, Logan. I do hope that I didn’t take too long."
    Lg smiling "Not at all. In fact, you were right on time."
    Lg normal "Could you place the generator right next to the control panel, please?"
    Ry shy flip "Sorry if I sound a bit ignorant, but do you mean that screen over there?"
    Lg "The one and only."

    hide remy with dissolve
    $ renpy.pause (3.0)
    show remy normal flip at left with dissolve
    $ renpy.pause (2.5)

    Lg "Finished. Now let’s hope this thing can withstand the power output of the generator {i}without{/i} exploding in my face."
    m "Logan hooked the generator up to the control panel, showing subtle signs of doubt."
    Lg serious "Well, here goes everything."

    hide logan with dissolve
    hide remy with dissolve

    $ renpy.pause (1.0)
    play sound "fx/highvoltzap_kol.wav"
    $ renpy.pause (3.0)

    m "Suddenly, I heard a loud zapping noise, which was soon followed by the sound of metal scraping next to metal. As I turned to Logan, I could see how his face lit up in sheer excitement."

    show logan smiling at Position(xpos = 0.75) with dissolve
    show remy normal flip at left with dissolve

    Lg "And looks like I managed to do the impossible once again."

    show logan serious with dissolve
    $ renpy.pause (2.5)
    show logan normal with dissolve

    Lg "With the help of a few individuals from Martin’s group."
    Ry smile flip "Congratulations, Logan! I’m glad that you managed to pull it off."
    Lg smiling "I thank you for your congratulatory statements."
    Lg normal "Soon, we’ll all be able to enjoy a steady supply of fresh food."
    c "This is a really exciting moment. I can’t wait!"
    Lg "Of course you can’t. In all honesty, I think that you’ve gotten too used to the comforts in Remy’s world, and now you’re not able to enjoy the several cans of food left for us."
    Lg thinking "Either that, or from what I can gather from Remy, your cooking is just horrid."

    show remy shy flip with dissolve

    menu:
        "The food was similar to the food here, though.":
            $ renpy.pause (0.5)

            Lg "Is that so?"
            Lg normal "Well, no way for me to ever find out."
            Ry smile flip "I can confirm [player_name]’s statement. Everything I ate here tasted remarkably similar, and yet totally different all at once."
            Lg thinking "What an interesting concept, then."


        "No need to be so harsh. I just like good food.":
            $ renpy.pause (0.5)

            Lg smiling "Yeah, who doesn’t?"
            Lg serious "Thing is, I’ve been waiting for this moment for much longer than you have, since you got to taste some similar, if not, {i}exactly{/i} the same food that everybody used to eat before the solar flare."
            Lg normal "And if I had to guess, you probably didn’t do much cooking during your duties as ambassador, for obvious reasons."
            c "Alright. You win this one."
            Lg smiling "See, was that so hard to admit?"


        "Are you a wizard, by any chance?":
            $ renpy.pause (0.5)

            Lg "Now what on earth made you think that?"
            c "I guess you’re not, then."
            c "If you were, then you would have known why."

            $ renpy.pause (0.5)

            Lg serious "..."



    $ renpy.pause (0.5)
    Ry look flip "Logan, there is something urgent that me and [player_name] need to share with you."
    Lg thinking "Oh? Do share."
    Ry "I saw that a storm was approaching. If I had to guess, then it should probably hit around tonight at the earliest."

    #Yeah yeah, I know. I just copied and pasted this section
    #Sorry if you actually want to read through the code
    #This part alone probably will make it a nightmare
    #And all because I was too lazy to create more labels...
    #Oh wait, skipping will be an issue...
    #...
    #*sigh*
    #Fine, I'll create more labels
    #Done

    Lg thinking "A storm?"
    Lg "In this place?"
    Lg "At this time of year?"

    $ renpy.pause (1.5)

    Lg serious "Sorry, but I’m not so sure I believe you there."
    Lg "You do know that we live in a {i}desert{/i}, right? You know, one of the driest climates you could possibly get on Earth?"
    c "I know that it’s strange, but you have to believe him."
    c "Sadly, I can’t confirm anything, as my PDA had no information that I could use to identify the strange change in weather, but I did start to feel the air getting more humid before I came to see you."
    c "At least a bit, if that's worth anything."
    Lg "Well, if that’s the case, then it would be the first time a storm hit here in years."
    Lg "Mind if you can show me any signs of the storm approaching?"
    Ry shy flip "I don’t think that I even need to show you. Dark clouds are already visible on the horizon, and I can already start to hear some strong winds blowing."
    m "Me and Logan looked through one of the windows near the edge of the ceiling. I could spot some dark clouds approaching, as if all the rain in the desert these past few years had been gathering up in those few clouds."

    stop music fadeout (3.5)

    show koldarkclouds at Pan ((580,608), (0,0), 12.0) with fade
    $ renpy.pause (10.0)
    hide koldarkclouds with fade

    play music "mx/fervor_kol.ogg" fadein 1.0

    Lg "Damn it!" with Shake ((0, 0, 0, 0), 2.5, dist=30)
    Lg "Alright, let me think..."

    show logan thinking with dissolve
    $ renpy.pause (4.5)
    show logan serious with dissolve

    Lg "Okay. We need to warn everybody that didn’t come to help repair the factory, and fast. Tell them to reinforce their houses and to waterproof their possessions."
    Lg "If luck is on our side, then the city {i}shouldn’t{/i} be completely flooded when this is all over."
    c "I’ll go and find Martin. If I had to guess, he shouldn't be too far from here."
    Ry look flip "I’ll go with you, [player_name]. If I see any developments in the storm in the skies, then I’ll let you know as soon as possible."
    Lg "Good. [player_name], take the motorcycle I originally used to get here. It will save you some much necessary time."
    c "Alright. Where will we meet again after I’m done?"
    Lg "Right here."
    Lg "Now go!" with Shake ((0, 0, 0, 0), 2, dist=10)

    $ renpy.pause (0.5)
    scene kolfactoryoutstorm at Pan ((0, 0), (0, 0), 2.0) with dissolve
    $ renpy.pause (2.0)

    m "I rushed outside the building, with Remy following right behind me."
    m "After a bit of searching, I found the motorcycle that Logan was referring to hidden in a small corner near one of the secondary exits."

    show remy look with dissolve

    c "Remy, if you see Martin at some point, let me know immediately."
    Ry "And if I somehow find him before you do, then I’ll let him know of the storm."
    c "Deal. Good luck, and stay safe."
    Ry normal "You too, [player_name]."

    hide remy with dissolve
    play sound "fx/motorcycleaccelerate_kol.wav"
    $ renpy.pause (2.0)

    m "I climbed on the motorcycle and started the engine. Soon, I drove around, hoping to see where Martin was."

    scene kolcitystorm at Pan ((0, 360), (0, 360), 0.0) with fade
    $ renpy.pause (1.0)
    m "I rode the motorcycle through the streets of the city, hoping to find Martin before the storm got any worse."
    $ renpy.pause (2.0)

    jump tld_martinencounter





    label tld_factoryend:

    $ renpy.pause (0.5)
    scene kolfactoryoutstorm at Pan ((0, 0), (0, 60), 1.5) with fade
    $ renpy.pause (2.0)

    stop sounds

    m "After a few minutes of driving, I reached the factory. Luckily, it hadn’t started to rain yet, although I could guess that it wouldn’t be long anymore before it does."
    c "(Looks like I made it in time.)"

    play sound "fx/landing.ogg"
    $ renpy.pause (1.0)

    m "Remy soon landed after with a mildly distraught face."

    show remy look with dissolvemed

    Ry "I don’t know if you felt it, but the winds just changed direction. It looks like the storm will hit us earlier than expected."
    Ry sad "If I had to guess, I’d say in about half an hour."
    c "So, a few hours earlier than scheduled."
    c "Damn it. We’ll have to make this quick, then."

    $ renpy.pause (1.0)
    scene kolfactory3 at Pan ((0, 0), (0, 127), 4.0) with dissolve
    $ renpy.pause (3.0)

    m "We entered the factory, only to find Logan already waiting for us."
    m "He appeared extremely worried at first, but somewhat lightened up when he saw us."

    show logan serious at Position(xpos = 0.75) with dissolve
    show remy normal flip at left with dissolve

    Lg "You’re back. Were you able to find Martin and warn everybody?"
    c "Sort of."
    c "I found Martin at the outskirts of town studying the weather."
    c "According to him, we should be able to avoid the storm’s heaviest blow."
    c "In short, we should still be mostly safe."
    Lg "And how do you know that he’s correct?"
    Lg "For all I know, he could just be saying that to avoid mass panic."
    Lg "I’ve seen far too many cases like that in my life."
    c "I can only guess here, as he didn’t elaborate much."
    c "He seems to know a lot about weather and storms in general, though."
    Ry "During my flight, I could also see the clouds starting to shift in the winds. I wanted to let [player_name] know, but Martin already beat me to it."
    Ry look flip "Problem is, the rain should hit way earlier than I originally estimated."
    Lg "The time being in... ?"
    Ry sad flip "Around half an hour."

    hide logan with dissolve
    m "Logan turned around and walked in a small circle, presumably deep in thought about what would be the best move to make. After a few minutes, he stopped and turned back towards me and Remy."

    show logan serious at Position(xpos = 0.75) with dissolve

    $ renpy.pause (2.5)

    Lg "*sigh*"
    Lg "I’ll set out some instructions for the workers still here to go home as soon as they’re finished with whatever they’re busy with."
    Lg "Since this place hasn’t crumbled yet, it’s best to leave any additional repairs for later. At least the roof is completely finished."
    Lg "I just hope that whatever they did is sufficient enough to protect any necessary equipment."
    Lg normal "You two can go home now. I think that the both of you earned some rest."
    Ry look flip "But what about you? Won’t you just get soaked in the rain when you go home?"
    Lg "I’ll manage somehow."
    Lg thinking "It does make me wonder, though. Do your scales protect you from getting wet, or do you get soaked like the rest of us?"
    Ry normal flip "Our scales do make us partially waterproof, but that can differ between species."
    Ry "For me, if I get really wet, I can just shake myself dry."
    Lg "That’s nice."
    Lg normal "Well, it’s best that you two leave while there’s still light outside. See you whenever this storm ends, I guess."
    c "See you, Logan."
    Ry "Goodbye, Logan. Do stay safe."

    scene black with fade
    stop music fadeout (2.0)
    $ renpy.pause (2.0)

    m "Me and Remy left the factory while Logan still lingered around the grounds. Surprisingly, the entire sky has now gotten dark, with only a few rays of sunshine penetrating the clouds."

    jump tld_day4end



label tld_martinencounter:

scene kolcitycentrestorm at Pan ((0,180),(0,180),3.0) with fade
$ renpy.pause (1.0)

m "I rode through the city centre, yet no trace could be found of him. I then had the idea that I should go to the guard tower to see if I could get a better view and spot him from there more quickly."
m "However, when I approached the city gate where we first encountered Martin and his group, I found him already standing at the outskirts of the city with a notebook in his hands."

$ renpy.pause (2.0)

scene kolcitygatestorm with fade
$ renpy.pause (1.0)
stop music fadeout (2.0)

$ renpy.pause (1.0)
show martin normal with dissolve
stop sound
$ renpy.pause (1.0)

play music "mx/onesix_kol.ogg" fadein 1.5

c "There you are, Martin! I desperately need to tell you something. You see, a-{w=0.8}{nw}"
Mt serious "-huge storm is brewing. I know. Kind of obvious, don't you think?"
Mt "I’ve been studying it for quite some time, actually. When I noticed that the air started to feel more humid and the wind started to get more intense, I decided that I should go to the closest open area to investigate."
Mt "Which brought me here staring at the skies to see if I could make any conclusions about our odds of escaping this storm unscathed."
Mt "Luckily, it seems that we received the tail end of the storm. Judging by the direction of the wind and how the clouds are more concentrated in certain regions than others, the storm {i}should{/i} just barely scrape us."
Mt "Mind you, there would still be {i}a lot{/i} of rain, but nothing that will damage the infrastructure here to an irrepairable state."
Mt normal "In a nutshell: I think that we’re mostly safe."
c "Wait, how are you able to make a conclusion like that? I couldn’t see or feel anything, except for the slight change in humidity."
Mt serious "Let’s just say that back in the day, I knew a guy who knew a guy who taught me a few things, so I know where and how to look."
c "Well, then that just makes you the most qualified of everybody here when it comes to predicting the weather."
Mt "Please, you shouldn’t call me qualified."
Mt "I just happen to know a few things, that’s all."
c "And those few things may or may not determine our fate. I just hope that you’re right with your predictions."
Mt "Well, there’s always the slight chance that I’m wrong, but it’s highly unlikely, judging from these wind directions and cloud formations."
c "Well, that’s comforting."
Mt confused "I’m sorry for asking, but was that sarcasm, by any chance? I’m not really good at detecting that."

menu:
    "Of course not. Why would I be sarcastic?":
        $ renpy.pause (0.5)

        Mt normal "Ah, thanks for confirming that, then."
        Mt "Sarcasm as a concept is just such a weird thing for me. I was never really able to get the hang of it."


    "Yes and no. It’s a bit of both, really.":
        $ renpy.pause (0.5)

        Mt "How does that even work?"
        c "Well, I'm being sarcastic by saying that the chance that you’re wrong isn’t really comforting, but I’m also being serious, as you gave the news that it’s highly unlikely that you will be wrong."
        Mt "I still don’t think I understand that fully."
        Mt normal "Well, at least you tried to explain it to me."


    "Yeah, it was. Sorry about that.":
        $ renpy.pause (0.5)

        Mt normal "Well, don’t worry about it. Sarcasm just isn’t for me."
        Mt "Still, thanks for pointing that out."


Mt "In any case, you shouldn’t worry about the storm. It’s really not as bad as it looks."
c "Noted. Did you tell anybody else yet?"
Mt "Not really. I figured that you might be the first person that would like to hear. Well, you and-{w=1.3}{nw}"

play sound "fx/landing.ogg"
$ renpy.pause (1.0)

m "Martin was interrupted by a loud beating of wings as Remy landed just beside me."

show martin normal flip at Position(xpos = 0.25) with ease
show remy normal at right with easeinright

Mt "-Remy."
c "What a coincidence."
Ry smile "Good news! The storm should safely pass by. We will feel some heavy rain, sure, but nothing to worry about."
Mt "And that would be confirmation I need to prove my point."
Ry look "Wait, was I too late to tell you, then?"
c "Not at all. Martin only speculated about the weather based on what he could determine at ground level."
c "I’d bet that things would be much different in the sky."
Ry normal "Well, I guess you’re right."
Ry look "Speaking of which, we should probably let Logan know what to expect."
Ry "Is there anything else that we should know about, Martin?"
Mt serious flip "Nothing that I can think of. I believe that we have this all figured out now."
Mt "I’ll go tell the news to the rest of my group, since they'll most likely listen to me more than they would to you. No offence, of course."
Mt "In the same vein, you two should probably go tell Logan."
Mt "He seems like the type of guy who would have a stroke if something didn’t go according to schedule, so it's only better if somebody that he trusts tells him about the storm."
c "You have no idea just how accurate you are, Martin."
Mt "I..."

$ renpy.pause (1.5)

Mt "...don't know whether that’s a good thing or a bad thing."
c "Give it a few weeks, then you should be able to answer that question yourself."

$ renpy.pause (1.0)

Ry shy "[player_name], we should really be going now. I don’t think that it would be wise to waste any more time."
c "Alright. See you later, Martin. Hopefully we can get more time to get to know each other better at some point."
Mt normal flip "I hope so too. You two do seem like really good company."
Mt "Well, cheers!"

hide martin with dissolve
hide remy with dissolve

play sound "fx/takeoff.ogg"
$ renpy.pause (1.0)
queue sound "fx/motorcycleaccelerate_kol.wav"
$ renpy.pause (2.0)

m "I climbed back on my motorcycle while Remy took off to the skies."

if kol_tld_wtpchosen == True:

    jump tld_wtpend

else:

    jump tld_factoryend
