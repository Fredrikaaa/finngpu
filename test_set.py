# Test set for GPU matching validation
# Format: (ad_id, expected_model, listing_title)
# Including listing titles to make manual verification easier
test_cases = [
    # RTX 40 Series
    ("375419768", "GeForce RTX 4060 Ti 8 GB", "ASUS RTX 4060 TI DUAL OC 8GB"),
    ("362913580", "GeForce RTX 4060 8 GB", "Gigabyte RTX 4060"),
    ("375986952", "GeForce RTX 4060 Ti 8 GB", "ASUS DUAL GeForce RTX 4060 TI OC"),

    # RTX 30 Series
    ("377273776", "GeForce RTX 3090 24 GB", "GeForce RTX 3090 24Gb"),
    ("377163049", "GeForce RTX 3090 24 GB", "RTX 3090 24Gb ICHILL X4 Skjermkort"),
    ("377045548", "GeForce RTX 3090 24 GB", "RTX 3090 24Gb ICHILL X4 Skjermkort"),
    ("375377822", "GeForce RTX 3080 10 GB", "RTX 3080 HP 10GB"),
    ("369419877", "GeForce RTX 3080 10 GB", "KFA2 GeForce RTX 3080 SG LHR"),
    ("376581898", "GeForce RTX 3070 8 GB", "Asus RTX Geforce 3070 turbo 8G"),
    ("376565651", "GeForce RTX 3070 8 GB", "ASUS TUF Gaming GeForce RTX™ 3070"),
    ("374780709", "GeForce RTX 3070 8 GB", "GIGABYTE GeForce RTX 3070 AORUS MASTER 8GB GRAFIKKORT"),
    ("376570994", "GeForce RTX 3070 8 GB", "Gigabyte GeForce RTX 3070 GAMING OC 8G"),
    ("362958481", "GeForce RTX 3070 Ti 8 GB", "GIGABYTE GeForce RTX 3070 Ti EAGLE - Grafikkort"),
    ("375916333", "GeForce RTX 3070 Ti 8 GB", "ASUS GeForce RTX 3070 Ti TUF OC"),
    ("355431993", "GeForce RTX 3060 Ti 8 GB", "3060ti skjermkort gpu"),
    ("377333881", "GeForce RTX 3060 Ti 8 GB", "NVIDIA GeForce RTX 3060 Ti"),
    ("376926740", "GeForce RTX 3060 Ti 8 GB", "Asus GeForce RTX 3060 Ti TUF Gaming OC V2 8GB"),
    ("376880031", "GeForce RTX 3060 12 GB", "ASUS TUF Gaming RTX 3060 OC 12GB"),
    ("360210206", "GeForce RTX 3060 12 GB", "ZotacGaming Geforce RTX 3060 Twin Edge 12gb"),

    # RTX 20 Series
    ("374352532", "GeForce RTX 2080 Ti 11 GB", "RTX 2080 ti"),
    ("373724105", "GeForce RTX 2080 SUPER 8 GB", "Rtx 2080super phantom skjermkort"),
    ("374896144", "GeForce RTX 2080 SUPER 8 GB", "ASUS GeForce RTX 2080 SUPER ROG STRIX OC - 8GB"),
    ("369063129", "GeForce RTX 2080 8 GB", "2080 skjermkort"),
    ("377068200", "GeForce RTX 2070 SUPER 8 GB", "GeForce® RTX 2070 SUPER™ WINDFORCE OC 3X 8G"),
    ("374788058", "GeForce RTX 2070 SUPER 8 GB", "Geforce RTX 2070 Super"),
    ("377124051", "GeForce RTX 2070 8 GB", "MSI RTX 2070 8 GB Gaming X Skjermkor."),
    ("376352146", "GeForce RTX 2070 8 GB", "RTX 2070 selges til rimelig pris"),
    ("375321896", "GeForce RTX 2060 6 GB", "RTX 2060 6GB •RESERVERT•"),
    ("377365251", "GeForce RTX 2060 6 GB", "Rtx 2060"),
    ("377066532", "GeForce RTX 2060 6 GB", "GeForce RTX 2060 DUAL EVO OC"),
    ("372209649", "GeForce RTX 2060 12 GB", "RTX 2060 12GB"),

    # GTX 16 Series & 10 Series
    ("376565572", "GeForce GTX 1660 Ti 6 GB", "Skjermkort Geforce 1660 ti Ghost 6gb"),
    ("309585615", "GeForce GTX 1660 SUPER 6 GB", "Gtx 1660 super"),
    ("377342777", "GeForce GTX 1070 8 GB", "ZOTAC GeForce 1070 8GB SKJERMKORT"),
    ("374042153", "GeForce GTX 1070 8 GB", "MSI gtx 1070 8gb"),
    ("377027141", "GeForce GTX 1070 Ti 8 GB", "Gtx 1070 TI"),
    ("376707784", "GeForce GTX 1080 Ti 11 GB", "GeForce GTX 1080 Ti (11GB)"),
    ("375531879", "GeForce GTX 1080 Ti 11 GB", "ASUS ROG Strix GeForce GTX 1080Ti OC 11GB"),
    ("354559137", "GeForce GTX 1080 8 GB", "MSI GTX 1080 SEAHAWK væskeavkjølt skjermkort"),
    ("373835804", "GeForce GTX 1080 8 GB", "NVIDIA GeForce 1080 SeaHawk X"),

    # AMD RX 7000 Series
    ("377358170", "Radeon RX 7900 XT 20 GB", "Powercolor AMD Radeon RX 7900 XT"),
    ("373345714", "Radeon RX 7900 GRE 16 GB", "Asus Dual Radeon RX 7900 GRE OC"),

    # AMD RX 6000 Series
    ("376713885", "Radeon RX 6950 XT 16 GB", "Amd Radeon 6950 XT"),
    ("371599734", "Radeon RX 6950 XT 16 GB", "XFX Radeon RX 6950 XT Speedster MERC 319 Skjermkort GPU Grafikkort"),
    ("341971152", "Radeon RX 6800 XT 16 GB", "RED DRAGON RX 6800XT 16GB GDDR6 RAM"),
    ("377086143", "Radeon RX 6800 XT 16 GB", "Asus Radeon RX 6800 XT"),
    ("375099773", "Radeon RX 6800 16 GB", "Amd Radeon RX 6800 16GB"),
    ("355002214", "Radeon RX 6750 12 GB", "RX6750 Skjermkort"),
    ("377407953", "Radeon RX 6700 XT 12 GB", "Asus Dual RX 6700XT"),
    ("376777632", "Radeon RX 6700 XT 12 GB", "Skjermkort/AMD Radeon 6700xt 12gb"),
    ("367667852", "Radeon RX 6650 XT 8 GB", "ASUS Radeon RX 6650 XT Dual OC"),
    ("365695264", "Radeon RX 6600 8 GB", "PowerColor Radeon RX 6600 Fighter"),
    ("374523080", "Radeon RX 6600 8 GB", "Radeon RX 6600 - 8 GB"),

    # AMD RX 5000 Series
    ("376193084", "Radeon RX 5700 XT 8 GB", "Gigabyte Radeon RX 5700 XT Gaming OC 8GB"),
    ("356371536", "Radeon RX 5700 XT 8 GB", "ASUS Radeon RX 5700 XT ROG Strix OC"),
    ("376332758", "Radeon RX 5700 XT 8 GB", "ASUS TUF Gaming Kabinett, 750W GOLD PSU og RX5700XT GPU"),
    ("371591158", "Radeon RX 5700 8 GB", "Skjermkort"),
    ("376782459", "Radeon RX 5700 8 GB", "Sapphire Radeon RX 5700"),

    # AMD RX 500 Series
    ("328239638", "Radeon RX 580 8 GB", "Skjermkort - Sapphire Pulse RX 580 8GB"),
    ("368624257", "Radeon RX 590 8 GB", "Sapphire RX 590 Special Edition 8GB GDDR5 Graphics Card"),

    # Cases that should be Unknown
    ("366113912", "Unknown", "Lenovo NVIDIA RTX A2000  6 G Grafikkort Skjermkort GPU"),
    ("370794263", "Unknown", "Nvidia Quadro P2200 5GB GDDR5X GPU Grafikk kort"),
    ("376506528", "Unknown", "Quadro P2000 skjermkort"),
    ("374460089", "Unknown", "Nvidia Quadro RTX 5000 16Gb GPU"),
    ("345311634", "Unknown", "Samsung Radeon Rx Vega 64 8gb graphics card/ skjermkort"),
    ("377323462", "Unknown", "Sparkle Intel Arc A770 TITAN OC 16gb Vram"),
    ("302774728", "Unknown", "8 GPU RX 580 4GB mining rig Til salgs"),

    # Multi GPU Cases
    ("368437409", "Multi", "Nytt 4090 TUF OC, 6900xt,3060ti/70ti,  3070,PNY3070, turbo 3070, Zotac 3070ti"),
    ("376184828", "Multi", "2 stk RTX 2070 Super og 1 stk RTX 2080"),
    ("362401743", "Multi", "AMD RX skjermkort; 5600 XT og 6800 XT"),
    
    # Cases with specific details that might confuse matching
    ("377071360", "GeForce GTX 1070 8 GB", "Hovedkort, cpu, minne og gpu"),
    ("369822861", "GeForce RTX 2060 6 GB", "RTX 2060 gaming setup, 144hz monitor"),
    ("376753897", "GeForce GTX 1650 Super 4 GB", "HP Pavillion // 1650 SUPER // i5-11400 // 512gb SSD + 1TB HDD"),
    ("377116412", "GeForce GTX 1070 8 GB", "GTX 1070 / i7 6700"),
    
    # Mining rig related listings that contain GPU info
    ("236227325", "Multi", " B250 mining hovedkort 12 skjermkort [CPU G3900 MEDFØLGER] "),
    ("371240068", "Multi", "Miningrig uten GPU"),
]
