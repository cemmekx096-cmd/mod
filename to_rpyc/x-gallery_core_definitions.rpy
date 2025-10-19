





define -2 gallery_characters = [None, 'Lena', 'Ian', 'Alison', 'Axel', 'Billy', 'Cherry', 'Cindy', 'Emma', 'Gillian', 'Holly', 'Ivy', 'Jack', 'Jeremy', 'Jessica', 'John', 'Louise', 'Marcel', 'Mark', 'Mike', 'Minerva', 'Nat', 'Robert', 'Seymour', 'Stan']

default -2 persistent.gall_lena_tattoo1 = False
default -2 persistent.gall_lena_tattoo2 = False
default -2 persistent.gall_lena_tattoo3 = False
default -2 persistent.gall_lena_piercing1 = False
default -2 persistent.gall_lena_piercing2 = False

default -2 gall_lena_look = 1
default -2 gall_flena = "n"

init -2 python:
    def merge_two_dicts(y):
        z = coreScope.copy()        
        z.update(y)
        return z

    def get_scenes_for_char(char, chapter=0):
        global gallery_scenes
        
        scenes = []
        for item in gallery_scenes:
            if item.is_for_char(char, chapter):
                scenes.append(item)
        
        return scenes

define -2 coreScope = {
    
    'ian_active': True,

    
    'ian_wits': 99,
    'ian_charisma': 99,
    'ian_athletics': 99,
    'ian_lust': 99,
    'ian_will': 2,
    'ian_money': 50,

    
    'ian_axel': 12,
    'ian_clark': 12,
    'ian_dad': 12,
    'ian_default': 12,
    'ian_jeremy': 12,
    'ian_mark': 12,
    'ian_mike': 12,
    'ian_perry': 12,
    'ian_robert': 12,
    'ian_seymour': 12,
    'ian_stan': 12,
    'ian_wade': 12,
    'ian_wen': 12,
    'ian_yuri': 12,

    
    'ian_lena': 12,
    'ian_alison': 12,
    'ian_cherry': 12,
    'ian_cindy': 12,
    'ian_gillian': 12,
    'ian_emma': 12,
    'ian_holly': 12,
    'ian_ivy': 12,
    'ian_jess': 12,
    'ian_lola': 12,
    'ian_louise': 12,
    'ian_minerva': 12,
    'ian_nat': 12,

    
    'lena_active': True,

    
    'lena_wits': 99,
    'lena_charisma': 99,
    'lena_athletics': 99,
    'lena_lust': 99,
    'lena_will': 2,
    'lena_money': 50,

    
    'lena_anthony': 12,
    'lena_arthur': 12,
    'lena_axel': 12,
    'lena_billy': 12,
    'lena_lenadad': 12,
    'lena_danny': 12,
    'lena_default': 12,
    'lena_ed': 12,
    'lena_jeremy': 12,
    'lena_mark': 12,
    'lena_mike': 12,
    'lena_perry': 12,
    'lena_producer': 12,
    'lena_robert': 12,
    'lena_seymour': 12,
    'lena_stan': 12,
    'lena_wade': 12,

    
    'lena_agnes': 12,
    'lena_alison': 12,
    'lena_cherry': 12,
    'lena_cindy': 12,
    'lena_emma': 12,
    'lena_gillian': 12,
    'lena_holly': 12,
    'lena_ivy': 12,
    'lena_jess': 12,
    'lena_lola': 12,
    'lena_louise': 12,
    'lena_molly': 12,
    'lena_lenamom': 12,

    
    'ivy_navel': True
}








default -2 ian_alison_pics = []
default -2 ian_axel_pics = []
default -2 ian_cherry_pics = []
default -2 ian_cindy_pics = []
default -2 ian_emma_pics = []
default -2 ian_gillian_pics = []
default -2 ian_holly_pics = []
default -2 ian_ian_pics = []
default -2 ian_ivy_pics = []
default -2 ian_jeremy_pics = []
default -2 ian_lena_pics = []
default -2 ian_louise_pics = []
default -2 ian_marcel_pics = []
default -2 ian_mike_pics = []
default -2 ian_misc_pics = []
default -2 ian_minerva_pics = []
default -2 ian_perry_pics = []
default -2 ian_robert_pics = []
default -2 ian_seymour_pics = []
default -2 ian_stan_pics = []
default -2 ian_wade_pics = []



default -2 lena_alison_pics = []
default -2 lena_axel_pics = []
default -2 lena_cindy_pics = []
default -2 lena_emma_pics = []
default -2 lena_holly_pics = []
default -2 lena_ian_pics = []
default -2 lena_ivy_pics = []
default -2 lena_jeremy_pics = []
default -2 lena_lena_pics = []
default -2 lena_louise_pics = []
default -2 lena_marcel_pics = []
default -2 lena_mike_pics = []
default -2 lena_misc_pics = []
default -2 lena_minerva_pics = []
default -2 lena_perry_pics = []
default -2 lena_robert_pics = []
default -2 lena_seymour_pics = []
default -2 lena_stan_pics = []
default -2 lena_wade_pics = []
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
