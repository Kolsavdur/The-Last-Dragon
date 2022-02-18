#defining variables
init python:
    kol_tld_remysleep1 = False #Day 1
    kol_tld_remyvideogames = False #Day 2
    kol_tld_martinaccepted = False #Day 3
    kol_tld_remysleep2 = False #Day 3
    kol_tld_remytherapy = False #Day 4
    kol_tld_remytherapycounter = 0 #Day 4

    #Videogame Variables
    kol_tld_mckick = 6
    kol_tld_mckickcrit = 12
    kol_tld_mckickfail = 4
    kol_tld_mcpunch = 5
    kol_tld_mcpunchcrit = 10
    kol_tld_mcpunchfail = 2
    kol_tld_mcspecial = 8
    kol_tld_mcspecialfail = 3
    kol_tld_mcspecialcrit = 15

    kol_tld_remykick = 9
    kol_tld_remykickfail = 5
    kol_tld_remypunch = 6
    kol_tld_remypunchfail = 4
    kol_tld_remyspecialfail = 4
    kol_tld_remyspecial = 12

    kol_tld_mchealth = 100
    kol_tld_remyhealth = 100



    #Ending Variables
    kol_tld_endinga = False
    kol_tld_endingb = False
    kol_tld_endingc = False
    kol_tld_endingd = False
    kol_tld_endinge = False

    kol_tld_secretending = False

    #Route Selection Variables
    kol_tld_wtpchosen = False

    #Other Variables
    kol_tld_fruitsnackstaken = False
    kol_tld_fruitsnackskept = False


#custom sprites
image remy sleep = "cr/kolremy_sleeping.png" #crap
image remy angrycry = "cr/kolremy_angrycry.png" #crap
image remy cry = "cr/kolremy_cry.png" #crap
image remy lookcry = "cr/kolremy_lookcry.png" #crap
image remy shycry = "cr/kolremy_shycry.png" #crap
image remy startcry = "cr/kolremy_startcry.png" #crap

image logan normal = "cr/kollogan_normal.png"
image logan serious = "cr/kollogan_serious.png"
image logan smiling = "cr/kollogan_smiling.png"
image logan surprised = "cr/kollogan_surprised.png"
image logan thinking = "cr/kollogan_thinking.png"

image logan tnormal = "cr/kollogan_tirednormal.png"
image logan tserious = "cr/kollogan_tiredserious.png"
image logan tsmiling = "cr/kollogan_tiredsmiling.png"
image logan tsurprised = "cr/kollogan_tiredsurprised.png"
image logan tthinking = "cr/kollogan_tiredthinking.png"

image martin normal = "cr/kolmartin_normal.png"
image martin happy = "cr/kolmartin_happy.png"
image martin serious = "cr/kolmartin_serious.png"
image martin confused = "cr/kolmartin_confused.png"
image martin shocked = "cr/kolmartin_shocked.png"


#defining flip variations of custom sprites
image remy sleep flip = im.Flip("cr/kolremy_sleeping.png", horizontal=True) #crap
image remy angrycry flip = im.Flip("cr/kolremy_angrycry.png", horizontal=True) #crap
image remy cry flip = im.Flip("cr/kolremy_cry.png", horizontal=True) #crap
image remy lookcry flip = im.Flip("cr/kolremy_lookcry.png", horizontal=True) #crap
image remy shycry flip = im.Flip("cr/kolremy_shycry.png", horizontal=True) #crap
image remy startcry flip = im.Flip("cr/kolremy_startcry.png", horizontal=True) #crap

image logan normal flip = im.Flip("cr/kollogan_normal.png", horizontal=True)
image logan serious flip = im.Flip("cr/kollogan_serious.png", horizontal=True)
image logan smiling flip = im.Flip("cr/kollogan_smiling.png", horizontal=True)
image logan surprised flip = im.Flip("cr/kollogan_surprised.png", horizontal=True)
image logan thinking flip = im.Flip("cr/kollogan_thinking.png", horizontal=True)

image logan tnormal flip = im.Flip("cr/kollogan_tirednormal.png", horizontal=True)
image logan tserious flip = im.Flip("cr/kollogan_tiredserious.png", horizontal=True)
image logan tsmiling flip = im.Flip("cr/kollogan_tiredsmiling.png", horizontal=True)
image logan tsurprised flip = im.Flip("cr/kollogan_tiredsurprised.png", horizontal=True)
image logan tthinking flip = im.Flip("cr/kollogan_tiredthinking.png", horizontal=True)

image martin normal flip = im.Flip("cr/kolmartin_normal.png", horizontal=True)
image martin happy flip = im.Flip("cr/kolmartin_happy.png", horizontal=True)
image martin serious flip = im.Flip("cr/kolmartin_serious.png", horizontal=True)
image martin confused flip = im.Flip("cr/kolmartin_confused.png", horizontal=True)
image martin shocked flip= im.Flip("cr/kolmartin_shocked.png", horizontal=True)

#defining darkened version of character sprites
image remy sleep dk = im.Recolor("cr/kolremy_sleeping.png", 80, 80, 100, 255) #crap
image remy lookcry dk = im.Recolor("cr/kolremy_lookcry.png", 80, 80, 100, 255) #crap
image remy normal b dk =  im.Recolor("cr/remy_normal_b.png", 80, 80, 100, 255) #base game
image remy smile b dk =  im.Recolor("cr/remy_smile_b.png", 80, 80, 100, 255) #base game
image remy shy b dk =  im.Recolor("cr/remy_shy_b.png", 80, 80, 100, 255) #base game

image logan normal dk = im.Recolor("cr/kollogan_normal.png", 80, 80, 100, 255)
image logan serious dk = im.Recolor("cr/kollogan_serious.png", 80, 80, 100, 255)
image logan smiling dk = im.Recolor("cr/kollogan_smiling.png", 80, 80, 100, 255)
image logan surprised dk = im.Recolor("cr/kollogan_surprised.png", 80, 80, 100, 255)
image logan thinking dk = im.Recolor("cr/kollogan_thinking.png", 80, 80, 100, 255)

image logan tnormal dk = im.Recolor("cr/kollogan_tirednormal.png", 80, 80, 100, 255)
image logan tserious dk = im.Recolor("cr/kollogan_tiredserious.png", 80, 80, 100, 255)
image logan tsmiling dk = im.Recolor("cr/kollogan_tiredsmiling.png", 80, 80, 100, 255)
image logan tsurprised dk = im.Recolor("cr/kollogan_tiredsurprised.png", 80, 80, 100, 255)
image logan tthinking dk = im.Recolor("cr/kollogan_tiredthinking.png", 80, 80, 100, 255)





#defining characters
define Lg = Character(_("Logan"), color="#805546", image="logan")
define Mt = Character(_("Martin"), color="#e9cc86", image="martin")




#defining custom backgrounds
image koldesertcave = "bg/desertcave_kol.jpg"
image kolcitycentre = "bg/citycentre_kol.jpg"
image kolcitycentrestorm = "bg/citycentrestorm_kol.jpg"
image kolcityevening = "bg/cityevening_kol.png" #crap
image kolcitystorm = "bg/citystorm_kol.png"
image kolcitygate = "bg/citygate_kol.png"
image kolcitygatenight = "bg/citygatenight_kol.png"
image kolcitygatestorm = "bg/citygatestorm_kol.png"
image kolcitynight = "bg/citynight_kol.png" #crap
image kolfactory1 = "bg/factory1_kol.jpeg"
image kolfactory1night = "bg/factory1night_kol.jpeg"
image kolfactory2 = "bg/factory2_kol.jpeg"
image kolfactory2night = "bg/factory2night_kol.jpeg"
image kolfactory3 = "bg/factory3_kol.jpeg" #crap
image kolfactory3night = "bg/factory3night_kol.jpeg"
image kolfactory4 = "bg/factory4_kol.png" #crap
image kolfactoryout = "bg/factoryout_kol.jpg"
image kolfactoryoutnight = "bg/factoryoutnight_kol.jpg"
image kolfactoryoutstorm = "bg/factoryoutstorm_kol.jpg"
image kolguardtower = "bg/guardtower_kol.jpg"
image kolguardtowernight = "bg/guardtowernight_kol.jpg"
image kolloganhouse = "bg/loganhouse_kol.jpeg"
image kolloganhousenight = "bg/loganhousenight_kol.jpeg"
image kolloganhousestorm = "bg/loganhousestorm_kol.jpeg"
image kolloganhouseevening = "bg/loganhouseevening_kol.jpeg"
image kolloganout = "bg/loganout_kol.jpg"
image kolloganoutnight = "bg/loganoutnight_kol.jpg"
image kolloganoutstorm = "bg/loganoutstorm_kol.jpg"
image kolloganstudy = "bg/loganstudy_kol.png"
image kollogantv = "bg/logantv_kol.jpg"
image kollogantvnight = "bg/logantvnight_kol.jpg"
image kolmchouseday = "bg/mchouseday_kol.png"
image kolmchouseevening = "bg/mchouseevening_kol.png"
image kolmchousenight = "bg/mchousenight_kol.png"
image kolmchousestorm = "bg/mchousestorm_kol.png"
image kolnightdesert = "bg/nightdesert_kol.jpg"
image kolremyhouse = "bg/remyhouse_kol.jpeg"
image kolremyhouseout = "bg/remyhouseout_kol.jpg"
image kolwatertank = "bg/tank_kol.jpg"
image kolwtp1 = "bg/wtp1_kol.jpeg"
image kolwtp1night = "bg/wtp1night_kol.jpeg"
image kolwtp2 = "bg/wtp2_kol.jpeg"
image kolwtp3 = "bg/wtp3_kol.jpg" #crap
image kolwtp3night = "bg/wtp3night_kol.jpg"
image kolwtp4 = "bg/wtp4_kol.jpeg" #crap
image kolwtp4night = "bg/wtp4night_kol.jpeg"
image kolwtpout = "bg/wtpout_kol.png"
image kolwtpoutnight = "bg/wtpoutnight_kol.png"
image kolwtpoutstorm = "bg/wtpoutstorm_kol.png"
image kolwtproof = "bg/wtproof_kol.jpg"




#defining custom character graphics
image kolremya = "cg/remy_a_kol.jpg"
image kolremye = "cg/remy_e_kol.jpg"
image koldarkclouds = "cg/darkclouds_kol.jpg"

#defining credits
image kolcredits1 = "cg/koltldcredits1.png"
image kolcredits2 = "cg/koltldcredits2.png"



#Music and Sound effects that are going to be added to CRAP

#mx

#crapattack.ogg
#crapbelieve.ogg
#crapcouch.ogg
#crapexile.ogg
#craphope.ogg
#craploss.ogg
#crapprotocol.ogg
#crapsaviour.ogg
#crapstride.ogg
#crapsubmergedforest.ogg
#crapsurge.ogg
#crapvanished.ogg
#crapwarp.ogg


#fx

#crapdrill.wav
#craphammer.wav
#craphighvoltzap.wav
#crapmagnetzap.wav
#craptinyexplode.wav
#crapwind.wav
#crapzap.wav
