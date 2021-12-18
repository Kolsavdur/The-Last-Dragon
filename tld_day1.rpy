#Oh? It seems that we have a curious onlooker here in my code...
#Well, of course I don't mind. It's just that I'm a bit embarrassed to show my awful programming skills.
#In any case, maybe you could find some secrets here?
#Yeah, I don't really know what to say here...
#Still, I do hope you enjoy The Last Dragon as much as I did making it!
#Now, before you say anything:
#-Yes, I know the writing is... questionable.
#-Yes, the backgrounds don't fit into the game's art style.
#-And yes, I was too lazy to create my own human sprites, so I just took the two sprites in that one April Fool's joke.
#In the end, does it really matter what I did to create TLD if you enjoyed it regardless?
#...
#Well, enough ramblinng for now. Your here to look at some code like the absolute nerd you are, correct?
#As requested, down below is the code.
#I just figured that anybody actually interested to look at the code should at least have some acknowledgement first.
#Regardless, welcome to my Remy fanfiction: Mod Edition!
#
#With love,
#Kolsavdür


label tld_day1:

$ save_name = (_("TLD - Day 1"))

stop music fadeout (2.0)
$ renpy.pause (3.0)
play music "mx/judgement.ogg" fadein 0.5

c "I need to stay and protect Remy. He can’t be left alone in a world as desolate as this. He won’t survive!"
As "Do you think I’ll let you do what you want when everything has already been destroyed by the comet? If you refuse, nothing will be changed and the dragons will be gone forever."
Ry "Please, [player_name]. I’ll be fine. You need to go and save them all."
c "Remy, I’m not prepared to go through the portal and leave you behind. It would be extremely cruel of me to ruin any sense of hope you may have after everything you went through."

show remy angry flip with dissolve

Ry "This isn’t just about me or what I want! If I have to live in even greater despair so that there could be a chance for you to save everyone, then I’ll gladly suffer knowing that my pain has meaning." with Shake ((0, 0, 0, 0), 3, dist=20)
As "He has a point. It would be wise of you to listen. Besides, you’ll forget most of the things you do now when you step through the portal."
c "(There just has to be another way...)"
m "Suddenly, I remembered Lorem and Ipsum’s theories on time travel and different timelines. Maybe there was still a glimmer of hope left."
c "Wait. What if only one of us traveled back in time instead of us both? Wouldn’t that simply cause another timeline to be created?"
As "..."
As "Are you suggesting that I should be the only one to go through the portal?"
c "Yes. If what I believe about time travel seems to be correct, then you should be able to work with the version of me that appears in the newly created timeline."
c "Remember, if both of us went, then that would most likely drain the last reserves of energy left for Remy to use."
c "Thousands upon thousands have gone from the city through the portal. Add that to the energy already used by me while I was put in a coma by the other humans, and you have enough energy to activate the portal one more time at best."
Ry shy flip "..."
c "As long as simply one of us goes through, we can try again while Remy can survive in this harsh world."
Ry "This is starting to get confusing…"
As "You really do not wish to listen, do you?"

$ renpy.pause (2.0)

As "*sigh*"
As "Very well. I’ll step through the portal and let you have your way. Only remember that you have doomed yourself and your companion in this timeline."

stop music fadeout (2.0)
play sound "fx/tel.wav"
$ renpy.pause (5.5)
hide izumi with dissolveslow
hide remy with dissolve

m "The Administrator activated the portal and stepped through it. After a flash of blinding light she disappeared, presumably back to the day of my arrival."
m "I looked at Remy. He seemed to have a confused yet grateful expression on his face."

stop sound fadeout (2.0)
play music "mx/anna4.ogg" fadein 1.0 #Wait, is this even a fitting track for the scene? idk...

show remy normal with dissolve

Ry "I don’t understand…"
c "What’s wrong, Remy?"
Ry sad "Why would you do all of this? Why do you want to throw a better life away for me of all people? "

menu:
    "I care about you a lot.":
        $ renpy.pause (0.5)
        c "Because I care too much about you to simply leave you alone. As far as I know, I’m the only one left here."
        c "I couldn’t possibly abandon you just so that you can figure everything out on your own."
        Ry "I see."

    "I don't want anybody to tell me what to do.":
        $ renpy.pause (0.5)
        c "I don’t want anybody forcing me to do something that I don’t want. After all, why should I go when I can stay with you?"
        Ry "That is a dangerous way of thinking, especially in a scenario like this."
        Ry "I’m just confused as to why you would refuse another chance to stop the comet, that’s all."

    "No reason in particular.":
        $ renpy.pause (0.5)
        Ry "..."
        Ry "And here I hoped that you would still have a bit of sense in you."
        c "But I do. You’ll just need to wait and see."
        Ry "I hope you're right, [player_name]."

Ry normal "I guess what’s done is done, then. What should we do now?"
c "Now, I guess I have to introduce you to what’s left of my world. Normally, this is the part where I would show you around the city, but I assume that you must be tired after flying for so long."
Ry "It’s no problem. I could have gone for much longer if necessary. We dragons have…"
Ry sad "...had a lot of energy compared to what I’ve seen in humans."
Ry normal "Still, I think that a bit of rest would be beneficial."
c "I could always show you my home, or what’s left of it. Much of it has now degraded, especially since I originally went through the portal."
c "There’s only so much I can do with such a limited amount of resources left, after all."
Ry shy "..."
Ry "There is something really important you need to know, [player_name]."
c "You can tell me anything, Remy."
Ry "There is a chance that we can rebuild this city."
c "How? There weren’t any generators to keep the city from falling apart before, and there aren’t any left to keep the both of us afloat right now."
c "Besides, the portal generator can only do so much before we run into some problems."
Ry "I brought three generators with me through the portal, as well as the PDA you gave me."
Ry smile "I figured that since your energy would be depleted, I brought some generators so that we can use one to power the portal enough for you to come back."
Ry "I brought the other two just in case you needed them after you awoke from your coma."
Ry sad "That was before everything I heard about the comet, though."

menu:
    "Where did you even get these generators?":
        $ renpy.pause (0.5)
        Ry normal "I took the generator I had in my house, as well as the one in your apartment."
        Ry "The third one was given to me by the council so that I can try and find you."
        Ry "As for the PDA, the council decided that I should use it to try as a guide so that I could find you faster."
        c "Wouldn’t the generator you took from my apartment count as stealing from the council?"
        Ry sad "Yes, it would. Not that it matters now, anyway."

    "You're a hero, Remy!":
        $ renpy.pause (0.5)
        c "Remy, you just gave the two of us actual hope for survival. You’re a hero!"
        Ry shy "Please, [player_name]. It’s the least I could do, especially after everything you did for me. It seemed only fair that I should help you in one way or another."
        Ry "You always went out of your way to help me, so I felt that I needed to do the same."
        Ry "Besides, I only did what seemed like the morally correct option at the time."

    "How did you get the generators here?":
        $ renpy.pause (0.5)
        c "How did you even bring the generators here? Surely there must have been a guard or two who might have spotted you carrying them."
        c "Besides, aren’t the generators too big to easily sneak around with?"
        Ry normal "You’re right on that first account. There were a lot of guards around the portal, but it seemed that they tended to be more in the underground building than around the portal itself."
        Ry smile "I went through the portal at a time where I knew that there wouldn’t be many guards. Those that were already there knew that I was coming to find you."
        Ry normal "As for the generators, the ones I brought were the newer models designed to be extremely portable. I simply snuck them under my wings when I entered."

c "What about that part you mentioned to fix the portal?"
Ry normal "Well, the council gave it to me after the humans described a certain problem that caused it to work in a rather strange way."
Ry "All I did was install that part into the controls of the portal here and tried to activate it."
c "And the generators? Where are they now?"
Ry smile "They should be safe in one of the buildings nearby. I’ll go get them for you."

hide remy with dissolve
play sound "fx/takeoff.ogg"

m "Remy flew off into the distance towards one of the buildings along the outskirts of the city."
m "A while later, he returned with what seemed to be a large basket in his mouth."

stop sound
play sound "fx/landing.ogg"
$ renpy.pause (1.0)

show remy normal with dissolve

Ry "Here are the generators and your PDA. I hope you don’t mind that I put them in this basket I found somewhere."
m "I picked the generators up from the basket and studied them. They seemed to be slightly larger than the ones offered in the trade, but far lighter. "
m "Now it made sense how Remy could carry these through the portal with him undetected. A sense of hope now washed over me."
c 'You actually managed to bring them with you...'
c "We might stand a chance at rebuilding this city now."
Ry smile "I’m glad that I could have helped you. Oh, and don’t worry; I took extra care at not dropping them, so they should all still be fine. "

scene kolcityevening at Pan((0,0),(0,0),0.0) with fade
$ renpy.pause (1.0)

m "We continued to talk for hours, catching up on what happened while I was in my coma."
m "Eventually, we realised just how long we talked for."

show remy normal with dissolve


c "Well, looks like the time caught us off guard. Let’s go home before it gets too late."
Ry "Lead the way."

scene black with fade
$ renpy.pause (1.0)
stop music fadeout (2.0)
scene kolmchouseevening at Pan ((300, 80), (0,80), 5.0) with dissolveslow

# Time to copy Remy 2!

play music "mx/soul.ogg" fadein 1.0

m "We entered my home. Upon looking around, I noticed a new crack that had formed since yesterday."
c "(I should really try and do some repairs to this place when I get the time.)"
m "I asked Remy to sit down on an old couch I had that, unsurprisingly, wasn’t really suited for dragons. Remy didn’t seem to mind as he made himself comfortable."
c "(At least he actually fits on furniture explicitly designed for humans only.)"

show remy normal with dissolve

c "Welcome to my home! Sorry that there aren’t any lights or things not falling apart."
Ry "Don’t worry about it. I do understand the situation humanity was in, after all."
c "Would you like something to eat, Remy? I imagine that you must be starving by now."
Ry "That would be really kind of you, [player_name]. What do you have available?"
c "Not much, I’m afraid. I have some canned food, as well as some pieces of dried meat. It seems that the humans only left me with food that has a long shelf life."
Ry smile "Would some of it be pieces of dried steak then, by any chance?"

menu:
    "I can't remember. Let me check.":
        $ renpy.pause (0.5)
        Ry normal "I see. In that case, I'll wait for you then."

        hide remy with dissolve

        m "I looked around the house and saw two sealed packets of dried steak chunks conveniently stored underneath the counter in an old cooler. "
        m "I started to wonder if these were still edible, but then I saw that the expiration date is still a few months away."
        c "(I should see if I could find a better way to preserve food for longer.)"
        c "(Just more work for later, I guess.)"
        c "Looks like there are two sealed packets of dried steak chunks left for us. Is that alright with you?"
        Ry "That would suffice, thank you."
        c "Well, no need to thank me if I haven’t even started cooking yet."
        m "I could hear Remy chuckle a bit after I said that."

    "One steak-filled dinner coming up!":
        $ renpy.pause (0.5)
        Ry normal "Interesting. I wonder how the taste would compare to the taste back home."
        c "Surprisingly similar, actually. I think that you’ll enjoy this."
        Ry smile "Then I can’t wait to taste your cooking!"


    "I do, but not auroch steaks.":
        $ renpy.pause (0.5)
        Ry "I was wondering if you would notice that. I didn’t think that you would remember."
        c "How could I forget our dinner? With cooking as good as yours, it’s really hard to forget."
        Ry shy "You flatter me too much, [player_name]. I don’t think I’ll ever understand that."
        c "You deserve every bit of it, Remy. You know how much I care about you."
        Ry "Thank you."
        Ry smile "Now, are we going to just sit here and talk or are we going to eat?"
        c "Sorry. Please wait a moment while I cook."

hide remy with dissolve

play sound "fx/veggies.ogg"

m "I prepared the meat by cutting it into more manageable pieces, as well as adding some spices. I then started to cook by emptying a can of mixed vegetables into a pot and letting it boil while the chunks were searing."

stop sound fadeout (1.0)
play sound "fx/fry.ogg"

m "An intense smell filled the room that reminded me a lot of the steakhouses we used to have before the solar flare."
m "Soon, the food was ready to be served."

stop sound fadeout (1.0)
show remy normal with dissolve

c "Here you go, Remy. I hope that this is enough for you."
Ry smile "You would be correct on that part. Looks like we can guess each other's portions fairly well then."
c "Regardless, I do hope that you like it. My cooking isn’t really the best."
Ry "Well, you are the best human cook I know, after all."
c "Thanks?"
m "I started to eat the food I had prepared, and while it didn’t taste nearly as well as Remy’s cooking, it definitely tasted better than I thought it would."
c "So, how do you like your first taste of human food?"
Ry normal "It’s surprisingly good, actually. It tastes shockingly similar to the things we had back home."
c "See, I told you the taste would be similar. Sadly, this is as good as it gets around here."
c "However, maybe we could change that. With the generators, we could restart food production if we somehow get the facilities up and running again."
Ry look "Don’t you think that we should maybe save those ideas for tomorrow? I need some time to wrap my head around everything that has happened today."
Ry sad "I still haven’t accepted the fact that everything I knew is now gone, and at this point, I don’t think I ever will."

menu:
    "You're right. We should leave this for tomorrow.":

        $ renpy.pause (2.0)
        show kolmchousenight behind remy at Pan((0,80),(0,80),5.0) with dissolve
        show remy sad dk with dissolve
        $ renpy.pause (2.0)

        Ry normal dk "I think it would be better. It is getting really late now, and I would still like to get a good night’s rest."
        Ry shy dk "I know this might sound weird, but do you mind if I sleep with you tonight? I don’t really feel comfortable in your world yet. Everything still feels so… strange."

        menu:
            "[[Accept]":
                c "Any time, Remy. I understand that you might feel a bit unsafe here. Letting you sleep with me is the least I could do."
                c "We’ll just need to make some space if we actually plan to fit on the bed."
                Ry dk "Thank you, [player_name]. This means a lot to me."
                Ry smile dk "Lucky for you, I don’t really snore, so you shouldn’t worry about that."
                c "Like I would ever mind."

                hide remy with dissolve

                m "We went to my bedroom, where I changed into my nightwear and climbed into my bed. Remy tried to fit in, and after much struggle, we finally settled. His scales felt strangely soft as he snuggled next to me." #SNUGGLES!

                show remy sleep dk with dissolve

                c "Good night, Remy."
                Ry "Good night, [player_name]."

                scene black with fade
                stop music fadeout (2.0)
                $ renpy.pause (2.0)

                $ kol_tld_remysleep1 = True

            "[[Decline]": # :(
                Ry sad dk "I understand. I really don’t know what came over me to ask something like that. I suppose I’ll just have to sleep here on the couch."
                Ry normal dk "Good night, [player_name]. I hope you sleep well tonight."
                c "Good night, Remy."

                hide remy with dissolve

                m "I walked to my room where I changed into my nightwear and climbed in my bed."
                c "(Ah, the wonders of sleeping in your own bed for once.)"
                m "I closed my eyes, waiting to be transported into a world of dreams."

                scene black with fade
                stop music fadeout (2.0)
                $ renpy.pause (2.0)

    "At least we're still here together.":


        Ry normal "I suppose it’s all that we have left now."
        Ry look "Truth be told, I don’t know what I would have done if you weren’t here with me in this strangely familiar world, and for that I’m really grateful, even if I don’t agree with your decision to stay here."
        c "Well, regardless of what I decided, any struggles we will face are struggles we will face together, no matter what."
        c "Remember, I’ll always be there for you, even if you feel otherwise."
        Ry shy "..."
        Ry "As will I."
        Ry normal "Now, should I help you clean the dishes, or are you going to take care of it?"
        c "I’ll do the dishes. I don’t think that the sink is big enough for dragons of your size to be able to use effectively."
        Ry "You do have a point there."

        $ renpy.pause (2.0)
        show kolmchousenight behind remy at Pan((0,80),(0,80),5.0) with dissolve
        hide remy with dissolve
        $ renpy.pause (2.0)

        m "I took away the dishes and cleaned them while I got lost in thought. Upon finishing them, I saw that Remy had fallen asleep on the couch."

        menu:
            "[[Join him.]":
                m "I decided to join Remy and lay down next to him in the little space available to me. I had no trouble falling asleep with Remy softly squeezing me against the back of the couch."

                scene black with fade
                stop music fadeout (2.0)
                $ renpy.pause (2.0)

                $ kol_tld_remysleep1 = True

            "[[Go to your room.]":
                m "Not wanting to disturb Remy, I quietly went to my room and changed into my nightwear. As I started to settle down, a feeling of comfort washed over me as I remembered how good it felt to sleep in my own bed."

                scene black with fade
                stop music fadeout (2.0)
                $ renpy.pause (2.0)

    "Maybe some dessert would help?":

        Ry "I’m not in the mood for something sweet right now, sorry."
        Ry normal "It does make me a bit curious, though: What kind of desserts do humans have? I didn’t have too much time to study your PDA yet, so I might as well ask you now."
        c "We share a lot of deserts. Of course, there are the obvious ones like cake or pie, but then there are some more obscure ones like éclairs or strudels."
        Ry "I think I know what an éclair is, but what’s a strudel?"
        c "In short, a strudel is a type of pastry with a sweet filling. Fruits like apples are most commonly used."
        Ry smile "Interesting. Maybe you should make me some one day."
        c "I would if I could, but to make a dessert like that is a bit above my current skill level."
        c "Back before the flare hit, we even had specialised chefs to make desserts, but that has fallen out of favour. Now, it’s only about eating what you can make and not what you want to make."
        Ry normal "I see."

        $ renpy.pause (2.0)
        show kolmchousenight behind remy at Pan((0,80),(0,80),5.0) with dissolve
        show remy normal dk with dissolve
        $ renpy.pause (2.0)

        Ry shy dk "..."
        Ry "I just noticed that it's gotten really late now. This might sound a bit awkward, but would you mind if I sleep with you tonight? I don’t really feel safe in this world yet. Everything just feels so… unusual."

        menu:
            "[[Accept]":
                c "Any time, Remy. I understand that you might feel a bit unsafe here. Letting you sleep with me is the least I could do."
                c "We’ll just need to make some space if we actually plan to fit on the bed."
                Ry "Thank you, [player_name]. This means a lot to me."
                Ry smile dk "Lucky for you, I don’t really snore, so you shouldn’t worry about that."
                c "Like I would ever mind."

                hide remy with dissolve

                m "We went to my bedroom, where I changed into my nightwear and climbed into my bed. Remy tried to fit in, and after much struggle, we finally settled. His scales felt strangely soft as he snuggled next to me."
                c "Good night, Remy."
                Ry sleep dk "Good night, [player_name]."

                scene black with fade
                stop music fadeout (2.0)
                $ renpy.pause (2.0)

                $ kol_tld_remysleep1 = True

            "[[Decline]":
                Ry sad dk "I understand. I really don’t know what came over me to ask something like that. I suppose I’ll just have to sleep here on the couch."
                Ry normal dk "Good night, [player_name]. I hope you sleep well tonight."
                c "Good night, Remy."

                hide remy with dissolve

                m "I walked to my room where I changed into my nightwear and climbed in my bed."
                c "(Ah, the wonders of sleeping in your own bed for once.)"
                m "I closed my eyes, waiting to be transported into a world of dreams."

                scene black with fade
                stop music fadeout (2.0)
                $ renpy.pause (2.0)


jump tld_day2
