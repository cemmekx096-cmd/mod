
transform look:
    linear 8.0 yalign 1.0
    linear 4.0 yalign 0.05
    repeat 1





screen lexie01():
    add "lexie01" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("lexie01bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("lexie01", transition=fade)
    key "game_menu" action Hide("lexie01", transition=fade)

screen lexie01bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "lexie01"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("lexie01bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("lexie01bis", transition=fade)

screen lexie02():
    add "lexie02"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie02", transition=fade)
    key "game_menu" action Hide("lexie02", transition=fade)

screen lexie03():
    add "lexie03" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("lexie03bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("lexie03", transition=fade)
    key "game_menu" action Hide("lexie03", transition=fade)


screen lexie03bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "lexie03"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("lexie03bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("lexie03bis", transition=fade)

screen lexie04():
    add "lexie04" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("lexie04bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("lexie04", transition=fade)
    key "game_menu" action Hide("lexie04", transition=fade)

screen lexie04bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "lexie04"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("lexie04bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("lexie04bis", transition=fade)


screen lexie05():
    add "lexie05"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie05", transition=fade)
    key "game_menu" action Hide("lexie05", transition=fade)

screen lexie06():
    add "lexie06"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie06", transition=fade)
    key "game_menu" action Hide("lexie06", transition=fade)

screen lexie07():
    add "lexie07"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie07", transition=fade)
    key "game_menu" action Hide("lexie07", transition=fade)


screen lexie08():
    add "lexie08"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie08", transition=fade)
    key "game_menu" action Hide("lexie08", transition=fade)

screen lexie09():
    add "lexie09"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie09", transition=fade)
    key "game_menu" action Hide("lexie09", transition=fade)

screen lexie10():
    add "lexie10"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie10", transition=fade)
    key "game_menu" action Hide("lexie10", transition=fade)

screen lexie11():
    add "lexie11"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie11", transition=fade)
    key "game_menu" action Hide("lexie11", transition=fade)

screen lexie12():
    add "lexie12"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie12", transition=fade)
    key "game_menu" action Hide("lexie12", transition=fade)

screen lexie13():
    add "lexie13"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie13", transition=fade)
    key "game_menu" action Hide("lexie13", transition=fade)

screen lexie13a():
    add "lexie13a"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie13a", transition=fade)
    key "game_menu" action Hide("lexie13a", transition=fade)

screen lexie13b():
    add "lexie13b"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie13b", transition=fade)
    key "game_menu" action Hide("lexie13b", transition=fade)

screen lexie13c():
    add "lexie13c"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie13c", transition=fade)
    key "game_menu" action Hide("lexie13c", transition=fade)

screen lexie13d():
    add "lexie13d"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie13d", transition=fade)
    key "game_menu" action Hide("lexie13d", transition=fade)

screen lexie13e():
    add "lexie13e"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie13e", transition=fade)
    key "game_menu" action Hide("lexie13e", transition=fade)

screen lexie14():
    add "lexie14" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("lexie14bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("lexie14", transition=fade)
    key "game_menu" action Hide("lexie14", transition=fade)


screen lexie14bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "lexie14"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("lexie14bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("lexie14bis", transition=fade)


screen lexie15():
    add "lexie15"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie15", transition=fade)
    key "game_menu" action Hide("lexie15", transition=fade)

screen lexie16():
    add "lexie16"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie16", transition=fade)
    key "game_menu" action Hide("lexie16", transition=fade)

screen lexie17():
    add "lexie17"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie17", transition=fade)
    key "game_menu" action Hide("lexie17", transition=fade)

screen lexie18():
    add "lexie18"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("lexie18", transition=fade)
    key "game_menu" action Hide("lexie18", transition=fade)









screen michelle01():
    add "michelle01" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("michelle01bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("michelle01", transition=fade)
    key "game_menu" action Hide("michelle01", transition=fade)

screen michelle01bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "michelle01"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("michelle01bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("michelle01bis", transition=fade)

screen michelle02():
    add "michelle02"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("michelle02", transition=fade)
    key "game_menu" action Hide("michelle02", transition=fade)

screen michelle03():
    add "michelle03"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("michelle03", transition=fade)
    key "game_menu" action Hide("michelle03", transition=fade)

screen michelle04():
    add "michelle04"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("michelle04", transition=fade)
    key "game_menu" action Hide("michelle04", transition=fade)


screen michelle05():
    add "michelle05"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("michelle05", transition=fade)
    key "game_menu" action Hide("michelle05", transition=fade)


screen michelle06():
    add "michelle06" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("michelle06bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("michelle06", transition=fade)
    key "game_menu" action Hide("michelle06", transition=fade)

screen michelle06bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "michelle06"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("michelle06bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("michelle06bis", transition=fade)
















screen marya01():
    add "marya01" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("marya01bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("marya01", transition=fade)
    key "game_menu" action Hide("marya01", transition=fade)

screen marya01bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "marya01"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("marya01bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("marya01bis", transition=fade)

screen marya02():
    add "marya02"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("marya02", transition=fade)
    key "game_menu" action Hide("marya02", transition=fade)

screen marya03():
    add "marya03"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("marya03", transition=fade)
    key "game_menu" action Hide("marya03", transition=fade)

screen marya04():
    add "marya04"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("marya04", transition=fade)
    key "game_menu" action Hide("marya04", transition=fade)

screen marya05():
    add "marya05"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("marya05", transition=fade)
    key "game_menu" action Hide("marya05", transition=fade)

screen marya06():
    add "marya06"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("marya06", transition=fade)
    key "game_menu" action Hide("marya06", transition=fade)

screen marya07():
    add "marya07" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("marya07bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("marya07", transition=fade)
    key "game_menu" action Hide("marya07", transition=fade)

screen marya07bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "marya07"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("marya07bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("marya07bis", transition=fade)

screen marya08():
    add "marya08"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("marya08", transition=fade)
    key "game_menu" action Hide("marya08", transition=fade)

screen marya09():
    add "marya09" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("marya09bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("marya09", transition=fade)
    key "game_menu" action Hide("marya09", transition=fade)

screen marya09bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "marya09"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("marya09bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("marya09bis", transition=fade)


screen marya10():
    add "marya10"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("marya10", transition=fade)
    key "game_menu" action Hide("marya10", transition=fade)



screen marya11():
    add "marya11"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("marya11", transition=fade)
    key "game_menu" action Hide("marya11", transition=fade)

screen marya12():
    add "marya12"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("marya12", transition=fade)
    key "game_menu" action Hide("marya12", transition=fade)

screen marya13():
    add "marya13"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("marya13", transition=fade)
    key "game_menu" action Hide("marya13", transition=fade)

screen marya14():
    add "marya14" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("marya14bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("marya14", transition=fade)
    key "game_menu" action Hide("marya14", transition=fade)

screen marya14bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "marya14"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("marya14bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("marya14bis", transition=fade)


















screen voyeur_01():
    add "voyeur_01"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("voyeur_01", transition=fade)
    key "game_menu" action Hide("voyeur_01", transition=fade)

screen voyeur_02():
    add "voyeur_02"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("voyeur_02", transition=fade)
    key "game_menu" action Hide("voyeur_02", transition=fade)

screen voyeur_03():
    add "voyeur_03"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("voyeur_03", transition=fade)
    key "game_menu" action Hide("voyeur_03", transition=fade)


screen copine01():
    add "copine01"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("copine01", transition=fade)
    key "game_menu" action Hide("copine01", transition=fade)

screen copine02():
    add "copine02"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("copine02", transition=fade)
    key "game_menu" action Hide("copine02", transition=fade)

screen copine03():
    add "copine03"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("copine03", transition=fade)
    key "game_menu" action Hide("copine03", transition=fade)

screen copine04():
    add "copine04"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("copine04", transition=fade)
    key "game_menu" action Hide("copine04", transition=fade)


screen rita01():
    add "rita01" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("rita01bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("rita01", transition=fade)
    key "game_menu" action Hide("rita01", transition=fade)

screen rita01bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "rita01"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("rita01bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("rita01bis", transition=fade)

screen rita02():
    add "rita02"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("rita02", transition=fade)
    key "game_menu" action Hide("rita02", transition=fade)

screen rita03():
    add "rita03"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("rita03", transition=fade)
    key "game_menu" action Hide("rita03", transition=fade)


screen jennifer01():
    add "jennifer01"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("jennifer01", transition=fade)
    key "game_menu" action Hide("jennifer01", transition=fade)

screen jennifer02():
    add "jennifer02"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("jennifer02", transition=fade)
    key "game_menu" action Hide("jennifer02", transition=fade)

screen jennifer03():
    add "jennifer03" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("jennifer03bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("jennifer03", transition=fade)
    key "game_menu" action Hide("jennifer03", transition=fade)

screen jennifer03bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "jennifer03"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("jennifer03bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("jennifer03bis", transition=fade)



screen melissa01():
    add "melissa01"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("melissa01", transition=fade)
    key "game_menu" action Hide("melissa01", transition=fade)


screen monique01():
    add "monique01"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("monique01", transition=fade)
    key "game_menu" action Hide("monique01", transition=fade)

screen monique02():
    add "monique02"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("monique02", transition=fade)
    key "game_menu" action Hide("monique02", transition=fade)


screen monique03():
    add "monique03"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("monique03", transition=fade)
    key "game_menu" action Hide("monique03", transition=fade)



screen monique04():
    add "monique04" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("monique04bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("monique04", transition=fade)
    key "game_menu" action Hide("monique04", transition=fade)

screen monique04bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "monique04"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("monique04bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("monique04bis", transition=fade)


screen monique05():
    add "monique05"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("monique05", transition=fade)
    key "game_menu" action Hide("monique05", transition=fade)





screen nicole01():
    add "nicole01"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("nicole01", transition=fade)
    key "game_menu" action Hide("nicole01", transition=fade)

screen nicole02():
    add "nicole02"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("nicole02", transition=fade)
    key "game_menu" action Hide("nicole02", transition=fade)

screen nicole03():
    add "nicole03"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("nicole03", transition=fade)
    key "game_menu" action Hide("nicole03", transition=fade)

screen nicole04():
    add "nicole04"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("nicole04", transition=fade)
    key "game_menu" action Hide("nicole04", transition=fade)


screen kateb01():
    add "kateb01" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("kateb01bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("kateb01", transition=fade)
    key "game_menu" action Hide("kateb01", transition=fade)

screen kateb01bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "kateb01"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("kateb01bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("kateb01bis", transition=fade)

screen kateb02():
    add "kateb02" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("kateb02bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("kateb02", transition=fade)
    key "game_menu" action Hide("kateb02", transition=fade)

screen kateb02bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "kateb02"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("kateb02bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("kateb02bis", transition=fade)

screen kateb03():
    add "kateb03"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("kateb03", transition=fade)
    key "game_menu" action Hide("kateb03", transition=fade)



screen kateb04():
    add "kateb04" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("kateb04bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("kateb04", transition=fade)
    key "game_menu" action Hide("kateb04", transition=fade)

screen kateb04bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "kateb04"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("kateb04bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("kateb04bis", transition=fade)





screen kate01():
    add "kate01" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("kate01bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("kate01", transition=fade)
    key "game_menu" action Hide("kate01", transition=fade)

screen kate01bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "kate01"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("kate01bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("kate01bis", transition=fade)



screen alex01():
    add "alex01" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("alex01bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("alex01", transition=fade)
    key "game_menu" action Hide("alex01", transition=fade)

screen alex01bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "alex01"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("alex01bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("alex01bis", transition=fade)

screen alex02():
    add "alex02"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("alex02", transition=fade)
    key "game_menu" action Hide("alex02", transition=fade)

screen alex03():
    add "alex03"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("alex03", transition=fade)
    key "game_menu" action Hide("alex03", transition=fade)

screen alex04():
    add "alex04"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("alex04", transition=fade)
    key "game_menu" action Hide("alex04", transition=fade)

screen alex05():
    add "alex05"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("alex05", transition=fade)
    key "game_menu" action Hide("alex05", transition=fade)

screen alex06():
    add "alex06"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("alex06", transition=fade)
    key "game_menu" action Hide("alex06", transition=fade)

screen alex07():
    add "alex07"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("alex07", transition=fade)
    key "game_menu" action Hide("alex07", transition=fade)

screen alex08():
    add "alex08"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("alex08", transition=fade)
    key "game_menu" action Hide("alex08", transition=fade)

screen alex09():
    add "alex09" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("alex09bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("alex09", transition=fade)
    key "game_menu" action Hide("alex09", transition=fade)

screen alex09bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "alex09"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("alex09bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("alex09bis", transition=fade)

screen alex10():
    add "alex10" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("alex10bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("alex10", transition=fade)
    key "game_menu" action Hide("alex10", transition=fade)

screen alex10bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "alex10"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("alex10bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("alex10bis", transition=fade)



screen alex11():
    add "alex11"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("alex11", transition=fade)
    key "game_menu" action Hide("alex11", transition=fade)


screen alex12():
    add "alex12" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("alex12bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("alex12", transition=fade)
    key "game_menu" action Hide("alex12", transition=fade)

screen alex12bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "alex12"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("alex12bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("alex12bis", transition=fade)

screen alex13():
    add "alex13" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("alex13bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("alex13", transition=fade)
    key "game_menu" action Hide("alex13", transition=fade)

screen alex13bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "alex13"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("alex13bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("alex13bis", transition=fade)


screen alex14():
    add "alex14"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("alex14", transition=fade)
    key "game_menu" action Hide("alex14", transition=fade)

screen alex15():
    add "alex15"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("alex15", transition=fade)
    key "game_menu" action Hide("alex15", transition=fade)

screen alex15male():
    add "alex15male"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("alex15male", transition=fade)
    key "game_menu" action Hide("alex15male", transition=fade)

screen alex16():
    add "alex16"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("alex16", transition=fade)
    key "game_menu" action Hide("alex16", transition=fade)

screen alex17():
    add "alex17"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("alex17", transition=fade)
    key "game_menu" action Hide("alex17", transition=fade)

screen alex18():
    add "alex18"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("alex18", transition=fade)
    key "game_menu" action Hide("alex18", transition=fade)

screen alex19():
    add "alex19"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("alex19", transition=fade)
    key "game_menu" action Hide("alex19", transition=fade)

screen alex20():
    add "alex20" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("alex20bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("alex20", transition=fade)
    key "game_menu" action Hide("alex20", transition=fade)

screen alex20bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "alex20"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("alex20bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("alex20bis", transition=fade)




















































screen amal01():
    add "amal01"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("amal01", transition=fade)
    key "game_menu" action Hide("amal01", transition=fade)


screen amal02():
    add "amal02" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("amal02bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("amal02", transition=fade)
    key "game_menu" action Hide("amal02", transition=fade)

screen amal02bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "amal02"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("amal02bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("amal02bis", transition=fade)

screen amal03():
    add "amal03"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("amal03", transition=fade)
    key "game_menu" action Hide("amal03", transition=fade)

screen amal04():
    add "amal04"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("amal04", transition=fade)
    key "game_menu" action Hide("amal04", transition=fade)


screen greta01():
    add "greta01"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("greta01", transition=fade)
    key "game_menu" action Hide("greta01", transition=fade)


screen greta02():
    add "greta02" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("greta02bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("greta02", transition=fade)
    key "game_menu" action Hide("greta02", transition=fade)

screen greta02bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "greta02"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("greta02bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("greta02bis", transition=fade)

screen greta03():
    add "greta03"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("greta03", transition=fade)
    key "game_menu" action Hide("greta03", transition=fade)

screen greta04():
    add "greta04"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("greta04", transition=fade)
    key "game_menu" action Hide("greta04", transition=fade)





screen julienne01():
    add "julienne01" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("julienne01bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("julienne01", transition=fade)
    key "game_menu" action Hide("julienne01", transition=fade)

screen julienne01bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "julienne01"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("julienne01bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("julienne01bis", transition=fade)

screen julienne02():
    add "julienne02"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("julienne02", transition=fade)
    key "game_menu" action Hide("julienne02", transition=fade)

screen julienne03():
    add "julienne03"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("julienne03", transition=fade)
    key "game_menu" action Hide("julienne03", transition=fade)

screen julienne04():
    add "julienne04"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("julienne04", transition=fade)
    key "game_menu" action Hide("julienne04", transition=fade)

screen julienne05():
    add "julienne05"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("julienne05", transition=fade)
    key "game_menu" action Hide("julienne05", transition=fade)

screen julienne06():
    add "julienne06"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("julienne06", transition=fade)
    key "game_menu" action Hide("julienne06", transition=fade)



screen vanille01():
    add "vanille01"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("vanille01", transition=fade)
    key "game_menu" action Hide("vanille01", transition=fade)


screen vanille02():
    add "vanille02" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("vanille02bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("vanille02", transition=fade)
    key "game_menu" action Hide("vanille02", transition=fade)

screen vanille02bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "vanille02"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("vanille02bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("vanille02bis", transition=fade)

screen vanille03():
    add "vanille03"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("vanille03", transition=fade)
    key "game_menu" action Hide("vanille03", transition=fade)

screen vanille04():
    add "vanille04"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("vanille04", transition=fade)
    key "game_menu" action Hide("vanille04", transition=fade)

screen vanille05():
    add "vanille05" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("vanille05bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("vanille05", transition=fade)
    key "game_menu" action Hide("vanille05", transition=fade)

screen vanille05bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "vanille05"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("vanille05bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("vanille05bis", transition=fade)



screen vanille06():
    add "vanille06"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("vanille06", transition=fade)
    key "game_menu" action Hide("vanille06", transition=fade)


screen vanille07():
    add "vanille07" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("vanille07bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("vanille07", transition=fade)
    key "game_menu" action Hide("vanille07", transition=fade)

screen vanille07bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "vanille07"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("vanille07bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("vanille07bis", transition=fade)





screen carolina01():
    add "carolina01" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("carolina01bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("carolina01", transition=fade)
    key "game_menu" action Hide("carolina01", transition=fade)

screen carolina01bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "carolina01"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("carolina01bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("carolina01", transition=fade)


screen carolina02():
    add "carolina02" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("carolina02bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("carolina02", transition=fade)
    key "game_menu" action Hide("carolina02", transition=fade)

screen carolina02bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "carolina02"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("carolina02bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("carolina02", transition=fade)

screen carolina03():
    add "carolina03"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("carolina03", transition=fade)
    key "game_menu" action Hide("carolina03", transition=fade)







screen guliana01():
    add "guliana01" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("guliana01bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("guliana01", transition=fade)
    key "game_menu" action Hide("guliana01", transition=fade)

screen guliana01bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "guliana01"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("guliana01bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("guliana01", transition=fade)





screen madison01():
    add "madison01"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("madison01", transition=fade)
    key "game_menu" action Hide("madison01", transition=fade)


screen madison02():
    add "madison02" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("madison02bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("madison02", transition=fade)
    key "game_menu" action Hide("madison02", transition=fade)

screen madison02bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "madison02"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("madison02bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("madison02bis", transition=fade)

screen madison03():
    add "madison03"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("madison03", transition=fade)
    key "game_menu" action Hide("madison03", transition=fade)

screen madison04():
    add "madison04"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("madison04", transition=fade)
    key "game_menu" action Hide("madison04", transition=fade)

screen madison05():
    add "madison05"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("madison05", transition=fade)
    key "game_menu" action Hide("madison05", transition=fade)

screen madison06():
    add "madison06" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("madison06bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("madison06", transition=fade)
    key "game_menu" action Hide("madison06", transition=fade)

screen madison06bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "madison06"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("madison06bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("madison06bis", transition=fade)





















screen wonderland_01():
    add "wonderland_01"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("wonderland_01", transition=fade)
    key "game_menu" action Hide("wonderland_01", transition=fade)

screen wonderland_02():
    add "wonderland_02"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("wonderland_02", transition=fade)
    key "game_menu" action Hide("wonderland_02", transition=fade)

screen wonderland_03():
    add "wonderland_03"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("wonderland_03", transition=fade)
    key "game_menu" action Hide("wonderland_03", transition=fade)

screen wonderland_04():
    add "wonderland_04"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("wonderland_04", transition=fade)
    key "game_menu" action Hide("wonderland_04", transition=fade)

screen wonderland_05():
    add "wonderland_05"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("wonderland_05", transition=fade)
    key "game_menu" action Hide("wonderland_05", transition=fade)






screen jennifer01_2000():
    add "jennifer01_2000" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("jennifer01bis_2000", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("jennifer01_2000", transition=fade)
    key "game_menu" action Hide("jennifer01_2000", transition=fade)

screen jennifer01bis_2000():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "jennifer01_2000"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("jennifer01bis_2000", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("jennifer01bis_2000", transition=fade)


screen jennifer02_2000():
    add "jennifer02_2000" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("jennifer02bis_2000", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("jennifer02_2000", transition=fade)
    key "game_menu" action Hide("jennifer02_2000", transition=fade)

screen jennifer02bis_2000():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "jennifer02_2000"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("jennifer02bis_2000", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("jennifer02bis_2000", transition=fade)


screen jennifer03_2000():
    add "jennifer03_2000" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("jennifer03bis_2000", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("jennifer03_2000", transition=fade)
    key "game_menu" action Hide("jennifer03_2000", transition=fade)

screen jennifer03bis_2000():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "jennifer03_2000"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("jennifer03bis_2000", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("jennifer03bis_2000", transition=fade)


screen jennifer04_2000():
    add "jennifer04_2000" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("jennifer04bis_2000", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("jennifer04_2000", transition=fade)
    key "game_menu" action Hide("jennifer04_2000", transition=fade)

screen jennifer04bis_2000():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "jennifer04_2000"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("jennifer04bis_2000", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("jennifer04bis_2000", transition=fade)


screen jennifer05_2000():
    add "jennifer05_2000" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("jennifer05bis_2000", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("jennifer05_2000", transition=fade)
    key "game_menu" action Hide("jennifer05_2000", transition=fade)

screen jennifer05bis_2000():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "jennifer05_2000"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("jennifer05bis_2000", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("jennifer05bis_2000", transition=fade)


screen jennifer06_2000():
    add "jennifer06_2000"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("jennifer06_2000", transition=fade)
    key "game_menu" action Hide("jennifer06_2000", transition=fade)







screen nicole01_2000():
    add "nicole01_2000"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("nicole01_2000", transition=fade)
    key "game_menu" action Hide("nicole01_2000", transition=fade)

screen nicole02_2000():
    add "nicole02_2000" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("nicole02bis_2000", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("nicole02_2000", transition=fade)
    key "game_menu" action Hide("nicole02_2000", transition=fade)

screen nicole02bis_2000():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "nicole02_2000"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("nicole02bis_2000", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("nicole02bis_2000", transition=fade)

screen nicole03_2000():
    add "nicole03_2000"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("nicole03_2000", transition=fade)
    key "game_menu" action Hide("nicole03_2000", transition=fade)






screen mia01():
    add "mia01"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("mia01", transition=fade)
    key "game_menu" action Hide("mia01", transition=fade)

screen mia02():
    add "mia02"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("mia02", transition=fade)
    key "game_menu" action Hide("mia02", transition=fade)




screen ameria01():
    add "ameria01"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("ameria01", transition=fade)
    key "game_menu" action Hide("ameria01", transition=fade)

screen ameria02():
    add "ameria02"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("ameria02", transition=fade)
    key "game_menu" action Hide("ameria02", transition=fade)

screen ameria03():
    add "ameria03"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("ameria03", transition=fade)
    key "game_menu" action Hide("ameria03", transition=fade)

screen ameria04():
    add "ameria04" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("ameria04_bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("ameria04", transition=fade)
    key "game_menu" action Hide("ameria04", transition=fade)

screen ameria04_bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "ameria04"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("ameria04_bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("ameria04_bis", transition=fade)


screen ameria05():
    add "ameria05"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("ameria05", transition=fade)
    key "game_menu" action Hide("ameria05", transition=fade)

screen ameria06():
    add "ameria06"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("ameria06", transition=fade)
    key "game_menu" action Hide("ameria06", transition=fade)

screen ameria07():
    add "ameria07"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("ameria07", transition=fade)
    key "game_menu" action Hide("ameria07", transition=fade)

screen ameria08():
    add "ameria08"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("ameria08", transition=fade)
    key "game_menu" action Hide("ameria08", transition=fade)

screen ameria09():
    add "ameria09"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("ameria09", transition=fade)
    key "game_menu" action Hide("ameria09", transition=fade)

screen ameria10():
    add "ameria10"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("ameria10", transition=fade)
    key "game_menu" action Hide("ameria10", transition=fade)





screen mizuki01():
    add "mizuki01"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("mizuki01", transition=fade)
    key "game_menu" action Hide("mizuki01", transition=fade)

screen mizuki02():
    add "mizuki02"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("mizuki02", transition=fade)
    key "game_menu" action Hide("mizuki02", transition=fade)

screen mizuki03():
    add "mizuki03"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("mizuki03", transition=fade)
    key "game_menu" action Hide("mizuki03", transition=fade)

screen mizuki04():
    add "mizuki04" at look
    imagebutton:
        idle "gui/extra_exit_idle.webp"
        action Show("mizuki04_bis", transition=fade)
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("mizuki04", transition=fade)
    key "game_menu" action Hide("mizuki04", transition=fade)

screen mizuki04_bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "mizuki04"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("mizuki04_bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"

    key "game_menu" action Hide("mizuki04_bis", transition=fade)


screen mizuki05():
    add "mizuki05"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("mizuki05", transition=fade)
    key "game_menu" action Hide("mizuki05", transition=fade)

screen mizuki06():
    add "mizuki06"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("mizuki06", transition=fade)
    key "game_menu" action Hide("mizuki06", transition=fade)

screen mizuki07():
    add "mizuki07"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("mizuki07", transition=fade)
    key "game_menu" action Hide("mizuki07", transition=fade)

screen mizuki08():
    add "mizuki08"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("mizuki08", transition=fade)
    key "game_menu" action Hide("mizuki08", transition=fade)

screen mizuki09():
    add "mizuki09"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("mizuki09", transition=fade)
    key "game_menu" action Hide("mizuki09", transition=fade)

screen mizuki10():
    add "mizuki10"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("mizuki10", transition=fade)
    key "game_menu" action Hide("mizuki10", transition=fade)

screen mizuki11():
    add "mizuki11"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("mizuki11", transition=fade)
    key "game_menu" action Hide("mizuki11", transition=fade)

screen mizuki12():
    add "mizuki12"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("mizuki12", transition=fade)
    key "game_menu" action Hide("mizuki12", transition=fade)

screen mizuki13():
    add "mizuki13"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("mizuki13", transition=fade)
    key "game_menu" action Hide("mizuki13", transition=fade)

screen mizuki14():
    add "mizuki14"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("mizuki14", transition=fade)
    key "game_menu" action Hide("mizuki14", transition=fade)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
