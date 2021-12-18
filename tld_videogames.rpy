label remy_videogames:

#Don't mind me; just gonna spend several hours winging it while writing this code as I have no idea how to do this...
#-Kolsavdür

$ renpy.pause (2.0)

menu:
    "Use a kick.":
        #Player's turn to attack
        $ kol_tld_success1 = renpy.random.randint(1, 10)
        $ renpy.pause (0.5)

        if kol_tld_success1 > 8:
            $ kol_tld_remyhealth = kol_tld_remyhealth - kol_tld_mckickcrit
            m "I managed to land a successful kick on Remy."
            m "A critical hit!"
            $ renpy.pause (1.0)

            if kol_tld_remyhealth <= 0:
                $ kol_tld_secretending = True

                stop music fadeout (2.0)
                $ renpy.pause (3.0)
                play music "mx/stride_kol.ogg" fadein 0.5

                Ry look flip "I can’t believe this…"
                Ry "You’re amazing! How were you even able to play that well if it’s been years since you last {i}touched{/i} a video game?"
                c "I guess that it was just the muscle memory from my youth being revived."
                c "Or maybe I’m secretly just {i}that{/i} good."
                Ry smile flip "Touché."

                jump videogames_end

            else:
                pass

        elif kol_tld_success1 >= 4 and kol_tld_success1 <= 8:
                $ kol_tld_remyhealth = kol_tld_remyhealth - kol_tld_mckick
                m "I managed to land a successful kick on Remy while he was trying to start a combo."
                $ renpy.pause (1.0)

                if kol_tld_remyhealth <= 0:
                    $ kol_tld_secretending = True

                    stop music fadeout (2.0)
                    $ renpy.pause (3.0)
                    play music "mx/stride_kol.ogg" fadein 0.5

                    Ry look flip "I can’t believe this…"
                    Ry "You’re amazing! How were you even able to play that well if it’s been years since you last {i}touched{/i} a video game?"
                    c "I guess that it was just the muscle memory from my youth being revived."
                    c "Or maybe I’m secretly just {i}that{/i} good."
                    Ry smile flip "Touché."

                    jump videogames_end

                else:
                    pass

        else:
            $ kol_tld_remyhealth = kol_tld_remyhealth - kol_tld_mckickfail
            m "I tried to land a kick on Remy."
            m "Sadly, he was able to block it."
            $ renpy.pause (1.0)

            if kol_tld_remyhealth <= 0:
                $ kol_tld_secretending = True

                stop music fadeout (2.0)
                $ renpy.pause (3.0)
                play music "mx/stride_kol.ogg" fadein 0.5

                Ry look flip "I can’t believe this…"
                Ry "You’re amazing! How were you even able to play that well if it’s been years since you last {i}touched{/i} a video game?"
                c "I guess that it was just the muscle memory from my youth being revived."
                c "Or maybe I’m secretly just {i}that{/i} good."
                Ry smile flip "Touché."

                jump videogames_end

            else:
                pass


        #Remy's turn to attack
        #Needs balancing
        $ kol_tld_remyattack = renpy.random.randint(1, 10)
        $ kol_tld_remysuccessspecial = renpy.random.randint(1, 10)
        $ kol_tld_mcdefense = renpy.random.randint(1, 10)

        if kol_tld_remyattack > 8:

            if kol_tld_mcdefense > 6:
                $ kol_tld_mchealth = kol_tld_mchealth - kol_tld_remykickfail
                m "Remy tried to retaliate with a kick, but I managed to block it."
                $ renpy.pause (1.0)

            else:
                $ kol_tld_mchealth = kol_tld_mchealth - kol_tld_remykick
                m "Remy retaliated with a kick, landing a hefty blow on me."
                $ renpy.pause (1.0)

        elif kol_tld_remyattack >= 4 and kol_tld_remyattack <= 8:

            if kol_tld_mcdefense > 4:
                $ kol_tld_mchealth = kol_tld_mchealth - kol_tld_remypunchfail
                m "Remy leapt in to punch me, but I managed to block it just before he hit me."
                $ renpy.pause (1.0)

            else:
                $ kol_tld_mchealth = kol_tld_mchealth - kol_tld_remypunch
                m "Remy took revenge on my attack with a punch, which connected flawlessly."
                $ renpy.pause (1.0)

        else:

            if kol_tld_remysuccessspecial > 7:
                $ kol_tld_mchealth = kol_tld_mchealth - kol_tld_remyspecial
                m "Remy decided that enough was enough and charged a special move."
                m "It managed to hit, dealing significant damage to me."
                $ renpy.pause (1.0)

            else:
                $ kol_tld_mchealth = kol_tld_mchealth - kol_tld_remyspecialfail
                m "Remy decided that enough was enough and charged a special move."
                m "However, I managed to block it just in time and avoided most of the impact."
                $ renpy.pause (1.0)



    "Use a punch.":
        #Player's turn to attack
        $ kol_tld_success2 = renpy.random.randint(1, 10)
        $ renpy.pause (0.5)

        if kol_tld_success2 > 7:
            $ kol_tld_remyhealth = kol_tld_remyhealth - kol_tld_mcpunchcrit
            m "I managed to land a successful punch on Remy."
            m "A critical hit!"
            $ renpy.pause (1.0)

            if kol_tld_remyhealth <= 0:
                $ kol_tld_secretending = True

                stop music fadeout (2.0)
                $ renpy.pause (3.0)
                play music "mx/stride_kol.ogg" fadein 0.5

                Ry look flip "I can’t believe this…"
                Ry "You’re amazing! How were you even able to play that well if it’s been years since you last {i}touched{/i} a video game?"
                c "I guess that it was just the muscle memory from my youth being revived."
                c "Or maybe I’m secretly just {i}that{/i} good."
                Ry smile flip "Touché."

                jump videogames_end

            else:
                pass

        elif kol_tld_success2 >= 3 and kol_tld_success2 <= 7:
            $ kol_tld_remyhealth = kol_tld_remyhealth - kol_tld_mcpunch
            m "I managed to land a successful punch on Remy while he gave me an opening."
            $ renpy.pause (1.0)

            if kol_tld_remyhealth <= 0:
                $ kol_tld_secretending = True

                stop music fadeout (2.0)
                $ renpy.pause (3.0)
                play music "mx/stride_kol.ogg" fadein 0.5

                Ry look flip "I can’t believe this…"
                Ry "You’re amazing! How were you even able to play that well if it’s been years since you last {i}touched{/i} a video game?"
                c "I guess that it was just the muscle memory from my youth being revived."
                c "Or maybe I’m secretly just {i}that{/i} good."
                Ry smile flip "Touché."

                jump videogames_end

            else:
                pass

        else:
            $ kol_tld_remyhealth = kol_tld_remyhealth - kol_tld_mcpunchfail
            m "I tried to land a punch on Remy."
            m "Sadly, he was able to block it."
            $ renpy.pause (1.0)

            if kol_tld_remyhealth <= 0:
                $ kol_tld_secretending = True

                stop music fadeout (2.0)
                $ renpy.pause (3.0)
                play music "mx/stride_kol.ogg" fadein 0.5

                Ry look flip "I can’t believe this…"
                Ry "You’re amazing! How were you even able to play that well if it’s been years since you last {i}touched{/i} a video game?"
                c "I guess that it was just the muscle memory from my youth being revived."
                c "Or maybe I’m secretly just {i}that{/i} good."
                Ry smile flip "Touché."

                jump videogames_end

            else:
                pass


         #Remy's turn to attack
         #Needs balancing
        $ kol_tld_remyattack = renpy.random.randint(1, 10)
        $ kol_tld_remysuccessspecial = renpy.random.randint(1, 10)
        $ kol_tld_mcdefense = renpy.random.randint(1, 10)

        if kol_tld_remyattack > 8:

            if kol_tld_mcdefense > 6:
                $ kol_tld_mchealth = kol_tld_mchealth - kol_tld_remykickfail
                m "Remy tried to retaliate with a kick, but I managed to block it."
                $ renpy.pause (1.0)

            else:
                $ kol_tld_mchealth = kol_tld_mchealth - kol_tld_remykick
                m "Remy retaliated with a kick, landing a hefty blow on me."
                $ renpy.pause (1.0)

        elif kol_tld_remyattack >= 4 and kol_tld_remyattack <= 8:

            if kol_tld_mcdefense > 4:
                $ kol_tld_mchealth = kol_tld_mchealth - kol_tld_remypunchfail
                m "Remy leapt in to punch me, but I managed to block it just before he hit me."
                $ renpy.pause (1.0)

            else:
                $ kol_tld_mchealth = kol_tld_mchealth - kol_tld_remypunch
                m "Remy took revenge on my attack with a punch, which connected flawlessly."
                $ renpy.pause (1.0)

        else:

            if kol_tld_remysuccessspecial > 7:
                $ kol_tld_mchealth = kol_tld_mchealth - kol_tld_remyspecial
                m "Remy decided that enough was enough and charged a special move."
                m "It managed to hit, dealing significant damage to me."
                $ renpy.pause (1.0)

            else:
                $ kol_tld_mchealth = kol_tld_mchealth - kol_tld_remyspecialfail
                m "Remy decided that enough was enough and charged a special move."
                m "However, I managed to block it just in time and avoided most of the impact."
                $ renpy.pause (1.0)



    "Peform a special move.":
        $ kol_tld_success3 = renpy.random.randint(1, 10)
        $ renpy.pause (0.5)

        if kol_tld_success3 > 9:
            $ kol_tld_remyhealth = kol_tld_remyhealth - kol_tld_mcspecialcrit
            m "I tried to perform one of my special moves on Remy."
            m "A critical hit!"
            $ renpy.pause (1.0)

            if kol_tld_remyhealth <= 0:
                $ kol_tld_secretending = True

                stop music fadeout (2.0)
                $ renpy.pause (3.0)
                play music "mx/stride_kol.ogg" fadein 0.5

                Ry look flip "I can’t believe this…"
                Ry "You’re amazing! How were you even able to play that well if it’s been years since you last {i}touched{/i} a video game?"
                c "I guess that it was just the muscle memory from my youth being revived."
                c "Or maybe I’m secretly just {i}that{/i} good."
                Ry smile flip "Touché."

                jump videogames_end

            else:
                pass

        elif kol_tld_success3 >= 7 and kol_tld_success3 <= 9:
            $ kol_tld_remyhealth = kol_tld_remyhealth - kol_tld_mcspecial
            m "I tried to perform one of my special moves on Remy."
            m "Luckily, it landed."
            $ renpy.pause (1.0)

            if kol_tld_remyhealth <= 0:
                $ kol_tld_secretending = True

                stop music fadeout (2.0)
                $ renpy.pause (3.0)
                play music "mx/stride_kol.ogg" fadein 0.5

                Ry look flip "I can’t believe this…"
                Ry "You’re amazing! How were you even able to play that well if it’s been years since you last {i}touched{/i} a video game?"
                c "I guess that it was just the muscle memory from my youth being revived."
                c "Or maybe I’m secretly just {i}that{/i} good."
                Ry smile flip "Touché."

                jump videogames_end

            else:
                pass

        else:
            $ kol_tld_remyhealth = kol_tld_remyhealth - kol_tld_mcspecialfail
            m "I tried to perform one of my special moves on Remy."
            m "Sadly, Remy reacted just in time and blocked it."
            $ renpy.pause (1.0)

            if kol_tld_remyhealth <= 0:
                $ kol_tld_secretending = True

                stop music fadeout (2.0)
                $ renpy.pause (3.0)
                play music "mx/stride_kol.ogg" fadein 0.5

                Ry look flip "I can’t believe this…"
                Ry "You’re amazing! How were you even able to play that well if it’s been years since you last {i}touched{/i} a video game?"
                c "I guess that it was just the muscle memory from my youth being revived."
                c "Or maybe I’m secretly just {i}that{/i} good."
                Ry smile flip "Touché."

                jump videogames_end

            else:
                pass


        #Remy's turn to attack
        $ kol_tld_remyattack = renpy.random.randint(1, 10)
        $ kol_tld_remysuccessspecial = renpy.random.randint(1, 10)

        if kol_tld_remyattack > 8:
            $ kol_tld_mchealth = kol_tld_mchealth - kol_tld_remykick
            m "Remy retaliated with a kick, landing a hefty blow on me."
            $ renpy.pause (1.0)

        elif kol_tld_remyattack >= 4 and kol_tld_remyattack <= 8:
            $ kol_tld_mchealth = kol_tld_mchealth - kol_tld_remypunch
            m "Remy took revenge on my attack with a punch, which connected flawlessly."
            $ renpy.pause (1.0)

        else:

            if kol_tld_remysuccessspecial > 6:
                $ kol_tld_mchealth = kol_tld_mchealth - kol_tld_remyspecial
                m "Remy decided that enough was enough and charged a special move."
                m "It managed to hit, dealing significant damage to me."
                $ renpy.pause (1.0)

            else:
                $ kol_tld_mchealth = kol_tld_mchealth - kol_tld_remyspecialfail
                m "Remy decided that enough was enough and charged a special move."
                m "However, I managed to block it just in time and avoided most of the damage."
                $ renpy.pause (1.0)

#Heh. Who even cared about code readability?


if kol_tld_mchealth <= 0:

    stop music fadeout (2.0)
    $ renpy.pause (3.0)
    play music "mx/stride_kol.ogg" fadein 0.5

    Ry smile flip "Would you look at that. I actually won!"
    Ry "I’ll admit, I thought that I was going to lose there for a second."
    c "Come on, don’t lie to me. I know that you thought you were going to win this match right from the start."
    Ry normal flip "Alright, I {i}did{/i} believe that I was going to win, but mainly because I knew that it had been a really long time since you last played any video games."
    Ry look flip "Except for that one time in my office."
    Ry normal flip "I think you could say that I simply took advantage of the situation while I had the chance to do so."
    c "You really don't have to rub it in, you know."
    Ry smile flip "Sorry about that. I just got excited at winning against an actual person instead of the game itself for once."

    jump videogames_end

else:
    m "Your total health remaining: [kol_tld_mchealth]%%. Remy's total health remaining: [kol_tld_remyhealth]%%."
    jump remy_videogames
