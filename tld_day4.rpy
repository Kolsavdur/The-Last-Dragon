label tld_day4:

$ save_name = (_("TLD - Day 4"))

$ renpy.pause (3.0)
scene kolmchouseday at Pan ((300, 80), (0,80), 5.0) with dissolveslow

$ renpy.pause (2.0)
play music "mx/couch_kol.ogg" fadein 1.5 #Vibin' - The Music Track

m "I woke up slowly, trying to adjust to the shining rays of sunlight that had a tendency to shine directly in my eyes in the morning. I proceeded to get myself ready for the day by going to the kitchen."
m "Much to my surprise, I saw that Logan was already at my house cooking some breakfast. Remy also seemed to be awake, but still looked quite tired from yesterday’s events."

show logan normal at Position(xpos = 0.75) with dissolve
show remy normal flip at left with dissolve

Lg "And you’re awake. Good. I was wondering if you’d fallen into another coma with how late you were sleeping."
c "But it’s only eight in the morning..."
Lg "Thus proving my point."
Lg "Here. I figured that you may want this."
m "He handed me a plate of food, as well as a pepper shaker on the side."
c "Thanks."
Lg "Anything to make you get up faster."
Lg smiling "Heck, you took so long that Remy finished eating before you even woke up."
Ry shy flip "Well, you {i}did{/i} wake me up, Logan. I don’t think that I really had any say in the matter."
Ry look flip "It would have been nice if I could have slept for a while longer, though..."
Lg normal "Looks like we have two lazy slackers instead of one."
Lg smiling "You two really are a match made in heaven."

menu:
    "I wouldn’t go far as to say that we’re slackers.":
        $ renpy.pause (0.5)
        Lg serious "But it’s the truth."
        Lg "We can’t afford to do nothing if we want to survive."
        c "Says the person who’s favourite hobby is sleep deprivation." #One of my most favourite non-Remy lines
        Lg normal "Touché, [player_name]."
        Lg serious "Stil, work has to be done, and you know that."


    "Well, I guess you’re right.":
        $ renpy.pause (0.5)
        Lg "See, I’m almost always correct when making such deductions."
        Lg "I’ll just have to add one to my counter later."
        Lg thinking "Now that I think about it, you two are actually pretty similar in personality."
        Lg normal "You two would fit well with each other."


    "No need to call us out like that!":
        $ renpy.pause (0.5)
        Lg serious "Wait..."
        Lg "Were you referring to the slacking part or the matchmaking part?"
        c "I’ll let you figure that out on your own."
        $ renpy.pause (2.0)
        Lg "..."


$ renpy.pause (1.5)

Lg normal "Anyways, the plan is simple for today."

if kol_tld_martinaccepted == True:

    jump tld_day4good

else:

    jump tld_day4bad



label tld_day4end:


$ renpy.pause (4.0)
scene kolmchousestorm at Pan ((300, 80), (0,80), 5.0) with dissolveslow
$ renpy.pause (1.5)

m "Me and Remy hurried back home. Luckily for us, the first raindrops started to fall just as we closed the door."

play music "fx/rainloop_kol.ogg" fadein 1.0

m "Soon, we could hear the rain starting to pour down."

show remy normal with dissolve
$ renpy.pause (1.5)

Ry smile "Looks like we made it just in time."
Ry shy "I’m pretty sure that you wouldn’t appreciate walking around in soggy clothes, especially with this weather. You’d probably even catch a cold out there."
c "Yeah. Wet clothes aren’t exactly the most comfortable, as you can imagine."
Ry normal "That’s understandable. Should I make something to eat, or are you not hungry?"
c "I think that I’ll have something later. Strangely enough, I think that today’s work made me lose my appetite."
Ry "Alright then."

show remy shy with dissolve

m "Remy looked at me with a sad smile, as if he wanted to say something."

$ renpy.pause (1.5)

Ry "..."

$ renpy.pause (0.5)

Ry "[player_name], is there any chance that I could talk to you now? I have a lot on my mind, and I don’t think that I’m able to keep it to myself anymore."

menu:
    "Of course you can.":
    #Time to copy Remy3! Now with extra depression!
    #Says the person who can't even write depression...
    #Damn, just realised that this entire section is cringe
    #Won't change it though. Too lazy.
    #Wait, is this entire mod just in writer purgatory then?
    #Hmmmmm...
        $ renpy.pause (2.5)

        c "Any time, Remy. After all, I’m always here to hear you out and to help you, regardless of what happens to us."
        Ry sad "Thank you, [player_name]."
        Ry "I feel that what I’m about to say will probably change the way in which you think of me."
        c "Nothing will be able to change the way in which I feel about you, Remy."
        Ry "I really don’t think so."
        Ry "I realised something a while ago that has been crushing me ever since I came to that conclusion."
        c "What is it?"

        stop music fadeout (1.5)
        $ renpy.pause (2.0)

        Ry "I-{w=1.0}{nw}"

        show remy cry with dissolve
        play music "mx/gravity_kol.ogg" fadein 1.0

        Ry "I am the reason why my world had been destroyed by the comet."

        menu:
            "How so?":
                pass


            "No, you aren’t.":
                $ renpy.pause (0.5)

                $ kol_tld_remytherapycounter += 1

                Ry "I am, [player_name]."
                Ry " And nothing you could say will make me feel otherwise."


            "Well, now that you mention it...":
                $ renpy.pause (0.5)

                $ kol_tld_remytherapycounter -= 1

                Ry "See, I’m glad you can understand."
                Ry "This was all my fault. {w}Just like how everything always was."



        Ry "By bringing the generators and the PDA here to you, I took away valuable power that could have been used to redirect the comet."
        Ry "If it wasn’t for my own selfish interests, then everybody would still be alive."

        menu:
            "It didn’t matter if you took those generators.":
                $ renpy.pause (0.5)

                $ kol_tld_remytherapycounter += 1

                Ry "Then please, explain that to me."
                c "The rest of the humans that came to your world wouldn’t have let the dragons use the huge generator in the underground facility to redirect the comet."
                c "They were far too greedy for their own good."
                Ry "So us trying to make peace with them never even mattered in the first place..."


            "You did take them to help me, didn’t you?":
                $ renpy.pause (0.5)

                Ry "But by doing so I left everyone to die a horrible death."
                c "You did what you could, though."
                Ry "But in the end, it wasn’t enough."
                Ry "It never was."


            "I do agree with you.":
                $ renpy.pause (0.5)

                $ kol_tld_remytherapycounter -= 1

                Ry "See? If I never took the generators to help you, and instead tried to be a better ambassador to the humans, this never would have happened."
                Ry "But no, this pathetic, selfish dragon just {i}had{/i} to ruin it all for everybody."
                Ry "And just look where that got us."


        $ renpy.pause (0.5)
        Ry lookcry "I can’t even begin to imagine all the fear and pain everybody felt in those last few moments before the comet hit."
        Ry "Everybody hoped for me to return with you to try and negotiate with the humans."
        Ry "All those who were disappointed in me for not returning; thinking that I abandoned them all..."
        Ry cry "I can hear them cursing my name for letting everybody down."
        c "But what about those that maybe still cared about you in some way? Surely not everybody would have been disappointed in you."
        Ry "That’s the part I’ve been wanting to avoid confronting the most."
        Ry "It’s often those that once cared about you in some way that you end up hurting the most."
        Ry "Not friends. {w}Not enemies. {w}Old, forgotten acquaintances."

        menu:
            "They probably understood the situation.":
                $ renpy.pause (0.5)

                $ kol_tld_remytherapycounter += 1

                c "Well, they probably understood how desperate the mission was."
                c "I don’t think that they fully believed that you could find me and bring me back to negotiate with the other humans."
                c "And if they did, chances are, they also believed that I wouldn’t be able to convince the humans to sign a peace treaty."
                c "Not after what happened with Reza."

                show remy angrycry with dissolve

                Ry "Don’t you even dare to try and tell me that!"  with Shake ((0, 0, 0, 0), 2.5, dist=15)

                show remy shycry with dissolvemed

                Ry "I was there when they all wished me good luck."
                Ry "They entrusted all their hopes and dreams onto me."
                Ry cry "And I failed them all."


            "And you let them all down.":
                $ renpy.pause (0.5)

                $ kol_tld_remytherapycounter -= 1

                Ry "That I did, [player_name]."
                Ry cry "That I did."


            "Maybe their deaths weren’t as bad as you think.":
                $ renpy.pause (0.5)

                Ry "Are we lying to ourselves now?"
                Ry "We both know that everybody died a horrendous death because of my neglect."
                Ry "To burn alive as everyone and everything around you is reduced to ashes..."

                $ renpy.pause (1.5)

                Ry cry "I can’t think of any worse fate."


        $ renpy.pause (1.5)

        Ry "In all truth, I don’t even know why I’m here."
        Ry "Why did I escape the fate that everybody else shared?"
        Ry "Nobody deserved it. Not even Emera."
        c "It’s because you volunteered to try and make things right for everybody else."
        Ry "At far too high of a cost."

        $ renpy.pause (0.5)

        Ry shycry "..."
        Ry "Now, I’m all that’s left of my world."
        Ry "Everything I knew has been reduced to a smoldering crater."

        $ renpy.pause (0.5)

        Ry cry "..."
        Ry "Nothing even mattered in the first place, did it?"

        menu:
            "Don’t tell that to yourself.":
                $ renpy.pause (0.5)

                c "Please, don’t say such things. You know that it’s not true."
                Ry "..."
                Ry lookcry "If everything I ever did; everything I ever knew..."
                Ry "Ended up burning to the ground..."

                $ renpy.pause (1.5)

                Ry cry "What was the point of even trying?"
                c "The point is to live and thrive. We need to experience new things and spend time with the ones we love."
                c "That’s why we need to try."
                Ry "I guess."


            "You can always make up for it.":
                $ renpy.pause (0.5)

                $ kol_tld_remytherapycounter -= 1

                Ry "How?"
                c "By helping restore the city to its former glory."
                c "Think about it like this: I could help you make up for your mistakes if we could spend the time and energy giving hope to a place where all hope was originally lost."
                Ry lookcry "Well, I suppose that’s true."


            "We all have to create our own meaning.":
                $ renpy.pause (0.5)

                $ kol_tld_remytherapycounter += 1

                c "It doesn’t matter whether something meant anything or not. We all need to find something that gives us meaning."
                c "That’s all how we could go on without feeling any purpose in life."
                Ry "Like spending time with someone you care about?"
                c "Among other things."
                Ry lookcry "I see."



        $ renpy.pause (0.5)
        Ry cry "Still, how could I ever live with myself now?"
        Ry "Since the beginning, all I ever did was get in everybody’s way."
        Ry "It happened with Emera. It happened with the other humans that came to my world."
        Ry "And it’s happening with you."

        menu:
            "Just like it always had.":
                $ renpy.pause (0.5)

                $ kol_tld_remytherapycounter -= 1

                if kol_tld_martinaccepted == True:

                    Ry "And, chances are, it will still continue with Logan and Martin."

                else:

                    Ry "And, chances are, it will still continue with Logan as well."


                Ry "That’s all I ever was and will ever be."
                Ry "A burden."


            "You’re not dragging me down.":
                $ renpy.pause (0.5)

                Ry "But I am."
                Ry "You could have gone on to do so many great things if it weren’t for this horrible excuse of a partner."
                Ry "Maybe even..."

                $ renpy.pause (1.0)

                Ry "You could have succeeded where I failed and saved everybody."


            "And yet I'm still here with you.":
                $ renpy.pause (0.5)

                $ kol_tld_remytherapycounter += 1

                Ry "But what does it matter? Why would you voluntarily want me dragging you down?"
                c "Because you still mean so much to me."

                if kol_tld_martinaccepted == True:

                    c "And I think that it’s a similar case with Logan and Martin as well."

                else:

                    c "And I think that it’s a similar case with Logan as well."


                c "You’re doing so many great things helping everybody, even if you don’t realise it."
                Ry "But it’s not going to bring everybody back."
                c "No, it won’t."
                c "But that still doesn’t make you a burden, no matter what the situation might be like."
                Ry lookcry "Thanks, [player_name]."


        $ renpy.pause (0.5)

        Ry lookcry "..."
        Ry cry "I just realised something new from our conversation."
        c "What is it, Remy?"

        if kol_tld_martinaccepted == True:

            Ry "With Martin and his group here, I realised that there are so many people here that depend on my help."
            Ry shycry "I can see how everybody helps each other, trying to survive in this hostile world."
            Ry cry "Then there’s me, who will only disappoint yet another group of people that need my help."
            Ry lookcry "Sure, it’s great to have a second chance now, but..."
            Ry cry "What if I end up hurting even more people than I already have?"

            menu:
                "I doubt that they’ll take any offence.":

                    c "I don’t think that it will be quite easy to hurt them, especially after all they went through."
                    c "Besides, I think that the chances are greater that they’ll be offended by Logan far more than everything that you could say."
                    Ry "But so many of them are afraid of me and are always making an effort to stay out of my way."
                    Ry "I’ll just scare them away and ruin the potential help this city may receive."
                    c "How?"
                    Ry "..."
                    Ry "I don’t think I want to explain."


                "Then I’ll be here to help you.":

                    $ kol_tld_remytherapycounter += 1

                    c "Remember that I’m an ambassador, Remy. If something were to go seriously wrong, then I’ll be here to help you."
                    Ry "Thus wasting your precious time that you could have spent doing something more helpful."
                    Ry "I truly am a waste of everybody’s energy."
                    c "Not if the helpful thing {i}is{/i} to try and resolve any conflict between you and the rest of Martin’s group."
                    Ry lookcry "I see."


                "You’d probably get casted out.":

                    $ kol_tld_remytherapycounter -= 1

                    c "There would probably be a vote to cast you out of the city if that were to happen."
                    c "Some would probably see you as a strain on our resources here."
                    Ry "Just like your criminals."
                    Ry "How fitting of me."



        else:

            Ry "Remember those people we recently chased away?"
            c "I do. What about them?"
            Ry "..."
            Ry "They’re probably dead now, and it’s all my fault."
            Ry "I could have saved them, [player_name], but instead I sent them all to their graves."
            Ry "Even after everything I realised about myself, I still continue to make the same mistakes, with others having to pay the price for it."

            menu:
                "How do you know they’re all dead?":
                    $ renpy.pause (0.5)

                    Ry "I can’t say for sure. Even if they are still alive, it won’t be long before they all die."
                    Ry lookcry "And to throw away their hope after all they went through..."
                    Ry "Only scum like me could do such a thing."
                    c "You do know that it isn’t your fault, right?"
                    Ry cry "But it is. {w}It always is."


                "At this rate you’ll cause the extinction of two races.":
                    $ renpy.pause (0.5)

                    $ kol_tld_remytherapycounter -= 1

                    Ry "Then we’ll both be the last of our kind."
                    Ry shycry "Strangely, I wouldn’t feel as alone in such a scenario."
                    Ry lookcry "Not that it would matter in the end."


                "There is still hope for them.":
                    $ renpy.pause (0.5)

                    $ kol_tld_remytherapycounter += 1

                    Ry "No. There can’t be. You said yourself that there weren’t any cities left in the area."
                    c "But they could always join one of the mobile groups."
                    Ry lookcry "And potentially find the raiders they’ve been trying to run away from?"
                    Ry "It just wouldn’t end well."
                    c "But we can always hope."
                    Ry "I guess that’s all we can do, now."
                    Ry "Even if it doesn’t matter in the end."



        Ry shycry "Although, maybe there is still a way to fix my mistakes."
        Ry "Maybe there is even a chance that I could see-{w=1.0}{nw}"

        $ renpy.pause (1.0)

        Ry cry "..."
        c "What are you talking about Remy?"
        c "Wait. {w}Don’t tell me-{w=0.5}{nw}"
        Ry "The portal."
        Ry shycry "That strange person did mention that it could be used for time travel, correct?"
        Ry "With it, I could go back in time and try harder to prevent the comet from hitting."

        menu:
            "It isn’t worth the risk.":

                c "Don’t make such a rash decision. We don’t know what the consequences would be if you were to go back in time."
                c "The risk is far too great."
                Ry "I need to at least {i}try{/i}, though."
                c "I know, Remy. The thing is, we don’t know what would happen if you were to arrive at the other side."
                c "If I had to guess, meeting yourself could probably cause a time paradox if you’re not careful enough."
                c "Maybe something even worse entirely."
                Ry cry "So even that is a lost hope, then."


            "And leave everybody here on their own?":
                $ renpy.pause (1.0)

                $ kol_tld_remytherapycounter -= 1

                Ry cry "..."
                Ry "I’m sorry..."


            "Running away won’t fix your problems.":

                $ kol_tld_remytherapycounter += 1

                c "Going through the portal won’t fix your problems here, Remy."
                c "Remember, if what I understand about time travel is correct, then an entire new timeline will be created."
                c "Sure, you’d be able to prevent the comet from hitting, but only in that specific timeline."
                c "This one will remain unaffected."
                c "You wouldn’t escape from your problems. In fact, the chances are much higher that you’d only create more."

                $ renpy.pause (1.0)

                Ry cry "..."
                Ry "I understand."



        $ renpy.pause (2.0)

        Ry lookcry "Can I ask you an unusual question, [player_name]?"
        c "Go right ahead."
        Ry "What would you do if I suddenly disappeared?"

        menu:
            "I would probably go and look for you.":
                $ renpy.pause (0.5)

                $ kol_tld_remytherapycounter += 1

                Ry "I see."


            "I don’t know.":
                $ renpy.pause (0.5)

                Ry "I see..."


            "I’d celebrate.":
                $ renpy.pause (1.0)

                $ kol_tld_remytherapycounter += 1

                Ry "..."


        c "Why would you ask such a question, if I may ask?"
        Ry cry "I can’t tell you, [player_name]. Not now."
        c "Alright then."

        $ renpy.pause (3.0)



        if kol_tld_remytherapycounter > 1:

            Ry shycry "Still, there’s one thing left to tell you now."
            Ry "Thank you, [player_name]."
            c "There’s no need to thank me, Remy. I’m always available to help you."
            Ry "I know. It just feels so weird to know that somebody cares about me enough to listen to what I have to say."
            Ry "I haven’t had somebody like that since..."
            Ry cry "..."
            c "Amelia?"
            Ry "Yes. Amelia."
            c "Don’t worry, Remy. It’s alright. I’m here for you. {w}Always."
            Ry shycry "I truly don’t deserve any kindness from you, [player_name]."
            Ry cry "Trash like me shouldn’t receive even emotionless wishes."
            c "You aren’t trash, Remy."
            c "You’re the most valuable person I know. Don’t you dare forget that."
            Ry shycry "I don’t want to sound like a broken record, but thank you."
            Ry "Truly."
            c "It’s fine, Remy. Remember, I’m always there to talk to, if you need any help."
            Ry "I’ll remember that."

            hide remy with dissolve
            show kolmchousenight behind remy at Pan((0,80),(0,80),5.0) with fade
            $ renpy.pause (2.0)

            m "Remy gave a large yawn, with me following shortly after. I looked at the time and saw that it was quite late into the night."

            show remy normal dk with dissolve

            c "Well, it seems that it has gotten quite late. I think that we should get ready for bed now."
            c "Would you like to sleep with me tonight?"
            Ry "That would be much appreciated."
            c "Then follow me."

            hide remy with dissolve

            m "We both prepared for bed while we continued to talk with each other. After we were finished, I climbed into my bed, with Remy climbing in after me."
            m "Remy, however, started to hug me as soon as he got comfortable in the bed, pulling me closer to him."
            m "He gave me a small kiss afterwards."

            show remy sleep dk with dissolve

            Ry "Goodnight, [player_name]."
            c "Goodnight, Remy. Do try and have a good night’s rest."
            Ry "I’ll try."

            hide remy with dissolve

            m "Just before I drifted to sleep, I felt something wet rolling down on my hair."

            $ renpy.pause (2.0)

            m "A tear."

            scene black with fade
            stop music fadeout (2.0)
            $ renpy.pause (4.0)

            $ kol_tld_remytherapy = True


            jump tld_endingselect


        else:

            Ry "At least I learned a few things from our conversation."
            Ry "You helped me realise how much of a horrible person I actually am, and how much I actually messed up."
            Ry "I thank you for that, [player_name]."
            Ry "Now, I think that I need some time to think."

            hide remy with dissolve
            show kolmchousenight behind remy at Pan((0,80),(0,80),5.0) with fade
            $ renpy.pause (2.0)

            m "Remy gave a large yawn, with me following shortly after. I looked at the time and saw that it was quite late into the night."

            show remy lookcry dk with dissolve

            c "Well, it seems that it has gotten quite late. I think that we should get ready for bed now."
            Ry "I think that it would probably be best. I..."

            $ renpy.pause (2.0)


            Ry "...have a lot to think about now."
            c "That’s fine. I’ll be heading off to my room if you want to come and talk to me again."
            Ry "Goodnight, [player_name]."
            c "Goodnight, Remy."

            hide remy with dissolve

            m "I walked closer to Remy and gave him a hug around the neck. At first Remy seemed to resist, but eventually embraced it."
            m "I prepared for the night’s rest and went to my bed. As I drifted to sleep, I could hear the soft sounds of crying from the living room."

            scene black with fade
            stop music fadeout (2.0)
            $ renpy.pause (4.0)

            $ kol_tld_remytherapy = True


            jump tld_endingselect




    "I’m sorry, but not today.":
        $ renpy.pause (2.5)

        c "I’m so sorry, Remy, but I don’t think that I have the energy to listen after what happened today."
        c "We’ll have to do this some other day."
        Ry sad "It’s fine, [player_name]. It wasn’t that important, anyways."
        Ry "What we’re doing now has a far greater priority."
        m "Remy looked at the roof for a second, appearing to be deep in thought."
        Ry normal "You know, I’m feeling really tired all of a sudden. Would it be alright if we went to sleep earlier today?"
        c "I think that it’s a wise choice."
        c "So much has happened today, and judging by what Logan has said, we’re probably going to do much, much more tomorrow."
        Ry "I see. Then we should head to bed as soon as we can, then."
        c "Agreed."

        hide remy with dissolve

        m "Both of us started to prepare for bed, with Remy keeping the conversation going. Eventually, the two of us were ready for the night."
        c "So, where would you like to sleep tonight?"

        show remy normal with dissolve

        Ry "I think that I’ll take the couch. I wouldn’t want to bother you too much while you try to sleep."
        c "Then it’s settled. Goodnight, Remy."
        Ry "Goodnight, [player_name]."

        hide remy with dissolve

        m "I walked closer to Remy and gave him a hug around the neck. At first Remy seemed to resist, but eventually embraced it."
        m "I prepared a few things for tomorrow and went to bed. As I drifted to sleep, I could hear the soft sounds of crying from the living room."

        scene black with fade
        stop music fadeout (2.0)
        $ renpy.pause (4.0)



        jump tld_endingselect
