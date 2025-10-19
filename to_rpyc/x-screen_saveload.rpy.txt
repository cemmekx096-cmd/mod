










init -501 screen save():
    tag menu
    use file_slots(_("Save"))


init -501 screen load():
    tag menu

    if main_menu:
        use file_slots(_("Load"))
    else:
        use phone_load

define -1 saveload_maxpages = 900
define -1 saveload_previus_page = 1

init -501 screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    default hover_slot = None

    use game_menu(title):
        vbox style "file_slots_vbox":

            order_reverse True


            button style "page_label":
                key_events True
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                spacing gui.slot_spacing
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        hovered SetLocalVariable("hover_slot", slot)
                        unhovered SetLocalVariable('hover_slot', None)
                        action FileAction(slot)

                        has vbox spacing 2

                        add Frame(FileScreenshot(slot), xysize=(gui.slot_width, gui.slot_height)) xalign 0.5

                        text FileTime(slot, format="%c", empty=_("empty slot")):
                            style "slot_time_text"
                            xalign 0.5

                        text FileSaveName(slot):
                            style "slot_name_text"
                            xalign 0.5

                        key "save_delete" action FileDelete(slot)

                        if hover_slot == slot:
                            imagebutton:
                                auto "/gui/button/delete_%s_button.png"
                                action FileDelete(slot)
                                xpos 186
                                ypos -196
                                hovered SetLocalVariable("hover_slot", slot)
                                unhovered SetLocalVariable('hover_slot', None)
                        else:
                            add Null(30,30)


            hbox style "page_hbox":
                style_prefix "page"
                spacing gui.page_spacing

                $ realpage = int(FilePageName(0,0))
                $ page = realpage
                if page < 1:
                    $ page = saveload_previus_page

                textbutton _("<<"):
                    if page > 1:
                        action FilePage(1)
                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action SelectedIf(FilePage("auto")), SetVariable('saveload_previus_page', page)

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action SelectedIf(FilePage("quick")), SetVariable('saveload_previus_page', page)

                $ start = max(page - 5 - max(5 + page - saveload_maxpages, 0), 1)
                $ end = min(page + 6 + min(max(6 - page, 0), 6), saveload_maxpages + 1)

                for p in range(start, end):
                    textbutton "[p]" action FilePage(p)

                textbutton _(">"):
                    if page < saveload_maxpages or realpage == 0:
                        action FilePageNext()
                textbutton _(">>"):
                    if page < saveload_maxpages or realpage == 0:
                        action FilePage(saveload_maxpages)


init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text

init -1 style file_slots_vbox:
    xalign 0.5
    spacing 60

init -1 style file_slots_vbox:
    variant "small"
    spacing 110

init -1 style page_label is gui_label:
    xpadding 75
    ypadding 5
    xalign 0.5

init -1 style page_label_text is gui_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color
    outlines [(0, "#0008", 1, 1)]

init -1 style page_hbox:
    align (0.5, 0.94)

init -1 style page_button is gui_button:
    properties gui.button_properties("page_button")

init -1 style page_button_text is gui_button_text:
    properties gui.button_text_properties("page_button")
    outlines [(0, "#0008", 1, 1)]

init -1 style slot_button is gui_button:
    properties gui.button_properties("slot_button")

init -1 style slot_button_text is gui_button_text:
    properties gui.button_text_properties("slot_button")
    outlines [(0, "#0008", 1, 1)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
