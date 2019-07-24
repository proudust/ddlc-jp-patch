translate None label:
    label showpoem(poem=None, music=True, track=None, revert_music=True, img=None, where=i11, paper=None):
        if poem == None:
            return
        if not persistent.jpmode_auto_poem:
            $ after_afm = _preferences.afm_enable
            $ _preferences.afm_enable = False
        play sound page_turn
        if music:
            $ currentpos = get_pos()
            if track:
                $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>" + track
            else:
                $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_" + poem.author + ".ogg"
            stop music fadeout 2.0
            $ renpy.music.play(audio.t5b, channel="music_poem", fadein=2.0, tight=True)
        window hide
        if paper:
            show screen poem(poem, paper=paper)
        else:
            show screen poem(poem)
        if not persistent.first_poem:
            $ persistent.first_poem = True
            $ renpy.save_persistent()
            show expression "gui/poem_dismiss.png" as poem_dismiss:
                xpos 1050 ypos 590
        with Dissolve(1)
        $ pause()
        if img:
            $ renpy.hide(poem.author)
            $ renpy.show(img, at_list=[where])
        hide screen poem
        hide poem_dismiss
        with Dissolve(.5)
        window auto
        if music and revert_music:
            $ currentpos = get_pos(channel="music_poem")
            $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
            stop music_poem fadeout 2.0
            $ renpy.music.play(audio.t5c, fadein=2.0)
        if not persistent.jpmode_auto_poem:
            $ _preferences.afm_enable = after_afm
        return

    screen poem(currentpoem, paper="paper"):
        style_prefix "poem"
        vbox:
            add paper
        viewport id "vp":
            child_size (710, None)
            mousewheel True
            draggable True
            has vbox
            null height 40
            if currentpoem.author == "yuri":
                if currentpoem.yuri_2:
                    text "[currentpoem.title!t]\n\n[currentpoem.text!t]" style "yuri_text"
                elif currentpoem.yuri_3:
                    text "[currentpoem.title!t]\n\n[currentpoem.text!t]" style "yuri_text_3"
                else:
                    text "[currentpoem.title!t]\n\n[currentpoem.text!t]" style "yuri_text"
            elif currentpoem.author == "sayori":
                text "[currentpoem.title!t]\n\n[currentpoem.text!t]" style "sayori_text"
            elif currentpoem.author == "natsuki":
                text "[currentpoem.title!t]\n\n[currentpoem.text!t]" style "natsuki_text"
            elif currentpoem.author == "monika":
                text "[currentpoem.title!t]\n\n[currentpoem.text!t]" style "monika_text"
            null height 100
        vbar value YScrollValue(viewport="vp") style "poem_vbar"
