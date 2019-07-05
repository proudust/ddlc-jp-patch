define build.name = "DDLC_JP"

init python:
    build.archive("jp", "all")
    build.classify("game/tl/Japanese/**.jpg", "jp")
    build.classify("game/tl/Japanese/**.png", "jp")
    build.classify("game/tl/Japanese/**.txt", "jp")
    build.classify("game/tl/Japanese/**.chr", "jp")
    build.classify("game/tl/Japanese/**.rpyc", "jp")
    build.classify("game/gui/font/*.ttf", "jp")
    build.classify("game/gui/font/*.otf", "jp")

    build.archive("none", "all")
    build.classify("game/tl/None/**.rpyc", "none")
    build.classify("game/images/null.png", "none")

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.classify('**.rpa',None)
    build.classify('firstrun',None)
    build.classify('options.rpy',None)
    build.classify('/characters/**', None)

    build.documentation('*.html')
    build.documentation('*.txt')

    build.include_old_themes = False
