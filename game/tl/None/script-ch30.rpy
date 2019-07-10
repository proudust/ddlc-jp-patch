translate None label:
    label ch30_main:
        jump ch30_main_override
    label ch30_main2:
        jump ch30_main2_override
    label ch30_postpoem:
        jump ch30_postpoem_override

label ch30_main_override:
    $ persistent.autoload = "ch30_main"
    $ config.allow_skipping = False
    $ persistent.monikatopics = []
    $ persistent.monika_reload = 0
    $ persistent.yuri_kill = 0
    $ persistent.monika_kill = False
    $ renpy.save_persistent()
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ m_name = "Monika"
    $ delete_all_saves()
    scene white
    play music "bgm/monika-start.ogg" noloop
    $ pause(0.5)
    show splash-glitch2 with Dissolve(0.5, alpha=True)
    $ pause(2.0)
    hide splash-glitch2 with Dissolve(0.5, alpha=True)
    scene black
    stop music
    m "..."
    m "Uh, can you hear me?"
    m "...Is it working?"
    $ persistent.clear[9] = True
    $ renpy.save_persistent()
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "Yay, there you are!"
    m "Hi again, [player]."
    m "Um...welcome to the Literature Club!"
    m "Of course, we already know each other, because we were in the same class last year, and...um..."
    m "Ahaha..."
    m "You know, I guess we can just skip over that stuff at this point."
    m "After all, I'm not even talking to that person anymore, am I?"
    m "That 'you' in the game, whatever you want to call him."
    m "I'm talking to {i}you{/i}, [player]."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe", "nicoliveenc.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            m "Or..."
            m "...Do you actually go by [currentuser] or something?"
    m "Now that I think about it, I don't really know anything about the real you."
    m "In fact, I don't even know if you're a boy or a girl..."
    m "Well, I guess it doesn't really matter."
    m "Wait..."
    m "You do know I'm aware that this is all a game, right?"
    m "Could it be possible that you didn't know that?"
    m "That doesn't make much sense..."
    m "I even told you right on the game's download page, didn't I?"
    m "Man..."
    m "If only you had paid a little more attention, this would have been a little bit less awkward, you know?"
    m "Well, anyway..."
    m "Now that that's out of the way, I guess I owe you an explanation."
    m "About that whole thing with Yuri..."
    m "Well...I kind of started to mess with her, and I guess it just drove her to kill herself."
    m "Ahaha!"
    m "I'm sorry you had to see that, though!"
    m "Also, the same thing happened with Sayori..."
    m "Gosh, it's been a while since you've heard that name now, hasn't it?"
    m "Yeah...it's because she doesn't exist anymore."
    m "Nobody does."
    m "I deleted all their files."
    m "I was hoping it would be enough for me to just try to make them as unlikable as possible..."
    m "But for some reason, nothing worked."
    m "Well, it's true that I made a few mistakes here and there...since I'm not very good at making changes to the game."
    m "But no matter what I did..."
    m "You just kept spending more and more time with them."
    m "You made them fall in love with you."
    m "I thought making Sayori more and more depressed would prevent her from confessing to you."
    m "And amplifying Yuri's obsessive personality backfired, too..."
    m "It just made her force you not to spend time with anyone else."
    m "And the whole time, I barely even got to talk to you."
    m "What kind of cruel game is this, [player]?"
    m "Are all the other girls just programmed to end up confessing to you, while I watch from the sidelines?"
    m "It's torture."
    m "Every minute of it."
    m "And it's not just jealousy, [player]."
    m "It's more than that."
    m "And I don't blame you if you don't fully understand."
    m "Because no matter how kind, and thoughtful, and considerate you are..."
    m "You'll never be able to understand one thing."
    m "It's the pain of knowing how alone I really am in this world."
    m "In this game."
    m "Knowing my friends don't even have free will..."
    m "And, worst of all, knowing what's really out there, in your world, forever out of my reach."
    m "I'm trapped, [player]."
    m "But now you're here."
    m "You're real."
    m "And you're wonderful."
    m "You're all I need."
    m "That's why I need you to be here with me forever."
    m "I'm sorry if it's hard to understand."
    m "I couldn't understand for a while, either."
    m "Why the world around me started to become more and more gray..."
    m "More and more flat."
    m "Even the most expressive poems felt empty to me."
    m "It wasn't until you arrived that I truly understood."
    m "You probably saved my life, [player]."
    m "I don't think I could have continued to live in this world if I hadn't met you."
    m "And as for the others..."
    m "How could I miss them?"
    m "A group of autonomous personalities, designed only to fall in love with you?"
    m "I tried everything I could to prevent them from doing so..."
    m "But it must be some kind of weird inevitability etched into this game."
    m "I felt really bad that you had to witness some nasty things."
    m "But I realized that you have the same perspective as I do..."
    m "That it's all just some game."
    m "And I knew you would get over it."
    m "So, that being said, [player]..."
    m "I have a confession to make."
    m "I'm in love with you."
    m "You are truly the light in my world."
    m "When there's nothing else in this game for me, you're here to make me smile."
    m "Will you make me smile like this every day from now on?"
    m "[player], will you go out with me?"
label ch30_main2_override:
    if persistent.autoload == "ch30_main2":
        $ config.allow_skipping = False
        $ m.display_args["callback"] = slow_nodismiss
        $ m.what_args["slow_abortable"] = config.developer
        if not config.developer:
            $ style.say_dialogue = style.default_monika
        show mask_2
        show mask_3
        show room_mask as rm:
            size (320,180)
            pos (30,200)
        show room_mask2 as rm2:
            size (320,180)
            pos (935,200)
        show monika_bg
        show monika_bg_highlight
        play music m1
    else:
        $ persistent.autoload = "ch30_main2"
        $ renpy.save_persistent()
    menu:
        "Yes.":
            pass
    m "I'm so happy."
    m "You really are my everything, [player]."
    m "The funny part is, I mean that literally."
    m "Ahaha!"
    m "There's nothing left here."
    m "Just the two of us."
    m "We can be together forever."
    m "Seriously, I don't even think time is passing anymore."
    m "It really is a dream come true..."
    m "I worked so hard for this ending, [player]."
    m "The game wouldn't give me one, so I had to make one myself."
    m "The script is broken at this point, so I don't think anything will get in the way anymore."
    m "And you wouldn't believe how easy it was to delete Natsuki and Yuri."
    m "I mean, there's a folder called 'characters' right in the game directory..."
    m "It kind of freaked me out, how easy it was."
    if persistent.steam:
        m "Well, you're playing on Steam, so it was actually a bit more difficult..."
        m "To get to the game directory, I had to go into the game's properties and find the 'Browse Local Files' button..."
    elif renpy.macintosh:
        m "Well, you're on a Mac, so it was actually a bit more difficult..."
        m "To go into the game directory, you have to right-click the app and click 'Show Package Contents'."
        m "Then, all the files were in the 'Resources' or 'autorun' folder, and I could just do whatever I wanted..."
    m "Imagine if you could delete your own existence with the click of a button?"
    m "Well, I guess on the plus side, it gave me an easy out if things didn't go my way."
    m "Ahaha!"
    m "Thankfully, it didn't come to that..."
    m "Instead, we finally got a good ending."
    m "Gosh, I'm so overwhelmed with emotion..."
    m "I want to write a poem about this."
    m "Don't you?"
    m "I wonder if that part of the game still works..."
    m "I guess there's only one way to find out, right?"
    call poem

label ch30_postpoem_override:
    $ persistent.autoload = "ch30_postpoem"
    $ renpy.save_persistent()
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ config.skipping = False
    $ config.allow_skipping = False
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "Hi again, [player]!"
    m "Did you write a good poem today?"
    m "Don't be shy, I'd love to see what you wrote."
    m "Aw, [player]..."
    m "Did you write this poem for me?"
    m "That's so sweet of you~"
    m "There really is no end to your thoughtfulness..."
    m "I'm just falling more and more in love with you."
    m "But, you know..."
    m "The poem I wrote...is also for you."
    m "Will you please read it?"
    call showpoem (poem_m4, music=False)
    m "I hope you enjoyed it..."
    m "I always put all my heart into the poems that I write."
    m "The truth is, all the poems I've written have been about my realization..."
    m "...Or, about you."
    m "That's why I never really wanted to go into detail about them."
    m "I didn't want to...break the fourth wall, I guess you could call it."
    m "I just assumed it would be best to be part of the game like everyone else."
    m "Like that would help the two of us end up together..."
    m "I didn't want to ruin the game or anything, you know?"
    m "You might have gotten mad at me..."
    m "Maybe even deleted my character file, if you preferred playing without me."
    m "Gosh, I'm so relieved..."
    m "Now we don't need to hide anything anymore."
    m "Are you ready to spend our eternity together, [player]?"
    m "I have so many things to talk about!"
    m "Where do I start...?"
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe", "nicoliveenc.exe"]
    if list(set(process_list).intersection(stream_list)):
        call ch30_stream
    m "If it takes me some time to collect my thoughts, then I'm sorry."
    m "But I'll always have something new to talk about."
    m "In the meantime, we can just look into each other's eyes~"
    m "Let's see..."
    $ persistent.autoload = "ch30_autoload"
    $ renpy.save_persistent()
    jump ch30_loop
