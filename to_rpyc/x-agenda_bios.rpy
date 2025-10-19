define phone_agenda_list = {
    'ian': [
        PhoneAgendaEntry(id='ian', name='Ian', show_if='ian_agenda'),
        PhoneAgendaEntry(id='agnes', name='Agnes', show_if='chapter > 5 and ian_agnes_agenda', use_ian_default=True),
        PhoneAgendaEntry(id='alison', name='Alison', show_if='ian_alison_agenda'),
        PhoneAgendaEntry(id='axel', name='Axel', show_if='ian_axel_agenda'),
        PhoneAgendaEntry(id='billy', name='Billy', show_if='chapter > 6 and ian_billy_agenda'),
        PhoneAgendaEntry(id='cherry', name='Cherry', show_if='ian_cherry_agenda'),
        PhoneAgendaEntry(id='cindy', name='Cindy', show_if='ian_cindy_agenda'),
        PhoneAgendaEntry(id='ed', name='Ed', show_if='ian_ed_agenda', use_ian_default=True),
        PhoneAgendaEntry(id='emma', name='Emma', show_if='ian_emma_agenda'),
        PhoneAgendaEntry(id='holly', name='Holly', show_if='ian_holly_agenda'),
        PhoneAgendaEntry(id='ivy', name='Ivy', show_if='ian_ivy_agenda'),
        PhoneAgendaEntry(id='jeremy', name='Jeremy', show_if='ian_jeremy_agenda'),
        PhoneAgendaEntry(id='jessb', name='Jessica', show_if='chapter > 5 and ian_jess_agenda and jess_bad'),
        PhoneAgendaEntry(id='jessg', name='Jessica', show_if='chapter > 5 and ian_jess_agenda and not jess_bad'),
        PhoneAgendaEntry(id='lena', name='Lena', show_if='ian_lena_agenda'),
        PhoneAgendaEntry(id='lola', name='Lola', show_if='ian_lola_agenda'),
        PhoneAgendaEntry(id='louise', name='Louise', show_if='ian_louise_agenda'),
        PhoneAgendaEntry(id='mayor', name='Mayor Vermeer', show_if='chapter > 3 and ian_mayor_agenda', use_ian_default=True, use_lena_default=True),
        PhoneAgendaEntry(id='minerva', name='Minerva', show_if='ian_minerva_agenda', use_lena_default=True),
        PhoneAgendaEntry(id='perry', name='Perry', show_if='ian_perry_agenda'),
        PhoneAgendaEntry(id='robert', name='Robert', show_if='ian_robert_agenda'),
        PhoneAgendaEntry(id='seymour', name='Seymour', show_if='ian_seymour_agenda'),
        PhoneAgendaEntry(id='stan', name='Stan', show_if='ian_stan_agenda'),
        PhoneAgendaEntry(id='victor', name='Victor', show_if='chapter > 6 and ian_victor_agenda'),
        PhoneAgendaEntry(id='yuri', name='Yuri', show_if='chapter > 3 and ian_yuri_agenda', use_lena_default=True),
        PhoneAgendaEntry(id='wade', name='Wade', show_if='ian_wade_agenda'),
        PhoneAgendaEntry(id='wen', name='Wen', show_if='ian_wen_agenda', use_lena_default=True),
    ],
    'lena': [
        PhoneAgendaEntry(id='lena', name='Lena', show_if='lena_agenda'),
        PhoneAgendaEntry(id='lola', name='Lola', show_if='lena_lola_agenda'),
        PhoneAgendaEntry(id='agnes', name='Agnes', show_if='chapter > 5 and lena_agnes_agenda', use_ian_default=True),
        PhoneAgendaEntry(id='alison', name='Alison', show_if='lena_alison_agenda'),
        PhoneAgendaEntry(id='axel', name='Axel', show_if='lena_axel_agenda'),
        PhoneAgendaEntry(id='billy', name='Billy', show_if='chapter > 6 and lena_billy_agenda'),
        PhoneAgendaEntry(id='cherry', name='Cherry', show_if='lena_cherry_agenda'),
        PhoneAgendaEntry(id='cindy', name='Cindy', show_if='lena_cindy_agenda'),
        PhoneAgendaEntry(id='lenadad', name='Dad', show_if='lena_lenadad_agenda', use_ian_default=True),
        PhoneAgendaEntry(id='danny', name='Danny', show_if='lena_danny_agenda', use_ian_default=True),
        PhoneAgendaEntry(id='ed', name='Ed', show_if='lena_ed_agenda', use_ian_default=True),
        PhoneAgendaEntry(id='emma', name='Emma', show_if='lena_emma_agenda'),
        PhoneAgendaEntry(id='holly', name='Holly', show_if='lena_holly_agenda'),
        PhoneAgendaEntry(id='ian', name='Ian', show_if='lena_ian_agenda'),
        PhoneAgendaEntry(id='ivy', name='Ivy', show_if='lena_ivy_agenda'),
        PhoneAgendaEntry(id='jeremy', name='Jeremy', show_if='lena_jeremy_agenda'),
        PhoneAgendaEntry(id='jessb', name='Jessica', show_if='chapter > 5 and lena_jess_agenda and jess_bad', use_ian_default=True, use_lena_default=True),
        PhoneAgendaEntry(id='jessg', name='Jessica', show_if='chapter > 5 and lena_jess_agenda and not jess_bad', use_ian_default=True, use_lena_default=True),
        PhoneAgendaEntry(id='louise', name='Louise', show_if='lena_louise_agenda'),
        PhoneAgendaEntry(id='mike', name='Mike', show_if='chapter > 4 and lena_mike_agenda'),
        PhoneAgendaEntry(id='mayor', name='Mayor Vermeer', show_if='chapter > 3 and lena_mayor_agenda', use_ian_default=True, use_lena_default=True),
        PhoneAgendaEntry(id='minerva', name='Minerva', show_if='lena_minerva_agenda', use_lena_default=True),
        PhoneAgendaEntry(id='molly', name='Molly', show_if='lena_molly_agenda'),
        PhoneAgendaEntry(id='lenamom', name='Mom', show_if='lena_lenamom_agenda', use_ian_default=True),
        PhoneAgendaEntry(id='perry', name='Perry', show_if='lena_perry_agenda'),
        PhoneAgendaEntry(id='robert', name='Robert', show_if='lena_robert_agenda'),
        PhoneAgendaEntry(id='seymour', name='Seymour', show_if='lena_seymour_agenda'),
        PhoneAgendaEntry(id='stan', name='Stan', show_if='lena_stan_agenda'),
        PhoneAgendaEntry(id='victor', name='Victor', show_if='chapter > 6 and lena_victor_agenda'),
        PhoneAgendaEntry(id='wade', name='Wade', show_if='lena_wade_agenda'),
    ],
}

define bio_characters = {
    
    
    'ian': {
        'bio': [
            
            
            ('chapter > 3 and ian_lena_sex', "Ian is a struggling writer wannabe. He studied literature and journalism, but he's far from achieving his dream of publishing a book, and he's starting to wonder if that will ever happen. He barely gets by doing book reviews as an intern at a magazine, so the only way he could afford to move out of his parents' house was to go live with his friend Perry. His love life is a mess, too. He broke up with his four-year-long girlfriend a year ago, and it still weighs heavily on him. \nAfter meeting Lena and hanging out several times, they couldn't deny the strong attraction they felt for each other and finally slept together. Still, they both feel it's too early to define their relationship..."),
            ('True', "Ian is a struggling writer wannabe. He studied literature and journalism, but he's far from achieving his dream of publishing a book, and he's starting to wonder if that will ever happen. He barely gets by doing book reviews as an intern at a magazine, so the only way he could afford to move out of his parents' house was to go live with his friend Perry. His love life is a mess, too. He broke up with his four-year-long girlfriend a year ago, and it still weighs heavily on him."),
        ],
        'lena': [
            
            ('ian_lena_over or ian_lena_breakup', "broken"),
            ('ian_lena < 2', "mad"),
            ('chapter > 3 and ian_lena_sex', "love"),
            ('ian_lena < 4', "neutral"),
            ('True', "smile"),
        ],
        'alison': [
            ('chapter > 10 and ian_alison_fuck', "love"),
            ('ian_alison_breakup', "broken"),
            ('chapter > 1 and ian_alison_sex', "love"),
            ('ian_alison < 2', "mad"),
            ('ian_alison < 4', "neutral"),
            ('True', "smile"),
        ],
        'emma': [
            ('chapter > 4 and ian_emma_sex', "love"),
            ('ian_emma < 2', "mad"),
            ('ian_emma < 4', "neutral"),
            ('True', "smile"),
        ],
        'minerva': [
            ('ian_minerva_over', "broken"),
            ('chapter > 5 and ian_minerva_sex', "love"),
            ('ian_minerva < 4', "mad"),
            ('ian_minerva < 7', "neutral"),
            ('True', "smile"),
        ],
        'cherry': [
            ('chapter > 1 and ian_cherry_sex', "love"),
            ('ian_cherry < 2', "mad"),
            ('ian_cherry < 4', "neutral"),
            ('True', "smile"),
        ],
        'holly': [
            ('ian_holly_dating', "love"),
            ('ian_holly < 2', "mad"),
            ('ian_holly < 4', "neutral"),
            ('True', "smile"),
        ],
        'cindy': [
            ('ian_cindy_over', "broken"),
            ('ian_cindy < 2', "mad"),
            ('ian_cindy_sex or ian_cindy_dating', "love"),
            ('ian_cindy < 4', "neutral"),
            ('True', "smile"),
        ],
    },
    'lena': {
        'bio': [
            ('chapter > 3 and ian_lena_sex', "Lena is no ordinary girl. She might be beautiful, but there's a lot more under the surface. Hard-working, passionate and intelligent, she has never had it easy, having to struggle to get ahead most of the time. She had to stop studying to support herself and her humble family, and her emotional life has been tough, too. After having ended a toxic relationship with her ex-boyfriend, Axel, she's trying to find purpose and meaning in her life again. \nAfter meeting Ian and hanging out several times, they couldn't deny the strong attraction they felt for each other and finally slept together. Still, they both feel it's too early to define their relationship..."),
            ('True', "Lena is no ordinary girl. She might be beautiful, but there's a lot more under the surface. Hard-working, passionate and intelligent, she has never had it easy, having to struggle to get ahead most of the time. She had to stop studying to support herself and her humble family, and her emotional life has been tough, too. After having ended a toxic relationship with her ex-boyfriend, Axel, she's trying to find purpose and meaning in her life again."),
        ],
        'louise': [
            ('chapter > 4 and lena_louise_sex', "love"),
            ('lena_reject_louise', "broken"),
            ('lena_louise < 2', "mad"),
            ('lena_louise < 4', "neutral"),
            ('True', "smile"),
        ],
        'minerva': [
            ('lena_default < 2', "mad"),
            ('True', "neutral"),
        ],
        'robert': [
            ('chapter > 3 and lena_robert_sex and lena_robert_over', "broken"),
            ('chapter > 2 and lena_robert_sex', "love"),
            ('chapter > 3 and lena_robert_over', "neutral"),
            ('lena_robert < 2', "mad"),
            ('lena_robert < 4', "neutral"),
            ('True', "smile"),
        ],
        'mike': [
            ('lena_mike_over', "broken"),
            ('lena_mike < 2', "mad"),
            ('lena_mike_sex', "love"),
            ('lena_mike < 4', "neutral"),
            ('True', "smile"),
        ],
        'holly': [
            ('lena_holly_sex or v10_lena_holly_sex or v11_lena_holly_sex', "love"),
            ('lena_holly < 2', "mad"),
            ('lena_holly < 4', "neutral"),
            ('True', "smile"),
        ],
    },
    'alison': {
        'bio': [
            ("chapter > 5 and ian_alison_dating and alison_jeremy", "Alison was another of Ian's classmates during high school. Though she has her own group of friends, she and Ian had a very good relationship. After high school, Alison focused on her Civil Engineering studies, and she and Ian grew distant, even though they kept in touch occasionally. Even though she's a beautiful and intelligent woman, she seems to be going through a tough break. She recently lost her job and broke off her three-year relationship with her boyfriend... \nIan couldn't keep ignoring the sexual tension between him and Alison, and they ended up having sex. Alison doesn't seem to be looking for a serious relationship, though, since she also slept with Jeremy...\nAlison and Ian kept their physical relationship going. She seemed quite enthusiastic about it, even though Ian could sense something was a bit off..."),
            ("chapter > 5 and ian_alison_dating", "Alison was another of Ian's classmates during high school. Though she has her own group of friends, she and Ian had a very good relationship. After high school, Alison focused on her Civil Engineering studies, and she and Ian grew distant, even though they kept in touch occasionally. Even though she's a beautiful and intelligent woman, she seems to be going through a tough break. She recently lost her job and broke off her three-year relationship with her boyfriend... \nIan couldn't keep ignoring the sexual tension between him and Alison, and they ended up having sex. Alison doesn't seem to be looking for a serious relationship, though...\nAlison and Ian kept their physical relationship going. She seemed quite enthusiastic about it, even though Ian could sense something was a bit off..."),
            ("chapter > 2 and ian_alison_sex and alison_jeremy", "Alison was another of Ian's classmates during high school. Though she has her own group of friends, she and Ian had a very good relationship. After high school, Alison focused on her Civil Engineering studies, and she and Ian grew distant, even though they kept in touch occasionally. Even though she's a beautiful and intelligent woman, she seems to be going through a tough break. She recently lost her job and broke off her three-year relationship with her boyfriend... \nIan couldn't keep ignoring the sexual tension between him and Alison, and they ended up having sex. Alison doesn't seem to be looking for a serious relationship, though, since she also slept with Jeremy..."),
            ("chapter > 2 and ian_alison_sex", "Alison was another of Ian's classmates during high school. Though she has her own group of friends, she and Ian had a very good relationship. After high school, Alison focused on her Civil Engineering studies, and she and Ian grew distant, even though they kept in touch occasionally. Even though she's a beautiful and intelligent woman, she seems to be going through a tough break. She recently lost her job and broke off her three-year relationship with her boyfriend... \nIan couldn't keep ignoring the sexual tension between him and Alison, and they ended up having sex. Alison doesn't seem to be looking for a serious relationship, though..."),
            ("chapter > 2 and alison_jeremy", "Alison was another of Ian's classmates during high school. Though she has her own group of friends, she and Ian had a very good relationship. After high school, Alison focused on her Civil Engineering studies, and she and Ian grew distant, even though they kept in touch occasionally. Even though she's a beautiful and intelligent woman, she seems to be going through a tough break. She recently lost her job and broke off her three-year relationship with her boyfriend... \nShe and Jeremy hooked up and are now seeing each other."),
            ("True", "Alison was another of Ian's classmates during high school. Though she has her own group of friends, she and Ian had a very good relationship. After high school, Alison focused on her Civil Engineering studies, and she and Ian grew distant, even though they kept in touch occasionally. Even though she's a beautiful and intelligent woman, she seems to be going through a tough break. She recently lost her job and broke off her three-year relationship with her boyfriend..."),
        ]
    },
    'axel': {
        'bio': [
            ("lena_active and chapter > 5 and v6_axel_pose", "Axel is Lena's ex-boyfriend. They met through Ivy, and both of them got Lena into the modeling world. He makes a living both as a model and photographer, though he claims to be more interested in being behind a camera rather than in front of one. His magnetic and dominant personality has granted him a lot of success, but that doesn't seem to be enough to make him happy.\nAfter thinking it over, Lena agreed to meet Axel and allow him to explain himself and get the closure he was asking for. But after finding some old polaroids, Lena could start feeling it's her who hasn't gotten the closure she needs... Those doubts became even bigger after she found herself unexpectedly working with Axel once again in a photo shoot that was dangerously close to getting out of control."),
            ("lena_active and chapter > 3 and v4_axel_date and axel_pictures_watch", "Axel is Lena's ex-boyfriend. They met through Ivy, and both of them got Lena into the modeling world. He makes a living both as a model and photographer, though he claims to be more interested in being behind a camera rather than in front of one. His magnetic and dominant personality has granted him a lot of success, but that doesn't seem to be enough to make him happy.\nAfter thinking it over, Lena agreed to meet Axel and allow him to explain himself and get the closure he was asking for. But after finding some old polaroids, Lena could start feeling it's her who hasn't gotten the closure she needs..."),
            ("lena_active and chapter > 3 and v4_axel_date", "Axel is Lena's ex-boyfriend. They met through Ivy, and both of them got Lena into the modeling world. He makes a living both as a model and photographer, though he claims to be more interested in being behind a camera rather than in front of one. His magnetic and dominant personality has granted him a lot of success, but that doesn't seem to be enough to make him happy.\nAfter thinking it over, Lena agreed to meet Axel and allow him to explain himself and get the closure he was asking for. Lena hoped Axel was finally ready to turn the page, just as she did."),
            ("lena_active", "Axel is Lena's ex-boyfriend. They met through Ivy, and both of them got Lena into the modeling world. He makes a living both as a model and photographer, though he claims to be more interested in being behind a camera rather than in front of one. His magnetic and dominant personality has granted him a lot of success, but that doesn't seem to be enough to make him happy."),
            
            ("True", "Axel is a professional photographer Cindy met one night at a bar. He seems very confident, and no wonder why: he's tall, handsome, and charming. One could say he's the kind of guy who gets everything he wants served on a silver platter..."),
        ]
    },
    'cindy': {
        'bio': [
            ("chapter > 5 and v5_cindy_shoot", "Cindy is Wade’s girlfriend. They met in college and have been dating for about three years. Cindy is a beautiful, charming and cheerful girl, always full of energy, but she has a temper and always wants things to go her way, and she’s used to getting what she wants.\nShe met Axel, who offered her a modeling opportunity. Cindy was on the fence, but Ian encouraged her and even went with her to the shooting. It ended up being a way sexier experience than they anticipated..."),
            ("chapter > 5", "Cindy is Wade’s girlfriend. They met in college and have been dating for about three years. Cindy is a beautiful, charming and cheerful girl, always full of energy, but she has a temper and always wants things to go her way, and she’s used to getting what she wants.\nLately, she has been feeling frustrated with her relationship with Wade. She doesn't find the passion she's looking for in her boyfriend, and new opportunities are arising..."),
            ("True", "Cindy is Wade’s girlfriend. They met in college and have been dating for about three years. Cindy is a beautiful, charming and cheerful girl, always full of energy, but she has a temper and always wants things to go her way, and she’s used to getting what she wants."),
        ]
    },
    'emma': {
        'bio': [
            ("chapter > 4 and ian_emma_sex", "Emma is one of the most easy-going human beings one can meet. She's a free soul, and she wanders through life like a leaf moved by the wind, always with a smile and positive attitude, open to experience what the world has to offer. She played in a band with Ian and Perry while they were in high school, and they have been friends ever since. She's always moving and making new friends, so it can be hard to see her sometimes, much to Perry's discontent. \nDuring a night out at the club, Ian realized Emma was interested in something more than plain friendship. After dancing and flirting, they ended up at Ian's place, where they had an intense night of sex. If Perry only knew...!"),
            ("True", "Emma is one of the most easy-going human beings one can meet. She's a free soul, and she wanders through life like a leaf moved by the wind, always with a smile and positive attitude, open to experience what the world has to offer. She played in a band with Ian and Perry while they were in high school, and they have been friends ever since. She's always moving and making new friends, so it can be hard to see her sometimes, much to Perry's discontent."),
        ]
    },
    'holly': {
        'bio': [
            ("True", "Though young, Holly is quite a successful writer. For as long as she can remember, she was the kind of girl who enjoyed living between the pages of a book rather than going to parties and doing all that extroverted stuff. Her books are now gaining quite a following, so she combines her job as a professional writer with an internship to finally earn her college degree. Despite her devoted fan base, she still can't believe her books are appreciated and she often acts insecurely around other people, feeling afraid of leaving her shell."),
        ]
    },
    'ivy': {
        'bio': [
            ("True", "Ivy is Lena's closest friend and the only one she still keeps from her high school years. Ivy has always been a whirlwind, passionate, adventurous, and quite brash, but also fun and loyal. It was Ivy who introduced Lena to the modeling world and to Axel. She's an incredibly sexy girl, and she has never shied away from it, quite the contrary, using her looks for her benefit and making a living off them. She loves dancing, partying, flirting, and meeting new people, and there's always something crazy going on with her."),
        ]
    },
    'jeremy': {
        'bio': [
            ("True", "Ian has known Jeremy for a very long time. They used to be friends when they were kids and even took karate lessons together after school for a few years. Their paths diverged after high school until they met each other again at the local gym. Jeremy has changed quite a lot after all these years. He's a confident and easy-going guy who loves to go out, party, and flirt with the ladies."),
        ]
    },
    'louise': {
        'bio': [
            ("chapter > 4 and lena_louise_sex", "Louise and Lena met at college, and they became good friends. She moved to the city to study and didn't know too many people, so she was glad to find someone she could get along with since she's not the most out-going person. In fact, she tends to be moody, and she always has some drama going on, especially with guys. She has a complicated character, but once you get to know her, she's a nice, sensitive girl and a loyal friend. \nTurns out her mysterious boyfriend was Jeremy, Ian's friend. However, he was playing the field and being unfaithful to Louise. Lena told her about it, but she didn't believe it... Until she saw it with her own eyes. Seeking solace in her friend, Louise made a move on Lena, and both girls shared a night of sapphic passion together."),
            ("chapter > 4 and not louise_jeremy", "Louise and Lena met at college, and they became good friends. She moved to the city to study and didn't know too many people, so she was glad to find someone she could get along with since she's not the most out-going person. In fact, she tends to be moody, and she always has some drama going on, especially with guys. She has a complicated character, but once you get to know her, she's a nice, sensitive girl and a loyal friend. \nTurns out her mysterious boyfriend was Jeremy, Ian's friend. However, he was playing the field and being unfaithful to Louise. Lena told her about it, but she didn't believe it... Until she saw it with her own eyes. Seeking solace in her friend, Louise made a move on Lena, but she was rejected."),
            ("chapter > 4", "Louise and Lena met at college, and they became good friends. She moved to the city to study and didn't know too many people, so she was glad to find someone she could get along with since she's not the most out-going person. In fact, she tends to be moody, and she always has some drama going on, especially with guys. She has a complicated character, but once you get to know her, she's a nice, sensitive girl and a loyal friend. \nTurns out her mysterious boyfriend was Jeremy, Ian's friend. However, he was playing the field and being unfaithful to Louise. Lena learned about this but decided against telling her friend..."),
            ("chapter > 3 and not louise_jeremy", "Louise and Lena met at college, and they became good friends. She moved to the city to study and didn't know too many people, so she was glad to find someone she could get along with since she's not the most out-going person. In fact, she tends to be moody, and she always has some drama going on, especially with guys. She has a complicated character, but once you get to know her, she's a nice, sensitive girl and a loyal friend. \nTurns out her mysterious boyfriend was Jeremy, Ian's friend. However, he was playing the field and being unfaithful to Louise. When Lena learned about this, she decided to tell her friend."),
            ("chapter > 3", "Louise and Lena met at college, and they became good friends. She moved to the city to study and didn't know too many people, so she was glad to find someone she could get along with since she's not the most out-going person. In fact, she tends to be moody, and she always has some drama going on, especially with guys. She has a complicated character, but once you get to know her, she's a nice, sensitive girl and a loyal friend. \nTurns out her mysterious boyfriend was Jeremy, Ian's friend. However, he was playing the field and being unfaithful to Louise. Lena learned about this but decided against telling her friend..."),
            ("True", "Louise and Lena met at college, and they became good friends. She moved to the city to study and didn't know too many people, so she was glad to find someone she could get along with since she's not the most out-going person. In fact, she tends to be moody, and she always has some drama going on, especially with guys. She has a complicated character, but once you get to know her, she's a nice, sensitive girl and a loyal friend."),
        ]
    },
    'perry': {
        'bio': [
            ("True", "Perry is Ian's roommate. He's been a loyal friend of his since high school, and they even played in a band together during that time. When Ian had to move out of his parents' house, Perry offered him to share his family's apartment for a small rent, and he accepted. Perry is laid back, lazy, and prefers to drink beer, play video games and watch porn rather than get a job or do something productive. He has artistic talents to tap into, but he needs to get off his butt and take responsibility for his life."),
        ]
    },
    'seymour': {
        'bio': [
            ("chapter > 3 and v3_seymour_reject", "Seymour is one of the most important figures in the literary world. He began his career as a book writer, and after moderate success, he struck gold when he became a publisher. Now he's the head of one of the biggest publishing brands in the world, having a ton of the most important best-selling books and authors under his wing. He's well-mannered and cultured and has the calm but imposing presence of someone who's used to being obeyed. One can clearly get a glimpse of the intelligence that resides behind his clear, icy eyes. \nHe showed interest in hiring Lena as a model, but she refused. Used to always getting what he wants, Seymour didn't like being rejected..."),
            ("chapter > 3", "Seymour is one of the most important figures in the literary world. He began his career as a book writer, and after moderate success, he struck gold when he became a publisher. Now he's the head of one of the biggest publishing brands in the world, having a ton of the most important best-selling books and authors under his wing. He's well-mannered and cultured and has the calm but imposing presence of someone who's used to being obeyed. One can clearly get a glimpse of the intelligence that resides behind his clear, icy eyes. \nHe showed interest in hiring Lena as a model, and she agreed. Being in business with someone that influential could prove useful... But she was also intrigued by him."),
            ("True", "Seymour is one of the most important figures in the literary world. He began his career as a book writer, and after moderate success, he struck gold when he became a publisher. Now he's the head of one of the biggest publishing brands in the world, having a ton of the most important best-selling books and authors under his wing. He's well-mannered and cultured and has the calm but imposing presence of someone who's used to being obeyed. One can clearly get a glimpse of the intelligence that resides behind his clear, icy eyes."),
        ]
    },
    'stan': {
        'bio': [
            ("True", "Anyone would say Stan is a typical nerd. He is a shy and usually quiet guy who works as a programmer from home. He spends most of the time in his room, glued to his computer screen, be it working, playing games, or who knows what else. It seems like most of his social life is conducted on-line, and he has no luck with the ladies. His clumsy social skills and unattractive appearance are to blame..."),
        ]
    },
    'wade': {
        'bio': [
            ("chapter > 5 and wade_cindy == 2", "Wade has been friends with Ian and Perry since high school and played in a band together with them. He has never had any trouble with the ladies since his good looks always made him stand out, especially compared to his friends. He always had a few girls to hook up with until he began dating Cindy. Since he never had to really make an effort and he has an incredibly beautiful girlfriend already, he's gotten even more complacent these last few years. Seems all he's interested in is playing video games, drinking beer, and enjoying a simple life. Maybe that's why he and Perry get along really well.\nRecently he and Cindy have been fighting a lot, and their relationship is going through a rough patch. Ian is trying to help his friend sort things out and save his relationship with Cindy."),
            ("chapter > 5", "Wade has been friends with Ian and Perry since high school and played in a band together with them. He has never had any trouble with the ladies since his good looks always made him stand out, especially compared to his friends. He always had a few girls to hook up with until he began dating Cindy. Since he never had to really make an effort and he has an incredibly beautiful girlfriend already, he's gotten even more complacent these last few years. Seems all he's interested in is playing video games, drinking beer, and enjoying a simple life. Maybe that's why he and Perry get along really well.\nRecently he and Cindy have been fighting a lot, and their relationship is going through a rough patch. Things don't look too promising, though..."),
            ("True", "Wade has been friends with Ian and Perry since high school and played in a band together with them. He has never had any trouble with the ladies since his good looks always made him stand out, especially compared to his friends. He always had a few girls to hook up with until he began dating Cindy. Since he never had to really make an effort and he has an incredibly beautiful girlfriend already, he's gotten even more complacent these last few years. Seems all he's interested in is playing video games, drinking beer, and enjoying a simple life. Maybe that's why he and Perry get along really well."),
        ]
    },
    'minerva': {
        'bio': [
            ("chapter > 5 and ian_minerva_sex", "Minerva is a cultured, hard-working, fashionable, and empowered woman. She runs the magazine and is a competent boss. Too bad she seems to dislike Ian for some reason and is never happy with anything he does... On the other hand, she displays a motherly attitude when dealing with Holly.\nAfter a series of very vocal disagreements with Ian in the workplace, she threatened to fire him, but when pushed into a corner by him, Minerva revealed the true reasons behind her attitude towards him: she hated how much Ian's defiance turned her on, trapped as she was in an unhappy and tedious marriage. She finally got what she wanted, and Ian offered to release all her pent-up sexual frustration, pounding her hard in her office."),
            ("chapter > 5 and ian_defy_minerva", "Minerva is a cultured, hard-working, fashionable, and empowered woman. She runs the magazine and is a competent boss. Too bad she seems to dislike Ian for some reason and is never happy with anything he does... On the other hand, she displays a motherly attitude when dealing with Holly.\nAfter a series of very vocal disagreements with Ian in the workplace, she threatened to fire him, but when pushed into a corner by him, Minerva revealed the true reasons behind her attitude towards him: she hated how much Ian's defiance turned her on, trapped as she was in an unhappy and tedious marriage. Ian managed to keep his job and refused to help Minerva find a release to all her pent-up sexual frustration."),
            ("chapter > 5 and ian_job_magazine == 0", "Minerva is a cultured, hard-working, fashionable, and empowered woman. She runs the magazine and is a competent boss. Too bad she seems to dislike Ian for some reason and is never happy with anything he does... On the other hand, she displays a motherly attitude when dealing with Holly.\nAfter a series of very vocal disagreements with Ian in the workplace, Minerva had enough and fired Ian, leaving him suddenly jobless."),
            ("True", "Minerva is a cultured, hard-working, fashionable, and empowered woman. She runs the magazine and is a competent boss. Too bad she seems to dislike Ian for some reason and is never happy with anything he does... On the other hand, she displays a motherly attitude when dealing with Holly."),
        ]
    },
    'ed': {
        'bio': [
            ("chapter > 5 and cafe_music", "Ed is as kind and friendly as his wife, Molly. Together they run a café, which they opened several years back. Ed is in charge of the kitchen, and he's a great cook. He has always led a simple life and never wanted for anything more than to have a happy and fulfilling life near those he loves. His only regret is not having had a son...\nThe café was struggling, and it seemed like they would need to close up shop... However, Lena offered to play a concert to help Ed and Molly draw more customers in. Will it work?"),
            ("chapter > 5 and cafe_nude", "Ed is as kind and friendly as his wife, Molly. Together they run a café, which they opened several years back. Ed is in charge of the kitchen, and he's a great cook. He has always led a simple life and never wanted for anything more than to have a happy and fulfilling life near those he loves. His only regret is not having had a son...\nThe café was struggling, and it seemed like they would need to close up shop... However, Lena offered to organize a life drawing event in which she would pose nude to help Ed and Molly draw more customers in. Will it work?"),
            ("chapter > 5 and cafe_steal", "Ed is as kind and friendly as his wife, Molly. Together they run a café, which they opened several years back. Ed is in charge of the kitchen, and he's a great cook. He has always led a simple life and never wanted for anything more than to have a happy and fulfilling life near those he loves. His only regret is not having had a son...\nThe café was struggling, and it seemed like they would need to close up shop... Seeing she would lose this job soon, Lena decided to steal some money from the drawer to help her own finances at Ed and Molly's expense."),
            ("chapter > 5", "Ed is as kind and friendly as his wife, Molly. Together they run a café, which they opened several years back. Ed is in charge of the kitchen, and he's a great cook. He has always led a simple life and never wanted for anything more than to have a happy and fulfilling life near those he loves. His only regret is not having had a son...\nThe café was struggling, and things looked dire: Ed and Molly would need to close up shop, there was no way around it..."),
            ("True", "Ed is as kind and friendly as his wife, Molly. Together they run a café, which they opened several years back. Ed is in charge of the kitchen, and he's a great cook. He has always led a simple life and never wanted for anything more than to have a happy and fulfilling life near those he loves. His only regret is not having had a son..."),
        ]
    },
    'molly': {
        'bio': [
            ("chapter > 5 and cafe_music", "Molly is one of the kindest and most warm-hearted persons one can meet. She's been married to her loving husband, Ed, for many years, and together they opened a small business that they run together. She would've made for a great mom. Too bad she could never bear children... Maybe that's the reason she extends her motherly and heart-warming nature to those around her.\nThe café was struggling, and it seemed like they would need to close up shop... However, Lena offered to play a concert to help Ed and Molly draw more customers in. Will it work?"),
            ("chapter > 5 and cafe_nude", "Molly is one of the kindest and most warm-hearted persons one can meet. She's been married to her loving husband, Ed, for many years, and together they opened a small business that they run together. She would've made for a great mom. Too bad she could never bear children... Maybe that's the reason she extends her motherly and heart-warming nature to those around her.\nThe café was struggling, and it seemed like they would need to close up shop... However, Lena offered to organize a life drawing event in which she would pose nude to help Ed and Molly draw more customers in. Will it work?"),
            ("chapter > 5 and cafe_steal", "Molly is one of the kindest and most warm-hearted persons one can meet. She's been married to her loving husband, Ed, for many years, and together they opened a small business that they run together. She would've made for a great mom. Too bad she could never bear children... Maybe that's the reason she extends her motherly and heart-warming nature to those around her.\nThe café was struggling, and it seemed like they would need to close up shop... Seeing she would lose this job soon, Lena decided to steal some money from the drawer to help her own finances at Ed and Molly's expense."),
            ("chapter > 5", "Molly is one of the kindest and most warm-hearted persons one can meet. She's been married to her loving husband, Ed, for many years, and together they opened a small business that they run together. She would've made for a great mom. Too bad she could never bear children... Maybe that's the reason she extends her motherly and heart-warming nature to those around her.\nThe café was struggling, and things looked dire: Ed and Molly would need to close up shop, there was no way around it... "),
            ("True", "Molly is one of the kindest and most warm-hearted persons one can meet. She's been married to her loving husband, Ed, for many years, and together they opened a small business that they run together. She would've made for a great mom. Too bad she could never bear children... Maybe that's the reason she extends her motherly and heart-warming nature to those around her."),
        ]
    },
    'robert': {
        'bio': [
            ("chapter > 3 and lena_robert_sex and lena_robert_over", "Robert works as a head waiter in a prestigious restaurant, an achievement which he's proud of. His job's not his passion, though, but a means to pay the bills and enjoy the kind of life he wants. Right now, he's interested in partying and going out, but he would probably like to get a girlfriend, too... \nLena was trying to get over her breakup with Axel and, following Ivy's advice, decided to break her dry spell with Robert. They began a physical relationship, but Lena never saw Robert as boyfriend material. \nShe didn't take long to dump him, seeing their relationship wasn't going anywhere."),
            ("chapter > 2 and lena_robert_sex", "Robert works as a head waiter in a prestigious restaurant, an achievement which he's proud of. His job's not his passion, though, but a means to pay the bills and enjoy the kind of life he wants. Right now, he's interested in partying and going out, but he would probably like to get a girlfriend, too... \nLena was trying to get over her breakup with Axel and, following Ivy's advice, decided to break her dry spell with Robert. They began a physical relationship, but Lena never saw Robert as boyfriend material."),
            ("True", "Robert works as a head waiter in a prestigious restaurant, an achievement which he's proud of. His job's not his passion, though, but a means to pay the bills and enjoy the kind of life he wants. Right now, he's interested in partying and going out, but he would probably like to get a girlfriend, too..."),
        ]
    },
    'lenamom': {
        'bio': [
            ("True", "Lena's mom has always been a hard-working woman. Maybe too preoccupied with making ends meet to be as caring as Lena would've needed, she can be a bit obtuse and disregard her daughter's feelings. That's why they have always had a difficult relationship, to the extent that Lena knew from a very early age she wanted to go to live on her own."),
        ]
    },
    'lenadad': {
        'bio': [
            ("True", "Boris is a simple man. He learned the baker trade from his father and opened up his own bakery in the neighborhood after marrying Denna. He would've felt way more comfortable having a son rather than a daughter. He loves her dearly, and because of that, he always tends to be way too overprotective. He was diagnosed with cancer a couple of years ago, fell ill, and was forced to sell the bakery. Thankfully, he seems to be recovering."),
        ]
    },
    'wen': {
        'bio': [
            ("True", "You can always find Wen at the gym or at the bar, emptying bottle after bottle of beer. Those are his two passions: martial arts and drinking, and maybe also fucking around with people. Despite his short stature, he's built like a tank and was a high-caliber competitor when he was younger."),
        ]
    },
    'yuri': {
        'bio': [
            ("True", "Yuri is the kickboxing coach at the gym where Ian trains. Sometimes he's absent since he still goes to Thailand to train, even though he's been retired for a couple of years. However, he was a successful professional fighter, with twenty-three fights, with a record of nineteen wins and twelve knockouts."),
        ]
    },
    'lola': {
        'bio': [
            ("True", "Lola is Lena's cat. She's had her since she was sixteen and loves her very much. Not much can be said about Lola since she's just a normal house cat... Or is she?"),
        ]
    },
    'danny': {
        'bio': [
            ("True", "Danny's passion is art and photography, more specifically artistic nude portraits. Though he can't afford to work as a photographer full time yet, he's dedicated to making a name for himself and getting deeper into this scene. He met Ivy and Lena through a friend who's also a photographer and has wanted to shoot Lena since that day. If he ends up making it, he can be a good contact to have."),
        ]
    },
    'cherry': {
        'bio': [
            ("ian_active and chapter > 5 and ian_cherry_dating", "Cherry met Alison at the office, and they became friends. It's through her that Perry and Ian got to meet her. She's a stylish girl, and her stunning looks turn many heads. Cherry studied Fine Arts and loves avant-garde art, but she's been unable to make a living as a painter. Other than that, she's outgoing, nice and confident, but there's more to know about her... \nThe night Cherry met Ian, she ended up at his place and had sex with him, but it seems Cherry isn't looking for a relationship since she's already hung up on somebody. Despite that, she and Ian seemed to connect, and they hooked up a second time, and they are open to keep seeing each other from time to time."),
            ("ian_active and chapter > 1 and ian_cherry_sex", "Cherry met Alison at the office, and they became friends. It's through her that Perry and Ian got to meet her. She's a stylish girl, and her stunning looks turn many heads. Cherry studied Fine Arts and loves avant-garde art, but she's been unable to make a living as a painter. Other than that, she's outgoing, nice and confident, but there's more to know about her... \nThe night Cherry met Ian, she ended up at his place and had sex with him, but it seems Cherry isn't looking for a relationship."),
            ("True", "Cherry met Alison at the office, and they became friends. It's through her that Perry and Ian got to meet her. She's a stylish girl, and her stunning looks turn many heads. Cherry studied Fine Arts and loves avant-garde art, but she's been unable to make a living as a painter. Other than that, she's outgoing, nice and confident, but there's more to know about her..."),
            
            ("True", ""),
        ]
    },
    'mayor': {
        'bio': [
            ("True", "Thomas Vermeer is Perry's father and was elected Mayor of the city almost four years ago. He's affiliated with a left-leaning party, but due to the current and complicated economic situation, they have been falling short on their promised social policies. Perry doesn't want to have anything to do with the political struggles that his father is immersed in, and he feels he's a disappointment to his high-achieving father."),
        ]
    },
    'agnes': {
        'bio': [
            ("True", "Agnes Addingworth was born into a very wealthy family. That, and her tenacious attitude and intelligence enabled her to make a name for herself in the fashion business when not many women were yet able to. Thanks to her connections and an ambitious drive, she made a name for herself, a name she has been able to grow and maintain for decades. She's now considered one of the pioneers and celebrities of the current fashion scene."),
        ]
    },
    'jessb': {
        'bio': [
            ("True", "Jessica recently moved to the city, where she found work as a tattoo artist. It seems she hasn't led the safest and exemplary life, and the wear of her experiences show on her. She's an undeniably attractive girl, one who seemingly had all the opportunities she could want, but who rarely cracks a smile nowadays."),
        ]
    },
    'jessg': {
        'bio': [
            ("True", "Jessica recently moved to the city, where she found work as a tattoo artist. She's not only talented but also a strikingly beautiful and charming girl. Looks like she had a somewhat troubled youth, but now she's in a happy relationship."),
        ]
    },
    'mike': {
        'bio': [
            ("lena_active and chapter > 5 and lena_mike_dating", "Mike is a part-time DJ at Blazer club. He seems to be an easy-going guy, and his laid-back attitude and good looks make him pretty popular with people. He seems to have a good relationship with Jeremy and Ivy. He has a girlfriend, and they live together. \nLena met him at the club and was immediately attracted to him. After sleeping with Mike once, Lena knew she wanted to keep that relationship going, so she contacted him. It took just a bit of convincing, but Mike seems more than pleased to keep hooking up with Lena behind his girlfriend's back..."),
            ("lena_active and lena_mike_sex", "Mike is a part-time DJ at Blazer club. He seems to be an easy-going guy, and his laid-back attitude and good looks make him pretty popular with people. He seems to have a good relationship with Jeremy and Ivy. He has a girlfriend, and they live together. \nLena met him at the club and was immediately attracted to him. After flirting with him the whole night, she invited him over and had sex with him."),
            ("lena_active and v5_mike_dance", "Mike is a part-time DJ at Blazer club. He seems to be an easy-going guy, and his laid-back attitude and good looks make him pretty popular with people. He seems to have a good relationship with Jeremy and Ivy. He has a girlfriend, and they live together. \nLena met him at the club and was immediately attracted to him, but decided against taking things further since Mike is already in a relationship."),
            ("True", "Mike is a part-time DJ at Blazer club. He seems to be an easy-going guy, and his laid-back attitude and good looks make him pretty popular with people. He seems to have a good relationship with Jeremy and Ivy. He has a girlfriend, and they live together."),
        ]
    },
    'billy': {
        'bio': [
            ("True", "Billy used to be a friend of Jeremy's when they were kids, before Jeremy changed cities. They met again after a lot of years and they seem to have a lot in common: both enjoy the party life-style and want to have a good time. Seems Billy is well-off and wants to use his money to build up some sort of modeling brand, and he's looking for girls to work with and invest in."),
        ]
    },
    'victor': {
        'bio': [
            ("True", "Victor White is one of the few original best-selling authors who manage to survive current trend of corporate meddling by publishers. Acclaimed by his Science Fiction and fantasy novels, he's been building a name for himself for almost a decade, and even though he's far from a super-star, he is admired and respected in the right circles. One of his current projects is kickstarting an independent literary magazine."),
        ]
    },
}
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
