label tld_endingselect:

#This code is an absolute mess
#(Added later) And ungodly inefficient!
#I'm so, so sorry that you have to look at this horrid code management


if kol_tld_martinaccepted == True: #Initiates A, B and C

    if kol_tld_remytherapy == True: #Branches between A and B

        if kol_tld_remytherapycounter <= 1: #Checks if Remy opening up scene failed; plays short Ending E

            jump tld_EndingE

        elif kol_tld_remysleep1 and kol_tld_remysleep2 and kol_tld_remyvideogames == True: #Checks for Ending A

            jump tld_EndingA

        else: #Branches to Ending B

            jump tld_EndingB


    else: #No therapy? Ending C for you!

        jump tld_EndingC



#Why is this code so inefficient?!

elif kol_tld_remysleep1 == False: #Checks for Long Ending E

    if kol_tld_remysleep2 == False:

        if kol_tld_remyvideogames == False:

            if kol_tld_remytherapy == False:

                jump tld_EndingE

            elif kol_tld_remytherapycounter <= 1: #Checks if Remy opening up scene failed; plays short Ending E

                jump tld_EndingE


#Why am I just copy pasting the jump to Ending D here instead of making an actual efficient checklist? Idk...
            else:
                jump tld_EndingD

        else:
            jump tld_EndingD

    else:
        jump tld_EndingD

else:

    jump tld_EndingD












label tld_EndingA:

#Introducing to you: The single most wholesome Remy thing probably ever!
#This, at least in my case, will purify your soul from the horrors of this world.
#Enjoy!

$ save_name = (_("TLD - Ending A"))

$ renpy.pause (2.0)

m "It wasn’t long, however, before I woke up again."
Ry normal "[player_name]?"

scene kolmchousenight behind remy at Pan((0,80),(0,80),5.0) with dissolveslow

show remy shy dk with dissolve

Ry "[player_name], are you awake?"
c "Yeah, I’m awake now."
Ry "I’m sorry for waking you up at this time. I heard the rain stopped for a bit, so I wanted to ask you something important."
c "Why? You know that we’re going to have a busy day tomorrow, so we should get as much sleep as we can."
Ry "I know, [player_name]."
Ry smile dk "It’s just that I have planned something for quite some time now, and I feel that now would be the best time to do that little something."
Ry shy dk "Maybe this wasn’t the best time after all."

menu:
    "Yeah, we should get back to sleep.":
        $ renpy.pause (1.0)

        Ry "Alright, then. I’m sorry for waking you up."
        c "Don’t worry, Remy."
        c "Goodnight."
        Ry normal dk "Goodnight, [player_name]."

        scene black with fade
        $ renpy.pause (3.0)
        jump tld_Credits




    "No, it’s alright.":
        $ renpy.pause (1.0)

        Ry "Are you sure? I wouldn’t want to be the reason that you aren’t able to stay awake tomorrow."
        c "Well, there isn’t really any point in going back to sleep now."
        c "Besides, you made me curious with what you have planned."
        Ry smile dk "I’m sure that you’ll enjoy it as much as I will."
        Ry normal dk "I do think that you still need to get prepared, though."
        c "Agreed."

        hide remy with dissolve

        m "I switched from my nightwear to my regular clothing while Remy waited outside my room. Soon, I was ready for whatever Remy had planned at such an odd hour."

        show remy normal dk with dissolve

        c "Alright, I’m finished. What do you have in store?"
        Ry "Well, I figured that maybe we should explore the landscape together."
        Ry smile dk "You still need to do your job as ambassador and show me around the environment, after all."
        c "Don’t you think that it’s a bit dangerous to go traveling now?"
        c "What if the storm suddenly starts again, or if one of us gets injured?"
        Ry normal dk "That is true. However, I feel that this is the best time that we have, especially if Logan is constantly going to keep us busy."
        Ry smile dk "Besides, I always liked the rain at night."
        Ry normal dk "So, are you still willing to go, [player_name]?"
        c "Well, sounds like a fun time for me."
        Ry smile dk "In that case, let’s get outside, then."

        $ renpy.pause (1.0)
        scene kolcitynight at Pan ((0, 360), (0, 0), 4.0) with dissolve
        play music "mx/amb/night.ogg" fadein 2.0

        m "Me and Remy went into the cold yet idyllic night. The streets were still wet from the ongoing storm, yet it seemed that nothing had been damaged too seriously."
        m "We roamed around the city for a while until we arrived at one of the city gates."

        scene kolcitygatenight with dissolvemed
        show remy normal dk with dissolve

        c "Before we go, I need to ask you something, Remy."
        Ry "What is it?"
        c "Does anybody else know that we’re going to be gone?"
        Ry shy dk "Well..."
        Ry "I considered inviting Logan and Martin, but I ultimately decided that this outing should only be for the two of us."
        Ry look dk "I hope that you don’t mind."

        menu:
            "Well, you only live once.":
                $ renpy.pause (0.5)

                Ry "What are you implying, [player_name]?"
                c "Let’s just say that I’m happy it’s just the both of us."
                Ry normal dk "I am as well. I think it’s only for the better if Logan and Martin didn’t know about this."


            "Maybe you should have let them know.":
                $ renpy.pause (0.5)

                Ry "Maybe I should have. It’s only safer, after all."
                Ry normal dk "Well, what's done is done. There isn’t anything we could do to change it."

                show remy sad dk with dissolvemed

                Ry "No matter how much we want it to be otherwise."


            "I don’t think that you should do that next time.":
                $ renpy.pause (0.5)

                Ry "So, is that a yes or a no?"
                c "It’s a yes. Just let somebody else know beforehand when you do this again, otherwise, we could get in some serious trouble."
                Ry normal dk "I’ll remember that, then."




        $ renpy.pause (1.5)

        c "Now that I think about it, how are we even going to get around?"
        c "The wet sand is going to make traveling much harder for us."
        Ry shy dk "I did realise that, [player_name]."

        stop music fadeout (2.0)
        $ renpy.pause (3.0)
        play music "mx/hope_kol.ogg" fadein 2.0

        Ry "That’s why I want you to ride on my back while I’m flying around."
        c "Are you sure that you’ll be able to support me?"
        Ry "Well, all this flying around recently has made me a bit stronger. I should be able to carry you around, at least for a short while."
        c "I don’t think that it’s the best option for you, Remy."
        Ry "Please, [player_name]. I insist."
        c "There really isn’t any way to convince you, is there?"
        c "..."
        c "Alright."
        Ry smile dk "I’ll lower myself so that it will be easier for you to get on."
        Ry normal dk "Just try to not get in the way of my wings too much, though. I do kind of need them, after all."


        hide remy with dissolve

        m "Remy lowered his body for me to climb on his back. I tried to make it not too uncomfortable for Remy, but I could see from the expressions on his face that he felt otherwise."

        Ry look "Hey, I told you to watch out for my wings!"
        c "Sorry..."
        m "After some trouble, I finally got on Remy’s back in a way that he was comfortable enough for flight."

        Ry smile "Well, this is a surprise."
        c "What is it? {w}Wait..."
        c "Don’t tell me that I’m overweight."
        Ry "Quite the opposite! You’re actually much lighter than I thought you would be."
        c "Thanks?"
        Ry normal "In any case, hold on to my neck while I’m flying. It would be quite bad if you happened to fall off mid-flight, wouldn’t you agree?"
        c "Yeah. I’ll make sure to hold on tight."
        Ry "So, are you ready?"

        menu:
            "I was born ready.":
                pass

            "Well, I’ve been ready ever since you woke me up.":
                pass

            "Let’s go!":
                pass


        Ry "Alright, then. Prepare yourself!"

        play sound "fx/takeoff.ogg"

        $ renpy.pause (1.0)

        m "Remy started to gain a faster pace, and, with a heavy beating of his wings, took off to the skies."

        scene kolnightdesert at Pan ((0, 360), (0, 0), 15.0) with fade

        m "Soon, we were high above the city with miles of landscape ahead of us."
        m "Holding on to Remy’s neck, I could feel the cool night breeze flowing through my hair."

        c "This is amazing!"
        Ry smile "I’m really glad you’re enjoying this, [player_name]. To be honest, I was kind of nervous whether you would like flying around."
        c "Well, let’s just say that I’m pleasantly surprised by how exciting this feels. We should definitely do this again sometime."
        Ry normal "Only if time allows it."

        $ renpy.pause (5.0)

        m "I looked around, seeing the city in ways I haven’t seen since the solar flare. A wave of nostalgia hit over me, remembering the days where we didn’t have to struggle for survival."
        m "I also saw the endless desert, wondering how we managed to come so far with so little."
        Ry "So, where would you like to go first?"
        c "I think that I’d like to stay in the sky for a bit longer."
        Ry smile "Well, in that case, I’d be-{w=1.0}{nw}"

        $ renpy.pause (1.0)

        m "Suddenly, I felt a drop of rain hitting my shoulder."
        Ry look "..."
        Ry "And here I hoped that we would have just a little more time."
        c "Maybe we don’t have to return to the city yet."
        c "There should be a cave nearby that we could take shelter in."
        Ry "I think that I saw a cave around here somewhere when I was looking for you. I’ll take you straight to it, if you can give me some general directions."
        c "Of course."

        $ renpy.pause (1.0)

        m "Remy started to pick up speed in ways that I didn’t think were possible for a dragon like him."
        c "(That exercise must really be paying off for us right now.)"
        m "With my directions and Remy’s speed, we were able to find the cave just as the rain started to pour."

        scene koldesertcave at Pan ((0, 20), (0, 220), 4.5) with fade
        stop music fadeout (2.0)
        $ renpy.pause (3.0)
        play sound "fx/landing.ogg"

        m "Remy quickly descended to the ground and entered the cave. I climbed off of Remy’s back with even less elegance than I did before, but Remy didn’t seem to mind this time."
        m "Just as we started to unwind, the rain fell from the clouds once more, with a light wind following soon afterwards."

        play music "mx/starlight_kol.ogg" fadein 1.5

        show remy normal dk with dissolve

        Ry smile dk "Looks like we made it just in time!"
        c "Well, at least I don’t have to worry about going around in wet clothes."
        Ry normal dk "That’s also a good thing, I suppose."
        Ry look dk "Still, it’s a bit inconvenient now that we’re trapped here in this cave. I think that we may have to stay here for the night."

        if sebastianunplayed == False:

            c "At least I have some experience with sleeping in caves."
            Ry shy dk "You do?"
            c "Yeah. I once went on a camping trip with Sebastian, in which we spent the night in a cave."
            Ry "I didn’t think you were the camping type, though."
            c "Well, you experience something new every day."
            Ry normal dk "That’s certainly one way of looking at it."

        else:
            pass



        $ renpy.pause (1.0)
        c "So, what are we going to do now?"
        Ry normal dk "I think that we should just relax for a bit. I’m still a bit tired of flying that far with you, after all."
        c "That is a fair point. My legs are feeling a bit weird now."
        Ry "I understand."

        show remy shy dk with dissolve

        Ry "Do you mind if I...?"
        c "Not at all, Remy."

        hide remy with dissolve

        m "Remy laid down on the ground next to me and snuggled tightly. Remy was strangely warm to the touch, despite having flown in the cold weather for quite some time."
        c "Comfortable?"

        show remy normal dk with dissolve

        Ry smile dk "With you here, more than just comfortable."

        show remy normal dk with dissolve

        $ renpy.pause (1.0)
        m "We relaxed in silence for some time before Remy started to talk again."
        $ renpy.pause (2.0)

        Ry look dk "May I confess something to you, [player_name]?"
        c "Any time, Remy."
        Ry "I thought a lot about what you said, and I realised something really important."
        Ry shy dk "I have gone through so much, and yet..."
        Ry "I'm still here. {w}And it’s all thanks to you."
        c "No need to thank me, Remy."
        Ry "I’m serious here, [player_name]. I don’t think that I’d be here today without you."
        Ry "I can’t even imagine what would have happened to me if you went through the portal."
        Ry sad dk "Sure, you must have felt horrible abandoning everybody you cared about, but at least there is hope for them in another timeline."
        Ry normal dk "Now, we’re here, and with Logan and Martin too."
        Ry shy dk "I guess what I’m trying to say is that there truly is hope left in this world."
        Ry smile dk "You just need someone to help you find it."
        c "I’m honestly flattered. I’m happy that I could have helped you realise that, Remy."
        Ry sad dk "To be honest with you, I don’t think that I’ll ever move past what happened to Amelia, or with everybody I let down."
        Ry normal dk "But as long as you’re here, everything will be alright."

        menu:
            "I feel the same way.":

                c "Now with the both of us here, I can say that I feel the same way."
                c "As long as we stick together, everything will turn out alright in the end."
                Ry "Let’s just hope that it will be alright. A lot can happen from now on, after all."


            "Let’s both hope for a better future, together.":
                c "With all the help we have received the past few days, I can’t really argue with that."
                c "I think that I can confidently say that together, we can hope for a better future."
                Ry smile dk "And what a wonderful thing that hope is!"


            "[[Hug Remy.]":
                $ renpy.pause (1.0)

                hide remy with dissolve

                m "I lifted my arms and wrapped them around Remy in a tight hug. Remy seemed slightly surprised at first, but soon enveloped me with his large wings."

                show remy shy dk with dissolve

                Ry "T-Thank you, [player_name]. Your kindness is too much for words."
                c "Don’t worry about it."


        $ renpy.pause (3.5)
        hide remy with dissolve

        if remystatus == "neutral":
            m "Remy suddenly removed his tie and looked at me shyly. As he slowly approached, I could immediately see what he was trying to do."

        else:
            m "Remy suddenly removed his tie and looked at me with a shy grin in an almost familiar way, immediately describing his intentions."

        show kolremya at Pan((580, 326), (350, 0), 8.0) with fade
        $ renpy.pause (6.0)


        menu:
            "[[Kiss Remy.]":

                hide kolremya
                hide remy
                with fade

                $ renpy.pause (0.5)
                m "I moved closer to Remy and welcomed his warm embrace. Soon we were kissing, just like we had done before the huge fireworks, albeit without the lingering threat of Reza."
                m "We parted soon after, with Remy having a great smile on his face."

                show remy smile b dk with dissolve

                Ry "Consider that as a thank you."
                Ry normal b dk "For everything."
                c "I'm happy that I could have helped you."
                c "In any case, why did you have to remove the tie, though?"
                Ry smile b dk "Let’s just say that I did it for nostalgic reasons."

                hide remy with dissolve

                m "Remy seemed to think for some time while he lay next to me. Afterwards, he let out a small yawn."

                show remy normal b dk with dissolve

                Ry "I think that we should get some sleep, especially if we want to get back home undetected."
                c "That would be for the better. It’s pretty late now, so I’d say that we should get a few hours of sleep before we wake up again. Hopefully, the storm should be gone by then."
                Ry shy b dk "Would you like to sleep under my wing, by any chance? I don’t really think that you’ll have a comfortable experience sleeping on the ground without any scales."
                c "I'd be honoured."

                hide remy with dissolve

                m "I laid down next to Remy and tried to make myself comfortable. It didn’t take long, however, for me to start drifting off to sleep."

                $ renpy.pause (1.0)
                scene black with dissolveslow
                $ renpy.pause (1.0)

                c "I hope you sleep well, Remy."
                Ry "You too, [player_name]."
                m "With the last few seconds I spent awake, I could see Remy smiling next to me."




            "[[Look away.]":

                hide kolremya
                hide remy
                with fade

                $ renpy.pause (0.5)
                m "As Remy moved closer, I looked away. Remy seemed to take the hint almost immediately and went back to snuggling next to me."

                show remy shy dk with dissolve

                Ry "I’m sorry, [player_name]. I didn’t know what came over me for a second."
                c "It’s alright."

                hide remy with dissolve

                m "Remy seemed to think for some time while he lay next to me. Afterwards, he let out a small yawn."

                show remy normal dk with dissolve

                Ry "I think that we should get some sleep, especially if we want to get back home undetected."
                c "That would be for the better. It’s pretty late now, so I’d say that we should get a few hours of sleep before we wake up again. Hopefully, the storm should be gone by then."
                Ry shy dk "Would you like to sleep under my wing, by any chance? I don’t really think that you’ll have a comfortable experience sleeping on the ground without any scales."
                c "I'd be honoured."

                hide remy with dissolve

                m "I laid down next to Remy and tried to make myself comfortable. It didn’t take long, however, for me to start drifting off to sleep."

                $ renpy.pause (1.0)
                scene black with dissolveslow
                $ renpy.pause (1.0)

                c "I hope you sleep well, Remy."
                Ry "You too, [player_name]."
                m "With the last few seconds I spent awake, I could see Remy smiling next to me."




        if kol_tld_secretending == True: #Secret Ending Time!

            $ save_name = (_("TLD - Ending A Extended"))

            stop music fadeout (4.0)
            $ renpy.pause (3.0)

            play sound "fx/system3.wav"
            s "Victory against Remy detected."

            $ renpy.pause (1.5)

            play sound "fx/system3.wav"
            s "Now initialising Secret Extention..."


            scene koldesertcave at Pan ((0, 20), (0, 220), 4.5) with dissolveslow

            m "A few hours passed before I woke up again. Luckily, it seemed that the storm had mostly calmed down to the point where we could travel without getting wet."
            m "I woke up Remy to let him know that we should get back home before the sun rises."

            show remy normal dk with dissolve

            Ry look dk "Hello, [player_name]. Is it time already?"
            c "Pretty much. The storm has mostly calmed down with the exception of a little wind, so we should get going now before morning hits."
            Ry "I see."

            hide remy with dissolve

            m "Remy spent several minutes trying to gather his thoughts. Eventually, he was awake enough to travel."
            m "Just like at the city gates, Remy lowered his body for me to climb on to his back. This time, however, I managed to get on with less struggle than before."
            Ry smile "Looks like you’re getting the hang of it, [player_name]."
            c "I think it’s just one of those things that you just need to practice over and over again before you get used to it."
            Ry normal "Maybe. Are you ready to go?"
            c "Sure am. Let's go."

            m "Remy took a few steps back and took off into the skies. Once again, I enjoyed the cool breeze that came with flying while Remy soared through the air."

            play sound "fx/takeoff.ogg"
            $ renpy.pause (3.0)

            scene kolnightdesert at Pan ((0, 360), (0, 0), 4.0) with fade

            m "This time, Remy wasted no time in getting to the city as fast as possible, as he flew a direct course to my house at astonishing speeds."

            $ renpy.pause (1.5)
            scene kolcitygatenight with fade
            play sound "fx/landing.ogg"

            m "Soon, we landed at the city gate. I climbed off of Remy, with him taking deep breaths after flying for such a far distance at such speeds."
            m "After letting Remy catch his breath, we started to walk back to my house."

            $ renpy.pause (2.0)

            show remy look dk with dissolve
            play music "mx/amb/night.ogg" fadein 2.0

            Ry "Wait, [player_name]. Can you hear that?"
            m "I tried to listen for any unusual noises, but couldn’t hear anything."
            c "Sorry, but I can’t hear anything."
            Ry "It sounds familiar, yet I can’t exactly remember from where. {w}And it seems to come from Logan’s house, as well."
            c "Should I go check it out, then?"
            Ry shy dk "I think that it would be for the better, as if it {i}has{/i} something to do with Logan, then you are far more suited to handle the situation."
            c "I understand. In that case, I’ll meet you back at our house."
            Ry normal dk "Alright. Good luck, [player_name]."

            hide remy with dissolve
            scene black with fade
            play sound "fx/steps/rough_gravel.wav"

            m "I started to walk to Logan’s house while Remy continued his path to my house. As I got closer and closer, I could hear some noises coming from inside Logan’s house."

            stop music fadeout (1.0)
            scene kolloganoutnight at Pan ((0, 0), (0, 250), 5.0) with dissolveslow

            m "Eventually, I could distinctly make out what those noises were as I reached Logan’s front door. Luckily for me, it seemed to be unlocked."

            play music "mx/warp_kol.ogg" fadein 1.0

            scene kolloganhousenight at Pan ((0, 220), (0,360), 3.0) with dissolveslow
            $ renpy.pause (4.0)
            scene kollogantvnight at Pan ((0, 200), (0,200), 3.0) with dissolve

            m "After some looking around, I found Logan busy with his repaired television. His hearing was far better than mine, however, and immediately turned the television off when he heard my footsteps enter the room."

            stop music

            show logan tsurprised dk with dissolve

            Lg "[player_name]? What on earth are you doing here at this time?"
            c "I heard some noises and decided that I should investigate."
            Lg tnormal dk "Well, there’s absolutely nothing to worry about. All I did was..."

            $ renpy.pause (1.0)

            Lg tannoyed dk "Uh..."

            $ renpy.pause (1.0)

            Lg "Hmmm..."

            $ renpy.pause (1.0)

            Lg tsmiling dk "Ah. Fix some old speakers and test them out!"
            c "And with what did you test them out?"
            Lg tannoyed dk "Uh..."

            $ renpy.pause (1.0)

            Lg tsmiling dk "A radio, of course!"
            c "So, you’re telling me that you managed to catch a non-existent radio signal late at night and decided that you should broadcast it to the surrounding area?"

            show logan tserious dk with dissolve
            $ renpy.pause (3.0)

            Lg "*sigh*"
            Lg "I’m not good at lying, am I?"
            Lg "Alright, I played some video games and decided to put the audio output extra loud."
            Lg "Surprisingly, this has apparent consequences." #Wow, who would have guessed?
            Lg "Please don’t go and share this information with anybody. I’d hate to hide the fact that I’m procrastinating on work by playing video games."
            c "On one condition."
            c "You'll have to win a single match against me."
            Lg tannoyed dk "This ought to be quite the challenge."

            play music "mx/warp_kol.ogg" fadein 1.0

            Lg tsmiling dk "I'm in."
            Lg "You'll find me much harder to beat than Remy, since I can actually use a controller properly."
            c "Your funeral, Logan."
            Lg tnormal dk "Heh. Talk about hubris."
            Lg "But enough talking. Let's start."
            c "Bring it!"

            $ renpy.pause (1.5)
            scene black with dissolveslow
            $ renpy.pause (3.5)


            $ _game_menu_screen = None
            $ renpy.block_rollback()

            show extra1 at Pan ((450, 0), (540,0), 25.0)
            show koltldcredits1 at right
            with dissolvemed

            $ renpy.pause (10.0)

            show black2 at right with dissolvemed
            show koltldcredits2 at right
            with dissolvemed

            $ renpy.pause (10.0)

            scene black with dissolvemed

            show rezabitten at Pan ((-500, 56), (-200,0), 24.0)
            show credits1 at left
            with dissolvemed

            $ renpy.pause (10.0)

            show black2 at left with dissolvemed

            show credits2 at left with dissolvemed

            $ renpy.pause (10.0)

            scene black with dissolvemed

            show remyapt at Pan ((0, 170), (600, 0), 24.0)
            show credits3 at right
            with dissolvemed

            $ renpy.pause (10.0)

            show black2 at right with dissolvemed

            show credits4 at right with dissolvemed

            $ renpy.pause (10.0)

            scene black with dissolvemed




            show remysad at Pan ((-250, 326), (430, 0), 25.0)
            show credits5 at left
            with dissolvemed

            $ renpy.pause (10.0)

            show black2 at left with dissolvemed

            show credits6 at left with dissolvemed

            $ renpy.pause (10.0)

            scene black with dissolvemed




            show cgvara at Pan ((0, 326), (1580, 0), 25)
            show credits7 at right
            with dissolvemed

            $ renpy.pause (10.0)

            show black2 at right with dissolvemed

            show credits8 at right with dissolvemed

            $ renpy.pause (10.0)

            scene black with dissolvemed



            show cg1 at Position(xpos=0.8, xanchor='center')
            show credits9 at left
            with dissolvemed

            $ renpy.pause (10.0)

            show black2 at left with dissolvemed

            show credits10 at left with dissolvemed

            $ renpy.pause (10.0)

            scene black with dissolvemed

            scene logo with dissolvemed

            $ renpy.pause (9.0)

            scene black with dissolvemed

            stop music fadeout 2.0

            $ renpy.pause (4.0)


            $ persistent.kol_tld_endinga = True
            $ persistent.kol_tld_ending_achieved = True
            $ persistent.kol_tld_secretending = True


            play sound "fx/system3.wav"
            s "Ending achieved: Extended [[A]quiring new Hope, or The Secret Ending for short."

            play sound "fx/system.wav"
            s "Congratulations! You have seen the best possible ending in The Last Dragon, as well as the secret extension! Looks like randomness has favoured you!"

            play sound "fx/system3.wav"
            s "Feel free to try and get another ending, or just savour this moment."

            jump ml_main_menu


        else:


            $ _game_menu_screen = None
            $ renpy.block_rollback()

            show extra1 at Pan ((450, 0), (540,0), 25.0)
            show koltldcredits1 at right
            with dissolvemed

            $ renpy.pause (10.0)

            show black2 at right with dissolvemed
            show koltldcredits2 at right
            with dissolvemed

            $ renpy.pause (10.0)

            scene black with dissolvemed

            show rezabitten at Pan ((-500, 56), (-200,0), 24.0)
            show credits1 at left
            with dissolvemed

            $ renpy.pause (10.0)

            show black2 at left with dissolvemed

            show credits2 at left with dissolvemed

            $ renpy.pause (10.0)

            scene black with dissolvemed

            show remyapt at Pan ((0, 170), (600, 0), 24.0)
            show credits3 at right
            with dissolvemed

            $ renpy.pause (10.0)

            show black2 at right with dissolvemed

            show credits4 at right with dissolvemed

            $ renpy.pause (10.0)

            scene black with dissolvemed




            show remysad at Pan ((-250, 326), (430, 0), 25.0)
            show credits5 at left
            with dissolvemed

            $ renpy.pause (10.0)

            show black2 at left with dissolvemed

            show credits6 at left with dissolvemed

            $ renpy.pause (10.0)

            scene black with dissolvemed




            show cgvara at Pan ((0, 326), (1580, 0), 25)
            show credits7 at right
            with dissolvemed

            $ renpy.pause (10.0)

            show black2 at right with dissolvemed

            show credits8 at right with dissolvemed

            $ renpy.pause (10.0)

            scene black with dissolvemed



            show cg1 at Position(xpos=0.8, xanchor='center')
            show credits9 at left
            with dissolvemed

            $ renpy.pause (10.0)

            show black2 at left with dissolvemed

            show credits10 at left with dissolvemed

            $ renpy.pause (10.0)

            scene black with dissolvemed

            scene logo with dissolvemed

            $ renpy.pause (9.0)

            scene black with dissolvemed

            stop music fadeout 2.0

            $ renpy.pause (4.0)



            $ persistent.kol_tld_endinga = True
            $ persistent.kol_tld_ending_achieved = True


            play sound "fx/system3.wav"
            s "Ending achieved: [[A]quiring New Hope, or Ending A for short."

            play sound "fx/system.wav"
            s "Congratulations! You have seen the best possible ending in The Last Dragon! I have a feeling that this won't be the last time that he'll want to fly with you..."

            play sound "fx/system3.wav"
            s "Feel free to try and get another ending, or just savour this moment."

            jump ml_main_menu







label tld_EndingB:

$ save_name = (_("TLD - Ending B"))

$ renpy.pause (3.0)
scene kolmchouseday at Pan ((300, 80), (0,80), 5.0) with dissolveslow
play music "mx/dash.ogg" fadein 1.0

m "I woke up fairly late in the morning. As I looked outside of my window, I saw that there weren’t any clouds in the skies anymore."
m "I turned to my side and noticed that Remy was still asleep. I decided that it was best to leave him be, however, especially after the events of last evening."
m "I started preparing myself for the day ahead of me. Much to my surprise, however, I found a small note under the front door."
c "{i}Meet me at the city centre at your own pace. And bring Remy with you, of course.{/i}"
c "{i}-Logan{/i}"
c "(What is he up to now?)"
m "I put the note down and started to make breakfast. It didn’t take long for Remy to enter the living room as I started cooking."

show remy normal with dissolve

Ry "Good morning, [player_name]."
c "Morning, Remy. I see that you decided to sleep in today."
Ry shy "Wait, I did?"
c "Well, both of us did. Don’t worry about it, though. I’m making breakfast for us, and supposedly, we’re going to the city centre at our own pace."
Ry normal "How come?"
c "Apparently Logan left a note saying that we should take our time this morning and meet him at the city centre."
Ry look "I wonder what he’s up to now."

menu:
    "My thoughts exactly.":
        $ renpy.pause (0.5)

        Ry shy "Is that so?"
        Ry smile "It looks like we think in a very similar way, then."
        c "Let’s be honest here: Logan is so unpredictable in his ways that he has become fairly predictable overall."
        Ry normal "I don’t think that I understand."
        c "Don’t worry. It just takes time to figure him out."


    "I think that I could guess.":
        $ renpy.pause (0.5)

        Ry normal "Well, what’s your guess, then?"
        c "If I had to make an assumption, I’d say that Logan is busy zapping things and swearing."

        show remy smile with dissolve
        $ renpy.pause (0.5)

        m "Remy gave a slight chuckle."
        Ry "Well, I wouldn’t say that you’re wrong there."


    "Let’s worry about it later.":
        $ renpy.pause (0.5)

        Ry normal "I think that it would be for the best."
        Ry "For now, let’s worry about breakfast."


$ renpy.pause (0.5)
show remy normal with dissolve

Ry "So, what are you making for us?"
c "It isn’t the most original or appetising, but I’m making some baked beans and sausages."
Ry smile "Sounds pretty good!"
Ry normal "Any way that I could help you out?"
c "It’s alright. I’m almost finished, anyways."
Ry "In that case, I’ll just wait on the couch."

hide remy with dissolve

m "Remy patiently waited for me as I finished up with the cooking. Soon, the food was finished."

show remy normal with dissolve

c "Here you go, Remy. Hopefully it doesn’t taste {i}too{/i} bad."
Ry smile "I’ll be the judge of that."
m "We slowly ate our breakfast in silence, with only a few glances being exchanged between us. When we were eventually finished, Remy gave me a slightly concerning look."

show remy look with dissolve

Ry "Well, that was..."

$ renpy.pause (0.3)

Ry "Interesting."
c "I know, Remy. I really need to learn how to make my food not taste like dirt at some point."
Ry normal "Come on, [player_name], I didn't think that it was {i}that{/i} bad."
c "But it could be better."
Ry "I suppose you’re right."
Ry "Well, now that we’re finished, do you think that we should go and see what Logan has in store for us?"
c "We don’t have much of a choice, to be honest."
Ry "And I suppose you’re right again. Let’s go."

hide remy with dissolve

$ renpy.pause (1.0)
scene city at Pan ((0, 360), (0, 0), 5.0) with dissolve
$ renpy.pause (7.0)

scene kolcitycentre at Pan ((0,180),(0,180), 3.0) with dissolve
$ renpy.pause (2.0)
stop music fadeout (2.0)

m "We went to the city centre while having a pleasant conversation with each other. Upon arriving, I was surprised to see Martin also there, standing next to Logan."

show remy normal flip at Position(xpos = 0.10) with dissolve
show logan normal at Position(xpos = 0.75) with dissolve
show martin normal at Position(xpos = 0.90) with dissolve
play music "mx/hydrangea.ogg" fadein 2.0 #Yes, I also decided to copy Bryce3. I cannot come up with an original idea for the life of me...

Lg smiling "Ah, welcome you two. I want to say that it took you long enough to get here, but that little note of mine already said otherwise."
Mt happy "Good morning [player_name]! And an especially good morning to you, Remy!"
c "Morning, Logan. Morning, Martin."
c "How are you two doing?"
Lg normal "Believe it or not, but I actually got a good night’s sleep for once. Turns out having an intense storm break out does wonders to your sleep."
Lg smiling "Looks like our little weatherboy made the right predictions."
Mt serious "Please don’t call me that, Logan."
Mt normal "Now, to answer your question, [player_name], I’m doing fairly well. A bit under the weather, but otherwise, I’m doing good."

show logan serious with dissolve
$ renpy.pause (1.0)

Lg "..."
Lg "Damn it, Martin."
Mt confused "What did I do wrong?"
Lg annoyed "Wait? You didn't notice?"
Mt "Notice what? I’m sorry if I’m sounding a bit oblivious, but I’m genuinely confused."

show logan serious with dissolve
$ renpy.pause (1.0)

Lg "*sigh*"
Lg "Nevermind."
c " I’m sorry to interrupt here, but what are we going to do today? This seems like a strange place to do anything useful."
Lg "You really want to know, huh?"
Lg "Alright, here’s the answer:"
Lg smiling "Nothing!"
Ry look flip "What do you mean by “nothing”?"
Mt normal "To celebrate the storm passing safely, Logan decided that we should take the day off and have a good ol’ fashioned barbeque."
Lg normal "That’s right! I mean, what better way is there to celebrate surviving a near cataclysmic event by cooking meat over an open fire?"
c "I’ll admit, this is really unusual. {w}Even for you, Logan."
Lg "Well, we didn’t have a proper chance to catch up yet, especially with all the things that have been going on."
Lg annoyed "Like, you know, the generators, Remy and Martin joining us, the repairs-{w=1.5}{nw}"
Mt serious "I think that [player_name] gets it, Logan."

menu:
    "Yeah. No need to make a comprehensive list.":
        $ renpy.pause (0.5)

        Lg normal "Suit yourself, then."
        Lg "Remember, lists help you to keep track of your schedules and remind you of what to do."
        Lg annoyed "Or so they taught me at university."


    "Really? But there were still some things that needed explaining.":
        $ renpy.pause (0.5)

        Mt "Alright, even {i}I{/i} could see that what you just said was sarcasm."
        c "Looks like you’ve gotten better."
        Mt normal "Spending some time with Logan did help quite a lot."
        c "Go figure."
        Lg serious "You do realise that I’m still here, right?"
        c "I know."

        $ renpy.pause (0.5)

        Lg "..."


    "But does Remy understand, though?":
        $ renpy.pause (0.5)

        Ry "I do. After all, I lived through each of those experiences."
        Lg serious "So did I."
        Lg annoyed "At least to a certain degree."



$ renpy.pause (1.0)

Lg normal "In any case, I have some meat and veggies right here."
Lg "Did you bring the matches like I asked you to, Martin?"
Mt normal "Yeah. They should be right here."
m "Martin searched inside his pockets for some time, but couldn’t find what he was looking for."

$ renpy.pause (0.5)


Mt serious "Or still at the house."
Mt "Oops."
Lg serious "So much for bringing everything."
Ry shy flip "I think I have a solution."
Mt normal "Oh? What’s your idea, Remy?"
Ry "It’s not something that I have done in some time, but I could try to light the fire."
Ry "You should all just stand back, just in case something goes wrong."
c "Seems fair enough."
Mt "Well, just give it your best shot."

$ renpy.pause (1.0)

Lg "Again? Really?"
c "For somebody who hates puns, you sure do seem to pick them up quite quickly."
Lg normal "Oh, shush."

hide remy with dissolve
hide logan with dissolve
hide martin with dissolve

m "Everybody took a few steps back to give Remy some space. He seemed to struggle a bit at first, but was soon able to spray two streams of liquid that ignited into a large fire as soon as it made contact with the firewood."

play sound "fx/firex.ogg"

show remy normal flip at Position(xpos = 0.10) with dissolve
show logan normal at Position(xpos = 0.75) with dissolve
show martin normal at Position(xpos = 0.90) with dissolve

Ry smile flip "Looks like I still got it."
Ry normal flip "Sure, I’ve lost my touch a fair bit, but otherwise a pretty good job."
c "Well, I’ve never seen you breathe fire before, so I can’t really say anything there."
Ry shy flip "Oh, I completely forgot that I never showed you how dragons breathe fire."
Ry smile flip "At least I could show you now."
Lg annoyed "I wonder how dragon fire would affect the meat."
Mt "If I had to guess, the meat would probably taste the same, as the heat and smoke from the fire doesn’t feel too different from your standard fires."
c "We’ll just have to find out."

hide remy with dissolve
hide logan with dissolve
hide martin with dissolve

m "We talked about random nonsense as we waited for the meat to cook. Martin, it seemed, was a master at cooking meat over an open fire, making sure that the meat never overcooked while also making sure every piece received a fair bit of smoke to add to the flavour."
m "Soon, the food was ready."

show remy normal flip at Position(xpos = 0.10) with dissolve
show logan normal at Position(xpos = 0.75) with dissolve
show martin normal at Position(xpos = 0.90) with dissolve

Mt happy "Alright, food’s done. Who wants what piece?"
Lg "I’ll take the pork chops."
Ry "I think that I’d like to have those over there."
c "The chicken wings?"
Ry shy flip "Are that what they’re called? I still need to learn the names of all the different foods here, so please bear with me."
Mt normal "It’s alright."
Mt "I’ll hand the chicken wings to Remy while I claim ownership of these ribs."
Mt "What do you want, [player_name]?"

menu:
    "Pork chops":
        $ renpy.pause (0.5)

        Lg smiling "A man of culture, I see?"
        Lg "Welcome to the club."
        c "Thanks, I guess."


    "Chicken wings":
        $ renpy.pause (0.5)

        Ry "Did you take them just because I took them?"
        c "I’ll leave that answer for myself."
        Ry normal flip "Well, I suppose it doesn’t matter. Just take what you want the most."


    "Ribs":
        $ renpy.pause (0.5)

        Mt happy "Feeling messy today, aren’t we?"
        c "I just like eating ribs, that’s all."
        Mt normal "I’m glad that we see eye to eye on what the best option at a barbeque is."


    "Sausage": # ;)
        $ renpy.pause (0.5)

        Lg smiling "An interesting choice, to be sure."
        Mt happy "I see that [player_name] is feeling a bit adventurous today."
        c "What are you all implying?"
        Lg "Oh, nothing."
        Mt "We’re just seeing that you want some “meat”, that’s all."
        m "Suddenly, realisation hit me as I made sense of what Logan and Martin were referring to."
        c "Oh..."
        Lg normal "And looks like you ruined it, Martin."
        Mt normal "Well, it was fun while it lasted."


    "Veggie skewers":
        $ renpy.pause (0.5)

        Mt "Going vegetarian, are we?"
        Lg annoyed "Wait, I always thought that you ate meat. Since when did that change?"
        c "Sometimes, it’s just nice to have a meat-free meal."
        Lg serious "Oh, you’re one of {i}those{/i}, aren’t you?"
        Mt confused "Those being?"
        Lg normal "Nevermind. Just an inside reference."


$ renpy.pause (1.0)

Mt normal "Well, now that we all have our food, I suggest that we dig in."
Lg normal "Agreed. I haven’t had anything to eat yet today, so I’m pretty damn hungry."

hide remy with dissolve
hide logan with dissolve
hide martin with dissolve

m "We all started to eat our meals, with everybody showing an expression of satisfaction. It wasn’t long before all our plates were empty."

show remy normal flip at Position(xpos = 0.10) with dissolve
show logan normal at Position(xpos = 0.75) with dissolve
show martin normal at Position(xpos = 0.90) with dissolve

c "Damn, that was good. Where did you learn to cook that well?" #Looks like everyone is a good cook except for MC...
Mt "I knew somebody back in my city that used to hold these amazing barbeque competitions."
Mt happy "All I did was learn from all the contenders."
Mt normal "Though, truth be told, I think the taste also had something to do with Remy’s fire, even if I did say otherwise beforehand."
Lg "Agreed. Not too dry with just the correct amount of smokey flavour. All in all, perfection."
Lg annoyed "Now that I think about it, these pork chops remind me of something that I used to do back in my university days."
Ry "How so?"
Lg normal "Well, me and my friends would always go to the local ice cream parlour after we had some smoked pork chops. It was kind of our tradition, so to speak."
Lg "I remember that I always used to get a nice bowl of spaghettieis for dessert, with my friends always getting some mango and cherry ice cream."
c "Wait, what? You ate spaghetti as a dessert?"
Lg serious "Are you seriously telling me that you mistook {i}spaghettieis{/i} for {i}spaghetti{/i} just now?"
Mt "I think I know what you’re talking about, Logan."
Mt happy "You’re referring to that one ice cream that looks like spaghetti, correct?"
Lg smiling "The one and only."
Ry smile flip "Now I remember! There once was a dragon that actually sold some spaghettieis back home."
Ry sad flip "I never really got the chance to taste it, though."
Ry normal flip "I only used to order plain vanilla ice cream."
Mt normal "So, dragons had ice cream. Interesting."

$ renpy.pause (1.5)

c "Now that I think about it, where did you even get all this food? There aren’t really any livestock left here, so it can't have been easy to get all this variety."
Lg normal "You can all thank Martin and his group for the food, as everybody somehow managed to bring quite a lot of supplies with him."
Lg "And thanks to the superior preservation technology they still had at Martin’s city, fresh meat could be stored for far, far longer time periods than normal."
c "Martin’s city really seemed like a paradise compared to what we have."
Mt serious "It was. It’s pretty sad to see it all gone, but what else is there that we can do now, except for trying to create a new home here?"
Lg serious "And to think that I almost shot all of you because I thought that you were all raiders in disguise. I shouldn’t have made such a rash decision without thinking it through first."
Mt normal "Don’t worry too much about it. I probably would have done something similar if our roles were switched around."
Mt serious "Still, pointing a gun at our faces was kind of a prick move."
Lg "Yeah, I know. My most sincere apologies about that. I guess that I’ll just have to work on my reactions a bit."
Ry "Speaking of work: What are we going to do now after we cleaned up the mess?"

if kol_tld_wtpchosen == True:
    Lg "Well, we’re going back to the water treatment plant, of course. No point in just wasting such a beautiful day like this."

else:
    Lg "Well, we’re going back to the factory, of course. No point in just wasting such a beautiful day like this."


Ry look flip "..."
Lg normal "I’m just pulling your leg, Remy. Do what you want! I figured that we have kind of been overworking ourselves recently, so a day off wouldn't hurt {i}that{/i} much."
Ry shy flip "You wouldn’t still have that video game system somewhere, do you?"
Lg smiling "It’s still where you last saw it. Knock yourself out."
Mt confused "Wait, what are you talking about?"
Lg normal "I’ll explain later."
Mt serious "Just another thing to add to the list..."

if kol_tld_remyvideogames == True:
    Ry smile flip "Let’s go have ourselves a rematch, [player_name]."
    c "You wouldn’t smile like that after I’m done with you."
    Ry normal flip "We shall see."

else:
    Ry normal flip "Now, let's go play some video games, since you didn't want to play last time."
    c "Alright. Let's see how good you actually are."
    Ry smile flip "You'd be surprised."



scene black with dissolveslow
$ renpy.pause (7.0)


$ _game_menu_screen = None
$ renpy.block_rollback()

show extra1 at Pan ((450, 0), (540,0), 25.0)
show koltldcredits1 at right
with dissolvemed

$ renpy.pause (10.0)

show black2 at right with dissolvemed
show koltldcredits2 at right
with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

show rezabitten at Pan ((-500, 56), (-200,0), 24.0)
show credits1 at left
with dissolvemed

$ renpy.pause (10.0)

show black2 at left with dissolvemed

show credits2 at left with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

show remyapt at Pan ((0, 170), (600, 0), 24.0)
show credits3 at right
with dissolvemed

$ renpy.pause (10.0)

show black2 at right with dissolvemed

show credits4 at right with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed




show remysad at Pan ((-250, 326), (430, 0), 25.0)
show credits5 at left
with dissolvemed

$ renpy.pause (10.0)

show black2 at left with dissolvemed

show credits6 at left with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed




show cgvara at Pan ((0, 326), (1580, 0), 25)
show credits7 at right
with dissolvemed

$ renpy.pause (10.0)

show black2 at right with dissolvemed

show credits8 at right with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed



show cg1 at Position(xpos=0.8, xanchor='center')
show credits9 at left
with dissolvemed

$ renpy.pause (10.0)

show black2 at left with dissolvemed

show credits10 at left with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

scene logo with dissolvemed

$ renpy.pause (9.0)

scene black with dissolvemed

stop music fadeout 2.0

$ renpy.pause (4.0)


$ persistent.kol_tld_endingb = True
$ persistent.kol_tld_ending_achieved = True



play sound "fx/system3.wav"
s "Ending achieved: [[B]ounded by Service, or Ending B for short."

play sound "fx/system.wav"
s "Congratulations! You have seen The Last Dragon's good ending! See, Martin could be trusted after all!"

play sound "fx/system3.wav"
s "Feel free to try and get another ending, or just savour this moment."

jump ml_main_menu



label tld_EndingC:


$ save_name = (_("TLD - Ending C"))

$ renpy.pause (3.0)
scene kolmchouseday at Pan ((300, 80), (0,80), 5.0) with dissolveslow

m "I woke up early in the morning with a slight ache in my side. I started to prepare for the day by switching my clothes and heading to the kitchen to make breakfast."
m "However, I saw that Remy was already awake, sitting on the floor with his wings covering his eyes. When he heard me, he unfurled them, revealing a tired expression."

play music "mx/loss_kol.ogg" fadein 2.0 #Once againn, weird music choice, but whatever

show remy look with dissolvemed

Ry "Oh, hello [player_name]."
c "Good morning, Remy. How did you sleep?"
Ry "Barely. I’ve spent most of the night awake trying to process some thoughts, that’s all."
c "Does it have to do with what you wanted to tell me last night?"
Ry "Partly."
c "Well, if you want to share your thoughts, then go ahead. Since we’re awake early today, we have more than enough time to discuss it."

show remy sad with dissolve
$ renpy.pause (1.8)

Ry "I’ll try to keep it short."
Ry "I don’t know how much more I can take. Everytime I have a small bit of hope, the universe just seems to take it away from me."
c "I’m sorry to hear that, Remy. Is there anything I could do to help?"

$ renpy.pause (1.5)

Ry "I don't know."
Ry "Everything I’ve ever done seems to hurt someone in some way."
Ry shy "And yet, there are some things I did that have helped others."
Ry look "Just look at Martin and his group, for example. I can’t imagine what would have happened to them if we didn’t let them into the city."
Ry "Another example is the repairs we have been trying to do. Would those even have been possible without my help?"
Ry sad "I just can’t make sense of anything anymore."
c "Well, I’m here to try and help you make sense, if anything."
Ry shy "And I appreciate that, [player_name]. Truly, I do."
Ry look "It’s just that..."

$ renpy.pause (1.5)

Ry sad "I wonder if that would be enough."
c "Is this about Amelia, by any chance?"
Ry "..."
Ry "Not only her."
Ry look "But that would have to wait. I think that we should go and see Logan now. I don’t know if he would be awake, considering how early it is, but it’s worth a shot."
c "We’re talking about Logan here. I’d be surprised if he hasn’t already begun with work."
Ry "Yeah, you're right."

play sound "fx/knocking1.ogg"

m "We were just about to leave the house when we heard a knocking at the door."
c "(Looks like we didn’t even need to go anywhere.)"

play sound "fx/door/door_open.wav"

m "I opened the door, only to find Martin instead."
$ renpy.pause (2.5)

show remy at right with ease
show martin normal flip at Position(xpos=0.25) with easeinleft

Mt happy flip "Salutations, O Great [player_name] and Remy! How are you doing on this ever so fine morning?" #Martin is Bri'ish confirmed
c "I’m doing pretty good. Why the fancy talk, though?"
Mt normal flip "Just a little something I’ve been practicing, that’s all."
m "Martin looked over to Remy and seemed to immediately understand the situation."
Mt serious flip "I can see that you’re not doing too well, Remy. Didn’t look like you got much sleep, either."
Mt "Is there something on your mind that you want to talk about?"
Ry shy "I just think that I need some time alone, that’s all."
Mt "Are you sure? I’ve learned from my group that spending time alone to gather your thoughts rarely helps you in the long run, especially if those thoughts are negative in nature."
Mt "However, if you aren’t ready yet, then I can understand that."
Mt "Having somebody try and force you to open up when you’re unwilling can cause some serious problems for your relationships."
Mt "And I’m talking from experience." #What experience? Hmmmmm...
Ry look "I see. Thank you for the offer, Martin, but I don’t think I’m ready to share with anybody other than [player_name] yet."
Mt "Gotcha. Just take your time. I’ve found that time doesn’t heal all wounds, but with the right people, it can certainly numb the pain enough." #That is a good wisdom, tbh.
Ry "I’ll remember that."
c "So, what brings you here this early?"
Mt normal flip "I wanted to talk to you about the... {w}what did you call it again?"
Mt "Ah. {w}The portal."
c "What about it?"
Mt "Well, a few people decided that they wanted to try and get a closer look at, and I quote, “the machine that brought the white dragon here.”"
Mt serious flip "However, when they got near, the portal started to make some strange sounds."

stop music fadeout (15.0)

Mt "Said people ran away as fast as they could to find me, told me everything that happened, and, well, now I’m here."
Mt "I think that it would be a pretty good idea if you checked on the portal."
m "I wondered what could have triggered the portal to behave like the way that Martin had described. In the end, I couldn’t come up with any decisive answer."
c "I’ll check it out right now and see what’s wrong."
c "Are you coming with me, Martin?"
Mt normal flip "I’m good. I don’t know about anybody else, but literal portals to other worlds tends to freak me out a bit. I’ll just head to Logan and see if I could help him with anything there."
c "Alright, then. See you later."
Mt "Cheers!"

show martin normal with dissolve
hide martin with easeoutleft
show remy at Position(xpos=0.75) with ease #Yay! More inefficient and useless line sof code!

m "Martin soon left, heading in the direction of Logan’s house. I looked back at Remy and saw that he was in even deeper thought than he was before."
c "What do you think about what Martin told us, Remy?"
Ry look "I can’t say. This isn’t just something that I could try and research to get some extra insight. I’m completely lost here."
c "That makes both of us, I’m afraid."
Ry normal "I suppose the only thing that we could do is to check it out."
c "That it would be a wise decision."

hide remy with dissolve

$ renpy.pause (2.0)
scene city at Pan ((0, 240), (0, 0), 4.5) with dissolve

m "We both went outside, anxious to see what happened to the portal. The storm had mostly cleared, although some gusts of winds could still be felt."
m "Eventually, we reached the portal. Upon initial inspection, nothing seemed to have been damaged or changed."

play music "mx/clocks_kol.ogg"

show remy normal flip with dissolve

c "That’s odd. It doesn’t seem that anything is wrong."
Ry "Maybe you could check the logs. If the portal made some strange sounds, then any extra information that could be usable should probably be stored in there."
c "Good idea."

hide remy with dissolve

play sound "fx/telbuttons.ogg"
$ renpy.pause (2.0)

m "I checked the logs on the portal. At first, nothing seemed out of the ordinary. Only records of the portal being used during our trips showed, as well as the records of everybody in the city using it."
m "I started to lose hope of figuring out what’s wrong, until I saw something at the “Receiving” logs."

$ renpy.pause (2.0)

m "A failed attempt from an unknown source at approximately twenty minutes ago tried to send something through."
c "What the..."

show remy look flip with dissolve

Ry "What happened, [player_name]?"
c "According to the logs, there was a failed attempt from an unknown source to send something through."
Ry shy flip "Wait..."
Ry "Could it mean that... {w}They’re still alive?"
c "That wouldn’t make any sense, though. The comet did hit, so everything would have been destroyed, including the portal on the other side."
c "What I don’t understand, however, is what the unknown source was referring to."
c "If it {i}was{/i} from the other side, then it wouldn’t have said that it was from an unknown source, since the portal displayed that it was connected to another portal when we first activated it."
Ry look flip "Maybe it’s because something has gone wrong with the portal that prevents it from verifying its connection, or something like that."
Ry sad flip "For all we know, maybe somebody survived and is trying to escape from my world."
c "No, that wouldn’t be possible. The meteor would have been far too large for any complex life like dragons to have survived."
c "I’m sorry, but there isn’t anybody left."
Ry "I see."

$ renpy.pause (1.0)

Ry look flip "Then why did the portal activate?"
c "I don’t know. Maybe we should talk to Lo-{w=0.7}{nw}"

hide remy with dissolve
play sound "fx/telstart.ogg"

m "Suddenly, strange sounds came from the portal. It didn’t sound like the usual noises that came when you activated the portal, however."
m "Me and Remy took a few steps back, wondering what was happening now. The portal continued to operate for a few more seconds, then deactivated."

stop sound

m "After I inspected the portal further, I spotted a small note on the ground. I picked it up with a sense of curiosity and opened it up. As I continued reading, my expression started to change to one of confusion and fear."

show remy normal with dissolve

Ry "What is that?"
c "This is a note that appeared from the portal. I’ll read it out loud for you."

$ renpy.pause (1.0)

c "{i}TTT #47. If this note happens to reach you, please return it by typing the following code into the portal’s destination co-ordinates.{/i}"
c "{i}As for the meaning of this note, pay no attention to it. Finding the truth will only hurt us in the long run, especially if this proves to be a success.{/i}"
c "{i}That will be all.{/i}"

show remy shy with dissolve

$ renpy.pause (2.5)

Ry "..."
Ry "I don’t think I understand, [player_name]. What should we do?"

menu:
    "I think that we should send the note back.":
        $ renpy.pause (1.5)

        c "Well, it’s obvious whoever sent this wants it back, so we should probably do so."
        Ry look "Are you sure? I don’t feel so safe about whoever “us” is..."
        c "I don’t think we have much of a choice, Remy."
        Ry "I suppose we don’t. Let’s just get this over with."

        hide remy with dissolve

        play sound "fx/telstart.ogg"

        m "I carefully entered the co-ordinates into the portal and placed the note on the ground. It took several minutes, but the portal did eventually start, sending the note back to where it came from."

        $ renpy.pause (1.5)
        show remy normal with dissolve

        c "And it’s done."
        Ry "Let’s hope that nothing bad happens because of it."
        c "Agreed."

        $ renpy.pause (3.0)

        c "And it seems that it's almost midday. Logan is going to be {i}really{/i} angry with us for being so late."
        Ry "In that case, we should really get going now."
        c "Yeah. Let's go."

        scene black with dissolveslow
        $ renpy.pause (7.0)


        $ _game_menu_screen = None
        $ renpy.block_rollback()

        show extra1 at Pan ((450, 0), (540,0), 25.0)
        show koltldcredits1 at right
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at right with dissolvemed
        show koltldcredits2 at right
        with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed

        show rezabitten at Pan ((-500, 56), (-200,0), 24.0)
        show credits1 at left
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at left with dissolvemed

        show credits2 at left with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed

        show remyapt at Pan ((0, 170), (600, 0), 24.0)
        show credits3 at right
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at right with dissolvemed

        show credits4 at right with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed




        show remysad at Pan ((-250, 326), (430, 0), 25.0)
        show credits5 at left
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at left with dissolvemed

        show credits6 at left with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed




        show cgvara at Pan ((0, 326), (1580, 0), 25)
        show credits7 at right
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at right with dissolvemed

        show credits8 at right with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed



        show cg1 at Position(xpos=0.8, xanchor='center')
        show credits9 at left
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at left with dissolvemed

        show credits10 at left with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed

        scene logo with dissolvemed

        $ renpy.pause (9.0)

        scene black with dissolvemed

        stop music fadeout 2.0

        $ renpy.pause (4.0)


        $ persistent.kol_tld_endingc = True
        $ persistent.kol_tld_ending_achieved = True


        play sound "fx/system3.wav"
        s "Ending achieved: [[C]ommunication through Times, or Ending C for short."

        play sound "fx/system.wav"
        s "Congratulations! You have seen The Last Dragon's neutral ending! I wonder what happened with the portal..."

        play sound "fx/system3.wav"
        s "Feel free to try and get another ending, ideally a better one."

        jump ml_main_menu


    "Let’s keep the note to ourselves.":
        $ renpy.pause (1.5)

        c "I’ll have to admit, I don’t like that ominous message of something hurting us if we try to find out whatever this actually is."
        c "I think that we should just keep the note to ourselves."
        Ry normal "I agree. I don’t think that it’s safe to continue with whatever this is."
        Ry "Are you going to destroy the note?"
        c "I think that I’m going to keep it. At least for now."
        Ry "I see."

        $ renpy.pause (3.0)

        Ry "Look, [player_name]. It seems that we spent quite a bit of time here. If we don’t hurry, then Logan isn’t going to be happy with us."
        c "Alright, then. Let’s go."



        scene black with dissolveslow
        $ renpy.pause (7.0)


        $ _game_menu_screen = None
        $ renpy.block_rollback()

        show extra1 at Pan ((450, 0), (540,0), 25.0)
        show koltldcredits1 at right
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at right with dissolvemed
        show koltldcredits2 at right
        with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed

        show rezabitten at Pan ((-500, 56), (-200,0), 24.0)
        show credits1 at left
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at left with dissolvemed

        show credits2 at left with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed

        show remyapt at Pan ((0, 170), (600, 0), 24.0)
        show credits3 at right
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at right with dissolvemed

        show credits4 at right with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed




        show remysad at Pan ((-250, 326), (430, 0), 25.0)
        show credits5 at left
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at left with dissolvemed

        show credits6 at left with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed




        show cgvara at Pan ((0, 326), (1580, 0), 25)
        show credits7 at right
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at right with dissolvemed

        show credits8 at right with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed



        show cg1 at Position(xpos=0.8, xanchor='center')
        show credits9 at left
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at left with dissolvemed

        show credits10 at left with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed

        scene logo with dissolvemed

        $ renpy.pause (9.0)

        scene black with dissolvemed

        stop music fadeout 2.0

        $ renpy.pause (4.0)

        $ persistent.kol_tld_endingc = True
        $ persistent.kol_tld_ending_achieved = True


        play sound "fx/system3.wav"
        s "Ending achieved: [[C]ommunication through Times, or Ending C for short."

        play sound "fx/system.wav"
        s "Congratulations! You have seen The Last Dragon's neutral ending! I wonder what happened with the portal..."

        play sound "fx/system3.wav"
        s "Feel free to try and get another ending, ideally a better one."

        jump ml_main_menu



#Alright, this is for all you knowledge seeking nerds out there.
#This is what happened:
#TTT stands for Timeline Travel Test
#What this ending is essentialy about, is that Izumi, with the help of System maybe, found a way to connect to alternate timelines
#I say that System helped her, since System has shown some evidence of timeline manipulation (see Bryce death scene)
#All I did was expand on that concept to say that Izumi has found a way to come in contact with different versions of you, the player
#Thus, the test is number 47, as this is her 47th attempt to try and send something through to any timeline; it just happened to end up in yours
#What will Izumi do? What are her plans if this proves to be a success? Idk you make your own headcanon
#I'm too lazy to expand upon this idea...
#Hmmmmmm...
#Maybe this is what the necklace in the secret ending was for...





label tld_EndingD:

#Look at this sad, pathetic attempt to try and create a sad ending. If only I knew how to write depression...

$ save_name = (_("TLD - Ending D"))

$ renpy.pause (2.0)
scene kolmchousenight at Pan((0,80),(0,80),5.0) with dissolveslow
play music "fx/rainloop_kol.ogg" fadein 1.0

m "I woke up a few hours later with the sounds of heavy rain and wind keeping me awake. I wondered for a while whether Logan would be okay, and if he managed to get home before the storm hit us."
m "After struggling to fall asleep again, I decided to wander around the house, waiting for the opportunity to feel tired again."
m "However, when I reached the living room, Remy wasn’t sleeping on the couch."
c "(Wait, where did Remy go?)"
m "I looked around to see if I could find Remy, but he was nowhere to be found. That was when I noticed a crucial detail."
m "The front door was slightly open."

stop music fadeout (1.0)

m "A sense of panic washed over me as I wondered where Remy could have gone. I spent several minutes trying to think of any possibilities, until I found the most likely solution."

$ renpy.pause (1.0)
play music "mx/judgement_kol.ogg" fadein 1.0

c "The portal!"

if kol_tld_remytherapy == True:
    m "It made sense. Remy felt a hefty sense of guilt, so it was only logical that he tried to make things right by trying to go back in time, despite my attempted warnings of what may happen."

else:
    m "Somehow, I had a feeling that Remy might have wanted to go back in time to prevent something bad from happening. Was it to prevent Amelia’s death? Or perhaps was it to prevent something else?"


m "Regardless, there was only one thing that needed to be done: I must go to the portal to try and prevent Remy from going back in time."

$ renpy.pause (1.0)
scene kolcitynight at Pan ((0, 360), (0, 0), 4.0) with dissolve

m "I rushed outside into the rain, hoping to arrive at the portal before it’s too late. I could feel the large raindrops hitting my body as I ran as fast as I could while my clothes started to get heavier and heavier."
m "It wasn’t long before I reached the portal. With tired legs, I looked around for any trace of Remy, but none could be found."

$ renpy.pause (2.0)

m "It seems that I was too late. Remy had gone back in time."
m "I decided to look at the portal logs to confirm whether he actually used the portal, however, as making rash conclusions can only cause problems if I happened to be wrong."

play sound "fx/telbuttons.ogg"
$ renpy.pause (2.0)

m "However, upon inspecting the logs, I didn’t find anything that showed the portal being used."
m "Only a failed attempt to activate it roughly fifty minutes ago."
c "(So, Remy didn’t manage to go back in time. But why? What prevented him from doing so?)"
m "Ultimately, I decided that going to Logan would be my best option to find Remy."

$ renpy.pause (4.0)
scene kolloganoutnight at Pan ((0, 0), (0, 250), 5.0) with fade

m "It took quite some time, but eventually I reached Logan’s house. I knocked as loud as I could, hoping that Logan would still be awake at this hour."

play sound "fx/knocking2.ogg"
$ renpy.pause (4.0)
queue sound "fx/door/door_open.wav"
$ renpy.pause (2.0)

m "Unsurprisingly, he was."

show logan tsurprised dk with dissolvemed

Lg "[player_name]? What the heck are you doing here?"
Lg "And {i}why{/i} are you soaked in your pyjamas?"
c "I’ll explain later. Let’s just get inside for now. I don’t want to be in the rain for any more than it is necessary."
Lg tserious dk "Fine. Come in."

scene kolloganhousenight at Pan ((0, 220), (0,360), 3.0) with dissolveslow
$ renpy.pause (5.0)
show logan tserious dk with dissolve

Lg "Alright, now explain yourself."

$ renpy.pause (2.0)
Lg "*sigh*"
Lg "And to think that I almost got a decent night’s sleep in."
c "Remy is missing."

show logan tsurprised dk with dissolve

Lg "{i}WHAT?!{/i}" with Shake ((0, 0, 0, 0), 1.5, dist=18)
Lg "What do you mean Remy is missing?"
c "Well, Remy simply wasn’t at home. I noticed that the door was open, which led me to believe that he wandered around the city, despite the heavy rains and wind."
c "I figured that maybe Remy went to the portal, and I was right. {w}Sort of."
c "According to the logs, he tried to use the portal almost an hour ago, but for some reason it didn’t activate. I went directly to you to let you know so that we could figure something out."

show logan tannoyed dk with dissolve

m "Logan seemed to grumble something under his breath, then tried to think about the information I gave him."
Lg tserious dk "Why would Remy want to use the portal, though? From what I know about him, he doesn’t seem to be the type to try and go back to his world, especially after everything had been destroyed."
c "It’s a complicated story; one that would take too long to explain now."
Lg "So be it."
Lg tannoyed dk "Hmmm..."

$ renpy.pause (2.0)

Lg tserious dk "I’m at a complete loss, [player_name]. I really am."
Lg "I don’t know him as well as you do, so any behaviours he might have that could have influenced him in some way are lost to me. You’re essentially the best lead we have."

if kol_tld_wtpchosen == True:
    Lg "The only recommendation I could give is to search the city. Perhaps he could be at the water treatment plant to try and look for something, but that’s just a wild guess."

else:
    Lg "The only recommendation I could give is to search the city. Perhaps he could be at the factory to try and look for something, but that’s just a wild guess."


Lg tannoyed dk "The fact that he went to the portal, however, just throws a spanner in the works."
c "Will you help me look for him?"
Lg "Well, since you already ruined my opportunity for some good sleep, I might as well try to help you out."
Lg tserious dk "You’ll have to ride with me on my motorcycle, though. The faster we reach our destination, the better the odds at finding something that could help us find Remy."
c "Okay."

hide logan with dissolve

if kol_tld_wtpchosen == True:

    play sound "fx/motorcycleaccelerate_kol.wav"

    scene black with fade
    $ renpy.pause (2.0)

    m "We climbed on Logan’s motorcycle and drove as fast as we could to the water treatment plant. Much to my dismay, Logan only had a single helmet, which caused me to be constantly bombarded by raindrops in my eyes."

    scene kolwtpoutnight at Pan((0,0),(0,80),4.0) with dissolve
    $ renpy.pause (5.0)
    stop sound fadeout (1.0)

    m "We did reach our destination at a relatively fast pace, even if I felt like I had soaked up all of the storm’s rain."

    show logan tnormal dk with dissolve

    Lg "Alright, I’m going to check the inner parts of the water treatment plant. You can check the outer parts, as well as all the entrances. I’ll shout if I find anything."
    c "Got it. I’ll do the same. Good luck, Logan."
    Lg tserious dk "Again with the luck, damn it..."
    c "I was just trying to-{w=0.7}{nw}"
    Lg "Annoy me? Because you certainly got that going for you."

    $ renpy.pause (2.0)

    Lg "*sigh*"
    Lg "I really need to sleep more."

    scene kolwtp3night at Pan ((0, 0), (0, 127), 4.0) with dissolve
    $ renpy.pause (2.0)

    m "I started looking for anything that might indicate Remy’s whereabouts, but the darkness hindered my progress."

    $ renpy.pause (1.0)
    scene kolwtp1night at Pan ((0, 0), (0, 0), 4.0) with dissolve
    $ renpy.pause (2.0)

    m "As I wandered through the building, I could see that most of the infrastructure still survived the storm thus far, but whether they will still be here tomorrow morning remains to be seen."
    m "After searching for what felt like hours, I started to lose hope of finding Remy here. Suddenly, I heard a distant voice coming from the central facility."
    Lg "[player_name]! Over here!" with Shake ((0, 0, 0, 0), 1.5, dist=10)

    stop music fadeout (2.0)
    $ renpy.pause (1.0)
    scene kolwtp4night at Pan ((0, 0), (0, 0), 4.0) with dissolve
    $ renpy.pause (2.0)

    m "I ran through the halls until I saw Logan. He looked far more distraught than I would have expected, having an almost melancholic expression on his face."

    show logan tserious dk with dissolve
    play music "mx/moving_on_kol.ogg" fadein 1.5

    Lg "So, I didn’t find Remy here, just like I suspected. However, I found something far worse."
    Lg "..."
    Lg "I think this is meant for you, [player_name]."

    hide logan with dissolve

    m "Logan handed me a small note while avoiding my eyes."

    show logan tserious dk with dissolve

    Lg "I don’t have anything to say. It’s just that..."
    Lg "..."
    Lg "Fucking hell, I feel sorry for the poor guy. I just hope he’ll be alright, wherever he might be." #WOAH! The F-Bomb has been dropped! I repeat, the F-Bomb has been dropped!

    hide logan with dissolve

    m "I opened the note and started to read. The barely legible handwriting with almost no light made the note extremely hard to read, but I somehow managed to make out what it said."

    $ renpy.pause (2.0)

    c "{i}By the time you have found this note, I will be long gone. I know that this is sudden, but I just can’t continue to drag you all down. If I stay here any longer, then I am going to be the reason that this city will fall.{/i}"
    c "{i}All the hard work you and Logan put in so far is something that amazes me. I can only imagine all the progress the both of you would be able to make if this useless dragon stopped getting in the way. All I ever do is make everything worse.{/i}"
    c "{i}You have a lot of potential, [player_name]. As a leader, as an ambassador, and as a close friend. It would be better for all of us if I left. Mind you, this isn’t something that I want to do, especially after everything you did for me. However, the things I have done and will most likely keep doing are more than enough reasons for me to be kicked out of the city.{/i}"
    c "{i}I wish you and Logan the best of luck. Hopefully, one day, you’ll be able to find somebody actually useful to help you out instead of dragging you down and getting in the way. Like me.{/i}"
    c "{i}I hope that you can forgive me for the way I have repaid your kindness.{/i}"
    c "{i}Goodbye, [player_name]. I’ll miss you.{/i}"
    c "{i}-Remy{/i}"

    $ renpy.pause (3.0)

    show logan tserious dk with dissolveslow

    Lg "Are you alright? No offense, but you look horrible."

    menu:
        "I don’t know.":
            $ renpy.pause (1.0)

            Lg "The we’re experiencing the same emotions right now."
            Lg "I didn’t think that I could ever feel sad for someone I have barely known for a few days, but here I am."
            Lg "Let’s just hope that Remy is better off now."


        "I hope so.":
            $ renpy.pause (1.0)

            Lg tannoyed dk "That’s an interesting way of thinking, [player_name]."
            Lg "To hope that you’ll feel better when you just experienced something horrible rarely brings any comfort, especially in a scenario like this."
            Lg tserious dk "Just... don’t end up lying to yourself. It will only make things worse."


        "I don’t want to talk about it right now.":
            $ renpy.pause (1.0)

            Lg "That’s fair enough, I suppose."
            Lg "Just remember to let it out when you're ready, as bottling emotions up only causes more problems down the road."



    c "I don’t think that you’re helping, Logan."
    Lg "I know. Helping people with emotional problems isn’t really my specialty."
    Lg "In any case, I think that we had enough for tonight."
    Lg "Let’s leave this for tomorrow and see what we can come up with."
    Lg "For now, come with me. I’ll take you to your home."


    scene black with dissolveslow
    $ renpy.pause (7.0)



    $ _game_menu_screen = None
    $ renpy.block_rollback()

    show extra1 at Pan ((450, 0), (540,0), 25.0)
    show koltldcredits1 at right
    with dissolvemed

    $ renpy.pause (10.0)

    show black2 at right with dissolvemed
    show koltldcredits2 at right
    with dissolvemed

    $ renpy.pause (10.0)

    scene black with dissolvemed

    show rezabitten at Pan ((-500, 56), (-200,0), 24.0)
    show credits1 at left
    with dissolvemed

    $ renpy.pause (10.0)

    show black2 at left with dissolvemed

    show credits2 at left with dissolvemed

    $ renpy.pause (10.0)

    scene black with dissolvemed

    show remyapt at Pan ((0, 170), (600, 0), 24.0)
    show credits3 at right
    with dissolvemed

    $ renpy.pause (10.0)

    show black2 at right with dissolvemed

    show credits4 at right with dissolvemed

    $ renpy.pause (10.0)

    scene black with dissolvemed




    show remysad at Pan ((-250, 326), (430, 0), 25.0)
    show credits5 at left
    with dissolvemed

    $ renpy.pause (10.0)

    show black2 at left with dissolvemed

    show credits6 at left with dissolvemed

    $ renpy.pause (10.0)

    scene black with dissolvemed




    show cgvara at Pan ((0, 326), (1580, 0), 25)
    show credits7 at right
    with dissolvemed

    $ renpy.pause (10.0)

    show black2 at right with dissolvemed

    show credits8 at right with dissolvemed

    $ renpy.pause (10.0)

    scene black with dissolvemed



    show cg1 at Position(xpos=0.8, xanchor='center')
    show credits9 at left
    with dissolvemed

    $ renpy.pause (10.0)

    show black2 at left with dissolvemed

    show credits10 at left with dissolvemed

    $ renpy.pause (10.0)

    scene black with dissolvemed

    scene logo with dissolvemed

    $ renpy.pause (9.0)

    scene black with dissolvemed

    stop music fadeout 2.0

    $ renpy.pause (4.0)


    $ persistent.kol_tld_endingd = True
    $ persistent.kol_tld_ending_achieved = True



    play sound "fx/system3.wav"
    s "Ending achieved: [[D]etriment to All, or Ending D for short."

    play sound "fx/system.wav"
    s "You have now seen The Last Dragon's bad ending! Let's hope that Remy is safe."

    play sound "fx/system3.wav"
    s "Feel free to try and get another ending, hopefully a better one."

    jump ml_main_menu



else:
    play sound "fx/motorcycleaccelerate_kol.wav"

    scene black with fade
    $ renpy.pause (2.0)

    m "We climbed on Logan’s motorcycle and drove as fast as we could to the factory. Much to my dismay, Logan only had a single helmet, which caused me to be constantly bombarded by raindrops in my eyes."

    scene kolfactoryoutnight at Pan((0,0),(0,80),4.0) with dissolve
    $ renpy.pause (5.0)
    stop sound fadeout (1.0)

    m "We did reach our destination at a relatively fast pace, even if I felt like I had soaked up all of the storm’s rain."

    show logan tnormal dk with dissolve

    Lg "Alright, I’m going to check the inner parts of the factory. You can check the outer parts, as well as all the entrances. I’ll shout if I find anything."
    c "Got it. I’ll do the same. Good luck, Logan."
    Lg tserious dk "Again with the luck, damn it..."
    c "I was just trying to-{w=0.7}{nw}"
    Lg "Annoy me? Because you certainly got that going for you."

    $ renpy.pause (2.0)

    Lg "*sigh*"
    Lg "I really need to sleep more."

    scene kolfactory3night at Pan ((0, 0), (0, 127), 4.0) with dissolve
    $ renpy.pause (2.0)

    m "I started looking for anything that might indicate Remy’s whereabouts, but the darkness hindered my progress."

    $ renpy.pause (1.0)
    scene kolfactory2night at Pan ((0, 0), (0, 0), 4.0) with dissolve
    $ renpy.pause (2.0)

    m "As I wandered through the building, I could see that most of the infrastructure still survived the storm thus far, but whether they will still be here tomorrow morning remains to be seen."
    m "After searching for what felt like hours, I started to lose hope of finding Remy here. Suddenly, I heard a distant voice coming from the central facility."
    Lg "[player_name]! Over here!" with Shake ((0, 0, 0, 0), 1.5, dist=10)

    stop music fadeout (2.0)
    $ renpy.pause (1.0)
    scene kolfactory1night at Pan ((0, 0), (0, 0), 4.0) with dissolve
    $ renpy.pause (2.0)

    m "I ran through the halls until I saw Logan. He looked far more distraught than I would have expected, having an almost melancholic expression on his face."

    show logan tserious dk with dissolve
    play music "mx/moving_on_kol.ogg" fadein 1.5

    Lg "So, I didn’t find Remy here, just like I suspected. However, I found something far worse."
    Lg "..."
    Lg "I think this is meant for you, [player_name]."

    hide logan with dissolve

    m "Logan handed me a small note while avoiding my eyes."

    show logan tserious dk with dissolve

    Lg "I don’t have anything to say. It’s just that..."
    Lg "..."
    Lg "Fucking hell, I feel sorry for the poor guy. I just hope he’ll be alright, wherever he might be." #WOAH! The F-Bomb has been dropped! I repeat, the F-Bomb has been dropped!

    hide logan with dissolve

    m "I opened the note and started to read. The barely legible handwriting with almost no light made the note extremely hard to read, but I somehow managed to make out what it said."

    $ renpy.pause (2.0)

    c "{i}By the time you have found this note, I will be long gone. I know that this is sudden, but I just can’t continue to drag you all down. If I stay here any longer, then I am going to be the reason that this city will fall.{/i}"
    c "{i}All the hard work you and Logan put in so far is something that amazes me. I can only imagine all the progress the both of you would be able to make if this useless dragon stopped getting in the way. All I ever do is make everything worse.{/i}"
    c "{i}You have a lot of potential, [player_name]. As a leader, as an ambassador, and as a close friend. It would be better for all of us if I left. Mind you, this isn’t something that I want to do, especially after everything you did for me. However, the things I have done and will most likely keep doing are more than enough reasons for me to be kicked out of the city.{/i}"
    c "{i}I wish you and Logan the best of luck. Hopefully, one day, you’ll be able to find somebody actually useful to help you out instead of dragging you down and getting in the way. Like me.{/i}"
    c "{i}I hope that you can forgive me for the way I have repaid your kindness.{/i}"
    c "{i}Goodbye, [player_name]. I’ll miss you.{/i}"
    c "{i}-Remy{/i}"

    $ renpy.pause (3.0)

    show logan tserious dk with dissolveslow

    Lg "Are you alright? No offense, but you look horrible."

    menu:
        "I don’t know.":
            $ renpy.pause (1.0)

            Lg "The we’re experiencing the same emotions right now."
            Lg "I didn’t think that I could ever feel sad for someone I have barely known for a few days, but here I am."
            Lg "Let’s just hope that Remy is better off now."


        "I hope so.":
            $ renpy.pause (1.0)

            Lg tannoyed dk "That’s an interesting way of thinking, [player_name]."
            Lg "To hope that you’ll feel better when you just experienced something horrible rarely brings any comfort, especially in a scenario like this."
            Lg tserious dk "Just... don’t end up lying to yourself. It will only make things worse."


        "I don’t want to talk about it right now.":
            $ renpy.pause (1.0)

            Lg "That’s fair enough, I suppose."
            Lg "Just remember to let it out when you're ready, as bottling emotions up only causes more problems down the road."



    c "I don’t think that you’re helping, Logan."
    Lg "I know. Helping people with emotional problems isn’t really my specialty."
    Lg "In any case, I think that we had enough for tonight."
    Lg "Let’s leave this for tomorrow and see what we can come up with."
    Lg "For now, come with me. I’ll take you to your home."


    scene black with dissolveslow
    $ renpy.pause (7.0)



    $ _game_menu_screen = None
    $ renpy.block_rollback()

    show extra1 at Pan ((450, 0), (540,0), 25.0)
    show koltldcredits1 at right
    with dissolvemed

    $ renpy.pause (10.0)

    show black2 at right with dissolvemed
    show koltldcredits2 at right
    with dissolvemed

    $ renpy.pause (10.0)

    scene black with dissolvemed

    show rezabitten at Pan ((-500, 56), (-200,0), 24.0)
    show credits1 at left
    with dissolvemed

    $ renpy.pause (10.0)

    show black2 at left with dissolvemed

    show credits2 at left with dissolvemed

    $ renpy.pause (10.0)

    scene black with dissolvemed

    show remyapt at Pan ((0, 170), (600, 0), 24.0)
    show credits3 at right
    with dissolvemed

    $ renpy.pause (10.0)

    show black2 at right with dissolvemed

    show credits4 at right with dissolvemed

    $ renpy.pause (10.0)

    scene black with dissolvemed




    show remysad at Pan ((-250, 326), (430, 0), 25.0)
    show credits5 at left
    with dissolvemed

    $ renpy.pause (10.0)

    show black2 at left with dissolvemed

    show credits6 at left with dissolvemed

    $ renpy.pause (10.0)

    scene black with dissolvemed




    show cgvara at Pan ((0, 326), (1580, 0), 25)
    show credits7 at right
    with dissolvemed

    $ renpy.pause (10.0)

    show black2 at right with dissolvemed

    show credits8 at right with dissolvemed

    $ renpy.pause (10.0)

    scene black with dissolvemed



    show cg1 at Position(xpos=0.8, xanchor='center')
    show credits9 at left
    with dissolvemed

    $ renpy.pause (10.0)

    show black2 at left with dissolvemed

    show credits10 at left with dissolvemed

    $ renpy.pause (10.0)

    scene black with dissolvemed

    scene logo with dissolvemed

    $ renpy.pause (9.0)

    scene black with dissolvemed

    stop music fadeout 2.0

    $ renpy.pause (4.0)


    $ persistent.kol_tld_endingd = True
    $ persistent.kol_tld_ending_achieved = True


    play sound "fx/system3.wav"
    s "Ending achieved: [[D]etriment to All, or Ending D for short."

    play sound "fx/system.wav"
    s "You have now seen The Last Dragon's bad ending! Let's hope that Remy is safe."

    play sound "fx/system3.wav"
    s "Feel free to try and get another ending, hopefully a better one."

    jump ml_main_menu




label tld_EndingE:

#Please forgive me for what you are about to witness...

$ save_name = (_("TLD - Ending E"))

$ renpy.pause (2.0)
scene kolmchousenight at Pan((0,80),(0,80),5.0) with dissolveslow
play music "fx/rainloop_kol.ogg" fadein 1.0
$ renpy.pause (4.0)

m "I woke up in the middle of the night, somehow fully rested enough for another day’s work. I tried to fall back to sleep, but my body simply wouldn’t let me. In the end, I decided that I should grab a snack, figuring that it would help me to potentially go back to sleep."
m "I walked quietly around the house, trying to reach the kitchen without waking Remy up. Eventually I reached the pantry, only to find that there wasn’t anything light to eat; only ingredients for a hefty meal."

stop music fadeout (2.0)
m "Disappointed, I slowly wandered into the living room to check on Remy. However, Remy was nowhere to be found."

play music "mx/martyr_kol.ogg" fadein 1.0

c "Remy? Are you there?"

$ renpy.pause (2.0)

m "No response came."
m "I tried calling out for Remy once more, but nothing happened. I decided to look around the house for him, as I figured that maybe, just maybe, he was simply sleeping in another room."
m "That was when, out of the corner of my eye, I saw that there was a huge puddle of water at the front door."
c "(Why is the floor here wet? Last time I checked, there weren’t any leaks that-{w=1.3}{nw})"
m "A terrible realisation hit me as I pieced together what happened. It seemed that Remy left the house to go outside in the ongoing storm. I tried to think of any possibilities where Remy could have wandered, but nothing came."

$ renpy.pause (2.0)

c "Wait..."
c "The portal!"
m "There was a good chance that Remy could have potentially used the portal to try and travel back in time, or to try and see whether his world still existed."

if kol_tld_remytherapy == False:

    if kol_tld_martinaccepted == False:
        m "A sense of dread started to linger over me as I considered this possibility. What would happen if Remy successfully used the portal? Where would he go? What would Logan think of all this?"

    else:
        m "A sense of dread started to linger over me as I considered this possibility. What would happen if Remy successfully used the portal? Where would he go? What would Logan and Martin think of all this?"

else:

    if kol_tld_martinaccepted == False:
        m "A sense of dread started to linger over me as I considered this possibility. What would happen if Remy successfully used the portal, despite my warnings? Where would he go? What would Logan think of all this?"

    else:
        m "A sense of dread started to linger over me as I considered this possibility. What would happen if Remy successfully used the portal, despite my warnings? Where would he go? What would Logan and Martin think of all this?"



m "All questions that would have to be answered later."

$ renpy.pause (1.0)
scene kolcitynight at Pan ((0, 360), (0, 0), 4.0) with dissolve

m "I rushed outside while still in my nightwear straight into the rain. At first, a strong sense of discomfort swept over me as I felt the raindrops being absorbed into my clothes, but the urgency of this situation didn’t allow me to complain."

$ renpy.pause (3.0)

m "It took me several minutes of constantly struggling against the wind trying to push me back, but I did eventually reach the portal."

$ renpy.pause (1.0)

m "Remy wasn’t there."

$ renpy.pause (1.0)

c "(Wait. Maybe Remy hasn’t left yet. I should probably check the logs.)"

play sound "fx/telbuttons.ogg"
$ renpy.pause (2.0)

m "I booted the portal partially so that I could have access to the portal logs. At first, all I found were entries of the humans exchanging letters to the dragons, then me and Reza’s departure. After far too much scrolling, I came across a peculiar entry."
m "There was a failed attempt to use the portal an hour and a half ago. Upon further inspection, I found that somebody tried to activate the portal, but couldn’t get it operational due to something not responding in the internals."
c "(I’ll have to let Logan know of this. Maybe he’ll be able to fix whatever happened to the portal.)"
c "(After all, he fixed damn near everything so far, so why not a super sophisticated time machine?)" #I mean, Logan does have an infinite amount of plot armour, so... Nah, jk jk... Unless...

$ renpy.pause (2.0)

m "I kept searching for any more information that might indicate where Remy could be, but I couldn’t find anything. I started to lose hope until I saw yet another crucial detail from the corner of my eye."
m "There was a hole in the mud that was shaped like a dragon’s foot. I looked to see if I could see any more, but only a few that weren’t completely destroyed by the rain still remained."
m "Luckily, they were more than enough footprints to give me a rough idea as to where they led. I decided that since I had no other leads, I should follow the trail to see where it would take me."

scene black with fade
play sound "fx/steps/steps.ogg"
$ renpy.pause (6.5)
scene kolremyhouseout at Pan ((0, 60), (0, 360), 5.0) with dissolveslow
stop sound

m "It took me some time trying to make sure that I was on the correct path, but I did eventually end up at an abandoned house that was secluded from the rest of the city. "
m "Since the trail broke here, I figured that Remy might have either still been inside, or took off to the skies from here."

play sound "fx/door/opendoorslow.ogg"
$ renpy.pause (2.0)
scene kolremyhouse at Pan ((0, 260), (0, 160), 6.0) with dissolveslow

m "I slowly opened the door, and with a loud creak, I entered the house. I found that the interior was completely dark, except for some moonlight that shone through the windows."
c "Remy? Are you here?"

stop music fadeout (6.5)
$ renpy.pause (2.0)

m "Still no response."
m "I explored the house even further, hoping to see any sign of Remy. Eventually, I found a room slightly large in size with a strange object in front of me. "
m "I stepped closer until what little moonlight was available to me showed me what the object was."

play music "mx/day_10_kol.ogg" fadein (2.0)

c "No..."
c "NO!"
c "REMY!" with Shake ((0, 0, 0, 0), 0.8, dist=25)

$ remydead = True

show kolremye at Pan ((250, 324), (250, 0), 8.0) with fade
$ renpy.pause (5.0)
scene black with dissolveslow
scene kolremyhouse at Pan ((0, 160), (0, 160), 0.0)

m "I immediately rushed towards Remy and tried to get him down. Eventually, I was able to loosen the rope just enough so that he could be set free."

play sound "fx/impact.wav"

m "Upon doing so, he fell limply towards the ground with a loud thud."
m "I checked to see if there were any signs of life left in him."

$ renpy.pause (3.0)

m "There were none."

$ renpy.pause (1.0)

c "Remy..."
c "Forgive me for not being there during your last moments..."
m "I looked around to see if there was anything that Remy might have left me. Eventually, I found a small notebook on a nearby dresser. I checked the first page and found the confirmation I was looking for."
m "Whatever was written down here was meant for me. I started to read the barely legible handwriting found within in what little light was available to me."

stop music fadeout (2.0)

scene black with dissolveslow
$ renpy.pause (2.0)
nvl clear
window show

play music "mx/left_behind_kol.ogg" fadein 1.0

#THIS IS LITERAL HELL AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA MAKE IT STOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPPP

n "To [player_name], the one who showed me what hope felt like and the reason I lasted as long as I did."
n "I’m so, so sorry that you had to find me like this, [player_name]. I really am. I wished that I could say a proper goodbye, but I didn’t want to hurt you even more than I already have."

if kol_tld_remytherapy == True:
    n "I came to the conclusion that since everything I did only hurt everybody’s chances at rebuilding the city, I only did the most logical thing left for a leech like me. Now, you don’t have to worry about a pathetic failure only disappointing everybody even further."

else:
    n "I realised a few days ago that I was the one responsible for the death of everybody back in my world, as without the generators I took, nobody could have ever stood a chance. And even if I didn’t take them, I couldn’t negotiate with the other humans to try and resolve this conflict, resulting in me needing to abandon everybody to get you."

    window hide
    nvl clear
    window show

    n "I know that I can’t try to help you anymore, but I believe that this is for the better. A monster like me can’t ever hope to try and make things right. Especially not after I caused everybody and everything I knew to burn to the ground."
    n "Everything was always my fault, even if I didn’t notice it at the time. First with me causing Amelia’s death by not being there for her in her greatest time of need; all because of my selfish desires to keep our relationship a secret."
    n "Then with Emera and how I always managed to damage priceless artefacts while I was working. She was right about everything she said to me. How {i}could{/i} I even have worked for the council when all I did was break everything I touched?"

    window hide
    nvl clear
    window show

    n "Next it was with everybody at home and how they believed in me. I always wondered why the people that always laughed at me suddenly looked up to me as a sort of saviour. Not that it matters. Now, they’re gone. As is everybody else."
    n "The same could have been said with Martin. For all I know, he and his group are most likely dead. And what did I do? I simply let them run away instead of trying to help them even further. I caused even more deaths, as if an entire civilisation wasn’t enough."
    n "And then there’s you."


window hide
nvl clear
window show

n "I really hate leaving you here alone, but it was the only option. I am a walking hazard, waiting for any opportunity to cause immense pain to you when you least expect it. Any sane person would already have left me on my own."
n "And yet you still stood at my side."
n "After everything that happened, both here and back home, you never gave up on me. You helped me to realise that maybe there was still a reason to continue living. You are such an amazing person for showing enough interest in me to not only tolerate me, but to become one of the closest people I ever knew. I don’t think that I’ll ever understand why you kept holding on to a lost cause like me."

window hide
nvl clear
window show

n "This makes everything so much harder for me, however, as I’m constantly torn from whether to continue living and getting in everyone’s way, or to do what I feared the most and throw away all the hard work you did for me. I guess that if you’re reading this, then you already know what happened."
n "I hope that you could understand my decision, but if you don’t, then that’s alright too. I don’t want to cause you to worry about me any further. Maybe you’ll eventually understand why I did it. If you actually do, however, then... I’m sorry."
n "Please, don’t let me weigh you down too much. The last thing I want is to continue being a burden in death. I don’t know where I’ll be going now, but just know that I will be watching over you, wherever I’ll be. It’s the least I could do after everything you did for me."

window hide
nvl clear
window show

#THE FEELS OF THIS AAAAAAAAAAAAAAAAAAASFPOHEPWAINDFPIGHZXHKHQIOIHZVFOUVHZCGOIUATRRETGKFG

n "Now, I hope to rejoin with everybody else. Once again, I hate to leave you alone, but this is for the better. I think that I’m probably going to be berated by everyone else, but at least I’ll be reunited with Amelia. I’ll even tell her everything about you! I’m sure she’ll want to meet you someday, when your time has finally come."
n "I left a little something in the bottom most drawer for you as a token of how great of a person you were to me. Take it if you will; I’m not going to force you. "
n "Thank you, [player_name]. For everything. Now I can rest easy, knowing that my death has now repaid my debt for all the pain and suffering I have caused."

window hide
nvl clear

stop music fadeout (2.0)
scene kolremyhouse at Pan ((0, 160), (0, 160), 0.0)
$ renpy.pause (3.0)
play music "mx/prayer_kol.ogg" fadein 1.0

m "I slowly put the small notebook down while processing what Remy said. A sense of guilt started to wash over me as I tried to comprehend and organise my thoughts."
m "After some time, I decided that I should probably check the drawer that Remy mentioned and save the thinking for later. Upon opening it, I found a small note, as well as Remy’s tie."
m "I picked up the note first and started to read, dreading what it may say."
c "{i}Just like how Amelia gave this tie to me so that I could be reminded of her, I give my tie to you as a reminder of me.{/i}"
c "{i}Wear it proudly, [player_name]. And please, each time you think of it, remember me.{/i}"
c "{i}Don’t let my memory be forgotten. Please. {/i}"

$ renpy.pause (2.0)

m "Remy’s last words haunted me for a bit as I decided what I had to do now."

menu:
    "[[Take Remy’s tie.]":
        $ renpy.pause (1.8)

        m "I decided to honour Remy’s last wishes and took the tie with me. I put the tie around my neck and wore it proudly, just like Remy asked."
        m "I prepared to leave the house, taking Remy’s notes with me as a reminder of everything that had happened. I looked at Remy for one final time as sorrow started to overcome me."

        scene black with dissolveslow
        $ renpy.pause (1.0)

        m "I left the house and walked into the stormy weather, unsure of what to do now."

        $ renpy.pause (6.0)


        $ _game_menu_screen = None
        $ renpy.block_rollback()

        show extra1 at Pan ((450, 0), (540,0), 25.0)
        show koltldcredits1 at right
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at right with dissolvemed
        show koltldcredits2 at right
        with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed

        show rezabitten at Pan ((-500, 56), (-200,0), 24.0)
        show credits1 at left
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at left with dissolvemed

        show credits2 at left with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed

        show remyapt at Pan ((0, 170), (600, 0), 24.0)
        show credits3 at right
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at right with dissolvemed

        show credits4 at right with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed




        show remysad at Pan ((-250, 326), (430, 0), 25.0)
        show credits5 at left
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at left with dissolvemed

        show credits6 at left with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed




        show cgvara at Pan ((0, 326), (1580, 0), 25)
        show credits7 at right
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at right with dissolvemed

        show credits8 at right with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed



        show cg1 at Position(xpos=0.8, xanchor='center')
        show credits9 at left
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at left with dissolvemed

        show credits10 at left with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed

        scene logo with dissolvemed

        $ renpy.pause (9.0)

        scene black with dissolvemed

        stop music fadeout 2.0

        $ renpy.pause (4.0)


        $ persistent.kol_tld_endinge = True
        $ persistent.kol_tld_ending_achieved = True


        play sound "fx/system3.wav"
        s "Ending achieved: [[E]xtinction of Dragonkind, or Ending E for short."

        play sound "fx/system.wav"
        s "You have seen the worst possible ending in The Last Dragon."

        play sound "fx/system3.wav"
        s "..."

        play sound "fx/system3.wav"
        s "I'm sorry that you had to go through that."

        play sound "fx/system3.wav"
        s "Don't worry, as the other endings are better. This I guarantee."

        play sound "fx/system3.wav"
        s "Still, if you need a bit of a break, then I understand. I'll be here, waiting for your return."

        jump ml_main_menu


    "[[Leave the house.]":
        $ renpy.pause (1.8)

        m "In the end, I decided that I should leave everything the way Remy had left it as a final homage."
        m "I prepared to leave the house and looked at Remy for one final time. Sorrow started to overcome me as I walked outside into the stormy weather."

        scene black with dissolveslow


        $ renpy.pause (6.0)

        $ _game_menu_screen = None
        $ renpy.block_rollback()

        show extra1 at Pan ((450, 0), (540,0), 25.0)
        show koltldcredits1 at right
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at right with dissolvemed
        show koltldcredits2 at right
        with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed

        show rezabitten at Pan ((-500, 56), (-200,0), 24.0)
        show credits1 at left
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at left with dissolvemed

        show credits2 at left with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed

        show remyapt at Pan ((0, 170), (600, 0), 24.0)
        show credits3 at right
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at right with dissolvemed

        show credits4 at right with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed




        show remysad at Pan ((-250, 326), (430, 0), 25.0)
        show credits5 at left
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at left with dissolvemed

        show credits6 at left with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed




        show cgvara at Pan ((0, 326), (1580, 0), 25)
        show credits7 at right
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at right with dissolvemed

        show credits8 at right with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed



        show cg1 at Position(xpos=0.8, xanchor='center')
        show credits9 at left
        with dissolvemed

        $ renpy.pause (10.0)

        show black2 at left with dissolvemed

        show credits10 at left with dissolvemed

        $ renpy.pause (10.0)

        scene black with dissolvemed

        scene logo with dissolvemed

        $ renpy.pause (9.0)

        scene black with dissolvemed

        stop music fadeout 2.0

        $ renpy.pause (4.0)

        $ persistent.kol_tld_endinge = True
        $ persistent.kol_tld_ending_achieved = True


        play sound "fx/system3.wav"
        s "Ending achieved: [[E]xtinction of Dragonkind, or Ending E for short."

        play sound "fx/system.wav"
        s "You have seen the worst possible ending in The Last Dragon."

        play sound "fx/system3.wav"
        s "..."

        play sound "fx/system3.wav"
        s "I'm sorry that you had to go through that."

        play sound "fx/system3.wav"
        s "Don't worry, as the other endings are better. This I guarantee."

        play sound "fx/system3.wav"
        s "Still, if you need a bit of a break, then I understand. I'll be here, waiting for your return."

        jump ml_main_menu

#This ending I sweaer is going to be the death of me. Why did I even create this? Why would I unleash such a horrific nightmare upon this world? This is all my fault. This entire mod is hot garbage. Why did I waste almost four months working on this? All for nothing...
#...
#Forgive me, Remy. You didn't deserve this fate.



#Ya know what? Screw it. I'm copy pasting this code in each individual ending because I can't figure out how to get the ending message to display correctly
#I'll just leave the following code as a comment in case I may need it for later

#label tld_Credits:
#Remember to start with a pause here

#scene black with dissolveslow
#
#$ renpy.pause (5.0)
#
#$ _game_menu_screen = None
#$ renpy.block_rollback()
#
#show extra1 at Pan ((450, 0), (540,0), 25.0)
#show kolcredits1 at right
#with dissolvemed
#
#$ renpy.pause (10.0)
#
#show black2 at right with dissolvemed
#show kolcredits2 at right
#with dissolvemed
#
#$ renpy.pause (10.0)
#
#scene black with dissolvemed
#
#show rezabitten at Pan ((-500, 56), (-200,0), 24.0)
#show credits1 at left
#with dissolvemed
#
#$ renpy.pause (10.0)
#
#show black2 at left with dissolvemed
#
#show credits2 at left with dissolvemed
#
#$ renpy.pause (10.0)
#
#scene black with dissolvemed
#
#show remyapt at Pan ((0, 170), (600, 0), 24.0)
#show credits3 at right
#with dissolvemed
#
#$ renpy.pause (10.0)
#
#show black2 at right with dissolvemed
#
#show credits4 at right with dissolvemed
#
#$ renpy.pause (10.0)
#
#scene black with dissolvemed
#
#
#
#
#show remysad at Pan ((-250, 326), (430, 0), 25.0)
#show credits5 at left
#with dissolvemed
#
#$ renpy.pause (10.0)
#
#show black2 at left with dissolvemed
#
#show credits6 at left with dissolvemed
#
#$ renpy.pause (10.0)
#
#scene black with dissolvemed
#
#
#
#
#show cgvara at Pan ((0, 326), (1580, 0), 25)
#show credits7 at right
#with dissolvemed
#
#$ renpy.pause (10.0)
#
#show black2 at right with dissolvemed
#
#show credits8 at right with dissolvemed
#
#$ renpy.pause (10.0)
#
#scene black with dissolvemed
#
#
#
#show cg1 at Position(xpos=0.8, xanchor='center')
#show credits9 at left
#with dissolvemed
#
#$ renpy.pause (10.0)
#
#show black2 at left with dissolvemed
#
#show credits10 at left with dissolvemed
#
#$ renpy.pause (10.0)
#
#scene black with dissolvemed
#
#scene logo with dissolvemed
#
#$ renpy.pause (9.0)
#
#scene black with dissolvemed
#
#stop music fadeout 2.0
#
#$ renpy.pause (4.0)
#
#
#if kol_tld_endinga == True:
#
#    play sound "fx/system3.wav"
#    s "Ending achieved: [[A]quiring New Hope, or Ending A for short."
#
#    play sound "fx/system.wav"
#    s "Congratulations! You have seen the best possible ending in The Last Dragon! I have a feeling that this won't be the last time that he'll want to fly with you..."
#
#    play sound "fx/system3.wav"
#    s "Feel free to try and get another ending, or just savour this moment."
#
#    jump mainmenu
#
#elif kol_tld_secretending == True:
#
#    play sound "fx/system3.wav"
#    s "Ending achieved: Extended [[A]quiring new Hope, or The Secret Ending for short."
#
#    play sound "fx/system.wav"
#    s "Congratulations! You have seen the best possible ending in The Last Dragon, as well as the secret extension! Looks like randomness has favoured you!"
#
#    play sound "fx/system3.wav"
#    s "Feel free to try and get another ending, or just savour this moment."
#
#    jump mainmenu
#
#
#elif kol_tld_endingb == True:
#
#    play sound "fx/system3.wav"
#    s "Ending achieved: [[B]ounded by Service, or Ending B for short."
#
#    play sound "fx/system.wav"
#    s "Congratulations! You have seen The Last Dragon's good ending! See, Martin could be trusted after all!"
#
#    play sound "fx/system3.wav"
#    s "Feel free to try and get another ending, or just savour this moment."
#
#    jump mainmenu
#
#
#elif kol_tld_endingc == True:
#
#    play sound "fx/system3.wav"
#    s "Ending achieved: [[C]ommunication through Times, or Ending C for short."
#
#    play sound "fx/system.wav"
#    s "Congratulations! You have seen The Last Dragon's neutral ending! I wonder what happened with the portal..."
#
#    play sound "fx/system3.wav"
#    s "Feel free to try and get another ending, ideally a better one."
#
#    jump mainmenu
#
#
#elif kol_tld_endingd == True:
#
#    play sound "fx/system3.wav"
#    s "Ending achieved: [[D]etriment to All, or Ending D for short."
#
#    play sound "fx/system.wav"
#    s "You have now seen The Last Dragon's bad ending! Let's hope that Remy is safe."
#
#    play sound "fx/system3.wav"
#    s "Feel free to try and get another ending, hopefully a better one."
#
#    jump mainmenu
#
#
#else:
#
#    play sound "fx/system3.wav"
#    s "Ending achieved: [[E]xtinction of Dragonkind, or Ending E for short."
#
#    play sound "fx/system.wav"
#    s "You have seen the worst possible ending in The Last Dragon."
#
#    play sound "fx/system3.wav"
#    s "..."
#
#    play sound "fx/system3.wav"
#    s "I'm sorry that you had to go through that."
#
#    play sound "fx/system3.wav"
#    s "Don't worry, as the other endings are better. This I guarantee."
#
#    play sound "fx/system3.wav"
#    s "Still, if you need a bit of a break, then I understand. I'll be here, waiting for your return."
#
#    jump mainmenu
