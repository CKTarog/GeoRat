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

    #kr
    imagebutton:
        xpos 795
        ypos 235
        idle "map_korea.png"
        hover "map_korea_hover.png"
        action ShowMenu("korea")

#ph
screen philippines():
    tag menu
    frame:
        xalign 100
        yalign 100
        textbutton "Return" action Return()

    add "map_ph.png"
    text "Choose an Island":
        xalign 0.9
        yalign 0.5
        size 50
    
    #luzon
    imagebutton:
        xpos 276
        ypos 28
        idle "map_luzon_idle.png"
        hover "map_luzon_hover.png"
        action ShowMenu("luzon")
    
#jp
screen japan():
    tag menu
    add "map_jp.png"
    frame:
        xalign 100
        yalign 100
        textbutton "Return" action Return()

    text "Choose a prefecture":
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

    #kansai
    imagebutton:
        xpos 495
        ypos 565
        idle "japan_kansai_idle.png"
        hover "japan_kansai_hover.png"
        action ShowMenu("kansai")

#kr
screen korea():
    tag menu
    add "map_kr.png"
    frame:
        xalign 100
        yalign 100
        textbutton "Return" action Return()

    text "Choose a city":
        xalign 0.9
        yalign 0.5
        size 50

    #seoul
    imagebutton:
        xpos 446
        ypos 155
        idle "korea_seoul_idle.png"
        hover "korea_seoul_hover.png"
        action Show("startSeoul")

    #deagu
    imagebutton:
        xpos 797
        ypos 392
        idle "korea_deagu_idle.png"
        hover "korea_deagu_hover.png"
        action Show("startDeagu")

    #busan
    imagebutton:
        xpos 934
        ypos 482
        idle "korea_busan_idle.png"
        hover "korea_busan_hover.png"
        action Show("startBusan")

screen luzon():
    tag menu
    
    add "map_luzon"
    frame:
        xalign 100
        yalign 100
        textbutton "Return" action ShowMenu("philippines")

    text "Choose a city":
        xalign 0.9
        yalign 0.5
        size 50

    #manila-taguig
    imagebutton:
        xpos 442
        ypos 586
        idle "luzon_manila_idle.png"
        hover "luzon_manila_hover.png"
        action Show("startManila")

    #baguio
    imagebutton:
        xpos 392
        ypos 300
        idle "luzon_baguio_idle.png"
        hover "luzon_baguio_hover.png"
        action Show("startBaguio")

screen kansai():
    tag menu
    add "map_kansai.png"
    frame:
        xalign 100
        yalign 100
        textbutton "Return" action ShowMenu("japan")

    text "Choose a city":
        xalign 0.9
        yalign 0.5
        size 50

    #kyoto
    imagebutton:
        xpos 223
        ypos 275
        idle "kansai_kyoto_idle"
        hover "kansai_kyoto_hover"
        action Show("startKyoto")

    #osaka
    imagebutton:
        xpos 555
        ypos 437
        idle "kansai_osaka_idle"
        hover "kansai_osaka_hover"
        action Show("startOsaka")

        

screen startManila():
    modal True
    image "luzon_manila_hover.png":
        xpos 442
        ypos 586
    frame:
        xalign 0.98
        yalign 0.5
        padding(200,200,200,200)
        vbox:
            text "MANILA"
            textbutton ">Start":
                action Jump("manilaStory")
            textbutton ">Back":
                action Hide("startManila")

screen startBaguio():
    modal True
    image "luzon_baguio_hover.png":
        xpos 392
        ypos 300
    frame:
        xalign 0.98
        yalign 0.5
        padding(200,200,200,200)
        vbox:
            text "BAGUIO"
            textbutton ">Start":
                action Jump("baguioStory")
            textbutton ">Back":
                action Hide("startBaguio")
        
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
            textbutton ">Start":
                action Jump("kantoStory")
            textbutton ">Back":
                action Hide("startKanto")
            
screen startKyoto():
    modal True
    image "kansai_kyoto_hover.png":
        xpos 223
        ypos 275
    frame:
        xalign 0.98
        yalign 0.5
        padding(200,200,200,200)
        vbox:
            text "KYOTO"
            textbutton ">Start":
                action Jump("kyotoStory")
            textbutton ">Back":
                action Hide("startKyoto")
screen startOsaka():
    modal True
    image "kansai_osaka_hover.png":
        xpos 555
        ypos 437
    frame: 
        xalign 0.98
        yalign 0.5
        padding(200,200,200,200)
        vbox:
            text "OSAKA"
            textbutton ">Start":
                action Jump("osakaStory")
            textbutton ">Back":
                action Hide("startOsaka")

screen startSeoul():
    modal True
    image "korea_seoul_hover.png":
        xpos 446
        ypos 155
    frame: 
        xalign 0.98
        yalign 0.5
        padding(200,200,200,200)
        vbox:
            text "SEOUL"
            textbutton ">Start":
                action Jump("seoulStory")
            textbutton ">Back":
                action Hide("startSeoul")

screen startDeagu():
    modal True
    image "korea_deagu_hover.png":
        xpos 797
        ypos 392
    frame: 
        xalign 0.98
        yalign 0.5
        padding(200,200,200,200)
        vbox:
            text "DEAGU"
            textbutton ">Start":
                action Jump("deaguStory")
            textbutton ">Back":
                action Hide("startDeagu")

screen startBusan():
    modal True
    image "korea_busan_hover.png":
        xpos 934
        ypos 482
    frame: 
        xalign 0.98
        yalign 0.5
        padding(200,200,200,200)
        vbox:
            text "BUSAN"
            textbutton ">Start":
                action Jump("busanStory")
            textbutton ">Back":
                action Hide("startBusan")
label ph:
    scene bg_menu

label kanto:
    scene bg_menu

label kyoto:
    scene bg_menu

label osaka:
    scene bg_menu
