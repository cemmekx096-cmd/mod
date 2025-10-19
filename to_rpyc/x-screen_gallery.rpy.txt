

define -5 gallery_cols = 3
define -5 gallery_rows = 2
define -5 gallery_cols_rows = gallery_cols * gallery_rows

define -5 gallery_scene_xsize = 410
define -5 gallery_scene_ysize = 231







default -5 persistent.gallery_scenes = []

init -5 python:
    def gallery_unlock_scene(scene_name):
        if not scene_name in persistent.gallery_scenes:
            persistent.gallery_scenes.append(scene_name)
            renpy.show_screen("screen_notif_unlock")

    def gallery_scene_unlocked(scene_name):
        return scene_name in persistent.gallery_scenes

    class GalleryScene:
        def __init__(self, kind, name, img, param, unlocked_if, chars, chapter, textInv=None, scope=None, img_scale=None, update_logic=None):
            self.kind = kind
            self.name = name
            self.chapter = chapter
            self.param = param
            self.unlocked_if = unlocked_if
            self.chars = chars
            
            self.textInv = textInv
            if self.textInv is None:
                self.textInv = False
            
            self.update_logic = update_logic
            
            self.scope = scope
            if self.scope is None:
                self.scope = {}
            
            self.scope['chapter'] = self.chapter
            
            self.img = img
            self.img_locked = im.Blur(im.Grayscale(im.MatrixColor(img, im.matrix.brightness(-0.2))), 4)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        def update_img(self):
            if self.update_logic:  
                self.img = self.update_logic()
        
        def is_image(self):
            return self.kind == 'image'
        
        def is_unlocked(self):
            
            if persistent.gallery_force_unlock:
                return True
            else:
                return eval(self.unlocked_if)
        
        def is_for_char(self, char, chapter):
            return (char is None or char in self.chars) and (chapter == 0 or chapter == self.chapter)

    def scope_edit_start(scene_item):
        if scene_item.chapter < 4:
            scene_item.scope.update({'lena_tattoo1': False})
            scene_item.scope.update({'lena_tattoo2': False})
            scene_item.scope.update({'lena_tattoo3': False})
            scene_item.scope.update({'lena_piercing1': False})
            scene_item.scope.update({'lena_piercing2': False})
        else:
            if scene_item.scope.get('scene_protection'):
                scene_item.scope.update({'lena_tattoo1': False})
                scene_item.scope.update({'lena_tattoo2': False})
                scene_item.scope.update({'lena_tattoo3': False})
            else:
                if persistent.gall_lena_tattoo1:
                    scene_item.scope.update({'lena_tattoo1': True})
                else:
                    scene_item.scope.update({'lena_tattoo1': False})
                if persistent.gall_lena_tattoo2:
                    scene_item.scope.update({'lena_tattoo2': True})
                else:
                    scene_item.scope.update({'lena_tattoo2': False})
                if persistent.gall_lena_tattoo3:
                    scene_item.scope.update({'lena_tattoo3': True})
                else:
                    scene_item.scope.update({'lena_tattoo3': False})
            if persistent.gall_lena_piercing1:
                scene_item.scope.update({'lena_piercing1': True})
                scene_item.scope.update({'lena_piercing2': False})
            elif persistent.gall_lena_piercing2:
                scene_item.scope.update({'lena_piercing1': False})
                scene_item.scope.update({'lena_piercing2': True})
        
        return Replay(scene_item.param, scope=scene_item.scope, locked=False)


    def update_all_gallery_images():
        for scene in gallery_scenes:
            scene.update_img()

init -505 screen screen_gallery(char=None, _page=1, char_page=1, chapter=0):
    tag menu

    default page = _page
    default char_title = char
    if char_title is None:
        $ char_title = _("All")

    use game_menu(_("Gallery"), scroll=None, gallery_nav=True, gallery_char=char, gallery_chapter=chapter, gallery_page=page, gallery_char_page=char_page):
        style_prefix "scenes"

        vbox style "empty":
            yoffset -20
            xalign 0.5
            label char_title style "gui_label" xalign 0.5 text_size gui.title_text_size bottom_margin 20

            vbox style "gallery_slots_vbox":
                $ scenes = get_scenes_for_char(char, chapter)
                $ scenes_len = len(scenes)
                $ pages = scenes_len // gallery_cols_rows + min(scenes_len % gallery_cols_rows, 1)

                if pages > 1:

                    hbox:
                        xalign 0.5
                        style_prefix "page"
                        spacing gui.page_spacing

                        textbutton _("<<"):
                            if page > 1:
                                action SetScreenVariable('page', 1)
                        textbutton _("<"):
                            if page > 1:
                                action SetScreenVariable('page', page - 1)

                        $ start = max(page - 5 - max(5 + page - pages, 0), 1)
                        $ end = min(page + 6 + min(max(6 - page, 0), 6), pages + 1)

                        for p in range(start, end):
                            textbutton "[p]" action SetScreenVariable('page', p)

                        textbutton _(">"):
                            if page < pages:
                                action SetScreenVariable('page', page + 1)

                        textbutton _(">>"):
                            if page < pages:
                                action SetScreenVariable('page', pages)
                else:
                    textbutton ""

                grid gallery_cols gallery_rows:
                    xalign 0.5
                    spacing 60

                    $ slots = 0

                    for i in range(min(gallery_cols_rows, scenes_len)):
                        $ idx = (page-1) * gallery_cols_rows + i
                        if idx < scenes_len:
                            $ scene_item = scenes[idx]
                            $ slots += 1

                            frame style "empty":
                                has vbox
                                xysize (gallery_scene_xsize, gallery_scene_ysize)
                                fixed:
                                    if scene_item.is_unlocked():
                                        imagebutton:
                                            idle scene_item.img align (0.5, 0.5)

                                            action If(scene_item.is_image(), 
                                                    true=Show("screen_image", img=scene_item.param, transition=dissolve), 
                                                    false=scope_edit_start(scene_item)
                                                )
                                    else:
                                        imagebutton:
                                            idle scene_item.img_locked align (0.5, 0.5)

                                            action NullAction()

                                    if scene_item.textInv and scene_item.is_unlocked():
                                        text _("Chapter [scene_item.chapter]") align (1.0, 1.0) offset (-8, -3) size 22 color "#000000"
                                    else:
                                        text _("Chapter [scene_item.chapter]") align (1.0, 1.0) offset (-8, -3) size 22

                                    frame style "frame_transparent" xysize (gallery_scene_xsize, gallery_scene_ysize)

                                if scene_item.is_unlocked():
                                    text scene_item.name
                                    text ' & '.join(scene_item.chars) color gui.idle_small_color
                                else:
                                    text _("Locked") color gui.insensitive_color
                                    text ''

                    if slots < gallery_cols_rows:
                        for i in range(gallery_cols_rows - slots):
                            null









init -5 style gallery_slots_vbox is file_slots_vbox:
    spacing 40

init -5 style gallery_slots_vbox is file_slots_vbox:
    variant "small"
    spacing 50

init -505 screen screen_image(img, i=0, transition=dissolve, font=gui.interface_text_font, array_len=None):
    zorder 999
    modal True

    if array_len is None:
        $ array_len = len(img) - 1

    $ layers = isinstance(img[i], list)

    if layers:
        for l in img[i]:
            if isinstance(l, list):
                add l[0] pos l[1] anchor (0.5, 0.5)
            else:
                add l align (0.5, 0.5)
    else:
        add img[i] align (0.5, 0.5)

    text "%d/%d" % (i+1, array_len + 1):
        align (0.99, 0.99)
        font font
        outlines [(2, "#111", 0, 0)]

    if i < array_len:
        key "mouseup_1" action Show("screen_image", img=img, i=i+1, array_len=array_len, transition=transition, font=font)
        key "mouseup_3" action Show("screen_image", img=img, i=i+1, array_len=array_len, transition=transition, font=font)
    else:
        key "mouseup_1" action Hide("screen_image", transition=transition)
        key "mouseup_3" action Hide("screen_image", transition=transition)

    key "K_ESCAPE" action Hide("screen_image", transition=transition)
    key "mouseup_2" action NullAction()

init -5 style scenes_frame is empty:
    xysize (398, 300)

init -5 style scenes_vbox:
    spacing 8
    yalign 0.5

init -5 style scenes_filters_frame:
    background Frame("gui/frame2.webp", 6, 6, 6, 6)
    offset (420, 180)
    yanchor 1.0
    xsize 1400
    xpadding 40

init -5 style scenes_filters_hbox:
    xfill True
    box_wrap True
    spacing 30




init -5 style scenes_text is about_text:
    xalign 0.5
    size 26
    layout "nobreak"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
