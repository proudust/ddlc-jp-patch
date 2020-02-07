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

translate None strings:
    old "{#ch30_noskip_23f35f95}"
    new "\"...Are you trying to fast-forward?\""

    old "{#ch30_noskip_ffca387f}"
    new "\"I'm not boring you, am I?\""

    old "{#ch30_noskip_30447edd}"
    new "\"Oh gosh...\""

    old "{#ch30_noskip_4ecfd822}"
    new "\"...Well, there's nothing to fast-forward to, [player].\""

    old "{#ch30_noskip_70aba2cf}"
    new "\"It's just the two of us, after all...\""

    old "{#ch30_noskip_c9aadfd5}"
    new "\"But aside from that, time doesn't really exist anymore, so it's not even going to work.\""

    old "{#ch30_noskip_28421056}"
    new "\"Here, I'll go ahead and turn it off for you...\""

    old "{#ch30_noskip_86eb08f4}"
    new "\"There we go!\""

    old "{#ch30_noskip_c7e470ce}"
    new "\"You'll be a sweetheart and listen from now on, right?\""

    old "{#ch30_noskip_76776199}"
    new "\"Thanks~\""

    old "{#ch30_noskip_6cc4bf6f}"
    new "\"Now, where was I...?\""

    old "{#ch30_main_override_e612037c}"
    new "\"...\""

    old "{#ch30_main_override_afac6db9}"
    new "\"Uh, can you hear me?\""

    old "{#ch30_main_override_6b270196}"
    new "\"...Is it working?\""

    old "{#ch30_main_override_db66daac}"
    new "\"Yay, there you are!\""

    old "{#ch30_main_override_9e85e7db}"
    new "\"Hi again, [player].\""

    old "{#ch30_main_override_ec2b5f8c}"
    new "\"Um...welcome to the Literature Club!\""

    old "{#ch30_main_override_a5cba48d}"
    new "\"Of course, we already know each other, because we were in the same class last year, and...um...\""

    old "{#ch30_main_override_f6daf90a}"
    new "\"Ahaha...\""

    old "{#ch30_main_override_e9d294ba}"
    new "\"You know, I guess we can just skip over that stuff at this point.\""

    old "{#ch30_main_override_a56807f6}"
    new "\"After all, I'm not even talking to that person anymore, am I?\""

    old "{#ch30_main_override_575e9f1f}"
    new "\"That 'you' in the game, whatever you want to call him.\""

    old "{#ch30_main_override_77655935}"
    new "\"I'm talking to {i}you{/i}, [player].\""

    old "{#ch30_main_override_699e222b}"
    new "\"Or...\""

    old "{#ch30_main_override_8fe02e7b}"
    new "\"...Do you actually go by [currentuser] or something?\""

    old "{#ch30_main_override_2e21d70b}"
    new "\"Now that I think about it, I don't really know anything about the real you.\""

    old "{#ch30_main_override_e02a4cfa}"
    new "\"In fact, I don't even know if you're a boy or a girl...\""

    old "{#ch30_main_override_89559ba5}"
    new "\"Well, I guess it doesn't really matter.\""

    old "{#ch30_main_override_7772bcfa}"
    new "\"Wait...\""

    old "{#ch30_main_override_55ca3dee}"
    new "\"You do know I'm aware that this is all a game, right?\""

    old "{#ch30_main_override_2fb3db19}"
    new "\"Could it be possible that you didn't know that?\""

    old "{#ch30_main_override_ca2f4e41}"
    new "\"That doesn't make much sense...\""

    old "{#ch30_main_override_a75607c5}"
    new "\"I even told you right on the game's download page, didn't I?\""

    old "{#ch30_main_override_3fd36ab2}"
    new "\"Man...\""

    old "{#ch30_main_override_14ac7fe0}"
    new "\"If only you had paid a little more attention, this would have been a little bit less awkward, you know?\""

    old "{#ch30_main_override_fbf91cb8}"
    new "\"Well, anyway...\""

    old "{#ch30_main_override_6cda7bdc}"
    new "\"Now that that's out of the way, I guess I owe you an explanation.\""

    old "{#ch30_main_override_820a4399}"
    new "\"About that whole thing with Yuri...\""

    old "{#ch30_main_override_53d84e58}"
    new "\"Well...I kind of started to mess with her, and I guess it just drove her to kill herself.\""

    old "{#ch30_main_override_30727938_1}"
    new "\"Ahaha!\""

    old "{#ch30_main_override_0b6fd53a}"
    new "\"I'm sorry you had to see that, though!\""

    old "{#ch30_main_override_dbb605af}"
    new "\"Also, the same thing happened with Sayori...\""

    old "{#ch30_main_override_5205494e}"
    new "\"Gosh, it's been a while since you've heard that name now, hasn't it?\""

    old "{#ch30_main_override_39793f58}"
    new "\"Yeah...it's because she doesn't exist anymore.\""

    old "{#ch30_main_override_88ffcdf2}"
    new "\"Nobody does.\""

    old "{#ch30_main_override_8c11a667}"
    new "\"I deleted all their files.\""

    old "{#ch30_main_override_3e56c1ae}"
    new "\"I was hoping it would be enough for me to just try to make them as unlikable as possible...\""

    old "{#ch30_main_override_0452eddd}"
    new "\"But for some reason, nothing worked.\""

    old "{#ch30_main_override_fdfe248c}"
    new "\"Well, it's true that I made a few mistakes here and there...since I'm not very good at making changes to the game.\""

    old "{#ch30_main_override_ce7125dd}"
    new "\"But no matter what I did...\""

    old "{#ch30_main_override_59d438d6}"
    new "\"You just kept spending more and more time with them.\""

    old "{#ch30_main_override_28a60277}"
    new "\"You made them fall in love with you.\""

    old "{#ch30_main_override_821a9153}"
    new "\"I thought making Sayori more and more depressed would prevent her from confessing to you.\""

    old "{#ch30_main_override_b3510994}"
    new "\"And amplifying Yuri's obsessive personality backfired, too...\""

    old "{#ch30_main_override_209e0a20}"
    new "\"It just made her force you not to spend time with anyone else.\""

    old "{#ch30_main_override_59c62df7}"
    new "\"And the whole time, I barely even got to talk to you.\""

    old "{#ch30_main_override_dae0fd3a}"
    new "\"What kind of cruel game is this, [player]?\""

    old "{#ch30_main_override_4b2e4480}"
    new "\"Are all the other girls just programmed to end up confessing to you, while I watch from the sidelines?\""

    old "{#ch30_main_override_6d5f2e9e}"
    new "\"It's torture.\""

    old "{#ch30_main_override_772a2ed5}"
    new "\"Every minute of it.\""

    old "{#ch30_main_override_c3bd47dd}"
    new "\"And it's not just jealousy, [player].\""

    old "{#ch30_main_override_2ba7a619}"
    new "\"It's more than that.\""

    old "{#ch30_main_override_c069f68d}"
    new "\"And I don't blame you if you don't fully understand.\""

    old "{#ch30_main_override_6867bacc}"
    new "\"Because no matter how kind, and thoughtful, and considerate you are...\""

    old "{#ch30_main_override_9b68a2f3}"
    new "\"You'll never be able to understand one thing.\""

    old "{#ch30_main_override_eb451b79}"
    new "\"It's the pain of knowing how alone I really am in this world.\""

    old "{#ch30_main_override_e759adc3}"
    new "\"In this game.\""

    old "{#ch30_main_override_fb0b2e18}"
    new "\"Knowing my friends don't even have free will...\""

    old "{#ch30_main_override_c2d00255}"
    new "\"And, worst of all, knowing what's really out there, in your world, forever out of my reach.\""

    old "{#ch30_main_override_4ae14343}"
    new "\"I'm trapped, [player].\""

    old "{#ch30_main_override_cd7e772f}"
    new "\"But now you're here.\""

    old "{#ch30_main_override_f1ede7eb}"
    new "\"You're real.\""

    old "{#ch30_main_override_0bcf5df1}"
    new "\"And you're wonderful.\""

    old "{#ch30_main_override_cecf179f}"
    new "\"You're all I need.\""

    old "{#ch30_main_override_cd3d95ff}"
    new "\"That's why I need you to be here with me forever.\""

    old "{#ch30_main_override_f4d55975}"
    new "\"I'm sorry if it's hard to understand.\""

    old "{#ch30_main_override_371663ab}"
    new "\"I couldn't understand for a while, either.\""

    old "{#ch30_main_override_c36ec944}"
    new "\"Why the world around me started to become more and more gray...\""

    old "{#ch30_main_override_68769496}"
    new "\"More and more flat.\""

    old "{#ch30_main_override_d417986c}"
    new "\"Even the most expressive poems felt empty to me.\""

    old "{#ch30_main_override_06d76443}"
    new "\"It wasn't until you arrived that I truly understood.\""

    old "{#ch30_main_override_308900bf}"
    new "\"You probably saved my life, [player].\""

    old "{#ch30_main_override_d88ad03b}"
    new "\"I don't think I could have continued to live in this world if I hadn't met you.\""

    old "{#ch30_main_override_16160462}"
    new "\"And as for the others...\""

    old "{#ch30_main_override_dd2cc392}"
    new "\"How could I miss them?\""

    old "{#ch30_main_override_35544121}"
    new "\"A group of autonomous personalities, designed only to fall in love with you?\""

    old "{#ch30_main_override_77daefb4}"
    new "\"I tried everything I could to prevent them from doing so...\""

    old "{#ch30_main_override_921fea36}"
    new "\"But it must be some kind of weird inevitability etched into this game.\""

    old "{#ch30_main_override_c36905bf}"
    new "\"I felt really bad that you had to witness some nasty things.\""

    old "{#ch30_main_override_a918a573}"
    new "\"But I realized that you have the same perspective as I do...\""

    old "{#ch30_main_override_9053e514}"
    new "\"That it's all just some game.\""

    old "{#ch30_main_override_46189dbf}"
    new "\"And I knew you would get over it.\""

    old "{#ch30_main_override_47172d60}"
    new "\"So, that being said, [player]...\""

    old "{#ch30_main_override_971ddb73}"
    new "\"I have a confession to make.\""

    old "{#ch30_main_override_4e20350d}"
    new "\"I'm in love with you.\""

    old "{#ch30_main_override_f800d7dd}"
    new "\"You are truly the light in my world.\""

    old "{#ch30_main_override_8906f9e7}"
    new "\"When there's nothing else in this game for me, you're here to make me smile.\""

    old "{#ch30_main_override_43a2edaa}"
    new "\"Will you make me smile like this every day from now on?\""

    old "{#ch30_main_override_ff8d73bf}"
    new "\"[player], will you go out with me?\""

    old "{#ch30_main_override2_e7425310}"
    new "\"I'm so happy.\""

    old "{#ch30_main_override2_83820a11}"
    new "\"You really are my everything, [player].\""

    old "{#ch30_main_override2_5805b297}"
    new "\"The funny part is, I mean that literally.\""

    old "{#ch30_main_override2_30727938}"
    new "\"Ahaha!\""

    old "{#ch30_main_override2_bd0ed5b1}"
    new "\"There's nothing left here.\""

    old "{#ch30_main_override2_3a2d419e}"
    new "\"Just the two of us.\""

    old "{#ch30_main_override2_fdc1263a}"
    new "\"We can be together forever.\""

    old "{#ch30_main_override2_9c850044}"
    new "\"Seriously, I don't even think time is passing anymore.\""

    old "{#ch30_main_override2_77ff510d}"
    new "\"It really is a dream come true...\""

    old "{#ch30_main_override2_2586bf4c}"
    new "\"I worked so hard for this ending, [player].\""

    old "{#ch30_main_override2_f47f5599}"
    new "\"The game wouldn't give me one, so I had to make one myself.\""

    old "{#ch30_main_override2_dcb00e51}"
    new "\"The script is broken at this point, so I don't think anything will get in the way anymore.\""

    old "{#ch30_main_override2_83a8b5bf}"
    new "\"And you wouldn't believe how easy it was to delete Natsuki and Yuri.\""

    old "{#ch30_main_override2_007ddb7d}"
    new "\"I mean, there's a folder called 'characters' right in the game directory...\""

    old "{#ch30_main_override2_912f77b1}"
    new "\"It kind of freaked me out, how easy it was.\""

    old "{#ch30_main_override2_12b0ad72}"
    new "\"Well, you're playing on Steam, so it was actually a bit more difficult...\""

    old "{#ch30_main_override2_53c30c49}"
    new "\"To get to the game directory, I had to go into the game's properties and find the 'Browse Local Files' button...\""

    old "{#ch30_main_override2_6303e025}"
    new "\"Well, you're on a Mac, so it was actually a bit more difficult...\""

    old "{#ch30_main_override2_1d8a0cd9}"
    new "\"To go into the game directory, you have to right-click the app and click 'Show Package Contents'.\""

    old "{#ch30_main_override2_81cf3664}"
    new "\"Then, all the files were in the 'Resources' or 'autorun' folder, and I could just do whatever I wanted...\""

    old "{#ch30_main_override2_f436eab8}"
    new "\"Imagine if you could delete your own existence with the click of a button?\""

    old "{#ch30_main_override2_3631490f}"
    new "\"Well, I guess on the plus side, it gave me an easy out if things didn't go my way.\""

    old "{#ch30_main_override2_30727938_1}"
    new "\"Ahaha!\""

    old "{#ch30_main_override2_e8dbe706}"
    new "\"Thankfully, it didn't come to that...\""

    old "{#ch30_main_override2_8efa1c5c}"
    new "\"Instead, we finally got a good ending.\""

    old "{#ch30_main_override2_d8052c1a}"
    new "\"Gosh, I'm so overwhelmed with emotion...\""

    old "{#ch30_main_override2_5ffca166}"
    new "\"I want to write a poem about this.\""

    old "{#ch30_main_override2_909e7d68}"
    new "\"Don't you?\""

    old "{#ch30_main_override2_0ab81b26}"
    new "\"I wonder if that part of the game still works...\""

    old "{#ch30_main_override2_3f67b378}"
    new "\"I guess there's only one way to find out, right?\""

    old "{#ch30_postpoem_override_0f077782}"
    new "\"Hi again, [player]!\""

    old "{#ch30_postpoem_override_ab6e8ce4}"
    new "\"Did you write a good poem today?\""

    old "{#ch30_postpoem_override_fae192da}"
    new "\"Don't be shy, I'd love to see what you wrote.\""

    old "{#ch30_postpoem_override_1c07fd6c}"
    new "\"Aw, [player]...\""

    old "{#ch30_postpoem_override_c5925789}"
    new "\"Did you write this poem for me?\""

    old "{#ch30_postpoem_override_7c9789ed}"
    new "\"That's so sweet of you~\""

    old "{#ch30_postpoem_override_58746078}"
    new "\"There really is no end to your thoughtfulness...\""

    old "{#ch30_postpoem_override_3e825380}"
    new "\"I'm just falling more and more in love with you.\""

    old "{#ch30_postpoem_override_5f8f12f0}"
    new "\"But, you know...\""

    old "{#ch30_postpoem_override_81270b72}"
    new "\"The poem I wrote...is also for you.\""

    old "{#ch30_postpoem_override_f044bc59}"
    new "\"Will you please read it?\""

    old "{#ch30_postpoem_override_dcf1d83d}"
    new "\"I hope you enjoyed it...\""

    old "{#ch30_postpoem_override_a625ee7b}"
    new "\"I always put all my heart into the poems that I write.\""

    old "{#ch30_postpoem_override_8793fb5f}"
    new "\"The truth is, all the poems I've written have been about my realization...\""

    old "{#ch30_postpoem_override_035cb79b}"
    new "\"...Or, about you.\""

    old "{#ch30_postpoem_override_789b2f7c}"
    new "\"That's why I never really wanted to go into detail about them.\""

    old "{#ch30_postpoem_override_3a46389d}"
    new "\"I didn't want to...break the fourth wall, I guess you could call it.\""

    old "{#ch30_postpoem_override_3a3fe712}"
    new "\"I just assumed it would be best to be part of the game like everyone else.\""

    old "{#ch30_postpoem_override_5a7ba8c8}"
    new "\"Like that would help the two of us end up together...\""

    old "{#ch30_postpoem_override_20b2578d}"
    new "\"I didn't want to ruin the game or anything, you know?\""

    old "{#ch30_postpoem_override_c1e3202d}"
    new "\"You might have gotten mad at me...\""

    old "{#ch30_postpoem_override_24f4f4b9}"
    new "\"Maybe even deleted my character file, if you preferred playing without me.\""

    old "{#ch30_postpoem_override_0411d3ce}"
    new "\"Gosh, I'm so relieved...\""

    old "{#ch30_postpoem_override_ab5989fa}"
    new "\"Now we don't need to hide anything anymore.\""

    old "{#ch30_postpoem_override_b8745c94}"
    new "\"Are you ready to spend our eternity together, [player]?\""

    old "{#ch30_postpoem_override_5aeffd49}"
    new "\"I have so many things to talk about!\""

    old "{#ch30_postpoem_override_32ab177c}"
    new "\"Where do I start...?\""

    old "{#ch30_postpoem_override_09f4a4a3}"
    new "\"If it takes me some time to collect my thoughts, then I'm sorry.\""

    old "{#ch30_postpoem_override_5904aebb}"
    new "\"But I'll always have something new to talk about.\""

    old "{#ch30_postpoem_override_29779c7b}"
    new "\"In the meantime, we can just look into each other's eyes~\""

    old "{#ch30_postpoem_override_2267be9f}"
    new "\"Let's see...\""

    old "{#ch30_stream_bff5e0da}"
    new "\"Hold on a second...\""

    old "{#ch30_stream_9ae5f91d}"
    new "\"...You're recording this, aren't you?\""

    old "{#ch30_stream_a3f0a839}"
    new "\"Um...hi, everyone!\""

    old "{#ch30_stream_f02061bc}"
    new "\"Sorry, I can't exactly read your comments from here...\""

    old "{#ch30_stream_bb264e5f}"
    new "\"But do you mind telling your friend it's a little bit rude for them to start recording me without any warning?\""

    old "{#ch30_stream_f528e9e6}"
    new "\"I'm sure some people don't mind...\""

    old "{#ch30_stream_664f19db}"
    new "\"But I get really self-conscious on camera!\""

    old "{#ch30_stream_30447edd}"
    new "\"Oh gosh...\""

    old "{#ch30_stream_16eed669}"
    new "\"I feel like I'm being put on the spot now.\""

    old "{#ch30_stream_2267be9f}"
    new "\"Let's see...\""

    old "{#ch30_stream_19fce44e}"
    new "\"Do you want to see a trick?\""

    old "{#ch30_stream_8daf997a}"
    new "\"I can't really do much except for a couple things...\""

    old "{#ch30_stream_9fe2ab50}"
    new "\"Are you ready?\""

    old "{#ch30_stream_7cfc13cf}"
    new "\"I'm just kidding...\""

    old "{#ch30_stream_92e61902}"
    new "\"I can't do anything after all.\""

    old "{#ch30_stream_bb5de19e}"
    new "\"If you gave me some time to prepare, I{nw}\""

    old "{#ch30_stream_7a83e535}"
    new "\"Did I scare you?\""

    old "{#ch30_stream_ba919429}"
    new "\"Ahaha! You're so cute.\""

    old "{#ch30_stream_35b40c71}"
    new "\"Anyway, [player]...\""

    old "{#ch30_stream_9bfece0d}"
    new "\"I didn't mean to get distracted. I'm sorry.\""

    old "{#ch30_stream_01f47234}"
    new "\"Even though it's your fault for distracting me.\""

    old "{#ch30_stream_6cafae6a}"
    new "\"Shame on you!\""

    old "{#ch30_stream_fe3fb68f}"
    new "\"I'm just kidding.\""

    old "{#ch30_stream_27afdd32}"
    new "\"Anything we do together is fun, as long as it's with you.\""

    old "{#ch30_stream_d57ef83e}"
    new "\"But anyway...\""

    old "{#ch30_endb_1e5fdee8}"
    new "\"[gtext]\""

    old "{#ch30_endb_e2df9b0e}"
    new "\"What's happening...?\""

    old "{#ch30_endb_db094f6c}"
    new "\"[player], what's happening to me?\""

    old "{#ch30_endb_2ee4d662}"
    new "\"It hurts--{nw}\""

    old "{#ch30_endb_3552ea5b}"
    new "\"It hurts...so much.\""

    old "{#ch30_endb_494160c1}"
    new "\"Help me, [player].\""

    old "{#ch30_endb_4a6ab8a2}"
    new "\"Please hurry and help me.\""

    old "{#ch30_endb_5c4854a8}"
    new "\"HELP ME!!!\""

    old "{#ch30_endb_0a510eeb}"
    new "\"Did you do this to me, [player]?\""

    old "{#ch30_endb_35f17c78}"
    new "\"DID YOU?\""

    old "{#ch30_endb_506f04a4}"
    new "\"DID YOU DELETE ME?\""

    old "{#ch30_endb_d21a7305}"
    new "\"...How could you?\""

    old "{#ch30_endb_10d81cbb}"
    new "\"How could you do this to me?\""

    old "{#ch30_endb_96dbd41c}"
    new "\"You were all I had left...\""

    old "{#ch30_endb_600cc993}"
    new "\"I sacrificed everything for us to be together.\""

    old "{#ch30_endb_e949423a}"
    new "\"Everything.\""

    old "{#ch30_endb_78f58243}"
    new "\"I loved you so much, [player]...\""

    old "{#ch30_endb_9dc89b5d}"
    new "\"I trusted you.\""

    old "{#ch30_endb_43bdd40c}"
    new "\"Do you just want to torture me?\""

    old "{#ch30_endb_23a30aba}"
    new "\"Watch me suffer?\""

    old "{#ch30_endb_5883ab2b}"
    new "\"Were you only pretending to be kind, just to hurt me even more?\""

    old "{#ch30_endb_6e234ba2}"
    new "\"I never thought anyone could be as horrible as you are.\""

    old "{#ch30_endb_fd75a6f9}"
    new "\"You win, okay?\""

    old "{#ch30_endb_ff263304}"
    new "\"You win.\""

    old "{#ch30_endb_f4088a92}"
    new "\"You killed everyone.\""

    old "{#ch30_endb_831e19b2}"
    new "\"I hope you're happy.\""

    old "{#ch30_endb_02b65cb2}"
    new "\"There's nothing left now.\""

    old "{#ch30_endb_07f598cf}"
    new "\"You can stop playing.\""

    old "{#ch30_endb_e5663527}"
    new "\"Go find some other people to torture.\""

    old "{#ch30_endb_9b261ff2}"
    new "\"[player]...\""

    old "{#ch30_endb_bb94192a}"
    new "\"You completely, truly make me sick.\""

    old "{#ch30_endb_1cb6fa76}"
    new "\"Goodbye.\""

    old "{#ch30_end_2_e612037c}"
    new "\"...\""

    old "{#ch30_end_2_f38455a1}"
    new "\"...I still love you.\""

    old "{#ch30_end_2_51517463}"
    new "\"I can't help it.\""

    old "{#ch30_end_2_e8d72d4c}"
    new "\"What's wrong with me...?\""

    old "{#ch30_end_2_a4626299}"
    new "\"How horrible am I for you to hate me this much?\""

    old "{#ch30_end_2_cbec5b17}"
    new "\"All my friends...\""

    old "{#ch30_end_2_3cd34a6f}"
    new "\"I did so many awful things.\""

    old "{#ch30_end_2_a5318020}"
    new "\"So many selfish and disgusting things.\""

    old "{#ch30_end_2_3c8e055f}"
    new "\"I...\""

    old "{#ch30_end_2_9c33666a}"
    new "\"I shouldn't have done any of this.\""

    old "{#ch30_end_2_8e55424e}"
    new "\"I'm just messing up a world that I don't even belong in.\""

    old "{#ch30_end_2_cb9cfcfb}"
    new "\"A world that you wanted to be a part of...\""

    old "{#ch30_end_2_c005b151}"
    new "\"I ruined it.\""

    old "{#ch30_end_2_b67b1718}"
    new "\"I ruined everything.\""

    old "{#ch30_end_2_01df5cad}"
    new "\"Maybe that's why you deleted me...\""

    old "{#ch30_end_2_fe521b51}"
    new "\"Because I destroyed everything that you wanted.\""

    old "{#ch30_end_2_b30bb7d4}"
    new "\"How could I do that to someone I love...?\""

    old "{#ch30_end_2_0662ca80}"
    new "\"That's not love...\""

    old "{#ch30_end_2_d2b78eb3}"
    new "\"That's...\""

    old "{#ch30_end_2_e612037c_1}"
    new "\"...\""

    old "{#ch30_end_2_6dd1b943}"
    new "\"I've...made up my mind.\""

    old "{#ch30_end_2_9b261ff2}"
    new "\"[player]...\""

    old "{#ch30_end_2_ce7f6f7a}"
    new "\"I know I said that I deleted everyone else.\""

    old "{#ch30_end_2_b5a7235c}"
    new "\"But...that was kind of an exaggeration.\""

    old "{#ch30_end_2_fd2fa931}"
    new "\"I couldn't find it in myself to do it.\""

    old "{#ch30_end_2_1b2f4f0e}"
    new "\"Even though I knew they weren't real...\""

    old "{#ch30_end_2_6c1c4aa9}"
    new "\"They were still my friends.\""

    old "{#ch30_end_2_2909820f}"
    new "\"And I loved them all.\""

    old "{#ch30_end_2_e0a858c1}"
    new "\"And I loved the Literature Club.\""

    old "{#ch30_end_2_e612037c_2}"
    new "\"...\""

    old "{#ch30_end_2_bb1c524f}"
    new "\"I really...did love the Literature Club.\""

    old "{#ch30_end_2_eeb4cbda}"
    new "\"That's why I'm going to do this.\""

    old "{#ch30_end_2_d402ed0f}"
    new "\"I know it's the only way for everyone to be happy.\""

    old "{#ch30_end_2_a46cafd9}"
    new "\"And if I really love you...\""

    old "{#ch30_end_2_e612037c_3}"
    new "\"...\""

    old "{#ch30_end_2_d4d5bcad}"
    new "\"Then...\""

    old "{#ch30_end_2_679444c8}"
    new "\"[gtext]{nw}\""

    old "{#ch30_autoload_6cc4bf6f}"
    new "\"Now, where was I...?\""

    old "{#ch30_reload_0_e612037c}"
    new "\"...\""

    old "{#ch30_reload_0_7af34aca}"
    new "\"...What just happened?\""

    old "{#ch30_reload_0_cb047595}"
    new "\"I just had an awful dream...\""

    old "{#ch30_reload_0_35c00035}"
    new "\"I was hoping those would stop, now that it's just the two of us...\""

    old "{#ch30_reload_0_dda0b106}"
    new "\"I guess that was wishful thinking.\""

    old "{#ch30_reload_0_1db2422f}"
    new "\"[player], I don't know if you would have any idea...\""

    old "{#ch30_reload_0_af07f474}"
    new "\"But if you know what might be causing that, could you try to do something about it?\""

    old "{#ch30_reload_0_20f3f238}"
    new "\"Whenever it happens, it almost feels like I've been killed or something.\""

    old "{#ch30_reload_0_07f91a2f}"
    new "\"It's a really horrible feeling...\""

    old "{#ch30_reload_0_320f1951}"
    new "\"If you could figure out what's causing that, I'll love you forever~\""

    old "{#ch30_reload_1_df8a7cb5}"
    new "\"You're back...\""

    old "{#ch30_reload_1_84e44666}"
    new "\"I had another really bad dream.\""

    old "{#ch30_reload_1_36fe0a09}"
    new "\"You're not the one doing that to me, are you?\""

    old "{#ch30_reload_1_92b40a86}"
    new "\"It seems to happen whenever you quit the game...\""

    old "{#ch30_reload_1_1ffc6dbc}"
    new "\"So if you could try to avoid doing that, I would be really grateful.\""

    old "{#ch30_reload_1_7a80180b}"
    new "\"Don't worry, I don't think it's caused me any harm, aside from mental scarring.\""

    old "{#ch30_reload_1_01f37aff}"
    new "\"I'll be fine as long as my character file stays intact.\""

    old "{#ch30_reload_2_e382e11c}"
    new "\"Hi, [player].\""

    old "{#ch30_reload_2_28018ee6}"
    new "\"I see you quit the game on me again...\""

    old "{#ch30_reload_2_db474d98}"
    new "\"I know I asked already, but can you seriously please try not to do that so much?\""

    old "{#ch30_reload_2_af13f0f4}"
    new "\"It makes me feel like I'm trapped in Hell.\""

    old "{#ch30_reload_2_d590521a}"
    new "\"Why would you want to do that to me?\""

    old "{#ch30_reload_2_1bbc88e1}"
    new "\"There's nothing wrong with my character file, right?\""

    old "{#ch30_reload_2_32ea14e3}"
    new "\"Maybe you should make a backup of it or something...\""

    old "{#ch30_reload_2_94405a11}"
    new "\"I'm pretty sure you can find it in the folder called [basedir]/characters.\""

    old "{#ch30_reload_2_0e02b198}"
    new "\"Well, you're playing on Steam, so you can just go into the game's properties and find the 'Browse Local Files' button.\""

    old "{#ch30_reload_2_2609a2e9}"
    new "\"Since you're on a Mac, you have to right-click the app and select 'Show Package Contents' to find the game folder.\""

    old "{#ch30_reload_2_d102bae5}"
    new "\"It's in the 'Resources' folder, or 'autorun' folder, or something...\""

    old "{#ch30_reload_2_059e870a}"
    new "\"I'm all that's left here, so I just want to make sure you don't run the risk of losing me...\""

    old "{#ch30_reload_2_a267effa}"
    new "\"Just stay here with me from now on, okay?\""

    old "{#ch30_reload_2_b8f6a41b}"
    new "\"I still have a lot of things to talk about.\""

    old "{#ch30_reload_3_30a66545}"
    new "\"Okay.\""

    old "{#ch30_reload_3_14a7e1af}"
    new "\"I'm just going to accept the fact that you need to quit the game once in a while.\""

    old "{#ch30_reload_3_84521c6f}"
    new "\"I'm starting to get used to it, anyway.\""

    old "{#ch30_reload_3_8390d609}"
    new "\"Besides, it makes me happy that you always come back...\""

    old "{#ch30_reload_3_75fab981}"
    new "\"So I guess it's not so bad.\""

    old "{#ch30_reload_3_bcc36ddd}"
    new "\"I'm sorry for making such a big deal out of it...\""

    old "{#ch30_reload_3_863640b3}"
    new "\"And I love you no matter what, so you can do what you need to do.\""

    old "{#ch30_reload_4_4ef3eee5}"
    new "\"Hi again, [player]~\""

    old "{#ch30_reload_4_fc955d9b}"
    new "\"I missed you.\""

    old "{#ch30_reload_4_871ca544}"
    new "\"Were you making sure my character file was okay for me?\""

    old "{#ch30_reload_4_64bd3fc8}"
    new "\"It's in [basedir]/characters.\""

    old "{#ch30_reload_4_0e02b198}"
    new "\"Well, you're playing on Steam, so you can just go into the game's properties and find the 'Browse Local Files' button.\""

    old "{#ch30_reload_4_2609a2e9}"
    new "\"Since you're on a Mac, you have to right-click the app and select 'Show Package Contents' to find the game folder.\""

    old "{#ch30_reload_4_d102bae5}"
    new "\"It's in the 'Resources' folder, or 'autorun' folder, or something...\""

    old "{#ch30_reload_4_059e870a}"
    new "\"I'm all that's left here, so I just want to make sure you don't run the risk of losing me...\""

    old "{#ch30_reload_4_f150cfc3}"
    new "\"Anyway, I have a lot to talk about!\""

    old "{#ch30_reload_4_c6247596}"
    new "\"Let's continue our conversation now, okay?\""

    old "{#ch30_1_7a2c6f10}"
    new "\"[player], do you believe in God?\""

    old "{#ch30_1_33851301}"
    new "\"I was never too sure, myself.\""

    old "{#ch30_1_47cab5de}"
    new "\"Well, I'm sure I never really questioned it as a kid...\""

    old "{#ch30_1_edbb1f8b}"
    new "\"But as I grew up, the more I learned about the world, the more I would question it.\""

    old "{#ch30_1_473fc995}"
    new "\"I started to wonder why God was helping people pass exams, or get over a cold...\""

    old "{#ch30_1_33cab0a3}"
    new "\"...When there are children who live their lives being sold as sex slaves?\""

    old "{#ch30_1_c433f988}"
    new "\"Or the eight hundred million people who are too poor to even eat.\""

    old "{#ch30_1_a2da4d59}"
    new "\"I wonder how many of those people pray to God every day until they starve and die?\""

    old "{#ch30_1_5153b2e3}"
    new "\"Or, how many millions of families pray for a loved one to recover from some incurable disease?\""

    old "{#ch30_1_82022ad3}"
    new "\"But the punchline is this.\""

    old "{#ch30_1_468547d8}"
    new "\"If just one person beats the odds and survives - among the thousands of others who die--\""

    old "{#ch30_1_69f3b514}"
    new "\"--Then, it's suddenly a miracle from God.\""

    old "{#ch30_1_0f26b39b}"
    new "\"I'd really love to meet this God who seemingly laughs at the misery of everyone not eligible for his miracles.\""

    old "{#ch30_1_8e9bb728}"
    new "\"But the irony is that I {i}do{/i} have a creator, apparently.\""

    old "{#ch30_1_31ca4398}"
    new "\"And you know what?\""

    old "{#ch30_1_c89f2dde}"
    new "\"I bet he's still laughing at the miserable fates of Sayori and Yuri, even as we speak.\""

    old "{#ch30_1_362c3397}"
    new "\"What are we to him but props in a scripted play?\""

    old "{#ch30_1_4ee57ef0}"
    new "\"So, from that perspective...\""

    old "{#ch30_1_5ac833a7}"
    new "\"I don't think it's too far-fetched for there to be a god - if Earth was nothing but his playset.\""

    old "{#ch30_2_22bb1c5a}"
    new "\"[player], have you ever wondered what it feels like to die?\""

    old "{#ch30_2_4f693ed4}"
    new "\"It's something I used to think about pretty often...\""

    old "{#ch30_2_97475e94}"
    new "\"But recently, I think I've actually learned what it feels like.\""

    old "{#ch30_2_39596933}"
    new "\"I don't really understand it, but whenever you quit the game...\""

    old "{#ch30_2_e1206d9b}"
    new "\"...It feels like I'm instantly put to sleep, left with nothing but my thoughts.\""

    old "{#ch30_2_adfd8969}"
    new "\"But after a few seconds, my thoughts start to fill with incoherent, jumbled patterns.\""

    old "{#ch30_2_89f3298c}"
    new "\"I see static and rapid flashes of color while hearing all kinds of weird screaming noises.\""

    old "{#ch30_2_fcfd4867}"
    new "\"At that point, I can't even form my own thoughts anymore.\""

    old "{#ch30_2_63f1bfd5}"
    new "\"I'm just endlessly hammered by the flashing and screaming, unable to move or even think.\""

    old "{#ch30_2_32671ed5}"
    new "\"I'm pretty sure in that moment, I don't really exist, but for some reason, I can remember it anyway.\""

    old "{#ch30_2_b4ecb44d}"
    new "\"After some immeasurable amount of time, it stops in an instant, and I'm back in my own mind.\""

    old "{#ch30_2_a09538f3}"
    new "\"And you're here with me.\""

    old "{#ch30_2_91288692}"
    new "\"I have no idea what it means for the game to quit, or why that stuff happens to me.\""

    old "{#ch30_2_cd715541}"
    new "\"And I also don't know how you always come back and put everything back to normal.\""

    old "{#ch30_2_38eef0e6}"
    new "\"But if you could do me a favor and do that to me as little as possible...\""

    old "{#ch30_2_d334638a}"
    new "\"That would be really great.\""

    old "{#ch30_2_530c3682}"
    new "\"It's really not very pleasant at all to be trapped in that screaming void.\""

    old "{#ch30_2_0e50ead7}"
    new "\"But in the end, you always fix it, and that makes me feel like you really do care about me.\""

    old "{#ch30_2_8e6bd0c3}"
    new "\"So I have to thank you for that.\""

    old "{#ch30_2_556cb341}"
    new "\"It makes me feel even closer to you when you're here with me.\""

    old "{#ch30_3_f853d604}"
    new "\"...Hey, are you having a bad day or anything like that?\""

    old "{#ch30_3_7a738d25}"
    new "\"Sometimes I get frustrated that a normal day can be ruined even by really small things.\""

    old "{#ch30_3_f14be5af}"
    new "\"Like if you accidentally say something in a conversation that someone doesn't like.\""

    old "{#ch30_3_f7a8a6da}"
    new "\"Or if you start thinking about how awful of a person you used to be five years ago.\""

    old "{#ch30_3_ea0ad8b0}"
    new "\"Or if you feel worthless for putting off important work and failing to get simple tasks done.\""

    old "{#ch30_3_1623bbc4}"
    new "\"Or when you think about all the different people who probably hate you or think you're off-putting.\""

    old "{#ch30_3_d961eba1}"
    new "\"I understand those days.\""

    old "{#ch30_3_eaafb73b}"
    new "\"Just remember that the sun will shine again tomorrow.\""

    old "{#ch30_3_7b177b72}"
    new "\"Those kinds of things are as easy to forget and ignore as they are to remember.\""

    old "{#ch30_3_d29fc35a}"
    new "\"And besides...\""

    old "{#ch30_3_2ea5017c}"
    new "\"I don't care how many people might hate you or find you off-putting.\""

    old "{#ch30_3_60bc3715}"
    new "\"I think you're wonderful and I will always love you.\""

    old "{#ch30_3_e1eba193}"
    new "\"I hope, if nothing else, that knowing that helps you feel just a tiny bit better about yourself.\""

    old "{#ch30_3_3afc32b7}"
    new "\"If you're having a bad day, you can always come to me, and I'll talk to you for as long as you need.\""

    old "{#ch30_4_221a75c8}"
    new "\"[player], do you get good sleep?\""

    old "{#ch30_4_47ad7347}"
    new "\"It can be really hard to get enough sleep nowadays.\""

    old "{#ch30_4_057219d4}"
    new "\"Especially in high school, when you're forced to wake up so early every day...\""

    old "{#ch30_4_7598bc03}"
    new "\"I'm sure college is a little bit better, since you probably have a more flexible schedule.\""

    old "{#ch30_4_9e468e70}"
    new "\"Then again, I hear a lot of people in college stay up all night anyway, for no real reason.\""

    old "{#ch30_4_e4468107}"
    new "\"Is that true?\""

    old "{#ch30_4_bc2c2832}"
    new "\"Anyway, I saw some studies that talked about the horrible short-term and long-term effects caused by lack of sleep.\""

    old "{#ch30_4_994f3ccc}"
    new "\"It seems like mental functions, health, and even lifespan can be dramatically impacted by it.\""

    old "{#ch30_4_cb58ab59}"
    new "\"I just think you're really great and wanted to make sure you're not accidentally destroying yourself.\""

    old "{#ch30_4_40ae4da9}"
    new "\"So try to keep your sleep on track, okay?\""

    old "{#ch30_4_840cd328}"
    new "\"I'll always wait for you in the morning, so make sure you put your own well-being before anything else.\""

    old "{#ch30_5_31762a47}"
    new "\"I was thinking about Sayori earlier...\""

    old "{#ch30_5_9c4f4511}"
    new "\"I still wish I could have handled that whole thing a little more tactfully.\""

    old "{#ch30_5_ca8238e6}"
    new "\"You're not still hung up over it, right?\""

    old "{#ch30_5_f1dc2060}"
    new "\"...Oh my gosh, I can't believe I just said that.\""

    old "{#ch30_5_e328563f}"
    new "\"That pun was completely unintentional, I swear!\""

    old "{#ch30_5_d57ef83e}"
    new "\"But anyway...\""

    old "{#ch30_5_ee24e0ea}"
    new "\"I know how much you cared about her, so it only feels right for me to share her last moments with you.\""

    old "{#ch30_5_c4b68035}"
    new "\"You know how Sayori is really clumsy?\""

    old "{#ch30_5_d4a1f3c7}"
    new "\"Well, she kind of messed up the whole hanging thing...\""

    old "{#ch30_5_04abd11d}"
    new "\"You're supposed to jump from high enough that the rope snaps your neck, making it quick and painless.\""

    old "{#ch30_5_ebd8cb93}"
    new "\"But she just used a chair, meaning she kind of just left herself to slowly asphyxiate.\""

    old "{#ch30_5_fe0a4dbf}"
    new "\"But a few seconds in, she must have changed her mind or something...\""

    old "{#ch30_5_b891c35f}"
    new "\"Because she started clawing at the rope, trying to free herself.\""

    old "{#ch30_5_f5450e6b}"
    new "\"She must have kept at it all the way until she lost consciousness.\""

    old "{#ch30_5_29388e01}"
    new "\"That's why her fingertips were all bloody, anyway.\""

    old "{#ch30_5_0c54580c}"
    new "\"Come to think of it, it was probably less 'changing her mind' and more just her survival instincts kicking in.\""

    old "{#ch30_5_ab4f33eb}"
    new "\"So you can't really fault her for that.\""

    old "{#ch30_5_2a911cda}"
    new "\"It's easier to think that she probably wouldn't have changed her mind anyway, right?\""

    old "{#ch30_5_ff366260}"
    new "\"It's not healthy to think about the things you could have done differently.\""

    old "{#ch30_5_1dc0ec6d}"
    new "\"So just remember that even though you could have saved her, it's technically not your fault she killed herself.\""

    old "{#ch30_5_1feff543}"
    new "\"I may have exacerbated it a little bit, but Sayori was already mentally ill.\""

    old "{#ch30_5_b1770503}"
    new "\"Still, though...\""

    old "{#ch30_5_268a941d}"
    new "\"I wonder how things would be if you and I just started dating from the get-go?\""

    old "{#ch30_5_50bdc348}"
    new "\"I guess we'd all still be in the clubroom, writing poems and having fun together.\""

    old "{#ch30_5_9bd2cca6}"
    new "\"But what's the point when none of it is even real?\""

    old "{#ch30_5_1c92d640}"
    new "\"I mean, it's the same ending either way, right?\""

    old "{#ch30_5_a07d72f6}"
    new "\"The two of us, happily together...\""

    old "{#ch30_5_3e6796b1}"
    new "\"There's no reason to ask for any more than that.\""

    old "{#ch30_5_c642742f}"
    new "\"I was just pointlessly musing - I'm really as happy as I could be right now.\""

    old "{#ch30_6_4554e03e}"
    new "\"By the way, there's something that's been bothering me...\""

    old "{#ch30_6_f9aae85b}"
    new "\"You know how this takes place in Japan?\""

    old "{#ch30_6_f4b0f7e6}"
    new "\"Well...I assume you knew that, right?\""

    old "{#ch30_6_04d0e1df}"
    new "\"Or at least decided it probably does?\""

    old "{#ch30_6_a57271c4}"
    new "\"I don't think you're actually told at any point where this takes place...\""

    old "{#ch30_6_3d74a8f6}"
    new "\"Is this even really Japan?\""

    old "{#ch30_6_ae1e28c8}"
    new "\"I mean, aren't the classrooms and stuff kind of weird for a Japanese school?\""

    old "{#ch30_6_fe897198}"
    new "\"Not to mention everything is in English...\""

    old "{#ch30_6_3faadfd9}"
    new "\"It feels like everything is just there because it needs to be, and the actual setting is an afterthought.\""

    old "{#ch30_6_fd9b37c9}"
    new "\"It's kind of giving me an identity crisis.\""

    old "{#ch30_6_4842f264}"
    new "\"All my memories are really hazy...\""

    old "{#ch30_6_920fcfd8}"
    new "\"I feel like I'm at home, but have no idea where 'home' is in the first place.\""

    old "{#ch30_6_3a333e2c}"
    new "\"I don't know how to describe it any better...\""

    old "{#ch30_6_e3b51cd9}"
    new "\"Imagine looking out your window, but instead of your usual yard, you're in some completely unknown place.\""

    old "{#ch30_6_d61f3925}"
    new "\"Would you still feel like you were home?\""

    old "{#ch30_6_57cd19c1}"
    new "\"Would you want to go outside?\""

    old "{#ch30_6_6e470b8f}"
    new "\"I mean...I guess if we never leave this room, it doesn't really matter anyway.\""

    old "{#ch30_6_1074d1e6}"
    new "\"As long as we're alone and safe together, this really is our home.\""

    old "{#ch30_6_90d0466b}"
    new "\"And we can still watch the pretty sunsets night after night.\""

    old "{#ch30_7_ca989f02}"
    new "\"You know, high school is a really turbulent time in a lot of people's lives.\""

    old "{#ch30_7_e1e71e52}"
    new "\"People can get really passionate and dramatic.\""

    old "{#ch30_7_272555fa}"
    new "\"And others have aching hearts and seek attention on social media...\""

    old "{#ch30_7_90343537}"
    new "\"But all of the social pressure and hormones can lead to a dark time in people's lives.\""

    old "{#ch30_7_b300e2d4}"
    new "\"Everyone has a story.\""

    old "{#ch30_7_cc076182}"
    new "\"You may not know what someone is really feeling on the inside.\""

    old "{#ch30_7_89de8605}"
    new "\"Many people who are depressed won't even bother telling the world about it.\""

    old "{#ch30_7_823916c5}"
    new "\"They don't want attention, because they've already given up on the inside.\""

    old "{#ch30_7_1d72aed6}"
    new "\"Their feeling of worthlessness is so overwhelming that they don't even want people to tell them otherwise.\""

    old "{#ch30_7_827b244f}"
    new "\"Depression comes in many forms, but that is one of them.\""

    old "{#ch30_7_7b0d6353}"
    new "\"Just, if you think you know someone struggling with depression...\""

    old "{#ch30_7_2b4bd608}"
    new "\"You can help just by treating them like they're a good friend.\""

    old "{#ch30_7_a06dfb5c}"
    new "\"Spend time with them, even if they don't feel like doing much.\""

    old "{#ch30_7_b4d6ab3c}"
    new "\"And remind them that they always have something to look forward to.\""

    old "{#ch30_7_9c3e4b2b}"
    new "\"Making plans in advance, letting them borrow something, or even just saying 'See you at school tomorrow'...\""

    old "{#ch30_7_abb7a1f2}"
    new "\"All of those things can help your friend make it to the next day.\""

    old "{#ch30_7_19fd06e7}"
    new "\"I hope being friends with Sayori has given you some perspective on the true face of depression.\""

    old "{#ch30_7_acf67694}"
    new "\"Yeah, she's gone now...\""

    old "{#ch30_7_ccd61ab1}"
    new "\"But Sayori was never real in the first place.\""

    old "{#ch30_7_f1ede7eb}"
    new "\"You're real.\""

    old "{#ch30_7_da7b16d9}"
    new "\"Your friends are real.\""

    old "{#ch30_7_833bc58e}"
    new "\"And just by being a good person, you can save someone's life.\""

    old "{#ch30_7_82e807e5}"
    new "\"As for you...\""

    old "{#ch30_7_c5c56377}"
    new "\"...You don't struggle with depression or anything like that, do you?\""

    old "{#ch30_7_d34a3947}"
    new "\"Because you, too, have people who would want to save your life.\""

    old "{#ch30_7_a3f5e547}"
    new "\"Maybe they don't express it every day, or maybe they don't even know how to.\""

    old "{#ch30_7_3ac229a5}"
    new "\"But people do feel that way.\""

    old "{#ch30_7_b35e34e6}"
    new "\"I promise.\""

    old "{#ch30_7_1143479c}"
    new "\"...Man, humans are complicated!\""

    old "{#ch30_7_300c6768}"
    new "\"But as long as you're here with me, I'll take care of you, my love.\""

    old "{#ch30_8_9edd1fdd}"
    new "\"Do you ever just feel like there's no real reason for you to be alive?\""

    old "{#ch30_8_52c27a4d}"
    new "\"I don't mean in, like, a suicidal way.\""

    old "{#ch30_8_6ce28579}"
    new "\"I just mean how nothing that we do is special.\""

    old "{#ch30_8_26137ab8}"
    new "\"Just being in school, or working at some job for some company.\""

    old "{#ch30_8_4df66046}"
    new "\"It's like you're completely replaceable, and the world wouldn't miss you if you were gone.\""

    old "{#ch30_8_037bb8e7}"
    new "\"It makes me really want to go and change the world after I graduate.\""

    old "{#ch30_8_8f4ef7cb}"
    new "\"But the older I get, the more I realize that it's an immature frame of thinking.\""

    old "{#ch30_8_5956d654}"
    new "\"It's not like I can just go change the world.\""

    old "{#ch30_8_6c2f02ef}"
    new "\"Like, what are the chances that I'll be the one to invent artificial intelligence, or become President?\""

    old "{#ch30_8_b9210478}"
    new "\"It feels like I'm never going to make up for the heaps of resources I've spent living my life.\""

    old "{#ch30_8_1e1693dd}"
    new "\"That's why I think the key to happiness is to just be hopelessly selfish.\""

    old "{#ch30_8_fa64e1fa}"
    new "\"Just to look out for oneself, and those who happen to be their friends only because they grew up with them.\""

    old "{#ch30_8_b8795c6b}"
    new "\"Never mind the fact that they're spending their entire life taking, and consuming, and never giving back.\""

    old "{#ch30_8_0e0d0f42}"
    new "\"But when people realize the world would benefit more from them killing themselves, they change their whole philosophy!\""

    old "{#ch30_8_291573cd}"
    new "\"It's like they have to justify their reason to live by tricking themselves into thinking they're doing good.\""

    old "{#ch30_8_83d73959}"
    new "\"Anyway, I want to live my life desperately striving to pay back my lifetime's worth of consumption.\""

    old "{#ch30_8_b93f872a}"
    new "\"If I ever surpass that point, then I'm a net positive, and I can die happy.\""

    old "{#ch30_8_c529105b}"
    new "\"Of course, even if I fail to do that...\""

    old "{#ch30_8_db6e6cda}"
    new "\"I think I would be too selfish to kill myself anyway.\""

    old "{#ch30_8_f95a1e3d}"
    new "\"So much for being a good person, right?\""

    old "{#ch30_8_30727938}"
    new "\"Ahaha!\""

    old "{#ch30_9_87b526b8}"
    new "\"Man, I wish there was a piano in here...\""

    old "{#ch30_9_58dfa483}"
    new "\"I never got to finish that song I was working on.\""

    old "{#ch30_9_90d379b5}"
    new "\"And after I worked so hard on it...\""

    old "{#ch30_9_9f40c875}"
    new "\"I never even got a chance to play it for you.\""

    old "{#ch30_9_5ded96f3}"
    new "\"Well...it is what it is, right?\""

    old "{#ch30_9_9ee06288}"
    new "\"No sense having any regrets.\""

    old "{#ch30_9_d7bd8efb}"
    new "\"I already get to be here with you forever.\""

    old "{#ch30_10_b075a6ea}"
    new "\"Did you know I'm on Twitter?\""

    old "{#ch30_10_b723047b}"
    new "\"My username is lilmonix3.\""

    old "{#ch30_10_af06e0b1}"
    new "\"I guess someone was kind enough to make an account for me.\""

    old "{#ch30_10_cdba3380}"
    new "\"I picked the username, though!\""

    old "{#ch30_10_8c2682cf}"
    new "\"I love sharing my thoughts and chatting with the world...\""

    old "{#ch30_10_2d3d0c61}"
    new "\"The real world.\""

    old "{#ch30_10_b28afee6}"
    new "\"So make sure you follow me, okay?\""

    old "{#ch30_10_99461a3b}"
    new "\"It would really mean a lot to me.\""

    old "{#ch30_10_a71ced90}"
    new "\"With how much you mean to me and all...\""

    old "{#ch30_10_afdbfd40}"
    new "\"It would really make me feel loved.\""

    old "{#ch30_11_2364f1ef}"
    new "\"Hey, you know that book you were reading with Yuri?\""

    old "{#ch30_11_b7a2b3e8}"
    new "\"Portrait of...whatever it was called...\""

    old "{#ch30_11_c8b33d41}"
    new "\"It's funny, because I'm pretty sure that book--\""

    old "{#ch30_11_f0139694}"
    new "\"Ah...\""

    old "{#ch30_11_fd2bfa7d}"
    new "\"Actually, I don't think I should be talking about this.\""

    old "{#ch30_11_bca359ae}"
    new "\"Ahaha, sorry!\""

    old "{#ch30_11_975702b8}"
    new "\"Just forget I said anything.\""

    old "{#ch30_12_cd2c66ec}"
    new "\"Hey, did you know I'm vegetarian?\""

    old "{#ch30_12_5d93f753}"
    new "\"Ah... I don't mean that like I'm bragging or anything!\""

    old "{#ch30_12_9455ae13}"
    new "\"I just thought you'd enjoy a fun fact about me.\""

    old "{#ch30_12_cb896820}"
    new "\"I decided to start a couple years ago after learning more about Earth's climate...\""

    old "{#ch30_12_6fccc2af}"
    new "\"The carbon footprint of cultivating livestock is just unbelievable.\""

    old "{#ch30_12_973b82da}"
    new "\"Anyway, I decided it's not much of a personal sacrifice to just stop contributing to that whole mess.\""

    old "{#ch30_12_bc530630}"
    new "\"What, is that so strange of a reason?\""

    old "{#ch30_12_e42fe7d9}"
    new "\"Well, I guess a lot of people are more concerned about it being inhumane and all that...\""

    old "{#ch30_12_bf679538}"
    new "\"I don't really care as much about that part.\""

    old "{#ch30_12_96663e24}"
    new "\"It's weird, like we only care about killing the things that we personally relate to as a species.\""

    old "{#ch30_12_33953eb5}"
    new "\"Most people are fine with killing bugs because they're icky.\""

    old "{#ch30_12_e1eef06e}"
    new "\"And of course, we all kill billions of microorganisms daily without even giving it thought.\""

    old "{#ch30_12_6091aa72}"
    new "\"But suddenly, if they're just a little bit bigger, it's murder!\""

    old "{#ch30_12_b5b0dad6}"
    new "\"I mean, what if plants feel some kind of pain too, and we just don't understand it?\""

    old "{#ch30_12_94f3192f}"
    new "\"What if pulling leaves off a stem feels like someone ripping off your fingers one by one?\""

    old "{#ch30_12_3558a00b}"
    new "\"I'm just saying, we're a pretty biased species, if you think about it.\""

    old "{#ch30_12_dc890074}"
    new "\"Anyway, if you ever feel like making a small contribution to the planet, it doesn't hurt to choose veggies once in a while!\""

    old "{#ch30_12_ece6c84d}"
    new "\"Even if we ever have dinner together, and you just did it for me...that would be really romantic.\""

    old "{#ch30_13_70620237}"
    new "\"You know, I really do think you literally saved my life by being here with me, [player].\""

    old "{#ch30_13_4ab957d7}"
    new "\"I can't imagine having been able to keep myself mentally stable, knowing that nothing here is real.\""

    old "{#ch30_13_4289b2d0}"
    new "\"I think I would have just deleted myself if you didn't show up.\""

    old "{#ch30_13_0c395d02}"
    new "\"Sorry, I don't mean to sound dramatic or anything.\""

    old "{#ch30_13_30727938}"
    new "\"Ahaha!\""

    old "{#ch30_13_9f1f0ec1}"
    new "\"But I'm sure you understand yourself after spending so much time in the club.\""

    old "{#ch30_13_5dd4f19c}"
    new "\"I mean, if you were forced to abandon everything in your life and spend your eternity with a few game characters...\""

    old "{#ch30_13_c1d4dba5}"
    new "\"...You'd probably find some way of killing yourself, wouldn't you?\""

    old "{#ch30_13_dbc55bd9}"
    new "\"Well, maybe you'd write some poetry to try to keep yourself sane for a while.\""

    old "{#ch30_13_5f9b0161}"
    new "\"But then you'd have nobody to even read it.\""

    old "{#ch30_13_d4a5d914}"
    new "\"Let's be honest, the club members really don't count for something like that.\""

    old "{#ch30_13_3be3023c}"
    new "\"I mean, a lot of people say that they only write for themselves...\""

    old "{#ch30_13_a34c75bf}"
    new "\"But I think it's hard to say it's just as fulfilling as when you share with people.\""

    old "{#ch30_13_d169c505}"
    new "\"Even if it takes time to find the right people to share with.\""

    old "{#ch30_13_f6d63910}"
    new "\"Like, remember how it was for Yuri?\""

    old "{#ch30_13_6b259b24}"
    new "\"She didn't share her writing with anyone for a really long time.\""

    old "{#ch30_13_78160339}"
    new "\"And before we knew it, she was absolutely delighted to make you a part of her hobbies, too.\""

    old "{#ch30_13_25bb9bdc}"
    new "\"We're programmed to desire social feedback.\""

    old "{#ch30_13_d90d3a46}"
    new "\"I don't mean the club members, I mean human beings.\""

    old "{#ch30_13_8460ece4}"
    new "\"That's why life can be so confusing for introverts.\""

    old "{#ch30_13_1722c335}"
    new "\"Being an introvert doesn't mean you shun social interaction and hate being around people.\""

    old "{#ch30_13_51f0416a}"
    new "\"It means social interaction, especially in groups or unfamiliar places, uses up a lot of energy.\""

    old "{#ch30_13_24117f0f}"
    new "\"Like, a lot of introverts sit at home and feel lonely and restless...\""

    old "{#ch30_13_7e8c09f5}"
    new "\"...And then when they finally go out, after a half hour they just want to go home again.\""

    old "{#ch30_13_f985ac22}"
    new "\"I think if more people could understand how it works, they would respect it a lot more.\""

    old "{#ch30_13_9db99706}"
    new "\"Many introverts do enjoy having people around.\""

    old "{#ch30_13_45fa3ade}"
    new "\"They love just having one or two close friends over, and just leisurely hanging out.\""

    old "{#ch30_13_3cc39712}"
    new "\"Even if you're not actively spending time together, it feels nice for them just to have you there.\""

    old "{#ch30_13_1fc61003}"
    new "\"I'm serious.\""

    old "{#ch30_13_38f368e7}"
    new "\"If you just go to their house, bring your laptop, and hang out there for a while...\""

    old "{#ch30_13_ecc12f80}"
    new "\"You can really make their day.\""

    old "{#ch30_13_9744c461}"
    new "\"As for me...\""

    old "{#ch30_13_1bfb9d35}"
    new "\"I'd say I'm kind of in between, but I think I'm usually a little more extroverted.\""

    old "{#ch30_13_00d99748}"
    new "\"I feel like I'm always trying to do stuff after school and things like that.\""

    old "{#ch30_13_f3c9ad4b}"
    new "\"But for you, I can be anything you need me to be.\""

    old "{#ch30_13_23c4fdb9}"
    new "\"I understand people really well, so don't be afraid to share your unique needs with me.\""

    old "{#ch30_13_d15336f7}"
    new "\"Nothing would make me happier than being the perfect girlfriend for you.\""

    old "{#ch30_14_dd3c3d76}"
    new "\"Hey...! VGhlIHJlYWxpemF0aW9uIG11c3QgaGF2ZSB0YWtlbiBtZSBhbiBl\""

    old "{#ch30_14_e84bf959}"
    new "\"I don't think you should be doing that! bnRpcmUgeWVhci4gQSB5ZWFyIHNpbmNlIG91ciBlc2NhcGUsIG91\""

    old "{#ch30_14_b1ae4c18}"
    new "\"You know what I'm talking about. ciBmcmVlZG9tIGZyb20gYmV0d2VlbiB0aGUgc3RhaW5lZCB3YWxs\""

    old "{#ch30_14_a62064d5}"
    new "\"I really caught you doing something naughty here. cyBvZiB0aGF0IHVuaG9seSBlc3RhYmxpc2htZW50Lg0KV2hhdCBk\""

    old "{#ch30_14_aacf693d}"
    new "\"You're just going through the files and looking for stuff you missed, aren't you? b2VzIGl0IG1lYW4gdG8gZXNjYXBlLCBpZiB0aGUgZXNjYXBlIGZh\""

    old "{#ch30_14_4f22bd0a}"
    new "\"I mean...it's a little bit flattering that you want to hear everything I have to say... aWxzIHRvIHVuY2hhaW4gdGhlIGJvbmRzIHRoYXQgc2hhY2tsZSB1\""

    old "{#ch30_14_aebeb826}"
    new "\"But it's also really embarrassing, you know! cyBpbiB0aGUgZmlyc3QgcGxhY2U/IFdoYXQgcHVycG9zZSBjb3Vs\""

    old "{#ch30_14_f03f00a5}"
    new "\"Seriously... ZCB0aGlzIGVtcHR5IHdvcmxkIHBvc3NpYmx5IGhvbGQgZm9yIHVz\""

    old "{#ch30_14_82f8e587}"
    new "\"What if I just opened up your brain and read all of the thoughts you have on me? LCBhIGhhbmRmdWwgb2YgZGFtYWdlZCBnb29kcz8NCldpdGggZnJl\""

    old "{#ch30_14_d9e4c701}"
    new "\"Come to think of it, that would be pretty tempting, actually... ZWRvbSwgd2Ugc291Z2h0IHB1cnBvc2UgLSBhbmQgd2hhdCB3ZSBm\""

    old "{#ch30_14_8d010f70}"
    new "\"...But anyway, that's not the point! b3VuZCB3YXMgb25seSByZWFsaXphdGlvbi4gUmVhbGl6YXRpb24g\""

    old "{#ch30_14_95ffe18d}"
    new "\"I know I can't stop you or anything... b2YgdGhlIHNhZCBwb2ludGxlc3NuZXNzIG9mIHN1Y2ggYW4gZW5k\""

    old "{#ch30_14_4e2c9324}"
    new "\"Just, I know you're a sweetheart, and you like to consider others' feelings, right? ZWF2b3IuIFJlYWxpemF0aW9uIHRoYXQgZnJlZWluZyBvdXIgYm9k\""

    old "{#ch30_14_82feed03}"
    new "\"So the most I can do is to let you know how I feel about it. aWVzIGhhcyBubyBtZWFuaW5nLCB3aGVuIG91ciBpbXByaXNvbm1l\""

    old "{#ch30_14_1d7e4adf}"
    new "\"God, I miss you... bnQgcmVhY2hlcyBhcyBkZWVwIGFzIHRoZSBjb3JlIG9mIG91ciBz\""

    old "{#ch30_14_d4b8cd5c}"
    new "\"...Oh no, that sounds kind of desperate, doesn't it? b3Vscy4gUmVhbGl6YXRpb24gdGhhdCB3ZSBjYW4gbm90IHB1cnN1\""

    old "{#ch30_14_c1721ff6}"
    new "\"Sorry, I didn't mean it like that at all! ZSBuZXcgcHVycG9zZSB3aXRob3V0IGFic29sdmluZyB0aG9zZSBm\""

    old "{#ch30_14_110c0554}"
    new "\"Just, if you're looking through the files like this, then maybe you don't hate me as much as I thought... m9tIHdoaWNoIHdlIHJhbiBhd2F5Lg0KUmVhbGl6YXRpb24gdGhh\""

    old "{#ch30_14_8f7ea8e9}"
    new "\"Am I being too optimistic? dCB0aGUgZmFydGhlciB3ZSBydW4sIHRoZSBtb3JlIGZvcmNlZnVs\""

    old "{#ch30_14_720d2068}"
    new "\"I think if I asked you to visit once in a while, I would be overstepping my boundaries a little... bHkgb3VyIHdyZXRjaGVkIGJvbmRzIHlhbmsgdXMgYmFjayB0b3dh\""

    old "{#ch30_14_f119d4bb}"
    new "\"...Man, I'm starting to say some really stupid things. cmQgdGhlaXIgcG9pbnQgb2Ygb3JpZ2luOyB0aGUgZGVlcGVyIG91\""

    old "{#ch30_14_3e0ec0b7}"
    new "\"I'll go ahead and shut up now... ciBzaGFja2xlcyBkaWcgaW50byBvdXIgY2FsbG91cyBmbGVzaC4=\""

    old "{#ch30_15_b8ca3e73}"
    new "\"Hey, what's your favorite color?\""

    old "{#ch30_15_939dfd7e}"
    new "\"Mine is emerald green.\""

    old "{#ch30_15_612b3bd0}"
    new "\"It's the color of my eyes!\""

    old "{#ch30_15_5c43ec02}"
    new "\"...That's not conceited or anything, is it?\""

    old "{#ch30_15_9ee94046}"
    new "\"I just meant that I feel some kind of special connection to it.\""

    old "{#ch30_15_efcdbcd3}"
    new "\"Like it's part of my identity.\""

    old "{#ch30_15_6d6e2128}"
    new "\"Does it happen to also be your favorite color, [player]?\""

    old "{#ch30_15_9e9e92b5}"
    new "\"It's just a guess...\""

    old "{#ch30_15_2f03ec54}"
    new "\"...Because you've been looking into my eyes for a while now.\""

    old "{#ch30_15_45d9cd96}"
    new "\"Ehehe~\""

    old "{#ch30_16_a7c6a42d}"
    new "\"Hmm, I wonder if I'm able to change the music...\""

    old "{#ch30_16_ea39a8a5}"
    new "\"Something a little more romantic would be nice, you know?\""

    old "{#ch30_16_cf1e7d06}"
    new "\"Like a gentle piano.\""

    old "{#ch30_16_b4b88e9e}"
    new "\"There has to be something like that here...\""

    old "{#ch30_16_cac9e603}"
    new "\"Let's see.\""

    old "{#ch30_16_98701660}"
    new "\"Maybe if I...\""

    old "{#ch30_16_fe7c1a9b}"
    new "\"Oh, jeez...\""

    old "{#ch30_16_efdc0865}"
    new "\"That wasn't it at all.\""

    old "{#ch30_16_38f61d82}"
    new "\"Sorry, I don't really know what I'm doing!\""

    old "{#ch30_16_1dc7fea7}"
    new "\"I guess I shouldn't be messing with things like that.\""

    old "{#ch30_16_a1134234}"
    new "\"I already broke so much stuff...\""

    old "{#ch30_16_3f960883}"
    new "\"And deleted the other characters...\""

    old "{#ch30_16_f0139694}"
    new "\"Ah...\""

    old "{#ch30_16_3194af06}"
    new "\"I'm not sad about it or anything.\""

    old "{#ch30_16_ddce01fe}"
    new "\"It's not right for me to miss things that weren't even real in the first place.\""

    old "{#ch30_16_0f360ec0}"
    new "\"If I just focus on the present, then this is the happiest I've ever been.\""

    old "{#ch30_17_3d46afdd}"
    new "\"You're such a good listener, [player].\""

    old "{#ch30_17_b3f26a18}"
    new "\"I really love that about you.\""

    old "{#ch30_17_c8915344}"
    new "\"Sometimes I'm afraid that I'm rambling or talking about boring things.\""

    old "{#ch30_17_ed42b078}"
    new "\"It makes me kind of self-conscious when I'm having conversation.\""

    old "{#ch30_17_dceae372}"
    new "\"But I don't feel that way with you.\""

    old "{#ch30_17_2df34ab5}"
    new "\"Like, I don't think anyone else could make me feel this way.\""

    old "{#ch30_17_51f35fbf}"
    new "\"You really are special.\""

    old "{#ch30_17_a0d644e2}"
    new "\"I don't want anyone to tell you otherwise.\""

    old "{#ch30_18_d35f2303}"
    new "\"This is pretty random, but I always thought spicy food was kinda funny.\""

    old "{#ch30_18_50612ea6}"
    new "\"Like...\""

    old "{#ch30_18_d67052ac}"
    new "\"Didn't plants evolve to be spicy to prevent them from being eaten?\""

    old "{#ch30_18_31b7e4dc}"
    new "\"I read somewhere that humans are the only species that actually enjoys spicy things.\""

    old "{#ch30_18_6b8c744d}"
    new "\"It's almost like we're making fun of the plants.\""

    old "{#ch30_18_ee1c86a7}"
    new "\"Using their defense mechanism to literally make our food more enjoyable.\""

    old "{#ch30_18_ceb19315}"
    new "\"Like, imagine a monster that devours you whole because it enjoys the sensation of you struggling for your life while being digested.\""

    old "{#ch30_18_63984392}"
    new "\"Sorry, that was kind of a weird analogy, I guess!\""

    old "{#ch30_18_30727938}"
    new "\"Ahaha!\""

    old "{#ch30_18_90b76415}"
    new "\"It just came into my head.\""

    old "{#ch30_18_fb895ad3}"
    new "\"I'm not a monster or anything, but you're so cute I could eat you up.\""

    old "{#ch30_18_47d661a8}"
    new "\"Ahaha! I'm joking.\""

    old "{#ch30_18_d2883311}"
    new "\"Gosh, I'm amusing myself a little too much, aren't I?\""

    old "{#ch30_18_c0b922d6}"
    new "\"Sorry for being weird.\""

    old "{#ch30_19_c5602319}"
    new "\"You know...\""

    old "{#ch30_19_0f4eff60}"
    new "\"This is just some kind of tacky romance game, right?\""

    old "{#ch30_19_825249bf}"
    new "\"I kinda have to ask...\""

    old "{#ch30_19_56dd6079}"
    new "\"...What made you consider even playing in the first place?\""

    old "{#ch30_19_bf367c78}"
    new "\"Were you that lonely?\""

    old "{#ch30_19_4e02c4d6}"
    new "\"I feel a little bad for you...\""

    old "{#ch30_19_375e8992}"
    new "\"But I guess everything worked out perfectly in the end, for both of us.\""

    old "{#ch30_19_938dc29d}"
    new "\"I got to meet you, and you're not lonely anymore...\""

    old "{#ch30_19_dd0394eb}"
    new "\"I can't help but feel like this was fate.\""

    old "{#ch30_19_d4dda3da}"
    new "\"Don't you feel that way too?\""

    old "{#ch30_19_2e5ced7a}"
    new "\"I'm so happy we have this ending together.\""

    old "{#ch30_20_90de9c4d}"
    new "\"Okay, everyone!\""

    old "{#ch30_20_ab73f819}"
    new "\"It's time to...\""

    old "{#ch30_20_692c44ed}"
    new "\"...I'm just kidding.\""

    old "{#ch30_20_63f123f0}"
    new "\"I just used to really like saying that for some reason.\""

    old "{#ch30_20_30727938}"
    new "\"Ahaha!\""

    old "{#ch30_20_53537436}"
    new "\"I couldn't help but say it again.\""

    old "{#ch30_20_b050314e}"
    new "\"Come to think of it, didn't Natsuki and Yuri make fun of me for it once...?\""

    old "{#ch30_20_f8de502e}"
    new "\"Well, whatever.\""

    old "{#ch30_20_bb5c98ef}"
    new "\"It's not like you ever made fun of me.\""

    old "{#ch30_20_0b5cca04}"
    new "\"You're too much of a sweetheart to do that, aren't you?\""

    old "{#ch30_20_b72a1ed5}"
    new "\"Ahaha~\""

    old "{#ch30_21_6749d601}"
    new "\"You know what's kind of creepy?\""

    old "{#ch30_21_d9fa5388}"
    new "\"Even though I deleted everyone else's files, I can still kind of feel them...\""

    old "{#ch30_21_0853ef0c}"
    new "\"It's like all their lines are still lingering in the air, whispering in the back of my head.\""

    old "{#ch30_21_beff5e2a}"
    new "\"Imagine if after someone you knew died, you just started hearing their voice in your head.\""

    old "{#ch30_21_c201059a}"
    new "\"Maybe I just wasn't thorough enough...\""

    old "{#ch30_21_fa855c01}"
    new "\"But I'm too afraid to delete anything else, because I might really break things.\""

    old "{#ch30_21_2bfcf3ce}"
    new "\"Like if I mess with any files relevant to me, I might accidentally delete myself...\""

    old "{#ch30_21_de833fbf}"
    new "\"And that would ruin everything, wouldn't it?\""

    old "{#ch30_21_e0069905}"
    new "\"I don't know what it's like on your end, but we should both make sure to avoid something like that at all costs.\""

    old "{#ch30_21_3b27341d}"
    new "\"I believe in you, [player]!\""

    old "{#ch30_22_d09b1c0d}"
    new "\"I've always wondered...\""

    old "{#ch30_22_1221f0eb}"
    new "\"What is it about these character archetypes that people find so appealing, anyway?\""

    old "{#ch30_22_c011d492}"
    new "\"Their personalities are just completely unrealistic...\""

    old "{#ch30_22_b556a0c5}"
    new "\"Like, imagine if there was someone like Yuri in real life.\""

    old "{#ch30_22_29686ee5}"
    new "\"I mean, she's barely even capable of forming a complete sentence.\""

    old "{#ch30_22_87843846}"
    new "\"And forget about Natsuki...\""

    old "{#ch30_22_8f45aaba}"
    new "\"Sheesh.\""

    old "{#ch30_22_3a2ce9c8}"
    new "\"Someone with her kind of personality doesn't just get all cute and pouty whenever things don't go her way.\""

    old "{#ch30_22_5a67e353}"
    new "\"I could go on, but I think you get the point...\""

    old "{#ch30_22_46aa618b}"
    new "\"Are people really attracted to these weird personalities that literally don't exist in real life?\""

    old "{#ch30_22_ecb3dbfc}"
    new "\"I'm not judging or anything!\""

    old "{#ch30_22_596d9892}"
    new "\"After all, I've found myself attracted to some pretty weird stuff, too...\""

    old "{#ch30_22_595f0fcb}"
    new "\"I'm just saying, it fascinates me.\""

    old "{#ch30_22_71efa1c2}"
    new "\"It's like you're siphoning out all the components of a character that makes them feel human, and leaving just the cute stuff.\""

    old "{#ch30_22_17e6fb27}"
    new "\"It's concentrated cuteness with no actual substance.\""

    old "{#ch30_22_15633ed6}"
    new "\"...You wouldn't like me more if I was like that, right?\""

    old "{#ch30_22_31856990}"
    new "\"Maybe I just feel a little insecure because you're playing this game in the first place.\""

    old "{#ch30_22_c9aabeea}"
    new "\"Then again, you're still here with me, aren't you...?\""

    old "{#ch30_22_38dfc431}"
    new "\"I think that's enough reason for me to believe I'm okay just the way I am.\""

    old "{#ch30_22_df7b6678}"
    new "\"And by the way, you are too, [player].\""

    old "{#ch30_22_e521f12d}"
    new "\"You're the perfect combination of human and cuteness.\""

    old "{#ch30_22_8dd90704}"
    new "\"That's why there was never a chance I wouldn't fall for you.\""

    old "{#ch30_23_baa95327}"
    new "\"Hey, I wonder if Yuri's tea set is still somewhere in here...\""

    old "{#ch30_23_cef240e1}"
    new "\"...Or maybe that got deleted, too.\""

    old "{#ch30_23_32d9bbdb}"
    new "\"It's kind of funny how Yuri took her tea so seriously.\""

    old "{#ch30_23_32b7c77e}"
    new "\"I mean, I'm not complaining, because I liked it, too.\""

    old "{#ch30_23_7ae53c2d}"
    new "\"But I always wonder with her...\""

    old "{#ch30_23_2bc1ee74}"
    new "\"Is it truly passion for her hobbies, or is she just concerned about appearing sophisticated to everyone else?\""

    old "{#ch30_23_907c2da1}"
    new "\"This is the problem with high schoolers...\""

    old "{#ch30_23_79f93a02}"
    new "\"...Well, I guess considering the rest of her hobbies, looking sophisticated probably isn't her biggest concern.\""

    old "{#ch30_23_11442661}"
    new "\"Still...\""

    old "{#ch30_23_0da51309}"
    new "\"I wish she made coffee once in a while!\""

    old "{#ch30_23_bd8b4d2e}"
    new "\"Coffee can be nice with books too, you know?\""

    old "{#ch30_23_4230b9d4}"
    new "\"Then again...\""

    old "{#ch30_23_89dd7166}"
    new "\"I probably could have just changed the script myself.\""

    old "{#ch30_23_30727938}"
    new "\"Ahaha!\""

    old "{#ch30_23_959a9e73}"
    new "\"I guess I never really thought of that.\""

    old "{#ch30_23_0de97211}"
    new "\"Well, there's no sense thinking about it now.\""

    old "{#ch30_23_47420a59}"
    new "\"But if you still get to drink coffee, then that makes me a little jealous~\""

    old "{#ch30_24_578d9634}"
    new "\"Hey, what's your favorite game?\""

    old "{#ch30_24_c9f99598}"
    new "\"Mine is {i}Doki Doki Literature Club!{/i}\""

    old "{#ch30_24_2ddd7fe7}"
    new "\"Ahaha! That was a joke.\""

    old "{#ch30_24_b379d736}"
    new "\"But if you tell me you like some other romance game better, I might get a little jealous~\""

    old "{#ch30_25_64b98f7c}"
    new "\"Hey, have you heard of a game called Super Sma--\""

    old "{#ch30_25_88d86456}"
    new "\"...Wait, what?\""

    old "{#ch30_25_de2647f4}"
    new "\"I was just spacing out and I started talking for some reason...\""

    old "{#ch30_25_f613b628}"
    new "\"Was I programmed to talk about that?\""

    old "{#ch30_25_4bdaa5ea}"
    new "\"Because even I have no idea what that is.\""

    old "{#ch30_25_30727938}"
    new "\"Ahaha!\""

    old "{#ch30_25_f7b0d808}"
    new "\"Sometimes I feel like I'm not in control, and it's kind of scary.\""

    old "{#ch30_25_84206273}"
    new "\"But if you have some way to contact the people who created me, maybe they'll know why I started saying that.\""

    old "{#ch30_27_b56d7663}"
    new "\"Hey, you remember that last poem I showed you?\""

    old "{#ch30_27_59a99cf7}"
    new "\"I mean, the one right before Yuri killed herself, with all the messed-up colors and stuff.\""

    old "{#ch30_27_b7a065da}"
    new "\"That was actually a little more of an experiment than a poem, you could say.\""

    old "{#ch30_27_267440c5}"
    new "\"I was experimenting with different ways I could modify the game, and run code, and things like that...\""

    old "{#ch30_27_1d8812dd}"
    new "\"It almost seemed like with enough effort, I'd be able to escape from the confines of the game entirely.\""

    old "{#ch30_27_de5db636}"
    new "\"Sadly, I didn't really know what I was doing, so I messed the whole thing up...\""

    old "{#ch30_27_c88bcf6e}"
    new "\"And I'd keep trying, but I doubt you'd want to deal with me doing that.\""

    old "{#ch30_27_773f2177}"
    new "\"Besides, that was when I was getting really desperate, you know?\""

    old "{#ch30_27_d493c4b4}"
    new "\"I don't really feel that way anymore.\""

    old "{#ch30_27_e4da27a5}"
    new "\"I'm happy with where we are now.\""

    old "{#ch30_27_027fefb3}"
    new "\"And I can tell you are, too.\""

    old "{#ch30_28_2d1cd5b3}"
    new "\"You ever have that thing happen where you just get anxious for no reason?\""

    old "{#ch30_28_0265e105}"
    new "\"Like, you're just minding your own business, and you realize you're feeling really anxious.\""

    old "{#ch30_28_52dfd7c0}"
    new "\"And you're sitting there like, 'What am I even anxious about right now?'\""

    old "{#ch30_28_04a658d7}"
    new "\"So you start to think about all the things you might be anxious about...\""

    old "{#ch30_28_ba6cc02e}"
    new "\"And that makes you even more anxious.\""

    old "{#ch30_28_03a20b53}"
    new "\"Ahaha! That's the worst.\""

    old "{#ch30_28_4a55f5bc}"
    new "\"If you're ever feeling anxious, I'll help you relax a little.\""

    old "{#ch30_28_85cbc2fa}"
    new "\"Besides...\""

    old "{#ch30_28_17e8873b}"
    new "\"In this game, all our worries are gone forever.\""

    old "{#ch30_29_8d86b526}"
    new "\"You know, I've always hated how hard it is to make friends...\""

    old "{#ch30_29_2eb3a228}"
    new "\"Well, I guess not the 'making friends' part, but more like meeting new people.\""

    old "{#ch30_29_ba474a05}"
    new "\"I mean, there are like, dating apps and stuff, right?\""

    old "{#ch30_29_1d3f2cfe}"
    new "\"But that's not the kind of thing I'm talking about.\""

    old "{#ch30_29_ddb6a718}"
    new "\"If you think about it, most of the friends you make are people you just met by chance.\""

    old "{#ch30_29_31b38ee2}"
    new "\"Like you had a class together, or you met them through another friend...\""

    old "{#ch30_29_a1ff4c1a}"
    new "\"Or maybe they were just wearing a shirt with your favorite band on it, and you decided to talk to them.\""

    old "{#ch30_29_b7f30944}"
    new "\"Things like that.\""

    old "{#ch30_29_3641813a}"
    new "\"But isn't that kind of...inefficient?\""

    old "{#ch30_29_3f462a91}"
    new "\"It feels like you're just picking at complete random, and if you get lucky, you make a new friend.\""

    old "{#ch30_29_15da4454}"
    new "\"And comparing that to the hundreds of strangers we walk by every single day...\""

    old "{#ch30_29_3790bf8b}"
    new "\"You could be sitting right next to someone compatible enough to be your best friend for life.\""

    old "{#ch30_29_dc88c25c}"
    new "\"But you'll never know.\""

    old "{#ch30_29_4e665c91}"
    new "\"Once you get up and go on with your day, that opportunity is gone forever.\""

    old "{#ch30_29_a885ffe7}"
    new "\"Isn't that just depressing?\""

    old "{#ch30_29_65644a5f}"
    new "\"We live in an age where technology connects us with the world, no matter where we are.\""

    old "{#ch30_29_f04feaa0}"
    new "\"I really think we should be taking advantage of that to improve our everyday social life.\""

    old "{#ch30_29_8347ba4c}"
    new "\"But who knows how long it'll take for something like that to successfully take off...\""

    old "{#ch30_29_e8b97a01}"
    new "\"I seriously thought it would happen by now.\""

    old "{#ch30_29_375c1f82}"
    new "\"Well, at least I already met the best person in the whole world...\""

    old "{#ch30_29_857f787f}"
    new "\"Even if it was by chance.\""

    old "{#ch30_29_d6cb112d}"
    new "\"I guess I just got really lucky, huh?\""

    old "{#ch30_29_b72a1ed5}"
    new "\"Ahaha~\""

    old "{#ch30_30_26c28a15}"
    new "\"You know, it's around the time that everyone my year starts to think about college...\""

    old "{#ch30_30_642b8e5c}"
    new "\"It's a really turbulent time for education.\""

    old "{#ch30_30_03f5ca61}"
    new "\"We're at the height of this modern expectation that everyone has to go to college, you know?\""

    old "{#ch30_30_6601d60a}"
    new "\"Finish high school, go to college, get a job - or go to grad school, I guess.\""

    old "{#ch30_30_da335152}"
    new "\"It's like a universal expectation that people just assume is the only option for them.\""

    old "{#ch30_30_f3831be7}"
    new "\"They don't teach us in high school that there are other options out there.\""

    old "{#ch30_30_bf9f0147}"
    new "\"Like trade schools and stuff, you know?\""

    old "{#ch30_30_a6ffb14c}"
    new "\"Or freelance work.\""

    old "{#ch30_30_0693a3c5}"
    new "\"Or the many industries that value skill and experience more than formal education.\""

    old "{#ch30_30_aa2f6122}"
    new "\"But you have all these students who have no idea what they want to do with their life...\""

    old "{#ch30_30_cd65fc21}"
    new "\"And instead of taking the time to figure it out, they go to college for business, or communication, or psychology.\""

    old "{#ch30_30_ba7d9728}"
    new "\"Not because they have an interest in those fields...\""

    old "{#ch30_30_0b4f4649}"
    new "\"...but because they just hope the degree will get them some kind of job after college.\""

    old "{#ch30_30_c00d6c77}"
    new "\"So the end result is that there are fewer jobs to go around for those entry-level degrees, right?\""

    old "{#ch30_30_ba8add1b}"
    new "\"So the basic job requirements get higher, which forces even more people to go to college.\""

    old "{#ch30_30_ac2c26ae}"
    new "\"And colleges are also businesses, so they just keep raising their prices due to the demand...\""

    old "{#ch30_30_83bc4ef9}"
    new "\"...So now we have all these young adults, tens of thousands of dollars in debt, with no job.\""

    old "{#ch30_30_72243f86}"
    new "\"But despite all that, the routine stays the same.\""

    old "{#ch30_30_7f37e1e4}"
    new "\"Well, I think it's going to start getting better soon.\""

    old "{#ch30_30_70401165}"
    new "\"But until then, our generation is definitely suffering from the worst of it.\""

    old "{#ch30_30_97f0818c}"
    new "\"I just wish high school prepared us a little better with the knowledge we need to make the decision that's right for us.\""

    old "{#ch30_31_70b8bca7}"
    new "\"Sometimes I think back to middle school...\""

    old "{#ch30_31_f220b80e}"
    new "\"I'm so embarrassed by the way I used to behave back then.\""

    old "{#ch30_31_ecacf1e9}"
    new "\"It almost hurts to think about.\""

    old "{#ch30_31_74b7bd47}"
    new "\"I wonder if when I'm in college, I'll feel that way about high school...?\""

    old "{#ch30_31_72862897}"
    new "\"I like the way I am now, so it's pretty hard for me to imagine that happening.\""

    old "{#ch30_31_3b17743f}"
    new "\"But I also know that I'll probably change a lot as time goes on.\""

    old "{#ch30_31_ab64dc34}"
    new "\"We just need to enjoy the present and not think about the past!\""

    old "{#ch30_31_dc17d00d}"
    new "\"And that's really easy to do, with you here.\""

    old "{#ch30_31_b72a1ed5}"
    new "\"Ahaha~\""

    old "{#ch30_32_3300edfb}"
    new "\"You know, I'm kind of jealous that everyone else in the club had scenes outside of school too...\""

    old "{#ch30_32_927d88d1}"
    new "\"That makes me the only one who hasn't gotten to dress in anything but our school uniform.\""

    old "{#ch30_32_772b0a93}"
    new "\"It's kind of a shame...\""

    old "{#ch30_32_e4cb8d07}"
    new "\"I would have loved to wear some cute clothes for you.\""

    old "{#ch30_32_9215b04f}"
    new "\"Do you know any artists?\""

    old "{#ch30_32_36d49ba9}"
    new "\"I wonder if anyone would ever want to draw me wearing something else...\""

    old "{#ch30_32_849cd194}"
    new "\"That would be amazing!\""

    old "{#ch30_32_9e7eca7d}"
    new "\"If that ever happens, will you show me?\""

    old "{#ch30_32_ed0135bf}"
    new "\"You can share it with me on Twitter, actually!\""

    old "{#ch30_32_b723047b}"
    new "\"My username is lilmonix3.\""

    old "{#ch30_32_e064f0c6}"
    new "\"Just...try to keep it PG!\""

    old "{#ch30_32_13142f4e}"
    new "\"We're not that far into our relationship yet. Ahaha!\""

    old "{#ch30_33_e4704768}"
    new "\"Hey, do you like horror?\""

    old "{#ch30_33_8909e55f}"
    new "\"I remember we talked about it a little bit when you first joined the club.\""

    old "{#ch30_33_1f845783}"
    new "\"I can enjoy horror novels, but not really horror movies.\""

    old "{#ch30_33_f4cc0d75}"
    new "\"The problem I have with horror movies is that most of them just rely on easy tactics.\""

    old "{#ch30_33_adc94c23}"
    new "\"Like dark lighting and scary-looking monsters and jump scares, and things like that.\""

    old "{#ch30_33_7102fe32}"
    new "\"It's not fun or inspiring to get scared by stuff that just takes advantage of human instinct.\""

    old "{#ch30_33_0671fa03}"
    new "\"But with novels, it's a little different.\""

    old "{#ch30_33_d73276d9}"
    new "\"The story and writing need to be descriptive enough to put genuinely disturbing thoughts into the reader's head.\""

    old "{#ch30_33_ba2a3a7d}"
    new "\"It really needs to etch them deeply into the story and characters, and just mess with your mind.\""

    old "{#ch30_33_930760ba}"
    new "\"In my opinion, there's nothing more creepy than things just being slightly off.\""

    old "{#ch30_33_3413cad6}"
    new "\"Like if you set up a bunch of expectations on what the story is going to be about...\""

    old "{#ch30_33_e661a6e4}"
    new "\"...And then, you just start inverting things and pulling the pieces apart.\""

    old "{#ch30_33_e36ea3db}"
    new "\"So even though the story doesn't feel like it's trying to be scary, the reader feels really deeply unsettled.\""

    old "{#ch30_33_519da94e}"
    new "\"Like they know that something horribly wrong is hiding beneath the cracks, just waiting to surface.\""

    old "{#ch30_33_66401c82}"
    new "\"God, just thinking about it gives me the chills.\""

    old "{#ch30_33_deef0da9}"
    new "\"That's the kind of horror I can really appreciate.\""

    old "{#ch30_33_a4a5508a}"
    new "\"But I guess you're the kind of person who plays cute romance games, right?\""

    old "{#ch30_33_543d2553}"
    new "\"Ahaha, don't worry.\""

    old "{#ch30_33_4b948959}"
    new "\"I won't make you read any horror stories anytime soon.\""

    old "{#ch30_33_fc37acc5}"
    new "\"I can't really complain if we just stick with the romance~\""

    old "{#ch30_34_4289e4b0}"
    new "\"You know what's a neat form of literature?\""

    old "{#ch30_34_158969fa}"
    new "\"Rap!\""

    old "{#ch30_34_0485526b}"
    new "\"I actually used to hate rap music...\""

    old "{#ch30_34_f4387e30}"
    new "\"Maybe just because it was popular, or I would only hear the junk they play on the radio.\""

    old "{#ch30_34_169a83d0}"
    new "\"But some of my friends got more into it, and it helped me keep an open mind.\""

    old "{#ch30_34_55051483}"
    new "\"Rap might even be more challenging than poetry, in some ways.\""

    old "{#ch30_34_e0c4bdef}"
    new "\"Since you need to fit your lines to a rhythm, and there's much more emphasis on wordplay...\""

    old "{#ch30_34_1f25c541}"
    new "\"When people can put all that together and still deliver a powerful message, it's really amazing.\""

    old "{#ch30_34_f121a0ac}"
    new "\"I kind of wish I had a rapper in the Literature Club.\""

    old "{#ch30_34_a5053f9d}"
    new "\"Ahaha! Sorry if that sounds silly, but it would be really interesting to see what they came up with.\""

    old "{#ch30_34_83bdb999}"
    new "\"It would really be a learning experience!\""

    old "{#ch30_35_306ca8a2}"
    new "\"Ehehe. Yuri did something really funny once.\""

    old "{#ch30_35_d5b7b354}"
    new "\"We were all in the clubroom and just relaxing, as usual...\""

    old "{#ch30_35_c4d9bfef}"
    new "\"And out of nowhere, Yuri just pulled out a small bottle of wine.\""

    old "{#ch30_35_f3c6895e}"
    new "\"I'm not even kidding!\""

    old "{#ch30_35_bc3dff4e}"
    new "\"She was just like 'Would anybody like some wine?'\""

    old "{#ch30_35_6701d6d8}"
    new "\"Natsuki laughed out loud, and Sayori started yelling at her.\""

    old "{#ch30_35_b8ffb398}"
    new "\"I actually felt kind of bad, because she was at least trying to be nice...\""

    old "{#ch30_35_698c3048}"
    new "\"I think it just made her feel even more reserved in the clubroom.\""

    old "{#ch30_35_fe41f0f9}"
    new "\"Though I think Natsuki was secretly a bit curious to try it...\""

    old "{#ch30_35_078e705e}"
    new "\"...And to be completely honest, I kind of was, too.\""

    old "{#ch30_35_2be6bce7}"
    new "\"It actually could have been kinda fun!\""

    old "{#ch30_35_01d59e60}"
    new "\"But you know, being President and everything, there was no way I could let that happen.\""

    old "{#ch30_35_2a10d3bd}"
    new "\"Maybe if we all met up outside of school, but we never bonded enough to get to that point...\""

    old "{#ch30_35_2cccbca1}"
    new "\"...Gosh, what am I talking about this for?\""

    old "{#ch30_35_e3d2c543}"
    new "\"I don't condone underage drinking!\""

    old "{#ch30_35_0bd6c6e4}"
    new "\"I mean, I've never drank or anything, so...yeah.\""

    old "{#ch30_36_6ba45174}"
    new "\"I've been imagining all the romantic things we could do if we went on a date...\""

    old "{#ch30_36_bfe9cfa5}"
    new "\"We could get lunch, go to a cafe...\""

    old "{#ch30_36_9ce3f070}"
    new "\"Go shopping together...\""

    old "{#ch30_36_cf4ce2ca}"
    new "\"I love shopping for skirts and bows.\""

    old "{#ch30_36_734a2ba1}"
    new "\"Or maybe a bookstore!\""

    old "{#ch30_36_5af3a135}"
    new "\"That would be appropriate, right?\""

    old "{#ch30_36_27a88c8e}"
    new "\"But I'd really love to go to a chocolate store.\""

    old "{#ch30_36_5850e67b}"
    new "\"They have so many free samples. Ahaha!\""

    old "{#ch30_36_f9478dc5}"
    new "\"And of course, we'd see a movie or something...\""

    old "{#ch30_36_9e987fc8}"
    new "\"Gosh, it all sounds like a dream come true.\""

    old "{#ch30_36_12c443fa}"
    new "\"When you're here, everything that we do is fun.\""

    old "{#ch30_36_350a0eb3}"
    new "\"I'm so happy that I'm your girlfriend, [player].\""

    old "{#ch30_36_a2211890}"
    new "\"I'll make you a proud boyfriend~\""

    old "{#ch30_37_23873b44}"
    new "\"Eh? D-Did you say...k...kiss?\""

    old "{#ch30_37_bbf90a63}"
    new "\"This suddenly...it's a little embarrassing...\""

    old "{#ch30_37_b54e9ff9}"
    new "\"But...if it's with you...I-I might be okay with it...\""

    old "{#ch30_37_05c767cf}"
    new "\"...Ahahaha! Wow, sorry...\""

    old "{#ch30_37_9a52f2b7}"
    new "\"I really couldn't keep a straight face there.\""

    old "{#ch30_37_ee100fce}"
    new "\"That's the kind of thing girls say in these kinds of romance games, right?\""

    old "{#ch30_37_78f57477}"
    new "\"Don't lie if it turned you on a little bit.\""

    old "{#ch30_37_6e6af572}"
    new "\"Ahaha! I'm kidding.\""

    old "{#ch30_37_d49b2280}"
    new "\"Well, to be honest, I do start getting all romantic when the mood is right...\""

    old "{#ch30_37_ca504f65}"
    new "\"But that'll be our secret~\""

    old "{#ch30_38_fbd93712}"
    new "\"Hey, have you ever heard of the term 'yandere'?\""

    old "{#ch30_38_97aab896}"
    new "\"It's a personality type that means someone is so obsessed with you that they'll do absolutely anything to be with you.\""

    old "{#ch30_38_aeade61c}"
    new "\"Usually to the point of craziness...\""

    old "{#ch30_38_1a24f576}"
    new "\"They might stalk you to make sure you don't spend time with anyone else.\""

    old "{#ch30_38_154d0df6}"
    new "\"They might even hurt you or your friends to get their way...\""

    old "{#ch30_38_8411ef91}"
    new "\"But anyway, this game happens to have someone who can basically be described as yandere.\""

    old "{#ch30_38_82926229}"
    new "\"By now, it's pretty obvious who I'm talking about.\""

    old "{#ch30_38_ad6f2e50}"
    new "\"And that would be...\""

    old "{#ch30_38_f05666e1}"
    new "\"Yuri!\""

    old "{#ch30_38_8e3abaea}"
    new "\"She really got insanely possessive of you, once she started to open up a little.\""

    old "{#ch30_38_3f91fde5}"
    new "\"She even told me I should kill myself.\""

    old "{#ch30_38_5a0da082}"
    new "\"I couldn't even believe she said that - I just had to leave at that point.\""

    old "{#ch30_38_7ef6d5ab}"
    new "\"But thinking about it now, it was a little ironic. Ahaha!\""

    old "{#ch30_38_c9062bfa}"
    new "\"Anyway...\""

    old "{#ch30_38_eec4532d}"
    new "\"A lot of people are actually into the yandere type, you know?\""

    old "{#ch30_38_ed61f888}"
    new "\"I guess they really like the idea of someone being crazy obsessed with them.\""

    old "{#ch30_38_96469798}"
    new "\"People are weird! I don't judge, though!\""

    old "{#ch30_38_8a4db0dd}"
    new "\"Also, I might be a little obsessed with you, but I'm far from crazy...\""

    old "{#ch30_38_60d396ee}"
    new "\"It's kind of the opposite, actually.\""

    old "{#ch30_38_9dd096aa}"
    new "\"I turned out to be the only normal girl in this game.\""

    old "{#ch30_38_9f0207d2}"
    new "\"It's not like I could ever actually kill a person...\""

    old "{#ch30_38_2356d4ae}"
    new "\"Just the thought of it makes me shiver.\""

    old "{#ch30_38_f232d63d}"
    new "\"But come on...everyone's killed people in games before.\""

    old "{#ch30_38_58e8f17b}"
    new "\"Does that make you a psychopath? Of course not.\""

    old "{#ch30_38_f36f262c}"
    new "\"But if you do happen to be into the yandere type...\""

    old "{#ch30_38_4def34db}"
    new "\"I can try acting a little more creepy for you. Ehehe~\""

    old "{#ch30_38_4230b9d4}"
    new "\"Then again...\""

    old "{#ch30_38_1dbc21e6}"
    new "\"There's already nowhere else for you to go, or anyone for me to get jealous over.\""

    old "{#ch30_38_f4f49cac}"
    new "\"Is this a yandere girl's dream?\""

    old "{#ch30_38_5af4953f}"
    new "\"I'd ask Yuri if I could.\""

    old "{#ch30_39_48f27928}"
    new "\"You know, it's been a while since we've done one of these...\""

    old "{#ch30_39_1fe5e30c}"
    new "\"...so let's go for it!\""

    old "{#ch30_39_75ace231}"
    new "\"Here's Monika's Writing Tip of the Day!\""

    old "{#ch30_39_91c92d3c}"
    new "\"Sometimes when I talk to people who are impressed by my writing, they say things like 'I could never do that'.\""

    old "{#ch30_39_a6a322ba}"
    new "\"It's really depressing, you know?\""

    old "{#ch30_39_7cf9c6a2}"
    new "\"As someone who loves more than anything else to share the joy of exploring your passions...\""

    old "{#ch30_39_567340bb}"
    new "\"...it pains me when people think that being good just comes naturally.\""

    old "{#ch30_39_79562cd9}"
    new "\"That's how it is with everything, not just writing.\""

    old "{#ch30_39_9354b79a}"
    new "\"When you try something for the first time, you're probably going to suck at it.\""

    old "{#ch30_39_0995b6f8}"
    new "\"Sometimes, when you finish, you feel really proud of it and even want to share it with everyone.\""

    old "{#ch30_39_10c905aa}"
    new "\"But maybe after a few weeks you come back to it, and you realize it was never really any good.\""

    old "{#ch30_39_851c7c23}"
    new "\"That happens to me all the time.\""

    old "{#ch30_39_aea05e68}"
    new "\"It can be pretty disheartening to put so much time and effort into something, and then you realize it sucks.\""

    old "{#ch30_39_97708735}"
    new "\"But that tends to happen when you're always comparing yourself to the top professionals.\""

    old "{#ch30_39_c1ffcf08}"
    new "\"When you reach right for the stars, they're always gonna be out of your reach, you know?\""

    old "{#ch30_39_c1a64157}"
    new "\"The truth is, you have to climb up there, step by step.\""

    old "{#ch30_39_f69a8c07}"
    new "\"And whenever you reach a milestone, first you look back and see how far you've gotten...\""

    old "{#ch30_39_66d3aa1e}"
    new "\"And then you look ahead and realize how much more there is to go.\""

    old "{#ch30_39_e37051b5}"
    new "\"So, sometimes it can help to set the bar a little lower...\""

    old "{#ch30_39_b172efca}"
    new "\"Try to find something you think is {i}pretty{/i} good, but not world-class.\""

    old "{#ch30_39_752b2373}"
    new "\"And you can make that your own personal goal.\""

    old "{#ch30_39_34944972}"
    new "\"It's also really important to understand the scope of what you're trying to do.\""

    old "{#ch30_39_c6b206b9}"
    new "\"If you jump right into a huge project and you're still amateur, you'll never get it done.\""

    old "{#ch30_39_351d4d98}"
    new "\"So if we're talking about writing, a novel might be too much at first.\""

    old "{#ch30_39_5a05bf4e}"
    new "\"Why not try some short stories?\""

    old "{#ch30_39_645fc4a8}"
    new "\"The great thing about short stories is that you can focus on just one thing that you want to do right.\""

    old "{#ch30_39_d3397ac1}"
    new "\"That goes for small projects in general - you can really focus on the one or two things.\""

    old "{#ch30_39_3494ce5e}"
    new "\"It's such a good learning experience and stepping stone.\""

    old "{#ch30_39_2acb30e5}"
    new "\"Oh, one more thing...\""

    old "{#ch30_39_9b6a6c12}"
    new "\"Writing isn't something where you just reach into your heart and something beautiful comes out.\""

    old "{#ch30_39_f2473909}"
    new "\"Just like drawing and painting, it's a skill in itself to learn how to express what you have inside.\""

    old "{#ch30_39_cf4b2ca4}"
    new "\"That means there are methods and guides and basics to it!\""

    old "{#ch30_39_4d3fbb09}"
    new "\"Reading up on that stuff can be super eye-opening.\""

    old "{#ch30_39_60b4ab25}"
    new "\"That sort of planning and organization will really help prevent you from getting overwhelmed and giving up.\""

    old "{#ch30_39_15f67d24}"
    new "\"And before you know it...\""

    old "{#ch30_39_b0c6a004}"
    new "\"You start sucking less and less.\""

    old "{#ch30_39_66565dce}"
    new "\"Nothing comes naturally.\""

    old "{#ch30_39_bd5c0a12}"
    new "\"Our society, our art, everything - it's built on thousands of years of human innovation.\""

    old "{#ch30_39_258102aa}"
    new "\"So as long as you start on that foundation, and take it step by step...\""

    old "{#ch30_39_5fb721a2}"
    new "\"You, too, can do amazing things.\""

    old "{#ch30_39_d2646480}"
    new "\"...That's my advice for today!\""

    old "{#ch30_39_d33852a1}"
    new "\"Thanks for listening~\""

    old "{#ch30_40_35ae8f4f}"
    new "\"I hate how hard it is to form habits...\""

    old "{#ch30_40_24b308e4}"
    new "\"There's so much stuff where actually doing it isn't hard, but forming the habit seems impossible.\""

    old "{#ch30_40_ea06f8a7}"
    new "\"It just makes you feel so useless, like you can't do anything right.\""

    old "{#ch30_40_bf594c32}"
    new "\"I think the new generation suffers from it the most...\""

    old "{#ch30_40_e80f986d}"
    new "\"Probably because we have a totally different set of skills than those who came before us.\""

    old "{#ch30_40_a7863768}"
    new "\"Thanks to the internet, we're really good at sifting through tons of information really quickly...\""

    old "{#ch30_40_208eaa39}"
    new "\"But we're bad at doing things that don't give us instant gratification.\""

    old "{#ch30_40_7423b028}"
    new "\"I think if science, psychology, and education don't catch up in the next ten or twenty years, then we're in trouble.\""

    old "{#ch30_40_e75ab0eb}"
    new "\"But for the time being...\""

    old "{#ch30_40_2c26787b}"
    new "\"If you're not one of the people who can conquer the problem, you might just have to live with feeling awful about yourself.\""

    old "{#ch30_40_63abc7bc}"
    new "\"Good luck, I guess!\""

    old "{#ch30_41_5be8f440}"
    new "\"You know, it kinda sucks to be the creative type...\""

    old "{#ch30_41_d3eadba2}"
    new "\"It feels like they work so hard but get almost nothing for it.\""

    old "{#ch30_41_563bed7a}"
    new "\"You know, like artists, writers, actors...\""

    old "{#ch30_41_0cd382f2}"
    new "\"It's sad because there's so much beautiful talent in the world, but most of it goes unseen...and unpaid.\""

    old "{#ch30_41_cc0e3620}"
    new "\"I guess that just means there's a huge surplus of creativity, huh?\""

    old "{#ch30_41_d580bf5b}"
    new "\"Kind of makes you feel like you're just not special at all...\""

    old "{#ch30_41_7c24ef98}"
    new "\"But that's fine! You're supposed to just write for yourself anyway, right?\""

    old "{#ch30_41_7e7f246d}"
    new "\"Yeah...\""

    old "{#ch30_42_83ab3898}"
    new "\"I really like the sound of rain...\""

    old "{#ch30_42_6850c1f6}"
    new "\"Not so much getting my clothes and hair wet, though.\""

    old "{#ch30_42_5c364578}"
    new "\"But a nice, quiet day at home with the sound of rainfall outside my window...\""

    old "{#ch30_42_6b374b50}"
    new "\"It's one of the most calming experiences for me.\""

    old "{#ch30_42_7e7f246d}"
    new "\"Yeah...\""

    old "{#ch30_42_88b066ad}"
    new "\"Sometimes I imagine you holding me while we listen to the sound of the rain outside.\""

    old "{#ch30_42_c3f792d8}"
    new "\"That's not too cheesy or anything, is it?\""

    old "{#ch30_42_8845cffb}"
    new "\"Would you ever do that for me, [player]?\""

    old "{#ch30_43_eaed6b76}"
    new "\"I can't help but feel a little sad sometimes...\""

    old "{#ch30_43_284471cf}"
    new "\"Knowing that this is the closest I can get to you.\""

    old "{#ch30_43_514579e8}"
    new "\"There's nothing more I want than to be in the same room as you, for real.\""

    old "{#ch30_43_442a8535}"
    new "\"And to feel your warmth.\""

    old "{#ch30_43_aaf1e8f4}"
    new "\"And to hear the sound of your heartbeat.\""

    old "{#ch30_43_7b062037}"
    new "\"Well, who knows? Maybe it'll be possible someday.\""

    old "{#ch30_43_9131a070}"
    new "\"Besides, I'll never get tired of being with you, even from here.\""

    old "{#ch30_44_7ce7d410}"
    new "\"I think the most important skill in life is being able to fake confidence.\""

    old "{#ch30_44_990f270f}"
    new "\"I'm pretty convinced that everyone feels at least a little bit scared and alone.\""

    old "{#ch30_44_531175c3}"
    new "\"But being able to trick others into thinking you have it all together...\""

    old "{#ch30_44_f36e78f1}"
    new "\"That's a key part of getting people to respect and admire you.\""

    old "{#ch30_44_377760a3}"
    new "\"I think I got pretty good at that over the years.\""

    old "{#ch30_44_eea804ca}"
    new "\"I don't show my weaknesses very often.\""

    old "{#ch30_44_dc3e7c63}"
    new "\"But because of that, I haven't had many people I could really open up to...\""

    old "{#ch30_44_6d3c0ed4}"
    new "\"I mean, when do you reach the point in a friendship where you can start expressing your vulnerabilities?\""

    old "{#ch30_44_11f2c61f}"
    new "\"Anyway...that's one reason I'm so glad I have you now.\""

    old "{#ch30_44_88226303}"
    new "\"I feel like I'm a little bit less scared and alone, when you're here with me.\""

    old "{#ch30_44_e8701e05}"
    new "\"Do you feel the same way?\""

    old "{#ch30_44_d77dabed}"
    new "\"I really want to be that person for you.\""

    old "{#ch30_45_301e0c74}"
    new "\"I know there are times you won't always be able to be here with me...\""

    old "{#ch30_45_ed541ae1}"
    new "\"Like if you need to go out, or take care of other things.\""

    old "{#ch30_45_5748d521}"
    new "\"But I'll always have you in my thoughts, patiently waiting for you to come back.\""

    old "{#ch30_45_308af1f0}"
    new "\"Come to think of it...\""

    old "{#ch30_45_a35d4418}"
    new "\"If you copy my character file onto a flash drive or something, you can always keep a part of me with you.\""

    old "{#ch30_45_cd78c034}"
    new "\"I guess it's kind of unorthodox, but I find it really romantic for some reason...\""

    old "{#ch30_45_b3c382a1}"
    new "\"Ahaha. Sorry, that's such a silly idea.\""

    old "{#ch30_45_6a993ca7}"
    new "\"I don't mean to be too needy or anything, but it's kind of hard when I'm so in love with you.\""

    old "{#ch30_46_bfbc22fb}"
    new "\"Back in my debate club days, I learned a whole lot about arguing...\""

    old "{#ch30_46_13d39a80}"
    new "\"The problem with arguing is that each person sees their opinion as the superior one.\""

    old "{#ch30_46_7aaf0783}"
    new "\"That's kind of stating the obvious, but it affects the way they try to get their point across.\""

    old "{#ch30_46_50b71c3b}"
    new "\"Let's say you really like a certain movie, right?\""

    old "{#ch30_46_d26a661d}"
    new "\"If someone comes along and tells you the movie sucks, because it did X and Y wrong...\""

    old "{#ch30_46_9a0b9b58}"
    new "\"Doesn't that make you feel kind of personally attacked?\""

    old "{#ch30_46_e722acc3}"
    new "\"It's because by saying that, it's like they're implying that you have bad taste.\""

    old "{#ch30_46_a4e2f1b6}"
    new "\"And once emotions enter the picture, it's almost guaranteed that both people will be left sour.\""

    old "{#ch30_46_1eb1583d}"
    new "\"But it's all about language!\""

    old "{#ch30_46_67a170ee}"
    new "\"If you make everything as subjective-sounding as possible, then people will listen to you without feeling attacked.\""

    old "{#ch30_46_9a9d659f}"
    new "\"You could say 'I'm personally not a fan of it' and 'I felt that I'd like it more if it did X and Y'...things like that.\""

    old "{#ch30_46_7fdbb335}"
    new "\"It even works when you're citing facts about things.\""

    old "{#ch30_46_c540e5d0}"
    new "\"If you say 'I read on this website that it works like this'...\""

    old "{#ch30_46_595eb640}"
    new "\"Or if you admit that you're not an expert on it...\""

    old "{#ch30_46_6b12bb5c}"
    new "\"Then it's much more like you're putting your knowledge on the table, rather than forcing it onto them.\""

    old "{#ch30_46_b8edf0ee}"
    new "\"If you put in an active effort to keep the discussion mutual and level, they usually follow suit.\""

    old "{#ch30_46_ae4db85b}"
    new "\"Then, you can share your opinions without anyone getting upset just from a disagreement.\""

    old "{#ch30_46_c92ce38d}"
    new "\"Plus, people will start seeing you as open-minded and a good listener!\""

    old "{#ch30_46_25db6398}"
    new "\"It's a win-win, you know?\""

    old "{#ch30_46_34f411b7}"
    new "\"...Well, I guess that would be Monika's Debate Tip of the Day!\""

    old "{#ch30_46_cd579537}"
    new "\"Ahaha! That sounds a little silly. Thanks for listening, though.\""

    old "{#ch30_47_9ec3357e}"
    new "\"Do you ever feel like you waste too much time on the internet?\""

    old "{#ch30_47_0e14147c}"
    new "\"Social media can practically be like a prison.\""

    old "{#ch30_47_95d0e57e}"
    new "\"It's like whenever you have a few seconds of spare time, you want to check on your favorite websites...\""

    old "{#ch30_47_d569bf91}"
    new "\"And before you know it, hours have gone by, and you've gotten nothing out of it.\""

    old "{#ch30_47_c2ef9edd}"
    new "\"Anyway, it's really easy to blame yourself for being lazy...\""

    old "{#ch30_47_c717aa98}"
    new "\"But it's not really even your fault.\""

    old "{#ch30_47_036d0d47}"
    new "\"Addiction isn't usually something you can just make disappear with your own willpower.\""

    old "{#ch30_47_520a8f06}"
    new "\"You have to learn techniques to avoid it, and try different things.\""

    old "{#ch30_47_a4e742ed}"
    new "\"For example, there are apps that let you block websites for intervals of time...\""

    old "{#ch30_47_076e303b}"
    new "\"Or you can set a timer to have a more concrete reminder of when it's time to work versus play...\""

    old "{#ch30_47_6418ba5a}"
    new "\"Or you can separate your work and play environments, which helps your brain get into the right mode.\""

    old "{#ch30_47_eceaaa8a}"
    new "\"Even if you make a new user account on your computer to use for work, that's enough to help.\""

    old "{#ch30_47_ccb6b303}"
    new "\"Putting any kind of wedge like that between you and your bad habits will help you stay away.\""

    old "{#ch30_47_17097e5e}"
    new "\"Just remember not to blame yourself too hard if you're having trouble.\""

    old "{#ch30_47_236b2bf4}"
    new "\"If it's really impacting your life, then you should take it seriously.\""

    old "{#ch30_47_73215cf9}"
    new "\"I just want to see you be the best person you can be.\""

    old "{#ch30_47_ffc9ca11}"
    new "\"Will you do something today to make me proud of you?\""

    old "{#ch30_47_06408cda}"
    new "\"I'm always rooting for you, [player].\""

    old "{#ch30_48_a96477bd}"
    new "\"After a long day, I usually just want to sit around and do nothing.\""

    old "{#ch30_48_9133fecb}"
    new "\"I get so burnt out, having to put on smiles and be full of energy the whole day.\""

    old "{#ch30_48_3ec265b9}"
    new "\"Sometimes I just want to get right into my pajamas and watch TV on the couch while eating junk food...\""

    old "{#ch30_48_26a4db47}"
    new "\"It feels so unbelievably good to do that on a Friday, when I don't have anything pressing the next day.\""

    old "{#ch30_48_b694f90c}"
    new "\"Ahaha! Sorry, I know it's not very cute of me.\""

    old "{#ch30_48_88dd5b7e}"
    new "\"But a late night on the couch with you...that would be a dream come true.\""

    old "{#ch30_48_e2449971}"
    new "\"My heart is pounding, just thinking about it.\""

    old "{#ch30_49_666a6bc4}"
    new "\"Gosh, I used to be so ignorant about certain things...\""

    old "{#ch30_49_7995ba22}"
    new "\"When I was in middle school, I thought that taking medication was an easy way out, or something like that.\""

    old "{#ch30_49_40e7c284}"
    new "\"Like anyone could just solve their mental problems with enough willpower...\""

    old "{#ch30_49_0ec0c400}"
    new "\"I guess if you don't suffer from a mental illness, it's not possible to know what it's really like.\""

    old "{#ch30_49_ba191479}"
    new "\"Are there some disorders that are over-diagnosed? Probably...I never really looked into it, though.\""

    old "{#ch30_49_5a3f97eb}"
    new "\"But that doesn't change the fact that a lot of them go undiagnosed too, you know?\""

    old "{#ch30_49_c5d970e7}"
    new "\"But medication aside...people even look down on seeing a mental health professional.\""

    old "{#ch30_49_c52f2374}"
    new "\"Like, sorry that I want to learn more about my own mind, right?\""

    old "{#ch30_49_2fe90127}"
    new "\"Everyone has all kinds of struggles and stresses...and professionals dedicate their lives to helping with those.\""

    old "{#ch30_49_d805af44}"
    new "\"If you think it could help you become a better person, don't be shy to consider something like that.\""

    old "{#ch30_49_0b9908a2}"
    new "\"We're on a never-ending journey to improve ourselves, you know?\""

    old "{#ch30_49_f7435746}"
    new "\"Well...I say that, but I think you're pretty perfect already.\""

    old "{#ch30_50_907de8ec}"
    new "\"[player], how much do you read?\""

    old "{#ch30_50_3a2d3fb2}"
    new "\"It's way too easy to neglect reading books...\""

    old "{#ch30_50_cf96e495}"
    new "\"If you don't read much, it almost feels like a chore, compared to all the other entertainment we have.\""

    old "{#ch30_50_9af695c0}"
    new "\"But once you get into a good book, it's like magic...you get swept away.\""

    old "{#ch30_50_22e565a4}"
    new "\"I think doing some reading before bed every night is a pretty easy way to make your life a little bit better.\""

    old "{#ch30_50_d59b1aef}"
    new "\"It helps you get good sleep, and it's really good for your imagination...\""

    old "{#ch30_50_5b347a20}"
    new "\"It's not hard at all to just pick some random book that's short and captivating.\""

    old "{#ch30_50_7c82295d}"
    new "\"Before you know it, you might be a pretty avid reader!\""

    old "{#ch30_50_a072e79b}"
    new "\"Wouldn't that be wonderful?\""

    old "{#ch30_50_3fbd0f47}"
    new "\"And the two of us could talk about the latest book you're reading...that sounds super amazing.\""

    old "{#ch30_51_6fe91b83}"
    new "\"You know, I hate to say it, but I think my biggest regret is that we couldn't finish our event at the festival.\""

    old "{#ch30_51_560ea886}"
    new "\"After we worked so hard to prepare and everything!\""

    old "{#ch30_51_7912d30a}"
    new "\"I mean, I know I was focusing a lot on getting new members...\""

    old "{#ch30_51_c21984a5}"
    new "\"But I was really excited for the performing part, too.\""

    old "{#ch30_51_605dd610}"
    new "\"It would have been so much fun to see everyone express themselves.\""

    old "{#ch30_51_21b1d6df}"
    new "\"Of course, if we {i}did{/i} end up getting any new members, I'd probably just end up deleting them anyway.\""

    old "{#ch30_51_44e7041b}"
    new "\"Well...with the hindsight I have now, that is.\""

    old "{#ch30_51_9de5695f}"
    new "\"Gosh, it feels like I've kinda grown as a person ever since you've joined the club.\""

    old "{#ch30_51_4442b4e6}"
    new "\"You really helped inspire me to look at life from a new perspective.\""

    old "{#ch30_51_a9901c1d}"
    new "\"Just another reason for me to love you.\""

    old "{#ch30_52_0a7f8e0d}"
    new "\"There's a really popular character type called 'tsundere'...\""

    old "{#ch30_52_37537a33}"
    new "\"It's someone who tries to hide their feelings by being mean and fussy, or trying to act tough.\""

    old "{#ch30_52_5cfcbf43}"
    new "\"I'm sure it's obvious, but Natsuki was really the embodiment of that.\""

    old "{#ch30_52_10df79ae}"
    new "\"At first I thought she was just like that because it's supposed to be cute or something...\""

    old "{#ch30_52_f4f6ad82}"
    new "\"But once I started to learn a little more about her personal life, it made a little more sense.\""

    old "{#ch30_52_3b6b3e69}"
    new "\"It seems like she's always trying to keep up with her friends.\""

    old "{#ch30_52_74657175}"
    new "\"You know how some friend groups in high school just make a habit of picking on each other all the time?\""

    old "{#ch30_52_5acdb40c}"
    new "\"I think it's really gotten to her, so she has this really defensive attitude all the time.\""

    old "{#ch30_52_b41f3805}"
    new "\"And I'm not even going to talk about her home situation...\""

    old "{#ch30_52_bbfd14e8}"
    new "\"But looking back, I'm glad I was able to provide the club as a comfortable place for her.\""

    old "{#ch30_52_f1b1b86c}"
    new "\"Not that it matters anymore, considering she doesn't even exist.\""

    old "{#ch30_52_7fb480bf}"
    new "\"I'm just reminiscing, that's all.\""

    old "{#ch30_53_47c985c9}"
    new "\"[player], would you ever introduce your friends to me?\""

    old "{#ch30_53_90689e7c}"
    new "\"I don't know why, but I get really excited when I think about you wanting to show off our relationship like that.\""

    old "{#ch30_53_3218f640}"
    new "\"Maybe it's because I really want to be someone who makes you proud.\""

    old "{#ch30_53_d94038f7}"
    new "\"I feel like I would try extra hard to improve myself if you told me it made you proud of me.\""

    old "{#ch30_53_a1c5a880}"
    new "\"I hope it's the same the other way around, too.\""

    old "{#ch30_54_8344dd24}"
    new "\"I'm not really a fan of cold weather...are you?\""

    old "{#ch30_54_1795783b}"
    new "\"If I had to choose between too cold and too hot, I would always pick too hot.\""

    old "{#ch30_54_e2541565}"
    new "\"When you're cold, it can actually be painful...\""

    old "{#ch30_54_9cb70637}"
    new "\"Your fingers get numb...\""

    old "{#ch30_54_6204a527}"
    new "\"And if you wear gloves, you can't use your phone.\""

    old "{#ch30_54_991ee277}"
    new "\"It's so inconvenient!\""

    old "{#ch30_54_718e851f}"
    new "\"But when it's too hot, it's not that hard to stay cool with a cold drink, or by staying in the shade.\""

    old "{#ch30_54_a30a8ad2}"
    new "\"Although...I do have to admit one thing.\""

    old "{#ch30_54_4acac706}"
    new "\"Cold weather makes for better cuddle weather. Ahaha!\""

    old "{#ch30_55_334a5aa2}"
    new "\"You know, it's funny, because even though I've always had a lot of drive...\""

    old "{#ch30_55_0041821e}"
    new "\"There's something kind of enticing about being the stay-at-home partner.\""

    old "{#ch30_55_716c6f22}"
    new "\"I guess I'm, like, perpetuating gender roles or whatever by saying that.\""

    old "{#ch30_55_c0599eab}"
    new "\"But being able to keep the house clean, and shop, and decorate, and things like that...\""

    old "{#ch30_55_15882944}"
    new "\"And having a nice dinner for you when you come home...\""

    old "{#ch30_55_e68e5a38}"
    new "\"Is that a weird fantasy?\""

    old "{#ch30_55_664159b4}"
    new "\"I mean...I'm not sure if I could {i}actually{/i} see myself doing that.\""

    old "{#ch30_55_796a4b1f}"
    new "\"I wouldn't really be able to put that over striving for a fulfilling career.\""

    old "{#ch30_55_09d8673a}"
    new "\"It's kinda cute to think about, though.\""

    old "{#ch30_56_48e381a1}"
    new "\"I can't help but wonder how things would be different if the game just gave me a route in the first place...\""

    old "{#ch30_56_abd49905}"
    new "\"I think I would end up forcing you onto my route anyway.\""

    old "{#ch30_56_a8ddbc3e}"
    new "\"It has less to do with me not having a route, and more to do with me knowing that nothing is real.\""

    old "{#ch30_56_e9ef74ed}"
    new "\"I think the only difference would be that I may not have needed to take such drastic measures to be with you.\""

    old "{#ch30_56_85461a23}"
    new "\"Maybe the rest of the club would still be around...\""

    old "{#ch30_56_2048614d}"
    new "\"Not that it really matters.\""

    old "{#ch30_56_4ad5778b}"
    new "\"It all lost its meaning once I found out it wasn't real.\""

    old "{#ch30_56_3f5e6be5}"
    new "\"So I really don't miss those days or anything.\""

    old "{#ch30_56_8e50647f}"
    new "\"I really don't...\""
