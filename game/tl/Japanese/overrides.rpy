define config.default_language = "Japanese"

# フォント設定
translate Japanese python:
    gui.default_font = "gui/font/VL-Gothic-Regular.ttf"
    gui.name_font = "gui/font/VL-Gothic-Regular.ttf"
    gui.interface_font = "gui/font/VL-Gothic-Regular.ttf"
    gui.choice_button_borders = Borders(10, 5, 10, 5)

translate Japanese style _default:
    font "gui/font/MTLc3m.ttf"

translate Japanese style normal:
    outlines [(2, "#444", 0, 0), (1, "#444", 2, 2)]

translate Japanese style button_text:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style check_button_text:
    font "gui/font/Mikachan.ttf"

translate Japanese style choice_button_text:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style edited:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style game_menu_label_text:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style navigation_button_text:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style poemgame_text:
    font "gui/font/Mikachan.ttf"

translate Japanese style pref_label_text:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style radio_button_text:
    font "gui/font/Mikachan.ttf"

# 詩
translate Japanese style yuri_text:
    font "gui/font/851tegaki_zatsu_normal.ttf"
    size 28

translate Japanese style yuri_text_2:
    font "gui/font/gatasosyo.ttf"
    size 36

translate Japanese style yuri_text_3:
    font "gui/font/gatasosyo.ttf"
    size 27
    kerning -12
    language "western"

translate Japanese style natsuki_text:
    font "gui/font/SNsanafonP.ttf"
    size 30

translate Japanese style sayori_text:
    font "gui/font/HolidayMDJP.otf"
    size 30

translate Japanese style monika_text:
    font "gui/font/Ruriiro_font.ttf"
    size 30

# エンドクレジット
translate Japanese style credits_header:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style credits_text:
    font "gui/font/Mikachan.ttf"

style monika_credits_text_Japanese is monika_credits_text:
    font "gui/font/Ruriiro_font.ttf"

# 接頭詞・接尾詞の設定
translate Japanese python:
    mc = DynamicCharacter('player', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed")
    s = DynamicCharacter('s_name', image='sayori', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed")
    m = DynamicCharacter('m_name', image='monika', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed")
    n = DynamicCharacter('n_name', image='natsuki', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed")
    y = DynamicCharacter('y_name', image='yuri', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed")
    ny = Character('Nat & Yuri', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed")

# エンディング
image mcredits_1a_Japanese:
    ypos credits_ypos_tl
    xoffset -340
    "black"
    10.33
    Text("Every day,{#translate}", style="monika_credits_text_Japanese") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_1b_Japanese:
    ypos credits_ypos_tl
    xoffset -55
    "black"
    11.75
    Text("I imagine a future where{#translate}", style="monika_credits_text_Japanese") with ImageDissolve("images/menu/wipeleft.png", 5.0, ramplen=4, alpha=False)
image mcredits_1c_Japanese:
    ypos credits_ypos_tl
    xoffset 290
    "black"
    13.76
    Text("I can be with you{#translate}", style="monika_credits_text_Japanese") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_2a_Japanese:
    ypos credits_ypos_tl + 50
    xoffset -270
    "black"
    19.45
    Text("In my hand{#translate}", style="monika_credits_text_Japanese") with ImageDissolve("images/menu/wipeleft.png", 8.0, ramplen=4, alpha=False)
image mcredits_2b_Japanese:
    ypos credits_ypos_tl + 50
    xoffset -20
    "black"
    20.9
    Text(" is a pen that will write a poem{#translate}", style="monika_credits_text_Japanese") with ImageDissolve("images/menu/wipeleft.png", 12.0, ramplen=4, alpha=False)
image mcredits_2c_Japanese:
    ypos credits_ypos_tl + 50
    xoffset 255
    "black"
    23.27
    Text("of me and you{#translate}", style="monika_credits_text_Japanese") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcredits_3_Japanese:
    ypos credits_ypos_tl + 100
    "black"
    28.35
    Text("The ink flows down into a dark puddle{#translate}", style="monika_credits_text_Japanese") with ImageDissolve("images/menu/wipeleft.png", 6.5, ramplen=4, alpha=False)
image mcredits_4_Japanese:
    ypos credits_ypos_tl + 150
    xoffset -5
    "black"
    32.9
    Text(" Just move your hand -- write the way into his heart!{#translate}", style="monika_credits_text_Japanese") with ImageDissolve("images/menu/wipeleft.png", 5.0, ramplen=4, alpha=False)
image mcredits_5_Japanese:
    ypos credits_ypos_tl + 200
    "black"
    37.5
    Text("But in this world of infinite choices{#translate}", style="monika_credits_text_Japanese") with ImageDissolve("images/menu/wipeleft.png", 6.5, ramplen=4, alpha=False)
image mcredits_6a_Japanese:
    ypos credits_ypos_tl + 250
    xoffset -235
    "black"
    42.0
    Text(" What will it take{#translate}", style="monika_credits_text_Japanese") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcredits_6b_Japanese:
    ypos credits_ypos_tl + 250
    xoffset 115
    "black"
    43.47
    Text(" just to find that special day?{#translate}", style="monika_credits_text_Japanese") with ImageDissolve("images/menu/wipeleft.png", 6.0, ramplen=4, alpha=False)
