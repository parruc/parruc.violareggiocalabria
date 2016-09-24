# -*- coding: utf-8 -*-
from datetime import date
from datetime import datetime
from parruc.violareggiocalabria import _


base_perm = "parruc.violareggiocalabria: Add "


folders = [{"title": _(u"Partite"), "permission": base_perm + "Partita",
            "view": "partite", "slider": True},
           {"title": _(u"Roster"), "permission": base_perm + "Giocatore",
            "nextPreviousEnabled": True, "view": "giocatori"},
           {"title": _(u"News"), "permission": base_perm + "News Item",
            "nextPreviousEnabled": True, "view": "news", "slider": True},
           {"title": _(u"Sponsor"), "permission": base_perm + "Sponsor",
            "exclude_from_nav": True},
           {"title": _(u"Banner"), "permission": base_perm + "Banner",
            "exclude_from_nav": True},
           {"title": _(u"Leagues"), "permission": base_perm + "League",
            "exclude_from_nav": True},
           {"title": _(u"Partner"), "permission": base_perm + "Partner",
            "exclude_from_nav": True},
           {"title": _(u"Squadre"), "permission": base_perm + "Squadra",
            "exclude_from_nav": True},
           {"title": _(u"Società"), },
           {"title": _(u"Video"), "permission": base_perm + "Video",
            "exclude_from_nav": True},
           {"title": _(u"Slide"), "permission": "parruc.flexslider: Add Slide",
            "exclude_from_nav": True},
           {"title": _(u"Giovanili"), }, ]

pages = [{"title": _(u"Storia"), 'parent': "societa"},
         {"title": _(u"Club"), 'parent': "societa"},
         {"title": _(u"Pala Calafiore"), 'parent': "societa"},
         {"title": _(u"Caffè Mauro"), },
         {"title": _(u"Contatti"), "view": "contatti"},
         ]

links = [{"title": "Contact Info",
          "remoteUrl": "${navigation_root_url}/contatti", }]

leagues = [{"title": "A1", "description": _("Serie A1")},
           {"title": "A2", "description": _("Serie A2"), 'is_main': True},
           {"title": "Under 18", "description": _("under 18")}, ]

teams = [{"title": u"Givova Scafati", "played": 30, "points": 40,
          "image_logo": "loghi/givova-scafati.png",
          "image_teaser": "teaser1.jpg", "league_name": "A2", },
         {"title": u"BCC Agropoli", "played": 30, "points": 38,
          "image_logo": "loghi/bcc-agropoli.png",
          "image_teaser": "teaser1.jpg", "league_name": "A2", },
         {"title": u"Orsi Tortona", "played": 30, "points": 38,
          "image_logo": "loghi/orsi-tortona.png",
          "image_teaser": "teaser1.jpg", "league_name": "A2", },
         {"title": u"FMC Ferentino", "played": 30, "points": 36,
          "image_logo": "loghi/mfc-ferentino.png",
          "image_teaser": "teaser1.jpg", "league_name": "A2", },
         {"title": u"Mens Sana Basket 1871 Siena", "played": 30, "points": 36,
          "image_logo": "loghi/menssana-siena.png",
          "image_teaser": "teaser1.jpg", "league_name": "A2", },
         {"title": u"Moncada Agrigento", "played": 30, "points": 34,
          "image_logo": "loghi/moncada-agrigento.png",
          "image_teaser": "teaser1.jpg", "league_name": "A2", },
         {"title": u"Lighthouse Conad Trapani", "played": 30, "points": 32,
          "image_logo": "loghi/lighthouseconad-trapani.png",
          "image_teaser": "teaser1.jpg", "league_name": "A2", },
         {"title": u"Novipiù Casale Monferrato", "played": 30, "points": 30,
          "image_logo": "loghi/novapiu-casale.png",
          "image_teaser": "teaser1.jpg", "league_name": "A2", },
         {"title": u"Bermé Reggio Calabria", "played": 30, "points": 28,
          "image_logo": "loghi/viola-reggiocalabria.png", "league_name": "A2",
          "is_viola": True, "image_teaser": "teaser2.jpg"},
         {"title": u"Angelico Biella", "played": 30, "points": 28,
          "image_logo": "loghi/angelico-biella.png",
          "image_teaser": "teaser1.jpg", "league_name": "A2", },
         {"title": u"Assigeco Casalpusterlengo", "played": 30, "points": 26,
          "image_logo": "loghi/assigeco-casalpusterlengo.png",
          "image_teaser": "teaser1.jpg", "league_name": "A2", },
         {"title": u"Benacquista Ass. Latina", "played": 30, "points": 26,
          "image_logo": "loghi/latina-basket.png",
          "image_teaser": "teaser1.jpg", "league_name": "A2", },
         {"title": u"Npc Rieti", "played": 30, "points": 26,
          "image_logo": "loghi/npc-rieti.png",
          "image_teaser": "teaser1.jpg", "league_name": "A2", },
         {"title": u"Acea Roma", "played": 30, "points": 26,
          "image_logo": "loghi/acea-roma.png",
          "image_teaser": "teaser1.jpg", "league_name": "A2", },
         {"title": u"Paffoni Omegna", "played": 30, "points": 24,
          "image_logo": "loghi/paffoni-omegna.png",
          "image_teaser": "teaser1.jpg", "league_name": "A2", },
         {"title": u"La Briosa Barcellona", "played": 30, "points": 12,
          "image_logo": "loghi/briosa-barcellona.png",
          "image_teaser": "teaser1.jpg", "league_name": "A2", }, ]


partite = [{"title": u"Vittoria al cardiopalma",
            "home_index": 8, "away_index": 5, "match_type": "regular",
            "score_home": 99, "score_away": 75, "fb_link": "http://fb.com",
            "start": datetime(2016, 7, 1, 15, 30, 0), },
           {"title": u"Vittoria al cardiopalma", "match_type": "regular",
            "home_index": 8, "away_index": 9,
            "score_home": 88, "score_away": 87, "fb_link": "http://fb.com",
            "start": datetime(2016, 8, 1, 15, 30, 0), },
           {"title": u"Grande vittoria fuori casa", "match_type": "regular",
            "home_index": 2, "away_index": 8,
            "score_home": 45, "score_away": 98, "fb_link": "http://fb.com",
            "start": datetime(2016, 9, 1, 19, 30, 0), },
           {"title": u"Sconfitta di misura", "match_type": "regular",
            "home_index": 1, "away_index": 8,
            "score_home": 76, "score_away": 90, "fb_link": "http://fb.com",
            "start": datetime(2016, 10, 1, 21, 30, 0), }, ]

slides = [{"title": u"La viola mette a segno punti preziosi",
           "url": "/",
           "image": "slide1.jpg"},
          {"title": u"Un'altra vittoria per i ragazzi della Viola",
           "url": "/",
           "image": "slide2.jpg"}, ]

videos = [{"title": u"Coach Frates post Viola Tortona",
           "video_category": "interview",
           "url": "https://www.youtube.com/embed/BFTz_-bIVuM"},
          {"title": u"Valerio Costa post Viola Casalpusterlengo",
           "video_category": "interview",
          "url": "https://www.youtube.com/embed/18Op_UYJEYw"},
          {"title": u"Coach Bolignano post Viola Trapani",
           "video_category": "interview",
           "url": "https://www.youtube.com/embed/YjnDyeSrgYo"},
          {"title": u"Roberto Rullo post Viola Trapani",
           "video_category": "interview",
           "url": "https://www.youtube.com/embed/rzlLYloWQpM"}
          ]
players = [{"name": "Ion", "surname": "Lupusor", "role": "Ala", "height": 203,
            "weight": 95, "birth_date": date(1996, 1, 27),
            "image_path": "player.jpg",
            "stats": [{"year": "2015/2016", "played": 30, "score": 150,
                       "played_time": 502, "rebounds": 81, "blocked": 9,
                       "two_points_shots": 70, "two_points_shots_percent": 59,
                       "three_points_shots": 37,
                       "three_points_shots_percent": 30, }, ]
            },
           {"name": "Lorenzo", "surname": "Caroti", "role": "Playmaker",
            "height": 185, "weight": 75, "birth_date": date(1997, 7, 1),
            "image_path": "09-LorenzoCaroti.jpg",
            "stats": [{"year": "2015/2016", "played": 30, "score": 340,
                       "played_time": 865, "rebounds": 67, "blocked": 7,
                       "two_points_shots": 105, "two_points_shots_percent": 44,
                       "three_points_shots": 151,
                       "three_points_shots_percent": 32, }, ]
            },
           {"name": "Tommaso", "surname": "Guariglia", "role": "Centro",
            "height": 207, "birth_date": date(1997, 8, 8),
            "image_path": "player.jpg",
            "stats": [{"year": "2015/2016", "played": 26, "score": 207,
                       "played_time": 530, "rebounds": 143, "blocked": 15,
                       "two_points_shots": 158, "two_points_shots_percent": 56,
                       "three_points_shots": 2,
                       "three_points_shots_percent": 50, }, ]
            },
           {"name": "Celis", "surname": "Taflaj", "role": "Guardia",
            "height": 201, "weight": 81, "birth_date": date(1998, 3, 12),
            "image_path": "04-Celis_Taflaj.jpg",
            "stats": [{"year": "2015/2016", "played": 10, "score": 18,
                       "played_time": 85, "rebounds": 11, "blocked": 0,
                       "two_points_shots": 15, "two_points_shots_percent": 33,
                       "three_points_shots": 10,
                       "three_points_shots_percent": 10, }, ]
            },
           {"name": "Augustus", "surname": "Fabi", "role": "Ala",
            "height": 200, "birth_date": date(1991, 10, 22),
            "image_path": "10-AugustinFabi.jpg",
            "stats": [{"year": "2015/2016", "played": 24, "score": 186,
                       "played_time": 622, "rebounds": 76, "blocked": 2,
                       "two_points_shots": 83, "two_points_shots_percent": 34,
                       "three_points_shots": 100,
                       "three_points_shots_percent": 36, }, ]
            },
           {"name": "Roberto", "surname": "Marulli", "role": "Playmaker",
            "height": 190, "weight": 84, "birth_date": date(1991, 9, 21),
            "image_path": "22-RobertoMarulli.jpg",
            "stats": [{"year": "2015/2016", "played": 27, "score": 236,
                       "played_time": 616, "rebounds": 56, "blocked": 6,
                       "two_points_shots": 77, "two_points_shots_percent": 58,
                       "three_points_shots": 107,
                       "three_points_shots_percent": 36, }, ]
            },
           ]

news = [{"title": u"News diprova 1",
         "description": "Questa è una news di prova"},
        {"title": u"News diprova 2",
         "description": "Questa è una news di prova"},
        {"title": u"News diprova 3",
         "description": "Questa è una news di prova"},
        {"title": u"News diprova 4",
         "description": "Questa è una news di prova"},
        {"title": u"News diprova 5", "description":
         "Questa è una news di prova"}, ]

partners = [{"title": u"Partner 1", "image": "loghi/viola-reggiocalabria.png",
             "link": "http://fb.com"},
            {"title": u"Partner 2", "image": "loghi/viola-reggiocalabria.png",
             "link": "http://fb.com"},
            {"title": u"Partner 3", "image": "loghi/viola-reggiocalabria.png",
             "link": "http://fb.com"}]

sponsors = [{"title": u"Sponsor 1", "image": "loghi/viola-reggiocalabria.png",
             "link": "http://fb.com"},
            {"title": u"Sponsor 2", "image": "loghi/viola-reggiocalabria.png",
             "link": "http://fb.com"},
            {"title": u"Sponsor 3", "image": "loghi/viola-reggiocalabria.png",
             "link": "http://fb.com"},
            {"title": u"Sponsor 4", "image": "loghi/viola-reggiocalabria.png",
             "link": "http://fb.com"}]

banners = [{"title": u"Banner 1", "image": "banner-test-horizzontal.png",
            "weight": 10, "position": "horizzontal", "link": "http://fb.com"},
           {"title": u"Banner 2", "image": "banner-test-vertical.png",
            "weight": 20, "position": "vertical", "link": "http://fb.com"},
           {"title": u"Banner 3", "image": "banner-test-horizzontal.png",
            "weight": 10, "position": "horizzontal", "link": "http://fb.com"},
           {"title": u"Banner 4", "image": "banner-test-vertical.png",
            "weight": 20, "position": "vertical", "link": "http://fb.com"}]
