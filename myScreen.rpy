label myScreen:

screen mapScreen:
    tag menu
    add "map_normal.png"  
    frame:
        xalign 0.0
        yalign 0.0
        style_prefix "red"
        textbutton _("Return") action Return()
        
    text "Choose a country":
        xalign 0.92
        yalign 0.5 
        size 50

    #ph
    imagebutton:
        xpos 939
        ypos 735
        idle "map_philippines.png"
        hover "map_philippines_hover.png"
        action ShowMenu("philippines")

    #jp
    imagebutton:
        xpos 978
        ypos 84
        idle "map_japan.png"
        hover "map_japan_hover.png"
        action ShowMenu("japan")

#ph
screen philippines():
    tag menu
    add "map_ph.png"
    frame:
        xalign 100
        yalign 100
        textbutton "Return" action Return()
    text "Choose an Island":
        xalign 0.9
        yalign 0.5
        size 50
    
    #visayas
    imagebutton:
        xpos 626
        ypos 404
        idle "map_visayas_idle.png"
        hover "map_visayas_hover.png"
        action ShowMenu("visayas")
    
#jp
screen japan():
    tag menu
    add "map_jp.png"
    frame:
        xalign 100
        yalign 100
        textbutton "Return" action Return()

    text "Choose prefecture":
        xalign 0.9
        yalign 0.5
        size 50

    #kanto
    imagebutton:
        xpos 740
        ypos 500
        idle "japan_kanto_idle.png"
        hover "japan_kanto_hover.png"
        action Show("startKanto")
        
screen visayas():
    tag menu
    add "map_visayas"
    frame:
        xalign 100
        yalign 100
        textbutton "Return" action ShowMenu("philippines")

    text "Choose a city":
        xalign 0.9
        yalign 0.5
        size 50

    #bohol
    imagebutton:
        xpos 733
        ypos 705
        idle "visayas_bohol_idle.png"
        hover "visayas_bohol_hover.png"
        action Show("startBohol")

#ph-visayas-bohol
screen startBohol():
    modal True
    image "visayas_bohol_hover.png":
        xpos 733
        ypos 705
    frame:
        xalign 0.98
        yalign 0.5
        padding(200,200,200,200)
        vbox:
            text "BOHOL"
            textbutton ">Start":
                action Jump("boholStory")
            textbutton ">Back":
                action Hide("startBohol")
        
screen startKanto():
    modal True
    image "japan_kanto_hover.png":
        xpos 740
        ypos 500
    frame:
        xalign 0.98
        yalign 0.5
        padding(200,200,200,200)
        vbox:
            text "KANTO"
            text "----"
            text "Japan's largest plain"
            text "and densely populated"
            text "as it contains the"
            text "nation's capital, Tokyo."
            textbutton ">Start":
                action Jump("kantoStory")
            textbutton ">Back":
                action Hide("startKanto")

