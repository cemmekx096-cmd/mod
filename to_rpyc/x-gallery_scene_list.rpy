



define gallery_scenes = [
    
    
    

    GalleryScene(
        kind="scene",
        chapter=1,
        name=_("Ian watches porn"),
        img="gallery/thumb_v1_ianfap.webp",
        param="gallery_CH01_S01",
        unlocked_if="gallery_scene_unlocked('CH01_S01')",
        chars=['Ian'],
        scope=coreScope
    ),

    GalleryScene( 
        kind="image",
        chapter=1,
        name=_("Ivy sends a nude to Jeremy"),
        img="gallery/thumb_v1_selfiejeremy.webp",
        param=["v1_selfiejeremy"],
        unlocked_if="renpy.seen_image('v1_selfiejeremy')",
        chars=['Ivy']
    ),

    GalleryScene(
        kind="scene",
        chapter=1,
        name=_("Shower time"),
        img="gallery/thumb_v1_lena_shower.webp",
        update_logic=lambda:"gallery/thumb_v1_lena_shower_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v1_lena_shower_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v1_lena_shower_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v1_lena_shower.webp",
        param="gallery_CH01_I01",
        unlocked_if="renpy.seen_image('v1_lena_shower')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=1,
        name=_("First pole dance lesson"),
        img="gallery/thumb_v1_pole2.webp",
        textInv = True,
        param="gallery_CH01_S02",
        unlocked_if="gallery_scene_unlocked('CH01_S02')",
        chars=['Lena', 'Ivy'],
        scope=merge_two_dicts({
            'ian_active': False,
            'ivy_navel': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=1,
        name=_("Photo shoot with Danny"),
        img="gallery/thumb_v1_pose1.webp",
        textInv = True,
        param="gallery_CH01_S03",
        unlocked_if="gallery_scene_unlocked('CH01_S03')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=1,
        name=_("Ian goes to a life drawing event"),
        img="gallery/thumb_v2_lenadraw1.webp",
        param="gallery_CH01_S04",
        unlocked_if="gallery_scene_unlocked('CH01_S04')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    
    
    
    
    GalleryScene( 
        kind="image",
        chapter=2,
        name=_("Ian and Perry look up Lena's PG"),
        img="gallery/thumb_v1_peoplegram.webp",
        param=["v1_peoplegram", "v1_pg2", "v1_pg3b"],
        unlocked_if="renpy.seen_image('v1_pg3')",
        chars=['Lena']
    ),

    GalleryScene(
        kind="image",
        chapter=2,
        name=_("Alison sends a selfie to Ian"),
        img="gallery/thumb_v2_alison_selfie1.webp",
        param=["v2_alison_selfie1"],
        unlocked_if="renpy.seen_image('v2_alison_selfie1')",
        chars=['Alison']
    ),

    GalleryScene( 
        kind="image",
        chapter=2,
        name=_("Alison sends a selfie to Jeremy"),
        img="gallery/thumb_v2_alison_selfie2.webp",
        param=["v2_alison_selfie2"],
        unlocked_if="renpy.seen_image('v2_alison_selfie2')",
        chars=['Alison']
    ),

    GalleryScene(
        kind="scene",
        chapter=2,
        name=_("Ivy shows StalkFap during pole dance"),
        img="gallery/thumb_v2_pole1.webp",
        textInv = True,
        param="gallery_CH02_S01",
        unlocked_if="gallery_scene_unlocked('CH02_S01')",
        chars=['Lena', 'Ivy'],
        scope=merge_two_dicts({
            'ian_active': False,
            'ivy_navel': False,
            'v1_talk_ivy': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=2,
        name=_("Lena agrees to drinks"),
        img="gallery/thumb_v2_robert5.webp",
        param="gallery_CH02_S03",
        unlocked_if="gallery_scene_unlocked('CH02_S03')",
        chars=['Lena', 'Robert'],
        scope=merge_two_dicts({
            'ian_active': False,
            'lena_robert': 5
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=2,
        name=_("The morning after"),
        img="gallery/thumb_v2_robert6.webp",
        textInv = True,
        param="gallery_CH02_S04",
        unlocked_if="gallery_scene_unlocked('CH02_S04')",
        chars=['Lena', 'Robert'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v2_robert_home': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=2,
        name=_("Third pole dance lesson"),
        img="gallery/thumb_v2_gym.webp",
        textInv = True,
        param="gallery_CH02_S05",
        unlocked_if="gallery_scene_unlocked('CH02_S05')",
        chars=['Lena', 'Ivy'],
        scope=merge_two_dicts({
            'ian_active': False,
            'ivy_navel': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=2,
        name=_("Ian brings Cherry home after the bar"),
        img="gallery/thumb_v2_cherry5.webp",
        param="gallery_CH02_S06",
        unlocked_if="gallery_scene_unlocked('CH02_S06')",
        chars=['Ian', 'Cherry'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=2,
        name=_("Ian brings Alison home after the bar"),
        img="gallery/thumb_v2_alison5.webp",
        param="gallery_CH02_S07",
        unlocked_if="gallery_scene_unlocked('CH02_S07')",
        chars=['Ian', 'Alison'],
        scope=coreScope
    ),

    
    
    
    
    GalleryScene(
        kind="image",
        chapter=3,
        name=_("Ivy posts on StalkFap"),
        img="gallery/thumb_v3_ivyselfie1.webp",
        param=["v3_ivyselfie1"],
        unlocked_if="renpy.seen_image('v3_stalkfap1')",
        chars=['Ivy']
    ),

    GalleryScene(
        kind="image",
        chapter=3,
        name=_("Lena kisses Ian"),
        img="gallery/thumb_v2_ian_kiss2b.webp",
        param=["v2_ian_kiss1b", "v2_ian_kiss2b"],
        unlocked_if="renpy.seen_image('v2_ian_kiss2') or renpy.seen_image('v2_ian_kiss2b')",
        chars=['Lena', 'Ian']
    ),

    GalleryScene(
        kind="scene",
        chapter=3,
        name=_("Lena has sex after her date"),
        img="gallery/thumb_v3_robert10b.webp",
        textInv = True,
        param="gallery_CH03_S01",
        unlocked_if="gallery_scene_unlocked('CH03_S01')",
        chars=['Lena', 'Robert'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v2_robert_bj': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=3,
        name=_("Lena spies on Louise and Jeremy"),
        img="gallery/thumb_v3_louise1.webp",
        param="gallery_CH03_S02",
        unlocked_if="gallery_scene_unlocked('CH03_S02')",
        chars=['Louise', 'Jeremy'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=3,
        name=_("Lena agrees to model for Stan"),
        img="gallery/thumb_v3_stan2.webp",
        textInv = True,
        param="gallery_CH03_S08",
        unlocked_if="gallery_scene_unlocked('CH03_S08')",
        chars=['Lena', 'Stan'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v2_stan_model': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=3,
        name=_("Cherry wakes up Ian"),
        img="gallery/thumb_v3_cherry1.webp",
        textInv = True,
        param="gallery_CH03_S03",
        unlocked_if="gallery_scene_unlocked('CH03_S03')",
        chars=['Ian', 'Cherry'],
        scope=coreScope
    ),

    GalleryScene(
        kind="image",
        chapter=3,
        name=_("Ian looks at Cherry's Peoplegram"),
        img="gallery/thumb_v3_peoplegram_cherry1.webp",
        param=["v3_peoplegram_cherry1b", "v3_peoplegram_cherry2"],
        unlocked_if="renpy.seen_image('v3_peoplegram_cherry2')",
        chars=['Cherry']
    ),

    GalleryScene( 
        kind="image",
        chapter=3,
        name=_("Ian looks at Cindy's Peoplegram"),
        img="gallery/thumb_v3_cindy_peoplegram.webp",
        param=["v3_cindy_peoplegram"],
        unlocked_if="renpy.seen_image('v3_cindy_peoplegram')",
        chars=['Cindy']
    ),

    GalleryScene(
        kind="image",
        chapter=3,
        name=_("Ian thinks of Gillian"),
        img="gallery/thumb_v3_gillian3.webp",
        param=["v3_gillian1", "v3_gillian2", "v3_gillian3"],
        unlocked_if="renpy.seen_image('v3_gillian3')",
        chars=['Gillian']
    ),

    GalleryScene( 
        kind="image",
        chapter=3,
        name=_("Alison sends a nude to Ian"),
        img="gallery/thumb_v3_alison_selfie.webp",
        param=["v3_alison_selfie"],
        unlocked_if="renpy.seen_image('v3_alison_selfie')",
        chars=['Alison']
    ),

    GalleryScene(
        kind="scene",
        chapter=3,
        name=_("Ian goes on a date"),
        img="gallery/thumb_v3_alison7.webp",
        param="gallery_CH03_S04",
        unlocked_if="gallery_scene_unlocked('CH03_S04')",
        chars=['Ian', 'Alison'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=3,
        name=_("Lena masturbates"),
        img="gallery/thumb_v3_solo1.webp",
        textInv = True,
        param="gallery_CH03_S05",
        unlocked_if="gallery_scene_unlocked('CH03_S05')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v3_spy': True,
            'v3_spy_full': True, 
            'v2_ian_date': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=3,
        name=_("Lena calls Robert over"),
        img="gallery/thumb_v3_robert4.webp",
        textInv = True,
        param="gallery_CH03_S06",
        unlocked_if="gallery_scene_unlocked('CH03_S06')",
        chars=['Lena', 'Robert'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v2_robert_home': True
        })
    ),

    
    
    
    
    GalleryScene( 
        kind="image",
        chapter=4,
        name=_("Ivy shows Jeremy's nude"),
        img="gallery/thumb_v5_jeremy_selfie.webp",
        param=["v5_jeremy_selfie"],
        unlocked_if="renpy.seen_image('v5_jeremy_selfie')",
        chars=['Jeremy']
    ),

    GalleryScene(
        kind="scene",
        chapter=4,
        name=_("Lena agrees to a photo shoot with Seymour"),
        img="gallery/thumb_v4_seymour6.webp",
        param="gallery_CH04_S01",
        unlocked_if="gallery_scene_unlocked('CH04_S01')",
        chars=['Lena', 'Seymour'],
        scope=merge_two_dicts({
            'ian_active': False,
            'lena_posh': 2,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=4,
        name=_("Lena masturbates 2"),
        img="gallery/thumb_v4_solo1.webp",
        textInv = True,
        param="gallery_CH04_S02",
        unlocked_if="gallery_scene_unlocked('CH04_S02')",
        chars=['Lena', 'Axel'],
        scope=merge_two_dicts({
            'v2_ian_date': True,
            'v3_robert_repeat': False,
            'v3_spy': True,
            'v4_seymour_date': True,
            'seymour_shoot': 4,
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=4,
        name=_("Lena blows Robert at work"),
        img="gallery/thumb_v4_restaurant2.webp",
        param="gallery_CH04_S03",
        unlocked_if="gallery_scene_unlocked('CH04_S03')",
        chars=['Lena', 'Robert'],
        scope=merge_two_dicts({
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene( 
        kind="image",
        chapter=4,
        name=_("Alison sends a boob pic to Ian"),
        img="gallery/thumb_v4_alison_selfie.webp",
        param=["v4_alison_selfie"],
        unlocked_if="renpy.seen_image('v4_alison_selfie')",
        chars=['Alison']
    ),

    GalleryScene( 
        kind="image",
        chapter=4,
        name=_("Cherry sends a nude to Ian"),
        img="gallery/thumb_v3_peoplegram_cherry2b.webp",
        param=["v3_peoplegram_cherry2b"],
        unlocked_if="renpy.seen_image('v3_peoplegram_cherry2b')",
        chars=['Cherry']
    ),

    GalleryScene( 
        kind="image",
        chapter=4,
        name=_("Louise's private nudes"),
        img="gallery/thumb_v4_louise_selfie1.webp",
        param=["v4_louise_selfie1", "v4_louise_selfie2", "v4_louise_selfie3"],
        unlocked_if="renpy.seen_image('v4_louise_selfie3')",
        chars=['Louise', 'Jeremy']
    ),

    GalleryScene( 
        kind="image",
        chapter=4,
        name=_("Jeremy shares Alison's titfuck"),
        img="gallery/thumb_v4_alison_jeremy.webp",
        param=["v4_alison_jeremy"],
        unlocked_if="renpy.seen_image('v4_alison_jeremy')",
        chars=['Alison', 'Jeremy']
    ),

    GalleryScene(
        kind="scene",
        chapter=4,
        name=_("Holly joins the pole dance lesson"),
        img="gallery/thumb_v4_gym_holly1.webp",
        textInv = True,
        param="gallery_CH04_S04",
        unlocked_if="gallery_scene_unlocked('CH04_S04')",
        chars=['Lena', 'Holly', 'Ivy'],
        scope=merge_two_dicts({
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=4,
        name=_("Lena invites Ian over"),
        img="gallery/thumb_v4_lena6.webp",
        param="gallery_CH04_S06",
        unlocked_if="gallery_scene_unlocked('CH04_S06')",
        chars=['Lena', 'Ian'],
        scope=merge_two_dicts({
            'ian_active': False,
            'scene_protection': True
        })
    ),

    
    
    
    
    GalleryScene(
        kind="scene",
        chapter=5,
        name=_("Ian goes to Cindy's photo shoot"),
        img="gallery/thumb_v5_cindy7b.webp",
        textInv = True,
        param="gallery_CH05_S01",
        unlocked_if="gallery_scene_unlocked('CH05_S01')",
        chars=['Cindy'],
        scope=merge_two_dicts({'scene_protection': True})
    ),

    GalleryScene(
        kind="scene",
        chapter=5,
        name=_("Ivy performs at the club"),
        img="gallery/thumb_v5_ivy1.webp",
        param="gallery_CH05_S02",
        unlocked_if="gallery_scene_unlocked('CH05_S02')",
        chars=['Ivy'],
        scope=merge_two_dicts({'scene_protection': True})
    ),

    GalleryScene(
        kind="scene",
        chapter=5,
        name=_("Ian brings Emma home after dancing"),
        img="gallery/thumb_v5_emma5.webp",
        param="gallery_CH05_S03",
        unlocked_if="gallery_scene_unlocked('CH05_S03')",
        chars=['Ian', 'Emma'],
        scope=merge_two_dicts({
            'alison_jeremy': True,
            'ian_alison_sex': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=5,
        name=_("Ian brings Alison home after dancing"),
        img="gallery/thumb_v5_alison3.webp",
        param="gallery_CH05_S04",
        unlocked_if="gallery_scene_unlocked('CH05_S04')",
        chars=['Ian', 'Alison'],
        scope=merge_two_dicts({
            'v5_perry_club': False,
            'scene_protection': True
        })
    ),

    GalleryScene( 
        kind="image",
        chapter=5,
        name=_("Jeremy shares his sex tape"),
        img="gallery/thumb_v5_voyeur1.webp",
        param=["alison_voyeur_v5"],
        unlocked_if="renpy.seen_image('v5_voyeur4')",
        chars=['Alison', 'Jeremy']
    ),

    GalleryScene( 
        kind="image",
        chapter=5,
        name=_("Lena took stalkfap more seriously"),
        img="gallery/thumb_v5_stalkfap1.webp",
        param=["v5_stalkfap1"],
        unlocked_if="renpy.seen_image('v5_stalkfap1_comp') or renpy.seen_image('v5_stalkfap1')",
        chars=['Lena']
    ),

    GalleryScene(
        kind="scene",
        chapter=5,
        name=_("Louise seeks comfort"),
        img="gallery/thumb_v5_louise1.webp",
        param="gallery_CH05_S05",
        unlocked_if="gallery_scene_unlocked('CH05_S05')",
        chars=['Lena', 'Louise'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v4_confront_louise': True,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=5,
        name=_("Lena brings Mike home from the club"),
        img="gallery/thumb_v5_mike5c.webp",
        param="gallery_CH05_S06",
        unlocked_if="gallery_scene_unlocked('CH05_S06')",
        chars=['Lena', 'Mike'],
        scope=merge_two_dicts({
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=5,
        name=_("Lena needs more professional pictures"),
        img="gallery/thumb_v5_model2b.webp",
        textInv = True,
        param="gallery_CH05_S07",
        unlocked_if="gallery_scene_unlocked('CH05_S07') or gallery_scene_unlocked('CH05_S08')",
        chars=['Lena', 'Stan'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v3_stan_shoot': 3,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=5,
        name=_("Robert sexts with Lena"),
        img="gallery/thumb_v5_sexting2.webp",
        param="gallery_CH05_S09",
        unlocked_if="gallery_scene_unlocked('CH05_S09')",
        chars=['Lena', 'Robert'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v4_robert_sex': True,
            'scene_protection': True
        })
    ),

    GalleryScene( 
        kind="image",
        chapter=5,
        name=_("Lena posted another selfie"),
        img="gallery/thumb_v5_stalkfap2.webp",
        param=["v5_stalkfap2", "v5_stalkfap2b"],
        unlocked_if="renpy.seen_image('v5_stalkfap2') or renpy.seen_image('v5_stalkfap2b')",
        chars=['Lena']
    ),

    
    
    
    
    GalleryScene( 
        kind="image",
        chapter=6,
        name=_("Cindy's modeling pics"),
        img="gallery/thumb_v6_cindy_pic2a.webp",
        param=["v6_cindy_pic1", "v6_cindy_pic2a", "v6_cindy_pic2b"],
        unlocked_if="renpy.seen_image('v6_cindy_pic1') or renpy.seen_image('v6_cindy_pg2b')",
        chars=['Cindy']
    ),

    GalleryScene( 
        kind="image",
        chapter=6,
        name=_("Ian asks Cindy for another one"),
        img="gallery/thumb_v6_cindy_pic3.webp",
        param=["v6_cindy_pic3"],
        unlocked_if="renpy.seen_image('v6_cindy_pic3')",
        chars=['Cindy']
    ),

    GalleryScene( 
        kind="image",
        chapter=6,
        name=_("Cherry texts Ian"),
        img="gallery/thumb_v6_cherry_selfie.webp",
        param=["v6_cherry_selfie"],
        unlocked_if="renpy.seen_image('v6_cherry_selfie')",
        chars=['Cherry']
    ),

    GalleryScene( 
        kind="image",
        chapter=6,
        name=_("Perry shows Ivy's Peoplegram"),
        img="gallery/thumb_v6_ivy_pg.webp",
        param=["v6_ivy_pgb"],
        unlocked_if="renpy.seen_image('v6_ivy_pg')",
        chars=['Ivy']
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Ian takes Alison home after the bar"),
        img="gallery/thumb_v6_alison5.webp",
        param="gallery_CH06_S01",
        unlocked_if="gallery_scene_unlocked('CH06_S01')",
        chars=['Ian', 'Alison'],
        scope=merge_two_dicts({
            'v6_rightaway': 'alison',
            'ian_alison_like': 2,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Ian takes Cherry home after bar"),
        img="gallery/thumb_v6_cherry3.webp",
        param="gallery_CH06_S02",
        unlocked_if="gallery_scene_unlocked('CH06_S02')",
        chars=['Ian', 'Cherry'],
        scope=merge_two_dicts({
            'v6_rightaway': 'cherry',
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Lena & Ian have sex after date"),
        img="gallery/thumb_v6_lena3.webp",
        param="gallery_CH06_S03",
        unlocked_if="gallery_scene_unlocked('CH06_S03')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts({
            'lena_bj': 5,
            'scene_protection': True
        })
    ),
    
    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Ian hatefucks Minerva"),
        img="gallery/thumb_v6_minerva5.webp",
        param="gallery_CH06_S04",
        unlocked_if="gallery_scene_unlocked('CH06_S04')",
        chars=['Ian', 'Minerva'],
        scope=merge_two_dicts({
            'holly_gym': True,
            'scene_protection': True
        })
    ),

    GalleryScene( 
        kind="scene",
        chapter=6,
        name=_("Lena rewarded Ian / Teased Mike or Robert"),
        img="gallery/thumb_v6_lena_selfie1.webp",
        param="gallery_CH06_S15",
        unlocked_if="gallery_scene_unlocked('CH06_S15')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene( 
        kind="image",
        chapter=6,
        name=_("Lena decides to please her fans"),
        img="gallery/thumb_v6_stalkfap2.webp",
        param=["v6_stalkfap2"],
        unlocked_if="renpy.seen_image('v6_stalkfap2')",
        chars=['Lena']
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Pole dance lesson 5"),
        img="gallery/thumb_v6_gym_ivy.webp",
        textInv = True,
        param="gallery_CH06_S05",
        unlocked_if="gallery_scene_unlocked('CH06_S05')",
        chars=['Lena', 'Holly', 'Ivy'],
        scope=merge_two_dicts({
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Holly gets kissed"),
        img="gallery/thumb_v6_holly2_ivy.webp",
        textInv = True,
        param="gallery_CH06_S06",
        unlocked_if="gallery_scene_unlocked('CH06_S06')",
        chars=['Lena', 'Holly', 'Ivy'],
        scope=merge_two_dicts({
            'ian_active': False,
            'cheat_mode': True,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Lena is awakened by Louise"),
        img="gallery/thumb_v6_louise1.webp",
        param="gallery_CH06_S07",
        unlocked_if="gallery_scene_unlocked('CH06_S07')",
        chars=['Lena', 'Louise'],
        scope=merge_two_dicts({
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene( 
        kind="image",
        chapter=6,
        name=_("Lena checks Ivy's Stalkfap posts"),
        img="gallery/thumb_v6_stalkfap_ivy1.webp",
        param=["v6_stalkfap_ivy1","v6_stalkfap_ivy2", "v6_stalkfap_twerk"],
        unlocked_if="renpy.seen_image('v6_stalkfap_ivy2')",
        chars=['Ivy']
    ),
    
    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Lena masturbates 3"),
        img="gallery/thumb_v4_solo2.webp",
        param="gallery_CH06_S08",
        unlocked_if="gallery_scene_unlocked('CH06_S08')",
        chars=['Lena', 'Jeremy', 'Louise'],
        scope=merge_two_dicts({
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Lena invited Mike over"),
        img="gallery/thumb_v6_mike2.webp",
        param="gallery_CH06_S09",
        unlocked_if="gallery_scene_unlocked('CH06_S09')",
        chars=['Lena', 'Mike'],
        scope=merge_two_dicts({
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Robert comes back from his trip"),
        img="gallery/thumb_v6_robert1.webp",
        param="gallery_CH06_S10",
        unlocked_if="gallery_scene_unlocked('CH06_S10')",
        chars=['Lena', 'Robert'],
        scope=merge_two_dicts({
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Lena invited Ian over"),
        img="gallery/thumb_v6_ian4b.webp",
        param="gallery_CH06_S11",
        unlocked_if="gallery_scene_unlocked('CH06_S11')",
        chars=['Lena', 'Ian'],
        scope=merge_two_dicts({
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Lena wakes Robert with a bj"),
        img="gallery/thumb_v2_robert7.webp",
        textInv = True,
        param="gallery_CH06_S12",
        unlocked_if="gallery_scene_unlocked('CH06_S12')",
        chars=['Lena', 'Robert'],
        scope=merge_two_dicts({
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=6,
        name=_("Lena has a photo shoot with Axel"),
        img="gallery/thumb_v6_axel4.webp",
        param="gallery_CH06_S13",
        unlocked_if="gallery_scene_unlocked('CH06_S13') or gallery_scene_unlocked('CH06_S14')",
        chars=['Lena', 'Axel', 'Seymour'],
        scope=merge_two_dicts({
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene( 
        kind="image",
        chapter=6,
        name=_("Ivy shows her tattoo"),
        img="gallery/thumb_v6_ivy_tattoo.webp",
        param=["v6_ivy_tattoo"],
        unlocked_if="renpy.seen_image('v6_ivy_tattoo')",
        chars=['Ivy']
    ),

    
    
    
    
    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Ian masturbates to nudes"),
        img="gallery/thumb_v7_jerkoff1.webp",
        param="gallery_CH07_S01",
        unlocked_if="gallery_scene_unlocked('CH07_S01')",
        chars=['Ian'],
        scope=merge_two_dicts({'scene_protection': True})
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Ian asks Jeremy for more"),
        img="gallery/thumb_v7_alisonbbc1.webp",
        param="gallery_CH07_S20",
        unlocked_if="gallery_scene_unlocked('CH07_S20')",
        chars=['Alison', 'Jeremy'],
        scope=merge_two_dicts({
            'v1_encourage_alison': True,
            'ian_alison_dating': False,
            'ian_alison_sex': False,
            'v3_alison_boobjob': False,
            'v5_alison_boobjob': False,
            'ian_alison_like': 0,
            'v6_alison_extra_pic': False,
            'v6_alison_cum': False,
            'v2_alison_home': False,
            'alison_voyeur': True,
            'v5_alison_jeremy': True,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Cindy's second photo shoot"),
        img="gallery/thumb_v7_cindy_pic2.webp",
        param="gallery_CH07_S21",
        unlocked_if="gallery_scene_unlocked('CH07_S21')",
        chars=['Cindy'],
        scope=merge_two_dicts({
            'ian_cindy_model': True,
            'ian_go_cindy': 3,
            'v5_cindy_shoot': True,
            'wade_cindy': 0,
            'v5_cindy_nude': 2,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Minerva needs Ian"),
        img="gallery/thumb_v7_minerva3.webp",
        param="gallery_CH07_S02",
        unlocked_if="gallery_scene_unlocked('CH07_S02')",
        chars=['Ian', 'Minerva'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Ian visits Lena's life drawing"),
        img="gallery/thumb_v7_drawing1a.webp",
        param="gallery_CH07_S03",
        unlocked_if="gallery_scene_unlocked('CH07_S03')",
        chars=['Lena'],
        scope=merge_two_dicts({'scene_protection': True})
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Lena had a sexy dream"),
        img="gallery/thumb_v7_dream2.webp",
        textInv = True,
        param="gallery_CH07_S04",
        unlocked_if="gallery_scene_unlocked('CH07_S04')",
        chars=['Lena', 'Axel'],
        scope=merge_two_dicts({
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Lena goes to another life drawing"),
        img="gallery/thumb_v7_drawing4a.webp",
        param="gallery_CH07_S05",
        unlocked_if="gallery_scene_unlocked('CH07_S05')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Lena takes Robert home after life drawing"),
        img="gallery/thumb_v7_robert1.webp",
        param="gallery_CH07_S06",
        unlocked_if="gallery_scene_unlocked('CH07_S06')",
        chars=['Lena', 'Robert'],
        scope=merge_two_dicts({
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Lena goes with Ian after life drawing"),
        img="gallery/thumb_v7_lena2.webp",
        param="gallery_CH07_S07",
        unlocked_if="gallery_scene_unlocked('CH07_S07')",
        chars=['Lena', 'Ian'],
        scope=merge_two_dicts({
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("The morning after life drawing with Robert"),
        img="gallery/thumb_v7_robert4.webp",
        param="gallery_CH07_S08",
        unlocked_if="gallery_scene_unlocked('CH07_S08')",
        chars=['Lena', 'Robert'],
        scope=merge_two_dicts({
            'ian_active': False,
            'lena_robert_dating': True,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("The morning after life drawing with Ian"),
        img="gallery/thumb_v7_lena8b.webp",
        param="gallery_CH07_S18",
        unlocked_if="gallery_scene_unlocked('CH07_S18')",
        chars=['Lena', 'Ian'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v7_ian_date': True,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Lena masturbates after her dream"),
        img="gallery/thumb_v7_solo1.webp",
        param="gallery_CH07_S19",
        unlocked_if="gallery_scene_unlocked('CH07_S19')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False,
            'lena_axel_desire': True,
            'scene_protection': True
        })
    ),

    GalleryScene( 
        kind="image",
        chapter=7,
        name=_("Ivy shows off Mark"),
        img="gallery/thumb_v7_mark.webp",
        param=["v7_mark"],
        unlocked_if="renpy.seen_image('v7_mark')",
        chars=['Mark']
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Lena visits Mike at his dj booth"),
        img="gallery/thumb_v7_mike1a.webp",
        param="gallery_CH07_S09",
        unlocked_if="gallery_scene_unlocked('CH07_S09')",
        chars=['Lena', 'Mike'],
        scope=merge_two_dicts({
            'v7mikemusic': 'latin',
            'lena_wardrobe_charisma1': True,
            'lena_wardrobe_athletics1': True,
            'lena_wardrobe_wits1': True,
            'lena_wardrobe_lust1': True,
            'lena_mike_dating': True,
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Lena catches Louise masturbating"),
        img="gallery/thumb_v7_louise1c.webp",
        param="gallery_CH07_S10",
        unlocked_if="gallery_scene_unlocked('CH07_S10')",
        chars=['Lena', 'Louise'],
        scope=merge_two_dicts({
            'lena_louise_sex': True,
            'lena_wardrobe_charisma1': True,
            'lena_wardrobe_athletics1': True,
            'lena_wardrobe_wits1': True,
            'lena_wardrobe_lust1': True,
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Party with Ivy, Jeremy, and Louise"),
        img="gallery/thumb_v7_ivy3.webp",
        param="gallery_CH07_S11",
        unlocked_if="gallery_scene_unlocked('CH07_S11')",
        chars=['Lena', 'Ivy', 'Jeremy', 'Louise'],
        scope=merge_two_dicts({
            'v3_spy_full': True,
            'lena_bbc': True,
            'lena_axel_desire': True,
            'lena_wardrobe_charisma1': True,
            'lena_wardrobe_athletics1': True,
            'lena_wardrobe_wits1': True,
            'lena_wardrobe_lust1': True,
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Lena records a video for Stalkfap"),
        img="gallery/thumb_v7_dance3.webp",
        param="gallery_CH07_S12",
        unlocked_if="gallery_scene_unlocked('CH07_S12')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'stan_simp': 1,
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Emma visits before Wade's b-day party"),
        img="gallery/thumb_v7_emma2.webp",
        param="gallery_CH07_S13",
        unlocked_if="gallery_scene_unlocked('CH07_S13')",
        chars=['Ian', 'Emma'],
        scope=merge_two_dicts({'scene_protection': True})
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Alison visits before Wade's b-day party"),
        img="gallery/thumb_v7_alison2.webp",
        param="gallery_CH07_S14",
        unlocked_if="gallery_scene_unlocked('CH07_S14')",
        chars=['Ian', 'Alison'],
        scope=merge_two_dicts({
            'alison_sexy': 2,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Ian follows Cindy after her argument"),
        img="gallery/thumb_v7_cindy10.webp",
        param="gallery_CH07_S15",
        unlocked_if="gallery_scene_unlocked('CH07_S15')",
        chars=['Ian', 'Cindy'],
        scope=merge_two_dicts({
            'ian_go_cindy': True,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Ian goes with Holly to the bookfair"),
        img="gallery/thumb_v7_holly4.webp",
        param="gallery_CH07_S16",
        unlocked_if="gallery_scene_unlocked('CH07_S16')",
        chars=['Ian', 'Holly'],
        scope=merge_two_dicts({
            'v7_effort_holly': True,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=7,
        name=_("Lena indulges her curiosity"),
        img="gallery/thumb_v7_solo_bbc2.webp",
        textInv = True,
        param="gallery_CH07_S17",
        unlocked_if="gallery_scene_unlocked('CH07_S17')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'v7_game': True,
            'cafe_music': True,
            'ian_active': False,
            'scene_protection': True
        })
    ),

    
    
    
    
    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("The morning after"),
        img="gallery/thumb_v8_hotel1.webp",
        param="gallery_CH08_S01",
        unlocked_if="gallery_scene_unlocked('CH08_S01')",
        chars=['Ian', 'Holly'],
        scope=merge_two_dicts({
            'v7_holly_bj': True,
            'v7_holly_rough': True,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Lena has sex at the restaurant"),
        img="gallery/thumb_v8_robert1.webp",
        param="gallery_CH08_S02",
        unlocked_if="gallery_scene_unlocked('CH08_S02')",
        chars=['Lena', 'Robert'],
        scope=merge_two_dicts({
            'v8_robert_public': True,
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene( 
        kind="image",
        chapter=8,
        name=_("Ivy's Peoplegram photos"),
        img="gallery/thumb_v8_ivy_pg1.webp",
        param=["v8_ivy_pg1","v8_ivy_pg2"],
        unlocked_if="renpy.seen_image('v8_ivy_pg2')",
        chars=['Ivy']
    ),

    GalleryScene( 
        kind="image",
        chapter=8,
        name=_("Ed gives Lena his drawing"),
        img="gallery/thumb_v8_ed_drawing.webp",
        param=["v8_ed_drawing"],
        unlocked_if="renpy.seen_image('v8_ed_drawing')",
        chars=['Lena']
    ),

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Lena bought something for Louise"),
        img="gallery/thumb_v8_louise1.webp",
        param="gallery_CH08_S03",
        unlocked_if="gallery_scene_unlocked('CH08_S03')",
        chars=['Lena', 'Louise'],
        scope=merge_two_dicts({
            'v6_louise_orgasm': True,
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Lena sexts with fans and friends"),
        img="gallery/thumb_v8_sexting2.webp",
        param="gallery_CH08_S04",
        unlocked_if="gallery_scene_unlocked('CH08_S04')",
        chars=['Lena', 'Ian', 'Jeremy', 'Mike', 'Robert'],
        scope=merge_two_dicts({
            'lena_money': 3,
            'ian_active': False,
            'scene_protection': True
        })
    ),

    

    GalleryScene( 
        kind="image",
        chapter=8,
        name=_("Alison sends Ian a present at work"),
        img="gallery/thumb_v8_selfie_alison1.webp",
        param=["v8_selfie_alison1"],
        unlocked_if="renpy.seen_image('v8_selfie_alison1')",
        chars=['Alison']
    ),

    GalleryScene( 
        kind="image",
        chapter=8,
        name=_("Jeremy shares a pic of him and Emma"),
        img="gallery/thumb_v8_emma_jeremy.webp",
        param=["v8_emma_jeremy"],
        unlocked_if="renpy.seen_image('v8_emma_jeremy')",
        chars=['Jeremy', 'Emma']
    ),

    GalleryScene( 
        kind="image",
        chapter=8,
        name=_("Ian sexts with Alison"),
        img="gallery/thumb_v8_selfie_alison3.webp",
        param=["v8_selfie_alison3","v8_selfie_alison4", "v8_selfie_alison5", "v8_selfie_dick"],
        unlocked_if="renpy.seen_image('v8_selfie_alison5')",
        chars=['Ian','Alison']
    ),

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Ian goes into Minerva's office"),
        img="gallery/thumb_v8_minerva1.webp",
        param="gallery_CH08_S05",
        unlocked_if="gallery_scene_unlocked('CH08_S05')",
        chars=['Ian', 'Minerva'],
        scope=merge_two_dicts({
            'ian_minerva_sex': True,
            'v7_minerva_sex': True,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Sex after the concert"),
        img="gallery/thumb_v8_lena2.webp",
        param="gallery_CH08_S06",
        unlocked_if="gallery_scene_unlocked('CH08_S06')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts({
            'ian_lena_sex_late': False,
            'v7_cindy_kiss': False,
            'ian_lena_love': True,
            'lena_ian_love': True,
            'lena_bj': 4,
            'ian_dirty_talk': 2,
            'lena_wardrobe_wits1': True,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="image",
        chapter=8,
        name=_("Ian teases Cherry"),
        img="gallery/thumb_v8_selfie_cherry.webp",
        param=["v8_sexting_ian","v8_selfie_cherry"],
        unlocked_if="renpy.seen_image('v8_selfie_cherry')",
        chars=['Ian', 'Cherry']
    ),

    GalleryScene( 
        kind="image",
        chapter=8,
        name=_("Ian shows Axel's PG to his friends"),
        img="gallery/thumb_v9_axel_pg1.webp",
        param=["v9_axel_pg1", "v9_axel_pg2"],
        unlocked_if="renpy.seen_image('v9_axel_pg2')",
        chars=['Axel']
    ),

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Ian walks in on Perry & Emma"),
        img="gallery/thumb_v8_perry.webp",
        param="gallery_CH08_S08",
        unlocked_if="gallery_scene_unlocked('CH08_S08')",
        chars=['Emma', 'Perry'],
        scope=merge_two_dicts({'scene_protection': True})
    ),

    

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Lena invites Mike over"),
        img="gallery/thumb_v8_mike1.webp",
        param="gallery_CH08_S11",
        unlocked_if="gallery_scene_unlocked('CH08_S11')",
        chars=['Lena', 'Mike'],
        scope=merge_two_dicts({
            'v8_lena_sexting': 'mike',
            'v7_mike_bj': True,
            'mike_dirty_talk': 2,
            'lena_anal_first': 'mike',
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Lena wakes up Jeremy"),
        img="gallery/thumb_v8_jeremy1.webp",
        param="gallery_CH08_S09",
        unlocked_if="gallery_scene_unlocked('CH08_S09')",
        chars=['Lena', 'Jeremy'],
        scope=merge_two_dicts({
            'lena_bbc': True,
            'v3_spy_full': True,
            'v7_bbc_cum': True,
            'ian_active': False,
            'scene_protection': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("The girls have a drink"),
        img="gallery/thumb_v8_ivy3.webp",
        param="gallery_CH08_S10",
        unlocked_if="gallery_scene_unlocked('CH08_S10')",
        chars=['Lena', 'Holly', 'Ivy'],
        scope=merge_two_dicts({
            'ian_ivy': 5,
            'lena_go_holly': 3,
            'holly_change': 2,
            'lena_bdick': 3,
            'lena_axel_desire': True,
            'holly_gym': True,
            'v6_holly_kiss': 'lena',
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Holly goes home with Lena"),
        img="gallery/thumb_v8_holly3.webp",
        update_logic=lambda:"gallery/thumb_v8_holly3_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v8_holly3_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v8_holly3_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v8_holly3.webp",
        param="gallery_CH08_S12",
        unlocked_if="gallery_scene_unlocked('CH08_S12')",
        chars=['Lena', 'Holly'],
        scope=merge_two_dicts({
            'lena_go_holly': 3,
            'holly_change': 2,
            'holly_gym': True,
            'v6_holly_kiss': 'lena',
            'ian_active': False
        })
    ),

    

    GalleryScene(
        kind="scene",
        chapter=8,
        name=_("Emma wakes Ian after doing drugs"),
        img="gallery/thumb_v8_emma1.webp",
        param="gallery_CH08_S07",
        unlocked_if="gallery_scene_unlocked('CH08_S07')",
        chars=['Ian', 'Emma'],
        scope=merge_two_dicts({
            'v8_trip': True,
            'v7_emma_bj': True
        })
    ),

    
    
    

    GalleryScene( 
        kind="image",
        chapter=9,
        name=_("Lena kept Ian's shirt"),
        img="gallery/thumb_v9_lena_selfie1.webp",
        update_logic=lambda:"gallery/thumb_v9_lena_selfie1_t13.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo3 else "gallery/thumb_v9_lena_selfie1_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v9_lena_selfie1_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v9_lena_selfie1.webp",
        param=["v9_lena_selfie1_comp"],
        unlocked_if="renpy.seen_image('v9_lena_selfie1_comp')",
        chars=['Lena']
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Holly gives Ian a blowjob"),
        img="gallery/thumb_v9_holly4.webp",
        param="gallery_CH09_S01",
        unlocked_if="gallery_scene_unlocked('CH09_S01')",
        chars=['Ian', 'Holly'],
        scope=merge_two_dicts({
            'holly_change': 3,
            'ian_chad': 4,
            'v8_holly_bj': True,
            'holly_look': '1skirt'
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Ian texts Emma"),
        img="gallery/thumb_v9_emma2.webp",
        param="gallery_CH09_S13",
        unlocked_if="gallery_scene_unlocked('CH09_S13')",
        chars=['Ian', 'Emma'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Ian texts Jeremy"),
        img="gallery/thumb_v9_emma6.webp",
        param="gallery_CH09_S14",
        unlocked_if="gallery_scene_unlocked('CH09_S14')",
        chars=['Emma', 'Jeremy'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Ian confesses to Cherry"),
        img="gallery/thumb_v9_cherry5.webp",
        param="gallery_CH09_S02",
        unlocked_if="gallery_scene_unlocked('CH09_S02')",
        chars=['Ian', 'Cherry'],
        scope=merge_two_dicts({
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True,
            'v6_cherry_anal': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Ian accompanies Alison on her trip"),
        img="gallery/thumb_v9_alison13.webp",
        textInv = True,
        param="gallery_CH09_S03",
        unlocked_if="gallery_scene_unlocked('CH09_S03')",
        chars=['Ian', 'Alison'],
        scope=merge_two_dicts({
            'alison_sexy': 2,
            'alison_extras': 1,
            'ian_alison_like': 2,
            'alison_satisfaction': 5,
            'v6_alison_cum': True,
            'v8_alison_sext': 3,
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True
        })
    ),

    GalleryScene( 
        kind="image",
        chapter=9,
        name=_("Holly steps out of her comfort zone"),
        img="gallery/thumb_v9_holly_selfie1.webp",
        param=["v9_holly_selfie1"],
        unlocked_if="renpy.seen_image('v9_holly_selfie1')",
        chars=['Holly']
    ),

    GalleryScene( 
        kind="image",
        chapter=9,
        name=_("Holly misses Ian"),
        img="gallery/thumb_v9_holly_selfie2.webp",
        param=["v9_holly_selfie2"],
        unlocked_if="renpy.seen_image('v9_holly_selfie2')",
        chars=['Holly']
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Ian welcomes Lena back"),
        img="gallery/thumb_v9_lena8a.webp",
        update_logic=lambda:"gallery/thumb_v9_lena8a_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v9_lena8a_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v9_lena8a_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v9_lena8a.webp",
        param="gallery_CH09_S04",
        unlocked_if="gallery_scene_unlocked('CH09_S04')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts({
            'ian_lena_couple': True,
            'ian_lena_sex': True,
            'lena_bj': 4,
            'ian_chad': 4
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Jeremy sends a video from Alison's trip"),
        img="gallery/thumb_v9_bbc2.webp",
        param="gallery_CH09_S05",
        unlocked_if="gallery_scene_unlocked('CH09_S05')",
        chars=['Alison', 'Billy', 'Jeremy'],
        scope=merge_two_dicts({
            'alison_sexy': 2,
            'v9alisonphone': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Ian accompanies Cindy to Axel's shoot"),
        img="gallery/thumb_v9_cindy_shoot1b.webp",
        param="gallery_CH09_S06",
        unlocked_if="gallery_scene_unlocked('CH09_S06')",
        chars=['Axel', 'Cindy'],
        scope=merge_two_dicts({
            'v5_cindy_shoot': True,
            'v5_cindy_nude': 2,
            'v7_axel_date': True,
            'ian_cindy_model': True,
            'v7_cindy_kiss': True,
            'ian_cindy_sex': True,
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Ian confesses to Cindy"),
        img="gallery/thumb_v9_cindy6.webp",
        param="gallery_CH09_S07",
        unlocked_if="gallery_scene_unlocked('CH09_S07')",
        chars=['Ian', 'Cindy'],
        scope=merge_two_dicts({
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True
        })
    ),

    GalleryScene( 
        kind="image",
        chapter=9,
        name=_("Lena posted to Stalkfap"),
        img="gallery/thumb_v9_stalkfap1.webp",
        update_logic=lambda:"gallery/thumb_v9_stalkfap1_t123.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v9_stalkfap1_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v9_stalkfap1_t13.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo3 else "gallery/thumb_v9_stalkfap1_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v9_stalkfap1_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v9_stalkfap1_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v9_stalkfap1_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v9_stalkfap1.webp",
        param=["v9_stalkfap1"],
        unlocked_if="renpy.seen_image('v9_stalkfap1')",
        chars=['Lena']
    ),

    GalleryScene( 
        kind="image",
        chapter=9,
        name=_("Lena's home videos"),
        img="gallery/thumb_v9_stalkfap2.webp",
        update_logic=lambda:"gallery/thumb_v9_stalkfap2_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v9_stalkfap2.webp",
        param=["v9_stalkfap2", "v9_stalkfap3", "v9_stalkfap4", "v9_stalkfap5"],
        unlocked_if="renpy.seen_image('v9_stalkfap5')",
        chars=['Lena']
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Robert helps Lena unpack"),
        img="gallery/thumb_v9_robert1.webp",
        update_logic=lambda:"gallery/thumb_v9_robert1_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v9_robert1.webp",
        param="gallery_CH09_S08",
        unlocked_if="gallery_scene_unlocked('CH09_S08')",
        chars=['Lena', 'Robert'],
        scope=merge_two_dicts({'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Mike helps Lena unpack"),
        img="gallery/thumb_v9_mike2.webp",
        param="gallery_CH09_S09",
        unlocked_if="gallery_scene_unlocked('CH09_S09')",
        chars=['Lena', 'Mike'],
        scope=merge_two_dicts({
            'lena_anal': 2,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Lena poses for Axel"),
        img="gallery/thumb_v9_lena_shoot3b.webp",
        update_logic=lambda:"gallery/thumb_v9_lena_shoot3b_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v9_lena_shoot3b_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v9_lena_shoot3b_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v9_lena_shoot3b.webp",
        param="gallery_CH09_S10",
        unlocked_if="gallery_scene_unlocked('CH09_S10')",
        chars=['Lena', 'Axel'],
        scope=merge_two_dicts({
            'v6_axel_pose': 3,
            'axel_disposition': 2,
            'axel_pictures_watch': True,
            'lena_axel_desire': True,
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Lena submits to Axel"),
        img="gallery/thumb_v9_axel6a.webp",
        param="gallery_CH09_S11",
        unlocked_if="gallery_scene_unlocked('CH09_S11')",
        chars=['Lena', 'Axel'],
        scope=merge_two_dicts({
            'v6_axel_pose': 3,
            'axel_disposition': 2,
            'axel_pictures_watch': True,
            'lena_axel_desire': True,
            'ian_active': False
        })
    ),

    GalleryScene( 
        kind="scene",
        chapter=9,
        name=_("Holly greets Ivy"),
        img="gallery/thumb_v9_holly8.webp",
        textInv = True,
        param="gallery_CH09_S15",
        unlocked_if="gallery_scene_unlocked('CH09_S15')",
        chars=['Holly', 'Ivy'],
        scope=merge_two_dicts({'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=9,
        name=_("Lena signs the contract"),
        img="gallery/thumb_v9_seymour3.webp",
        update_logic=lambda:"gallery/thumb_v9_seymour3_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v9_seymour3_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v9_seymour3_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v9_seymour3.webp",
        param="gallery_CH09_S12",
        unlocked_if="gallery_scene_unlocked('CH09_S12')",
        chars=['Lena', 'Seymour'],
        scope=merge_two_dicts({
            'seymour_disposition': 3,
            'ian_active': False
        })
    ),

    
    
    

    
    
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Ian pays to see Lena's exclusive content"),
        img="gallery/thumb_v10_stalkfap2c.webp",
        update_logic=lambda:"gallery/thumb_v10_stalkfap2c_t123.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v10_stalkfap2c_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v10_stalkfap2c_t13.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo3 else "gallery/thumb_v10_stalkfap2c_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v10_stalkfap2c_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v10_stalkfap2c_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v10_stalkfap2c_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v10_stalkfap2c.webp",
        param="gallery_CH10_S19",
        unlocked_if="gallery_scene_unlocked('CH10_S19')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_lena_couple': True,
            'stalkfap': True,
            'ian_stalkfap': True,
            'stalkfap_pro': 2,
            'v7_dance': 2,
            'v7_dance_provoke': 3
        })
    ),

    GalleryScene(
        kind="image",
        chapter=10,
        name=_("Ian teases the ladies"),
        img="gallery/thumb_v10_selfie_ian.webp",
        param=["v10_selfie_ian"],
        unlocked_if="renpy.seen_image('v10_selfie_ian')",
        chars=['Ian']
    ),

    GalleryScene( 
        kind="image",
        chapter=10,
        name=_("Alison responds to teasing"),
        img="gallery/thumb_v10_selfie_alison.webp",
        param=["v10_selfie_alison"],
        unlocked_if="renpy.seen_image('v10_selfie_alison')",
        chars=['Alison']
    ),

    GalleryScene( 
        kind="image",
        chapter=10,
        name=_("Cherry rewards a caring Ian"),
        img="gallery/thumb_v10_selfie_cherry.webp",
        param=["v10_selfie_cherry"],
        unlocked_if="renpy.seen_image('v10_selfie_cherry')",
        chars=['Cherry']
    ),

    GalleryScene( 
        kind="image",
        chapter=10,
        name=_("Cindy responds to teasing"),
        img="gallery/thumb_v10_selfie_cindy1.webp",
        param=["v10_selfie_cindy1"],
        unlocked_if="renpy.seen_image('v10_selfie_cindy1')",
        chars=['Cindy']
    ),

    GalleryScene( 
        kind="image",
        chapter=10,
        name=_("Holly gives something in return"),
        img="gallery/thumb_v10_selfie_holly.webp",
        param=["v10_selfie_holly"],
        unlocked_if="renpy.seen_image('v10_selfie_holly')",
        chars=['Holly']
    ),

    GalleryScene( 
        kind="image",
        chapter=10,
        name=_("Lena says good night"),
        img="gallery/thumb_v10_selfie_lena1.webp",
        update_logic=lambda:"gallery/thumb_v10_selfie_lena1_t123.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v10_selfie_lena1_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v10_selfie_lena1_t13.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo3 else "gallery/thumb_v10_selfie_lena1_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v10_selfie_lena1_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v10_selfie_lena1_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v10_selfie_lena1_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v10_selfie_lena1.webp",
        param=["v10_selfie_lena1"],
        unlocked_if="renpy.seen_image('v10_selfie_lena1')",
        chars=['Lena']
    ),
    
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Ian and Holly stop by Ian's place"),
        img="gallery/thumb_v10_holly8.webp",
        textInv = True,
        param="gallery_CH10_S04",
        unlocked_if="gallery_scene_unlocked('CH10_S04')",
        chars=['Ian', 'Holly'],
        scope=merge_two_dicts({
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True,
            'holly_change': 3
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Ian brings Lena home after the park"),
        img="gallery/thumb_v10_ian4.webp",
        update_logic=lambda:"gallery/thumb_v10_ian4_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v10_ian4_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v10_ian4_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v10_ian4.webp",
        param="gallery_CH10_S02",
        unlocked_if="gallery_scene_unlocked('CH10_S02')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts({
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True
        })
    ),
    
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Ian looks up Jess online"),
        img="gallery/thumb_v10_jess0.webp",
        param="gallery_CH10_S01",
        unlocked_if="gallery_scene_unlocked('CH10_S01')",
        chars=['Jessica'],
        scope=merge_two_dicts({
            'v10_text_jess': 3
        })
    ),
    
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Ian meets Minerva after work"),
        img="gallery/thumb_v10_minerva2.webp",
        param="gallery_CH10_S21",
        unlocked_if="gallery_scene_unlocked('CH10_S21')",
        chars=['Ian', 'Minerva'],
        scope=merge_two_dicts({
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True,
            'v8_minerva_sex': True
        })
    ),
    
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Ian wrestles with Ivy"),
        img="gallery/thumb_v10_ivy_gym2.webp",
        textInv = True,
        param="gallery_CH10_S05",
        unlocked_if="gallery_scene_unlocked('CH10_S05')",
        chars=['Ian', 'Ivy'],
        scope=merge_two_dicts({'jiujitsu': 4})
    ),

    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Emma ambushes Ian in the restroom"),
        img="gallery/thumb_v10_emma1.webp",
        param="gallery_CH10_S06",
        unlocked_if="gallery_scene_unlocked('CH10_S06')",
        chars=['Ian', 'Emma'],
        scope=merge_two_dicts({
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True,
            'ian_lena_dating': True,
            'emma_jeremy': True,
            'v9_emma_sext': 2,
            'emma_satisfaction': 1
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Ian goes with Lena after the concert"),
        img="gallery/thumb_v10_ian7.webp",
        param="gallery_CH10_S20",
        unlocked_if="gallery_scene_unlocked('CH10_S20')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts({
            'cafe_help': True,
            'stalkfap': True,
            'ian_stalkfap': 2,
            'ian_lena_couple': True,
            'ian_lena_sex': True,
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True
        })
    ),
    
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Cindy and Ian have an overdue talk"),
        img="gallery/thumb_v10_cindy9.webp",
        param="gallery_CH10_S03",
        unlocked_if="gallery_scene_unlocked('CH10_S03')",
        chars=['Ian', 'Cindy'],
        scope=merge_two_dicts({
            'v10_text_cindy': True,
            'cindy_satisfaction': 3,
            'v9cindycunnilingus': True
        })
    ),

    GalleryScene(
        kind="image",
        chapter=10,
        name=_("Cindy promises to meet again soon"),
        img="gallery/thumb_v10_selfie_cindy2.webp",
        param=["v10_selfie_cindy2"],
        unlocked_if="renpy.seen_image('v10_selfie_cindy2')",
        chars=['Cindy']
    ),
    
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Ian has a threesome with Alison and Jeremy"),
        img="gallery/thumb_v10_alison1.webp",
        param="gallery_CH10_S07",
        unlocked_if="gallery_scene_unlocked('CH10_S07')",
        chars=['Ian', 'Alison', 'Jeremy'],
        scope=merge_two_dicts({
            'alison_jeremy_3some': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Ian goes over for lunch to Alison's"),
        img="gallery/thumb_v10_alisonian4.webp",
        param="gallery_CH10_S17",
        unlocked_if="gallery_scene_unlocked('CH10_S17')",
        chars=['Ian', 'Alison'],
        scope=merge_two_dicts({
            'ian_alison_love': True,
            'v9_alison_trip': True,
            'v10ianshoppedwine': True,
            'v10_wine': True
        })
    ),

    
    
    GalleryScene(
        kind="image",
        chapter=10,
        name=_("Mike teases Lena during the concert"),
        img="gallery/thumb_v10_selfie_mike.webp",
        param=["v10_selfie_mike"],
        unlocked_if="renpy.seen_image('v10_selfie_mike')",
        chars=['Mike']
    ),

    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Lena invites Mike after the concert"),
        img="gallery/thumb_v10_mike5.webp",
        update_logic=lambda:"gallery/thumb_v10_mike5_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v10_mike5_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v10_mike5_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v10_mike5.webp",
        param="gallery_CH10_S18",
        unlocked_if="gallery_scene_unlocked('CH10_S18')",
        chars=['Lena', 'Mike'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v10_lena_sex': 0,
            'lena_mike_love': True,
            'v9_axel_sex': True
        })
    ),

    GalleryScene( 
        kind="scene",
        chapter=10,
        name=_("Lena gives Louise some much needed attention"),
        img="gallery/thumb_v10_louise2.webp",
        update_logic=lambda:"gallery/thumb_v10_louise2_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v10_louise2_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v10_louise2_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v10_louise2.webp",
        param="gallery_CH10_S12",
        unlocked_if="gallery_scene_unlocked('CH10_S12')",
        chars=['Lena', 'Louise'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v5_louise_orgasm': True,
            'v6_louise_orgasm': True,
            'v8_louise_sex': True
        })
    ),
    
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Lena thinks about Axel"),
        img="gallery/thumb_v10_axel1.webp",
        update_logic=lambda:"gallery/thumb_v10_axel1_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v10_axel1_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v10_axel1_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v10_axel1.webp",
        textInv = True,
        param="gallery_CH10_S15",
        unlocked_if="gallery_scene_unlocked('CH10_S15')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v10_axel_text': 1,
            'v9_axel_sex': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Holly has her first shoot"),
        img="gallery/thumb_v10_holly11.webp",
        param="gallery_CH10_S08",
        unlocked_if="gallery_scene_unlocked('CH10_S08')",
        chars=['Lena', 'Holly', 'Ivy'],
        scope=merge_two_dicts({
            'ian_active': False,
            'lena_go_holly': 4
        })
    ),

    GalleryScene(
        kind="image",
        chapter=10,
        name=_("Holly goes with Mark"),
        img="gallery/thumb_v10_holly_mark.webp",
        param=["v10_holly_mark"],
        unlocked_if="renpy.seen_image('v10_holly_mark')",
        chars=['Holly', 'Mark']
    ),

    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Lena and her dance partner need to cool off"),
        img="gallery/thumb_v10_wc3_dress.webp",
        param="gallery_CH10_S09",
        unlocked_if="gallery_scene_unlocked('CH10_S09')",
        chars=['Lena', 'Ian', 'Mark', 'Mike'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v10_lena_drug': True,
            'billy_model': True,
            'billy_trust': 1,
            'lena_mike_dating': True,
            'v10_mark_flirt': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_lust1': True,
            'lena_wardrobe_black_dress': True,
            'lena_wardrobe_wits1': True,
            'lena_wardrobe_athletics1': True,
            'lena_wardrobe_charisma1': True,
            'lena_wardrobe_lust1': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Lena goes home with the birthday girl"),
        img="gallery/thumb_v10_ivy4.webp",
        textInv = True,
        param="gallery_CH10_S10",
        unlocked_if="gallery_scene_unlocked('CH10_S10')",
        chars=['Lena', 'Ivy'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v10_lena_drug': True,
            'v8_holly_sex': 'lenaivy'
        })
    ),
    
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Shoot for Stalkfap"),
        img="gallery/thumb_v10_shoot1_stan.webp",
        param="gallery_CH10_S13",
        unlocked_if="gallery_scene_unlocked('CH10_S13')",
        chars=['Lena', 'Ian', 'Mike', 'Stan'],
        scope=merge_two_dicts({
            'ian_active': False,
            'lena_wardrobe_bunny': True,
            'lena_wardrobe_lingerie': True,
            'stalkfap_pro': 2
        })
    ),
    
    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Lena finally gets another professional shoot"),
        img="gallery/thumb_v10_shooting1.webp",
        update_logic=lambda:"gallery/thumb_v10_shooting1_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v10_shooting1.webp",
        param="gallery_CH10_S14",
        unlocked_if="gallery_scene_unlocked('CH10_S14')",
        chars=['Lena', "Seymour"],
        scope=merge_two_dicts({'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=10,
        name=_("Lena has a threesome with Louise and Jeremy"),
        img="gallery/thumb_v10_jeremy2.webp",
        update_logic=lambda:"gallery/thumb_v10_jeremy2_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v10_jeremy2.webp",
        param="gallery_CH10_S11",
        unlocked_if="gallery_scene_unlocked('CH10_S11')",
        chars=['Lena', 'Jeremy','Louise'],
        scope=merge_two_dicts({'ian_active': False})
    ),

    
    
    

    
    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena uses Louise for pleasure"),
        img="gallery/thumb_v11_louise1.webp",
        update_logic=lambda:"gallery/thumb_v11_louise1_t13.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo3 else "gallery/thumb_v11_louise1_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v11_louise1_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v11_louise1.webp",
        param="gallery_CH11_S01",
        unlocked_if="gallery_scene_unlocked('CH11_S01')",
        chars=['Lena', 'Louise'],
        scope=merge_two_dicts({
            'ian_active': False,
            'toy_double': True
        })
    ),
    
    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Ian invites Lena to dinner"),
        img="gallery/thumb_v11_ian2.webp",
        update_logic=lambda:"gallery/thumb_v11_ian2_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v11_ian2_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v11_ian2_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v11_ian2.webp",
        param="gallery_CH11_S02",
        unlocked_if="gallery_scene_unlocked('CH11_S02')",
        chars=['Lena', 'Ian'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v11iandinner': True,
            'cafe_help': True
        })
    ),

    
    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Ian dreams of Gillian"),
        img="gallery/thumb_v11_gillian1.webp",
        param="gallery_CH11_S03",
        unlocked_if="gallery_scene_unlocked('CH11_S03')",
        chars=['Gillian'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Cindy invites Ian when Wade is away"),
        img="gallery/thumb_v11_cindy2.webp",
        textInv = True,
        param="gallery_CH11_S04",
        unlocked_if="gallery_scene_unlocked('CH11_S04')",
        chars=['Ian', 'Cindy'],
        scope=merge_two_dicts({
            'ian_cindy_love': True,
            'v10_cindy_bj': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Ian and Holly meet up before Emma's event"),
        img="gallery/thumb_v11_holly1b.webp",
        textInv = True,
        param="gallery_CH11_S05",
        unlocked_if="gallery_scene_unlocked('CH11_S05')",
        chars=['Ian', 'Holly'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Ian and Alison look at art"),
        img="gallery/thumb_v11_gallery1b.webp",
        textInv = True,
        param="gallery_CH11_S06",
        unlocked_if="gallery_scene_unlocked('CH11_S06')",
        chars=['Ian', 'Alison'],
        scope=merge_two_dicts({
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Ian celebrates Cherry's art exhibition"),
        img="gallery/thumb_v11_cherry3.webp",
        param="gallery_CH11_S07",
        unlocked_if="gallery_scene_unlocked('CH11_S07')",
        chars=['Ian', 'Cherry'],
        scope=merge_two_dicts({
            'ian_cherry_love': True,
            'v6_cherry_anal': 2,
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Alison invites Ian over after the exhibition"),
        img="gallery/thumb_v11_alison4.webp",
        textInv = True,
        param="gallery_CH11_S08",
        unlocked_if="gallery_scene_unlocked('CH11_S08')",
        chars=['Ian', 'Alison'],
        scope=merge_two_dicts({
            'ian_wardrobe_wits1': True,
            'ian_wardrobe_charisma1': True,
            'ian_wardrobe_athletics1': True,
            'ian_wardrobe_lust1': True,
            'alison_satisfaction': 5
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Holly makes Ian feel better"),
        img="gallery/thumb_v11_holly8.webp",
        textInv = True,
        param="gallery_CH11_S09",
        unlocked_if="gallery_scene_unlocked('CH11_S09')",
        chars=['Ian', 'Holly'],
        scope=merge_two_dicts({
            'ian_holly_love': True,
            'holly_gym': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Ian and Lena watch a movie and chill"),
        img="gallery/thumb_v11_lena3.webp",
        update_logic=lambda:"gallery/thumb_v11_lena3_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v11_lena3_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v11_lena3_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v11_lena3.webp",
        textInv = True,
        param="gallery_CH11_S10",
        unlocked_if="gallery_scene_unlocked('CH11_S10')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts({
            'ian_lena_dating': True
        })
    ),

    
    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena is bored in her old room"),
        img="gallery/thumb_v11_solo1.webp",
        update_logic=lambda:"gallery/thumb_v11_solo1_t123.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v11_solo1_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v11_solo1_t13.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo3 else "gallery/thumb_v11_solo1_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v11_solo1_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v11_solo1_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v11_solo1_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v11_solo1.webp",
        param="gallery_CH11_S11",
        unlocked_if="gallery_scene_unlocked('CH11_S11')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False,
            'ian_lena_dating': True,
            'lena_mike_dating': True,
            'lena_robert_dating': True,
            'lena_axel_desire': True,
            'lena_seymour_dating': True,
            'v8_jeremy_flirt': True,
            'v8_jeremy_sex': True,
            'lena_jeremy_sex': True,
            'v10_jeremy_3some': True,
            'lena_cheating': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena talks with a subscriber"),
        img="gallery/thumb_v11_solo5b.webp",
        textInv = True,
        param="gallery_CH11_S11b",
        unlocked_if="gallery_scene_unlocked('CH11_S11b')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False,
            'stalkfap': True,
            'stalkfap_pro': 2,
            'v10_stalkfap': 'ian',
            'toy_badboy': True,
            'lena_anal': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena had some self-care time"),
        img="gallery/thumb_v11_solo2.webp",
        update_logic=lambda:"gallery/thumb_v11_solo2_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v11_solo2_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v11_solo2_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v11_solo2.webp",
        param="gallery_CH11_S11c",
        unlocked_if="gallery_scene_unlocked('CH11_S11c')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False,
            'lena_anal': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Mike had been dying to see Lena again"),
        img="gallery/thumb_v11_mike3.webp",
        update_logic=lambda:"gallery/thumb_v11_mike3_t13.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo3 else "gallery/thumb_v11_mike3_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v11_mike3_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v11_mike3.webp",
        param="gallery_CH11_S13",
        unlocked_if="gallery_scene_unlocked('CH11_S13')",
        chars=['Lena', 'Mike'],
        scope=merge_two_dicts({'ian_active': False})
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Robert catches up with Lena"),
        img="gallery/thumb_v11_robert1.webp",
        update_logic=lambda:"gallery/thumb_v11_robert1_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v11_robert1.webp",
        param="gallery_CH11_S14",
        unlocked_if="gallery_scene_unlocked('CH11_S14')",
        chars=['Lena', 'Robert'],
        scope=merge_two_dicts({'ian_active': False})
    ),

    GalleryScene(
        kind="image",
        chapter=11,
        name=_("Ivy shows how Holly and Mark's date went"),
        img="gallery/thumb_v11_holly_mark1.webp",
        param=["v11_holly_mark1", "v11_holly_mark2"],
        unlocked_if="renpy.seen_image('v11_holly_mark2')",
        chars=['Holly', 'Mark']
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("The girls show what they have learned"),
        img="gallery/thumb_v11_poledance1.webp",
        textInv = True,
        param="gallery_CH11_S15",
        unlocked_if="gallery_scene_unlocked('CH11_S15')",
        chars=['Lena', 'Holly', 'Ivy'],
        scope=merge_two_dicts({
            'ian_active': False,
            'ian_minerva_sex': True,
            'holly_gym': True,
            'v11_holly_change': True,
            'lena_holly_sex': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("The girls have fun in the showers"),
        img="gallery/thumb_v11_shower1b.webp",
        textInv = True,
        param="gallery_CH11_S16",
        unlocked_if="gallery_scene_unlocked('CH11_S16')",
        chars=['Lena', 'Holly', 'Ivy'],
        scope=merge_two_dicts({
            'ian_active': False,
            'ian_minerva_sex': True,
            'holly_gym': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Just two best friends showering together"),
        img="gallery/thumb_v11_shower2.webp",
        update_logic=lambda:"gallery/thumb_v11_shower2_t123.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v11_shower2_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v11_shower2_t13.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo3 else "gallery/thumb_v11_shower2_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v11_shower2_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v11_shower2_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v11_shower2_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v11_shower2.webp",
        textInv = True,
        param="gallery_CH11_S16b",
        unlocked_if="gallery_scene_unlocked('CH11_S16b')",
        chars=['Lena', 'Ivy'],
        scope=merge_two_dicts({
            'ian_active': False,
            'ian_minerva_sex': True,
            'holly_gym': True,
            'v10_ivy_sex': 3
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena makes Holly feel special"),
        img="gallery/thumb_v11_holly20.webp",
        param="gallery_CH11_S17",
        unlocked_if="gallery_scene_unlocked('CH11_S17')",
        chars=['Lena', 'Holly'],
        scope=merge_two_dicts({
            'ian_active': False,
            'lena_holly_dating': True,
            'ian_holly_dating': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena had a surprise for Ian"),
        img="gallery/thumb_v11_3some6.webp",
        update_logic=lambda:"gallery/thumb_v11_3some6_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v11_3some6.webp",
        param="gallery_CH11_S18",
        unlocked_if="gallery_scene_unlocked('CH11_S18')",
        chars=['Lena', 'Louise', 'Ian'],
        scope=merge_two_dicts({
            'ian_active': False,
            'ian_lena_couple': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena invites Louise to join her and Mike"),
        img="gallery/thumb_v11_3some5_mike.webp",
        update_logic=lambda:"gallery/thumb_v11_3some5_mike_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v11_3some5_mike_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v11_3some5_mike_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v11_3some5_mike.webp",
        param="gallery_CH11_S19",
        unlocked_if="gallery_scene_unlocked('CH11_S19')",
        chars=['Lena', 'Louise', 'Mike'],
        scope=merge_two_dicts({
            'ian_active': False,
            'lena_mike_love': True
        })
    ),

    GalleryScene(
        kind="image",
        chapter=11,
        name=_("Lena and Stan have their first kiss"),
        img="gallery/thumb_v11_stan.webp",
        update_logic=lambda:"gallery/thumb_v11_stan_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v11_stan.webp",
        textInv = True,
        param=["v11_stan"],
        unlocked_if="renpy.seen_image('v11_stan')",
        chars=['Lena', 'Stan']
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena plays with her reflection"),
        img="gallery/thumb_v11_seymour2.webp",
        update_logic=lambda:"gallery/thumb_v11_seymour2_t123.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v11_seymour2_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v11_seymour2_t13.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo3 else "gallery/thumb_v11_seymour2_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v11_seymour2_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v11_seymour2_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v11_seymour2_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v11_seymour2.webp",
        param="gallery_CH11_S20",
        unlocked_if="gallery_scene_unlocked('CH11_S20')",
        chars=['Lena', 'Seymour'],
        scope=merge_two_dicts({
            'ian_active': False,
            'lena_wardrobe_charisma1': True,
            'lena_wardrobe_black_dress': True,
            'seymour_necklace': True
        })
    ),
    
    

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena and Emma go shopping"),
        img="gallery/thumb_v11_bikini2.webp",
        update_logic=lambda:"gallery/thumb_v11_bikini2_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v11_bikini2.webp",
        param="gallery_CH11_S21",
        textInv = True,
        unlocked_if="gallery_scene_unlocked('CH11_S21')",
        chars=['Lena', 'Emma'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v11_lena_dress': 4,
            'v11_emma_date': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena flirts with Jeremy"),
        img="gallery/thumb_v11_bbc1.webp",
        update_logic=lambda:"gallery/thumb_v11_bbc1_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v11_bbc1.webp",
        param="gallery_CH11_S22",
        unlocked_if="gallery_scene_unlocked('CH11_S22')",
        chars=['Lena', 'Jeremy'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v11sms2_jeremy': True,
            'lena_jeremy_sex': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Marcel heard rumors"),
        img="gallery/thumb_v11_bbc2b_marcel.webp",
        update_logic=lambda:"gallery/thumb_v11_bbc2b_marcel_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v11_bbc2b_marcel.webp",
        textInv = True,
        param="gallery_CH11_S23",
        unlocked_if="gallery_scene_unlocked('CH11_S23')",
        chars=['Lena', 'Marcel'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena and Axel figure things out"),
        img="gallery/thumb_v11_axel3.webp",
        param="gallery_CH11_S24",
        unlocked_if="gallery_scene_unlocked('CH11_S24')",
        chars=['Lena', 'Axel'],
        scope=merge_two_dicts({
            'ian_active': False,
            'axel_disposition': 3,
            'lena_axel_desire': True,
            'lena_axel_dating': True,
            'lena_drugs': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena visits the VIP"),
        img="gallery/thumb_v11_jack2a.webp",
        update_logic=lambda:"gallery/thumb_v11_jack2a_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v11_jack2a_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v11_jack2a_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v11_jack2a.webp",
        param="gallery_CH11_S27",
        unlocked_if="gallery_scene_unlocked('CH11_S27')",
        chars=['Lena', 'Jack'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena brings Mark home after bartending"),
        img="gallery/thumb_v11_mark2b.webp",
        update_logic=lambda:"gallery/thumb_v11_mark2b_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v11_mark2b_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v11_mark2b_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v11_mark2b.webp",
        param="gallery_CH11_S25",
        unlocked_if="gallery_scene_unlocked('CH11_S25')",
        chars=['Lena', 'Mark'],
        scope=merge_two_dicts({
            'ian_active': False,
            'stalkfap_pro': True,
            'lena_anal': 2,
            'v10_wc_bj': 'mark'
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=11,
        name=_("Lena goes to Ian's after bartending"),
        img="gallery/thumb_v11_lenaian1.webp",
        update_logic=lambda:"gallery/thumb_v11_lenaian1_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v11_lenaian1.webp",
        textInv = True,
        param="gallery_CH11_S26",
        unlocked_if="gallery_scene_unlocked('CH11_S26')",
        chars=['Lena', 'Ian'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    
    
    

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Cherry wakes Ian"),
        img="gallery/thumb_v12_cherry4.webp",
        textInv = True,
        param="gallery_CH12_S01",
        unlocked_if="gallery_scene_unlocked('CH12_S01')",
        chars=['Ian', 'Cherry'],
        scope=merge_two_dicts({
            'ian_cherry_love': True
        })
    ),

    GalleryScene(
        kind="image",
        chapter=12,
        name=_("Cindy is choosing her bikini"),
        img="gallery/thumb_v12_cindy_selfie1.webp",
        param=["v12_cindy_selfie1", "v12_cindy_selfie2"],
        unlocked_if="renpy.seen_image('v12_cindy_selfie2')",
        chars=['Cindy']
    ),

    GalleryScene(
        kind="image",
        chapter=12,
        name=_("Alison invites Ian to her place"),
        img="gallery/thumb_v12_alison_selfie1.webp",
        param=["v12_alison_selfie1"],
        unlocked_if="renpy.seen_image('v12_alison_selfie1')",
        chars=['Alison']
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Minerva requires assistance in her office"),
        img="gallery/thumb_v12_minerva5b.webp",
        textInv = True,
        param="gallery_CH12_S02",
        unlocked_if="gallery_scene_unlocked('CH12_S02')",
        chars=['Ian', 'Minerva'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Cindy struggles with her feelings"),
        img="gallery/thumb_v12_cindy7b.webp",
        textInv = True,
        param="gallery_CH12_S03",
        unlocked_if="gallery_scene_unlocked('CH12_S03')",
        chars=['Ian', 'Cindy'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Alison has a stressful day"),
        img="gallery/thumb_v12_alison3.webp",
        textInv = True,
        param="gallery_CH12_S04",
        unlocked_if="gallery_scene_unlocked('CH12_S04')",
        chars=['Ian', 'Alison'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian pays for Lena's exclusive content"),
        img="gallery/thumb_v12_stalkfap6b.webp",
        update_logic=lambda:"gallery/thumb_v12_stalkfap6b_t123.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v12_stalkfap6b_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v12_stalkfap6b_t13.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo3 else "gallery/thumb_v12_stalkfap6b_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v12_stalkfap6b_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v12_stalkfap6b_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v12_stalkfap6b_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v12_stalkfap6b.webp",
        param="gallery_CH12_S05",
        unlocked_if="gallery_scene_unlocked('CH12_S05')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'lena_wardrobe_bunny': True,
            'lena_wardrobe_lingerie': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Jess needs a place to crash"),
        img="gallery/thumb_v12_jess1.webp",
        textInv = True,
        param="gallery_CH12_S06",
        unlocked_if="gallery_scene_unlocked('CH12_S06')",
        chars=['Ian', 'Jessica'],
        scope=merge_two_dicts({
            'v10_jess_porn': True
        })
    ),

    

    GalleryScene(
        kind="image",
        chapter=12,
        name=_("Lena admires her pictures"),
        img="gallery/thumb_v12_bbc_phone1.webp",
        param=["v12_bbc_phone1", "gallery/gall_v12_bbc_phone1.webp"],
        unlocked_if="gallery_scene_unlocked('CH12_I03')",
        chars=['Lena', 'Jeremy']
    ),

    GalleryScene(
        kind="image",
        chapter=12,
        name=_("Lena admires her pictures"),
        img="gallery/thumb_v12_bbc_phone2.webp",
        param=["v12_bbc_phone2", "gallery/gall_v12_bbc_phone2.webp"],
        unlocked_if="gallery_scene_unlocked('CH12_I04')",
        chars=['Lena', 'Marcel']
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ivy shows Holly's slutty side"),
        img="gallery/thumb_v12_holly_slut4.webp",
        textInv = True,
        param="gallery_CH12_S07",
        unlocked_if="gallery_scene_unlocked('CH12_S07')",
        chars=['Holly', 'Clark', 'Robert'],
        scope=merge_two_dicts({
            'ian_active': False,
            'holly_gym': True,
            'holly_slut': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Lena remembers that night at Blazer's"),
        img="gallery/thumb_v12_solo2.webp",
        update_logic=lambda:"gallery/thumb_v12_solo2_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v12_solo2_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v12_solo2_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v12_solo2.webp",
        param="gallery_CH12_S08",
        unlocked_if="gallery_scene_unlocked('CH12_S08')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Axel meets Lena at the station"),
        img="gallery/thumb_v12_axel15b.webp",
        update_logic=lambda:"gallery/thumb_v12_axel15b_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v12_axel15b_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v12_axel15b_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v12_axel15b.webp",
        param="gallery_CH12_S09",
        unlocked_if="gallery_scene_unlocked('CH12_S09')",
        chars=['Lena', 'Axel'],
        scope=merge_two_dicts({
            'v9_axel_sex': True,
            'ian_active': False
        })
    ),

    

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian and Holly get settled in their room"),
        img="gallery/thumb_v12_holly4c.webp",
        textInv = True,
        param="gallery_CH12_S10",
        unlocked_if="gallery_scene_unlocked('CH12_S10')",
        chars=['Ian', 'Holly'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian wakes to Emma"),
        img="gallery/thumb_v12_emma1.webp",
        textInv = True,
        param="gallery_CH12_S11",
        unlocked_if="gallery_scene_unlocked('CH12_S11')",
        chars=['Ian', 'Emma'],
        scope=merge_two_dicts({
            'ian_emma_sex': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Holly enjoys the beach"),
        img="gallery/thumb_v12_holly_beach1b.webp",
        textInv = True,
        param="gallery_CH12_S12",
        unlocked_if="gallery_scene_unlocked('CH12_S12')",
        chars=['Holly'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian protects Emma against sunburns"),
        img="gallery/thumb_v12_emma_beach1.webp",
        textInv = True,
        param="gallery_CH12_S13",
        unlocked_if="gallery_scene_unlocked('CH12_S13')",
        chars=['Ian', 'Emma'],
        scope=merge_two_dicts({
            'v12_emma_dress': 3,
            'emma_bikini': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian and Holly try to cool off in the sea"),
        img="gallery/thumb_v12_holly_sea2b.webp",
        textInv = True,
        param="gallery_CH12_S14",
        unlocked_if="gallery_scene_unlocked('CH12_S14')",
        chars=['Ian', 'Holly'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian helps Holly relax in the afternoon"),
        img="gallery/thumb_v12_holly6a.webp",
        textInv = True,
        param="gallery_CH12_S15",
        unlocked_if="gallery_scene_unlocked('CH12_S15')",
        chars=['Ian', 'Holly'],
        scope=merge_two_dicts({
            'ian_holly_love': True,
            'v12_holly_sea_sex': True,
            'v12_holly_sex1': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Lena arrives at the summer house"),
        img="gallery/thumb_v12_lena5a.webp",
        textInv = True,
        param="gallery_CH12_S16",
        unlocked_if="gallery_scene_unlocked('CH12_S16')",
        chars=['Ian', 'Lena'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian and Emma weren't ready for sleep"),
        img="gallery/thumb_v12_emma10.webp",
        textInv = True,
        param="gallery_CH12_S17",
        unlocked_if="gallery_scene_unlocked('CH12_S17')",
        chars=['Ian', 'Emma'],
        scope=merge_two_dicts({
            'ian_emma_sex': True,
            'v12_emma_sex1': True,
            'v12_emma_sunscreen': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian and Holly had a talk about Lena"),
        img="gallery/thumb_v12_holly14a.webp",
        textInv = True,
        param="gallery_CH12_S18",
        unlocked_if="gallery_scene_unlocked('CH12_S18')",
        chars=['Ian', 'Holly'],
        scope=merge_two_dicts({
            'v12_holly_sea_sex': True,
            'v12_holly_sex2': True,
            'holly_trinity': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian supports Lena in the evening"),
        textInv = True,
        img="gallery/thumb_v12_lena13b_squirt3.webp",
        update_logic=lambda:"gallery/thumb_v12_lena13b_squirt3_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v12_lena13b_squirt3.webp",
        param="gallery_CH12_S19",
        unlocked_if="gallery_scene_unlocked('CH12_S19')",
        chars=['Ian', 'Lena'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Louise decides to text Ian"),
        img="gallery/thumb_v12_louise3.webp",
        param="gallery_CH12_S20",
        unlocked_if="gallery_scene_unlocked('CH12_S20')",
        chars=['Louise'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ivy rewards Ian for his victory"),
        img="gallery/thumb_v12_ivy2.webp",
        param="gallery_CH12_S21",
        unlocked_if="gallery_scene_unlocked('CH12_S21')",
        chars=['Ivy'],
        scope=coreScope
    ),

    

    GalleryScene(
        kind="image",
        chapter=12,
        name=_("Ian has a talk with Gillian in his dreams"),
        img="gallery/thumb_v12_gillian_dream.webp",
        param=["v12_gillian_dream"],
        unlocked_if="gallery_scene_unlocked('CH12_S39')",
        chars=['Gillian']
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Lena needs help with sunscreen"),
        img="gallery/thumb_v12_lena_beach2.webp",
        update_logic=lambda:"gallery/thumb_v12_lena_beach2_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v12_lena_beach2_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v12_lena_beach2_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v12_lena_beach2.webp",
        textInv = True,
        param="gallery_CH12_S22",
        unlocked_if="gallery_scene_unlocked('CH12_S22')",
        chars=['Lena', 'Ian', 'Perry', 'Wade'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Photo shoot at the beach"),
        img="gallery/thumb_v12_holly_beach6b.webp",
        update_logic=lambda:"gallery/thumb_v12_holly_beach6b_t123.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v12_holly_beach6b_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v12_holly_beach6b_t13.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo3 else "gallery/thumb_v12_holly_beach6b_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v12_holly_beach6b_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v12_holly_beach6b_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v12_holly_beach6b_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v12_holly_beach6b.webp",
        textInv = True,
        param="gallery_CH12_S23",
        unlocked_if="gallery_scene_unlocked('CH12_S23')",
        chars=['Lena', 'Emma', 'Holly', 'Wade'],
        scope=merge_two_dicts({
            'v12_fireworks': True,
            'v11_emma_pics': True
        })
    ),

    GalleryScene(
        kind="image",
        chapter=12,
        name=_("Louise wishes Ian a good morning"),
        img="gallery/thumb_v12_louise5.webp",
        param=["v12_louise5"],
        unlocked_if="gallery_scene_unlocked('CH12_I24')",
        chars=['Louise']
    ),
    
    GalleryScene(
        kind="image",
        chapter=12,
        name=_("Cindy posts images of her Wildcats shoot"),
        img="gallery/thumb_v12_cindy_pg2.webp",
        param=["v12_cindy_pg1", "gallery/gall_v12_cindy_pg2b.webp"],
        unlocked_if="gallery_scene_unlocked('CH12_I25')",
        chars=['Cindy']
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian takes Lena's pictures"),
        img="gallery/thumb_v12_lena_22.webp",
        update_logic=lambda:"gallery/thumb_v12_lena_22_t123.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v12_lena_22_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v12_lena_22_t13.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo3 else "gallery/thumb_v12_lena_22_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v12_lena_22_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v12_lena_22_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v12_lena_22_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v12_lena_22.webp",
        param="gallery_CH12_S26",
        unlocked_if="gallery_scene_unlocked('CH12_S26')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts({
            'v10_stalkfap': 'ian',
            'lena_bikini': 3,
            'v12_lena_bikini': 3,
            'lena_background': 'lust',
            'lena_fty_3some': 1,
            'ian_lena_3some': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Cindy replies to Ian's messages"),
        img="gallery/thumb_v12_cindy_selfie2a.webp",
        param="gallery_CH12_S27",
        unlocked_if="gallery_scene_unlocked('CH12_S27')",
        chars=['Cindy'],
        scope=merge_two_dicts({
            'ian_fit': True,
            'cindy_ass': True,
            'cindy_satisfaction': 4,
            'v12_cindy_cum': 1,
            'ian_cindy_love': True,
            'v12_cindy_rel': 1,
            'v12_gift': 'cindy'
        })
    ),

    GalleryScene(
        kind="image",
        chapter=12,
        name=_("Ian touches Minerva's heart"),
        img="gallery/thumb_v12_minerva_selfie.webp",
        param=["v12_minerva_selfie"],
        unlocked_if="gallery_scene_unlocked('CH12_I28')",
        chars=['Minerva']
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian and Emma have to be quick"),
        img="gallery/thumb_v12_emma18.webp",
        param="gallery_CH12_S29",
        unlocked_if="gallery_scene_unlocked('CH12_S29')",
        chars=['Ian', 'Emma'],
        scope=merge_two_dicts({
            'lena_background': 'wits',
            'v12_emma_sex2': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian and Lena make love under the stars"),
        img="gallery/thumb_v12_lena25.webp",
        update_logic=lambda:"gallery/thumb_v12_lena25_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v12_lena25_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v12_lena25_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v12_lena25.webp",
        param="gallery_CH12_S30",
        unlocked_if="gallery_scene_unlocked('CH12_S30')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts({
            'v11_lena_squirt': True,
            'v12_lena_squirt': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian and Lena had a heart to heart"),
        img="gallery/thumb_v12_lena23.webp",
        update_logic=lambda:"gallery/thumb_v12_lena23_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v12_lena23_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v12_lena23_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v12_lena23.webp",
        param="gallery_CH12_S31",
        unlocked_if="gallery_scene_unlocked('CH12_S31')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts({
            'ian_lena_couple': True,
            'ian_chad': 5
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Perry finally scores"),
        img="gallery/thumb_v12_perry.webp",
        param="gallery_CH12_S32",
        unlocked_if="gallery_scene_unlocked('CH12_S32')",
        chars=['Emma', 'Perry'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Farewell sex"),
        img="gallery/thumb_v12_lena24.webp",
        update_logic=lambda:"gallery/thumb_v12_lena24_t123.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v12_lena24_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v12_lena24_t13.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo3 else "gallery/thumb_v12_lena24_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v12_lena24_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v12_lena24_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v12_lena24_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v12_lena24.webp",
        param="gallery_CH12_S33",
        unlocked_if="gallery_scene_unlocked('CH12_S33')",
        chars=['Ian', 'Lena'],
        scope=coreScope
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian gives his gift to Holly"),
        img="gallery/thumb_v12_holly18.webp",
        param="gallery_CH12_S34",
        unlocked_if="gallery_scene_unlocked('CH12_S34')",
        chars=['Ian', 'Holly'],
        scope=merge_two_dicts({
            'ian_holly_love': True,
            'v12_gift': 'holly'
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Lena discusses a MFM threesome with Ian"),
        img="gallery/thumb_v12_lena37b.webp",
        update_logic=lambda:"gallery/thumb_v12_lena37b_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v12_lena37b.webp",
        textInv = True,
        param="gallery_CH12_S35",
        unlocked_if="gallery_scene_unlocked('CH12_S35')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts({
            'lena_fty_bbc': True,
            'lena_mike_dating': True,
            'v11_mark_sex': True,
            'lena_robert_dating': True,
            'ian_lena_sex': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Ian punishes Lena"),
        img="gallery/thumb_v12_lena30.webp",
        param="gallery_CH12_S36",
        unlocked_if="gallery_scene_unlocked('CH12_S36')",
        chars=['Ian', 'Lena'],
        scope=merge_two_dicts({
            'ian_chad': 5,
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("The Holly trinity"),
        img="gallery/thumb_v12_trinity6.webp",
        update_logic=lambda:"gallery/thumb_v12_trinity6_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v12_trinity6.webp",
        textInv = True,
        param="gallery_CH12_S37",
        unlocked_if="gallery_scene_unlocked('CH12_S37')",
        chars=['Ian', 'Holly', 'Lena'],
        scope=merge_two_dicts({
            'v12_never_ever': True,
            'holly_trinity': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=12,
        name=_("Holly makes her move on Ian"),
        img="gallery/thumb_v12_holly24a.webp",
        param="gallery_CH12_S38",
        unlocked_if="gallery_scene_unlocked('CH12_S38')",
        chars=['Ian', 'Holly'],
        scope=merge_two_dicts({
            'holly_slut': True
        })
    ),

    GalleryScene( 
        kind="image",
        chapter=12,
        name=_("Alison entertains herself while Ian is away"),
        img="gallery/thumb_v12_alison_jeremy.webp",
        param=["v12_alison_jeremy"],
        unlocked_if="gallery_scene_unlocked('CH12_I40')",
        chars=['Alison', 'Jeremy']
    ),

    GalleryScene( 
        kind="scene",
        chapter=12,
        name=_("Cherry facetimes Ian"),
        img="gallery/thumb_v12_cherry_phone1.webp",
        param="gallery_CH12_S41",
        unlocked_if="gallery_scene_unlocked('CH12_S41')",
        chars=['Cherry'],
        scope=merge_two_dicts({
            'ian_cherry_love': True,
            'v12_cherry_dom': True,
            'v12_moon_text': 'cherry'
        })
    ),

    GalleryScene(
        kind="image",
        chapter=12,
        name=_("Axel adds Cindy to his project"),
        img="gallery/thumb_v12_axelpg2.webp",
        param=["v12_axelpg1", "v12_axelpg2"],
        unlocked_if="gallery_scene_unlocked('CH12_I39')",
        chars=['Cindy']
    ),

    
    
    

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Lena joins Seymour in front of the camera"),
        img="gallery/thumb_v13_seymour_pose2.webp",
        update_logic=lambda:"gallery/thumb_v13_seymour_pose2_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v13_seymour_pose2_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v13_seymour_pose2_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v13_seymour_pose2.webp",
        param="gallery_CH13_S01",
        unlocked_if="gallery_scene_unlocked('CH13_S01')",
        chars=['Lena', "Seymour"],
        scope=merge_two_dicts({
            'ian_active': False,
            'lena_travel': 'italy',
            'lena_posh': 4,
            'seymour_desire': True,
            'v6_seymour_shoot': True,
            'v6_axel_pose': 3
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Lena discovers Seymour's gift"),
        img="gallery/thumb_v13_seymour0b.webp",
        update_logic=lambda:"gallery/thumb_v13_seymour0b_t123.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v13_seymour0b_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v13_seymour0b_t13.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo3 else "gallery/thumb_v13_seymour0b_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v13_seymour0b_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v13_seymour0b_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v13_seymour0b_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v13_seymour0b.webp",
        param="gallery_CH13_S02",
        unlocked_if="gallery_scene_unlocked('CH13_S02')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False,
            'lena_posh': 4,
            'seymour_desire': True
        })
    ),

    GalleryScene( 
        kind="scene",
        chapter=13,
        name=_("Lena gives herself completely to Seymour"),
        img="gallery/thumb_v13_seymour10a.webp",
        textInv = True,
        update_logic=lambda:"gallery/thumb_v13_seymour10a_t123.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v13_seymour10a_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v13_seymour10a_t13.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo3 else "gallery/thumb_v13_seymour10a_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v13_seymour10a_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v13_seymour10a_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v13_seymour10a_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v13_seymour10a.webp",
        param="gallery_CH13_S03",
        unlocked_if="gallery_scene_unlocked('CH13_S03')",
        chars=['Lena', 'Seymour'],
        scope=merge_two_dicts({
            'ian_active': False,
            'seymour_desire': True
        })
    ),

    
    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Lena rewards Stan for his services"),
        img="gallery/thumb_v13_stan2c.webp",
        update_logic=lambda:"gallery/thumb_v13_stan2c_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v13_stan2c.webp",
        param="gallery_CH13_S04",
        unlocked_if="gallery_scene_unlocked('CH13_S04')",
        chars=['Lena', 'Stan'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v10_stalkfap': 'stan',
            'toy_double': True,
            'toy_lush': True,
            'toy_wand': True,
            'lena_anal': True,
            'stalkfap_pro': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Lena fulfills her custom video requests"),
        img="gallery/thumb_v13_solo1.webp",
        update_logic=lambda:"gallery/thumb_v13_solo1_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v13_solo1_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v13_solo1_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v13_solo1.webp",
        param="gallery_CH13_S05",
        unlocked_if="gallery_scene_unlocked('CH13_S05')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False,
            'toy_double': True,
            'toy_lush': True,
            'toy_wand': True,
            'lena_anal': True,
            'stalkfap_pro': 2
        })
    ),

    GalleryScene(
        kind="image",
        chapter=13,
        name=_("Jeremy wonders if Lena is back in town"),
        img="gallery/thumb_v13_jeremy_selfie.webp",
        param=["v13_jeremy_selfie"],
        unlocked_if="renpy.seen_image('v13_jeremy_selfie')",
        chars=['Jeremy']
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Lena finally tries her new toy"),
        img="gallery/thumb_v13_solo2a.webp",
        update_logic=lambda:"gallery/thumb_v13_solo2a_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v13_solo2a.webp",
        param="gallery_CH13_S07",
        unlocked_if="gallery_scene_unlocked('CH13_S07')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False,
            'toy_mandingo': True,
            'stalkfap_pro': 1,
            'lena_bbc_masturbate': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Lena goes on a date with John"),
        img="gallery/thumb_v13_guy2_john.webp",
        update_logic=lambda:"gallery/thumb_v13_guy2_john_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v13_guy2_john.webp",
        param="gallery_CH13_S08",
        unlocked_if="gallery_scene_unlocked('CH13_S08')",
        chars=['Lena', 'John'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Lena goes on a date with Robert"),
        img="gallery/thumb_v13_guy1_robert.webp",
        param="gallery_CH13_S09",
        unlocked_if="gallery_scene_unlocked('CH13_S09')",
        chars=['Lena', 'Robert'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v11_robert_sex': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Lena goes on a date with Mark"),
        img="gallery/thumb_v13_guy1_mark.webp",
        param="gallery_CH13_S10",
        unlocked_if="gallery_scene_unlocked('CH13_S10')",
        chars=['Lena', 'Mark'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Lena goes on a date with Ian"),
        img="gallery/thumb_v13_guy5a_ian.webp",
        param="gallery_CH13_S11",
        unlocked_if="gallery_scene_unlocked('CH13_S11')",
        chars=['Lena', 'Ian'],
        scope=merge_two_dicts({
            'ian_active': False,
            'ian_lena_dom': 1
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Lena goes on a date with Stan"),
        img="gallery/thumb_v13_stan10.webp",
        update_logic=lambda:"gallery/thumb_v13_stan10_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v13_stan10.webp",
        param="gallery_CH13_S12",
        unlocked_if="gallery_scene_unlocked('CH13_S12')",
        chars=['Lena', 'Stan'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v13_movie': 'n'
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Ian arrives late"),
        img="gallery/thumb_v13_trinity9.webp",
        textInv = True,
        update_logic=lambda:"gallery/thumb_v13_trinity9_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v13_trinity9.webp",
        param="gallery_CH13_S13",
        unlocked_if="gallery_scene_unlocked('CH13_S13')",
        chars=['Lena', 'Holly', 'Ian'],
        scope=merge_two_dicts({
            'ian_active': False,
            'holly_trinity': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Lena goes on a date with Holly"),
        img="gallery/thumb_v13_holly7.webp",
        textInv = True,
        param="gallery_CH13_S14",
        unlocked_if="gallery_scene_unlocked('CH13_S14')",
        chars=['Lena', 'Holly'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Lena goes on a date with Jeremy"),
        img="gallery/thumb_v13_jeremy5a.webp",
        param="gallery_CH13_S15",
        unlocked_if="gallery_scene_unlocked('CH13_S15')",
        chars=['Lena', 'Jeremy'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Ivy takes Holly on an adventure"),
        img="gallery/thumb_v13_glory5a.webp",
        textInv = True,
        update_logic=lambda:"gallery/thumb_v13_glory5a_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v13_glory5a.webp",
        param="gallery_CH13_S16",
        unlocked_if="gallery_scene_unlocked('CH13_S16')",
        chars=['Holly', 'Ivy'],
        scope=merge_two_dicts({
            'ian_active': False,
            'holly_guy': 4
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Lena and Emma have a sleepover"),
        img="gallery/thumb_v13_emma4.webp",
        update_logic=lambda:"gallery/thumb_v13_emma4_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v13_emma4_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v13_emma4_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v13_emma4.webp",
        param="gallery_CH13_S17",
        unlocked_if="gallery_scene_unlocked('CH13_S17')",
        chars=['Lena', 'Emma'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v11_emma_pics': 3
        })
    ),

    

    GalleryScene(
        kind="image",
        chapter=13,
        name=_("Holly's social media presence"),
        img="gallery/thumb_v13_holly_pl1.webp",
        param=["v13_holly_pl1", "v13_holly_pl2"],
        unlocked_if="gallery_scene_unlocked('CH13_I18')",
        chars=['Holly'],
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Lena and Emma confesss they were naughty"),
        img="gallery/thumb_v13_emma_lena_selfie2.webp",
        param="gallery_CH13_S19",
        unlocked_if="gallery_scene_unlocked('CH13_S19')",
        chars=['Lena', 'Emma'],
        scope=merge_two_dicts({
            'ian_lena_emma_3some': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Louise invites Ian over"),
        img="gallery/thumb_v13_louise2.webp",
        param="gallery_CH13_S20",
        unlocked_if="gallery_scene_unlocked('CH13_S20')",
        chars=['Ian', 'Louise'],
        scope=merge_two_dicts({
            'ian_promotion': True,
            'v4_show_louise': True,
            'ian_chad': 4
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Cindy returns from her modeling trip"),
        img="gallery/thumb_v13_cindy10.webp",
        param="gallery_CH13_S21",
        unlocked_if="gallery_scene_unlocked('CH13_S21')",
        chars=['Ian', 'Cindy'],
        scope=merge_two_dicts({
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Ian remembered Minerva's birthday"),
        img="gallery/thumb_v13_minerva7.webp",
        textInv = True,
        param="gallery_CH13_S22",
        unlocked_if="gallery_scene_unlocked('CH13_S22')",
        chars=['Ian', 'Minerva'],
        scope=coreScope
    ),

    GalleryScene(
        kind="image",
        chapter=13,
        name=_("Alison is home alone"),
        img="gallery/thumb_v13_alison_selfie.webp",
        param=["v13_alison_selfie"],
        unlocked_if="gallery_scene_unlocked('CH13_I23')",
        chars=['Ian', 'Alison'],
    ),

    GalleryScene(
        kind="image",
        chapter=13,
        name=_("Emma bent over the table"),
        img="gallery/thumb_v13_emma15.webp",
        param=["v13_emma15", "gall_v13_emma_kiss_wits", "gall_v13_emma_kiss_charisma", "gall_v13_emma_kiss_athletics", "gall_v13_emma_kiss_lust"],
        unlocked_if="gallery_scene_unlocked('CH13_I24')",
        chars=['Emma'],
    ),
    
    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Emma needs her fix in the restroom"),
        img="gallery/thumb_v13_emma16a.webp",
        param="gallery_CH13_S24",
        unlocked_if="gallery_scene_unlocked('CH13_S24')",
        chars=['Ian', 'Emma'],
        scope=merge_two_dicts({
            'v10_emma_sex': True,
            'emma_hot': True,
            'emma_hair': 'pink'
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Alison is home alone 2"),
        img="gallery/thumb_v13_alison4.webp",
        textInv = True,
        param="gallery_CH13_S25",
        unlocked_if="gallery_scene_unlocked('CH13_S25')",
        chars=['Ian', 'Alison'],
        scope=merge_two_dicts({
            'v13_alison_fuck': True,
            'alison_blonde': 3
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Ian persuades Alison"),
        img="gallery/thumb_v13_alison12.webp",
        textInv = True,
        param="gallery_CH13_S26",
        unlocked_if="gallery_scene_unlocked('CH13_S26')",
        chars=['Ian', 'Alison'],
        scope=merge_two_dicts({
            'ian_alison_dating': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Holly needs a place to stay the night"),
        img="gallery/thumb_v13_holly22b.webp",
        param="gallery_CH13_S27",
        unlocked_if="gallery_scene_unlocked('CH13_S27')",
        chars=['Ian', 'Holly'],
        scope=merge_two_dicts({
            'ian_chad': 5
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=13,
        name=_("Ian and Holly have a date without Lena"),
        img="gallery/thumb_v13_holly28.webp",
        param="gallery_CH13_S28",
        unlocked_if="gallery_scene_unlocked('CH13_S28')",
        chars=['Ian', 'Holly'],
        scope=merge_two_dicts({
            'holly_trinity': 2,
            'ian_lena_dating': True,
            'v3_ian_date': True
        })
    ),

    
    
    

    
    GalleryScene(
        kind="scene",
        chapter=14,
        name=_("Ivy wants a reward for driving"),
        img="gallery/thumb_v14_ivy_car2.webp",
        param="gallery_CH14_S01",
        unlocked_if="gallery_scene_unlocked('CH14_S01')",
        chars=['Lena', 'Ivy'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v11_shower_sex': True,
            'lena_fty_show': True,
            'toy_lush': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=14,
        name=_("Lena helps Danny warm up"),
        img="gallery/thumb_v14_pose10.webp",
        update_logic=lambda:"gallery/thumb_v14_pose10_t123.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v14_pose10_t12.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo2 else "gallery/thumb_v14_pose10_t13.webp" if persistent.gall_lena_tattoo1 and persistent.gall_lena_tattoo3 else "gallery/thumb_v14_pose10_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v14_pose10_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v14_pose10_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v14_pose10_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v14_pose10.webp",
        textInv = True,
        param="gallery_CH14_S02",
        unlocked_if="gallery_scene_unlocked('CH14_S02')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=14,
        name=_("Lena is falling for Jeremy"),
        img="gallery/thumb_v14_jeremy6a.webp",
        update_logic=lambda:"gallery/thumb_v14_jeremy6a_t1.webp" if persistent.gall_lena_tattoo1 else "gallery/thumb_v14_jeremy6a.webp",
        param="gallery_CH14_S03",
        unlocked_if="gallery_scene_unlocked('CH14_S03')",
        chars=['Lena', 'Jeremy'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v13_jeremy_deep': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=14,
        name=_("Seymour shows the results of their latest shoot"),
        img="gallery/thumb_v14_seymour1.webp",
        update_logic=lambda:"gallery/thumb_v14_seymour1_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v14_seymour1_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v14_seymour1_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v14_seymour1.webp",
        param="gallery_CH14_S04",
        unlocked_if="gallery_scene_unlocked('CH14_S04')",
        chars=['Lena', 'Seymour'],
        scope=merge_two_dicts({
            'ian_active': False,
            'lena_seymour_sex': True,
            'seymour_disposition': 3
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=14,
        name=_("Ivy is in need of content"),
        
        
        img="gallery/thumb_wipbg.webp",
        
        param= "gallery_WIP",
        unlocked_if="gallery_scene_unlocked('CH14_S05')",
        chars=['Lena', 'Billy', 'Ivy', 'Jeremy'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v14_room': 2,
            'billy_trust': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=14,
        name=_("Lena and Ivy end the night together"),
        img="gallery/thumb_v14_ivy6.webp",
        update_logic=lambda:"gallery/thumb_v14_ivy6_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v14_ivy6_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v14_ivy6_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v14_ivy6.webp",
        param="gallery_CH14_S06",
        unlocked_if="gallery_scene_unlocked('CH14_S06')",
        chars=['Lena', 'Ivy'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v14_room': 2,
            'v14_ivy_car': True,
            'ivy_jeremy': 2
        })
    ),

    
    GalleryScene(
        kind="scene",
        chapter=14,
        name=_("Lena relaxing at the pool"),
        img="gallery/thumb_v14_pose12.webp",
        update_logic=lambda:"gallery/thumb_v14_pose12_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v14_pose12_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v14_pose12_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v14_pose12.webp",
        param="gallery_CH14_S07",
        unlocked_if="gallery_scene_unlocked('CH14_S07')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=14,
        name=_("Lena receives a massage"),
        img="gallery/thumb_v14_anthony2b.webp",
        textInv = True,
        param="gallery_CH14_S08",
        unlocked_if="gallery_scene_unlocked('CH14_S08')",
        chars=['Lena', 'Anthony'],
        scope=merge_two_dicts({
            'ian_active': False,
            'v14_talk_anthony': 5,
            'lena_anthony': 8
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=14,
        name=_("Billy interviews Lena"),
        img="gallery/thumb_v14_interview3.webp",
        update_logic=lambda:"gallery/thumb_v14_interview3_t23.webp" if persistent.gall_lena_tattoo2 and persistent.gall_lena_tattoo3 else "gallery/thumb_v14_interview3_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v14_interview3_t3.webp" if persistent.gall_lena_tattoo3 else "gallery/thumb_v14_interview3.webp",
        param="gallery_CH14_S09",
        unlocked_if="gallery_scene_unlocked('CH14_S09')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False,
            'lena_anal': 2,
            'lena_fty_slave': True,
            'lena_posh': 4
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=14,
        name=_("The girls pose for Nymph"),
        
        
        img="gallery/thumb_wipbg.webp",
        
        param= "gallery_WIP",
        unlocked_if="gallery_scene_unlocked('CH14_S10')",
        chars=['Lena', 'Ivy', 'Jess', 'Sonia', 'Zarina'],
        scope=merge_two_dicts({
            'ian_active': False,
            'lena_fty_show': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=14,
        name=_("Mike calls his girlfriend"),
        img="gallery/thumb_v14_mike1.webp",
        update_logic=lambda:"gallery/thumb_v14_mike1_t2.webp" if persistent.gall_lena_tattoo2 else "gallery/thumb_v14_mike1.webp",
        param="gallery_CH14_S11",
        unlocked_if="gallery_scene_unlocked('CH14_S11')",
        chars=['Lena', 'Mike'],
        scope=merge_two_dicts({
            'ian_active': False,
            'lena_mike_dating': True,
            'lena_mike_love': True
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=14,
        name=_("Anthony asks Lena to pose for him"),
        
        
        img="gallery/thumb_wipbg.webp",
        
        param= "gallery_WIP",
        unlocked_if="gallery_scene_unlocked('CH14_S12')",
        chars=['Lena', 'Anthony'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=14,
        name=_("Ivy puts her mark on Lena"),
        
        
        img="gallery/thumb_wipbg.webp",
        
        param= "gallery_WIP",
        unlocked_if="gallery_scene_unlocked('CH14_S13')",
        chars=['Lena'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=14,
        name=_("Lena and Mike get wet"),
        
        
        
        img="gallery/thumb_wipbg.webp",
        
        param= "gallery_WIP",
        unlocked_if="gallery_scene_unlocked('CH14_S14')",
        chars=['Lena', 'Mike'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=14,
        name=_("Lena ends her second night with Mike"),
        
        img="gallery/thumb_wipbg.webp",
        
        param= "gallery_WIP",
        unlocked_if="gallery_scene_unlocked('CH14_S15')",
        chars=['Lena', 'Mike'],
        scope=merge_two_dicts({
            'ian_active': False,
            'lena_mike_love': 2
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=14,
        name=_("Lena ends her second night with Jeremy"),
        
        
        img="gallery/thumb_wipbg.webp",
        
        param= "gallery_WIP",
        unlocked_if="gallery_scene_unlocked('CH14_S16')",
        chars=['Lena', 'Jeremy'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    GalleryScene(
        kind="scene",
        chapter=14,
        name=_("Lena is a greedy girl"),
        
        
        img="gallery/thumb_wipbg.webp",
        
        param= "gallery_WIP",
        unlocked_if="gallery_scene_unlocked('CH14_S17')",
        chars=['Lena', 'Jeremy', 'Mike'],
        scope=merge_two_dicts({
            'ian_active': False
        })
    ),

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    

    

    
    
    

    
    

    
    

    
    

    
    

    
    

    
    
    
    
    
    
    
    

]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
