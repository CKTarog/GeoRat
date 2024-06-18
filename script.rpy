# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define W = Character("Ronald", style="name_ronald")
define NS = Character("Neutral", style="name_neutral")
define P = Character("Plu", style="name_plu")
define DB = Character("Dori", style="name_dori")
define K = Character("Kofu", style="name_kofu")
define PP = Character("Phythalum", style="name_phythalum")
define D = Character("Dash", style="name_dash")
define MC = Character("???", style="mystery_character")

transform height:
    xalign 0.5
    yalign 0.2
transform neutral:
    xalign 0.5
    yalign 0.5

# The game starts here.

label start:

    call screen mapScreen
    
label startDialogue:

    return

label boholStory:
    hide screen startBohol

    scene bg forest
    show sprite ronald at height
    W "Oh hey yo, traveler!!"
    W "Man! I thought you were never gonna wake up!"
    
    "Oh hey Ronald, my bad, I feel asleep"
    "Must've not slept enough last night..."

    W "That's alright! You make sure you take care of yourself though traveler!"
    
    "By the way Ronald,"

    W "What's up?"

    "Why are we in a jungle?"

    W "Oh right"
    W "You were sleep walking and as a good friend I am, I followed you!"

    "I did what?"
    "And you didn't bother to wake me up?"

    W "Nope!"
    W "You were sleeping so peacefully, and a good friend wouldn't wake their friends up"

    "Well if you say it like that I guess?"
    "Well for now our problem is how to get out of here."   
    "Ronald do you remember how to leave? Since you followed me and all that."
   
    W "Ermm..."
    W "I..... forgot?"

    "..."

    W "Well anyway let's start looking around and explore!"
    W "We might find our way out here!"

    "Ok..."

    W "Maybe we should go over the hills, that way we'll have a nice view and see where we need to go!"

    "I suppose."
    "But a hill's a hill."
    "It would be pretty tiring."

    W "Nonesense!"
    W "It's better we get out of here than not, and the hill's the only way."

    "(Maybe if you woke me up whe I was sleepwalking we wouldn't be here in the first place, but oh well.)"
    "Fair point..."

    hide sprite ronald

    "*We began our journey going to the hill"
    "*In it's own way it's pretty nice journeying with Ronald*"
    "*Everything was going fine until...*"
    
    show sprite ronald at height
    W "Wowza!"

    "!!!"
    "What happened?!"

    W "There is a little gremlin thing on the tree over there!"
    hide sprite ronald
    "*Ronald points where the gremlin he saw was*"
    scene bg tarsier
    "Woah it has large eyes and a small body..."

    W "It looks both cute and terrifying at the same time"

    "Wait a minute..."
    "I've seen this creature before"
    "This is a Tarsier..."

    W "Tar sheer?"

    "Close enough Ronald."
    "This is a Tarsier which is found in the Philippines, mainly in Bohol!"
    "..."
    "Ronald..."

    W "Yes?"

    "Just to confirm. You said I sleepwalked my way over here, and you followed?"

    W "You are so right!"

    "..."

    "*I let out a heavy sigh*"
    "Sorry, I'm stilll in disbelief that esomething like this actually happened."

    W "Well cheer up we'll eventually find our way out of this jungle."

    "Ronald if you aren't Ronald I would've been so mad over you..."

    W "What do you mean by that?"

    "It's fine Ronald."

    hide sprite ronald
    "*We managed to reach the top of the hill*"
    scene bg chocolateview

    W "This view is fire, and look there are even more similar hills!"

    "Yeah the view's really amazing up here, especially the hills. Even if we're on top of one right now"
    "(The view is truly amazing for our eyes)"
    show sprite ronald at height
    "But.. I feel like I'm starting to forget something important..."

    W "If you forgot about it, it must not be important!"

    "Yeah I guess you're ri-"
    "We're still lost Ronald"

    W "oh right."

    "We really need to go before things go dark."
    "I know that it's still the morning but you'll never know how long we might be stuck here."
    "If only I didn't sleepwa-"
    hide sprite ronald

    MC "You lost?"

    "*A mysterious voice comes from behind*"
    show sprite phythalum at height
    "*A ninja reveals himself*"

    "Yes we are..."
    "(I was about to ask if he was a local but a ninja in the Philippines doesn't make any sense)"
    MC "I see, it's not everyday that I see lost travelers over here."
    MC "Did you disobey  your tour guide or something and decided to not only see the Chocolate Hills upclose, but climb it as well?"

    "Oh! We're in the Chocolate Hills???"

    MC "Yup. The Chocolate Hills of Central Visayas Bohol."
    MC "The one and only."
    
    W "Ermm... Why is it called the 'Chocolate Hills'?"
    W "Can we eat this? It doesn't look sweet though..."

    MC "You're friend is quite the character huh."
    MC "As of right now they look green, but in the dry season this green grass would change color."
    MC "The green grass will turn into a chocolate-brown like color, hence their names the Chocolate Hills."

    "Woah, that's really fascinating..."
    "Oh right. Uhh sir..."
    "Could you help us find our way out of here sir?"

    MC "Yes, I know this Jungle like the back of my hand."
    PP "Oh and by the way my name is Phythalum, but you can call me Phyth."

    "Oh thank you Phyth."
    "My name is-"

    PP "it's fine I don't need to know your names. After all I'm still a stra-"

    show sprite ronald at height
    W "And my name is Ronald!"
    "(As he said that he looks very proud of himself)"
    PP "..."
    "..."

    show sprite phythalum at height
    PP "Really quite the character..."

    "A-anyway so can you please guide us?"
    PP "Oh I won't be guiding you unfortunately."

    "But you said you'll he-"

    PP "Let me finish, I'm a busy person mate, I have things I need to do."
    PP "And I can only give you directions."

    "Oh, that's enough for us."    

    PP "Very well listen closely and make sure you don't forget."

    hide sprite phythalum
     
    "*Phythalum begins telling us the directions with precise details on how to get out of this place*"

    show sprite phythalum at height
    PP "That should be just about it."

    "Thank you so much."

    show sprite ronald at height
    W "Ari ga toe!"

    show sprite phythalum at height
    PP "Don't sweat it, oh and one more thing..."
    PP "Becareful of the wildlife here, not all are friendly like the Tarsier you saw earlier."

    "Oh thanks for the heads up-"
    "Wait... How did you know about the Tarsie-"

    PP "Well I got to go now."
    PP "Goodbye and be safe!"
    PP "Emelipto Umuroi!"
    
    hide sprite phythalum
    "*He left so fast we didn't even see where he went.*"
    "No... vanish is the more appropriate term here, he just vanished..."

    "Hey Ronald."

    show sprite ronald at height
    W "Uhuh?"

    "What did he say? And what does it mean?"

    W "I'm pretty sure he told us to stay safe and gave his goodbyes."

    "No not that, the-"
    "Y'know what? Nevermind what I mentioned."

    W "Ok."

    "I envy how enthusiastic you are sometimes."
    "('Emelipto Umuroi'. What do those words mean?)"

    "Ok let's get going now Ronald before the mosquitoes appear and suck our blood."

    W "Yikes, I don't like mosquitoes."

    "Yeah yeah I know." 

    "*Me and Ronald traverse our way through the jungle as instructed by Phythalum.*"
    scene bg forest
    "Ah where do we go again when we're here?"

    W "Ermm... I don't know I didn't listen."

    "..."
    "I worry for you a lot of times."
    "Oh I remember now, follow me."

    W "I knew I could rely on you!"

    "You always rely on me though..."

    "Anyways we're probably almost there now."

    "Woah a path!"
    scene bg path
    show sprite ronald at height
    W "Wahoo!"

    "Ok let's get going"

    MC "Hey..."
    MC "You shouldn't really be going wandering out of the path, the guards might get mad at you you know?"

    "*A voice cames from behind us*"

    show sprite neutral at neutral
    MC "Geez be glad that I'm just some passerby, otherwise I'd probably file you or something"

    "Oh we're sorry, it's a long story on how we got into that situation."

    MC "Well everyone has their stories to share."
    MC "You lost or something?"
    
    "Well we were lost earlier, but we found our way back."

    MC "Oh and by the way, the name's..."
    MC "Neut-"
    show sprite ronald at right
    W "NUTELLA!!!"
    show sprite neutral at neutral
    NS "RONALD FOR THE LAST TIME IT'S NEUTRAL!"

    NS "Wait Ronald?"
    
    show sprite ronald at right
    W "Yes!"
    show neutral at neutral
    NS "Huh, didn't expect find you here." 
    NS "I'm assuming you're his friend I've been hearing about."

    "Yea.. I guess."

    NS "Glad you're safe from the jungle, things can get pretty nasty there."
    NS "Atleast you weren't bitten by a Samar Cobra"

    "Samar cobra?"

    show sprite ronald at height
    W "the Samar cobra is um erm.. a very dangerous snake yes!"

    show sprite neutral at neutral
    NS "..."
    NS "I feel bad for you putting up with this man."
    W "Awwww"
    NS "Anyways the Samar Cobra is in fact a dangerous snake and a cobra as the name suggests."
    NS "It is found in the Southern Philippines and also in Bohol."
    NS "It is highly venomous so thankfully you guys didn't get bitten by it while in the jungle."
    NS "It also has a bright yellow head, so it can easily be noticed in the jungle."
    
    "Didn't even think of snake existing in the Philippines."
    
    NS "Anyways I'll go continue my search for now, if you don't need anything."
    
    "Search? What are you searching for?"

    NS "Oh right I forgot to ask you guys, have you seen my wife by any chance while you were in the jungle?"

    show sprite ronald at height
    W "Nope"

    "There was almost no other people there"
    show sprite neutral at neutral
    NS "I see..."
    "Ah right"
    NS "?"
    "Do you know what the term \"Emelipto Umuroi\" means?"
    NS "..."
    NS "You met Phythalum in the jungle didn't you?"
    NS "And he's the reason you found your way over here."
    "Uh yes that's exactly how it went."
    "You know him?"
    NS "We have our own history."
    NS "Here's an advice from an old friend of his."
    NS "Don't trust every word he says."
    "ok?"

    NS "Despite no longer being lost in the jungle you folk still seem lost."
    NS "Want me to tour you?"

    "Is that really fine?"

    NS "Tis' fine, consider this as the start of our friendship Ronald's friend."
    W "yay!"

    NS "Come on let's go visit some tourist spots"

    "Thanks..."

    NS "Still anxious?"
    NS "Well I don't blame you, in your perspective I'm just some random perosn you met."
    NS "But I'm also a friend of Ronald and I've been freinds with him for over years now."

    show sprite ronald at height
    W "You're so right Neutal"

    show sprite neutral at neutral
    NS "..."
    NS "Even if he misspells and mispronounces my name, he's still my firend and he trusts me as his friend."
    NS "So you wanna go for a tour?"
    NS "Don't worry I know how to drive."
    NS "You can even learn more about Bohol in the process."
    "Yea sure that sounds fun."
    NS "So it's decided then."
    show sprite ronald at height
    W "Yipee!"
    hide sprite ronald

    "*Me and Ronald follow Neutral to his car*"
    scene bg car 
    "*We talk of our experience and our life while on the car ride*"
    "*We had fun talking, then the talking needed to end as we arrive to our destinations.*"

    show sprite neutral at neutral 
    NS "First destination is this shrine."
    scene bg shrine
    "Woah, it must have some important meaning if it's a tourist spot right?"
    NS "Yup"
    W  "Wow, these looks like 5 men eating and 1 disabled guy!"
    NS "It's known as the \"Blood Compact Shrine\" of Bohol"
    NS "It basically commemorates the blood compact a historical event."
    NS "It basically symbolizes the first treaty of friendship and alliance between Filipinos and Spaniards."
    "Wow that's interesting."
    NS "Ye Filipinos and Spaniards were always at each others neck back in the past."
    NS "So it's nice to know that Filipinos and Spaniards were able to find peace with one another."
    NS "Let's go to our next stop shall we?"
    hide sprite neutral
    "*We go back to Neutral's car*"
    scene bg car
    "(We're happy conversations once more)"
    "(Ronald is so excited for ou next stop it really brightens the mood)"

    show sprite neutral
    NS "Here we are."
    NS "We'll be quick with this since we're just gonna be here for the seeing."
    NS "This is Baclayon Church"
    scene bg baclayonchurch 

    "But what is it that makes this pretty popular?"

    W "YE, it's just a church."
    show sprite neutral at left
    NS "Well it's one of the oldest church the Philippines has to offer dating back to 1727. It's still structurally original and still with authentic materials."
    "Woah, that's really old."
    "So it's been there for more than a 100 years huh?"
    W "Wow that's way older than we are combined!"
    "Yeah."
    show sprite neutral at left
    NS "Welp let's go to our final stop before the sun sets."
    "Alright then, come on Ronald!"
    show sprite ronald at height
    W "Yipee!"
    hide sprite ronald
    scene bg car
    
    "(Maybe sleepwalking to the forest wasn't so bad.)"
    "(If it wasn't for that me and Ronald wouldn't have gone to so many place and learnt so many things.)"

    "Wait a minute..."
    show sprite ronald at right
    W "Hm?"
    "Aren't we going back to the Chocolate Hills?"
    NS "Yup we are!"
    "Why?"
    NS "you'll see..."
    NS "Anyways while we're on our way there let's recap what you've learned of Bohol shall we?"
    "Oh ok sure!"
    W "Nah I'd win!"

    "*Finally we arrived to the same place but not exactly*"

    NS "Now let's take a look at this view"
    scene bg endhill

    W "WOW!"
    W "It look so beautiful!"
    "Yeah the suneset looks so amazing with the Chocolate Hills."
    NS "Me and my wife used to go enjoy this view, glad you guys enjoyed it as well."
    show sprite ronald at right
    W "Wow..."
    W "I guess this truly was our GeoRat..."
    "..."
    "Ronald wha-"
    return

label kantoStory:
    hide screen startKanto

    #Station
    scene bg black
    "..."
    "(Awfully quiet, you feel slight shaking on where you are seated)"
    "(The silence doesn't last as you then hear a person speak, seemingly making an announcement...)"
    "(Announcement..?)"

    scene bg intrain
    "(You realize you two have missed your stop.)"
    "Ronald!"
    W "*honk shoo*"
    "Ronald wake up we missed our stop!"
    W "whuh-"

    show sprite ronald at height
    W "*Ronald slowly sits up properly on his seat as he stirs awake.*"
    W "M-missed our stop? For real??"

    "(As you we're about to answer, you we're cut off by the train announcer's voice.)"
    hide sprite ronald

    "Announcer " "Arriving at...Harajuku Station.."

    show sprite ronald at height
    W "Wait really?? There's no way!"
    "Yea, here look at the station map!"
    hide sprite ronald

    show station map at height
    "(You open the station map provided in almost every station you go to at Japan.)"
    "(It looks intimidating at first glance, but you think it shows just how complex the train system is here in Japan)"
    hide station map
    show station map harajuku at height
    "(Showing the map to Ronald, you point along the green line to show that we missed our stop in Meguro)"
    W "You're right!!"
    hide station map harajuku

    show sprite ronald at height
    W "Erm...what should we do??"
    "For now let's get off this stop at least."
    hide sprite ronald

    scene bg harajuku station
    "(The both of you get off at the stop)"
    show sprite ronald at height
    menu:
        W "Okay! Now what do we do?"
        "Explore a bit.":
            "Let's go explore a bit how about, we haven't been here, I'm quite curious."
        "Go find a place to eat":
            "Hey Ronald, I'm kind of hungry. Wanna find a place to eat?"
    
    W "Oh! Sure thing!"
    "I think the exit is..."
    W "Oh hey! Buddy!"
    hide sprite ronald
    "Huh? What?"
    W "There's signs here! Hmm, this says.."
    show station ad at neutral
    "Ronald.."
    W "Erm..."
    "We can't read this country's language."
    W "Oh, I forgot!"
    "Also, that doesn't seem to be a station sign Ronald, station signs should have english translations on them for tourists"
    W "Oh, what is this then?"
    "It might just be an advertisement poster."
    hide station ad
    "Look, it says 'West Exit' over there"
    W "Why is it specifically the 'West Exit'? Theres multiple exits?"
    "Probably, but, an exit's an exit so let's go."

    scene bg black
    "(The two of you make you're way out of Harajuku Station through the West Exit)"
    "(Exiting, you both are at awe of what greets you)"

    "Woah, Ronald"
    W "Yea...what is that??"
    "Wanna check it out?"
    W "Are we allowed to??"
    "I mean, it looks like many other people are going in as well so I think it is."
    "We'll find out I guess"
    W "Okay then! Let's go!"

    scene meiji shrine
    W "That structure is huge! That's cool!"
    "Yea, it looks old as well, it must've been here for so long."
    MC "Indeed, it's been here for around 109 years."
    W "And it hasn't broken since?"
    "Wait-"
    W "Wait a minute.."
    show sprite plu at height
    "Where did you come from??"
    W "Woah who are you??"
    P "Plu."
 
    W "Oh.. well uh, I'm Ronald and this is my friend!"
    "(Observing the stranger named Plu, nothing seems out of the ordinary other than the ears...)"
    P "Nice to meet the two of you, I assume you two are tourists?"
    W "Yep! We just wanted to check this cool place out!"
    P "Quite the place isn't? To answer you're question earlier,"
    hide sprite plu
    "(Plu starts walking into the place and the two of you follow with.)"
    "(But before entering, Plu stops in his tracks and bows his head before continuing inside)"

    scene inside meiji shrine
    "(Suddenly, you two have a free tour guide it seems..)"
    P "This shrine has been up since 1920. Also that 'structure' is called a 'Torii Gate'"

    menu:
        W "Oh so this is a shrine!"
        "Torii gate?":
            menu:
                P "Yes, Torii gates are what greets you at entrances of shrines."
                "Why was it built?":
                    P "It was built in honor of the first emperor, Emperor Meiji and his wife, Empress Shoken. Thus, this shrine is called the 'Meiji Shrine'"
        "Why was it built?":
            menu:
                P "It was built in honor of the first emperor, Emperor Meiji and his wife, Empress Shoken. Thus, this shrine is called the 'Meiji Shrine'"
                "Torii gate?":
                    P "Yes, Torii gates are what greets you at entrances of shrines." 
    show sprite ronald at height
    W "Woah that's cool!"
    show sprite plu at height
    P "Indeed, it's quite the popular place to visit here in Tokyo."
    "Interesting, why did you bow before entering earlier?"
    P "The both of you are not locals, so it is forgiven that you guys don't follow with but,"
    P "As shrines are sacred places, people often bow before entering its gates to show respect."
    W "Oh, I did not know! I'm so sorry!"
    "He said it's alright not to Ronald, since we aren't from here"
    P "Yeah, don't worry too much. Let's go further inside and hurry to the shrine"
    hide sprite plu


    scene further inside shrine
    "(You and the others walk further inside for a long while, this shrine is really big!)"
    W "Damn, we've been walking for a while and we aren't at the shrine yet?"
    W "Wait...so there's the actual shrine inside?"
    P "Yes, this is just the entrance and the way to the shrine."
    "Now I see why you said to hurry."
    W "Yeah, or we would be here much longer!"
    P "Well, not exactly my reasons."


    scene meiji near shrine
    P "Usually, shrines as popular as these have long lines. So if you'd want to visit, its best to have the patience to wait when lines are long."
    W "Oh damn! I hope it isn't that long right now!"
    P "Since it isn't exactly a notable date today, it might not be."
    "What times would the lines to the shrine be long?"
    show sprite plu at height
    P "New Years definitely. They would be extremely long actually, the longest it ever will be."
    show sprite ronald at height
    W "Oh, Why is that?"
    show sprite plu at height
    P "It is tradition to the people here to visit a shrine and pray for their wishes and blessing for the new and upcoming year. Theres also the proper etiquette to pray in shrines."
    hide sprite plu
    P "And look, seems like the line isn't that long today. Let's go."

    scene shrine front
    "(You arrive at the shrine, waiting in a short line you realize something..)"
    show sprite ronald at height
    "(As you glance at Ronald behind you, you see that he seems to have realized the same thing..)"
    show sprite plu at height
    W "Hold on Plu! I forgot!"
    P "What is it?"
    "(The shine nears, as the people in front leaves one by one after praying at the shrine)"
    "We don't know how the proper etiquette to pray to a shrine"
    "(As the question was late, you three find yourselves already in front of the shrine where people pray at)"

    P "Don't worry, its simple, just listen carefully and follow what I say:"
    P "Memorize: Shake the rope to ring the bell, Throw a coin into the offertory box, Bow twice, Clap twice, Pray, and Bow one final time"
    menu:
        P "Ready?"
        "Come again?":
            W "One last time Plu."
            menu:
                P "Memorize: Shake the rope to ring the bell, Throw a coin into the offertory box, Bow twice, Clap twice, Pray, and Bow one final time"
                "Pray":
                    jump choice_pray
        "Pray":
            jump choice_pray

#praying minigame
label choice_pray:
    P "Let's pray."
    hide sprite plu
    menu:
        "(First...)"
        "Throw coin into box.":
            jump choice_wrong
        "Shake rope":
            "(You shake the rope to ring the bell.)"
            menu:
                "(Second...)"
                "Clap twice.":
                    jump choice_wrong
                "Throw coin into box.":
                    "(You throw a coin into the offertory box)"
                    menu:
                        "(Third...)"
                        "Bow twice":
                            "(You bow twice at the shrine)"
                            menu:
                                "(Fourth...)"
                                "Clap twice":
                                    "(You clap twice)"
                                    menu:
                                        "(Fifth..)"
                                        "Bow":
                                            jump choice_wrong
                                        "Pray":
                                            "(You close your eyes and pray for a good time at your stay in Japan)"
                                            menu:
                                                "(Last..!)"
                                                "Bow":
                                                    jump pray_done
                                "Bow":
                                    jump choice_wrong

                        "Clap twice.":
                            jump choice_wrong

#wrong choice
label choice_wrong:
    show sprite plu at height
    P "That's wrong. Try again."
    #goes back to start of minigame
    jump choice_pray

#minigame done/rest of story continues
label pray_done:
    "(You bow at the shrine one last time)"
    show sprite plu at height
    P "Looks like you guys are done praying. Good job!"
    show sprite ronald at height
    W "Woohoo! That was tough."
    "Surprised I remembered all of it."
    show sprite plu at height
    P "People are waiting, let's go and walk again to exit the shrine now."
    show sprite ronald at height
    W "That was nice to visit! Let's go friend!"
    hide sprite ronald
    "(You all leave the shrine and make the long journey back out Meiji Shrine)"

    scene shrine wedding
    "(Walking back, there seems to be a line of people walking past at front)"
    "(Stopping at your track, you notice Ronald continuing forward but mesmarized by the sight.)"
    "(He's about to bump right into the people. You yank him back to avoid it.)"
    "(But someone else had already done so first.)"
    W "Woah!"
    MC "Dude, careful, you we're about to hit them."
    W "Thanks Plu! What are they doing though? They're dressed up quite formally."
    P "That's a wedding"

    W "Woah! It's a wedding?? That's fire!"
    MC "Yea, and you're pretty lucky to witness one randomly."
    W "No way! Really? Now that's more fire!!"
    "Wait really?? Right here?"
    "Wait no. Who are you??"
    show sprite phythalum at height
    "And where did Plu go??"
    W "Woah! A ninja???"
    MC "Emelipto Umuroi"
    "Huh?"
    W "Where's Plu?"
    PP "Look I don't know who this Plu guy is other than I'm not the guy, but call me Phythalum."
    W "And I'm Ronald!"
    "Oh hey, Plu was just here earlier."
    W "He was the one that mentioned this was a wedding!"
    "Grey hair, with ears-"
    PP "I don't see no other guy than the two of you so I don't know what you're on about."
    PP "Anyway, yes this is indeed a wedding."
    PP "Sit still and wait for them to pass or you'll disturb."
    hide sprite phythalum
    "(You watch the line of people apparently part of a wedding slowly pass by..)"

    scene further inside shrine
    "(As the people have passed by, you three continue walking towards the exit of the shrine..)"
    W "So..."
    W "Weddings can happen in shrines?"
    PP "Yes, this shine specifically hosts dozens of traditional Japanese weddings"
    W "That's cool!"

    scene inside meiji shrine
    W "But..."
    W "Where is Plu?"
    PP "Look man, I really don't know who this Plu guy is. What was it?"
    PP "I didn't see anyone with grey hair and with ears-"
    PP "Wait.."
    PP "Ears?"
    "Yes, ears."
    W "Oh right! He did have ears."

    scene meiji shrine
    show sprite phythalum at height
    PP "Dude"
    PP "You met a kitsune spirit or something?"
    show sprite ronald at height
    "Kitsune spirit?"
    W "What's a kitsune?"
    show sprite phythalum at height
    PP "Basically fox spirits. These are common stories revolving around shrines where there are spirits, maybe commonly fox spirits, that reside in the shrine."
    "Wait so if they're a spirit.."
    W "Aren't they technically ghosts?"
    PP "Yes, Ronald, you can say that."
    show sprite ronald at height
    W "So...we met a ghost?"
    "..."
    W "Damn! That's cool!"
    show sprite phythalum at height
    PP "Least expected you to be freaked out but alright."
    PP "Well, alright, it's time I leave"
    PP "Phythalum, out."
    hide sprite phythalum
    "(The ninja named Phythalum dissapears just like that)"
    show sprite ronald at height
    "You're not bothered we met a ghost??"
    W "Well, Plu was pretty cool!"
    "I guess you could say that. He did educate us after all."
    W "Yup. And teach us how to pray!"
    "That as well, well then, stations right there."
    W "Oh right! I almost forgot! Let's go-"
    "(Ronald's sentence is cut off by a roar of someone's stomach)"
    W "Eat somewhere first how about. Man, I'm starving!"
    "Sure thing, let's just hope we don't get lost."

    # This ends the story and returns to map screen.
    return


style name_ronald:
    color "#ffffff"
    outlines [(7, "#cc1414", 0, 0)]
    size 40

style name_neutral:
    color "#ffffff"
    outlines [(7, "#b215c7", 0, 0)]
    size 40

style name_phythalum:
    color "#ffffff"
    outlines [(7, "#000000", 0, 0)]
    size 40

style name_plu:
    color "#ffffff"
    outlines [(7, "#777777", 0, 0)]
    size 40

style name_dash:
    color "#ffffff"
    outlines [(7, "#ffa600", 0, 0)]
    size 40

style name_kofu:
    color "#ffffff"
    outlines [(7, "#ffd000", 0, 0)]
    size 40

style name_dori:
    color "#ffffff"
    outlines [(7, "#ee62d0", 0, 0)]
    size 40

style mystery_character:
    color "#ffffff"
    outlines [(7, "#000000", 0, 0)]
    size 40
    