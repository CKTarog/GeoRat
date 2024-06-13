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

label baguioStory:
    hide screen startBaguio

    show sprite ronald at height
    "Strawberries.."
    "Daniel has the file for this.."

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
    