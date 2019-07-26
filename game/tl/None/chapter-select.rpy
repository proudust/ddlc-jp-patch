label chapter_select:
    menu:
        "Act 1":
            menu:
                "Act 1 Day 1":
                    call chapter_select_after(0, 0)
                "Act 1 Day 2":
                    call chapter_select_after(0, 1)
                "Act 1 Day 3":
                    call chapter_select_after(0, 2)
                "Act 1 Day 4":
                    call chapter_select_after(0, 3)
                "Act 1 Day 5":
                    call chapter_select_after(0, 4)
                "Act 1 Day 6":
                    call chapter_select_after(0, 5)
        "Act 2":
            menu:
                "Act 2 Day 1":
                    call chapter_select_after(1, 0)
                "Act 2 Day 2":
                    call chapter_select_after(2, 1)
                "Act 2 Day 3":
                    call chapter_select_after(2, 2)
                "Act 2 Day 4":
                    call chapter_select_after(2, 3)
        "Act 3":
            call chapter_select_after(3, 0)
        "Act 4":
            call chapter_select_after(4, 0)
        "Ending":
            call chapter_select_after(5, 0)
    return

label chapter_select_after(playthrough, ch):
    python:
        persistent.playthrough = playthrough
        persistent.autoload = None
        renpy.save_persistent()
        chapter = ch - 1

        s_name = "Sayori"
        m_name = 'Monika'
        n_name = 'Natsuki'
        y_name = 'Yuri'

        quick_menu = True
        style.say_dialogue = style.normal
        in_sayori_kill = None
        allow_skipping = True
        config.allow_skipping = True

        def create_character(name):
            try: renpy.file(config.basedir + "/characters/" + name)
            except: open(config.basedir + "/characters/" + name, "wb").write(renpy.file(name).read())
        def create_file(name):
            try: renpy.file(config.basedir + "/" + name)
            except: open(config.basedir + "/" + name, "wb").write(renpy.file(name).read())
        create_character('sayori.chr')
        create_character('monika.chr')
        create_character('natsuki.chr')
        create_character('yuri.chr')
    call expression "chapter_select_pt" + str(playthrough) +"_day" + str(ch + 1)
    return

label chapter_select_pt0_day1:
    jump start
label chapter_select_pt0_day2:
    call poem
    call ch1_main
    call poemresponse_start
    call ch1_end
label chapter_select_pt0_day3:
    call poem
    $ chapter = 2
    call ch2_main
    call poemresponse_start
    call ch2_end
label chapter_select_pt0_day4:
    call poem
    $ chapter = 3
    call ch3_main
    call poemresponse_start
    call ch3_end
label chapter_select_pt0_day5:
    $ chapter = 4
    call ch4_main
label chapter_select_pt0_day6:
    $ chapter = 5
    $ create_file('hxppy thxughts.png')
    call ch5_main
    call endgame
    return

label chapter_select_pt1_day1:
    $ delete_character("sayori")
    jump start
label chapter_select_pt2_day2:
    jump playthrough2
label chapter_select_pt2_day3:
    call poem (False)
    $ create_file('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt')
    $ chapter = 2
    call ch22_main
    call poemresponse_start
    call ch22_end
label chapter_select_pt2_day4:
    call poem (False)
    $ chapter = 3
    call ch23_main
    if y_appeal >= 3:
        call poemresponse_start2
    else:
        call poemresponse_start
    call ch23_end
    return

label chapter_select_pt3_day1:
    $ persistent.autoload = "ch30_main"
    $ renpy.save_persistent()
    $ delete_character("sayori")
    $ delete_character('natsuki')
    $ delete_character('yuri')
    jump ch30_main

label chapter_select_pt4_day1:
    $ delete_character('monika')
    jump start

label chapter_select_pt5_day1:
    $ persistent.autoload = "credits"
    $ renpy.save_persistent()
    jump credits
