init python:
    def recreate_character(name):
        try:
            renpy.file("../characters/" + name + ".chr")
            delete_character(name)
            open(config.basedir + "/characters/" + name + ".chr", "wb").write(renpy.file(name + ".chr").read())
        except: pass

    # プレイヤー名の翻訳防止
    mc.name = 'player + "{w}"'

translate None python:
    # 接頭詞・接尾詞の設定
    for char in [mc, s, m, n, y, ny]:
        char.what_prefix = '"'
        char.what_suffix = '"'

    # .chrの差し替え
    recreate_character('sayori')
    recreate_character('monika')
    recreate_character('natsuki')
    recreate_character('yuri')

    # 文字化け用文字列に§を戻す
    if '§' in nonunicode:
        nonunicode += '§'
