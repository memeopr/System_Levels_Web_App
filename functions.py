import numpy as np


def system_levels(high_freq, tilt_at_high_freq, carrier_level, carrier_freq, split_arg="Low"):
    split = {"Low": (42, 54),
             "Mid": (85, 102),
             "High": (204, 254)}
    low_freq = split[split_arg.capitalize()][1]

    freq = np.array([54,
                    55,
                    55.25,
                    61.25,
                    67.25,
                    77.25,
                    83.25,
                    85,
                    91.25,
                    97.25,
                    102,
                    103.25,
                    109.25,
                    115.25,
                    121.25,
                    127.25,
                    133.25,
                    139.25,
                    145.25,
                    151.25,
                    157.25,
                    163.25,
                    169.25,
                    175.25,
                    181.25,
                    187.25,
                    193.25,
                    199.25,
                    205.25,
                    211.25,
                    217.25,
                    223.25,
                    229.25,
                    235.25,
                    241.25,
                    247.25,
                    253.25,
                    254,
                    259.25,
                    265.25,
                    271.25,
                    277.25,
                    283.25,
                    289.25,
                    295.25,
                    301.25,
                    307.25,
                    313.25,
                    319.25,
                    325.25,
                    331.25,
                    337.25,
                    343.25,
                    349.25,
                    355.25,
                    361.25,
                    367.25,
                    373.25,
                    379.25,
                    385.25,
                    391.25,
                    397.25,
                    403.25,
                    409.25,
                    415.25,
                    421.25,
                    427.25,
                    433.25,
                    439.25,
                    445.25,
                    450,
                    451.25,
                    457.25,
                    463.25,
                    469.25,
                    475.25,
                    481.25,
                    487.25,
                    493.25,
                    499.25,
                    505.25,
                    511.25,
                    517.25,
                    523.25,
                    529.25,
                    535.25,
                    541.25,
                    547.25,
                    550,
                    553.25,
                    559.25,
                    565.25,
                    571.25,
                    577.25,
                    583.25,
                    589.25,
                    595.25,
                    601.25,
                    607.25,
                    613.25,
                    619.25,
                    625.25,
                    631.25,
                    637.25,
                    643.25,
                    649.25,
                    655.25,
                    661.25,
                    667.25,
                    673.25,
                    679.25,
                    685.25,
                    691.25,
                    697.25,
                    703.25,
                    709.25,
                    715.25,
                    721.25,
                    727.25,
                    733.25,
                    739.25,
                    745.25,
                    750,
                    751.25,
                    757.25,
                    763.25,
                    769.25,
                    775.25,
                    781.25,
                    787.25,
                    793.25,
                    799.25,
                    805.25,
                    811.25,
                    817.25,
                    823.25,
                    829.25,
                    835.25,
                    841.25,
                    847.25,
                    853.25,
                    859.25,
                    860,
                    865.25,
                    870,
                    871.25,
                    877.25,
                    883.25,
                    889.25,
                    895.25,
                    901.25,
                    907.25,
                    913.25,
                    919.25,
                    925.25,
                    931.25,
                    937.25,
                    943.25,
                    949.25,
                    955.25,
                    961.25,
                    967.25,
                    973.25,
                    979.25,
                    985.25,
                    991.25,
                    997.25,
                    1000,
                    1003.25,
                    1009.25,
                    1015.25,
                    1021.25,
                    1027.25,
                    1033.25,
                    1039.25,
                    1045.25,
                    1051.25,
                    1057.25,
                    1063.25,
                    1069.25,
                    1075.25,
                    1081.25,
                    1087.25,
                    1093.25,
                    1099.25,
                    1105.25,
                    1111.25,
                    1117.25,
                    1123.25,
                    1129.25,
                    1135.25,
                    1141.25,
                    1147.25,
                    1153.25,
                    1159.25,
                    1165.25,
                    1171.25,
                    1177.25,
                    1183.25,
                    1189.25,
                    1195.25,
                    1201.25,
                    1207.25,
                    1213.25,
                    1218])
    freq = freq[np.where(freq == low_freq)[0][0]:np.where(freq <= high_freq)[0][-1] + 1]
    level = tilt_at_high_freq/(high_freq - low_freq) * (freq - carrier_freq) + carrier_level
    return freq, level


def mystery_freq(high_freq, tilt_at_high_freq, carrier_level, carrier_freq, freq, split_arg="Low"):
    split = {"Low": (42, 54),
             "Mid": (85, 102),
             "High": (204, 254)}
    low_freq = split[split_arg.capitalize()][1]

    level = tilt_at_high_freq / (high_freq - low_freq) * (freq - carrier_freq) + carrier_level
    return freq, level


def system_levels2(fh, lh, fl, ll, split_arg="Low"):
    split = {"Low": (42, 54),
             "Mid": (85, 102),
             "High": (204, 254)}
    low_freq = split[split_arg.capitalize()][1]
    freq = np.array([54,
                     55,
                     55.25,
                     61.25,
                     67.25,
                     77.25,
                     83.25,
                     85,
                     91.25,
                     97.25,
                     102,
                     103.25,
                     109.25,
                     115.25,
                     121.25,
                     127.25,
                     133.25,
                     139.25,
                     145.25,
                     151.25,
                     157.25,
                     163.25,
                     169.25,
                     175.25,
                     181.25,
                     187.25,
                     193.25,
                     199.25,
                     205.25,
                     211.25,
                     217.25,
                     223.25,
                     229.25,
                     235.25,
                     241.25,
                     247.25,
                     253.25,
                     254,
                     259.25,
                     265.25,
                     271.25,
                     277.25,
                     283.25,
                     289.25,
                     295.25,
                     301.25,
                     307.25,
                     313.25,
                     319.25,
                     325.25,
                     331.25,
                     337.25,
                     343.25,
                     349.25,
                     355.25,
                     361.25,
                     367.25,
                     373.25,
                     379.25,
                     385.25,
                     391.25,
                     397.25,
                     403.25,
                     409.25,
                     415.25,
                     421.25,
                     427.25,
                     433.25,
                     439.25,
                     445.25,
                     450,
                     451.25,
                     457.25,
                     463.25,
                     469.25,
                     475.25,
                     481.25,
                     487.25,
                     493.25,
                     499.25,
                     505.25,
                     511.25,
                     517.25,
                     523.25,
                     529.25,
                     535.25,
                     541.25,
                     547.25,
                     550,
                     553.25,
                     559.25,
                     565.25,
                     571.25,
                     577.25,
                     583.25,
                     589.25,
                     595.25,
                     601.25,
                     607.25,
                     613.25,
                     619.25,
                     625.25,
                     631.25,
                     637.25,
                     643.25,
                     649.25,
                     655.25,
                     661.25,
                     667.25,
                     673.25,
                     679.25,
                     685.25,
                     691.25,
                     697.25,
                     703.25,
                     709.25,
                     715.25,
                     721.25,
                     727.25,
                     733.25,
                     739.25,
                     745.25,
                     750,
                     751.25,
                     757.25,
                     763.25,
                     769.25,
                     775.25,
                     781.25,
                     787.25,
                     793.25,
                     799.25,
                     805.25,
                     811.25,
                     817.25,
                     823.25,
                     829.25,
                     835.25,
                     841.25,
                     847.25,
                     853.25,
                     859.25,
                     860,
                     865.25,
                     870,
                     871.25,
                     877.25,
                     883.25,
                     889.25,
                     895.25,
                     901.25,
                     907.25,
                     913.25,
                     919.25,
                     925.25,
                     931.25,
                     937.25,
                     943.25,
                     949.25,
                     955.25,
                     961.25,
                     967.25,
                     973.25,
                     979.25,
                     985.25,
                     991.25,
                     997.25,
                     1000,
                     1003.25,
                     1009.25,
                     1015.25,
                     1021.25,
                     1027.25,
                     1033.25,
                     1039.25,
                     1045.25,
                     1051.25,
                     1057.25,
                     1063.25,
                     1069.25,
                     1075.25,
                     1081.25,
                     1087.25,
                     1093.25,
                     1099.25,
                     1105.25,
                     1111.25,
                     1117.25,
                     1123.25,
                     1129.25,
                     1135.25,
                     1141.25,
                     1147.25,
                     1153.25,
                     1159.25,
                     1165.25,
                     1171.25,
                     1177.25,
                     1183.25,
                     1189.25,
                     1195.25,
                     1201.25,
                     1207.25,
                     1213.25,
                     1218])
    freq = freq[np.where(freq == low_freq)[0][0]:np.where(freq <= fh)[0][-1] + 1]
    slope = (lh-ll)/(fh-fl)
    level = slope * (freq - fh) + lh
    return freq, level


def mystery_freq2(freqh, levelh, freql, levell, freq_arg, split_arg="Low"):
    split = {"Low": (42, 54),
             "Mid": (85, 102),
             "High": (204, 254)}
    low_freq = split[split_arg.capitalize()][1]

    slope = (levelh - levell) / (freqh - freql)
    level = slope * (freq_arg - freqh) + levelh
    return freq_arg, level

def find_tilt(f1, f2):
    return


ncta_dict = {
            '2': (54, 60, 55.25, 57),
            '3': (60, 66, 61.25, 63),
            '4': (66, 72, 67.25, 69),
            '5': (76, 82, 77.25, 79),
            '6': (82, 88, 83.25, 85),
            '95': (90, 96, 91.25, 93),
            '96': (96, 102, 97.25, 99),
            '97': (102, 108, 103.25, 105),
            '98': (108, 114, 109.275, 111),
            '99': (114, 120, 115.275, 117),
            '14': (120, 126, 121.2625, 123),
            '15': (126, 132, 127.2625, 129),
            '16': (132, 138, 133.2625, 135),
            '17': (138, 144, 139.25, 141),
            '18': (144, 150, 145.25, 147),
            '19': (150, 156, 151.25, 153),
            '20': (156, 162, 157.25, 159),
            '21': (162, 168, 163.25, 165),
            '22': (168, 174, 169.25, 171),
            '7': (174, 180, 175.25, 177),
            '8': (180, 186, 181.25, 183),
            '9': (186, 192, 187.25, 189),
            '10': (192, 198, 193.25, 195),
            '11': (198, 204, 199.25, 201),
            '12': (204, 210, 205.25, 207),
            '13': (210, 216, 211.25, 213),
            '23': (216, 222, 217.25, 219),
            '24': (222, 228, 223.25, 225),
            '25': (228, 234, 229.2625, 231),
            '26': (234, 240, 235.2625, 237),
            '27': (240, 246, 241.2625, 243),
            '28': (246, 252, 247.2625, 249),
            '29': (252, 258, 253.2625, 255),
            '30': (258, 264, 259.2625, 261),
            '31': (264, 270, 265.2625, 267),
            '32': (270, 276, 271.2625, 273),
            '33': (276, 282, 277.2625, 279),
            '34': (282, 288, 283.2625, 285),
            '35': (288, 294, 289.2625, 291),
            '36': (294, 300, 295.2625, 297),
            '37': (300, 306, 301.2625, 303),
            '38': (306, 312, 307.2625, 309),
            '39': (312, 318, 313.2625, 315),
            '40': (318, 324, 319.2625, 321),
            '41': (324, 330, 325.2625, 327),
            '42': (330, 336, 331.275, 333),
            '43': (336, 342, 337.2625, 339),
            '44': (342, 348, 343.2625, 345),
            '45': (348, 354, 349.2625, 351),
            '46': (354, 360, 355.2625, 357),
            '47': (360, 366, 361.2625, 363),
            '48': (366, 372, 367.2625, 369),
            '49': (372, 378, 373.2625, 375),
            '50': (378, 384, 379.2625, 381),
            '51': (384, 390, 385.2625, 387),
            '52': (390, 396, 391.2625, 393),
            '53': (396, 402, 397.2625, 399),
            '54': (402, 408, 403.25, 405),
            '55': (408, 414, 409.25, 411),
            '56': (414, 420, 415.25, 417),
            '57': (420, 426, 421.25, 423),
            '58': (426, 432, 427.25, 429),
            '59': (432, 438, 433.25, 435),
            '60': (438, 444, 439.25, 441),
            '61': (444, 450, 445.25, 447),
            '62': (450, 456, 451.25, 453),
            '63': (456, 462, 457.25, 459),
            '64': (462, 468, 463.25, 465),
            '65': (468, 474, 469.25, 471),
            '66': (474, 480, 475.25, 477),
            '67': (480, 486, 481.25, 483),
            '68': (486, 492, 487.25, 489),
            '69': (492, 498, 493.25, 495),
            '70': (498, 504, 499.25, 501),
            '71': (504, 510, 505.25, 507),
            '72': (510, 516, 511.25, 513),
            '73': (516, 522, 517.25, 519),
            '74': (522, 528, 523.25, 525),
            '75': (528, 534, 529.25, 531),
            '76': (534, 540, 535.25, 537),
            '77': (540, 546, 541.25, 543),
            '78': (546, 552, 547.25, 549),
            '79': (552, 558, 553.25, 555),
            '80': (558, 564, 559.25, 561),
            '81': (564, 570, 565.25, 567),
            '82': (570, 576, 571.25, 573),
            '83': (576, 582, 577.25, 579),
            '84': (582, 588, 583.25, 585),
            '85': (588, 594, 589.25, 591),
            '86': (594, 600, 595.25, 597),
            '87': (600, 606, 601.25, 603),
            '88': (606, 612, 607.25, 609),
            '89': (612, 618, 613.25, 615),
            '90': (618, 624, 619.25, 621),
            '91': (624, 630, 625.25, 627),
            '92': (630, 636, 631.25, 633),
            '93': (636, 642, 637.25, 639),
            '94': (642, 648, 643.25, 645),
            '100': (648, 654, 649.25, 651),
            '101': (654, 660, 655.25, 657),
            '102': (660, 666, 661.25, 663),
            '103': (666, 672, 667.25, 669),
            '104': (672, 678, 673.25, 675),
            '105': (678, 684, 679.25, 681),
            '106': (684, 690, 685.25, 687),
            '107': (690, 696, 691.25, 693),
            '108': (696, 702, 697.25, 699),
            '109': (702, 708, 703.25, 705),
            '110': (708, 714, 709.25, 711),
            '111': (714, 720, 715.25, 717),
            '112': (720, 726, 721.25, 723),
            '113': (726, 732, 727.25, 729),
            '114': (732, 738, 733.25, 735),
            '115': (738, 744, 739.25, 741),
            '116': (744, 750, 745.25, 747),
            '117': (750, 756, 751.25, 753),
            '118': (756, 762, 757.25, 759),
            '119': (762, 768, 763.25, 765),
            '120': (768, 774, 769.25, 771),
            '121': (774, 780, 775.25, 777),
            '122': (780, 786, 781.25, 783),
            '123': (786, 792, 787.25, 789),
            '124': (792, 798, 793.25, 795),
            '125': (798, 804, 799.25, 801),
            '126': (804, 810, 805.25, 807),
            '127': (810, 816, 811.25, 813),
            '128': (816, 822, 817.25, 819),
            '129': (822, 828, 823.25, 825),
            '130': (828, 834, 829.25, 831),
            '131': (834, 840, 835.25, 837),
            '132': (840, 846, 841.25, 843),
            '133': (846, 852, 847.25, 849),
            '134': (852, 858, 853.25, 855),
            '135': (858, 864, 859.25, 861),
            '136': (864, 870, 865.25, 867),
            '137': (870, 876, 871.25, 873),
            '138': (876, 882, 877.25, 879),
            '139': (882, 888, 883.25, 885),
            '140': (888, 894, 889.25, 891),
            '141': (894, 900, 895.25, 897),
            '142': (900, 906, 901.25, 903),
            '143': (906, 912, 907.25, 909),
            '144': (912, 918, 913.25, 915),
            '145': (918, 924, 919.25, 921),
            '146': (924, 930, 925.25, 927),
            '147': (930, 936, 931.25, 933),
            '148': (936, 942, 937.25, 939),
            '149': (942, 948, 943.25, 945),
            '150': (948, 954, 949.25, 951),
            '151': (954, 960, 955.25, 957),
            '152': (960, 966, 961.25, 963),
            '153': (966, 972, 967.25, 969),
            '154': (972, 978, 973.25, 975),
            '155': (978, 984, 979.25, 981),
            '156': (984, 990, 985.25, 987),
            '157': (990, 996, 991.25, 993),
            '158': (996, 1002, 997.25, 999),
            '159': (1002, 1008, 1003.25, 1005),
            '160': (1008, 1014, 1009.25, 1011),
            '161': (1014, 1020, 1015.25, 1017),
            '162': (1020, 1026, 1021.25, 1023),
            '163': (1026, 1032, 1027.25, 1029),
            '164': (1032, 1038, 1033.25, 1035),
            '165': (1038, 1044, 1039.25, 1041),
            '166': (1044, 1050, 1045.25, 1047),
            '167': (1050, 1056, 1051.25, 1053),
            '168': (1056, 1062, 1057.25, 1059),
            '169': (1062, 1068, 1063.25, 1065),
            '170': (1068, 1074, 1069.25, 1071),
            '171': (1074, 1080, 1075.25, 1077),
            '172': (1080, 1086, 1081.25, 1083),
            '173': (1086, 1092, 1087.25, 1089),
            '174': (1092, 1098, 1093.25, 1095),
            '175': (1098, 1104, 1099.25, 1101),
            '176': (1104, 1110, 1105.25, 1107),
            '177': (1110, 1116, 1111.25, 1113),
            '178': (1116, 1122, 1117.25, 1119),
            '179': (1122, 1128, 1123.25, 1125),
            '180': (1128, 1134, 1129.25, 1131),
            '181': (1134, 1140, 1135.25, 1137),
            '182': (1140, 1146, 1141.25, 1143),
            '183': (1146, 1152, 1147.25, 1149),
            '184': (1152, 1158, 1153.25, 1155),
            '185': (1158, 1164, 1159.25, 1161),
            '186': (1164, 1170, 1165.25, 1167),
            '187': (1170, 1176, 1171.25, 1173),
            '188': (1176, 1182, 1177.25, 1179),
            '189': (1182, 1188, 1183.25, 1185),
            '190': (1188, 1194, 1189.25, 1191),
            '191': (1194, 1200, 1195.25, 1197),
            '192': (1200, 1206, 1201.25, 1203),
            '193': (1206, 1212, 1207.25, 1209),
            '194': (1212, 1218, 1213.25, 1215),
            '195': (1218, 1224, 1219.25, 1221),
            '196': (1224, 1230, 1225.25, 1227)
            }

ncta = [[2, 54, 60, 55.25, 57],
        [3, 60, 66, 61.25, 63],
        [4, 66, 72, 67.25, 69],
        [5, 76, 82, 77.25, 79],
        [6, 82, 88, 83.25, 85],
        [95, 90, 96, 91.25, 93],
        [96, 96, 102, 97.25, 99],
        [97, 102, 108, 103.25, 105],
        [98, 108, 114, 109.275, 111],
        [99, 114, 120, 115.275, 117],
        [14, 120, 126, 121.2625, 123],
        [15, 126, 132, 127.2625, 129],
        [16, 132, 138, 133.2625, 135],
        [17, 138, 144, 139.25, 141],
        [18, 144, 150, 145.25, 147],
        [19, 150, 156, 151.25, 153],
        [20, 156, 162, 157.25, 159],
        [21, 162, 168, 163.25, 165],
        [22, 168, 174, 169.25, 171],
        [7, 174, 180, 175.25, 177],
        [8, 180, 186, 181.25, 183],
        [9, 186, 192, 187.25, 189],
        [10, 192, 198, 193.25, 195],
        [11, 198, 204, 199.25, 201],
        [12, 204, 210, 205.25, 207],
        [13, 210, 216, 211.25, 213],
        [23, 216, 222, 217.25, 219],
        [24, 222, 228, 223.25, 225],
        [25, 228, 234, 229.2625, 231],
        [26, 234, 240, 235.2625, 237],
        [27, 240, 246, 241.2625, 243],
        [28, 246, 252, 247.2625, 249],
        [29, 252, 258, 253.2625, 255],
        [30, 258, 264, 259.2625, 261],
        [31, 264, 270, 265.2625, 267],
        [32, 270, 276, 271.2625, 273],
        [33, 276, 282, 277.2625, 279],
        [34, 282, 288, 283.2625, 285],
        [35, 288, 294, 289.2625, 291],
        [36, 294, 300, 295.2625, 297],
        [37, 300, 306, 301.2625, 303],
        [38, 306, 312, 307.2625, 309],
        [39, 312, 318, 313.2625, 315],
        [40, 318, 324, 319.2625, 321],
        [41, 324, 330, 325.2625, 327],
        [42, 330, 336, 331.275, 333],
        [43, 336, 342, 337.2625, 339],
        [44, 342, 348, 343.2625, 345],
        [45, 348, 354, 349.2625, 351],
        [46, 354, 360, 355.2625, 357],
        [47, 360, 366, 361.2625, 363],
        [48, 366, 372, 367.2625, 369],
        [49, 372, 378, 373.2625, 375],
        [50, 378, 384, 379.2625, 381],
        [51, 384, 390, 385.2625, 387],
        [52, 390, 396, 391.2625, 393],
        [53, 396, 402, 397.2625, 399],
        [54, 402, 408, 403.25, 405],
        [55, 408, 414, 409.25, 411],
        [56, 414, 420, 415.25, 417],
        [57, 420, 426, 421.25, 423],
        [58, 426, 432, 427.25, 429],
        [59, 432, 438, 433.25, 435],
        [60, 438, 444, 439.25, 441],
        [61, 444, 450, 445.25, 447],
        [62, 450, 456, 451.25, 453],
        [63, 456, 462, 457.25, 459],
        [64, 462, 468, 463.25, 465],
        [65, 468, 474, 469.25, 471],
        [66, 474, 480, 475.25, 477],
        [67, 480, 486, 481.25, 483],
        [68, 486, 492, 487.25, 489],
        [69, 492, 498, 493.25, 495],
        [70, 498, 504, 499.25, 501],
        [71, 504, 510, 505.25, 507],
        [72, 510, 516, 511.25, 513],
        [73, 516, 522, 517.25, 519],
        [74, 522, 528, 523.25, 525],
        [75, 528, 534, 529.25, 531],
        [76, 534, 540, 535.25, 537],
        [77, 540, 546, 541.25, 543],
        [78, 546, 552, 547.25, 549],
        [79, 552, 558, 553.25, 555],
        [80, 558, 564, 559.25, 561],
        [81, 564, 570, 565.25, 567],
        [82, 570, 576, 571.25, 573],
        [83, 576, 582, 577.25, 579],
        [84, 582, 588, 583.25, 585],
        [85, 588, 594, 589.25, 591],
        [86, 594, 600, 595.25, 597],
        [87, 600, 606, 601.25, 603],
        [88, 606, 612, 607.25, 609],
        [89, 612, 618, 613.25, 615],
        [90, 618, 624, 619.25, 621],
        [91, 624, 630, 625.25, 627],
        [92, 630, 636, 631.25, 633],
        [93, 636, 642, 637.25, 639],
        [94, 642, 648, 643.25, 645],
        [100, 648, 654, 649.25, 651],
        [101, 654, 660, 655.25, 657],
        [102, 660, 666, 661.25, 663],
        [103, 666, 672, 667.25, 669],
        [104, 672, 678, 673.25, 675],
        [105, 678, 684, 679.25, 681],
        [106, 684, 690, 685.25, 687],
        [107, 690, 696, 691.25, 693],
        [108, 696, 702, 697.25, 699],
        [109, 702, 708, 703.25, 705],
        [110, 708, 714, 709.25, 711],
        [111, 714, 720, 715.25, 717],
        [112, 720, 726, 721.25, 723],
        [113, 726, 732, 727.25, 729],
        [114, 732, 738, 733.25, 735],
        [115, 738, 744, 739.25, 741],
        [116, 744, 750, 745.25, 747],
        [117, 750, 756, 751.25, 753],
        [118, 756, 762, 757.25, 759],
        [119, 762, 768, 763.25, 765],
        [120, 768, 774, 769.25, 771],
        [121, 774, 780, 775.25, 777],
        [122, 780, 786, 781.25, 783],
        [123, 786, 792, 787.25, 789],
        [124, 792, 798, 793.25, 795],
        [125, 798, 804, 799.25, 801],
        [126, 804, 810, 805.25, 807],
        [127, 810, 816, 811.25, 813],
        [128, 816, 822, 817.25, 819],
        [129, 822, 828, 823.25, 825],
        [130, 828, 834, 829.25, 831],
        [131, 834, 840, 835.25, 837],
        [132, 840, 846, 841.25, 843],
        [133, 846, 852, 847.25, 849],
        [134, 852, 858, 853.25, 855],
        [135, 858, 864, 859.25, 861],
        [136, 864, 870, 865.25, 867],
        [137, 870, 876, 871.25, 873],
        [138, 876, 882, 877.25, 879],
        [139, 882, 888, 883.25, 885],
        [140, 888, 894, 889.25, 891],
        [141, 894, 900, 895.25, 897],
        [142, 900, 906, 901.25, 903],
        [143, 906, 912, 907.25, 909],
        [144, 912, 918, 913.25, 915],
        [145, 918, 924, 919.25, 921],
        [146, 924, 930, 925.25, 927],
        [147, 930, 936, 931.25, 933],
        [148, 936, 942, 937.25, 939],
        [149, 942, 948, 943.25, 945],
        [150, 948, 954, 949.25, 951],
        [151, 954, 960, 955.25, 957],
        [152, 960, 966, 961.25, 963],
        [153, 966, 972, 967.25, 969],
        [154, 972, 978, 973.25, 975],
        [155, 978, 984, 979.25, 981],
        [156, 984, 990, 985.25, 987],
        [157, 990, 996, 991.25, 993],
        [158, 996, 1002, 997.25, 999],
        [159, 1002, 1008, 1003.25, 1005],
        [160, 1008, 1014, 1009.25, 1011],
        [161, 1014, 1020, 1015.25, 1017],
        [162, 1020, 1026, 1021.25, 1023],
        [163, 1026, 1032, 1027.25, 1029],
        [164, 1032, 1038, 1033.25, 1035],
        [165, 1038, 1044, 1039.25, 1041],
        [166, 1044, 1050, 1045.25, 1047],
        [167, 1050, 1056, 1051.25, 1053],
        [168, 1056, 1062, 1057.25, 1059],
        [169, 1062, 1068, 1063.25, 1065],
        [170, 1068, 1074, 1069.25, 1071],
        [171, 1074, 1080, 1075.25, 1077],
        [172, 1080, 1086, 1081.25, 1083],
        [173, 1086, 1092, 1087.25, 1089],
        [174, 1092, 1098, 1093.25, 1095],
        [175, 1098, 1104, 1099.25, 1101],
        [176, 1104, 1110, 1105.25, 1107],
        [177, 1110, 1116, 1111.25, 1113],
        [178, 1116, 1122, 1117.25, 1119],
        [179, 1122, 1128, 1123.25, 1125],
        [180, 1128, 1134, 1129.25, 1131],
        [181, 1134, 1140, 1135.25, 1137],
        [182, 1140, 1146, 1141.25, 1143],
        [183, 1146, 1152, 1147.25, 1149],
        [184, 1152, 1158, 1153.25, 1155],
        [185, 1158, 1164, 1159.25, 1161],
        [186, 1164, 1170, 1165.25, 1167],
        [187, 1170, 1176, 1171.25, 1173],
        [188, 1176, 1182, 1177.25, 1179],
        [189, 1182, 1188, 1183.25, 1185],
        [190, 1188, 1194, 1189.25, 1191],
        [191, 1194, 1200, 1195.25, 1197],
        [192, 1200, 1206, 1201.25, 1203],
        [193, 1206, 1212, 1207.25, 1209],
        [194, 1212, 1218, 1213.25, 1215],
        [195, 1218, 1224, 1219.25, 1221],
        [196, 1224, 1230, 1225.25, 1227]]


def find_channel(freq, ncta=ncta):
    for i in ncta:
        if i[1] <= freq < i[2]:
            return i[0]


def find_freq(ch, ncta=ncta):
    for i in ncta:
        if i[0] == ch:
            return i[4]


def total_power(y):
    y_m = np.power(10, y/10)
    y_sum = np.sum(y_m)
    power = 10 * np.log10(y_sum)
    return power


if __name__ == "__main__":
    x, y = system_levels(1218, 17, 52, 1218, split_arg="low")
    w, z = mystery_freq(1200, 14.5, 52, 1200, 1201, split_arg="low")
    print(w, z)

    freq = 875.99
    ch = 75
    print(freq, find_channel(freq, ncta))

    print(ch, find_freq(ch, ncta))

    print(total_power(y))

    # To create .exe I used the following command in terminal:
    # pyinstaller --onefile --windowed --clean --icon icon.ico --name System_levels gui.py





