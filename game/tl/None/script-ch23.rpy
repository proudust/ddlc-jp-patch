translate None label:
    label ch23_end:
        jump ch23_end_override

label ch23_end_override:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("", Return(True), Return(True))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[2])
        scene black with Dissolve(1.0)
    else:
        pass
    scene bg club_day2
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "Okay, everyone!"
    m "It's time to figure out the festival preparations."
    m 1i "Let's hurry and get this over with."
    if n_appeal >= 2:
        show natsuki 4q zorder 3 at f31
        n "..."
    else:
        show natsuki 4q zorder 3 at f31
        n "Jeez..."
        n "Why is the mood so weird today?"
        n "Look, even Yuri isn't immune to it."
    show natsuki zorder 2 at t31
    show yuri 4b zorder 3 at f33
    y "Uu..."
    y "Stagnating air is common foreshadowing that something terrible is about to happen..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "Look, can we just get this done?"
    m 2d "I'm going to be printing and assembling all the poetry pamphlets."
    if n_appeal >= 2:
        m 2i "Natsuki, you can make cupcakes."
        m "I know you're at least good at that."
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 5u "..."
        show natsuki zorder 2 at t31
        show monika zorder 3 at f32
    else:
        m "Natsuki, I was thinking--"
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 2d "I want to make cupcakes!"
        show natsuki 2a zorder 2 at t31
        show monika zorder 3 at f32
        m 2a "...Yeah, that."
        m "Glad we're on the same page."
    m 1m "Yuri, you can..."
    m 1r "...Well, it doesn't matter."
    m 1i "Do whatever you want, as long as you think it'll help."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Monika..."
    y "I'm not useless, you know!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2p "I-I know that!"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 1l "I already know what I'd like to do."
    y 1h "We can't run a successful poetry event without having the right atmosphere for the occasion."
    y "So I'm going to make decorations and set up some nice mood lighting."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2j "There, see?"
    m "That's a great idea!"
    m 1a "And that gives us all something to do."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2f "Eh?"
    y "What about [player]?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2b "[player] is going to help me."
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4e "Wait, you?"
    n "You have the easiest job, Monika!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1i "Sorry, but that's just how it is."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 1f "Like hell it is!"
    n "What are you trying to pull?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3h "I-I agree with Natsuki!"
    y "Not only is your work already most suitable for one person..."
    y 3l "But my task is laborious enough to benefit from an extra pair of hands."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 4c "Mine too!"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 1h "What, your cupcakes?"
    y "Please."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "Like {i}you{/i} would fucking know!"
    n 1x "All you care about now is dragging [player] around with you and your stupid books."
    n 1f "You {i}and{/i} Monika!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2g "Hey!"
    m "I didn't even do anything!"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3e "Okay, then why not let [player] decide who to help instead of abusing your power?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1p "I'm not...abusing my power."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Yes you are, Monika."
    y "Just let [player] make the choice, okay?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1r "Okay, fine!"
    m "Fine."
    show monika 1h zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3w "Jeez..."
    n "[player], I know how fed up you are with these two by now."
    n 3c "We can just--"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2r "Natsuki, shut your fucking mouth and let him decide for himself."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "{i}You{/i} shut your mouth!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "Jesus christ..."
    m 1i "This is never going to end. Just make the choice, okay?"
    show monika zorder 2 at t32
    python:
        madechoice = renpy.display_menu([("Natsuki.", "natsuki"), ("Yuri.", "yuri"), ("Monika.", "monika")], screen="rigged_choice")

    if madechoice != "monika":
        window hide(None)
        $ musicpos = get_pos()
        stop music
        scene white
        show yuripupils zorder 10
        $ pause(3.0)
        show bg club_day:
            alpha 0.05
            yoffset 0 ytile 2
            linear 5.25 yoffset -720
            repeat
        show noise:
            alpha 0.1
        $ gtext = glitchtext(80)
        window auto
        menu:
            "[gtext]"
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
        scene bg club_day
        $ audio.t3m = "<from " + str(musicpos) + " loop 4.618>bgm/3.ogg"
        play music t3m
        show monika 5 at i11
    else:
        show natsuki zorder 1 at thide
        show yuri zorder 1 at thide
        hide natsuki
        hide yuri

    m 5a "Yay, you picked me!"
    m "We can meet at your house this weekend."
    m "I promise it'll be fun."
    m "Is Sunday okay with you?"
    show natsuki 1e zorder 3 at f31
    n "Are you fucking kidding me?"
    n "This isn't fair at all!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2i "It is fair, Natsuki."
    m "It's what he chose."
    show monika zorder 2 at t32
    show yuri 3r zorder 3 at f33
    y "No, it's not fair!"
    y "Giving us all this work and then taking [player] for yourself."
    y "What a shameful thing to do!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "Yuri, I didn't even give you any work."
    m 2i "You decided it for yourself."
    m "You're being a little unreasonable here."
    stop music
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y4 "I'm being unreasonable?"
    y 2y3 "Ahahaha!"
    y "Monika, I can't believe how delusional and self-important you are!"
    y "Pulling [player] away from me every single time you're not included in something."
    y 1y1 "Are you jealous?"
    y "Crazy?"
    y 1y3 "Or maybe you just hate yourself so much that you take it out on others?"
    y 1y4 "Here's a suggestion. Have you considered killing yourself?"
    y "It would be beneficial to your mental health."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5u "Yuri, you're scaring me a little..."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "Natsuki, let's just go."
    m 1i "I don't think she wants us around right now."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y3 "See, that wasn't very hard."
    y "All I want is to spend a little time with him."
    y "Is that so much to ask?"
    hide natsuki
    hide monika
    hide yuri
    with wipeleft
    "Yuri follows Monika and Natsuki to the door."
    show monika 5a zorder 2 at t11
    m "Hey, [player]..."
    m "Yuri is really something, isn't she?"
    show monika zorder 1 at thide
    hide monika
    "Monika giggles as Yuri pushes her out the door."
    python:
        try: renpy.file(config.basedir + "/have a nice weekend!")
        except: open(config.basedir + "/have a nice weekend!", "w").write(__("G2pilVJccjJiQZ1poiM3iYZhj3I0IRbvj3wxomnoeOatVHUxZ2ozGKJgjXMzj2LgoOitBOM1dSDzHMatdRpmQZpidNehG29mkTxwmDJbGJxsjnVeQT9mTPSwSAOwnuWhSE50ByMpcuJoqGstJOCxqHCtdvG3HJV0TOGuwOIyoOGhwOHgm2GhlZpyISJik3J/"))
        try: os.remove(config.basedir + "/hxppy thxughts.png")
        except: pass
        try: os.remove(config.basedir + "/CAN YOU HEAR ME.txt")
        except: pass
        try: os.remove(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
        except: pass

    play music t10y
    show yuri 2m zorder 2 at t11
    y "Finally."
    y 2y1 "Finally!"
    y 2s "This is really all I wanted."
    y 1y6 "[player], there's no need to spend the weekend with Monika."
    y "Don't listen to her."
    y 1y5 "Just come to my house instead."
    y 3y5 "The whole day, with just the two of us..."
    y "Doesn't that sound wonderful?"
    y 3y1 "Ahahaha!"
    y 3y4 "Wow... There's really something wrong with me, isn't there?"
    y "But you know what?"
    y 1y3 "I don't care anymore."
    y "I've never felt this good my whole life."
    y 1y4 "Just being with you is a far greater pleasure than anything I could imagine."
    y "I'm addicted to you."
    y 3y4 "It feels like I'm going to die if I'm not breathing the same air as you."
    y 4a "Doesn't it feel nice to have someone care about you so much?"
    y "To have someone who wants to revolve their entire life around you?"
    y 2y6 "But if it feels so good..."
    y 2y4 "Then why does it feel more and more like something horrible is going to happen?"
    y 2y6 "Maybe that's why I tried stopping myself at first..."
    y "But the feeling is too strong now."
    y 3y1 "I don't care anymore, [player]!"
    y "I have to tell you!"
    y 3y4 "I'm...I'm madly in love with you!"
    y "It feels like every inch of my body...every drop of blood in me...is screaming your name."
    y 3y3 "I don't care what the consequences are anymore!"
    y "I don't care if Monika is listening!"
    y 3w "Please, [player], just know how much I love you."
    y 3m "I love you so much that I even touch myself with the pen I stole from you."
    y 3y4 "I just want to pull your skin open and crawl inside of you."
    y 3y6 "I want you all to myself."
    y "And I will be only yours."
    y "Doesn't that sound perfect?"
    y 3s "Tell me, [player]."
    y "Tell me you want to be my lover."
    y "Do you accept my confession?"

    menu:
        "Yes.":
            jump yuri_kill
        "No.":
            jump yuri_kill

translate None strings:
    old "{#ch23_main_7050b825}"
    new "\"Hi, [player]!\""

    old "{#ch23_main_1df6e5d1}"
    new "\"I've been waiting for you.\""

    old "{#ch23_main_710e8cd1}"
    new "\"Are you ready to continue reading?\""

    old "{#ch23_main_7ae62c8f}"
    new "\"I brought my best tea today--\""

    old "{#ch23_main_f551a3f1}"
    new "\"Monika!\""

    old "{#ch23_main_9e09898f}"
    new "\"I told you not to--\""

    old "{#ch23_main_51576242}"
    new "\"Ugh...\""

    old "{#ch23_main_2ea6ab87}"
    new "\"Is she really late again?\""

    old "{#ch23_main_ce267a6e}"
    new "\"Inconsiderate as usual, Natsuki.\""

    old "{#ch23_main_ea04149f}"
    new "\"Excuse me?\""

    old "{#ch23_main_ff693c61}"
    new "\"Must you always interrupt my conversations with your incessant yelling?\""

    old "{#ch23_main_f3c12a1b}"
    new "\"What are you talking about?!\""

    old "{#ch23_main_3c0c663d}"
    new "\"You say that like I do it on a regular basis or something.\""

    old "{#ch23_main_61fe94b7}"
    new "\"I just wasn't paying attention, okay? I'm sorry.\""

    old "{#ch23_main_688e23bd}"
    new "\"Seriously... What's gotten into you lately?\""

    old "{#ch23_main_aec99ee7}"
    new "\"Look...\""

    old "{#ch23_main_77a57419}"
    new "\"I did some thinking about yesterday.\""

    old "{#ch23_main_b06fe910}"
    new "\"I was a little more hostile than I meant to be...\""

    old "{#ch23_main_6a970664}"
    new "\"I guess I really felt threatened or something.\""

    old "{#ch23_main_c611de3f}"
    new "\"But I know this is something we're doing together.\""

    old "{#ch23_main_9d78240c}"
    new "\"Another new member wouldn't hurt, as long as they're cool...\""

    old "{#ch23_main_3f2648e5}"
    new "\"And I guess another girl would be nice this time...\""

    old "{#ch23_main_d3a83711}"
    new "\"So...\""

    old "{#ch23_main_61e07ad0}"
    new "\"Natsuki...\""

    old "{#ch23_main_2c85ff6d}"
    new "\"Nobody cares.\""

    old "{#ch23_main_83c58f04}"
    new "\"Why don't you go look for some coins under the vending machines or something?\""

    old "{#ch23_main_a2465aed}"
    new "\"--!\""

    old "{#ch23_main_80e20624}"
    new "\"...\""

    old "{#ch23_main_03fdb2df}"
    new "\"...\""

    old "{#ch23_main_9f4a56c4}"
    new "\"Aw, man...\""

    old "{#ch23_main_055e03b2}"
    new "\"I'm the last one here again!\""

    old "{#ch23_main_6add972a}"
    new "\"Were you practicing piano again?\""

    old "{#ch23_main_36ae6554}"
    new "\"Yeah...\""

    old "{#ch23_main_f6daf90a}"
    new "\"Ahaha...\""

    old "{#ch23_main_f6674ca2}"
    new "\"You must have a lot of determination.\""

    old "{#ch23_main_2e753773}"
    new "\"Starting this club, and still trying to make time for piano...\""

    old "{#ch23_main_d085cf7d}"
    new "\"Well, maybe not determination...\""

    old "{#ch23_main_1c6578c8}"
    new "\"But I guess passion.\""

    old "{#ch23_main_d97c7a77}"
    new "\"It motivates me to work hard for the festival, too.\""

    old "{#ch23_main_e28db252}"
    new "\"Me?\""

    old "{#ch23_main_6707b26d}"
    new "\"N-Nothing...\""

    old "{#ch23_main_bb2cf764}"
    new "\"...\""

    old "{#ch23_main_18e5bacb}"
    new "\"Is it really that bad...?\""

    old "{#ch23_main_3cc8808d}"
    new "\"See, it {i}is{/i} something.\""

    old "{#ch23_main_08cc4542}"
    new "\"I'll get over it!\""

    old "{#ch23_main_47f66db8}"
    new "\"It's not even anything noteworthy...\""

    old "{#ch23_main_48539aa4}"
    new "\"I've just been feeling a little on edge lately...\""

    old "{#ch23_main_c4a524c3}"
    new "\"A-Anyway, we don't need to talk about it!\""

    old "{#ch23_main_3259bf54}"
    new "\"Well, I just felt like I needed to bring it up.\""

    old "{#ch23_main_83be9d6f}"
    new "\"It's not like I really care or anything...\""

    old "{#ch23_main_9f4a56c4_1}"
    new "\"Aw, man...\""

    old "{#ch23_main_055e03b2_1}"
    new "\"I'm the last one here again!\""

    old "{#ch23_main_e9f977cc}"
    new "\"Well, [player] just walked in too.\""

    old "{#ch23_main_6add972a_1}"
    new "\"Were you practicing piano again?\""

    old "{#ch23_main_36ae6554_1}"
    new "\"Yeah...\""

    old "{#ch23_main_f6daf90a_1}"
    new "\"Ahaha...\""

    old "{#ch23_main_f6674ca2_1}"
    new "\"You must have a lot of determination.\""

    old "{#ch23_main_2e753773_1}"
    new "\"Starting this club, and still trying to make time for piano...\""

    old "{#ch23_main_d085cf7d_1}"
    new "\"Well, maybe not determination...\""

    old "{#ch23_main_1c6578c8_1}"
    new "\"But I guess passion.\""

    old "{#ch23_main_baac88a3}"
    new "\"It motivates me to work hard for the festival and...\""

    old "{#ch23_main_a9dfe205}"
    new "\"Um...\""

    old "{#ch23_main_9977936e}"
    new "\"...\""

    old "{#ch23_main_a2744047}"
    new "\"Right...\""

    old "{#ch23_main_fd135007}"
    new "\"I-I forgot...\""

    old "{#ch23_main_3754a60b}"
    new "\"Um, about that, Natsuki...\""

    old "{#ch23_main_6f1da170}"
    new "\"We were all talking yesterday, and...\""

    old "{#ch23_main_93c7a69f}"
    new "\"Well...we decided that we would like to support the festival as well.\""

    old "{#ch23_main_a7088884}"
    new "\"However...!\""

    old "{#ch23_main_dac27ea1}"
    new "\"I understand how you feel about not wanting the club to change.\""

    old "{#ch23_main_edf39968}"
    new "\"I think we all kind of feel that way.\""

    old "{#ch23_main_8a809ddc}"
    new "\"So as long as we're all working together, this club will never become something we don't want.\""

    old "{#ch23_main_bb2cf764_1}"
    new "\"...\""

    old "{#ch23_main_c6a1d93a}"
    new "\"Um, also...\""

    old "{#ch23_main_fadce1c3}"
    new "\"If you help us out with the festival...\""

    old "{#ch23_main_f9ac06bc}"
    new "\"...Then I'll buy you a new manga!\""

    old "{#ch23_main_00e847a6}"
    new "\"...\""

    old "{#ch23_main_b932777d}"
    new "\"Ahahaha!\""

    old "{#ch23_main_5a4d1655}"
    new "\"Sorry, that last part was really funny.\""

    old "{#ch23_main_795c1df2}"
    new "\"Look...\""

    old "{#ch23_main_77a57419_1}"
    new "\"I did some thinking about yesterday.\""

    old "{#ch23_main_b06fe910_1}"
    new "\"I was a little more hostile than I meant to be...\""

    old "{#ch23_main_6a970664_1}"
    new "\"I guess I really felt threatened or something.\""

    old "{#ch23_main_c611de3f_1}"
    new "\"But I know this is something we're doing together.\""

    old "{#ch23_main_9d78240c_1}"
    new "\"Another new member wouldn't hurt, as long as they're cool...\""

    old "{#ch23_main_3f2648e5_1}"
    new "\"And I guess another girl would be nice this time...\""

    old "{#ch23_main_5b5b4f34}"
    new "\"...But more importantly, I would hate to see the event suck just because I chose to back out!\""

    old "{#ch23_main_0dc50158}"
    new "\"I'm a pro, you know!\""

    old "{#ch23_main_6991fd65}"
    new "\"So I'm gonna help too, and we'll make sure it's done right.\""

    old "{#ch23_main_6405094c}"
    new "\"Thank goodness...\""

    old "{#ch23_main_bc78cc3f}"
    new "\"Isn't that great, Monika?\""

    old "{#ch23_main_c3e4602b}"
    new "\"...Monika?\""

    old "{#ch23_main_4db600d5}"
    new "\"Ah--\""

    old "{#ch23_main_357961d6}"
    new "\"Yeah, that's wonderful!\""

    old "{#ch23_main_2e60affc}"
    new "\"It wouldn't be the same without you, Natsuki.\""

    old "{#ch23_main_96ff8363}"
    new "\"Anyway, [player]...\""

    old "{#ch23_main_ba6cd59b}"
    new "\"What do you want to do today?\""

    old "{#ch23_main_c183fdb2}"
    new "\"I was thinking we could--\""

    old "{#ch23_main_5cfe00eb}"
    new "\"We already have plans today.\""

    old "{#ch23_main_07eab780}"
    new "\"Ah...\""

    old "{#ch23_main_56ad88e4}"
    new "\"Is that so, Yuri?\""

    old "{#ch23_main_d470cf0a}"
    new "\"That's correct.\""

    old "{#ch23_main_8a88fa85}"
    new "\"[player] is already engaged in a novel that we're reading together.\""

    old "{#ch23_main_c4c4045b}"
    new "\"Aren't you glad I've already gotten him into literature, Monika?\""

    old "{#ch23_main_a7c87622}"
    new "\"I...\""

    old "{#ch23_main_1164b425}"
    new "\"I suppose...\""

    old "{#ch23_main_4ada0fd4}"
    new "\"I was just--\""

    old "{#ch23_main_a5ae1347}"
    new "\"Actually, it doesn't matter.\""

    old "{#ch23_main_09d0fb57}"
    new "\"It really doesn't.\""

    old "{#ch23_main_79fd62df}"
    new "\"You guys can do whatever you want.\""

    old "{#ch23_main_13ff9bc7}"
    new "\"{i}(Yes!){/i}{w=0.5}{nw}\""

    old "{#ch23_main_727caeb4}"
    new "\"Um... Thank you for understanding, Monika.\""

    old "{#ch23_end_override_90de9c4d}"
    new "\"Okay, everyone!\""

    old "{#ch23_end_override_0993759e}"
    new "\"It's time to figure out the festival preparations.\""

    old "{#ch23_end_override_772ec4c7}"
    new "\"Let's hurry and get this over with.\""

    old "{#ch23_end_override_bb2cf764}"
    new "\"...\""

    old "{#ch23_end_override_a8557d5c}"
    new "\"Jeez...\""

    old "{#ch23_end_override_2035e967}"
    new "\"Why is the mood so weird today?\""

    old "{#ch23_end_override_42c8edbf}"
    new "\"Look, even Yuri isn't immune to it.\""

    old "{#ch23_end_override_6559e79e}"
    new "\"Uu...\""

    old "{#ch23_end_override_3d9092ae}"
    new "\"Stagnating air is common foreshadowing that something terrible is about to happen...\""

    old "{#ch23_end_override_08590660}"
    new "\"Look, can we just get this done?\""

    old "{#ch23_end_override_5a08f549}"
    new "\"I'm going to be printing and assembling all the poetry pamphlets.\""

    old "{#ch23_end_override_dd665f4a}"
    new "\"Natsuki, you can make cupcakes.\""

    old "{#ch23_end_override_18c7cbb6}"
    new "\"I know you're at least good at that.\""

    old "{#ch23_end_override_07a96f6a}"
    new "\"...\""

    old "{#ch23_end_override_770e4677}"
    new "\"Natsuki, I was thinking--\""

    old "{#ch23_end_override_b0ad33ab}"
    new "\"I want to make cupcakes!\""

    old "{#ch23_end_override_b02e47f8}"
    new "\"...Yeah, that.\""

    old "{#ch23_end_override_58304296}"
    new "\"Glad we're on the same page.\""

    old "{#ch23_end_override_31d39fd0}"
    new "\"Yuri, you can...\""

    old "{#ch23_end_override_bed9d866}"
    new "\"...Well, it doesn't matter.\""

    old "{#ch23_end_override_222e42cb}"
    new "\"Do whatever you want, as long as you think it'll help.\""

    old "{#ch23_end_override_a17b13bf}"
    new "\"Monika...\""

    old "{#ch23_end_override_c0d26207}"
    new "\"I'm not useless, you know!\""

    old "{#ch23_end_override_acf82de7}"
    new "\"I-I know that!\""

    old "{#ch23_end_override_78d0b4fa}"
    new "\"I already know what I'd like to do.\""

    old "{#ch23_end_override_364de31c}"
    new "\"We can't run a successful poetry event without having the right atmosphere for the occasion.\""

    old "{#ch23_end_override_e9660d91}"
    new "\"So I'm going to make decorations and set up some nice mood lighting.\""

    old "{#ch23_end_override_19a8f971}"
    new "\"There, see?\""

    old "{#ch23_end_override_2d145eae}"
    new "\"That's a great idea!\""

    old "{#ch23_end_override_2ef36761}"
    new "\"And that gives us all something to do.\""

    old "{#ch23_end_override_5f1028e8}"
    new "\"Eh?\""

    old "{#ch23_end_override_69b689b0}"
    new "\"What about [player]?\""

    old "{#ch23_end_override_f12d9d00}"
    new "\"[player] is going to help me.\""

    old "{#ch23_end_override_03042821}"
    new "\"Wait, you?\""

    old "{#ch23_end_override_1cff0263}"
    new "\"You have the easiest job, Monika!\""

    old "{#ch23_end_override_ec97ece1}"
    new "\"Sorry, but that's just how it is.\""

    old "{#ch23_end_override_1cadb8f9}"
    new "\"Like hell it is!\""

    old "{#ch23_end_override_8c2e73b8}"
    new "\"What are you trying to pull?\""

    old "{#ch23_end_override_2d1ca9bc}"
    new "\"I-I agree with Natsuki!\""

    old "{#ch23_end_override_2fcdee48}"
    new "\"Not only is your work already most suitable for one person...\""

    old "{#ch23_end_override_916ef5f0}"
    new "\"But my task is laborious enough to benefit from an extra pair of hands.\""

    old "{#ch23_end_override_613a8351}"
    new "\"Mine too!\""

    old "{#ch23_end_override_55f6cc17}"
    new "\"What, your cupcakes?\""

    old "{#ch23_end_override_43eb3793}"
    new "\"Please.\""

    old "{#ch23_end_override_6c43f72e}"
    new "\"Like {i}you{/i} would fucking know!\""

    old "{#ch23_end_override_337d9e3a}"
    new "\"All you care about now is dragging [player] around with you and your stupid books.\""

    old "{#ch23_end_override_65c4d2ca}"
    new "\"You {i}and{/i} Monika!\""

    old "{#ch23_end_override_302246ea}"
    new "\"Hey!\""

    old "{#ch23_end_override_c61da5ee}"
    new "\"I didn't even do anything!\""

    old "{#ch23_end_override_83974bd9}"
    new "\"Okay, then why not let [player] decide who to help instead of abusing your power?\""

    old "{#ch23_end_override_53e2984b}"
    new "\"I'm not...abusing my power.\""

    old "{#ch23_end_override_5c462463}"
    new "\"Yes you are, Monika.\""

    old "{#ch23_end_override_6cda4708}"
    new "\"Just let [player] make the choice, okay?\""

    old "{#ch23_end_override_c26d6924}"
    new "\"Okay, fine!\""

    old "{#ch23_end_override_34212887}"
    new "\"Fine.\""

    old "{#ch23_end_override_cc188cde}"
    new "\"Jeez...\""

    old "{#ch23_end_override_73b7482c}"
    new "\"[player], I know how fed up you are with these two by now.\""

    old "{#ch23_end_override_c9ec79af}"
    new "\"We can just--\""

    old "{#ch23_end_override_f1c1e0f4}"
    new "\"Natsuki, shut your fucking mouth and let him decide for himself.\""

    old "{#ch23_end_override_01f5b930}"
    new "\"{i}You{/i} shut your mouth!\""

    old "{#ch23_end_override_9976091a}"
    new "\"Jesus christ...\""

    old "{#ch23_end_override_bf2e6adc}"
    new "\"This is never going to end. Just make the choice, okay?\""

    old "{#ch23_end_override_9128784d}"
    new "\"Yay, you picked me!\""

    old "{#ch23_end_override_8c48ee6a}"
    new "\"We can meet at your house this weekend.\""

    old "{#ch23_end_override_bb9bc753}"
    new "\"I promise it'll be fun.\""

    old "{#ch23_end_override_67ca5074}"
    new "\"Is Sunday okay with you?\""

    old "{#ch23_end_override_308070ea}"
    new "\"Are you fucking kidding me?\""

    old "{#ch23_end_override_77a6e6ae}"
    new "\"This isn't fair at all!\""

    old "{#ch23_end_override_08045a7c}"
    new "\"It is fair, Natsuki.\""

    old "{#ch23_end_override_a5a60aa3}"
    new "\"It's what he chose.\""

    old "{#ch23_end_override_c092a8ae}"
    new "\"No, it's not fair!\""

    old "{#ch23_end_override_c3761d87}"
    new "\"Giving us all this work and then taking [player] for yourself.\""

    old "{#ch23_end_override_de7db816}"
    new "\"What a shameful thing to do!\""

    old "{#ch23_end_override_eb1ce579}"
    new "\"Yuri, I didn't even give you any work.\""

    old "{#ch23_end_override_882dcfe0}"
    new "\"You decided it for yourself.\""

    old "{#ch23_end_override_0f02c58e}"
    new "\"You're being a little unreasonable here.\""

    old "{#ch23_end_override_ab03ad61}"
    new "\"I'm being unreasonable?\""

    old "{#ch23_end_override_f0b3f2ff}"
    new "\"Ahahaha!\""

    old "{#ch23_end_override_18e83623}"
    new "\"Monika, I can't believe how delusional and self-important you are!\""

    old "{#ch23_end_override_545f48d9}"
    new "\"Pulling [player] away from me every single time you're not included in something.\""

    old "{#ch23_end_override_97fd4494}"
    new "\"Are you jealous?\""

    old "{#ch23_end_override_c6ade6c2}"
    new "\"Crazy?\""

    old "{#ch23_end_override_d50febc8}"
    new "\"Or maybe you just hate yourself so much that you take it out on others?\""

    old "{#ch23_end_override_c3d21cd4}"
    new "\"Here's a suggestion. Have you considered killing yourself?\""

    old "{#ch23_end_override_07331406}"
    new "\"It would be beneficial to your mental health.\""

    old "{#ch23_end_override_930a0609}"
    new "\"Yuri, you're scaring me a little...\""

    old "{#ch23_end_override_f56c7ce9}"
    new "\"Natsuki, let's just go.\""

    old "{#ch23_end_override_21e3a942}"
    new "\"I don't think she wants us around right now.\""

    old "{#ch23_end_override_7dedcc9b}"
    new "\"See, that wasn't very hard.\""

    old "{#ch23_end_override_3556f8ae}"
    new "\"All I want is to spend a little time with him.\""

    old "{#ch23_end_override_24e5486c}"
    new "\"Is that so much to ask?\""

    old "{#ch23_end_override_745f0277}"
    new "Yuri follows Monika and Natsuki to the door."

    old "{#ch23_end_override_a6fb49ba}"
    new "\"Hey, [player]...\""

    old "{#ch23_end_override_289f2833}"
    new "\"Yuri is really something, isn't she?\""

    old "{#ch23_end_override_1bd53e19}"
    new "Monika giggles as Yuri pushes her out the door."

    old "{#ch23_end_override_48472cac}"
    new "\"Finally.\""

    old "{#ch23_end_override_6f7becde}"
    new "\"Finally!\""

    old "{#ch23_end_override_0ea00341}"
    new "\"This is really all I wanted.\""

    old "{#ch23_end_override_e0675fad}"
    new "\"[player], there's no need to spend the weekend with Monika.\""

    old "{#ch23_end_override_1c42a8cc}"
    new "\"Don't listen to her.\""

    old "{#ch23_end_override_8b46655e}"
    new "\"Just come to my house instead.\""

    old "{#ch23_end_override_0c29b271}"
    new "\"The whole day, with just the two of us...\""

    old "{#ch23_end_override_def926ca}"
    new "\"Doesn't that sound wonderful?\""

    old "{#ch23_end_override_fd7f98ce}"
    new "\"Ahahaha!\""

    old "{#ch23_end_override_90d54275}"
    new "\"Wow... There's really something wrong with me, isn't there?\""

    old "{#ch23_end_override_84558ab0}"
    new "\"But you know what?\""

    old "{#ch23_end_override_5b7c6a6a}"
    new "\"I don't care anymore.\""

    old "{#ch23_end_override_7c8fd563}"
    new "\"I've never felt this good my whole life.\""

    old "{#ch23_end_override_112ff60f}"
    new "\"Just being with you is a far greater pleasure than anything I could imagine.\""

    old "{#ch23_end_override_1362d6af}"
    new "\"I'm addicted to you.\""

    old "{#ch23_end_override_5e6ebd2a}"
    new "\"It feels like I'm going to die if I'm not breathing the same air as you.\""

    old "{#ch23_end_override_14185dfe}"
    new "\"Doesn't it feel nice to have someone care about you so much?\""

    old "{#ch23_end_override_9de8a560}"
    new "\"To have someone who wants to revolve their entire life around you?\""

    old "{#ch23_end_override_d81ffb78}"
    new "\"But if it feels so good...\""

    old "{#ch23_end_override_e06606db}"
    new "\"Then why does it feel more and more like something horrible is going to happen?\""

    old "{#ch23_end_override_36ddf789}"
    new "\"Maybe that's why I tried stopping myself at first...\""

    old "{#ch23_end_override_3bbfc16f}"
    new "\"But the feeling is too strong now.\""

    old "{#ch23_end_override_17c9d53a}"
    new "\"I don't care anymore, [player]!\""

    old "{#ch23_end_override_b7ae0f1d}"
    new "\"I have to tell you!\""

    old "{#ch23_end_override_80a57d60}"
    new "\"I'm...I'm madly in love with you!\""

    old "{#ch23_end_override_343025a1}"
    new "\"It feels like every inch of my body...every drop of blood in me...is screaming your name.\""

    old "{#ch23_end_override_715e5a8d}"
    new "\"I don't care what the consequences are anymore!\""

    old "{#ch23_end_override_3927c53b}"
    new "\"I don't care if Monika is listening!\""

    old "{#ch23_end_override_9d16ea33}"
    new "\"Please, [player], just know how much I love you.\""

    old "{#ch23_end_override_fd055dd7}"
    new "\"I love you so much that I even touch myself with the pen I stole from you.\""

    old "{#ch23_end_override_1e8884fa}"
    new "\"I just want to pull your skin open and crawl inside of you.\""

    old "{#ch23_end_override_e203cdfd}"
    new "\"I want you all to myself.\""

    old "{#ch23_end_override_149971d3}"
    new "\"And I will be only yours.\""

    old "{#ch23_end_override_b99df2bd}"
    new "\"Doesn't that sound perfect?\""

    old "{#ch23_end_override_e11c83e6}"
    new "\"Tell me, [player].\""

    old "{#ch23_end_override_c162d243}"
    new "\"Tell me you want to be my lover.\""

    old "{#ch23_end_override_ce414874}"
    new "\"Do you accept my confession?\""

    old "{#yuri_kill_1_4d4c9c12}"
    new "\"...Ahahaha.\""

    old "{#yuri_kill_1_3d40b880}"
    new "\"Ahahahahahaha!\""

    old "{#yuri_kill_1_4ddc816c}"
    new "\"Ahahahahahahahaha!\""

    old "{#yuri_kill_1_76475273}"
    new "\"AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA{nw}\""

    old "{#yuri_kill_loop_18a69774}"
    new "\"[persistent.yuri_kill] [gtext]\""

    old "{#yuri_kill_loop_356cde31}"
    new "\"[gtext]\""

    old "{#yuri_kill_3_b1967a39}"
    new "[gtext]"

    old "{#yuri_kill_3_090fa498}"
    new "\"Alright, it's festival time!\""

    old "{#yuri_kill_3_b205d720}"
    new "\"Wow, you got here before me?\""

    old "{#yuri_kill_3_c740f295}"
    new "\"I thought I was pretty ea--{nw}\""

    old "{#yuri_kill_3_05b631cb}"
    new "\"EYAH!\""

    old "{#yuri_kill_3_1e7c525c}"
    new "\"AAAAAAAAAAAAAAAHHHH!!!\""

    old "{#yuri_kill_3_a59d99d8}"
    new "Natsuki runs away."

    old "{#yuri_kill_3_e612037c}"
    new "\"...\""

    old "{#yuri_kill_3_49be24e9}"
    new "\"I'm here!\""

    old "{#yuri_kill_3_bac95057}"
    new "\"[player], did something happen?\""

    old "{#yuri_kill_3_1913d5f2}"
    new "\"Natsuki just ran past me...\""

    old "{#yuri_kill_3_3ac5a02b}"
    new "\"...Oh...\""

    old "{#yuri_kill_3_0362ff41}"
    new "\"...Oh.\""

    old "{#yuri_kill_3_f1cff12f}"
    new "\"...\""

    old "{#yuri_kill_3_3cbf362f}"
    new "\"Ahahaha!\""

    old "{#yuri_kill_3_6834df2a}"
    new "\"Well, that's a shame.\""

    old "{#yuri_kill_3_49f56652}"
    new "\"Wait, were you here the entire weekend, [player]?\""

    old "{#yuri_kill_3_fe7c1a9b}"
    new "\"Oh, jeez...\""

    old "{#yuri_kill_3_7f0b2e96}"
    new "\"I didn't realize the script was broken that badly.\""

    old "{#yuri_kill_3_6ea274cb}"
    new "\"I'm super sorry!\""

    old "{#yuri_kill_3_afa45be0}"
    new "\"It must have been pretty boring...\""

    old "{#yuri_kill_3_989d77b0}"
    new "\"I'll make it up to you, okay?\""

    old "{#yuri_kill_3_0fc97937}"
    new "\"Just gimme a sec...\""

    old "{#yuri_kill_3_da4f4260}"
    new "\"I'm almost done.\""

    old "{#yuri_kill_3_4fdfebc5}"
    new "\"I just want to have a cupcake real quick!\""

    old "{#yuri_kill_3_651eefb8}"
    new "Monika lifts the foil from [gtext]'s tray and takes a cupcake."

    old "{#yuri_kill_3_c05aafc0}"
    new "\"Seriously, these are the best!\""

    old "{#yuri_kill_3_38b79e4c}"
    new "\"I really just had to have one, since it's the last time I'll ever get the chance to.\""

    old "{#yuri_kill_3_19b43c0c}"
    new "\"You know, before they stop existing and everything.\""

    old "{#yuri_kill_3_0b28b069}"
    new "\"...But anyway, I really shouldn't be making you wait any longer.\""

    old "{#yuri_kill_3_78bd679a}"
    new "\"Just bear with me, okay?\""

    old "{#yuri_kill_3_1ffc01fd}"
    new "\"This should only take a second.\""
