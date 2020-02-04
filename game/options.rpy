define build.name = "DDLC_JP"
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]

init python:
    build.package(build.directory_name + "Mod", 'zip', build.name, description='DDLC Compatible Mod')

    build.archive("jp", build.name)
    build.classify("game/tl/Japanese/**.jpg", "jp")
    build.classify("game/tl/Japanese/**.png", "jp")
    build.classify("game/tl/Japanese/**.txt", "jp")
    build.classify("game/tl/Japanese/**.chr", "jp")
    build.classify("game/tl/Japanese/**.rpyc", "jp")
    build.classify("game/gui/font/*.ttf", "jp")
    build.classify("game/gui/font/*.otf", "jp")

    build.archive("none", build.name)
    build.classify("game/tl/None/**.rpyc", "none")
    build.classify("game/images/null.png", "none")

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('**.rpa', None)

    build.classify('README_jp.html', build.name)
    build.classify('readme (jp patch).txt', build.name)
    build.classify('ddmm-mod.json', build.name)

    build.include_old_themes = False
