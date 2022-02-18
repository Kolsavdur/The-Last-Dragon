label tld_day2:

$ save_name = (_("TLD - Day 2"))

$ renpy.pause (3.0)
scene kolmchouseday at Pan ((300, 80), (0,80), 5.0) with dissolveslow

play music "mx/submerged_forest_kol.ogg" fadein 0.5

m "I awoke from my sleep, knowing that a day full of tasks awaited me. On my way to get breakfast, I spotted Remy making what seemed to be pancakes."
m "How he managed to gather all the fresh ingredients necessary is beyond me, considering that I own nothing even remotely usable for baking."
m "When I approached Remy, he seemed to be mildly startled, but soon smiled at me."

show remy smile with dissolve

Ry "Oh! Good morning, [player_name]! How did you sleep last night?"

menu:
    "I didn't sleep that well.":
        $ renpy.pause (0.5)
        Ry look "That’s a shame. It’s been quite some time since I had a good night’s sleep too."
        Ry normal "At least I made you some breakfast, though."

    "Just an average night's rest.":
        $ renpy.pause (0.5)
        Ry "Then I’m glad to hear that. I had times where I slept better, to be honest, but all things considered, last night wasn’t too bad."
        Ry normal "I also made you some breakfast, if you would like some."

    "I slept pretty well.":
        $ renpy.pause (0.5)
        Ry "I’m happy for you, then. A good night’s sleep can often influence how the rest of the day follows."
        Ry "I also made you some breakfast, if you would like some."

c "Thanks. Might I ask how you got the ingredients to make these pancakes? Last time I checked, I didn’t have any ingredients like flour available."
Ry shy "The recipe I’m using has a lot of… substitutes, considering that you didn’t have the necessary ingredients."
Ry smile "Don’t worry. It’s still perfectly edible, though."

hide remy with dissolve
m "Hesitating, I took a bite of the pancakes offered to me. Surprisingly, they tasted exactly like the pancakes I used to eat on a frequent basis during my college years."
show remy normal with dissolve

c "(And more evidence towards Remy’s cooking being better than mine.)"
Ry smile "Judging by your expression, I’d say that you like your food, or am I mistaken?"
c "Remy, once again, you show me that your cooking is amazing. These taste exactly like the ones I always used to eat before the flare hit."
Ry shy "Is that so?"
Ry smile "Well, maybe it’s because I studied the recipes on your PDA while you were sleeping."
c "No wonder why they tasted so familiar. However, that still doesn’t answer how you could get the taste spot on without the original ingredients, though."
Ry normal "That is a secret I’ll keep to myself for now."

hide remy with dissolve
m "We finished our breakfasts and prepared for the busy day ahead. I wondered how much time we have left before all our supplies are drained."
m "It’s necessary that we get the food and water facilities up and running, but how we are going to accomplish such a daunting task is still beyond me."
m "Suddenly, Remy called out to me."
Ry "Wait for me, please!"
m "I waited a bit for Remy to catch up with me as I walked to the entrance to the now slightly less deserted city."

scene city at Pan ((0, 360), (0, 0), 4.0) with dissolve
show remy normal with dissolve

Ry shy "Sorry for holding you back. I had a bit of trouble getting everything ready before going out."

menu:
    "What a slowpoke.":
        $ renpy.pause (0.5)
        Ry look "There were still some things left that I needed to do, you know."
        Ry "It isn’t that easy to prepare yourself when everything is human-sized."
        c "Well, just work faster then."
        Ry "I wish..."

    "Don't stress too much about it.":
        $ renpy.pause (0.5)
        Ry look "Until I suddenly land myself in danger due to negligence on my part."
        c "I’m pretty sure that isn’t going to happen any time soon."
        Ry smile "Not if I get everything ready beforehand like I'm supposed to!"
        c "I suppose that's true..."

    "Like fitting through the doorways?":
        $ renpy.pause (0.5)
        Ry look "Among other things."
        Ry "I still need to get used to everything, though."
        Ry normal "At least I can cook with human-sized cookware."
        c "At least you got that going for you."

$ renpy.pause (1.0)
c "So, do you have any ideas for today?"
Ry normal "I figured that you could show me around what’s left of the city. I didn’t have the time to explore much after arriving here, and your PDA only gave a rough idea of where you might be, not necessarily the entire layout of the city."
c "That sounds like a good idea. It would be for the better if you had the opportunity to familiarise yourself in our world."
c "Be sure to stay close to me, though. The last thing I want right now is for you to get lost."
Ry "Of course."

scene kolcitycentre at Pan((0,180),(0,180),3.0) with dissolve

m "We walked for a while until we came to a flat area near the centre of the city. This area was always used as a sort of marketplace where people could exchange services for resources. Now it felt eerily quiet."

show remy normal with dissolve

c "Here’s a good place to start with our little tour. This is what used to be the trading plaza. All sorts of activity used to occur here like, unsurprisingly, trades. This was also quite a popular place to meet with others due to its location."
Ry "What kind of trades used to take place here?"
c "We used to do work in exchange for the resources some of us had left. This was frowned upon by the officials, as we all had to pool in our resources so that we could all survive."
c "That didn’t stop certain people from taking advantage of others, though."
Ry "I see. It’s a shame how some people only want to benefit themselves when in the end everybody, including them, suffers."
c "Well, if it didn’t hurt the city as a whole in a problematic way, then there would always be those who would turn a blind eye for a few scraps of resources."

scene kolwtpout at Pan((0,0),(0,0),2.0) with dissolve

m "We walked on through the streets until we reached the old water treatment plant. Without power, any water that happened to still remain in the old wells and reservoirs would contain many diseases which could potentially cause serious problems if consumed."

show remy normal with dissolve

c "This is where most of the city’s water was treated. Sadly, without power, the water could not be made safe enough for human consumption anymore."
Ry look "Couldn’t you simply have boiled the water to kill anything that might have lived in it?"
c "Not on a big enough scale. The little water we had left from the wells was already murky at best, let alone clean and safe."
c "Most people still took that water and boiled it as an extra security measure, but you could only drink so much dirty water before you start to get some serious problems."
Ry "It’s a miracle how so many people could have survived like this."
Ry smile "Looks like humans are far more resilient than I thought!"

scene kolfactoryout at Pan((0,90),(0,90),2.0) with dissolve

m "Nearby was the factory which provided a great amount of food for the city. It was in a lesser state of disrepair than the water treatment plant, but would still need a lot of attention if it was to be able to function at full capacity."

show remy normal with dissolve

Ry look "That building looks extremely old. Are you sure it’s safe to be here, [player_name]?"
c "Yes, it’s still pretty safe to explore around. Even if it’s worn down, it’s surprisingly one of the safer buildings here."
Ry "That doesn’t make me feel any better, though. Shouldn’t the officials have decommissioned it before it could hurt somebody?"
c "The officials didn’t want to expend any more resources on unnecessary things, such as decommissioning old buildings."
c "If they were to collapse, then it would just be something that happened. Nothing more, nothing less."
Ry "I see."
m "Suddenly, I realised that there could still be a small seed bank somewhere on the factory grounds, as since crops were likely to fail in this environment, a backup which contained crop seeds only seemed logical for the survival of the city."
c "Remy, I’m going to need your help here. There could be a small container nearby that may contain a few types of seeds which we can use to regrow crops after some basic repairs have been done to the necessary facilities."
Ry normal "Sure thing, [player_name]."

hide remy with dissolve

m "We quickly searched around the exterior of the factory grounds, but nothing was found."
c "(It seems that if there were any seeds left, it would already have been taken.)"
c "(Maybe someone took it with them before entering the portal?)"
m "Disappointed, we left the factory grounds, hoping that the next few places we went were more interesting."

show remy normal with dissolve
c "Well, that was a waste of time. Is there anywhere else you would like to go?"
Ry "Yes, actually. When I first arrived here in your world, I saw an open house near the city wall. I figured that it was only normal, since nobody was left here anymore."
Ry look "Only now have I realised how strange it was, considering that every other house is closed."

stop music fadeout (3.0)

c "What are you talking about?"
Ry "Don’t you think how unusual it is that a single house would be left open at the farthest reaches of the city, but not any other buildings?"

stop music
play music "mx/intrigue.ogg" fadein 1.0

m "I pondered Remy’s words for a moment and realised the potential of this discovery. I determined that someone could have left some resources behind which we could use to help in our survival."
m "But something just didn’t add up. Why would an open house that was essentially an invitation for raiders have anything of use? Unless..."
c "In which direction did you see this house?"
Ry normal "I think it was somewhere to the east of here, near the guard post at one of the city gates."
c "Then we have no time to lose. We need to go there. Now!"

scene kolloganout at Pan ((0, 0), (0, 250), 5.0) with dissolveslow

m "We ran as fast as we could to the place Remy described. After a few minutes of constant sprinting and a few more of catching my breath, we arrived at my destination."
m "The house was strangely in a better shape than the rest of the city, with what seemed to be attempts made on repairing the walls, as well as the surrounding infrastructure."
m "I noticed that the door was wide open. I feared that there could be something dangerous inside. Either that, or something very, very helpful."

stop music fadeout (2.0)

c "(Let’s hope that whatever is inside isn’t th-{w=0.5}{nw}"

play sound "fx/tinyexplode_kol.wav"
queue sound "fx/fall3.ogg"
$ renpy.pause (7.5)

m "Suddenly, I heard a small boom coming from the inside, followed by the sound of something falling. Unease and curiosity both arose within me as I considered the possibilities."

stop sound
play music "mx/threat.ogg" fadein 0.5
show remy look with dissolve

Ry "What was that noise?"
c "I don’t know for sure, but I can tell you one thing: It’s either {i}really{/i} good, or {i}really{/i} bad."
Ry "Should I check it out for you, then? I wouldn’t want you to get hurt, and chances are, my scales would probably be able to protect me against whatever is inside."
c "Remember, your scales didn’t help much against Reza’s gun, and I believe that if somebody was actually still here, then they most likely wouldn’t hesitate to shoot you."
c "I could still be able to negotiate with whoever is inside if the need arises."
c "I think that it would be better if you were nearby to cover me instead, just in case."
Ry "Alright. Please be safe."

stop music fadeout (2.0)
play sound "fx/steps/rough_gravel.wav"

scene kolloganhouse at Pan ((0, 220), (0,360), 3.0) with dissolveslow
stop sound fadeout (1.0)

play music "mx/politics.ogg" fadein 0.5

m "I slowly entered the house, making sure not to alert whatever was inside. It seemed to be quite spacious, not unlike the typical houses we used to have before the solar flare."
m "I looked around and saw many scattered electrical parts lying around, as well as some blueprints and schematics."
m "After some searching, I found a locked door next to a few boxes of old electrical devices. Hesitatingly, I knocked, hoping for a response."

play sound "fx/knocking1.ogg"
$ renpy.pause (3.5)

"???" "What? How could there…" #Logan reveal LET'S GOOOOOOOO!

play sound "fx/door/door_open.wav"

m "The strange voice sounded oddly familiar to me, but yet quite distinct. Slowly, the door unlocked, revealing a human face greeting me."

show kolloganstudy at Pan ((0, 40), (0,90), 1.0) with dissolve
$ renpy.pause (2.0)
show logan surprised with dissolve

"???" "Wait... [player_name]? What the heck are you doing here?"
c "Logan? I thought you went with all the others through the portal."
Lg serious "And I thought you were supposed to be an ambassador doing ambassador things in the dragon's world. Now, I’ll ask my question again: Why are you here?"
c "It’s a really long story, so I’ll summarise it to you as best as I can..."

scene black with fade
$ renpy.pause (4.0)

show kolloganstudy at Pan ((0, 40), (0,40), 0.0) with dissolve

show logan serious with dissolve

c "...and that’s what I’m doing in this city. I really thought I would be the only human left here, but to see you of all people still here is quite remarkable, especially regarding the circumstances."
c "I mean, I have been awake for..."
$ renpy.pause (2.0)
c "Hell, I don't even know how long. What I'm trying to say is, even after searching around the city for days, I couldn't find anybody else here until now."
Lg "That's because I've spent most of my time here in my study working."
Lg thinking "Not that it matters, as all my work has mostly gone to waste."
Lg normal "Oh, but now is not the time. You said that you have a dragon with you? I’ll have to see it if you have any hope of convincing me, [player_name]."
c "That dragon has a name, you know. Come, I’ll introduce you to him."

scene kolloganhouse at Pan ((0, 220), (0,220), 3.0) with dissolveslow
$ renpy.pause (2.0)

m "We walked past the huge mess that is Logan’s house towards the entrance, where I found Remy patiently waiting outside. He seemed to look relieved when he saw me."

scene kolloganout at Pan ((0, 250), (0, 250), 2.0) with dissolveslow
$ renpy.pause (2.0)

show remy smile with dissolve

Ry "Ah, you’re back! I’m glad that you made it out safe."
Ry normal "Did you find anything useful?"
c "Not something, but {i}someone{/i}."

show remy at right with ease
show logan surprised flip at Position(xpos = 0.25) with easeinleft

Lg "Well, I’ll be damned. It actually {i}is{/i} a dragon. And here I thought that Reza was just exaggerating about what’s on the other side."
c "Remy, meet Logan. He’s somebody I used to work with once while trying to keep myself afloat. I honestly thought that he would have been the first to leave, considering his useful skills, but it seems that I was wrong."
Ry smile "It’s a pleasure to meet you, Logan. My name is Remy, and I shall be the ambassador of dragonkind in your world."
m "Although Remy was smiling, I could feel that Remy wasn't exactly happy to say those words."
Lg serious flip "Aaaaand the dragon talks. This day just keeps getting more and more interesting..."
Lg normal flip "Well, Remy was it? It’s an honour meeting a mythical creature such as yourself."
Ry normal "The feeling is mutual, Logan."
Ry smile "We actually had a lot of myths and legends about humans, but I believe that [player_name] has already told you everything."
Lg "You would be correct there. No need to recap anything; I do have a really good memory."
Ry normal "What intrigues me, however, is the reason why you are still here. I mean, everybody left the city quite some time ago. Why did you stay behind?"
c "Yeah, why didn't you go through the portal, and why on earth is your place filled with so much scrap? This is really out of character, even for you."
Lg serious flip "I figured that you’d want to know the answer to that. Well, no point in standing outside. Take a seat, then we’ll talk."

scene kolloganhouse at Pan ((0, 220), (0,220), 0.0) with dissolveslow

m "We walked inside with me and Logan taking seats with Remy sitting on the floor. Turns out, it's really hard to sit reasonably comfortably when there was a huge pile of electronic scraps sitting at your feet."

show logan serious flip at Position(xpos = 0.25) with dissolve
show remy normal at right with dissolve

Lg "Comfortable yet? This will be a really long answer, so I don’t want you to concentrate on other things like your butt starting to cramp."
c "I’m good."
Ry "I think I’ll manage."
Lg " Alright. I’ll start right after you went through the portal, [player_name]."

stop music fadeout (2.0)

scene black with dissolveslow
$ renpy.pause (2.0)
nvl clear
window show

play music "mx/a_gift_kol.ogg" fadein 0.5 #Is this innfodump a bit weird and long? Hmmmmm...

n "Shortly after your departure into the unknown, humanity started to create a backup plan in case you and Reza weren’t able to bring the generators. Much debate went around on how we would do such a thing, considering that our last generator broke a while back."
n "Eventually, one of the officials decided to ask me to do what seemed to be impossible at the time. They figured that since I achieved my master’s degree in electromagnetism at a prestigious university back in the day, I would be qualified enough. I rejected, saying that there could be no way to do what they asked."
n "That was before we made a monumental discovery. A few miles northeast of here, one of the scouts found an abandoned copper mine with primitive, albeit intact, smelting gear and some remaining copper ore."

window hide
nvl clear
window show

n "Oh, but it gets better: Deeper in the mine, there were piles upon piles of disregarded electronic scrap. Some of the parts were even functional, to a basic degree."
n "Upon hearing this news, the authorities freaked out, to put it lightly. Once again, they asked me for my help, hoping with all the newly discovered scraps and copper, I could actually accomplish something. This time, I agreed."
n "They sent me some old copies of some basic schematics and blueprints, as well as the electronics. Luckily, somebody else was already responsible for smelting the copper to form usable wires. So many hours were spent with me testing which electronics could be used and which were worth as much as sand."
n "With the aid of the schematics, as well as the parts acquired, I completed an immense task: I made a functional electrical device by using the copper wires and the spare parts."

window hide
nvl clear
window show

n "It wasn’t much, mind you, but when you show something like that to a society in which most people haven’t seen a functioning lightbulb in years, you tend to be seen as a sort of public hero. Sadly, the authorities never understood the concept of slow progression, so they gave me something that not even a genius would try to attempt on their own."
n "They wanted me to make a generator from scratch."
n "I wanted to refuse, saying that it took a lot of machines and resources to even start making one, let alone some random guy with a few spare parts and too much time on his hands, but I couldn’t. I didn’t want to let everyone down by showing them a bit of hope, only to take it away from them at their greatest time of need."

window hide
nvl clear
window show

n "With the help of some former associates and anybody that still knew anything about electronics, we were able to create a rough prototype based on some really old blueprints. Where the authorities even got their hands on them in the first place will always remain a mystery to me. Regardless, upon turning the generator on, it lasted about two seconds before exploding, severely injuring one of my helpers."
n "It took about a week and a half, but I finally created a generator that could theoretically last about fifty seven seconds before it would start to fail. I wanted to work on it further so that it could actually be considered safe for use, but the city desperately needed it to the point that nobody could simply wait anymore."
n "That was, when out of nowhere, Reza came."

window hide
nvl clear
window show

n "You should have seen the looks on everybody’s faces when Reza stepped through the portal and walked all the way to the city centre with a large bite wound in his side. The entire city was in a frenzy, with everybody thinking that some sort of monster was about to come and kill the entire population."
n  "Reza told us about what happened to him, as well as the state of society on the other side of the portal. He made it sound as if the civilization on the other side was filled with bloodthirsty savages that have access to technology they shouldn’t even be able to comprehend."
n "As much as I respected Reza and his immense determination, I figured that maybe he deliberately twisted the truth a bit so that he could be seen as a sort of victim. He just seemed like that kind of guy to me. Well, I’m sure both of you would know more about him than I do, after all."

window hide
nvl clear
window show

n "Long story short, since Reza was seen as a saint by the people, the authorities issued an order that everyone needed to abandon the city and go through the portal to live in much better conditions. That’s how I presume a soldier found you in the first place."

window hide
nvl clear

scene kolloganhouse at Pan ((0, 220), (0,220), 0.0) with dissolveslow
show logan serious flip at Position(xpos = 0.25) with dissolve
show remy normal at right with dissolve
$ renpy.pause (2.0)

Lg "I was responsible for using that generator of mine to power the portal long enough so that the entire city could pass through, as the energy reserves we had left simply weren’t enough."
Lg "It also didn’t help that the generator we had powering the portal wasn’t powerful enough to transport the entire city on its own."
Lg "I was to make sure that everybody could go through the portal before my generator started to fail, which caused me to stay behind."
Lg "Since then, I’ve been trying to create another generator so that I could rejoin everybody else. That was before you came and told me everything that happened, though."
c "Wait, so this is what all the parts in the room are for? Why would you need this much electronics? It seems like a lot of unnecessary parts to me."
Lg "That’s because I used some of them to repair other devices I kept in my private collection from before the solar flare so that I could actually attempt to recreate a generator."
Lg normal flip "You don’t think I could actually recreate advanced electronics with a single circuit board and some basic soldering tools, do you?"
c "I see your point."
Ry smile "That is an amazing story you told. I don’t think that even our smartest could have done what you did from scratch."
Lg thinking flip "Is that so? Guess I overestimated everything your kind achieved, then."

show remy look with dissolve

menu:
    "It's only because you're overqualified.":
        $ renpy.pause (1.0)

        c "Or it’s because you have a degree in electromagnetism, as well as years worth of experience working on electronics as a hobby and a job."
        Lg smiling flip "Or that, I suppose."

    "Their technology was extremely advanced.":
        $ renpy.pause (1.0)

        c "Well, the technology the dragons had was very similar to what we had before the solar flare."
        c "Remember, they weren’t as easy to develop due to the dragons not having as much articulation in their joints as humans."
        Lg normal flip "I guess I can see where you’re coming from."

    "If only you could have seen everything in action.":
        $ renpy.pause (1.0)

        c "If only you knew what exactly kind of things were on the other side of the portal."
        Lg "Like what?"
        c "Things that I’ll keep to myself, for now."
        Lg normal flip "How ominous."
        

stop music fadeout (3.0)
show logan thinking flip with dissolve

m "Logan seemed to be deep in thought for a while, after which he smiled and looked at Remy with an expression similar to that of a smirk."

play music "mx/clouds.ogg" fadein 0.5

Lg normal flip "Say, you wouldn’t happen to know what video games are, do you Remy?"
Ry smile "I do! In fact, I’d say that I’m quite passionate about them."
c "Don’t tell me-{w=0.6}{nw}"
Lg "-that I have repaired an old video game system just for the heck of it. Of course I did, [player_name]. You should know by now that when I’m not working seriously, I do stupid stuff like this."
Lg smiling flip "Besides, what else did you think I tested my prototype generators on?"
Lg "I even got a near ancient television working just to take the joke a step further."
c "Why am I not surprised?"
Lg normal flip "I haven’t had the time recently to test it out, due to my generator exploding and all that. What do you say to hooking one of your generators up to play some video games?"
c "I feel like this would just be a waste of time, though."
Ry normal "Come on, [player_name]. Have some fun for once! All you did recently was focus on Reza and your duties of being an ambassador. It would be great for you to have some time off."
Ry shy "Besides, I never had the chance to show you some of my video games. It would make for a great opportunity for you to relive some old memories."

menu:
    "Well, I suppose it wouldn’t hurt.":
        $ renpy.pause (1.0)
        Lg smiling flip "Good choice. I’ll get everything ready for you. I’d recommend that Remy should go and get two generators for me."
        Lg normal flip "No offence, but he’s way faster than you could ever hope to be."
        c "Well, what am I supposed to do about it? He {i}is{/i} a dragon, after all."
        Lg smiling flip "Absolutely nothing!"
        Ry normal "Why do you need two generators? A single one should be more than enough to power everything that you need."
        Lg normal flip "I'd like a spare one to study and test on so that I can try to replicate the way it’s constructed."
        Lg "With that information I should be able to create better prototypes that won't explode in less than a minute."
        Ry "That makes sense. I’ll go and get the two generators for you, then."

        hide logan with dissolve
        hide remy with dissolve

        m "Remy stood up from the floor and stretched before exiting the door. A few minutes passed before he came back with two small generators in his claws."
        m "Logan looked at the generators in what I assumed was a combination of interest, amusement and shock. It was always hard to distinguish a specific emotion from him, regardless of what he was actually feeling."

        show logan surprised flip at Position(xpos = 0.25) with dissolve
        show remy normal at right with dissolve

        Lg "Damn, you were right, [player_name]. These generators are {i}tiny{/i} compared to what we had back in the day. Are you sure that these things can even turn on?"
        Ry smile "Those generators can pack an amazing punch. A single one can easily power an entire house, if not more. Nothing less from state of the art technology!"
        Lg thinking flip "Impressive. Even the wires are all connected in the same way as ours. It’s like these things were made with human technology in mind."
        Lg normal flip "Well, wait a few moments while I hook everything up."

        hide logan with dissolve

        m "Logan went to one room that was secluded from the rest of the house. I could hear how he fumbled around looking for the video game system in what I could only assume was one of the many piles of electronics in his house."

        play sound "fx/zap_kol.wav"

        m "A while later, I could hear a sudden zap with him swearing shortly afterwards."
        $ renpy.pause (2.0)
        m "Minutes passed before he came out again to call for me and Remy."

        show logan normal flip at Position(xpos = 0.25) with easeinleft

        Ry look "What were those strange sounds all about?"
        Lg " Don’t worry about it. Just some wires in the video game system that were acting weird. Nothing to be worried about."
        c "You wouldn’t even worry if you were suddenly on fire. You’re way to chill for your own good."
        Lg serious flip "And you have a problem with that?"
        c "Nope. Just pointing the obvious out."
        Lg normal flip "As always."

        scene kollogantv at Pan ((0, 0), (0,200), 3.5) with dissolve
        m "We entered the room and found an old television haphazardly connected to a now forgotten video game console that I used to play during my youth, as well as the generator powering it."
        m "The console itself had a slot in which you could insert tiny cards to play the video game of your choice."

        show logan normal with dissolve

        Lg "Before you start, you’re going to need this."
        m "Logan gave me a card with the words “Fighting Game” scribbled over it."
        Lg thinking "Luckily I didn’t need to do any repairs on the card, as it survived the solar flare. How on earth this could survive, but not nanobots in someone’s bloodstream, will baffle me until I die."
        c "Could it have something to do with the fact that it was buried under a bunch of other electronics, or maybe because it’s way simpler compared to the other parts salvaged from the mines?"
        Lg "No, as simpler things from way deeper in the mines didn’t survive. I guess that we’ll simply never know."
        Lg normal "Now, what are you waiting for? Ready to relive some memories again?"

        play sound "fx/card.wav"

        m "I put the card into the video game system and turned it on. Remarkably, it started to read the card and showed the main menu of the game."
        m "Somehow, Logan’s work was able to repair the system to its former glory. A wave of nostalgia washed over me as I held the controller and started to play."
        m "Suddenly, I heard Remy interrupting me."

        show logan normal at Position(xpos=0.75, xanchor='center') with ease
        show remy look flip at left with easeinleft

        Ry "Hey, I thought we were going to play together. Do you really want to keep all the fun to yourself?"
        c "Oh, sorry. I guess I got a bit carried away. Would you like to fight me, or should we play together on the same team?"
        Ry smile flip "I think I’ll fight you. I’m quite good at pulling off different combos in different situations, so I think that I can manage against you."
        Ry normal flip "First, however, I’m going to need a bit of a warm up, though. I think that I’ll need to get used to the game’s controls first. I’ll also need some time to get used to this controller."
        Ry "After all, this {i}was{/i} made for humans in mind, so I think I’ll have a hard time doing anything complicated, especially if I can’t move fast enough."
        Ry smile flip "Regardless, I believe that I’ll do well. After all, I’m just {i}that{/i} good."
        c "Is that a sense of hubris I’m detecting?"
        Ry "This isn’t hubris; I’m just acknowledging my skill."
        c "We’ll see about that."

        hide remy with dissolve
        hide logan with dissolve

        m "We both selected our characters, as well as the stage we were going to fight on. I selected a mode where we could practice a bit first so that both of us could get used to the controls."
        m "Remy was right, however. Even if he couldn’t move as effectively as he would with a controller suited for dragons, he was still an opponent to be feared. He somehow managed to perform combo after combo despite having never played a human fighting game."
        m "This was certainly going to be a tough challenge."

        show logan normal at Position(xpos = 0.75) with dissolve
        show remy smile flip at left with dissolve

        Ry "How was that for a warmup?"
        c "Far better than I expected. It’s almost as if you have already played this game before."
        Ry normal flip "Well, once you mastered the basics in one game, you can easily create similar combos in another, regardless of what type of moveset the game uses."
        Ry smile flip "I’m surprised how similar your games are to the ones I used to play."
        Ry normal flip "Maybe there is still hope for me against you."
        stop music fadeout (3.5)
        c "Says the guy who has absolutely destroyed me during the warmup."
        Ry smile flip "Alright, you got me there."

        show remy normal flip with dissolve
        hide logan with dissolve

        stop music
        play music "mx/warp_kol.ogg" fadein 1.0

        #After so long, it's finally time to play some video games!
        #Also, my apologies for this minigame..
        #After all, I am an avid believer of RNGesus!

        jump remy_videogames

        label videogames_end:

        Ry normal flip "Regardless, I believe that was really fun. I’m glad that I could play some video games with you, [player_name]."
        c "I agree. This was certainly a fun trip down memory lane."
        c "At least we actually got around to playing some video games with each other."
        Lg "So, are you finished playing, or should I continue to wait?"
        m "Logan’s voice startled me. I became so invested in fighting against Remy that I completely forgot that Logan was watching us the whole time."

        show logan normal at Position(xpos = 0.75) with dissolve

        c "Yes, I believe that we are done here. That is, unless Remy wants a rematch."
        Ry "I’m good, thanks. I believe that I’ve had more than enough excitement for now."
        Lg smiling "You know, you’re surprisingly good for someone who can’t even walk on two legs correctly."
        Lg normal "No offence, of course."
        Ry "None taken. I actually considered playing video games as a career back when I was young, but that was before I discovered my passion for research."
        c "I think that you would have made a great competitive player. You certainly have the skill."
        Ry "Thanks, [player_name], but in truth, I don’t feel like that would have been a suitable career path for me in the long run. After a while, it would just start to feel repetitive and boring."
        Ry smile flip "Research is far more interesting."
        c "You do have a point there."
        Lg "Well, I’d still like to test out your skill personally one day. Maybe we can fight against each other and see how that turns out."
        Ry "Sure! I’ll just need to have some time available one day, then we could see which one of us is better."
        Lg "Deal."

        $ kol_tld_remyvideogames = True

        scene kollogantvnight at Pan ((0, 200), (0,200), 3.0) with fade
        $ renpy.pause (2.0)

        m "I looked outside the window and realised that it was already night. We had stayed so long that nearly the entire day had been spent at Logan’s place, minus the small tour of the city earlier today."

        show logan normal dk at Position(xpos = 0.75) with dissolve
        show remy normal flip dk at left with dissolve

        c "Regardless, thank you for your time today. It was great to see you again, especially under these circumstances."
        Lg normal dk "Don’t worry about it. At least I know that I’m not completely alone in this damned excuse of a city."
        Lg smiling dk " And I got to meet a dragon of all things! I swear, if anybody was still here, then the entire city would have swarmed to meet you, Remy."
        Lg "You’d be an instant celebrity!"
        Ry shy flip dk "Really? I don’t really think that I’d attract that much attention."
        Lg normal dk "Oh, but it’s the truth."
        Ry normal flip dk "In any case, if you ever need any help, feel free to either find me or [player_name] and we’ll try to assist you in any way we can."
        Lg "Does that count from this moment on, by any chance?"
        c "Um, sure, I guess. What can we help you with?"
        Lg serious dk "Is there any chance that I can see your PDA? I have a slight hope that there may be something stored in there that could help me in creating and repairing some equipment."
        Lg "Leaving the generators here would also help, due to reasons that I already stated."
        c "If you can somehow use the information on the PDA to help rebuild the city in any way, then be my guest."
        Lg smiling dk "Great!"

        hide remy with dissolve
        hide logan with dissolve

        m "I gave Logan my PDA, which he received with a great smile. After some final parting words, me and Remy both left Logan to his own bizarre business."

        stop music fadeout (2.0)
        scene black with fade
        $ renpy.pause (2.0)
        play music "mx/barren.ogg"

        scene kolmchousenight at Pan ((300, 80), (0,80), 5.0) with dissolveslow

        m "We arrived back at my house. Remy seemed to be more tired than usual, as he immediately went straight to the couch while I made something for me to eat."
        m "When I looked back to Remy to offer him some food, he was sound asleep."
        c "(Seems Remy doesn’t need someone to sleep with tonight.)"
        m "I finished up with the remaining dishes and went straight to bed, letting my eyes wander around my room until I eventually fell asleep as well."

        scene black with fade
        stop music fadeout (2.0)
        $ renpy.pause (2.0)


    "Sorry, but we’re too busy to play video games.": #Now why would you choose this option? Jerk...
        stop music fadeout (1.0)
        $ renpy.pause (2.0)

        play music "mx/fragments.ogg"

        c "I’m sorry, but there is far too much for us to do right now, especially now that there are three people to share the city's limited resources with."
        c "We can't afford wasting any more of our time playing video games."
        Lg serious flip "You know, you really do have time. It’s only just after midday, and I’m pretty sure that there’s not much you can do for what’s left of the day."
        Ry sad "It’s fine, Logan. If [player_name] doesn’t want to play video games, then so be it."
        Ry "After all, there {i}is{/i} still a lot left to do, and we simply don’t have the time to just keep getting sidetracked for more than it is necessary."
        Lg "You do realise you’re missing out on a pretty big opportunity, right?"
        c "We do. That’s why we’ll come back at a later time when we can afford to do so."
        Lg "Suit yourselves, then."
        c "Regardless, thank you for your time today. It was great to see you again, especially under these circumstances."
        Lg normal flip "Don’t worry about it. At least I know that I’m not completely alone in this damned excuse of a city."
        Lg smiling flip " And I got to meet a dragon of all things! I swear, if anybody was still here, then the entire city would have swarmed to meet you, Remy."
        Lg "You’d be an instant celebrity!"
        Ry shy "Really? I don’t really think that I’d attract that much attention."
        Lg normal flip "Oh, but it’s the truth."
        Ry normal "In any case, if you ever need any help, feel free to either find me or [player_name] and we’ll try to assist you in any way we can."
        Lg "Does that count from this moment on, by any chance?"
        c "Um, sure, I guess. What can we help you with?"
        Lg serious flip "Is there any chance that I can see your PDA? I have a slight hope that there may be something stored in there that could help me in creating and repairing some equipment."
        Lg "Bringing two generators here would also be an immense help for my tests."
        c "If you can somehow use the information on the PDA and the generators to help rebuild the city in any way, then be my guest."
        Lg smiling flip "Great!"

        hide remy with dissolve
        hide logan with dissolve

        m "I gave Logan my PDA while Remy flew away to get the generators. When we gave everything to Logan after Remy had returned, he thanked us with a great smile on his face."
        m "After some final parting words, me and Remy both left Logan to his own bizarre business."

        scene black with fade
        $ renpy.pause (2.0)
        stop music fadeout (2.0)
        play music "mx/barren.ogg"

        scene kolmchousenight at Pan ((300, 80), (0,80), 5.0) with dissolveslow

        m "We arrived back at my house late at night after we decided to tour the city some more. Remy seemed to be more tired than usual, as he immediately went straight to the couch while I made something for me to eat."
        m "When I looked back to Remy to offer him some food, he was sound asleep."
        
        if kol_tld_remysleep1 == True:

            c "(Seems Remy doesn’t need someone to sleep with tonight.)"

        else:
            pass
            
        m "I finished up with the remaining dishes and went straight to bed, letting my eyes wander around my room until I eventually fell asleep as well."

        scene black with fade
        stop music fadeout (2.0)
        $ renpy.pause (2.0)

jump tld_day3
