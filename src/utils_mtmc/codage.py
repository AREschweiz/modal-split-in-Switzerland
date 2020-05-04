# coding=latin-1


dict_detailed_mode2main_mode_2015 = {1: 'A pied',  # Zu Fuss -> LV
                                     2: 'V�lo (incl. v�lo �lectrique)',  # Velo -> LV
                                     3: 'Deux-roues motoris�',  # Mofa, Motorfahrrad
                                     4: 'Deux-roues motoris�',  # Kleinmotorrad
                                     5: 'Deux-roues motoris�',  # Motorrad als Fahrer
                                     6: 'Deux-roues motoris�',  # Motorrad als Mitfahrer
                                     7: 'Voiture',  # Auto als Fahrer
                                     8: 'Voiture',  # Auto als Mitfahrer
                                     9: 'Train',  # Bahn/Zug
                                     10: 'Transports publics routiers',  # Postauto
                                     11: 'Transports publics routiers',  # Bus/Schulbus
                                     12: 'Transports publics routiers',  # Tram/Metro
                                     13: 'Autres',  # Taxi
                                     14: 'Autres',  # Reisecar
                                     15: 'Autres',  # Lastwagen
                                     16: 'Autres',  # Schiff, Boot
                                     17: 'Autres',  # Flugzeug / Luftfahrzeug
                                     18: 'Autres',  # Zahnradbahn, Standseilbahn, Seilbahn, Sessellift, Skilift
                                     19: 'Autres',  # Fahrzeugaehnliche Geraete
                                     20: 'V�lo (incl. v�lo �lectrique)',  # E-Bike ohne Kontrollschild
                                     21: 'V�lo (incl. v�lo �lectrique)',  # E-Bike mit gelbem Kontrollschild
                                     95: 'Autres',  # Anderes
                                     -99: 'Autres',  # Pseudoetappe
                                     -98: 'Autres',  # Keine Antwort
                                     -97: 'Autres'}  # Weiss nicht

dict_detailed_mode2main_mode_2010 = {1: 'A pied',  # Zu Fuss -> LV
                                     2: 'V�lo',  # Velo -> LV
                                     3: 'Deux-roues motoris�',  # Mofa, Motorfahrrad
                                     4: 'Deux-roues motoris�',  # Kleinmotorrad
                                     5: 'Deux-roues motoris�',  # Motorrad als Fahrer
                                     6: 'Deux-roues motoris�',  # Motorrad als Mitfahrer
                                     7: 'Voiture',  # Auto als Fahrer
                                     8: 'Voiture',  # Auto als Mitfahrer
                                     9: 'Train',  # Bahn/Zug
                                     10: 'Transports publics routiers',  # Postauto
                                     11: 'Transports publics routiers',  # Bus/Schulbus
                                     12: 'Transports publics routiers',  # Tram/Metro
                                     13: 'Autres',  # Taxi
                                     14: 'Autres',  # Reisecar
                                     15: 'Autres',  # Lastwagen
                                     16: 'Autres',  # Schiff, Boot
                                     17: 'Autres',  # Flugzeug / Luftfahrzeug
                                     18: 'Autres',  # Zahnradbahn, Standseilbahn, Seilbahn, Sessellift, Skilift
                                     19: 'Autres',  # Fahrzeugaehnliche Geraete
                                     20: 'Autres',  #
                                     -99: 'Autres'}  # Pseudoetappe

dict_detailed_mode2main_mode_2005 = {1: 'A pied',  # zu Fuss
                                     2: 'V�lo',  # Velo
                                     3: 'Deux-roues motoris�',  # Mofa, Motorfahrrad
                                     4: 'Deux-roues motoris�',  # Kleinmotorrad
                                     5: 'Deux-roues motoris�',
                                     6: 'Deux-roues motoris�',
                                     7: 'Voiture',
                                     8: 'Voiture',
                                     9: 'Train',
                                     10: 'Transports publics routiers',
                                     11: 'Transports publics routiers',
                                     12: 'Transports publics routiers',
                                     13: 'Autres',
                                     14: 'Autres',
                                     15: 'Autres',
                                     16: 'Autres',
                                     17: 'Autres',
                                     18: 'Autres',
                                     19: 'Autres',
                                     20: 'Autres',
                                     -99: 'Autres'}

dict_main_mode2group_of_modes_2015 = {'Autres': 'Autres',
                                      'A pied': 'Mobilit� douce',
                                      'V�lo (incl. v�lo �lectrique)': 'Mobilit� douce',
                                      'Deux-roues motoris�': 'Transport individuel motoris�',
                                      'Voiture': 'Transport individuel motoris�',
                                      'Transports publics routiers': 'Transports publics',
                                      'Train': 'Transports publics'}

dict_main_mode2group_of_modes_2010 = {'Autres': 'Autres',
                                      'A pied': 'Mobilit� douce',
                                      'V�lo': 'Mobilit� douce',
                                      'Deux-roues motoris�': 'Transport individuel motoris�',
                                      'Voiture': 'Transport individuel motoris�',
                                      'Transports publics routiers': 'Transports publics',
                                      'Train': 'Transports publics'}


dict_nb_centre_hors_agglo_bfs = {90306: 'Lyss',
                                 90329: 'Langenthal',
                                 90404: 'Burgdorf',
                                 90412: 'Kirchberg (BE)',
                                 90768: 'Spiez',
                                 91103: 'Sursee',
                                 91301: 'Einsiedeln',
                                 91362: 'Arth',
                                 91372: 'Schwyz',
                                 91407: 'Sarnen',
                                 91509: 'Stans',
                                 92275: 'Murten',
                                 92407: 'Oensingen',
                                 92583: 'Sch�nenwerd',
                                 93293: 'Mels - Sargans',
                                 93339: 'Uznach',
                                 93379: 'Wattwil',
                                 93402: 'Flawil',
                                 93787: 'St. Moritz',
                                 93851: 'Davos',
                                 93955: 'Landquart',
                                 94141: 'Reinach (AG)',
                                 94304: 'D�ttingen-B�ttstein',
                                 94946: 'Weinfelden',
                                 95401: 'Aigle',
                                 95822: 'Payerne',
                                 96300: 'Zermatt',
                                 96800: 'Porrentruy'}


dict_nb_agglo_bfs = {3251: 'Rheintal (CH)',
                     2125: 'Bulle',
                     6153: 'Monthey',
                     4260: 'Stein (AG) (CH)',
                     6248: 'Sierre',
                     5192: 'Lugano (CH)',
                     4401: 'Arbon - Rorschach',
                     6266: 'Sion',
                     5113: 'Locarno (CH)',
                     6421: 'La Chaux-de-Fonds - Le Locle (CH)',
                     4082: 'Wohlen (AG)',
                     1630: 'Glarus',
                     5938: 'Yverdon-les-Bains',
                     2546: 'Grenchen',
                     3271: 'Buchs (SG) (CH)',
                     6458: 'Neuch�tel',
                     5890: 'Vevey - Montreux',
                     5002: 'Bellinzona',
                     1711: 'Zug',
                     4671: 'Kreuzlingen (CH)',
                     6136: 'Martigny',
                     4436: 'Amriswil - Romanshorn',
                     5586: 'Lausanne',
                     6711: 'Del�mont (CH)',
                     5250: 'Chiasso - Mendrisio (CH)',
                     1344: 'Lachen',
                     3425: 'Wil (SG)',
                     4566: 'Frauenfeld',
                     2196: 'Fribourg',
                     3901: 'Chur',
                     2601: 'Solothurn',
                     6621: 'Gen�ve (CH)',
                     2939: 'Schaffhausen (CH)',
                     1061: 'Luzern',
                     3203: 'St. Gallen',
                     581: 'Interlaken',
                     942: 'Thun',
                     4021: 'Baden - Brugg',
                     1201: 'Altdorf (UR)',
                     261: 'Z�rich',
                     2701: 'Basel (CH)',
                     230: 'Winterthur',
                     2581: 'Olten - Zofingen',
                     4201: 'Lenzburg',
                     351: 'Bern',
                     4001: 'Aarau',
                     371: 'Biel/Bienne',
                     3336: 'Rapperswil-Jona - R�ti',
                     6002: 'Brig - Visp'}
