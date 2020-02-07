init python:
    def replace_dialogue_to_identifier(h):
        if h.kind != "adv": return

        identifier = renpy.game.context().translate_identifier
        h.what = "{#" + identifier + "}"

        if len(_history_list) and _history_list[-1].what == h.what: _history_list.pop(-1)

    config.history_callbacks.append(replace_dialogue_to_identifier)

translate None strings:
    old "サヨリ"
    new "Sayori"

    old "モニカ"
    new "Monika"

    old "ナツキ"
    new "Natsuki"

    old "ユリ"
    new "Yuri"

    old "ナツキ＆ユリ"
    new "Nat & Yuri"

    old "？？？"
    new "???"

    old "女子Ａ"
    new "Girl 1"

    old "女子Ｂ"
    new "Girl 2"

    old "女子Ｃ"
    new "Girl 3"
