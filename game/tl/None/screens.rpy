define readme_file = ""

init -1 python:
    def Uninstall():
        renpy.change_language(None)
        persistent.jppatch_uninstall = True
        renpy.save_persistent()
        renpy.utter_restart()
        return

    if persistent.jppatch_uninstall == True:
        import os
        try: os.unlink(config.basedir + "/game/jp.rpa")
        except: pass
        try: os.unlink(config.basedir + "/game/none.rpa")
        except: pass
        persistent.jppatch_uninstall = False
        renpy.save_persistent()
        renpy.quit()

translate None python:
    readme_file = "README.html"

label chapter_select:
    python:
        s_name = "Sayori"
        m_name = 'Monika'
        n_name = 'Natsuki'
        y_name = 'Yuri'
        try: renpy.file("../characters/sayori.chr")
        except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())
        try: renpy.file("../characters/monika.chr")
        except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
        try: renpy.file("../characters/natsuki.chr")
        except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
        try: renpy.file("../characters/yuri.chr")
        except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())

    menu:
        "Act 1 Day 1 ~ 6":
            $ persistent.playthrough = 0
            $ renpy.save_persistent()
            menu:
                "Act 1 Day 1":
                    jump start
                "Act 1 Day 2":
                    jump ch1_main
                "Act 1 Day 3":
                    jump ch2_main
                "Act 1 Day 4":
                    jump ch3_main
                "Act 1 Day 5":
                    jump ch4_main
                "Act 1 Day 6":
                    jump ch5_main
        "Act 2 Day 1 ~ 4":
            $ persistent.playthrough = 2
            $ renpy.save_persistent()
            $ delete_character("sayori")
            menu:
                "Act 2 Day 1":
                    jump ch10_main
                "Act 2 Day 2":
                    jump ch21_main
                "Act 2 Day 3":
                    jump ch22_main
                "Act 2 Day 4":
                    jump ch23_main
        "Act 3":
            $ persistent.playthrough = 3
            $ persistent.autoload = "ch30_main"
            $ renpy.save_persistent()
            $ delete_character("sayori")
            $ delete_character("natsuki")
            $ delete_character("yuri")
            jump ch30_main
        "Act 4":
            $ persistent.playthrough = 4
            $ persistent.autoload = None
            $ renpy.save_persistent()
            $ delete_character("monika")
            jump ch40_main
        "Ending":
            $ persistent.autoload = "credits"
            $ renpy.save_persistent()
            jump credits

translate None screen:
    screen navigation():
        vbox:
            style_prefix "navigation"
            xpos gui.navigation_xpos
            yalign 0.8
            spacing gui.navigation_spacing
            if not persistent.autoload or not main_menu:
                if main_menu:
                    if persistent.playthrough == 1:
                        textbutton _("ŔŗñĮ¼»ŧþŀÂŻŕěōì«") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))
                    else:
                        textbutton _("New Game") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))
                else:
                    textbutton _("History") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]
                    textbutton _("Save Game") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]
                textbutton _("Load Game") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]
                if _in_replay:
                    textbutton _("End Replay") action EndReplay(confirm=True)
                elif not main_menu:
                    if persistent.playthrough != 3:
                        textbutton _("Main Menu") action MainMenu()
                    else:
                        textbutton _("Main Menu") action NullAction()
                textbutton _("Settings") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]
                if renpy.variant("pc"):
                    textbutton _("Help") action [Help(readme_file), Show(screen="dialog", message="The help file has been opened in your browser.", ok_action=Hide("dialog"))]
                    textbutton _("Quit") action Quit(confirm=not main_menu)
            else:
                timer 1.75 action Start("autoload_yurikill")

translate None screen:
    screen preferences() tag menu:
        if renpy.mobile:
            $ cols = 2
        else:
            $ cols = 4

        use game_menu(_("Settings"), scroll="viewport"):
            vbox:
                xoffset 50
                hbox:
                    box_wrap True
                    if renpy.variant("pc"):
                        vbox:
                            style_prefix "radio"
                            label _("Display")
                            textbutton _("Window") action Preference("display", "window")
                            textbutton _("Fullscreen") action Preference("display", "fullscreen")
                    if config.developer:
                        vbox:
                            style_prefix "radio"
                            label _("Rollback Side")
                            textbutton _("Disable") action Preference("rollback side", "disable")
                            textbutton _("Left") action Preference("rollback side", "left")
                            textbutton _("Right") action Preference("rollback side", "right")
                    vbox:
                        style_prefix "check"
                        label _("Skip")
                        textbutton _("Unseen Text") action Preference("skip", "toggle")
                        textbutton _("After Choices") action Preference("after choices", "toggle")

                null height (4 * gui.pref_spacing)

                hbox:
                    style_prefix "slider"
                    box_wrap True
                    vbox:
                        label _("Text Speed")
                        bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)
                        label _("Auto-Forward Time")
                        bar value Preference("auto-forward time")

                    vbox:
                        if config.has_music:
                            label _("Music Volume")
                            hbox:
                                bar value Preference("music volume")

                        if config.has_sound:
                            label _("Sound Volume")
                            hbox:
                                bar value Preference("sound volume")
                                if config.sample_sound:
                                    textbutton _("Test") action Play("sound", config.sample_sound)

                        if config.has_voice:
                            label _("Voice Volume")
                            hbox:
                                bar value Preference("voice volume")
                                if config.sample_voice:
                                    textbutton _("Test") action Play("voice", config.sample_voice)

                        if config.has_music or config.has_sound or config.has_voice:
                            null height gui.pref_spacing
                            textbutton _("Mute All"):
                                action Preference("all mute", "toggle")
                                style "mute_all_button"

                hbox:
                    box_wrap True
                    vbox:
                        style_prefix "check"
                        label _("Language")
                        textbutton _("English") action Language(None)
                        $ languages = renpy.known_languages()
                        for language in languages:
                            textbutton _(language) action Language(language)

                    vbox:
                        style_prefix "check"
                        label _("Auto")
                        textbutton _("Poem") action ToggleField(persistent, 'jpmode_auto_poem', true_value=True, false_value=False)

                    vbox:
                        label ("")
                        textbutton _("Uninstall") action [Show(screen="confirm", message="Would you like to uninstall jp patch and quit?", yes_action=Function(Uninstall), no_action=Hide("confirm"))]
                        textbutton _("Chapter Select") action Start('chapter_select')

        text "v[config.version]":
            xalign 1.0 yalign 1.0
            xoffset -10 yoffset -10
            style "main_menu_version"

translate None screen:
    screen name_input(message, ok_action):
        modal True
        zorder 200
        style_prefix "confirm"
        add "gui/overlay/confirm.png"
        key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]
        frame:
            has vbox:
                xalign .5
                yalign .5
                spacing 30
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            input default "" value VariableInputValue("player") length 12 pixel_width 168
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("OK") action ok_action
