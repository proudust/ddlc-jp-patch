init python:
    def recreate_character(name):
        try:
            renpy.file("../characters/" + name + ".chr")
            delete_character(name)
            open(config.basedir + "/characters/" + name + ".chr", "wb").write(renpy.file(name + ".chr").read())
        except: pass

translate None python:
    recreate_character('sayori')
    recreate_character('monika')
    recreate_character('natsuki')
    recreate_character('yuri')
