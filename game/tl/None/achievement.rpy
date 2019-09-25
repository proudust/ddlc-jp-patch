define ACHIEVEMENT_START_GAME_ID = "ACHIEVEMENT_START_GAME"
define ACHIEVEMENT_START_GAME_NAME = "Welcome to the Literature Club!"
define ACHIEVEMENT_START_GAME_DESC = "Welcome to the Literature Club! It's always been a dream of mine to make something special out of the things I love. Now that you're a club member, you can help me make that dream come true in this cute game!"

translate None python:
    ddmm_register_achievement(ACHIEVEMENT_START_GAME_ID, __(ACHIEVEMENT_START_GAME_NAME), __(ACHIEVEMENT_START_GAME_DESC))

translate Japanese python:
    ddmm_register_achievement(ACHIEVEMENT_START_GAME_ID, __(ACHIEVEMENT_START_GAME_NAME), __(ACHIEVEMENT_START_GAME_DESC))

translate None ch0_main_41e273ca:
    $ ddmm_earn_achievement(ACHIEVEMENT_START_GAME_ID)
    s "Heeeeeeeyyy!!"

translate Japanese strings:
    old "Welcome to the Literature Club!"
    new "文芸部へようこそ！"

    old "Welcome to the Literature Club! It's always been a dream of mine to make something special out of the things I love. Now that you're a club member, you can help me make that dream come true in this cute game!"
    new "文芸部へようこそ！私の夢は大好きなことを通して、特別なものを作り出すこと。新入部員のあなたには、その夢をこの可愛いゲームで実現させるお手伝いをしてほしいの！"
