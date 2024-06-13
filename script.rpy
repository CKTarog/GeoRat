# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define W = Character("W", style="name_ronald")
define NS = Character("Neutral Special", style="name_neutral")
define P = Character("Plu", style="name_plu")
define DB = Character("Dori", style="name_dori")
define K = Character("Kofu", style="name_kofu")
define PP = Character("Phythalum", style="name_phythalum")
define D = Character("Dash", style="name_dash")

transform height:
    xalign 0.5
    yalign 0.2
transform neutral:
    xalign 0.5
    yalign 0.5

# The game starts here.

label start:
    scene bg room
    
    show sprite ronald at height
    # These display lines of dialogue.
    W "Welcome to GeoRat."
    W "Oh may wa moo... Shin day roo..."
    hide sprite ronald

    show sprite plu at height
    P "I SEE YOU HIDING IN THIS CORNER RONALD!!!"
    hide sprite plu 

    show sprite dori at height
    DB "Ronald you're cooked"
    hide sprite dori

    show sprite neutral at neutral
    NS "Hey, have you guys seen my wife?"
    NS "I miss her a lot."
    NS "Plea-"
    hide sprite neutral

    show sprite phythalum at height
    PP "WAH WAH WAH"
    PP "I DON'T WANNA FLIPPIN' HEAR IT!"
    hide sprite phythalum

    show sprite dash at height
    D "Yo silence! I wanna hear my cousin get cooked lol"
    hide sprite dash

    show sprite ronald at height
    W "YOOOOOOOOOUCH!!!"
    hide sprite ronald

    show sprite kofu at height
    # K "..."
    # K "The game literally hasn't started yet and your roles and appearances is not this early."
    # K "Also Neutral get back to work."
    K "So far WcRonald is the only one that should appear in this scene where in the world did you guys come from???"
    # K "ahem"
    # K "Anyway, welcome to GeoRat, as said, this game is still under development. Please come back at a later time."
    hide sprite kofu
    #calls the mapScreen

    call screen mapScreen
    
label startDialogue:
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # its supposed to be ronald but changing it doesnt work for some reason - CK
    return

label manilaStory:
    hide screen startManila

    # "The warm wind blows into your face as you seemingly have drifted to sleep."
    # "Hearing rustling nearby, you stir awake combined with the now faint noises of a crowd."
    # "..."

    show sprite ronald at height
    W "Oh hey yo, traveler!!"
    W "Man! I thought you were never gonna wake up!"
    
    "Oh hey Ronald, my bad, I feel asleep"
    "Must've not slept enough last night..."

    W "That's alright! You make sure you take care of yourself though traveler!"
    
    "By the way Ronald,"

    W "What's up?"

    "Why are we on a mountain?"

    W "I don't know, you were walking in your sleep and I followed."

    "I WAS WHAT AND YOU WHA-"
    hide sprite ronald


    show sprite phythalum at height
    PP "GET OUT OF MY SECRET TRAINING GROUNDS YOU ASSHATS!!"
    hide sprite phythalum
    # This ends the game.

    return
label baguioStory:
    hide screen startBaguio

    show sprite ronald at height
    "Strawberries.."
    "That's a lot of strawberries..."
    W "There sure is!"
    show sprite kofu at height
    K "Berries???"
    show sprite phythalum at height
    PP "no..you're not turning my head into 90 percent berries again Kofu, no..."

    return

label kantoStory:
    hide screen startKanto

    show sprite ronald at height
    W "oh hey yo japan!"
    W "Quiet a lot of non-asians here!"
    show sprite plu at height
    P "RONALDDDD"

    return
label kyotoStory:
    hide screen startKyoto

    scene bg streets

    "As you walk the unfamiliar streets of Japan, you hear rustling from a distance."
    "As you approach the noise, you see that it leads somewhere into the bushy realm."
    "Suddenly, you hear noises of a person, along with a growl of an animal."
    "Curious, you proceed to take a peek to see the situation, then you see-"
    scene bg kyoto

    show sprite phythalum at height
    PP "YOU'RE NOT GETTING AWAY THIS TIME!!"
    PP "CURSED DOG!!"
    

    return
label osakaStory:
    hide screen startOsaka

    scene bg room

    show sprite kofu at height
    K "Shizuku Osaka"
    K "no..."
    K "This is Mumei's house"
    show sprite dori at height
    DB "Love, I'm pretty sure you aren't supposed to be here..."
    show sprite kofu at height
    K "Yea, I don't think you are supposed to either"

    return

label seoulStory:
    hide screen startSeoul

    scene bg room

    show sprite ronald at height
    W "These signs don't look chinese or japanese to me!"
    W "What language do you think it is traveler?"

    "hmm..."
    "I'm pretty certain that its..."

    show sprite dash at height
    D "YO COUSIN!"
    show sprite ronald at height
    W "Oh my god!"
    W "Is that my cousin??"
    W "Don't worry traveler! He probably knows the area! We're saved!"
    show sprite dash at height
    D "I'm killing you"
    show sprite ronald at height
    W "Nevermind, we're not-"
    W "YOOUUUCHHHHH!!!"

    return

label deaguStory:
    hide screen startDeagu

    scene bg room

    show sprite dash at height
    D "look, all I know is the convience store, the transportation, and my house."
    D "Now leave me alone."
    show sprite ronald at height
    "yea ronald, I'm not sure if we should pursuade him any further-"
    W "But cousin!!"
    W "Can we at least stay for one day at your house"
    show sprite dash at height
    D "No!"
    D "You'd make a mess so no!"
    show sprite ronald at height
    W "Don't worry cousin! We won't-"
    show sprite dash at height
    D "DON'T. SAY. THAT."

    return

label busanStory:
    hide screen startBusan

    scene bg room

    show sprite ronald at height
    W "Look! That looks like a convenience store!"
    W "Let's stop by and rest there traveler!"
    W "And also buy some food! Man, I'm starving!"
    "(Entering the store, you hear a distressed sound)"
    "???" "WHYYYY"
    "huh...?"
    show sprite dori at height
    DB "d-do you want to buy one..?"
    show sprite kofu at height
    K "no...I still have some at home..its just...."
    K "WHY IS MY FAVORITE POCKY IN A KOREAN MART INSTEAD"
    show sprite ronald at height
    W "damn those people are making a ruckus huh?"

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

    