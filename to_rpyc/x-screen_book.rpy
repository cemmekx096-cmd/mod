screen screen_book(k):
    tag book

    add "gui/cards_bg.webp"

    for i in range(7):
        $ j = i+1
        if j == 1:
            for t in ['scifi', 'fantasy', 'historical']:
                if eval('book_%s' % t):
                    if j == k:
                        imagebutton idle im.Scale("card%s_%s_idle.webp" % (j, t), 283, 410) align (0.5, 0.5) xpos 200 at transform_book_card
                        imagebutton idle im.Scale("card_outline.webp", 283, 410) align (0.5, 0.5) xpos 200
                    else:
                        imagebutton idle im.Scale("card%s_%s_idle.webp" % (j, t), 283, 410) align (0.5, 0.5) xpos 200
        else:
            $ var = eval('book_card%s' % i)
            if var != 'n':
                if j == k:
                    imagebutton idle im.Scale("card_outline.webp", 283, 410) align (0.5, 0.5) xpos 200 + 253 * (j-1)
                    imagebutton idle im.Scale("card%s_%s_idle.webp" % (j, var.replace("_", "")), 283, 410) align (0.5, 0.5) xpos 200 + 253 * (j-1) at transform_book_card
                else:
                    imagebutton idle im.Scale("card%s_%s_idle.webp" % (j, var.replace("_", "")), 283, 410) align (0.5, 0.5) xpos 200 + 253 * (j-1)
            else:
                imagebutton idle im.Scale("card_outline.webp", 283, 410) align (0.5, 0.5) xpos 200 + 253 * (j-1)

    timer 3 action Hide('screen_book', transition=long_dissolve)


transform transform_book_card:
    zoom 0.0
    alpha 0.0
    block:
        parallel:
            linear 0.3 zoom 1.2
        parallel:
            linear 0.3 alpha 1.0

    linear 0.1 zoom 1.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
