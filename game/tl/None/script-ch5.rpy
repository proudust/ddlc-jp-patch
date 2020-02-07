translate None label:
    label ch5_main:
        jump ch5_main_override

label ch5_main_override:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    "It's the day of the festival."
    "Of all days, I expected this to be the one where I'd be walking to school with Sayori."
    "But Sayori isn't answering her phone."
    "I considered going to her house to wake her up, but decided that's a little too much."
    "Meanwhile, the preparations for the event should be nearly complete."
    if ch4_scene == "natsuki":
        "I managed to carry all the cupcakes myself by carefully stacking two trays."
        "Natsuki is already texting up a storm, but I can't respond, thanks to my hands being full."
    else:
        "The banner Yuri and I painted is dry, and I gently rolled it up to take with me."
        "She sent me a pleasant text reminding me not to forget anything, and I reassured her."
    "Funnily enough, I probably feel the same way as Natsuki about the event."
    "I'm more excited for it to be over so I can spend time with Sayori and [ch4_name] at the festival."
    "But knowing Monika, I'm sure the event will be great, too."

    scene bg club_day with wipeleft_scene
    show monika 5 zorder 2 at t11
    m "[player]!"
    m "You're the first one here."
    m "Thanks for being early!"
    mc "That's funny, I thought at least Yuri would be here by now."
    "Monika is placing little booklets on each of the desks in the classroom."
    "They must be the ones she prepared that have all the poems we're performing."
    "In the end, I found a random poem online that I thought Monika would like, and submitted it."
    "So, that's the one I'll be performing."
    m 1d "I'm surprised you didn't bring Sayori with you."
    mc "Yeah, she overslept again..."
    mc "That dummy."
    mc "You'd think that on days this important, she'd try a little harder..."
    "I say that, but I suddenly remember what Sayori told me yesterday..."
    "And I suddenly feel awful, knowing it's not nearly that simple for her."
    "I only said it because it's the way I'm used to thinking."
    "But..."
    "Maybe I should have gone to wake her up after all?"
    m 1k "Ahaha."
    m 4b "You should take a little responsibility for her, [player]!"
    m "I mean, especially after your exchange with her yesterday..."
    m "You kind of left her hanging this morning, you know?"
    show monika 4a
    mc "Exchange...?"
    mc "Monika-- You know about that??"
    m 2a "Of course I do."
    m "I'm the club president, after all."
    mc "But--!"
    "I stammer, embarrassed."
    "Did Sayori really tell her about it that quickly?"
    if sayori_confess:
        "That we're...a couple now?"
        "I didn't really plan on bringing it up with anyone yet..."
    else:
        "About how I basically turned down her confession?"
        "That makes me really seem like the bad guy here..."
        "But I'm the one who knows what's best for her, right?"
    mc "Jeez..."
    mc "You don't know the full story at all, so..."
    m 2j "Don't worry."
    m "I probably know a lot more than you think."
    mc "Eh...?"
    "Monika is being as friendly as usual, but for some reason I felt a chill down my spine after hearing that."
    m 5 "Hey, do you want to check out the pamphlets?"
    m "They came out really nice!"
    mc "Yeah, sure."
    "I grab one of the pamphlets laid out on the desks."
    mc "Oh yeah, they really did."
    mc "Something like this will definitely help people take the club more seriously."
    m "Yeah, I thought so too!"
    show monika zorder 1 at thide
    hide monika
    "I flip through the pages."
    "Each member's poem is neatly printed on its own page, giving it an almost professional feel."
    "I recognize Natsuki's and Yuri's poems from the ones they performed during our practice."
    mc "What's this...?"
    "I flip to Sayori's poem."
    "It's different from the one she practiced."
    "It's one that I haven't read before..."
    call showpoem (poem_s3, music=False)
    mc "Ah--"
    "What is this...?"
    "Reading the poem, I get a pit in my stomach."
    show monika 1d zorder 2 at t11
    m "[player]?"
    m "What's wrong?"
    mc "Ah, nothing..."
    "This poem feels completely different from everything else Sayori's written."
    "But more than that..."
    mc "I-I changed my mind!"
    mc "I'm going to go get Sayori, so..."
    m "Ah--"
    m 1b "Well, alright!"
    m "Try not to take too long, okay?"
    scene bg corridor with wipeleft
    "I quickly leave the classroom."
    m "Don't strain yourself~"
    "Monika calls that out after me."
    "I quicken my pace."

    scene bg residential_day with wipeleft_scene
    "What was I thinking?"
    "I should have tried a little bit harder for Sayori."
    "It's not a big deal to at least wait for her, or help her wake up."
    "Even the simple gesture of walking her to school makes her really happy."
    "Besides..."
    "I told her yesterday that things will be the same as they always have been."
    "That's all she needs, and what I want to give her."

    scene bg house with wipeleft
    "I reach Sayori's house and knock on the door."
    "I don't expect an answer, since she's not picking up her phone, either."
    "Like yesterday, I open the door and let myself in."
    scene black with wipeleft
    mc "Sayori?"
    "She really is a heavy sleeper..."
    "I swallow."
    "I can't believe I ended up doing this after all."
    "Waking her up in her own house..."
    if sayori_confess:
        "That really is something that a boyfriend would do, isn't it?"
    else:
        "Isn't that more like something a boyfriend would do?"
    "In any case..."
    "It just feels right."

    "Outside Sayori's room, I knock on her door."
    mc "Sayori?"
    mc "Wake up, dummy..."
    "There's no response."
    "I really didn't want to have to enter her room like this..."
    "Isn't it kind of a breach of privacy?"
    "But she really leaves me no choice."
    "I gently open the door."
    mc "{cps=30}.......Sayo--{/cps}{nw}"
    $ persistent.playthrough = 1
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ renpy.save_persistent()
    $ delete_character("sayori")
    $ in_sayori_kill = True
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    $ pause(3.75)
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    $ pause(0.01)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    $ pause(2.0)
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    $ pause(1.5)
    show white zorder 2
    show splash_glitch zorder 2
    $ pause(1.5)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    $ pause(4.0)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    $ pause(0.75)
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: sys.modules['renpy.error'].report_exception(__("Oh jeez...I didn't break anything, did I? Hold on a sec, I can probably fix this...I think...\nActually, you know what? This would probably be a lot easier if I just deleted her. She's the one who's making this so difficult. Ahaha! Well, here goes nothing."), False)
        except: pass
    $ pause(6.0)

    "..."
    hide fake_exception
    hide fake_exception2
    hide exception_bg
    "What the hell...?"
    "{i}What the hell??{/i}"
    "Is this a nightmare?"
    "It...has to be."
    "This isn't real."
    "There's no way this can be real."
    "Sayori wouldn't do this."
    "Everything was normal up until a few days ago."
    "That's why I can't believe what my eyes are showing me...!"
    scene black with dissolve_cg
    "I suppress the urge to vomit."
    "Just yesterday..."
    "I told Sayori I would be there for her."
    "I told her I know what's best, and that everything will be okay."
    "Then why...?"
    "Why would she do this...?"
    "How could I be so helpless?"
    "What did I do wrong?"
    if sayori_confess:
        "Confessing to her..."
        "I shouldn't have confessed to her."
        "That's not what Sayori needed at all."
        "She even told me how painful it is for others to care about her."
        "Then why did I confess to her, and make her feel even worse?"
    else:
        "Turning down her confession..."
        "That has to have been what pushed her over the edge."
        "Her agonized scream still echoes in my ears."
        "Why did I do that to her when she needed me the most?"
    "Why was I so selfish?"
    "This is my fault--!"
    "My swarming thoughts keep telling me everything I could have done to prevent this."
    "If I just spent more time with her."
    "Walked her to school."
    if sayori_confess:
        "And remained friends with her, like it always has been..."
    else:
        "And gave her what I know she wanted out of our relationship..."
    "...Then I could have prevented this."
    "I know I could have prevented this!"
    "Screw the Literature Club."
    "Screw the festival."
    "I just...lost my best friend."
    "Someone I grew up with."
    "She's gone forever now."
    "Nothing I do can bring her back."
    "This isn't some game where I can reset and try something different."
    "I had only one chance, and I wasn't careful enough."
    "And now I'll carry this guilt with me until I die."
    "Nothing in my life is worth more than hers..."
    "But I still couldn't do what she needed from me."
    "And now..."
    "I can never take it back."
    "Never."
    "Never."
    "Never."
    "Never."
    "Never..."
    $ in_sayori_kill = False

    return

translate None strings:
    old "{#ch5_main_override_291cd73e}"
    new "It's the day of the festival."

    old "{#ch5_main_override_f55f58cd}"
    new "Of all days, I expected this to be the one where I'd be walking to school with Sayori."

    old "{#ch5_main_override_5f35e367}"
    new "But Sayori isn't answering her phone."

    old "{#ch5_main_override_aa057f44}"
    new "I considered going to her house to wake her up, but decided that's a little too much."

    old "{#ch5_main_override_66ad1f62}"
    new "Meanwhile, the preparations for the event should be nearly complete."

    old "{#ch5_main_override_e71f443a}"
    new "I managed to carry all the cupcakes myself by carefully stacking two trays."

    old "{#ch5_main_override_5f772eb6}"
    new "Natsuki is already texting up a storm, but I can't respond, thanks to my hands being full."

    old "{#ch5_main_override_01a9488e}"
    new "The banner Yuri and I painted is dry, and I gently rolled it up to take with me."

    old "{#ch5_main_override_6156c542}"
    new "She sent me a pleasant text reminding me not to forget anything, and I reassured her."

    old "{#ch5_main_override_12c35a24}"
    new "Funnily enough, I probably feel the same way as Natsuki about the event."

    old "{#ch5_main_override_201144fc}"
    new "I'm more excited for it to be over so I can spend time with Sayori and [ch4_name] at the festival."

    old "{#ch5_main_override_8ede78be}"
    new "But knowing Monika, I'm sure the event will be great, too."

    old "{#ch5_main_override_f6a40c3b}"
    new "\"[player]!\""

    old "{#ch5_main_override_83e6198b}"
    new "\"You're the first one here.\""

    old "{#ch5_main_override_cbd0885b}"
    new "\"Thanks for being early!\""

    old "{#ch5_main_override_b16212d3}"
    new "\"That's funny, I thought at least Yuri would be here by now.\""

    old "{#ch5_main_override_869ed546}"
    new "Monika is placing little booklets on each of the desks in the classroom."

    old "{#ch5_main_override_158d922b}"
    new "They must be the ones she prepared that have all the poems we're performing."

    old "{#ch5_main_override_1fd6873b}"
    new "In the end, I found a random poem online that I thought Monika would like, and submitted it."

    old "{#ch5_main_override_8185735f}"
    new "So, that's the one I'll be performing."

    old "{#ch5_main_override_185b9181}"
    new "\"I'm surprised you didn't bring Sayori with you.\""

    old "{#ch5_main_override_c458dfb9}"
    new "\"Yeah, she overslept again...\""

    old "{#ch5_main_override_b260a3a6}"
    new "\"That dummy.\""

    old "{#ch5_main_override_81fc5eee}"
    new "\"You'd think that on days this important, she'd try a little harder...\""

    old "{#ch5_main_override_e8c60bf9}"
    new "I say that, but I suddenly remember what Sayori told me yesterday..."

    old "{#ch5_main_override_bfc9484c}"
    new "And I suddenly feel awful, knowing it's not nearly that simple for her."

    old "{#ch5_main_override_804f14c9}"
    new "I only said it because it's the way I'm used to thinking."

    old "{#ch5_main_override_bf0874e3}"
    new "But..."

    old "{#ch5_main_override_b06045eb}"
    new "Maybe I should have gone to wake her up after all?"

    old "{#ch5_main_override_716c1a0f}"
    new "\"Ahaha.\""

    old "{#ch5_main_override_39018d06}"
    new "\"You should take a little responsibility for her, [player]!\""

    old "{#ch5_main_override_a7c132be}"
    new "\"I mean, especially after your exchange with her yesterday...\""

    old "{#ch5_main_override_8ad57878}"
    new "\"You kind of left her hanging this morning, you know?\""

    old "{#ch5_main_override_2a8e5cd8}"
    new "\"Exchange...?\""

    old "{#ch5_main_override_fae1792d}"
    new "\"Monika-- You know about that??\""

    old "{#ch5_main_override_22f1452d}"
    new "\"Of course I do.\""

    old "{#ch5_main_override_bad6f1a7}"
    new "\"I'm the club president, after all.\""

    old "{#ch5_main_override_bcfeb37f}"
    new "\"But--!\""

    old "{#ch5_main_override_13e443ec}"
    new "I stammer, embarrassed."

    old "{#ch5_main_override_14d59814}"
    new "Did Sayori really tell her about it that quickly?"

    old "{#ch5_main_override_7b4085e0}"
    new "That we're...a couple now?"

    old "{#ch5_main_override_e98494a0}"
    new "I didn't really plan on bringing it up with anyone yet..."

    old "{#ch5_main_override_7078ecec}"
    new "About how I basically turned down her confession?"

    old "{#ch5_main_override_841118bf}"
    new "That makes me really seem like the bad guy here..."

    old "{#ch5_main_override_bea221f2}"
    new "But I'm the one who knows what's best for her, right?"

    old "{#ch5_main_override_9098da49}"
    new "\"Jeez...\""

    old "{#ch5_main_override_c012ccb9}"
    new "\"You don't know the full story at all, so...\""

    old "{#ch5_main_override_61ca7335}"
    new "\"Don't worry.\""

    old "{#ch5_main_override_8a0a254a}"
    new "\"I probably know a lot more than you think.\""

    old "{#ch5_main_override_bbe4458e}"
    new "\"Eh...?\""

    old "{#ch5_main_override_0ad66631}"
    new "Monika is being as friendly as usual, but for some reason I felt a chill down my spine after hearing that."

    old "{#ch5_main_override_115550e4}"
    new "\"Hey, do you want to check out the pamphlets?\""

    old "{#ch5_main_override_3dd8757c}"
    new "\"They came out really nice!\""

    old "{#ch5_main_override_b1ac94f7}"
    new "\"Yeah, sure.\""

    old "{#ch5_main_override_cf774ef8}"
    new "I grab one of the pamphlets laid out on the desks."

    old "{#ch5_main_override_c358e345}"
    new "\"Oh yeah, they really did.\""

    old "{#ch5_main_override_2dd533a0}"
    new "\"Something like this will definitely help people take the club more seriously.\""

    old "{#ch5_main_override_9d72086a}"
    new "\"Yeah, I thought so too!\""

    old "{#ch5_main_override_e9739dad}"
    new "I flip through the pages."

    old "{#ch5_main_override_dcc9e068}"
    new "Each member's poem is neatly printed on its own page, giving it an almost professional feel."

    old "{#ch5_main_override_d58b0f7f}"
    new "I recognize Natsuki's and Yuri's poems from the ones they performed during our practice."

    old "{#ch5_main_override_4ad8684c}"
    new "\"What's this...?\""

    old "{#ch5_main_override_781439d4}"
    new "I flip to Sayori's poem."

    old "{#ch5_main_override_48cf059d}"
    new "It's different from the one she practiced."

    old "{#ch5_main_override_d1acea01}"
    new "It's one that I haven't read before..."

    old "{#ch5_main_override_f9d65918}"
    new "\"Ah--\""

    old "{#ch5_main_override_ce9ffd82}"
    new "What is this...?"

    old "{#ch5_main_override_f8df116d}"
    new "Reading the poem, I get a pit in my stomach."

    old "{#ch5_main_override_de87a206}"
    new "\"[player]?\""

    old "{#ch5_main_override_6a3f2020}"
    new "\"What's wrong?\""

    old "{#ch5_main_override_ef5f85f4}"
    new "\"Ah, nothing...\""

    old "{#ch5_main_override_db0952f0}"
    new "This poem feels completely different from everything else Sayori's written."

    old "{#ch5_main_override_38f127a1}"
    new "But more than that..."

    old "{#ch5_main_override_d0abb0e9}"
    new "\"I-I changed my mind!\""

    old "{#ch5_main_override_45476ba9}"
    new "\"I'm going to go get Sayori, so...\""

    old "{#ch5_main_override_4db600d5}"
    new "\"Ah--\""

    old "{#ch5_main_override_0ceabd85}"
    new "\"Well, alright!\""

    old "{#ch5_main_override_69a061e2}"
    new "\"Try not to take too long, okay?\""

    old "{#ch5_main_override_80ea11e1}"
    new "I quickly leave the classroom."

    old "{#ch5_main_override_08b7a135}"
    new "\"Don't strain yourself~\""

    old "{#ch5_main_override_e2a4926d}"
    new "Monika calls that out after me."

    old "{#ch5_main_override_a2c82474}"
    new "I quicken my pace."

    old "{#ch5_main_override_1642a559}"
    new "What was I thinking?"

    old "{#ch5_main_override_b22de3d6}"
    new "I should have tried a little bit harder for Sayori."

    old "{#ch5_main_override_bf20ec7b}"
    new "It's not a big deal to at least wait for her, or help her wake up."

    old "{#ch5_main_override_e601aa4e}"
    new "Even the simple gesture of walking her to school makes her really happy."

    old "{#ch5_main_override_70e7cabf}"
    new "Besides..."

    old "{#ch5_main_override_68430306}"
    new "I told her yesterday that things will be the same as they always have been."

    old "{#ch5_main_override_e35fe926}"
    new "That's all she needs, and what I want to give her."

    old "{#ch5_main_override_558b962d}"
    new "I reach Sayori's house and knock on the door."

    old "{#ch5_main_override_b8d78e77}"
    new "I don't expect an answer, since she's not picking up her phone, either."

    old "{#ch5_main_override_a19898c6}"
    new "Like yesterday, I open the door and let myself in."

    old "{#ch5_main_override_e766b9e2}"
    new "\"Sayori?\""

    old "{#ch5_main_override_4f4ec354}"
    new "She really is a heavy sleeper..."

    old "{#ch5_main_override_17df0a8d}"
    new "I swallow."

    old "{#ch5_main_override_5166b167}"
    new "I can't believe I ended up doing this after all."

    old "{#ch5_main_override_66baf796}"
    new "Waking her up in her own house..."

    old "{#ch5_main_override_7e7f0370}"
    new "That really is something that a boyfriend would do, isn't it?"

    old "{#ch5_main_override_d39780a5}"
    new "Isn't that more like something a boyfriend would do?"

    old "{#ch5_main_override_cc4d5947}"
    new "In any case..."

    old "{#ch5_main_override_eff61fd1}"
    new "It just feels right."

    old "{#ch5_main_override_b771a755}"
    new "Outside Sayori's room, I knock on her door."

    old "{#ch5_main_override_e766b9e2_1}"
    new "\"Sayori?\""

    old "{#ch5_main_override_2d697678}"
    new "\"Wake up, dummy...\""

    old "{#ch5_main_override_4f673053}"
    new "There's no response."

    old "{#ch5_main_override_e55755b1}"
    new "I really didn't want to have to enter her room like this..."

    old "{#ch5_main_override_5f524499}"
    new "Isn't it kind of a breach of privacy?"

    old "{#ch5_main_override_92ad08b5}"
    new "But she really leaves me no choice."

    old "{#ch5_main_override_b0993b5c}"
    new "I gently open the door."

    old "{#ch5_main_override_414399e6}"
    new "\"{cps=30}.......Sayo--{/cps}{nw}\""

    old "{#ch5_main_override_a20cefa7}"
    new "..."

    old "{#ch5_main_override_d9da181d}"
    new "What the hell...?"

    old "{#ch5_main_override_3f892db7}"
    new "{i}What the hell??{/i}"

    old "{#ch5_main_override_3e132bf6}"
    new "Is this a nightmare?"

    old "{#ch5_main_override_bee33b8a}"
    new "It...has to be."

    old "{#ch5_main_override_b79b8271}"
    new "This isn't real."

    old "{#ch5_main_override_f7d3bace}"
    new "There's no way this can be real."

    old "{#ch5_main_override_d463aeb5}"
    new "Sayori wouldn't do this."

    old "{#ch5_main_override_80b8347e}"
    new "Everything was normal up until a few days ago."

    old "{#ch5_main_override_bcc0cf21}"
    new "That's why I can't believe what my eyes are showing me...!"

    old "{#ch5_main_override_14052544}"
    new "I suppress the urge to vomit."

    old "{#ch5_main_override_83c08dc6}"
    new "Just yesterday..."

    old "{#ch5_main_override_63d916b6}"
    new "I told Sayori I would be there for her."

    old "{#ch5_main_override_60eed88f}"
    new "I told her I know what's best, and that everything will be okay."

    old "{#ch5_main_override_d7afa724}"
    new "Then why...?"

    old "{#ch5_main_override_b65618dd}"
    new "Why would she do this...?"

    old "{#ch5_main_override_914b926a}"
    new "How could I be so helpless?"

    old "{#ch5_main_override_ef4dcc76}"
    new "What did I do wrong?"

    old "{#ch5_main_override_be3441df}"
    new "Confessing to her..."

    old "{#ch5_main_override_5d397de2}"
    new "I shouldn't have confessed to her."

    old "{#ch5_main_override_28eecbc0}"
    new "That's not what Sayori needed at all."

    old "{#ch5_main_override_83b32ad7}"
    new "She even told me how painful it is for others to care about her."

    old "{#ch5_main_override_866f2bae}"
    new "Then why did I confess to her, and make her feel even worse?"

    old "{#ch5_main_override_c298f032}"
    new "Turning down her confession..."

    old "{#ch5_main_override_43f22dd0}"
    new "That has to have been what pushed her over the edge."

    old "{#ch5_main_override_ed1a20bb}"
    new "Her agonized scream still echoes in my ears."

    old "{#ch5_main_override_390af3d1}"
    new "Why did I do that to her when she needed me the most?"

    old "{#ch5_main_override_52adb6dd}"
    new "Why was I so selfish?"

    old "{#ch5_main_override_b8970560}"
    new "This is my fault--!"

    old "{#ch5_main_override_784c9188}"
    new "My swarming thoughts keep telling me everything I could have done to prevent this."

    old "{#ch5_main_override_38a05e13}"
    new "If I just spent more time with her."

    old "{#ch5_main_override_61323b0a}"
    new "Walked her to school."

    old "{#ch5_main_override_fafa7f27}"
    new "And remained friends with her, like it always has been..."

    old "{#ch5_main_override_40330930}"
    new "And gave her what I know she wanted out of our relationship..."

    old "{#ch5_main_override_b500c19c}"
    new "...Then I could have prevented this."

    old "{#ch5_main_override_3fb68386}"
    new "I know I could have prevented this!"

    old "{#ch5_main_override_dbc1a352}"
    new "Screw the Literature Club."

    old "{#ch5_main_override_6ca38f65}"
    new "Screw the festival."

    old "{#ch5_main_override_9e6ea412}"
    new "I just...lost my best friend."

    old "{#ch5_main_override_bf83b2a4}"
    new "Someone I grew up with."

    old "{#ch5_main_override_8166b65b}"
    new "She's gone forever now."

    old "{#ch5_main_override_1346d49e}"
    new "Nothing I do can bring her back."

    old "{#ch5_main_override_47810304}"
    new "This isn't some game where I can reset and try something different."

    old "{#ch5_main_override_061507cc}"
    new "I had only one chance, and I wasn't careful enough."

    old "{#ch5_main_override_34819040}"
    new "And now I'll carry this guilt with me until I die."

    old "{#ch5_main_override_aa24ed84}"
    new "Nothing in my life is worth more than hers..."

    old "{#ch5_main_override_96fa7cd8}"
    new "But I still couldn't do what she needed from me."

    old "{#ch5_main_override_226d890f}"
    new "And now..."

    old "{#ch5_main_override_ad63a323}"
    new "I can never take it back."

    old "{#ch5_main_override_b8dc6375}"
    new "Never."

    old "{#ch5_main_override_b8dc6375_1}"
    new "Never."

    old "{#ch5_main_override_b8dc6375_2}"
    new "Never."

    old "{#ch5_main_override_b8dc6375_3}"
    new "Never."

    old "{#ch5_main_override_e650a699}"
    new "Never..."
