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
