label tld_day3:

$ save_name = (_("TLD - Day 3"))

$ renpy.pause (3.0)
scene kolmchouseday at Pan ((300, 80), (0,80), 5.0) with dissolveslow

play music "mx/exile_kol.ogg" fadein 0.5

m "I awoke from my sleep, feeling extremely well rested. As I looked outside my window, a shining ray of sunlight gleamed into my eyes."
c "(Yep, it’s daytime alright.)"


m "When I went into the living room, I found Remy still sleeping on the couch."
c "Good morning, Remy. It’s going to be a day full of work today, so I recommend that we start getting ready as soon as possible."
m "Remy slowly rose and stretched before greeting me. Afterwards, he slowly put his tie on and went to the kitchen to get something to eat."
m "When both of us had our meals, we went outside to meet up with Logan."

$ renpy.pause (2.0)
scene city at Pan ((0, 360), (0, 0), 5.0) with dissolve
show remy normal with dissolve

c "So, what do you think Logan is up to right now?"
Ry "Well, I think he’d most likely either be sleeping, or working on some project of his now that he received all the information he wants from the PDA."
c "That is true. After all, the PDAs were only available to high ranking authorities for whatever knowledge was already stored within like manuals for medical devices, or to those who were lucky enough to still own a working one."
c "And then there was the fact that the officials issued an order that all PDAs that still worked should be handed in so that they could be used in the trade."
c "He wouldn’t have had access to anything more than the scraps of information we still have in some books or the information he retained before the solar flare hit us and disrupted everything."
Ry "That makes sense. I assume you were one of the lucky ones with a working PDA, correct?"
c "Yes, although everything that was already stored on it wasn’t much use to a society of dragons."
c "Things like personal notes or records for the jobs I had to do, to name a few."
c "In the end, my PDA was completely wiped so that it could be used in the trade."
Ry "I think that information like personal notes would still be useful after all. Maybe some psychologists could gather some insight on how your average human would think or go about in their daily lives."
c "I guess so. Still, whatever the authorities had ordered needed to be done."
c "It just makes me wonder, though."
c "How did our scientists even {i}get{/i} the information on all the PDAs? Last time I checked, there weren’t any archives still operational that they could have transferred the knowledge from."
Ry smile "Well, maybe some divine human magic was involved?"
c "But we aren’t divine beings."
Ry "I know."

scene kolcitycentre at Pan((0,110),(0,180),3.0) with dissolve
$ renpy.pause (4.0)
scene kolloganout at Pan ((0, 0), (0, 250), 5.0) with dissolveslow

m "We walked through the city some further until we reached Logan’s house. I knocked on the door and waited several minutes for Logan to respond."

play sound "fx/knocking1.ogg"
queue sound "fx/door/door_open.wav"

$ renpy.pause (3.0)

m "I started to get worried about him, but my fears were relieved when the door opened. Logan revealed himself, looking far more tired than he did yesterday."

show logan tnormal at Position(xpos = 0.75) with dissolve
show remy normal flip at left with dissolve

Lg "Sorry about taking so long. I just needed to finish something up."
c "Are you alright? You look really exhausted."
Lg "That’s because I am. I stayed up all night going through your PDA and seeing what information I could use for my generator, as well as some other things."
Lg tsmiling "Looks like you were lucky to get the PDA filled with mostly things about technology, as well as a bit about some infrastructure."
Lg tthinking "I will admit, there were some strange things stored there. One such thing was a recipe for pancakes, of all things. Another example was-{w=1.0}{nw}"
Ry shy flip "Lipstick."

$ renpy.pause (1.5)

Lg tserious "..."
Ry "It’s a long story."
Lg "And I’m not even going to ask."
Lg tnormal "Anyways, I have made a very important discovery during my research."
c "Did you find something that you can use to improve your generator?"
Lg tsmiling "Not yet, although I’m feeling pretty close to doing so."

show remy normal flip with dissolve

Lg "The things I found are far more useful in the long term, though. Probably even more so than the generators."
c "Well, spit it out already. No need for dramatic build-up."
Lg tserious "Ugh, fine."
Lg tnormal "In short, I found blueprints for the water treatment plant, as well as the factory that supplied food for the city."
Lg "With the generators we have, as well as some extra supplies that we could salvage from parts we know are beyond saving, we should be able to repair both to a point where they {i}could{/i} somewhat be functional."
Ry smile flip "You really outdone yourself by being able to make a plan like that, Logan."
Lg tsmiling "And it only took me a single sleepless night."
c "How would you go about doing such a task? You know very well that even with Remy, we wouldn’t be able to repair all of it in a reasonable amount of time."

show remy normal flip with dissolve

c "Repairing an entire facility is an immense task without construction robots, you know."
Lg tnormal "That’s what I’m still trying to figure out."
Lg "I’ll have to put that aside for later, though. At the very least, we can start making the preparations for repairs and reconstructions."
Lg "We just need to decide on which one we should start on first." #This is going to be a time consuming pain to implement later...

menu:
    "Clean water would be far more useful right now.":
        $ renpy.pause (0.5)

        Lg 'A wise choice. Clean water is hard enough to come by, so being able to get more of it would probably help us not get sick.'
        Lg "Even if we have far more water than food currently, we can’t afford one of us getting sick and putting the survival of this city in danger."
        Ry "So, is it settled then?"
        Lg "Not unless [player_name] has any second thoughts."
        c "None at all."
        Lg tsmiling "Great. We should start working as soon as we can, then."
        Lg "Meet me at the water treatment plant in one hour. I still have some things to get ready, so I can’t come with you right now."
        Ry shy flip "Try not to fall asleep. I have done that more than enough times in my life when I needed to be somewhere important."
        Lg tnormal "I’ll try."
        m "Logan went back inside while me and Remy went to the water treatment plant."

        $ renpy.pause (0.5)
        scene kolwtpout at Pan((0,0),(0,60),4.0) with dissolve
        $ renpy.pause (2.0)

        m "It didn’t take long for us to reach our destination. However, we still had quite some time left before the scheduled meetup."

        show remy normal with dissolve

        Ry "I wonder if Logan is going to arrive on time."
        c "He’s a really dedicated man. When he says he’ll do something, Logan would try everything in his might to do it."
        c "Still, maybe he {i}has{/i} fallen asleep for a few minutes."
        c "It's not like I can really blame him, either. He has been through a lot these past few days, and getting his hands on a working generator as well as a bunch of human knowledge must be really exciting for him."
        c "Even if it is causing him to lose him some much needed sleep."
        Ry shy "I used to be in a very similar situation too."
        Ry "Sometimes I had to stay up all night to do some work that the council assigned to me."
        Ry "Sure, I used the bed in my office for when it was really late at night, but sometimes you just couldn’t afford to sleep or else everybody will be angry at you for not completing your work on time."
        Ry sad "Sometimes, you’d even be angry at yourself for not finishing said work and meeting expectations."
        c "Hey, you shouldn’t think about things like that now. Remember, that’s all in the past. All that matters is what you can do right now."
        Ry "I know. It’s just that the past is always the hardest to move on from."
        Ry "Especially with cases like-{w=0.5}{nw}" #FORESHADOWINNG??????? IN THIS MOD?????!!!

        play sound "fx/motorcyclearrive_kol.wav"
        $ renpy.pause (2.0)

        m "Suddenly, I heard a vroom coming from far away. After a few minutes, I saw Logan on the horizon riding with what appeared to be a motorcycle."
        m "He approached us shortly thereafter."

        stop sound fadeout (0.5)
        stop music fadeout (2.0)

        show remy normal at right with ease
        show logan tsmiling flip at Position(xpos = 0.25) with easeinleft
        $ renpy.pause (2.0)

        play music "mx/bricks_kol.ogg" fadein 1.0

        Lg "Good afternoon, fine gentlemen! I see we are quite early, correct?"
        Ry "Well, there wasn’t really a point just wandering around when we could just wait for you here instead."
        c "How did you get a motorcycle? Last time I checked, you still went around the city on foot."
        Lg tserious flip "Last time you checked, [player_name], was more than a month ago."
        Lg "In short, the authorities gave it to me as a reward when I agreed to try and create a generator."
        Lg tsmiling flip "The gas needed for the motorcycle, however, is another story."
        c "At least you have an effective way of traveling around the city. That may be really useful at some point."
        Lg tnormal flip "It already has been incredibly useful."
        Lg tserious flip "Now, here are some plans I made that we could use."
        m "Logan pulled out a few blueprints and a hoard of papers filled with his notes. All three of us went through the numerous options available and eventually settled on a plan."
        m "I was to go inside the building and see what parts of the facility could still be used, while Logan scoured for any salvageable electronics. Remy was left with looking for any structural flaws that could put the building in danger."
        c "(Well, here goes nothing...)"

        stop music fadeout (2.0)
        $ renpy.pause (1.0)
        scene kolwtp3 at Pan ((0, 0), (0, 127), 4.0) with dissolve
        $ renpy.pause (3.0)
        play music "mx/protocol_kol.ogg" fadein 1.0

        m "I entered the water treatment with a feeling of uncertainty, since anything could go wrong at any point during my search."

        $ renpy.pause (1.0)
        scene kolwtp2 at Pan ((0, 0), (0, 0), 4.0) with dissolve
        $ renpy.pause (2.0)

        m "I looked around to see if anything could be salvaged, but most of the metal scraps I could find had already rusted beyond any use. However, upon further inspection, I spotted a few boxes with some supplies near the entrance to the main chambers."
        m "There was a box filled with wooden planks, and another with some steel bolts. Behind all of them were a few piles of bricks and ceiling tiles, as well as some cement."
        c "(These will definitely prove useful.)"

        $ renpy.pause (1.0)
        scene kolwtp1 at Pan ((0, 0), (0, 0), 4.0) with dissolve
        $ renpy.pause (2.0)

        m "I wandered around the facility some more, hoping to find something that could be used to repair the machines or something else that will prevent further degradation, but I couldn’t find anything else."
        m "I decided that now was the time to report my findings to Logan and Remy."

        play sound "fx/creak2.ogg"
        queue sound "fx/creak3.ogg"

        m "Suddenly, I heard a strange creaking noise from the roof."
        $ renpy.pause (2.0)
        m "A support beam came loose soon after, crashing into an unstable wall and shattering a large window pane, spreading broken glass all around me."
        m "I could hear someone calling out to me."

        stop sound

        Ry sad "[player_name]! Are you alright?"
        c "Yeah, just startled, that’s all."

        show remy normal flip at left with easeinleft

        Ry "I’m glad to hear that, then."
        Ry smile flip "Quite ironic that you were nearby, don’t you think?"
        c "How so?"
        Ry normal flip "I wanted to warn you about the potential hazards of the support beams on the roof, but it seems that those very support beams caused me to find you."
        c "I just hope that it doesn’t happen again. If the beam’s angle was just a bit off, then I could have died."
        Ry look flip "Agreed."

        scene kolwtpout at Pan((0,0),(0,45),3.0) with dissolve
        $ renpy.pause (2.0)

        m "We both went outside, deciding that we should deliver our reports to Logan as soon as possible. Luckily for us, he was already waiting outside."

        show logan tserious flip at Position(xpos = 0.25) with dissolve
        show remy look at right with dissolve

        Lg "You two alright? I heard a strange crash from inside, and I figured that you two may be in trouble."
        Ry "We’re fine, thanks. Sadly, I think that this will happen a lot more often."
        Ry "According to what I found, a lot of the supports are failing. I’m no engineer, but even I can see that when walls and support beams start to wear out, bad things will follow."
        Ry smile "Luckily, I think that most of it could still be repaired, even if some parts are beyond saving."
        Ry normal "I think it would be best if those faulty parts are removed entirely to avoid further damages."
        Lg "I see. This makes for some tricky problems, as it could crash into the main purifiers if we take too long. Are the major facilities still intact?"
        Ry "As far as I could see, everything should still be secure. Only the parts on the outermost corridors need some serious attention."
        Lg tsmiling flip "Excellent. What did you find, [player_name]?"
        c "Well, I found a few supplies near an entrance to the main chamber that could be used to either reinforce weaker parts of the building, or completely repair parts to effectively start the plant back up."
        c "Aside from that, nothing else of use."
        c "That is, unless you consider rusted scraps of metal useful."
        Lg tserious flip "No, I don’t."
        Lg "What were the materials you found?"
        c "Bricks, cement, wood, ceiling tiles and some steel bolts."
        Lg "I see. It looks like the officials wanted to repair the plant to try and get clean water flowing to the city once more."
        Lg tthinking flip "Not that they could do much, anyway."
        Lg tnormal flip "All the necessary components were still there in the purifiers, so nothing needs to be added."
        Lg "I’m glad that the only thing needed to get this water treatment plant up and running again is some power and a few repairs to some of the purifiers."
        Lg "Looks like we struck it lucky, aside from that minor accident you two got yourselves into."
        Lg tsmiling flip "Regardless, you two did a good job. I believe that we’ll be able to repair this water treatment plant in a few weeks if we plan it well enough."

        $ kol_tld_wtpchosen = True


    "Getting more food available will help us right now.":
        $ renpy.pause (0.5)

        Lg "Right. I’d say that between the three of us, there’s enough food left for about a week at most, and that's {i}with{/i} rationing in mind."
        Lg "To be honest, I don't know about your personal food supplies [player_name], but I'd very much like to replenish mine."
        Lg "If we could get the factory up and running again as fast as we can, then we should be safe."
        Lg tthinking "That is, until we start to experience water problems."
        Lg tserious "Point is, choosing to repair the factory first is a good choice."
        Ry "So, food production it is, then?"
        Lg "Correct."
        c "Alright, how do we get started?"
        Lg "Meet me at the factory in about one hour. There are a few things that still have to be sorted, so I won’t come with you right now."
        Ry shy flip "Try not to fall asleep. I have done that more than enough times in my life when I needed to be somewhere important."
        Lg tnormal "I’ll try."
        m "Logan went back inside while me and Remy went to the factory."

        $ renpy.pause (0.5)
        scene kolfactoryout at Pan((0,0),(0,60),4.0) with dissolve
        $ renpy.pause (2.0)

        m "It didn’t take long for us to reach our destination. However, we still had quite some time left before the scheduled meetup."

        show remy normal with dissolve

        Ry "I hope Logan is doing okay. I wouldn’t want him to pass out due to overworking himself."
        c "Don’t worry about him. He always managed to pull through while somehow being even more tired than he is now."
        c "One night without sleep isn’t that much of a setback for him."
        Ry look "Still, it isn’t healthy to stay up all night working."
        Ry sad "Sadly, I’m talking from personal experience here, as well as what I've seen in others, as you might know."
        c "Well, can you blame him?"
        c "Logan has gone through a lot these past few days, especially now that he has access to a working generator, as well as a bunch of human knowledge."
        c "If anything, all of this must be really exciting for him."
        Ry "You know, I can understand working through the entire night, as I used to do that a lot when the council assigned some important work for me."
        Ry look "Sure, I used the bed in my office for when it was really late at night, but sometimes you just couldn’t afford to sleep, or else everybody will be angry at you for not completing your work on time."
        Ry sad "Sometimes, you’d even be angry at yourself for not finishing said work and meeting expectations."
        c "Hey, you shouldn’t think about things like that now. Remember, that’s all in the past. All that matters is what you can do right now."
        Ry "I know. It’s just that the past is always the hardest to move on from."
        Ry "Especially with cases like-{w=0.5}{nw}"

        play sound "fx/motorcyclearrive_kol.wav"
        $ renpy.pause (2.0)

        m "Suddenly, I heard a vroom coming from far away. After a few minutes, I saw Logan on the horizon riding with what appeared to be a motorcycle."
        m "He approached us shortly thereafter."

        stop sound fadeout (0.5)
        stop music fadeout (2.0)

        show remy normal at right with ease
        show logan tsmiling flip at Position(xpos = 0.25) with easeinleft
        $ renpy.pause (2.0)

        play music "mx/bricks_kol.ogg" fadein 1.0

        Lg "Good afternoon, fine gentlemen! I see we are quite early, correct?"
        Ry "Well, there wasn’t really a point just wandering around when we could just wait for you here instead."
        c "How did you get a motorcycle? Last time I checked, you still went around the city on foot."
        Lg tserious flip "Last time you checked, [player_name], was more than a month ago."
        Lg "In short, the authorities gave it to me as a reward when I agreed to try and create a generator."
        Lg tsmiling flip "The gas needed for the motorcycle, however, is another story."
        c "At least you have an effective way of traveling around the city. That may be really useful at some point."
        Lg tnormal flip "It already has been incredibly useful."
        Lg tserious flip "Now, here are some plans I made that we could use."
        m "Logan pulled out a few blueprints and a hoard of papers filled with his notes. All three of us went through the numerous options available and eventually settled on a plan."
        m "I was to go into the factory and look if there were any resources that could be used, while Logan searched for functional electronics. Remy was left searching for potential dangers."
        c "(Let’s hope that there are still potential resources left.)"
        m "I entered the factory, hoping that the interior would resemble the seemingly fixed exterior."

        stop music fadeout (2.0)
        $ renpy.pause (1.0)
        scene kolfactory3 at Pan ((0, 0), (0, 127), 4.0) with dissolve
        $ renpy.pause (3.0)
        play music "mx/vanished_kol.ogg" fadein 1.0

        m "My hopes soon vanished after encountering several walls with graffiti and heaps of scraps on the floor."
        m "It seemed that the factory wasn’t in as good of a state as I thought it would be. Regardless, I started searching for resources."

        $ renpy.pause (1.0)
        scene kolfactory4 at Pan ((0, 0), (0, 0), 4.0) with dissolve
        $ renpy.pause (2.0)

        m "I eventually encountered what seemed to be a storage room a few corridors from the entrance. I opened the door, finding a sealed container with dried fruit snacks."

        menu:
            "Take a packet of fruit snacks.": #Yum
                m "I took a packet of fruit snacks from the sealed container and put it in my pocket for later."
                c "(I wonder what Remy would think of these...)"

                $ kol_tld_fruitsnackstaken = True

            "Leave them all for now.":
                m "I decided to leave the fruit snacks for later when we inevitably retrieved them. For now, my job isn’t finished yet."


        $ renpy.pause (1.0)
        scene kolfactory2 at Pan ((0, 0), (0, 0), 4.0) with dissolve
        $ renpy.pause (2.0)

        m "I kept looking around the factory, hoping to see if there was anything else of value. Sadly, not much was found except for a few stray wooden planks and some scrap metal."
        c "(Looks like I’m done here for now.)"

        play sound "fx/zap_kol.wav"
        $ renpy.pause (1.0)

        m "On my way outside, however, I heard a zapping noise, followed by some swearing."
        scene kolfactory1 at Pan ((0, 20), (0, 20), 2.0) with dissolve
        $ renpy.pause (2.0)

        m "I rushed to the source of the noise and found Logan staring angrily at an open electrical panel in the central facility."

        show logan tserious at left with dissolve

        c "Logan! Are you alright?"

        Lg "If alright and frustrated are the same words to you, then yes, I am {i}really{/i} alright."
        c "I heard a loud zapping noise, so I thought you would be-{w=0.8}{nw}"
        Lg "Electrical discharge. I didn’t expect that a backup battery could still have enough power to be able to cause a discharge {i}that{/i} strong, however."
        Lg tthinking flip "It really makes me wonder how much tech is actually still functional in this city."
        Lg tserious flip "Still, it wouldn’t have mattered anyway, considering that most of the advanced electronics here are fried beyond belief."
        c "Well, at least you’re safe."
        Lg tsmiling flip "Did you really think that a little zap would be able to dissuade me after all I went through these past few years?"
        Lg "That was but a scratch!"
        Lg tthinking flip "...or a zap, in this case."
        c "I think that we should get out of here."
        Lg tnormal flip "Yeah. I had my fill of old electronics for today."

        scene kolfactoryout at Pan((0,0),(0,45),3.0) with dissolve
        $ renpy.pause (2.0)

        m "We both went outside so that we could group up with Remy whenever he arrived. Luckily for us, it didn’t take long before he appeared."

        show logan tnormal flip at Position(xpos = 0.25) with dissolve
        show remy normal at right with dissolve

        Ry "Hello, [player_name]. I see that you have already met with Logan."
        c "Yeah. There was just a slight problem that he needed help with, that’s all."
        Ry look "I see. Is everything alright?"
        Lg "No need to worry, Remy. Nothing more than a slight inconvenience."
        Lg "Tell me, what did you find?"
        Ry "Well, I saw that the outside looked in a pretty good shape, but that’s kind of obvious."
        Ry "The interior, though, has a few problems."
        Ry "I don’t want to sound harsh, but a lot of the structural supports seem extremely unstable."
        Ry "This could lead to some rooms collapsing, which could even damage the machines. Luckily, that’s only a worst case scenario."
        Ry normal "The best case scenario would be that the supports would still last for a few years."
        Lg "I see. Looks like reinforcements are our main priority."
        Lg tserious flip "In terms of the electrical components, I’m afraid most of it is destroyed."
        Lg "That doesn’t surprise me, though. It would have been a miracle if anything useful still worked as intended."
        Lg "I still think that I could be able to partly fix this factory so that it could start running again, although it would put quite the dent in our resources available."
        Lg tnormal flip "Speaking of which: what did you find, [player_name]?"
        c "Just a few wooden planks and some scrap metal."
        c "However, I did find a container with some food, though"
        #That moment when your kinda OC has an ungodly amount of plot armour yet is also the voice of reason in whatever random scenario you create...
        show logan tsurprised flip with dissolve

        Lg "{i}WHAT?!{/i}" with Shake ((0, 0, 0, 0), 2, dist=18)
        Lg "You mean to tell me that there is food stored in a near abandoned place that the authorities just seemed to forget existed?"
        c "It’s not much, but it should boost supplies for a while."
        Ry "What kind of food is it, if I may ask? Is it something that will last us a long time?"
        c "A few packets of dried fruit snacks. Nothing much, mind you, but I estimate that it's enough to extend our rations for about a few days."
        Lg tnormal flip "Good. Looks like the situation has just gotten a little less dire."
        Lg tsmiling flip "Regardless, you two did a great job. It will take a lot of time and effort to repair the factory to a functionable state, but with the generators and the PDA, it should definitely be possible."


Ry smile "I’m glad that I could have helped you, Logan."
c "Me too."
c "So, what should we do now?"
Lg tnormal flip "Whatever you want. I’ll try to make plans for our next move, so in the meantime, you two take it easy."
Lg "Maybe you could, I don't know, explore the city a bit?"
Ry normal "We actually already did that yesterday."
Ry look "However, I think that you’re the one who should take it easy, Logan. After all, you didn’t sleep last night. It would be far better for you if you rested for a while."
Lg tserious flip "..."
Lg "Alright."

stop music fadeout (2.0)

Lg tnormal flip "Let’s just hope that-{w=0.6}{nw}"

play sound "fx/raiders_kol.wav"
$ renpy.pause (7.0)
stop sound
m "Suddenly, a loud cluster of noises erupted from far outside the city borders. Strangely, it sounded like a swarm of bees, but far more mechanical."

Ry "What was that?"

show logan tserious flip with dissolve

Lg "Damn it! And here I hoped that things {i}wouldn't{/i} get worse!" with Shake ((0, 0, 0, 0), 2, dist=25)
Lg "I'm way too tired to deal with this right now..."
c "Are you talking about-{w=0.8}{nw}"
Lg "Sadly."

play music "mx/attack_kol.ogg" fadein 2.0

#Look at me! I'm artificially creating a pseudo intense scene for no apparent reason with a track that doesn't fit at all!

Lg "Raiders are coming."
Ry "Wait, are they those mobile groups you once told me about?"
c "Yeah, only this time, they’re going to cause a lot of problems if we don’t prepare this very second."
Lg "I’ll take my motorcycle and ride to the northern gate, as it’s most likely where they will appear."
Lg "Remy, see if you could fly and estimate how long until they arrive."
Ry shy "I- I’ll try."

hide remy with dissolve
play sound "fx/takeoff.ogg"

m "Remy took off with a heavy beating of his wings. A few seconds passed before I saw him scouting the city borders in the sky."

show logan tserious flip with ease

Lg "[player_name], I’ll need you to hide the generators and your PDA from the raiders, or else all our work will be for nothing."
c "But a generator is already hidden at my place, with the other two still being in your possession. As for the PDA, it should still be where you last put it, since you never gave it back to me."
$ renpy.pause (2.0)
Lg "*sigh*"
Lg "Good enough. Hop on then. We’ll see what we can do."

hide logan with dissolve
play sound "fx/motorcycleaccelerate_kol.wav"

$ renpy.pause (4.0)

m "I climbed on Logan’s motorcycle as we rushed to the northern gate. Luckily, due to how fast Logan drove, it didn't take us long before we reached our destination."

scene kolguardtower at Pan ((0, 180), (0, 0), 5.0) with dissolve
stop sound fadeout (1.0)

m "Logan rushed into one of the guard towers and armed himself with a submachine gun as an extra bit of preparation."
m "Remy landed right next to me shortly afterwards."

play sound "fx/landing.ogg"
$ renpy.pause (1.0)

show logan tserious flip at Position(xpos = 0.25) with dissolve
show remy normal at right with dissolve

Ry smile "Looks like Logan made a good guess. The raiders are heading to this gate as we speak. By the looks of it, they’ll arrive in five minutes."
Lg "Just in time, then."
Ry normal "However, they don’t really look that hostile. In fact, I spotted a few individuals that seemed really exhausted from travel."
Ry "I don’t think they want to cause harm to us."
c "We’ll just have to find out, then."
c "I think that it would be best if you hid somewhere for now, Remy."
c "I fear that if the raiders saw a dragon, they might start to panic and open fire on us."
Ry look "I understand."
Ry "Still, it would be nice not to run away from everything for once."
c "I know, Remy."

scene kolcitygate with dissolvemed
$ renpy.pause (2.0)
m "A few minutes passed before a large group of people appeared at the gate. There were quite a lot of motorcycles with several people clinging to each other on top."
m "A worn out man that seemed to lead the gang climbed off of his motorcycle and walked towards me and Logan."
m "Strangely enough, the cloak he wore somewhat reminded me of the Administrator, but without the mask."

show logan tserious flip at Position(xpos = 0.25) with dissolve
show martin shocked at Position(xpos = 0.75) with easeinright

"???" "Wait! Don’t shoot us!" #And now Martin reveal! Boy are character reveals exciting!
Lg "Then you better tell us what the heck you’re doing here."
Lg "And make it quick!" with Shake ((0, 0, 0, 0), 2, dist=10)
"???" "Alright, alright!"
Mt serious "First off, my name is Martin, and I don’t want to hurt you."
Mt "I know that we might look like a group of raiders, but that’s only because of the fact that we have been constantly running away for the last few weeks."
c "What were you running away from?"
Mt "How do I put this in a light way..."
Mt "Well..."
Mt "We were running away from raiders."
Lg tthinking flip "So, you’re telling me that the people here who look like raiders {i}aren’t{/i} raiders?"
Lg tserious flip "I still think that a valid explanation is due."
m "I could see that Logan gripped his gun even more tightly. Luckily, he lowered his weapon, immediately causing a noticeable drop in tensions."
Mt "It’s quite a long one. Do you want the short version of our story or the full explanation?"

menu:
    "I think that we can hear you out.":
        $ renpy.pause (0.5)

        Mt "Okay. I’ll try to be as thorough as I can. Please bear with me for a while."

        stop music fadeout (2.0)

        scene black with dissolveslow #Another infodump. Yay...
        $ renpy.pause (2.0) #At least you can kinda skip this one...
        nvl clear #Damn, why are infodumps so hard to make interesting?!
        window show

        play music "mx/saviour_kol.ogg" fadein 1.5

        n "We came from a somewhat small city about four hundred miles southeast from here. That’s about six hundred and forty-three kilometers, if you didn’t know. Personally, I believed that we were the only place left on earth that were still somewhat civilised, as we couldn’t establish communication with anywhere else."
        n "We held out for quite some time after the solar flare hit, with enough resources and technology left from the old world that we could operate on a very similar basis to how we did back then, to a certain degree."
        n "Most of our facilities and generators were functional, and if they weren’t, we had the skill and tech to be able to repair them. My guess is that we simply lucked out."

        window hide
        nvl clear
        window show

        n "Sadly, all this technology caused many of the civilians to start becoming greedy. People who I thought I could trust started to turn on the city and the people that thrived within. I thought that tensions only raised temporarily, and that they would eventually be settled."
        n "How wrong I was."
        n "A civil war started to break out between those who wanted to take what we had for themselves, and those that still wanted to help each other with a sense of community spirit."
        n "Those that wanted what we had for themselves were few, sure, but they had a very dangerous mentality:"
        n "“If I can’t have this for myself, then nobody will be able to.”"

        window hide
        nvl clear
        window show

        n "Things started to get dangerous for those who still wanted to help each other, so a handful of people decided that it would be best to run away from the city while they still had the opportunity to do so."
        n "Those people are the very people you see in front of you now."
        n "I have only heard reports from what happened to the city by a few people that joined us later. Any spare equipment that was left had been destroyed in skirmishes by the looters. The city is now a large heap of rubble and ash, with us being the only survivors."

        window hide
        nvl clear
        window show

        n "Eventually, after searching for a sign of any city that happened to be still standing, we encountered a group of raiders. As if we lucked out again, they took pity on us after hearing our story. Since we had no other choice for survival, we had to join them."
        n "The amount of horrors I committed while under their wings will haunt me for the rest of my life. I helped loot and destroy ruined camps, and cause chaos to any group still out there in the desert."
        n "In the end, we committed the very same acts we were originally running away from."

        window hide
        nvl clear
        window show

        n "One day, we decided that we simply couldn’t continue anymore. We took what we needed the most, like clean water and food rations, as well as some gas to refuel our motorcycles, and left. Sadly, even in the dead of night, we didn’t go unnoticed."
        n "I think that we did successfully escape, since we hadn’t been ambushed in about a week, but I can’t be sure. Most of my group was still paranoid, however, so we needed help, and fast."
        n "One of our scouts delivered that hope to us when he found another city-like structure on the horizon. Morale started to increase dramatically. I can’t tell you how happy everybody was, knowing that maybe, just {i}maybe{/i}, we could return to our old life again."

        window hide
        nvl clear
        window show

        n "The journey here, however, wasn't so easy. Our gas supplies were running dangerously low, even with the reserves we took from the raiders. The only choice we had left was to transfer fuel from our most damaged motorcycles and abandon them in favour of those that were most likely to make the journey."
        n "This caused some problems, as you could imagine. Not everybody could be transported, so some had to go on foot. We eventually decided that it would be best if we made shifts, taking turns to ride the bikes and waiting for the others to catch up. A slow process, sure, but the most efficient one we could manage."

        window hide
        nvl clear

        scene kolcitygate with dissolvemed
        show logan tserious flip at Position(xpos = 0.25) with dissolve
        show martin serious at Position(xpos = 0.75) with dissolve
        $ renpy.pause (2.0)

        Mt "Eventually, after many hardships, we made it to this city."
        Mt "The rest is history."


    "Make it as quick as you can.":
        stop music fadeout (1.5)
        $ renpy.pause (0.5)

        Mt "A- Alright, I’ll try."

        play music "mx/saviour_kol.ogg" fadein 0.5

        Mt "We lived in what we believed was the last civilised city on earth."
        Mt "Sadly, infighting started to rise over these last few months, which caused a civil war inside of the city."
        Mt "Any spare functional equipment we had was destroyed in acts of looting."
        Mt "These few people you see here before you are survivors that fled right after the civil war in our city started."
        Mt "We hoped that, maybe, we could find somewhere else to live."
        Mt "That wish came true, however, when one of our scouts spotted your city in the distance."
        Mt "One thing led to another, and here we are."
        Lg "That still doesn’t explain why you’re running from raiders, though."
        Mt "We were lucky enough to be able to join a group of raiders, so that we could get a few resources to survive."
        Mt "However, we eventually realised that we became what we were originally running from, so we ran away in the dead of night."
        Mt "We haven’t stopped running since."

Lg tthinking flip "I see."
Lg tserious flip "That’s very sad and all, but how do we know that the raiders haven’t secretly followed you here?"
Lg "Heck, how do we know that {i}you’re{/i} not secretly raiders. There are a few holes I see in your story, so I’m not sure I believe you."
c "You’re overreacting, Logan. So what if there are a few holes in their story? Nobody can remember every single part of their life, much less when they are under an extreme amount of pressure like those…"
c 'Uh...'
Mt "You can call us refugees."
c "Ah, refugees. Shouldn’t you at least have some time to think before you jump to conclusions?"

$ renpy.pause (1.5)

Lg "Hmph."
Lg "Fine. We’ll discuss it with Remy and see what he thinks about this."
c "Alright, Martin. Here’s the deal. We will discuss whether we should welcome you to what remains of our city."
c "In the meantime, feel free to wait outside the city walls until we have made our decision."
Mt happy "Thank you so much. You don’t know how much this means to us all!"

hide martin with dissolve
hide logan with dissolve

m "Martin left to tell the rest of his group about our conversation, as well as to give orders to wait ouside the city walls until further notice, while me and Logan went to go and find Remy."


scene black with fade
stop music fadeout (2.0)
$ renpy.pause (2.0)
scene kolguardtower at Pan ((0, 180), (0, 180), 3.0) with dissolve

$ renpy.pause (4.0)
show remy shy flip at left with dissolve
show logan tserious at Position(xpos = 0.75) with dissolve

play music 'mx/ancient_path_kol.ogg' fadein 2.0

Ry "Wait, so there was another human city this whole time?"
c "It seems so. I don’t know how they managed to live in the harsh conditions our city was left in after the solar flare, but they somehow managed."
Ry normal flip "Fascinating. I would have never figured that there would still be anyone else left besides you and Logan."
Ry look flip "Still, don’t you think it’s strange that nobody realised that until now?"
c "Well, I now have a suspicion that the authorities were able to make contact with other settlements in some way or another, but never told the masses."
Lg "Alright, enough with your suspicions. Now that Remy has been informed, we need to make a plan with these so-called “refugees”."
Lg tserious "I say that we prevent them from entering. The risk is far too great for untrustworthy people to enter and destroy everything we have worked for."
Lg "Besides, they have stolen before. What prevents them from doing so again?"
Lg "Not to mention the potential risk of {i}more{/i} raiders coming."
Lg "This whole situation just seems to me like one big, fat trap to me."
Ry normal flip "I feel that we should let them in."
Ry "If what Martin says is true, then we could potentially have much more skilled individuals that could help with some repairs."
Ry "We could also start to repopulate the city..."
$ renpy.pause (1.0)
Ry shy flip "When the time comes."
Ry normal flip "The point I’m trying to make is that by letting these people in, the chance for our survival will increase drastically."
Ry smile flip "Even more so with the generators and the PDA we have."
Lg "Not if they steal those first, however."
Lg "Or ruin what’s left of the infrastructure we could actually repair."
Lg "If that were to be the case, then there won’t be any hope to repair anything, regardless of whatever help we may receive."
Lg "They cannot be trusted. End of discussion."
Ry look flip "But we don’t have another choice."
Ry "Logan, you said yourself that we can’t hope to repair anything necessary if we don’t get more people."
Ry "Why would you pass the opportunity up when it presents itself to you on a silver platter?"
Lg "Because I know danger when I see it, and those people have the word “Danger” written all over their faces."

$ renpy.pause (2.0)
Ry "..."
Lg "..."
Ry "[player_name], what do you think would be the best course of action?"
Lg tthinking "Yeah, now that I’ve thought about it, you haven’t said anything yet."
Lg "What should we do to these raiders?"
Ry shy flip "You meant refugees."
Lg "Whatever."

menu:
    "We desperately need any extra help we can get.":
        $ renpy.pause (0.5)

        c "We need all the help we can get right now. There is simply no way that we could rebuild the entire city if it’s just the three of us."
        c "Besides, what Remy said is correct. If at least some of those people are skilled, then we could actually make the city prosper again."
        c "We simply have no other choice."
        Lg tserious "Did you even listen to what I said?"
        Lg "If we let them in, then any help that we could receive won't matter if they steal and destroy everything first!" with Shake ((0, 0, 0, 0), 2, dist=10)
        c "Look, Logan. If we turn Martin and his group away, then we could kiss all hope goodbye."
        c "You're willingly throwing away any hope that we might have here."
        c "You know very well that this city {i}will{/i} degrade without any help, as repairing the entire city all by ourselves is impossible."
        c "We have nothing to lose. If they do turn out to destroy the city, then we're doomed."
        c "If we don't accept them, then we're also doomed."
        c "However, if Martin and his group turns out to be helpful to us, then we can thrive again."

        show logan tthinking at Position(xpos = 0.75) with dissolve
        $ renpy.pause (3.5)

        Lg tserious "*sigh*"
        Lg "As much as I don’t want to do this, I guess that I’ll have to trust your judgement."
        Lg "Just don’t come crying to me when all our work has been undone."
        c "I’ll go tell Martin, then."

        hide remy with dissolve
        hide logan with dissolve

        scene kolcitygate with dissolvemed
        $ renpy.pause (2.0)

        m 'I went outside the city gate and found Martin talking with some of the members of his group. When he spotted me, his face seemed to light up.'

        show martin normal with dissolve

        Mt "Oh! You’re back!"
        Mt "So, have you come to a conclusion?"
        c "Yes, we have. You and your group are free to reside in the city, under two conditions."
        c "One, your group will help to restore what’s left of the city so that we all may thrive."
        c "Two, under no circumstances are you or anybody else allowed to cause any form of chaos, or your entire group will be expelled from the city walls."
        c "Do you accept these terms?"
        Mt happy "I gladly do."
        Mt "I don’t think words can express how much I’m grateful to you for giving us a chance."
        Mt normal "So, when are we allowed to enter?"
        c "Feel free to enter any time you want."
        c "Oh, and don’t mind where you can stay. Most of the houses are empty, so any place will suffice."
        Mt "Gotcha."

        hide martin with dissolve

        m "Martin went to his group to tell the good news. Soon, many cheers could be heard."

        play sound "fx/raidersenter_kol.wav"

        m "There was a huge rush at the gate with several motorcycles swarming the streets. After a few minutes, the outskirts were empty again."
        m "However, Martin stayed behind with a confused expression on his face."

        show martin confused with dissolve

        Mt "Wait, I thought that there would be more people here. This entire city just seems like a ghost town to me."
        Lg "That’s because it essentially is."
        m "Logan appeared from around the corner, still holding his submachine gun."

        show martin confused at Position(xpos = 0.75) with ease
        show logan tserious flip at Position(xpos = 0.25) with easeinleft
        $ renpy.pause (2.0)

        Lg "Just a few weeks ago, the city was still bustling with life."
        Lg "Now, it’s only the three of us."
        Mt "Three?"
        Mt "Forgive me, but I have only seen you and..."
        Mt "Uh..."
        c "I’m [player_name]. The other person here right now is Logan."
        c "My apologies. I only now realised that I haven’t formally introduced myself yet."
        Lg "Well, yes."
        Lg "The third person here is Remy, but he’s a bit..."

        $ renpy.pause (1.0)

        Lg "Foreign."
        Mt happy "Oh, don’t worry about it! After traveling for so long, I doubt that much would surprise me."
        Lg "I significantly doubt that."
        Lg "Prepare yourself for what you’re about to see."
        m "Logan then called for Remy. After a short while, he shyly appeared at the city gate."

        show remy normal flip above logan at Position(xpos = 0.03) with easeinleft
        show martin shocked at Position(xpos = 0.85) with ease

        m "Martin’s face twisted with shock and fear."
        Mt "-aaaaaaAAAAAAAAHHHHHHHHHH!!!" with Shake ((0, 0, 0, 0), 3, dist=35)
        Mt "D- D- DRAGON!!!"
        c "Calm down, Martin. Remy is really friendly. I promise that he won’t hurt you."
        Ry "Hello! You must be Martin, correct?"
        Mt "IT TALKS!" with Shake ((0, 0, 0, 0), 1, dist=10)
        Mt "I-{w=0.3}{nw}"

        hide martin with easeoutbottom

        stop music fadeout (20.0)

        m "I could see that Martin’s knees started to grow weak. He soon fell over, but I managed to catch him just before he hit the ground."
        c "Are you alright?"
        m "No response came. It seemed that Martin is unconscious."
        Lg "Damn it. Looks like we’ll have to take care of the brat for a while."
        c "No need to be so harsh, Logan. He’s just trying to survive like the rest of us."
        Ry shy flip "I shouldn’t have revealed myself so suddenly. If I was a bit more patient, then he wouldn’t have passed out."
        c "You shouldn’t worry, Remy. I doubt even the bravest would handle an encounter like that well."
        Ry "But you were perfectly fine when we first met."
        c "That’s only because I knew that I was about to meet an entire civilisation of dragons beforehand."
        c "Still, maybe we should explain everything to him as soon as he wakes up."
        Lg tnormal flip "That would probably be for the best."
        Lg "If panic starts to rise because of the news of an actual, existing dragon in the city, then we can kiss all our hopes and dreams goodbye."
        Lg tserious flip "For good."
        c "I’ll take him to your place, if that’s fine."
        Lg "Sure."
        c "Remy, would you like to come with me?"
        Ry smile flip "It would be my pleasure."

        scene black with fade
        $ renpy.pause (1.0)
        play sound "fx/steps/rough_gravel.wav"

        m "I carried Martin on my back as we went to Logan’s house. It took a while, as Martin was surprisingly heavy, but we made it in the end."
        $ renpy.pause (2.0)

        stop sound
        stop music
        scene kolloganhouse at Pan ((0, 220), (0,220), 0.0) with dissolve

        m "I put Martin on the couch and waited for him to wake up."

        $ renpy.pause (2.0)
        scene black with fade
        $ renpy.pause (1.0)

        m "Several hours passed before he returned to consciousness."

        scene kolloganhouse at Pan ((0, 220), (0,220), 0.0) with dissolve

        show martin confused flip at Position(xpos = 0.25) with dissolvemed

        play music "mx/morningrise.ogg" fadein 4.0

        Mt "W- Where am I?"
        c "You’re at Logan’s house. You passed out just after seeing Remy."
        Mt "You mean that..."
        m "He shuddered."
        Mt serious flip "...dragon?"
        c "Yes. Would you like to see him again?"
        Mt "I think that I need to prepare myself a bit first, though."
        Mt "In the meantime, could you maybe tell me why the city is so empty?"
        c "Sure. It all started when we found a portal during one of our scouting missions..."

        scene black with fade #Why so many damn fade to black scenes? That's a bit exccessive...
        $ renpy.pause (2.0)

        scene kolloganhouse at Pan ((0, 220), (0,220), 0.0) with dissolve
        show martin serious flip at Position(xpos = 0.25) with dissolve

        c "...now only me, Logan and Remy remain in this city."
        Mt happy flip "Amazing! An entire civilisation filled with dragons, of all things!"
        Mt serious flip "It’s sad that they aren’t alive anymore, though."
        Mt "I’m really sorry for all of your losses, in both human and dragonkind."
        c "Thank you."
        c "Now you understand why our situation is so dire and why we can’t afford to risk anything too chaotic."
        Mt "I see."
        Mt "I just wish that we could have recovered some of our tech, though."
        Mt happy flip "If we combined what we had with what you have, then we could almost recreate a pre-solar flare city!"
        Mt serious flip "Well, we can only dream, now."
        c "But we don’t have to."
        c "With your help, we could repair much of our broken infrastructure and electronics."
        Mt "I’m still immensely surprised that Logan actually managed to be able to repair something damaged by the flare."
        Mt "Our electricians have tried for months to get anything up and running again, but nothing worked."
        c " Maybe it was simply a mixture of dumb luck and genius skill."
        Mt "Maybe."

        $ renpy.pause (1.5)

        Mt "..."
        Mt normal flip "I think that I’m ready to see Remy now. Could you maybe get him for me?"
        c "Of course."
        m "I called for Remy, to which he responded with a quick entrance into the room."

        show remy normal at right with easeinright

        Ry "Is there something I can help you with, [player_name]?"
        c "Actually, Martin wanted to see you."
        Mt "Ah, Remy."
        Mt serious flip "I just wanted to say that I’m really sorry for freaking out."
        Mt "I didn't expect to see a living, talking dragon. When Logan said that you would be a bit foreign, I didn’t expect that this is what he meant."
        Ry smile "No worries! I understand that this is really unusual for you, so don’t feel too bad about yourself."
        Mt "Thank you, Remy."
        Mt normal flip "Friends?"
        Ry normal "Friends."

        $ renpy.pause (1.0)
        m "The two of them shaked hands, although I could see that Martin wasn’t entirely comfortable yet."
        Mt "Well, it was really nice meeting you all."
        Mt "I think that I should go now and rejoin with the others. They are probably sick from worrying about me."
        Mt happy flip "See you tomorrow!"
        c "Goodbye, Martin. Can you find your way around the city?"
        Mt normal flip "I’ll work it out eventually. Cheers!"

        hide martin with dissolve
        hide remy with dissolve

        $ renpy.pause (2.0)
        scene kolloganhouseevening at Pan ((0, 220), (0,220), 0.0) with dissolve
        $ renpy.pause (2.0)

        m "Martin left the house, leaving me and Remy alone. We decided that we should go back home, as it started to get dark. Before we did that, however, I took my PDA back from Logan so that I could put it somewhere more secure, just in case."

        stop music fadeout (2.0)
        $ renpy.pause (2.0)

        $ kol_tld_martinaccepted = True


    "We have too much to lose to risk it all now.":
        $ renpy.pause (0.5)

        c "You’re right, Logan."
        c "We have far too much to lose, so we can’t risk letting Martin and his group inside our city walls."
        c "It’s not something I’m comfortable with, but if we have any choice to survive, then we need to protect what little we have left."
        Lg tsmiling "Glad you understand my train of thought, [player_name]."
        Ry look flip "I understand."

        $ renpy.pause (1.0)

        Ry sad flip "I really just wanted to try and help them, that’s all."
        Ry "However, if you feel that this is the best option for us all, then so be it."
        Ry "I’ll wait here until you come back."

        hide remy with dissolve
        hide logan with dissolve
        scene kolcitygate with dissolvemed
        $ renpy.pause (2.0)

        m "Me and Logan went to Martin to share the news. As we approached, I saw Martin talking with some of the members in his group. When he saw us, his face visibly brightened."

        show martin normal at Position(xpos = 0.75) with dissolve
        show logan tserious flip at Position(xpos = 0.25) with dissolve

        Mt "Oh! You’re back!"
        Mt "So, have you come to a conclusion?"
        Lg "Yes, we have. Sadly, we’re not letting you in the city, as we simply don’t trust you enough with what little we have left."
        Lg "You’re also way too big of a risk to invest in."
        Lg "Especially if you’re running away from actual raiders that might attack {i}us{/i} at any time."

        show martin shocked with dissolve

        Mt "Wait, what?!" with Shake ((0, 0, 0, 0), 2, dist=15)
        Mt "You’re really going to reject us, after everything we’ve been through?"
        c "I’m really sorry, Martin, but this is just the way how things are."
        c "We simply can’t afford to have you in the city, especially with our limited resources."
        Mt "But where will we go?"
        Mt "So many of us can’t go on much further before we start to collapse from exhaustion!"
        Mt "Please! You have to understand!" with Shake ((0, 0, 0, 0), 2, dist=15)
        Mt "If we don’t take refuge here, then we are certain to meet the same fate that our city has!"
        Mt "I beg of you! Please, show some mercy!"
        m "Martin fell to his knees with a desperate expression on his face. Logan, however, pointed his submachine gun directly at Martin."
        Lg "I’ve had more than enough of this."
        Lg "If you don’t leave within the next thirty minutes, then I’ll give you the mercy you desperately want."
        Lg "And don’t you dare think that I’m bluffing here."

        play sound "fx/smg_kol.wav"
        $ renpy.pause (1.0)

        m "Logan gave a few warning shots as if to prove his point. Everybody in the area suddenly had an alarmed expression on their faces."
        Mt serious "I- I’ll be going now."
        Mt "I apologize for bothering you."

        hide martin with dissolve
        $ renpy.pause (2.0)
        play sound "fx/raidersleave_kol.wav"
        $ renpy.pause (2.0)

        m "Martin quickly spread the news around the group. Soon, everybody was back on their motorcycles, with a few running away on foot."
        m "Logan then looked at me with a satisfied expression on his face."
        Lg tsmiling flip "And that takes care of that, then."
        Lg "Good riddance."
        c "Did you really have to be that harsh on them?"
        Lg tserious flip "Look, [player_name]."
        Lg "This world is extremely harsh to anybody still brave enough to live in it."
        Lg "If they have managed to live this long in the desert, then I’m sure they’ll be able to survive for a bit longer."
        c "But they-{w=0.5}{nw}"
        Lg "No buts, [player_name]."
        Lg "They’ll survive."
        Lg "End of discussion."

        stop music fadeout (7.0)

        $ renpy.pause (1.0)
        Lg "Now, here’s our next move."
        Lg "Considering that they were being chased by raiders for basically half their journey, I think that it would be best if we keep guard for the rest of the day."
        Lg "Raiders might suddenly appear at any time looking for their scent."

        play music "mx/detective.ogg" fadein 7.0

        Lg "It’s best if we spend some time making sure we aren’t ambushed by doing some preparations first."
        c "Good idea. I’ll go tell Remy."

        hide logan with dissolve
        $ renpy.pause (1.0)

        scene kolguardtower at Pan ((0, 180), (0, 180), 3.0) with dissolve
        $ renpy.pause (2.0)

        m "I went back to the inside of the city gate to look for Remy, only for him to not be where he previously was."
        m "After a while, I found Remy in a secluded corner near one of the guard towers with an expression of deep thought and mild stress on his face."

        show remy look with dissolve

        c "There you are, Remy!"
        c "Why are you all the way out here?"
        Ry "I wanted to get away as soon as Logan started shooting his gun."
        Ry "Even after Reza, I’m still not used to the loud noises those things can make make. It always seems to make me nervous."
        c "That does make sense. In humans, hearing a gunshot can cause serious hearing problems if you're overexposed to them or aren’t wearing any protective gear."
        c "Still, you should have at least let me know where you went."
        Ry "I know, [player_name]. It’s just that I didn’t want to see the reactions of all the people that we chased away."
        c "You know, I think it’s better if you didn’t see that."

        $ renpy.pause (1.0)
        show remy normal with dissolve
        m "We exchanged a small smile with each other before talking again."
        $ renpy.pause (2.0)

        c "Logan has asked us to patrol the area for a while."
        c "He feels that since the group were being chased by raiders, we might be in some danger for some time."
        Ry look "That is quite smart of him, to be honest."
        Ry "I suppose that we should start as soon as we can, right?"
        c "I guess so."
        Ry "Alright then. I’ll see if anybody is approaching us while I’m flying around."
        c "Got it. I’ll walk around the city walls and keep guard from there. If you see anything strange, then let either me or Logan know as soon as possible."
        Ry "Will do."

        hide remy with dissolve
        $ renpy.pause (1.0)
        play sound "fx/takeoff.ogg"

        m "Remy took to the skies once more, making wide circles around the city."
        m "I went outside, keeping watch for any potential intruders while Logan kept watch on one of the guard towers."

        scene black with fade
        stop music fadeout (2.0)
        $ renpy.pause (3.0)
        play music "mx/amb/night.ogg" fadein 5.0
        $ renpy.pause (1.0)
        scene kolguardtowernight at Pan ((0, 180), (0, 180), 3.0) with fade

        m "A few hours passed before it started to get dark. I decided that it would be best if I went home now, as the chance of any raiders suddenly appearing here is highly unlikely."
        m "When I approached Logan to let him know, I found him deep asleep."
        c "(So much for keeping guard...)"
        m "Seeing that I entered the city, Remy swiftly flew down to my location. I could see that he was extremely tired from the day’s work."

        show remy normal dk with dissolve
        $ renpy.pause (2.0)

        c "Did you see anybody out there, by any chance?"
        Ry "Can’t say I did. You?"
        c "Neither did I."
        Ry look dk "Wait, where’s Logan?"
        c "He fell asleep in one of the guard towers. It doesn’t look like he’ll get up any time soon, either."
        Ry "Shouldn’t we wake him up, then? After all, it would be far safer for him to sleep in his own bed than out in a guard tower."
        c "Yes, it would. However, Logan is the type of person that if you wake up, all heck is going to break loose."
        c "It would probably be safer for us to leave him here."
        Ry "I see..."

        stop music fadeout (2.0)
        $ renpy.pause (2.0)


scene black with fade
$ renpy.pause (2.0)


play music "mx/campfire.ogg" fadein 1.5
scene kolmchousenight at Pan ((300, 80), (0,80), 5.0) with dissolveslow
$ renpy.pause (2.0)

m "Me and Remy arrived back home, tired from everything that had happened today. I started to cook some dinner for us while Remy made himself comfortable on the floor."

if kol_tld_fruitsnackstaken == True:
    m "Suddenly, I remembered that I still had the dried fruit snacks that I took with me from the factory."

    menu:
        "Store the snacks for later.":
            m "I decided that it would be best if I left the snacks for another day, so I stored it in one of the kitchen cupboards."

        "Share the snacks with Remy.":
            m "I took the packet of fruit snacks and opened it, putting it on both our plates alongside our food."

else:
    pass

m "I served the food to Remy, who accepted it with a tired expression on his face."

show remy dk normal with dissolve

Ry "Thank you, [player_name]."
Ry smile dk "I’m sure that this will taste great!"
c "I wouldn’t be so sure about that, Remy. I think everyone can cook better than I can."
Ry normal dk "But at least you {i}can{/i} cook. You’ll be surprised just how many dragons can’t actually cook. They’d rather spend their time hunting or eating out instead."

if kol_tld_fruitsnackstaken == True:
    m "Remy looked suspiciously at the fruit snacks I put on his plate."
    Ry "Forgive me if I sound rude, but what type of food is this? I don’t think that I ever saw something like it before."
    c "Those are dried fruit snacks. I figured that you may be a bit interested in tasting some of the fruit that we have to offer, even if they are only dried ones."
    Ry shy dk "That... suddenly makes a lot more sense now."
    Ry smile dk "Well, I guess that I’m obligated to try them."

    show remy normal dk with dissolve

    m "Remy took a bite out of the fruit snacks. He chewed on it for quite some time before giving his opinion."
    $ renpy.pause (0.8)

    Ry smile dk "These are surprisingly sweet. Few fruits back home could come close to these, even when dried."
    c "Yeah. I noticed that a lot of the fruits that I ate tasted much more sour than the fruits I was used to."
    Ry "Maybe we could taste some more fruit when we have the chance."
    c "For sure."

else:
    pass


m "We proceeded to finish our meals, with Remy finishing far later than I did."
m "I started to prepare for tonight’s rest when Remy interrupted me."
Ry shy dk "I’m sorry for bothering you, but I was wondering if I can sleep with you again. I know that I should sleep on my own, but it’s just really comforting to be with you."

menu:
    "Any time, Remy.":
        $ renpy.pause (0.5)

        Ry "Thank you, [player_name]. This does mean quite a lot, even if it doesn’t look like it."
        c "Don’t worry about it. I’m just happy that you’re happy."

        hide remy with dissolve

        m "I went to my bedroom, changed into my nightwear and climbed into my bed. Remy followed soon after."
        m "I felt Remy slowly hugging me, making sure to not press me too hard."

        $ renpy.pause (1.0)
        show remy sleep dk with dissolve
        $ renpy.pause (2.0)

        menu:
            "Return the hug.":
                $ renpy.pause (0.5)

                m "I put my arms around Remy and hugged him. He smiled and threw his wings over me in a way similar to that of a blanket. As I started to fall asleep, I could feel Remy giving me a small lick on the cheek."
                Ry "Goodnight, [player_name]."
                c "Sleep well, Remy."

                scene black with fade
                stop music fadeout (2.0)
                $ renpy.pause (2.0)

                $ kol_tld_remysleep2 = True


            "Fall asleep.":
                $ renpy.pause (0.5)

                c "Goodnight, Remy."
                Ry "Goodnight, [player_name]."
                Ry "And thank you. Again."
                c "No problem."

                scene black with fade
                stop music fadeout (2.0)
                $ renpy.pause (2.0)

                $ kol_tld_remysleep2 = True



    "I’m sorry, but I don’t think I can tonight.":
        $ renpy.pause (1.5)

        Ry look dk "I see. I suppose that you want to have some time for yourself tonight, especially after what happened today."
        Ry sad dk "I'll just sleep on the couch again."
        Ry "I'm sorry to bother you by asking such a question."
        Ry "Goodnight, [player_name]."

        hide remy with dissolve

        m "Before saying anything else, Remy went to the couch and curled up into a ball, falling fast asleep."
        m "As usual, I changed into my nightwear and climbed into my bed, waiting for sleep to take me once more."

        scene black with fade
        stop music fadeout (2.0)
        $ renpy.pause (2.0)


jump tld_day4
