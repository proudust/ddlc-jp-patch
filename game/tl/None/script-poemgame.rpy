translate None label:
    label poem(transition=True):
        stop music fadeout 2.0
        if persistent.playthrough == 3:
            scene bg notebook-glitch
        else:
            scene bg notebook
        show screen quick_menu
        if persistent.playthrough == 3:
            show m_sticker at sticker_mid
        else:
            if persistent.playthrough == 0:
                show s_sticker at sticker_left
            show n_sticker at sticker_mid
            if persistent.playthrough == 2 and chapter == 2:
                show y_sticker_cut at sticker_right
            else:
                show y_sticker at sticker_right
            if persistent.playthrough == 2 and chapter == 2:
                show m_sticker at sticker_m_glitch
        if transition:
            with dissolve_scene_full
        if persistent.playthrough == 3:
            play music ghostmenu
        else:
            play music t4
        $ config.skipping = False
        $ config.allow_skipping = False
        $ allow_skipping = False
        if persistent.playthrough == 0 and chapter == 0:
            call screen dialog("It's time to write a poem!\n\nPick words you think your favorite club member\nwill like. Something good might happen with\nwhoever likes your poem the most!", ok_action=Return())
        python:
            poemgame_glitch = False
            played_baa = False
            progress = 1
            numWords = 20
            sPointTotal = 0
            nPointTotal = 0
            yPointTotal = 0
            wordlist = list(full_wordlist)

            sayoriTime = renpy.random.random() * 4 + 4
            natsukiTime = renpy.random.random() * 4 + 4
            yuriTime = renpy.random.random() * 4 + 4
            sayoriPos = renpy.random.randint(-1,1)
            natsukiPos = renpy.random.randint(-1,1)
            yuriPos = renpy.random.randint(-1,1)
            sayoriOffset = 0
            natsukiOffset = 0
            yuriOffset = 0
            sayoriZoom = 1
            natsukiZoom = 1
            yuriZoom = 1





            while True:
                ystart = 160
                if persistent.playthrough == 2 and chapter == 2:
                    pstring = ""
                    for i in range(progress):
                        pstring += "1"
                else:
                    pstring = str(progress)
                ui.text(pstring + "/" + str(numWords), style="poemgame_text", xpos=810, ypos=80, color='#000')
                for j in range(2):
                    if j == 0: x = 440
                    else: x = 680
                    ui.vbox()
                    for i in range(5):
                        if persistent.playthrough == 3:
                            s = list(__("Monika"))
                            for k in range(len(s)):
                                if random.randint(0, 4) == 0:
                                    s[k] = ' '
                                elif random.randint(0, 4) == 0:
                                    s[k] = random.choice(nonunicode)
                            word = PoemWord("".join(s), 0, 0, 0, False)
                        elif persistent.playthrough == 2 and not poemgame_glitch and chapter >= 1 and progress < numWords and random.randint(0, 400) == 0:
                            word = PoemWord(glitchtext(80), 0, 0, 0, True)
                        else:
                            word = random.choice(wordlist)
                            wordlist.remove(word)
                        ui.textbutton(word.word, clicked=ui.returns(word), text_style="poemgame_text", xpos=x, ypos=i * 56 + ystart)
                    ui.close()

                t = ui.interact()
                if not poemgame_glitch:
                    if t.glitch:
                        poemgame_glitch = True
                        renpy.music.play(audio.t4g)
                        renpy.scene()
                        renpy.show("white")
                        renpy.show("y_sticker glitch", at_list=[sticker_glitch])
                    elif persistent.playthrough != 3:
                        renpy.play(gui.activate_sound)
                        if persistent.playthrough == 0:
                            if t.sPoint >= 3:
                                renpy.show("s_sticker hop")
                            if t.nPoint >= 3:
                                renpy.show("n_sticker hop")
                            if t.yPoint >= 3:
                                renpy.show("y_sticker hop")
                        else:
                            if persistent.playthrough == 2 and chapter == 2 and random.randint(0,10) == 0: renpy.show("m_sticker hop")
                            elif t.nPoint > t.yPoint: renpy.show("n_sticker hop")
                            elif persistent.playthrough == 2 and not persistent.seen_sticker and random.randint(0,100) == 0:
                                renpy.show("y_sticker hopg")
                                persistent.seen_sticker = True
                            elif persistent.playthrough == 2 and chapter == 2: renpy.show("y_sticker_cut hop")
                            else: renpy.show("y_sticker hop")
                else:
                    r = random.randint(0, 10)
                    if r == 0 and not played_baa:
                        renpy.play("gui/sfx/baa.ogg")
                        played_baa = True
                    elif r <= 5: renpy.play(gui.activate_sound_glitch)
                sPointTotal += t.sPoint
                nPointTotal += t.nPoint
                yPointTotal += t.yPoint
                progress += 1
                if progress > numWords:
                    break

            if persistent.playthrough == 0:

                if chapter == 1:
                    exec(ch1_choice[0] + "PointTotal += 5")

                unsorted_pointlist = {"sayori": sPointTotal, "natsuki": nPointTotal, "yuri": yPointTotal}
                pointlist = sorted(unsorted_pointlist, key=unsorted_pointlist.get)


                poemwinner[chapter] = pointlist[2]
            else:
                if nPointTotal > yPointTotal: poemwinner[chapter] = "natsuki"
                else: poemwinner[chapter] = "yuri"


            exec(poemwinner[chapter][0] + "_appeal += 1")


            if sPointTotal < POEM_DISLIKE_THRESHOLD: s_poemappeal[chapter] = -1
            elif sPointTotal > POEM_LIKE_THRESHOLD: s_poemappeal[chapter] = 1
            if nPointTotal < POEM_DISLIKE_THRESHOLD: n_poemappeal[chapter] = -1
            elif nPointTotal > POEM_LIKE_THRESHOLD: n_poemappeal[chapter] = 1
            if yPointTotal < POEM_DISLIKE_THRESHOLD: y_poemappeal[chapter] = -1
            elif yPointTotal > POEM_LIKE_THRESHOLD: y_poemappeal[chapter] = 1


            exec(poemwinner[chapter][0] + "_poemappeal[chapter] = 1")

        if persistent.playthrough == 2 and persistent.seen_eyes == None and renpy.random.randint(0,5) == 0:
            $ seen_eyes_this_chapter = True
            $ quick_menu = False
            play sound "sfx/eyes.ogg"
            $ persistent.seen_eyes = True
            $ renpy.save_persistent()
            stop music
            scene black with None
            show bg eyes_move
            $ pause(1.2)
            hide bg eyes_move
            show bg eyes
            $ pause(0.5)
            hide bg eyes
            show bg eyes_move
            $ pause(1.25)
            hide bg eyes with None
            $ quick_menu = True
        $ config.allow_skipping = True
        $ allow_skipping = True
        stop music fadeout 2.0
        hide screen quick_menu
        show black as fadeout:
            alpha 0
            linear 1.0 alpha 1.0
        $ pause(1.0)
        return
