# Test set for GPU matching validation
# Format: (ad_id, expected_model, listing_title)
# Including listing titles to make manual verification easier
test_cases = [

    # NVIDIA GPUs
    ("190878936", "GeForce GTX 1080 8 GB", "MSI GeForce GTX 1080 Gaming X! Lite brukt, selges rimelig."),
    ("262624107", "GeForce RTX 2060 6 GB", "Msi 2060 Gaming Z"),
    ("273919170", "GeForce RTX 2080 Ti 11 GB", "Asus ROG Strix RTX2080TI OC 11 Gaming"),
    ("279544829", "GeForce RTX 3060 Ti 8 GB", "gpu GeForce RTX 3060 Ti GAMING Z TRIO 8G LHR NY"),
    ("287137806", "GeForce RTX 3060 Ti 8 GB", "GeForce RTX 3060 Ti GAMING X 8G LHR"),
    ("306155637", "GeForce RTX 3060 12 GB", "RTX 3060 zotac 12gb"),
    ("309585615", "GeForce GTX 1660 SUPER 6 GB", "Gtx 1660 super"),
    ("320435726", "GeForce RTX 2060 6 GB", "GeForce RTX ZOTAC 2060"),
    ("323803923", "GeForce GTX 1070 8 GB", "Komplett Gamer Premium i150 + BenQ 24\" selges brukt"),
    ("329969572", "GeForce RTX 2070 8 GB", "NVIDIA GeForce RTX 2070 MSI Armor 8GB"),
    ("333070541", "GeForce RTX 2060 SUPER 8 GB", "Nvidia Graffikkort RTX 2060S 8GB!"),
    ("336571027", "GeForce RTX 3070 8 GB", "MSI RTX 3070 Supreme X gpu"),
    ("340984589", "GeForce GTX 1080 Ti 11 GB", "Hp Omen 880-109no"),
    ("341853146", "GeForce RTX 2080 Ti 11 GB", "Dell Presision 3640 Perfekt for VR Gaming."),
    ("341981334", "GeForce GTX 1060 6 GB", "Brukt Gaming maskin i3-7100 3.9Ghz, 8 GB RAM, 2x 256 GB SSD uten lisens"),
    ("343030548", "GeForce GTX 1070 8 GB", "Skjermkort MSI GeForce GTX 1070 ARMOR 8G OC"),
    ("343127039", "GeForce RTX 3080 10 GB", "ZOTAC GAMING GeForce RTX 3080 Trinity"),
    ("343360620", "GeForce GTX 1660 SUPER 6 GB", "GTX skjermkort"),
    ("346082927", "GeForce GTX 1080 8 GB", "Zotac GeForce GTX 1080 AMP EXTREME 8GB"),
    ("348965763", "GeForce RTX 4060 8 GB", "RTX 4060 GAMING OC 8GB (KUN GPU)"),
    ("349072622", "GeForce RTX 3070 Ti 8 GB", "Skjermkort Gigabyte RTX 3070ti"),
    ("353362563", "GeForce GTX 1070 8 GB", "MSI gtx 1070 8gb"),
    ("354559137", "GeForce GTX 1080 8 GB", "MSI GTX 1080 SEAHAWK væskeavkjølt skjermkort"),
    ("355431993", "GeForce RTX 3060 Ti 8 GB", "3060ti skjermkort gpu"),
    ("358981520", "GeForce GTX 1070 Ti 8 GB", "Datamaskin sett"),
    ("359957859", "GeForce RTX 2060 SUPER 8 GB", "Asus RTX2060S 8GB Turbo EVO"),
    ("360210206", "GeForce RTX 3060 12 GB", "ZotacGaming Geforce RTX 3060 Twin Edge 12gb"),
    ("361920143", "GeForce RTX 2060 SUPER 8 GB", "Asus RTX 2060S - GPU"),
    ("362913580", "GeForce RTX 4060 8 GB", "Gigabyte RTX 4060"),
    ("362958481", "GeForce RTX 3070 Ti 8 GB", "GIGABYTE GeForce RTX 3070 Ti EAGLE - Grafikkort"),
    ("364638491", "GeForce RTX 2080 Ti 11 GB", "RTX 2080 Ti på Vannkjøler (AIO)"),
    ("368480336", "GeForce GTX 1650 SUPER 4 GB", "Hp pavilion gaming PRIS KAN DISKUTERES"),
    ("368491248", "GeForce RTX 2070 8 GB", "Acer Predator Orion 3000 P03-600"),
    ("368491322", "GeForce GTX 1080 Ti 11 GB", "EVGA GEFORCE GTX 1080Ti FTW3 edition"),
    ("368798902", "GeForce RTX 2060 6 GB", "Komplett Gamer - 144Hz Edition"),
    ("369063129", "GeForce RTX 2080 8 GB", "2080 skjermkort"),
    ("369286763", "GeForce RTX 2080 8 GB", "ASUS GeForce RTX 2080 ROG Strix OC 8GB"),
    ("369419877", "GeForce RTX 3080 10 GB", "KFA2 GeForce RTX 3080 SG LHR"),
    ("369442800", "GeForce RTX 3080 10 GB", "Skjermkort Nvidia RTX 3080 OEM - 10 gb"),
    ("369463637", "GeForce RTX 3060 12 GB", "Geforce RTX 3060 12G"),
    ("369797821", "GeForce RTX 2070 SUPER 8 GB", "EVGA GEFORCE RTX 2070 Super XC Ultra Skjermkort"),
    ("369822861", "GeForce RTX 2060 6 GB", "RTX 2060 gaming setup, 144hz monitor"),
    ("369908670", "GeForce GTX 1070 8 GB", "Skjermkort - GeForce GTX 1070"),
    ("370351250", "GeForce RTX 3080 10 GB", "Asia Geforce etc 3080 TUF GAMING"),
    ("370352732", "GeForce RTX 3070 8 GB", "GeForce RTX™ 3070 VENTUS 3X OC # PRIS KAN DISKUTERES #"),
    ("370424423", "GeForce GTX 1070 8 GB", "GeForce GTX 1070 Quick Silver 8G OC"),
    ("370432532", "GeForce GTX 1070 8 GB", "MSI Gaming PS"),
    ("370643612", "GeForce RTX 3060 Ti 8 GB", "Rtx 3060 Ti 8gb MSI"),
    ("370875638", "GeForce RTX 3080 10 GB", "GIGABYTE RTX 3080 VISION OC"),
    ("370971848", "GeForce RTX 2080 SUPER 8 GB", "ASUS GeForce RTX 2080 SUPER DUAL EVO OC V2"),
    ("371619717", "GeForce GTX 1080 8 GB", "Nvidia 1080 Seahawk Vannkjølt. Stillegående (bare GPU)"),
    ("371725136", "GeForce RTX 3060 Ti 8 GB", "GeForce RTX™ 3060 Ti GAMING OC PRO 8G (rev. 2.0)"),
    ("372202786", "GeForce RTX 3060 Ti 8 GB", "GAMING PAKKE SELGES!!!!"),
    ("372209649", "GeForce RTX 2060 12 GB", "RTX 2060 12GB"),
    ("372529667", "GeForce GTX 1650 4 GB", "Acer Aspire // i5-11400f // 16gb RAM // GTX 1650"),
    ("372663343", "GeForce RTX 3060 12 GB", "3060 Geforce Rtx"),
    ("372856549", "GeForce RTX 3070 Ti 8 GB", "Nvidia Geforce RTX 3070 Ti Founders Edition"),
    ("372960714", "GeForce GTX 1650 4 GB", "Gaming setup"),
    ("373026502", "GeForce GTX 1660 SUPER 6 GB", "Full gaming pakke (Komplett premium i120++)"),
    ("373076316", "GeForce GTX 1080 Ti 11 GB", "Asus ROG Strix GeForce GTX 1080 Ti OC grafikkort 11G"),
    ("373098923", "GeForce GTX 1070 8 GB", "Asus strix gtx1070 8g gaming"),
    ("373201202", "GeForce RTX 3070 8 GB", "Grafikkort EVGA 3070 stor utgave, pent brukt!"),
    ("373201615", "GeForce RTX 3070 8 GB", "RTX geforce 3070 gpu! Salg!!"),
    ("373202118", "GeForce RTX 3070 8 GB", "Gainward Salg på 3070 rtx skjermkort! Salg!"),
    ("373202202", "GeForce RTX 3070 8 GB", "Salg på palit 3070 rtx skjermkort! Salg!"),
    ("373202303", "GeForce RTX 2070 SUPER 8 GB", "RTX 2070 super! Salg!"),
    ("373612728", "GeForce RTX 3070 8 GB", "Selger et MSI RTX 3070 Suprim X 8G LHR grafikk-kort."),
    ("373644889", "GeForce GTX 1080 Ti 11 GB", "ASUS GTX 1080 TI STRIX i perfekt tilstand"),
    ("373835804", "GeForce GTX 1080 8 GB", "NVIDIA GeForce 1080 SeaHawk X"),
    ("373940998", "GeForce RTX 3060 12 GB", "Lenovo legion t5"),
    ("374042153", "GeForce GTX 1070 8 GB", "MSI gtx 1070 8gb"),
    ("374109514", "GeForce GTX 1060 6 GB", "GamingPoint CHARGER RGB"),
    ("374352532", "GeForce RTX 2080 Ti 11 GB", "RTX 2080 ti"),
    ("374506297", "GeForce RTX 3060 Ti 8 GB", "Nvidia Geforce RTX 3060 TI"),
    ("374622137", "GeForce RTX 3060 12 GB", "(Vurderes solgt!) HP Pavilion TG01 R5-5"),
    ("374632603", "GeForce RTX 2060 SUPER 8 GB", "Gainward GeForce RTX 2060 SUPER Ghost 8gb"),
    ("374780709", "GeForce RTX 3070 8 GB", "GIGABYTE GeForce RTX 3070 AORUS MASTER 8GB GRAFIKKORT"),
    ("374788058", "GeForce RTX 2070 SUPER 8 GB", "Geforce RTX 2070 Super"),
    ("374820954", "GeForce RTX 2070 8 GB", "RTX 2070 - intel core i7-8700"),
    ("374896144", "GeForce RTX 2080 SUPER 8 GB", "ASUS GeForce RTX 2080 SUPER ROG STRIX OC - 8GB"),
    ("375206544", "GeForce GTX 1080 8 GB", "GTX 1080 fra Asus Rog Strix - Perfekt for gamingriggen"),
    ("375233518", "GeForce RTX 2070 8 GB", "Asus GeForce ROG Strix RTX 2070 OC grafikkort 8G"),
    ("375321896", "GeForce RTX 2060 6 GB", "RTX 2060 6GB •RESERVERT•"),
    ("375419768", "GeForce RTX 4060 Ti 8 GB", "ASUS RTX 4060 TI DUAL OC 8GB"),
    ("375835453", "GeForce RTX 3060 12 GB", "Komplett epic gaming Rtx 3060"),
    ("375916333", "GeForce RTX 3070 Ti 8 GB", "ASUS GeForce RTX 3070 Ti TUF OC"),
    ("375966586", "GeForce GTX 1080 Ti 11 GB", "ASUS GeForce GTX 1080Ti ROG Strix Gaming"),
    ("375986952", "GeForce RTX 4060 Ti 8 GB", "ASUS DUAL GeForce RTX 4060 TI OC"),
    ("376023380", "GeForce GTX 1660 SUPER 6 GB", "Gaming setup"),
    ("376030780", "GeForce RTX 3070 8 GB", "RTX Asus tuf 3070 Skjermkort"),
    ("376163907", "GeForce GTX 1080 Ti 11 GB", "Komplett Battlebox Ultimate GeForce GTX 1080Ti 11GB , Core i7-8700K, 32GB"),
    ("376208776", "GeForce RTX 3060 Ti 8 GB", "GeForce RTX 3060 Ti VENTUS 2X OC"),
    ("376352146", "GeForce RTX 2070 8 GB", "RTX 2070 selges til rimelig pris"),
    ("376565651", "GeForce RTX 3070 8 GB", "ASUS TUF Gaming GeForce RTX™ 3070"),
    ("376570994", "GeForce RTX 3070 8 GB", "Gigabyte GeForce RTX 3070 GAMING OC 8G"),
    ("376581898", "GeForce RTX 3070 8 GB", "Asus RTX Geforce 3070 turbo 8G"),
    ("376702098", "GeForce RTX 2070 SUPER 8 GB", "ASUS GeForce RTX 2070 SUPER ROG Strix OC Advanced Edition"),
    ("376756096", "GeForce RTX 3060 12 GB", "RTX 3060 12(!)GB"),
    ("376880031", "GeForce RTX 3060 12 GB", "ASUS TUF Gaming RTX 3060 OC 12GB"),
    ("376926740", "GeForce RTX 3060 Ti 8 GB", "Asus GeForce RTX 3060 Ti TUF Gaming OC V2 8GB"),
    ("377066532", "GeForce RTX 2060 6 GB", "GeForce RTX 2060 DUAL EVO OC"),
    ("377273776", "GeForce RTX 3090 24 GB", "GeForce RTX 3090 24Gb"),
    ("377342777", "GeForce GTX 1070 8 GB", "ZOTAC GeForce 1070 8GB SKJERMKORT"),
    ("377606872", "GeForce GTX 1070 8 GB", "Asus GTX1070 Skjermkort"),
    ("377699877", "GeForce GTX 1080 8 GB", "Gigabyte Nvidia 1080 GPU"),
    ("377706612", "GeForce GTX 1080 Ti 11 GB", "ASUS GeForce GTX 1080 Ti ROG Strix"),
    ("377707696", "GeForce GTX 1080 8 GB", "Nvidia Gefors Gtx1080 Fonder Edition"),
    ("377709592", "GeForce RTX 3060 Ti 8 GB", "Geforce RTX 3060Ti 8GB"),
    ("377734033", "GeForce RTX 2060 SUPER 8 GB", "GeForce RTX 2060 Dual OC, 8GB skjermkort"),

    # AMD GPUs
    ("295746765", "Radeon RX 590 8 GB", "XFX Radeon RX590 8GB"),
    ("328239638", "Radeon RX 580 8 GB", "Skjermkort - Sapphire Pulse RX 580 8GB"),
    ("341971152", "Radeon RX 6800 XT 16 GB", "RED DRAGON RX 6800XT 16GB GDDR6 RAM"),
    ("344551685", "Radeon RX 6500 XT 4 GB", "AMD radeon RX 6500 XT"),
    ("354979726", "Radeon RX 5700 8 GB", "AMD RX5700 i god stand selges"),
    ("355002214", "Radeon RX 6750 XT 12 GB", "RX6750 Skjermkort"),
    ("356371536", "Radeon RX 5700 XT 8 GB", "ASUS Radeon RX 5700 XT ROG Strix OC"),
    ("359441264", "Radeon RX 6900 XT 16 GB", "Raedon 6900XT"),
    ("360962892", "Radeon RX 6900 XT 16 GB", "AMD RADEON RX 6900 XT"),
    ("365180872", "Radeon RX 6700 XT 12 GB", "RX 6700 XT Skjermkort"),
    ("365695264", "Radeon RX 6600 8 GB", "PowerColor Radeon RX 6600 Fighter"),
    ("367271764", "Radeon RX 6600 XT 8 GB", "ASUS Radeon RX6600XT DUAL OC"),
    ("367667852", "Radeon RX 6650 XT 8 GB", "ASUS Radeon RX 6650 XT Dual OC"),
    ("368624257", "Radeon RX 590 8 GB", "Sapphire RX 590 Special Edition 8GB GDDR5 Graphics Card"),
    ("369971200", "Radeon RX 6900 XT 16 GB", "6900xt"),
    ("370138656", "Radeon RX 580 8 GB", "Asus ROG-STRIX-RX580-T8G-GAMING"),
    ("370405331", "Radeon RX 6600 8 GB", "MSI Radeon 6600"),
    ("371591158", "Radeon RX 5700 8 GB", "Skjermkort"),
    ("371599734", "Radeon RX 6950 XT 16 GB", "XFX Radeon RX 6950 XT Speedster MERC 319 Skjermkort GPU Grafikkort"),
    ("371727614", "Radeon RX 6700 XT 12 GB", "RX 6700 XT Speedster Qick 319 GPU"),
    ("371758716", "Radeon RX 6900 XT 16 GB", "AMD RADEON RX 6900 XT"),
    ("371834349", "Radeon RX 580 8 GB", "Rog Strix RX580 T8G Gaming"),
    ("373345714", "Radeon RX 7900 GRE 16 GB", "Asus Dual Radeon RX 7900 GRE OC"),
    ("374523080", "Radeon RX 6600 8 GB", "Radeon RX 6600 - 8 GB"),
    ("374981509", "Radeon RX 6950 XT 16 GB", "RX 6950 XT || Med kvittering!"),
    ("375099773", "Radeon RX 6800 16 GB", "Amd Radeon RX 6800 16GB"),
    ("375288343", "Radeon RX 6600 8 GB", "XFX Radeon RX 6600 SPEEDSTER SWFT 210 CORE"),
    ("375364761", "Radeon RX 6600 XT 8 GB", "Kraftig Gaming maskin selges BILLIG!"),
    ("375629474", "Radeon RX 5700 XT 8 GB", "InWin GRone Full Tower Svart RGB  i5 7400 3,0GHz, 16GB, 128GB SSD, 1TB"),
    ("376743349", "Radeon RX 580 8 GB", "Blackmagic eGPU"),
    ("376777632", "Radeon RX 6700 XT 12 GB", "Skjermkort/AMD Radeon 6700xt 12gb"),
    ("376782459", "Radeon RX 5700 8 GB", "Sapphire Radeon RX 5700"),
    ("377086143", "Radeon RX 6800 XT 16 GB", "Asus Radeon RX 6800 XT"),
    ("377668382", "Radeon RX 7700 XT 12 GB", "Sapphire PULSE AMD Radeon RX 7700 XT"),

    # Multi GPUs
    ("301727097", "Multi", "Selger 9 stk skjermkort!"),
    ("362401743", "Multi", "AMD RX skjermkort; 5600 XT og 6800 XT"),
    ("368437409", "Multi", "Nytt 4090 TUF OC, 6900xt,3060ti/70ti,  3070,PNY3070, turbo 3070, Zotac 3070ti"),
    ("376184828", "Multi", "2 stk RTX 2070 Super og 1 stk RTX 2080"),

    # Unknown GPUs
    ("186553432", "Unknown", "BANANA PI med Touch Skjerm 7″ mm."),
    ("197103206", "Unknown", "HP ProDesk 600 G1 SFF med Windows pro versjon"),
    ("210334582", "Unknown", "Onda D1800 BTC 6 GPU HK. Med cpu og 8 gb ram"),
    ("211030768", "Unknown", "Fujitsu Esprimo Windows11/Office2021 Nvidia 1050/Intel Q8300/8Gb RAM/360Gb SSD"),
    ("218966099", "Unknown", "Selger en top geforce GTX 780 Ti skjermkort med vannblokk"),
    ("237636385", "Unknown", "Gtx880m 4gb og kjøleplate for asus g750 serien"),
    ("238005694", "Unknown", "strømforsyning"),
    ("245307215", "Unknown", "HP 1200w server strømforsyning med breakout board og 12 kabler"),
    ("246389117", "Unknown", "Riserless hovedkort med plass til 8 GPU"),
    ("248292079", "Unknown", "PowerColor Red Dragon Radeon™ RX 570 4GB - Nytt kort"),
    ("254206491", "Unknown", "Skjermkort Nvidia Titan X 12 GB"),
    ("259045002", "Unknown", "Asrock H110 Pro BTC"),
    ("262092327", "Unknown", "ZOTAC ZBOX ID90"),
    ("268511754", "Unknown", "Nvidia PNY Quadro P5000 16GB"),
    ("280866222", "Unknown", "I7-6700-3400ghz,  16gb ram, 480gb ssd,  gpu (gtx970 4gb)"),
    ("287543955", "Unknown", "Utrulig arbeidsstasjoner med GPU og Windows 11 Pro"),
    ("298403201", "Unknown", "MSI Radon R9 380 Gaming 4gb"),
    ("315146332", "Unknown", "HP Z400 med 2.93 Xeon Quad CPU/10GB RAM/Enkelt skjermkort."),
    ("319642054", "Unknown", "Ny LOUQE RAW S1 mini ITX"),
    ("320903793", "Unknown", "Selvbygd datamaskin"),
    ("325177640", "Unknown", "Hp Z600 workstation"),
    ("327871429", "Unknown", "skjermkort msi gtx 960 gi bud"),
    ("329035256", "Unknown", "MSI Codex 3"),
    ("330556392", "Unknown", "Dell T3600 Xeon E5-1620  Quatro K4000"),
    ("330797746", "Unknown", "Intel i7  2600 / Gtx 960  / 8 Gb ddr3/ corsair 500W / Med eller uten SSD !"),
    ("332007145", "Unknown", "Datamaskin"),
    ("333629803", "Unknown", "Ati rage fury maxx agp skjermkort"),
    ("333825410", "Unknown", "MASSE datautstyr og deler - RAM, CPUer, GPUer, gamingtastatur, headset, mus++++"),
    ("336138344", "Unknown", "ATI Rage LT Pro 8MB SDRAM AGP Video Graphics Card- 109-55700-00"),
    ("338264544", "Unknown", "LOUQE Ghost S1 MK III  Arctic White - [NY]"),
    ("338944206", "Unknown", "NVIDIA Jetson Nano 2GB (Ny)"),
    ("345311634", "Unknown", "Samsung Radeon Rx Vega 64 8gb graphics card/ skjermkort"),
    ("346235525", "Unknown", "Gigabyte GA-990FXA-UD5, S-AM3+, AMD Phenom II X6 1090T Black Ed CPU og 12 GB RAM"),
    ("350424764", "Unknown", "Viftefrie skjermkort"),
    ("350643862", "Unknown", "Gaming rig med Ryzen 7 1800x, Vega 64 og 144Hz skjerm, mus, EK vannblokk, m.m!"),
    ("351376977", "Unknown", "Ekstern GPU m thunderbolt"),
    ("352240276", "Unknown", "CPU: i9 9900x Hovedkort: ASUS Prime x299 deluxe"),
    ("352922618", "Unknown", "Håndholdt Android terminal med integrert kvitteringsskriver"),
    ("356800877", "Unknown", "HP Pavilion Gaming Desktop"),
    ("358990501", "Unknown", "3450w! PSU"),
    ("359598161", "Unknown", "Retro Gaming: Asus 7900 GTX King Kong Limited Edition"),
    ("360236019", "Unknown", "NZXT Gaming datamaskin"),
    ("360692311", "Unknown", "14stk. Diverse Vintage Grafikkort"),
    ("360932309", "Unknown", "HP EliteDesk 800 G3 (TWR) med Windows 11 Pro, 32GB RAM, 512GB NVMe, 1TB SSD"),
    ("361056849", "Unknown", "HP EliteOne 800 (All-in-One) med Windows 11 Pro, 16GB RAM, 2 stk. 256GB SSD"),
    ("361317238", "Unknown", "NZXT H510 Alliance Limited Edition"),
    ("361592154", "Unknown", "Kraftig Lenovo ThinkCentre M720S pakke med Windows 11 Pro (24H2 versjon)"),
    ("361959373", "Unknown", "Lenovo V520S, Intel i5-7400, DDR4-8gb, SSD M2-128Gb, HDD-1Tb, Wi-Fi, Win 10 Pro"),
    ("361980305", "Unknown", "Asus Eee Top ET2002T - All-in-one desktop"),
    ("362483988", "Unknown", "Hp z4 G4 Server/workstation i9-7900x"),
    ("362490234", "Unknown", "gaming setup (ny pris!!!)"),
    ("363747046", "Unknown", "Aorus B550I PRO - Ryzen 9 3900X - 16GB 3000MHz"),
    ("364161121", "Unknown", "🔴 MSI RADEON RX VEGA 56 AirBoost OC Edition + Original Box"),
    ("365399486", "Unknown", "Hovedkort - ROG STRIX X570-E Gaming"),
    ("366113912", "Unknown", "Lenovo NVIDIA RTX A2000  6 G Grafikkort Skjermkort GPU"),
    ("367180380", "Unknown", "2 x Geforce GTX 680 kort"),
    ("367447424", "Unknown", "6U NAS Kabinett med SAS backplane - Passer i 60cm rack!"),
    ("367562535", "Unknown", "Rimelig gaming maskin"),
    ("368075062", "Unknown", "Server HP Proliant DL380 gen9"),
    ("368157918", "Unknown", "HP ProDesk 600 med Windows 11 Pro, 16GB RAM, 256GB SSD og 1TB HDD"),
    ("368158855", "Unknown", "HP ProDesk 400 G4 (SFF) med Windows 11 Pro, 32GB RAM og 1TB SSD"),
    ("368419172", "Unknown", "2400w psu. 1200w psu. 750w psu. Hovedkort. Skjermkort etc"),
    ("368633429", "Unknown", "SilverStone Sugo SG15"),
    ("368963933", "Unknown", "HP ProDesk"),
    ("368999457", "Unknown", "HP ProDesk 600 G5 SFF White!"),
    ("369276174", "Unknown", "Lenovo ThinkCentre med I5-8500T, 16Gb RAM, 256Gb NVME"),
    ("369821672", "Unknown", "Cooler Master Cosmos C700p"),
    ("369868244", "Unknown", "Dell T7500 workstation"),
    ("370254835", "Unknown", "Quadro P2200 skjermkort"),
    ("370342064", "Unknown", "ASUS TUF SABERTOOTH X58, i7 960, 12GB Kingston DDR3"),
    ("370497980", "Unknown", "Intel i7-7700, ASUS ROG Strix B250F Gaming, Ballistix 16GB RAM"),
    ("370581148", "Unknown", "Intel i9-10900X Prosessor LGA2066 (Uåpnet)"),
    ("370781696", "Unknown", "NVIDIA Quadro P4000 8GB VRAM"),
    ("370794263", "Unknown", "Nvidia Quadro P2200 5GB GDDR5X GPU Grafikk kort"),
    ("371075547", "Unknown", "*RESERVERT* IBM Aptiva P233mhz med 3dfx Voodoo 1"),
    ("371305683", "Unknown", "Selges Billig: kraftig desktop, Lenovo ThinkStation P510"),
    ("371473839", "Unknown", "i9 9900k 5.0 GHz"),
    ("371517170", "Unknown", "Fractal Design Node 202 med strømforsyning"),
    ("371546209", "Unknown", "Msi Nightblade MI3"),
    ("371966730", "Unknown", "SONNET eGFX Breakaway Box 550"),
    ("372349051", "Unknown", "Nvidia Quadro 6000"),
    ("372580059", "Unknown", "Strøken ikke brukt Quadro M4000 Nvidia  8GB Vram"),
    ("372724808", "Unknown", "Asus 27\" 4K gamingskjerm ROG Strix XG27UQ"),
    ("372850314", "Unknown", "Selger kabinett samt power supply og skjermkort. Det medfører et hovedkort."),
    ("372925719", "Unknown", "Acer Nitro N50-640 (LES BESKRIVELSE)"),
    ("373537465", "Unknown", "Dell 9020 pakke med Windows 11 Pro, 16GB RAM og 256GB SSD"),
    ("373740208", "Unknown", "Hovedkort, CPU og Skjermkort selges"),
    ("373923203", "Unknown", "MSI GE66 Raider Gaming Laptop"),
    ("374156380", "Unknown", "ASUS ROG Strix B550-E GAMING Hovedkort"),
    ("374199803", "Unknown", "Dell Tower 7910 + Lenovo D32\""),
    ("374393869", "Unknown", "HP EliteDesk 800 G3 Mini 65W med Windows 11 Pro, 16GB RAM, 256GB SSD"),
    ("374460089", "Unknown", "Nvidia Quadro RTX 5000 16Gb GPU"),
    ("374702676", "Unknown", "PNY NVIDIA RTX  A2000 6GB"),
    ("374978883", "Unknown", "BELKIN Thunderbolt 3 Dock Plus"),
    ("375123025", "Unknown", "Acer Nitro N50-600 Gaming"),
    ("375129972", "Unknown", "Old School Gamer"),
    ("375144232", "Unknown", "selger datamaskin for deler"),
    ("375258842", "Unknown", "Gaming oppsett"),
    ("376052489", "Unknown", "CPU hovedkort osv selges"),
    ("376506528", "Unknown", "Quadro P2000 skjermkort"),
    ("376691620", "Unknown", "ITX-bundle(B660/12400F/16GB)"),
    ("376706452", "Unknown", "GeForce GTX TITAN X (12GB)"),
    ("377028227", "Unknown", "Razer Core X Chroma RC21-01430"),
    ("377151492", "Unknown", "Ducky Zero 6108"),
    ("377495278", "Unknown", "Radeon RX Vega 64 Air Boost 8G"),
    ("377525888", "Unknown", "NVIDIA Jetson TX2 Developer Kit"),
]

# Archived listing data for future testing
archived_listings = {
    '186553432': {
        'heading': '''BANANA PI med Touch Skjerm 7″ mm.''',
        'description': '''Official 7″ inch 800*480 LCD Display Touch Screen for Banana PiSelges kr 2490,- for komplett sett med alt inkl., alternativ til raspberry pi ,sending med posten kr 73 ekstraKjører Kali Linux.TFT LCD MODULE:S070WV20-CT16 TP MODULE:FT5306 Size:7.0 inches Resolution:800 (RGB) x 480 Interface:24-bit RGB Connect type:Connector Color Depth:262K Display element:a-si Display Spec. Pixel pitch:0.192 x 0.1805 (mm) Pixel Configuration:R.G.B. Vertical Stripe Display Mode:Normally White Driver IC:HX8254-D, HX8664-B Surface Treatment:HC Viewing Direction:6 O’clock LCM(WxHxD) :164.9 X 100.0 X 5(mm) Active Area(mm):154.08 X 85.92 With CTP LED Numbers:27 LEDSwiki.52pi.com/index.php/Banana_Pi_official_7-Inch-Capacitance-Screen_SKU:Z-0088 CN2: LCD connector CN5: TP connector CN1: Bpi connectorBPI-M3 Banana Pi M3 A83T Octa-Core (8-core) 2GB RAM with WiFi & Bluetooth4.0BPI-M3 Banana Pi M3 A83T Octa-Core (8-core) 2GB RAM with WiFi & Bluetooth4.0 with Case, WiFi antenna, adhesive heating processor, 5v power adapter + micro SD Class 10 ready with kali linux installed 8GB INCL. ORIGINAL 7″ Bpi Touch Screen.What’s the BPi-M3? Banana PI BPI-M3 is the open source hardware platform, Banana PI BPI-M3 is an octa-core version of Banana Pi, it support WIFI+BT on board. Banana Pi BPI-M3 series run Android, Ubuntu linux, Raspberry Pi image and others OS.and eMMC flash onboard. Banana PI PBI-M3 hardware: 1.8GHz ARM Cortex-A7 octa-core processor, 2GB LPDDR3 SDRAM, Banana PI BPI-M3with Gigabit Ethernet port, It can run with Android 5.1.1 smoothly. The size of Banana PI BPI-M3 same as banana pi M1+, it can easily run with the game it support 1080P high definition video output, the GPIO compatible with Raspberry Pi B+ and can run the ROM Image.Hardware Specification: SOC Allwinner A83T ARM Cortex-A7 CPU A83T ARM Cortex-A7 octa-core,512 KB L1 cache 1 MB L2 cache GPU PowerVR SGX544MP1Comply with OpenGL ES 2.0, OpenCL 1.x, DX 9_3 SDRAM 2GB LPDDR3 (shared with GPU) Power 5V 2A via DC power port and/or MicroUSB (OTG)Features: Low-level peripherals 40 Pins Header, 28xGPIO, some of which can be used for specific functions including UART, I2C, SPI, PWM, I2S. On board Network 10/100/1000Mbps ethernet (Realtek RTL8211E/D) Wifi Module WiFi 802.11 b/g/n (AP 6212 module on board) Bluetooth BT4.0 On board Storage MicroSD (TF) card,SATA2.0 ,eMMC8G Display — Supports multi-channel HD display: — HDMI 1.4 (Type A – full) — MIPI Display Serial Interface (DSI) for raw LCD panels — 11 HDMI resolutions from 640×480 to 1920×1200 Video Multi-format FHD video decoding, including Mpeg1/2, Mpeg4, H.263, H.264, etc H.264 high profile 1080p60fps or 720p120fps encoding HEVC/H.265 decoder 1080P30fps with software Audio outputs HDMI,analog audio (via 3.5 mm TRRS jack), I2S audio (also potentially for audio input) Camera Parallel 8-bit camera interface MIPI Camera serial Interface(CSI) Audio input On board micphone USB 2 USB 2.0 host, 1 USB 2.0 OTG Buttons Reset button, Power button, U-boot button LEDs Power status Led and RJ45 Led Other IR recieverSpecs CPUA83T ARM Cortex-A7 octa-core,512 KB L1 cache 1 MB L2 cache GPUPowerVR SGX544MP1· Comply with OpenGL ES 2.0, OpenCL 1.x, DX 9_3 Memory2GB LPDDR3 (shared with GPU) Storage SupportMicroSD Card(up to 64GB)/SATA(up to 2TB USB-to-SATA; GL830)/eMMC(8GB onboard) Onboard Network10/100/1000Mbps ethernet (Realtek RTL8211E/D) WiFi802.11 b/g/n (AP6212) BluetoothBT4.0 (AP6212) Video InParallel 8-bit camera interface MIPI Camera serial Interface(CSI) Video OutHDMI 1.4 DHCP 1.2 with resolutions from(640×640 to 1920×1080) MIPI DSI for RAW LCD panels Audio Out3.5 mm Jack and HDMI Audio InOn board microphone Power SourceMicro USB, optional 5V DC port (center positive 1,6 x 4,4mm) USB Ports2x USB 2.0, USB OTG(Micro USB) ButtonsReset button, Power button, U-boot button GPIO40 Pins: GPIO, UART, I2C bus, I2S bus, SPI bus, PWN, +3.3v, +5v, ground LEDPower LED(red), RJ45 LED(blue), user define LED(green) OSAndroid and Linux etc.OS Dimensions92mm x 60mm Weight45gPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=186553432'
    },
    '190878936': {
        'heading': '''MSI GeForce GTX 1080 Gaming X! Lite brukt, selges rimelig.''',
        'description': '''Selges lite brukt MSI GeForce GTX 1080 Gaming X skjermkort. Kun brukt til spillingAlt tilbehør medfølger som esken etc.Minne  8 GBMinnebåndbredde  256-bitMinnefrekvens  10 GHzMinnetype  GDDR5X SDRAMPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/190878936'
    },
    '197103206': {
        'heading': '''HP ProDesk 600 G1 SFF med Windows pro versjon''',
        'description': '''PC-en med SSD og installert med følgende programvare og klar til bruk.::Windows 10 Pro::Open officeSpesifikasjoner:Modell: ProDesk 600 G1 SFFProsessor: Intel Celeron G1820 2,7GHzMinne: 8GB DDR3 (1 brikke av 4 plasser)Skjermkort 1: AMD Radeon HD 8490Skjermkort 2: Intel HD Graphics 530Harddisk 1: Sandisk 128GB SSDHarddisk 2: Seagate 500GB HD(ekstra 250kr)Porter i front:USB 3: 2 stkUSB 2: 2 stkLyd: Hodetelefon/mikrofonPorter bak:USB 3: 2 stkUSB 2: 4stkNettverk gigabitDisplay Port: 3 stk DVI: 1 stkVGA, COM port, PS/2 mus og tastaturLyd inn/utSkjermen er ikke inkludert i prisen.Ta gjerne kontakt hvis du har spørsmål!Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/197103206'
    },
    '210334582': {
        'heading': '''Onda D1800 BTC 6 GPU HK. Med cpu og 8 gb ram''',
        'description': '''Selger mitt Onda D1800 BTC mining hovedkort da jeg har bygget ny mining rig.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/210334582'
    },
    '211030768': {
        'heading': '''Fujitsu Esprimo Windows11/Office2021 Nvidia 1050/Intel Q8300/8Gb RAM/360Gb SSD''',
        'description': '''Normalfungerende PC med Microsoft Windows 11 Pro og Microsoft Office 2021 installert i aktiverte, norske versjoner (evigvarende, ikke abonnement). Den har mikrofon- og hodetelefon-uttak i fronten og bak, totalt åtte USB-porter. HDMI og div. andre tilkoblinger på skjermkortet.Frakt: 150,-Tlf: 95221468Adresse: Fagerborggata 48BTar kontanter og Vipps.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=211030768'
    },
    '218966099': {
        'heading': '''Selger en top geforce GTX 780 Ti skjermkort med vannblokk''',
        'description': '''HeisannSelger top gaming kort Geforce GTX 780 ti med vannblokk installert (original kjøleblokk følger ikke med). Kortet er testet og klar for ny eier. Den drar fortsatt de fleste spill.Emneknagger: GTX, GTX 780 Ti, Ti, gaming, skjermkort, grafikkort, graphics card,Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/218966099'
    },
    '238005694': {
        'heading': '''strømforsyning''',
        'description': '''2400w strømforsyning til GPU mining. Kan selges som kit med kort og kabler.2500kr uten kort og kablerMed kort og kabler blir prisen 3800kr.Mer info her:https://www.parallelminer.com/product/all-in-one-gpu-mining-power-supply-zsx-kit-delta-2400-watt-platinum-94-power-supply-200-240v/Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=238005694'
    },
    '245307215': {
        'heading': '''HP 1200w server strømforsyning med breakout board og 12 kabler''',
        'description': '''HP 1200w platinum server PSU selges med breakoutboard og 12stk kabler.Veldig effektiv og stabil strømforsyning, perfekt for miningKan sendes for kjøpers risiko.Mining | Bitcoin | Miningrig | Asic | GPUPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=245307215'
    },
    '262624107': {
        'heading': '''Msi 2060 Gaming Z''',
        'description': '''Selger min Msi 2060 Gaming Z skjermkort.Jeg har byttet thermal paste en gang og det gikk uproblematisk og temperaturen ble lavere.Kjøpt sommeren 2019 og brukt til 2022.Kortet er kun brukt til gaming.Bare å komme med bud.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=262624107'
    },
    '268511754': {
        'heading': '''Nvidia PNY Quadro P5000 16GB''',
        'description': '''Kortet ble kjøpt nytt på Elkjøp i desember, 2017 (23.999,-), og har vært brukt i en klippestasjon fram til midten av 2020. Kortet sto i ro i stasjonen all sin arbeidstid, ble aldri overklokket (da selger knapt vet hvordan man gjør det) - og brynte seg stort sett på Adobe Premiere.Kortet ble byttet ut da jeg trengte litt mer kapasitet på renderingtid samt 4K klippe-preview.Denne trofaste arbeidshesten av et skjermkort selges for 7500,-, og vil pakkes svært godt før sending. Frakt på 129,- kommer i tillegg.---Søkekord: data, pcPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=268511754'
    },
    '273919170': {
        'heading': '''Asus ROG Strix RTX2080TI OC 11 Gaming''',
        'description': '''Selges grunnet oppgraderingHeftig skjermkort, kjøpt på Elkjøp lagunen for 3 år siden. 16 000Kunn brukt til gaming (Warzone)Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/273919170'
    },
    '279544829': {
        'heading': '''gpu GeForce RTX 3060 Ti GAMING Z TRIO 8G LHR NY''',
        'description': '''Helt ny,ikke åpnet eske enn gang.Følger med Kvitering.Fått fra komplett.noKan sendesPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=279544829'
    },
    '280866222': {
        'heading': '''I7-6700-3400ghz,  16gb ram, 480gb ssd,  gpu (gtx970 4gb)''',
        'description': '''.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/280866222'
    },
    '287137806': {
        'heading': '''GeForce RTX 3060 Ti GAMING X 8G LHR''',
        'description': '''Enhetstype GrafikkortBusstype PCI Express 4.0Grafikkprogram NVIDIA GeForce RTX 3060 TiBoost Clock 1770 MHzCUDA-kjerner 4864VR-klar JaMaks. oppløsning 7680 x 4320Maks. antall skjermer som støttes 4Grensesnitt 3 x DisplayPortHDMIStøttede API DirectX 12, OpenGL 4.6Egenskaper NVIDIA Adaptive Vertical Sync, Airflow Control-teknologi, klar for NVIDIA G-Sync, MSI Zero Frozr-teknologi, RGB Mystic Light, NVIDIA Ampere GPU-teknologi, Torx 4.0 Fans, Core Pipe, Twin Frozr 8 Thermal Design, LHR (Lite Hash Rate), 2nd gen Ray Tracing Cores, 3rd gen Tensor Cores, HDCPEAN 4719072850029MinneStørrelse 8 GBTeknologi GDDR6 SDRAMMinnehastighet 14 GbpsBussbredde 256-bitSystemkravPåkrevd strømforsyning 600 WEkstrakrav 6-pins + 8-pins PCI Express-strømkontakterDiverseStrømforbruk ved drift 220 wattInkludert programvare MSI CenterTilpassede standarder DisplayPort 1.4aBredde 5.1 cmDybde 27.8 cmHøyde 13.1 cmVekt 1.007 kgFraktvekt 1.596 kgPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=287137806'
    },
    '295746765': {
        'heading': '''XFX Radeon RX590 8GB''',
        'description': '''Veldig bra skjermkort, undervolter fantastisk, kan køre med 120W omkring 1450MHz.Kan sendes eller leveres omkring Kristiansand.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=295746765'
    },
    '306155637': {
        'heading': '''RTX 3060 zotac 12gb''',
        'description': '''ZOTAC GeForce RTX 3060 AMP White EditionSkjermkort, PCI-Express 4.0, 12GB GDDR6, AmpereKjøpt i 2021 juniNesten ubrukt, fremdeles med folie og original eske.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=306155637'
    },
    '309585615': {
        'heading': '''Gtx 1660 super''',
        'description': '''ASUS GeForce GTX 1660 SUPER DUAL EVO AdvancedKortet er i bra stand ikke brukt til MiningGrafikkortBusstype PCI Express 3.0 x16Grafikkprogram NVIDIA GeForce GTX 1660 SUPERKjerneklokke 1530 MHzBoost Clock 1830 MHzCUDA-kjerner 1408Maks. oppløsning 7680 x 4320Maks. antall skjermer som støttes 3Grensesnitt DisplayPortHDMIDVI-DStøttede API DirectX 12, OpenGL 4.6Egenskaper ASUS DirectCU II Technology, klar for NVIDIA G-Sync, AUTO-EXTREME-teknologi, NVIDIA Ansel, NVIDIA Turing GPU-arkitektur, 2,7-spors Fan Cooler, Axial-tech Fan Design, 0dB Technology, HDCPEAN 4718017504607Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=309585615'
    },
    '315146332': {
        'heading': '''HP Z400 med 2.93 Xeon Quad CPU/10GB RAM/Enkelt skjermkort.''',
        'description': '''Har installert Windows på èin SSD for å teste maskina.Følger med èin 120GB Kingston SSD.Flott pc som passer veldig fint til kontor eller annet.https://icecat.biz/amp/p/vendorName/mpn/desc-2059691.htmlBør hentes for test før kjøp :)Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/315146332'
    },
    '319642054': {
        'heading': '''Ny LOUQE RAW S1 mini ITX''',
        'description': '''LOUQE RAW S1 mini ITX kabinett vurderes solgt. Produktet er nytt og i uåpnet eske.Eksklusivt mini ITX kabinett i anodisert aluminium.Built for the battle, built for the road, built with you in mind: The Raw S1 gives unparalleled accessibility in a PC build with its 360 degree component access, tool-free GPU installation, and built-in handle. From start to finish you\'ll be up in no time.Raw elegance: Designed and manufactured in Sweden, each case is CNC machined from 3.5mm thick aluminum (6063 aluminum alloy) and etched twice to create a case both velvet smooth and precise.Raw gaming power: The Raw S1 is designed to accommodate the most powerful 3-slot GPUs. Each case comes with a COBALT TWINAX PCI-e RC260 GEN 4+ riser cable to handle your most intensive GPU needs.Airflow in focus: Cooling air is pulled in by each heat generating component and directed upwards through the top in a chimney effect.Spesifikasjoner:DIMENSIONS (H x W x D): 379 x 172 x 191 mmVOLUME & WEIGHT: 12 L & 3,2 kgCOLORS: Rhodium GreyMATERIAL: Bead blasted, etched, anodized 6063 alloyGPU SUPPORT: Triple-Slot up to 145 x 65 x 320 mmEXTERNAL I/O: USB 3.0 type C to C extension (on the back)FORM FACTOR: SFF, Mini ITX, Tower (Sandwich layout)POWER SUPPLY SUPPORT: SFX, SFX-LCPU HEATSINK SUPPORT: Up to 75 mmSTORAGE SUPPORT: 1 x 2.5″ HDD/SSD + NVMEEXHAUST FAN MOUNTINGS: 120mm (back), 140mm (top)PCI RISER: Included Twin Axial 260 mm PCIe 16x Gen-4 riserFastpris 3000,-. Frakt med Norgespakke koster 135,-. Betaling med Vipps på forskudd, eller fiks ferdig.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=319642054'
    },
    '320903793': {
        'heading': '''Selvbygd datamaskin''',
        'description': '''Hjemmebygd datamaskin selges.Maskina er ganske gammel men nesten ikke brukt. Sannsynligvis har jeg ikke skrudd av og på maskina mer enn 20-30 ganger.Selling pointet til maskina er det store romslige kabinettet fra Silverstone.Det heter Fortress og har veldig god plass, synes for eksempel å huske at det er plass til 8-9 harddisker. Denne maskina vil derfor være utmerket som en hjemmeserver.Som dere ser på bildene har datamaskinen alle portene på toppen, det som pleier å være på baksiden. Vet ikke fordelen med akkurat dette, men det gjør det lett å komme til alle portenene og det er bra kjølemuligheter. Maskina har tre store og en mindre vifter med regulererbar hastighet, se ett av bildene.Det maskina ikke har er et bra skjermkort da jeg bare har brukt det innebygde skjermkortet i hovedkortet. Det er også veldig lite RAM, kun 8GB. Ellers var prosessoren en av de bedre modellene på markedet da.Mer om kabinettet her: https://www.silverstonetek.com/en/product/info/accessories/FT02/Her er resten av specsene:Kabinett: Silverstone Fortress SST-FT02B for hovedkortformatene ATX, Micro ATX eller SSI CEBHovedkort: Asus P8Z68-V PRO Z68 S-1155 ATXStrømforsyning: ?Prosessor: Intel Core I7 2600K 3.40GHZ 8MB S-1155Prosessorkjøler: Cooler Master Silent Pro ATX12V 2.3 600WRAM: CORSAIR 8GB DDR3 XMS3 VENGEANCE PC3-12800 1600MHZ CL9 (2X4GB)SSD: Crucial m4 SSD 2,5\" 128GB SATA 6 Gb/s (SATA3.0), 415MB/175MB/s read/writeHarddisk: Samsung Spinpoint F3 1TB SATA/300 7200RPM 32MBDVD: Samsung DVD±R/RW/RAM DL 22XTest av prosessoren: https://hardwaresecrets.com/core-i7-2600k-cpu-review/\"The reviewed CPU doesn’t have a direct competitor, since the most expensive CPU from AMD – the Phenom II X6 1100T (3.3 GHz) – costs USD 60 less. In any case, the Core i7-2600K was faster than the Phenom II X6 1100T in all programs we ran (again, except on 3DMark 11).Like the Core i5-2500K, one of the highlights of the new Core i7-2600K is its outstanding overclocking capability. We were able to put it to run at 4.9 GHz, an impressive 44.1% increase in the CPU’s internal clock rate.(...)However, if you are a professional user working with video and photo editing, 3D rendering, and other applications that really need more processing power, you will surely benefit from the new Core i7-2600K and its very attractive price for this kind of use.\"Jeg har originalesken til kabinettet så kan sende maskina, men den er ellers ganske så tung (kabinettet veier over 15 kg i seg selv) så foretrekker at den hentes på Byåsen. Eller så kan jeg levere den i Trondheim eller omegn. Jeg har også originapakkene til mange av delene hvis det trengs.Dessverre kan ikke fiks ferdig brukes på denne hvis den skal sendes siden maskina med komponenter veier omkring 21 kg (maks vekt er 20kg).Kan være behjelpelig med å levere i Trondheim og omegn, Nordmøre og Nord-ØsterdalMaskina kan også leveres med en gammel kopi av Windows 7.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/320903793'
    },
    '323803923': {
        'heading': '''Komplett Gamer Premium i150 + BenQ 24\" selges brukt''',
        'description': '''Kjøpt juli \'17 av Komplett. Pris ny: 18 523,-Perfekt pc for noen som er ute etter sin første pc eller et billig alternativ. Fungerer som den skal og kjører det meste med greie innstillinger. Selges som den står og er formatert. Strømkabel følger med.Skjermen er en BenQ 24\" 3D LED XL2411Z. Tilkoblings- og strømkabel følger med.Spesifikasjoner:Phanteks Eclipse P400SSilent Window - Satin Black, Varenr: 876462 / Prodnr: PH-EC416PSW_BKEVGA GQ 650W Hybrid Modular 80+ PSUATX 12V , 80 Plus Gold, Modular, 4x 6+2pin PCIe, 9x SATA, 3x Molex, 2x FD, Varenr: 889957 / Prodnr: 210-GQ-0650-V2Intel Core i7-7700 Kaby Lake ProsessorSocket-LGA1151, Quad Core, 3.6GHz, 8MB cache, 65W, 14nm, OEM/tray, uten kjøler, Varenr: 904706 / Prodnr: CM8067702868314Cooler Master Hyper TX3i Komplett Ed.Prosessorkjøler for Intel LGA115x, 92mm vifte, 800-2200 RPM, 17-30 dBA, Varenr: 915890 / Prodnr: RR-TX3E-22PK-K1MSI Z270 Tomahawk, Socket-1151Hovedkort, ATX, Z270, DDR4, 3xPCIe-x16, CFX, 2xM.2, Red LED, Varenr: 909732 / Prodnr: Z270 TOMAHAWKHyperX Fury DDR4 2666MHz 16GB2x8GB CL16 Black, Varenr: 922311 / Prodnr: HX426C16FB2K2/16Nvidia GeForce GTX 1070Skjermkort, PCI-Express 3.0, 8GB GDDR5, Pascal, Varenr: 926423 / Prodnr: GTX1070Samsung PM961 SSD 256GB M.2 NVMeV3 TLC, Polaris, up to 2800/1100MB/s read/write, for production only, Varenr: 898545 / Prodnr: MZVLW256HEHP-00000Samsung 970 EVO Plus 500GB SSDPCIe Gen 3.0 x 4, NVMe 1.3, V-NAND TLC, Up to 3500/3200MB/s read/write, 300TBWVarenr: 1120735 / Prodnr: MZ-V7S500BWMS COA Win 10 Home NordicPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/323803923'
    },
    '329035256': {
        'heading': '''MSI Codex 3''',
        'description': '''MSI Codex 3 selges.Utrolig god pc, yter bra på de aller fleste spill.Selger ettersom jeg selv skal kjøpe ny pc.Specs:GPU: Nvidia Geforce GTX 1050 TiCPU: Intel i5-8400RAM: 8GB DDR4Lagring: 1TB harddiskSSD: 128GBKom gjerne med spørsmål,Pris kan diskuteres.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=329035256'
    },
    '329969572': {
        'heading': '''NVIDIA GeForce RTX 2070 MSI Armor 8GB''',
        'description': '''Et fantastisk kraftig skjermkort for prisen!Har dessverre ikke boksen, siden jeg har flyttet og boksen ligger derfor igjen. Boks kan sendes separat om ønskelig!Helst hentes i person, kan møtes hvor som helst i oslo.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=329969572'
    },
    '330797746': {
        'heading': '''Intel i7  2600 / Gtx 960  / 8 Gb ddr3/ corsair 500W / Med eller uten SSD !''',
        'description': '''Byttet kjølepasta på CPU og GPU nydelig.CPU vifte ikke helt orginall men tilpasset til den!Virker og kjøler som den skal!- Intel i7 2600- Hp ipmmb-fm motherboard- Nvidia GTX 960-  8 Gb ram- Corsair 500 W Rgb- Windows 10- Kingstone 120 GB sata SSDKan kjøpe skjerm til den fra meg tillegg i prisen. Se på mine annonsser!Ta kontakt hvis du lurer på mer.Kan sendes.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=330797746'
    },
    '333629803': {
        'heading': '''Ati rage fury maxx agp skjermkort''',
        'description': '''Vurderer salg av et skjeldent skjermkort fra 99.Har original driver cd.Har byttet lager på begge viftene.Perfekt til retro pc bygg med windows 98.Søkeord: RetrogamingPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=333629803'
    },
    '333825410': {
        'heading': '''MASSE datautstyr og deler - RAM, CPUer, GPUer, gamingtastatur, headset, mus++++''',
        'description': '''Selger unna en god del deler som ikke blir brukt.Hva følger med?- 50GB++ med DDR3 minne- 20GB++ med minne til laptop, noe DDR4- Div skjermkort- Flere prosessorer fra eldre generasjoner, både AMD og Intel- Gaming tastaturer fra logitech og Steelseries- Flere eldre headset og noen gode gaming-muser- Maaasse kabler - DVI, HDMI, PSU, SATA+++- Webcamera fra Logitech- ++++PS:- Kan ikke garantere at alt fungerer 100%- Jeg vet med sikkerhet at noen veldig få av RAM-brikkene er defektPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=333825410'
    },
    '336138344': {
        'heading': '''ATI Rage LT Pro 8MB SDRAM AGP Video Graphics Card- 109-55700-00''',
        'description': '''Selger ett gammelt skjermkort fra ATI , fra 1998Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/336138344'
    },
    '336571027': {
        'heading': '''MSI RTX 3070 Supreme X gpu''',
        'description': '''Selger et MSI 3070 kort. Kvittering fåes på e-post etter kjøp, fra netonnet.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=336571027'
    },
    '340984589': {
        'heading': '''Hp Omen 880-109no''',
        'description': '''Skjekker intressen for min Omen maskin.God pc som har fungert utmerket i mitt eie.I7-8700kZ370 hovedkort32GB ddr4(husker ikke mhz, over 3000)500W internal psu1080Ti skjermkortSsd 256GB2TB hddBrukt til mye PUBG og Tarkov i mitt eie og fungert fint.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/340984589'
    },
    '341981334': {
        'heading': '''Brukt Gaming maskin i3-7100 3.9Ghz, 8 GB RAM, 2x 256 GB SSD uten lisens''',
        'description': '''Brukt Gaming maskin selges. Kan fremdeles kjøre de nyeste spillene, men prosessoren begynner å bli for dårlig. Sjekk hva dine spill krever. Maskinen er ny installert med Windows 11 home men mangler aktivisering. Du må selv skaffe deg en gyldig lisens. Maskinen er fra 2018 og begynner å bli gammel. Skjermkortet er et NVIDIA Geforce GTX 1060 med 6 GB RAM. 500W strømforsyning. 2 x 256 GB SSD disk. Unigine Heaven Benchmark 4.0 gir en FPS score på 132.7, score 3342. 1920x1080. Ekstern usb WIFI kort følger med. Er renset for støv og skitt, og ny kjølepasta er påsmurt. Grei maskin for en med lite penger.Kan hentes etter avtale, eller sendes i posten ved bruk av Finns Fiks ferdig.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=341981334'
    },
    '344551685': {
        'heading': '''AMD radeon RX 6500 XT''',
        'description': '''Selger mitt gamle grafikkort da jeg har oppgradert. Skjermkortet er en ASRock RADEON RX 6500 XT 4gb ram GDDR6 1080p.Har 1 DP og 1 HDMI port (se bilde)Det er i god tilstand og har blitt pent brukt.Send melding hvis det er noe du lurer på😊Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/344551685'
    },
    '346235525': {
        'heading': '''Gigabyte GA-990FXA-UD5, S-AM3+, AMD Phenom II X6 1090T Black Ed CPU og 12 GB RAM''',
        'description': '''Gigabyte GA-990FXA-UD5, S-AM3+ hovedkort med påmontert CPU, CPU kjøler og RAM.Cooler Master Hyper 212 Plus CPU Kjøler3 stk Corsair Vengeance DDR3 1600MHz 4GBAM3+ Socket:Support for AMD AM3+ FX processorsSupport for AMD AM3 Phenom™ II processors / AMD Athlon™ II processorsHyper Transport Bus5200 MT/sChipsetNorth Bridge: AMD 990FXSouth Bridge: AMD SB950Memory4 x 1.5V DDR3 DIMM sockets supporting up to 32 GB of system memory (Note 1)Dual channel memory architectureSupport for DDR3 2000(O.C.)/1866/1600/1333/1066 MHz memory modules (Note 2)AudioRealtek ALC889 codecHigh Definition Audio2/4/5.1/7.1-channelSupport for Dolby Home TheaterSupport for S/PDIF OutLAN1 x Realtek RTL8111E chip (10/100/1000 Mbit)Expansion Slots2 x PCI Express x16 slots, running at x16 (PCIEX16_1, PCIEX16_2) (Note 3)1 x PCI Express x16 slots, running at x8 (PCIEX8) (Note 4)2 x PCI Express x16 slots, running at x4 (PCIEX4_1, PCIEX4_2)1 x PCI Express x1 slot(All PCI Express slots conform to the PCI Express 2.0 standard.)1 x PCI slotMulti-Graphics TechnologySupport for NVIDIA® Quad-GPU SLI™ and 3-Way/2-Way NVIDIA® SLI™ TechnologiesSupport for AMD Quad-GPU CrossFireX™ and 3-Way/2-Way AMD CrossFire™Storage InterfaceSouth Bridge:6 x SATA 6Gb/s connectors (SATA3_0~SATA3_5) supporting up to 6 SATA 6Gb/s devicesSupport for SATA RAID 0, RAID 1, RAID5, RAID 10 and JBOD2 x Marvell 88SE9172 chips:2 x SATA 6Gb/s connectors (GSATA3_6, GSATA3_7) supporting up to 2 SATA 6Gb/s devices2 x eSATA 6Gb/s connectors on the back panel supporting up to 2 SATA 6Gb/s devicesSupport for RAID 0 and RAID 1USBSouth Bridge:Up to 14 USB 2.0/1.1 ports (8 ports on the back panel, 6 ports available through the internal USB headers)2 x Etron EJ168 chips:Up to 4 USB 3.0/2.0 ports (2 ports on the back panel, 2 ports available through the internal USB header)IEEE 1394VIA VT6308 chip:Up to 2 IEEE 1394a ports (1 port on the back panel, 1 port available through the internal IEEE 1394a header)Internal I/O Connectors1 x 24-pin ATX main power connector1 x 8-pin ATX 12V power connector8 x SATA 6Gb/s connectors1 x CPU fan header2 x system fan headers1 x power fan header1 x front panel header1 x front panel audio header1 x S/PDIF Out header3 x USB 2.0/1.1 headers1 x USB 3.0/2.0 header1 x IEEE 1394a header1 x serial port header1 x clearing CMOS jumper1 x Trusted Platform Module (TPM) headerBack Panel Connectors1 x PS/2 keyboard/mouse port1 x optical S/PDIF Out connector1 x IEEE 1394 port8 x USB 2.0/1.1 ports2 x USB 3.0/2.0 ports2 x eSATA 6Gb/s connector1 x RJ-45 port6 x audio jacks (Center/Subwoofer Speaker Out/Rear Speaker Out/Side Speaker Out/Line In/Line Out/Microphone)I/O ControllerITE IT8720 chipH/W MonitoringSystem voltage detectionCPU/System temperature detectionCPU/System/Power fan speed detectionCPU overheating warningCPU/System/Power fan fail warningCPU/System fan speed control (Note 5)BIOS2 x 32 Mbit flashUse of licensed AWARD BIOSSupport for DualBIOS™PnP 1.0a, DMI 2.0, SM BIOS 2.4, ACPI 1.0bSupport for @BIOSSupport for Q-FlashSupport for Xpress BIOS RescueSupport for Download CenterSupport for Xpress InstallSupport for Xpress Recovery2Support for EasyTune (Note 6)Support for Easy Energy SaverSupport for Smart RecoverySupport for Auto GreenSupport for ON/OFF ChargeSupport for Cloud OCSupport for 3TB+ UnlockSupport for Q-ShareForm FactorATX Form Factor; 30.5cm x 24.4cmPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/346235525'
    },
    '348965763': {
        'heading': '''RTX 4060 GAMING OC 8GB (KUN GPU)''',
        'description': '''Denne GPU\'en har vært brukt lite, ettersom PCen ikke var bygd for veldig lenge siden. Selges fordi jeg vil ha et sterkere kort til video redigering. Denne var kjøpt helt ny fra Proshop, og har kvittering. Selges, eller kan byttes mot et bedre kort med mellomlegg.Bud aksepteres.Proshop: https://www.proshop.no/Grafikkort/GIGABYTE-GeForce-RTX-4060-GAMING-OC-8GB-GDDR6-RAM-Grafikkort/3170383Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=348965763'
    },
    '350643862': {
        'heading': '''Gaming rig med Ryzen 7 1800x, Vega 64 og 144Hz skjerm, mus, EK vannblokk, m.m!''',
        'description': '''Super-PC til Salgs!Denne råe PC-en knuser alt du kaster på den, enten du spiller de nyeste spillene, redigerer videoer eller lager 3D-greier. Med en superrask prosessor, et heftig grafikkort, masse RAM og lagringsplass, er alt du trenger for en superrask og smidig opplevelse på plass.Det kommer også med en 27\" 1440p 144Hz rask gaming skjerm og mus.Perfekt for:Spillere som vil ha det beste for å knuse alle spilleneDe som lager videoer og 3D-greier og trenger en kraftig maskinProfesjonelle som trenger en pålitelig og rask PC for krevende tingPC-en er i topp stand og selges for 8000 kr.Specs:AMD Ryzen 7 1800xAMD Vega 64 (Radeon logoen lyser ikke. Var uheldig med noen kabler når jeg installerte vannblokken, men kortet fungerer ellers helt fint)16GB Dominator Platinum DDR4 (følger med CableMod memory modding kit, i hvit)ASUS Crosshair VI HeroSamsung 860 EVO 500GB NVME SSDCorsair H150i RGB Pro XTCorsair RM 850 i hvitPhanteks P400A kabinett (er litt modifisert for å få plass til viftene i fronten til å passe)AOC AGON 27\" 1440p 144Hz TN, (AG271QX)(Skjermen har en liten sprekk på høyre side av skjermen, men lite synlig ved bruk)HyperX Pulsefire FPS mus3stk 2TB Seagate HDDAsus AC Wifi kortEK Vannblokker til CPU og GPU følger også med!Kontakt meg for mer info eller for å se den.Kjøp denne PC-en nå og få en superrask og pålitelig maskin!NB! SENDER IKKE!Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=350643862'
    },
    '352922618': {
        'heading': '''Håndholdt Android terminal med integrert kvitteringsskriver''',
        'description': '''CPU: Qualcomm Quad-Core Cortex™-A53 1.3GHz, 64BitGPU: Qualcomm Adreno™ 304RAM: 2GB SDRAMROM: 16GB NAND FLASHOS: Android 10.0Skjerm: 6 tommer fargeskjermBerøringsskjerm: Multipunkts kapasitiv berøringsskjermWIFI: 802.11b/g/nBluetooth: BT 4.1GPS: GNSS gpsOne Gen 8B; selvstendig; assistert, XTRATrådløs: 2G: GSM/GPRS/EDGE, 3G: WCDMA, TD-SCDMA, CDMA2000, 4G: LTE: FDD/TDDBatteri: 7.4V/2600mAhEkstern minnekort: TF-kortHastighet: 10cm/sek ~ 150cm/sekHodets levetid: 800 tusen gangerLeseavstand: 5cmStøttet korttype: Mifare S50, Mifare S70, Mifare Ultralight CPU-kort (Bank)Dimensjoner: 225mm * 87mm * 58mmSim-kortgrensesnitt: Dobbel SIM-kortStrømadapterutgang: DC 9V/3.5AUtskriftsmetode: Termo-punktmetodePapir: Termorullpapir (standard) 57 * 45 mmEffektiv utskriftsområde: 48mmUtskriftshodets levetid: Pulsresistens: 100 millioner pulser/punkt (under våre standardforhold); Slitasjemotstand: papirreiseavstand 50km (utskriftsforhold: 25% eller mindre)Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=352922618'
    },
    '353362563': {
        'heading': '''MSI gtx 1070 8gb''',
        'description': '''Brukte skjermerkort lite siden gikk over til rtx 3070 ti.Pris kan diskutereChipset: NVIDIA GeForce GTX 1070Video Memory: 8GB GDDR5 and card dimension(mm)-6-pin x 1, 8-pin x 1Memory Clock: 8108 MHz (oc mode) ; Memory 8GB GDDR5 (256-bit) , Interface: PCI Express x16 3.0. DirectX Version Support - 12, OpenGL Version Support- 4.5, Multi-GPU Technology - SLI, 2-WayMax. Resolution: 7680 x 4320, support 4x Display monitorsPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=353362563'
    },
    '354559137': {
        'heading': '''MSI GTX 1080 SEAHAWK væskeavkjølt skjermkort''',
        'description': '''MSI GTX 1080 SEAHAWK -  Seahawk utgaven er væskeavkjølt med egen tilhørende vifte. Har satt på 2 ekstra vifter for enda bedre effekt.Har stått ubrukt en stund men fungerer som bare det. Litt dårlig bilde da den fremdeles er montert i den stasjonære pcn.Features:- PCI Express x16 3.0 bus- 8 GB GDDR5 memory- 10108 MHz memory clock frequency- 1708/1847 MHz GPU core clock frequency (GPU Boost 3.0 off/on)- 1x HDMI, 1x DVI and 3x DisplayPort connectors- DirectX 12 support- Support for 8K displays (7680 x 4320)- Nvidia SLI compatible (multi-GPU setup)- Support for up to 4 screens simultaneously- Kombustor, a built-in DirectX 12 benchmark- Nvidia SLI support- Nvidia VR ReadyPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/354559137'
    },
    '356371536': {
        'heading': '''ASUS Radeon RX 5700 XT ROG Strix OC''',
        'description': '''ASUS Radeon RX 5700 XT ROG Strix OC 8 GB GDDR6 PCI-E 4.0,Eit fint brukt skjermkort til salgs.Er kjørt test på før det blei tatt ut av pc sjå bilder.Har ikkje orginal eske eller innpakning.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=356371536'
    },
    '356800877': {
        'heading': '''HP Pavilion Gaming Desktop''',
        'description': '''Processor: AMD Ryzen 5 3600 6-core ProcessorRAM: 8GBGPU: AMD Radeon RX 5500SSD: 500GBpent brukt, virker som en helt ny pc. har ikke hatt noen problemer med den.PRIS KAN DISKUTERES.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/356800877'
    },
    '358990501': {
        'heading': '''3450w! PSU''',
        'description': '''Stor kraftig PSU3450wNesten ikke bruktKan sendesÅpen for budStikkord:Mining btc eth rvn asic gpu riserPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/358990501'
    },
    '359441264': {
        'heading': '''Raedon 6900XT''',
        'description': '''Lite brukt raedon 6900xt skjermkortPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=359441264'
    },
    '359598161': {
        'heading': '''Retro Gaming: Asus 7900 GTX King Kong Limited Edition''',
        'description': '''Selger en klenod av et retro skjermkort - Asus 7900 GTX King Kong Limited EditionDette kort var en toppmodell i Nvidia 7900 GTX serien med meget god kjøling og prestanda.Selges til pris i annons eller HBO vid stort intresse.Kortet er testet fysisk 2024-07-01 og virker som det skal og er i meget god stand.Offisielle drivers finnes til Windows XP / Windows 2000Moddade drivers finnes til Win98/DOS for dette kort (Google is your friend)Specs: https://www.techpowerup.com/gpu-specs/geforce-7900-gtx.c154Produsent: https://www.asus.com/supportonly/en7900_series/helpdesk_knowledge/All research om kort, kompabilitet, drivers etc. er 100% kjøpers ansvar!Hentes eller kan sendesPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=359598161'
    },
    '359957859': {
        'heading': '''Asus RTX2060S 8GB Turbo EVO''',
        'description': '''Selger en lite brukt GPU.Har oppgradert til 3070 pga video redigering.Kan sende.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=359957859'
    },
    '360210206': {
        'heading': '''ZotacGaming Geforce RTX 3060 Twin Edge 12gb''',
        'description': '''ZotacGaminh Geforce RTX 3060 Twin Edge 12gb skjermkort selges.Svært lite brukt.Følger med orginal eskePluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=360210206'
    },
    '360962892': {
        'heading': '''AMD RADEON RX 6900 XT''',
        'description': '''Lite brukt gpu, selges pga trenger den ikkje lengre.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=360962892'
    },
    '361056849': {
        'heading': '''HP EliteOne 800 (All-in-One) med Windows 11 Pro, 16GB RAM, 2 stk. 256GB SSD''',
        'description': '''HP EliteOne 800 G2 (All-in-One) med 23\" display kombinerer alle komponenter i en lukket enhet i stedet for å ha et separat PC-tårn og en skjerm:- Operativsystem: Windows 11 Pro (24H2 versjon)- CPU: Intel Core i5-6500 (3.2 GHz), 4 Cores- Skjermstørrelse: 23\" display (16:9), (Full HD)- GPU: Intel HD Graphics 530 (1920 x 1080px / 60Hz)- Lagring: 2 stk. av 256 GB SSD- RAM: 16 GB- Optisk drive: DVDRW HP PLDS DU8AESH- Antall USB 3.2 Gen 1 (3.1 Gen 1)Type-A-porter: 6 stk.- Antall USB 3.2 Gen 1 (3.1 Gen 1) Type-C-porter: 1 stk.- Ethernet LAN inngang: 10/100/1000 Mbit/s- Videoutgang: Display Port- Hodetelefoner utgang- Mikrofon inngang- Lyd utgang- Integrert WEB kamera med mikrofon- Trusted Platform Module (TPM) 2.0- Bredde (med stativ): 567,1 mm- Dybde (med stativ): 589 mm- Høyde (med stativ): 392,7 mm- Vekt (med stativ): ca. 7,5 kg(Ekstra USB stick for Wi-Fi nettverk er installert og følger med!)Leveres med HP original tastatur og mus. Klar til bruk. Må hentes.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=361056849'
    },
    '361592154': {
        'heading': '''Kraftig Lenovo ThinkCentre M720S pakke med Windows 11 Pro (24H2 versjon)''',
        'description': '''Her får du en svært kraftig og komplett løsning fra merkevareprodusent Lenovo:- Lenovo ThinkCentre M720S PC (SFF kabinett)  med Windows 11 Pro (24H2 versjon)- CPU: Intel Core i5-8400 (2.8 GHz), (6-cores)- Optisk stasjon DA8AESH CD / DVD +/- R / RW- Kortleser: 6-in-1 (i front)- Lagring: 1 TB SSD drive- RAM = 16 GB (DDR4)- GPU: Intel UHD Graphics 630 (1 GB RAM med 2 stk. DisplayPort utganger)- 4x USB 2.0 porter (på baksiden)- 4x USB 3.1 porter (i front)- 1x USB-C™ port (i front) - (USB 3.1 Gen 1 / 5.0Gbps or charge your device: 5V/3A)- 1x VGA videoutgang- 2x DisplayPort videoutganger- 1x Serial port inngang- 1x Ethernet, Fast Ethernet, Gigabit Ethernet port- Realtec High Definition Audio- 1x Line-out Audio utgang (på baksiden)- 1x Headset tilkobling (i front)- 1x Mikrofon inngang (i front)- W x H x D (mm): 92.5 x 343.5 x 290.5 (SFF form factor)- Vekt: ca. 6 kg- Skjerm: Lenovo ThinkVision LT2452p 24\", 1920 x 1200 px- Responstid: 5 ms- Sideforhold: 16:10- Skjermteknologi: LCD- Paneltype: IPS- Fargerdybde (antall): 16.77 mill.- Lysstyrke: 300 cd/m2Lenovo PC pakken leveres med:- Tastatur og mus fra Lenovo- Realtek RTL8188ETV Trådløs LAN 802.11n USB nettverk adapter.- Strømkabel, DisplayPort kabel, USB kabel (fra PC til USB-hub på skjermen).Klikk her for \"M720s User Guide and Hardware Maintenance Manual\":https://download.lenovo.com/pccbbs/thinkcentre_pdf/m720s_ughmm_en.pdfPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=361592154'
    },
    '361920143': {
        'heading': '''Asus RTX 2060S - GPU''',
        'description': '''Selger DUAL-RTX2060S-8G-EVOVet ikke så veldig mye om den da jeg kjøpte den i en pc jeg ikke trengte denne i, PCen fungerte når denne sto i. Men har ikke selv testet den noe særlig siden jeg hadde ett bedre kort liggendeSelges da jeg bruker ett annet kort å ikke har behov for denne.Denne må hentes i vennesla området da jeg ikke har mulighet til å sende.Selges uten noe form for garanti!Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=361920143'
    },
    '361980305': {
        'heading': '''Asus Eee Top ET2002T - All-in-one desktop''',
        'description': '''Asus Eee Top ET2002T i god stand.Asus Eee Top ET2002T alt-i-ett PC har en 20-tommers berøringsskjerm LCD-skjerm med en oppløsning på 1600 x 900- Dual Core Intel Atom 330 1,6 GHz-prosessor- 2 GB RAM- 250 GB harddisk- NVIDIA Ion GPU- innebygd WiFi b/g/n- Gigabit Ethernet- 6 USB 2.0-porter- kortleser- HDMI-inngang- DVD-brennerTrådløst tastatur og lader følger medPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=361980305'
    },
    '362401743': {
        'heading': '''AMD RX skjermkort; 5600 XT og 6800 XT''',
        'description': '''Selger fine AMD RX skjermkort, RDNA.Alle skjermkort er high-end modeller innenfor sitt segment.Alle er testet og fungerer fint uten støy.Kortene er blåst for støv og viftene er i god stand.Kvittering medfølger.Pris oppgitt er per stykk.RX 5600 XT ASUS DUAL-RX5600XT-A6G-EVO - 1200 NOKRX 6800 XT XFX Speedster MERC 319 AMD Radeon™ RX 6800 XT - 6000 NOKKan hentes eller sendes.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=362401743'
    },
    '362913580': {
        'heading': '''Gigabyte RTX 4060''',
        'description': '''GIGABYTE - NVIDIA GeForce RTX 4060WINDFORCE OC 8GB GDDR6 PCI Express 4.0Graphics Card - BlackAvailable end of august, start of September(because thats when ill get my new gpu delivered).Receipt included.Box (will try to find it in the bod).Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=362913580'
    },
    '363747046': {
        'heading': '''Aorus B550I PRO - Ryzen 9 3900X - 16GB 3000MHz''',
        'description': '''KJØLER ER SOLGT.Selger en pc-pakke her.Perfekt om du ønsker å bygge en ITX-pc4800,- ferdig pris.søkeord:gamingpcdelerhovedkortpc-pakkepc-deler pakkecpugpuitxmini pcPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=363747046'
    },
    '364161121': {
        'heading': '''🔴 MSI RADEON RX VEGA 56 AirBoost OC Edition + Original Box''',
        'description': '''🔴 MSI RADEON RX VEGA 56 AirBoost OC Edition + Original BoxAlt fungerer som skal. 👍Brukt: 1,5 år - I perfekt stand.Holdt rent og i lave temperaturer.Salgsårsak: Jeg selger mine gamle og ikke brukte GPU-er.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/364161121'
    },
    '364638491': {
        'heading': '''RTX 2080 Ti på Vannkjøler (AIO)''',
        'description': '''2080ti som er montert på en Kraken G12 for AIOhttps://nzxt.com/product/kraken-g12Følger med GPU, gamle kjøler og AIO.Gode temps, rundt 60grader under full load. Heftig gaming opplevelse. Nådde rundt 300-400fps i CS2Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/364638491'
    },
    '365180872': {
        'heading': '''RX 6700 XT Skjermkort''',
        'description': '''Amd Radeon  RX 6700 12GB memorymsiPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/365180872'
    },
    '365695264': {
        'heading': '''PowerColor Radeon RX 6600 Fighter''',
        'description': '''BeskrivelseBesøk nettbutikken for mer informasjon!Skjermkort med sammenlignbar ytelse som GTX 1080Ti, RTX 2070 og RTX 3060.Bedre ytelse enn:GTX 1080GTX 1070GTX 1060RX 5700RX 5600 XTRX 5600RTX 2060 SuperRTX 2060GTX 1660 SuperGTX 1660 TiPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/webstore/ad.html?finnkode=365695264'
    },
    '366113912': {
        'heading': '''Lenovo NVIDIA RTX A2000  6 G Grafikkort Skjermkort GPU''',
        'description': '''Selger Lenovo A2000 skjermkort - skjermkortet fungerer som det skalIkke brukt skjermkortet på to årProdusent: LenovoModell : RTX A2000Grafikkprosessor: NVIDIA RTX A2000Memory Size: 6 GPCI Express 4.0 x16Maks ekstern oppløsning7680 x 4320Maks. antall skjermer som støttes4GDDR6 SDRAM✅ Kan sendes✅ Kan hentes i Lørenskog & Oslo ( St. Olavs plass)Søkeord: Skjermkort, GPU, Lenovo, Grafikkort, A2000, A 2000Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/366113912'
    },
    '367447424': {
        'heading': '''6U NAS Kabinett med SAS backplane - Passer i 60cm rack!''',
        'description': '''Vurderer å selge mitt NAS-kabinett. Dette er custom made for å passe i vanlige 60cm brede og 60cm dybde rack (ikke de på 40cm), slik du ikke trenger \"full dybde\" server racks.Denne har 12 slots for disker, men 1 caddy trenger å skiftes (koster et par hundre, men bare låsen er løs så fungerer). Følger med SAS backplane som trenger bare en SAS kabel for å drive alle 12 diskene.Passer vanlig ATX hovedkort, og god plass til PSU og skjermkort (bruker pr dags dato et 1080TI så svært god access inni. Det er 4 hyller inni som kan brukes til f.eks 4 interne SSD-disker.Dette er et must for de som vil ha et rått kabinett for NAS som ikke finnes mange av her i Norge.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/367447424'
    },
    '368157918': {
        'heading': '''HP ProDesk 600 med Windows 11 Pro, 16GB RAM, 256GB SSD og 1TB HDD''',
        'description': '''Her får du en svært god og kraftig datamaskin fra merkevareprodusent:- HP ProDesk 600 G1 (SFF type) med Windows 11 Pro (24H2 versjon)- CPU: Intel Core i5-4590 (3.3 GHz)- Optisk stasjon 9.5mm Slim Desktop HPPLDS DVDRW DS8ACSH- Lagring: 256 GB SSD drive, 1TB SATA HDD- RAM: 16 GB (DDR3)- GPU: Intel HD Graphics 4600 (1 GB)- Trusted Platform Module (TPM) 2.0- USB 2.0: (2) front; (4) baksiden- USB 3.0: (2) front; (2) baksiden- 1x VGA videoutgang- 2x DisplayPort videoutganger med multi-stream- 1x Serial port- 1x PS / 2 tastatur port- 1x PS / 2 museport- 1x Ethernet, Fast Ethernet, Gigabit Ethernet port- 2x Line-out (headphone/speaker)- 2x Line-in (stereo/microphone)- Innebygget strømforsyning: 240 W active PFC- H x W x D (mm): 338 x 100 x 379- Vekt: ca. 8.1 kgFor mer info: https://support.hp.com/ie-en/document/c03846648Leveres med strømkabel og DisplayPort kabel. Klar til bruk.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/368157918'
    },
    '368437409': {
        'heading': '''Nytt 4090 TUF OC, 6900xt,3060ti/70ti,  3070,PNY3070, turbo 3070, Zotac 3070ti''',
        'description': '''Selger diverse skjermkort!Suprime 4080 super nytt/uåpnet med kvittering reservertAMD as rock 6900xt 16gb vram!5.500krMSI Rtx 3060ti,3.500krGigabyte Eqgle 3070, reservert3.500krRtx PNY 3070,3.500krRtx HP 3070,  reservert3.250krRtx Zotac 3070ti5.000krRTX 3070 turbo 3.500kr4090 Tuf OC nytt uåpnet 20.000 med kvitteringdiv 3070 3.500kr3060ti ghost 3.500kr2070 super 2500kr5600xt 1500krTa gjerne kontakt! NB skambud blir ikke besvart!Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=368437409'
    },
    '368480336': {
        'heading': '''Hp pavilion gaming PRIS KAN DISKUTERES''',
        'description': '''Hei selger men hp gaming pc som ikke er veldig mye brukt:) Si ifra hvis dere vil ha noen flere bilder!!Core i5NVIDIA GeForce GTX 1650 Super GPU8 GB DDR4 RAM, 512 GB SSDWindows 11Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=368480336'
    },
    '368491248': {
        'heading': '''Acer Predator Orion 3000 P03-600''',
        'description': '''Predator P03-600 (Prebuilt, kan byttes ram og ssd)Spesifikasjoner:GPU: RTX 2070CPU: i7 9700RAM: 16GBSSD: 512GBPC’en er i god stand. Spesifikasjonene til denne pc’en kan gi veldig høy fps i 1080p HD, men kan også kjøre 1440p QHD som jeg personlig har brukt det til, mindre fps men bedre bilde kvalitetPc’en er gammel 5 år. Den har nettop blitt byttet med ny thermal paste (GPU og CPU), blåst med luftsspray for å få vekk alt dusten, og tørket av får å se ren ut.Her er en liste over hva slags fps i 1080p og 1440p denne pcen gir meg.(Det er ingen forskjell med andre tester så det kan også kjekkes på youtube eller slikt)All fps\'en er gjennomsnittligFortnite (Low settings)1080p: 1951440p: 160Rocket League (Low settings)1080p: 3201440p: 280Grand Theft Auto (Max Settings)1080p: 901440p: 65Battlefront 2042 (Medium DLSS Quality)1080p: 1001440p: 80War Thunder (Max settings DLSS Quality)1080p:1451440p: 120No Man’s Sky ( High Settings)1080p: 1201440p: 100Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=368491248'
    },
    '368491322': {
        'heading': '''EVGA GEFORCE GTX 1080Ti FTW3 edition''',
        'description': '''ÅPEN FOR BUDBrukt skjermkort selges pga oppdatering. Selges uten noe garanti, men funket helt fint til mine spill før jeg byttet, byttet pga kjøpt ny pc.Sterkt kort for mining.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=368491322'
    },
    '368798902': {
        'heading': '''Komplett Gamer - 144Hz Edition''',
        'description': '''Selger min pent brukt pc fra Komplett. Skjerm følger ikke med.HyperX Alloy Elite RGB Gaming Tastaturkablet, nordisk, cherry mx red, rgb belysning, mekanisk gaming tastatur Varenr: 979594 / Prodnr: HX-KB2RD2-NO/R1Svive Luna S100 W Midi TowerVifter: 1x 120mm bak, ATX, mATX, mITX, Window Varenr: 1090679 / Prodnr: SVGCCS100V2Cooler Master B500 V2 KOMPLETT EditionATX 12V V2.3, 80Plus, 1x 4+4 CPU, 2x 6+2pin PCIe, 6x SATA, 3x Molex Varenr: 838663 / Prodnr: RS500-ACABB1-BKIntel Core i5-8400 ProsessorSocket-LGA1151, 6-Core, 6-Thread, 2.8/4.GHz, 65W, OEM/tray, uten kjøler Varenr: 975984 / Prodnr: CM8068403358811akasa AK-959CU Komplett EditionCPU Cooler, LGA 1150/1155/1156, 115W, PWM Varenr: 878490 / Prodnr: AK-959CU-M01Cooler Master Hyper TX3i CPU Kjøler775/1150/1151/1155/1156, 800-2200 RPM, 17-30 dBA Varenr: 891804 / Prodnr: RR-TX3E-22PK-B1MSI B360M Bazooka, Socket-1151Hovedkort, mATX, B360, DDR4, 3xPCIe-x16, M.2, USB 3.1, Mystic Light Sync Varenr: 999026 / Prodnr: B360M BAZOOKACrucial DDR4 2400MHz 16GB2x8GB 2400MHz (PC4-19200) DDR4 CL17 SR x8, 288pin, Single Ranked Varenr: 891087 / Prodnr: CT2K8G4DFS824AGainward GeForce RTX 2060 PhoenixSkjermkort, PCI-Express 3.0, 6GB, GDDR6, 1365/1680MHz, Turing Varenr: 1120472 / Prodnr: 426018336-4320Kingston A1000 480GB M.2 SSDM.2 2280, PCIe 3.0 x2, NVMe, 3D TLC, up to 1500/900 MB/s, 300TBW Varenr: 1005328 / Prodnr: SA1000M8/480GTP-LINK TL-WN822N 11n Wireless AdapterUSB, 300Mbps Varenr: 617287 / Prodnr: TL-WN822NWindows 10 HomeNordic + English Varenr: 200614 / Prodnr: KUK-00001Først person som tar kontakt får 1000kr rabatt ved kjøpet.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=368798902'
    },
    '368999457': {
        'heading': '''HP ProDesk 600 G5 SFF White!''',
        'description': '''Flott HP stasjonær pc selges. Kjapp og kraftig liten sak, i nydelig matt hvit/svart utførelse!Kan brukes til blant annet kontor, gaming, media etc.CPU: Intel i5-8500 @ 4100MHz, 6 kjerner/6 tråderGPU: Sapphire Pulse Radeon RX6400 4GB LPRAM: 16GB (2x8) @ 2666MHzSamsung P991 M.2 SSD - 256GB (W11 PRO Aktivert)Seagate 2TB harddisk (lagring/media)Fast pris.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=368999457'
    },
    '369063129': {
        'heading': '''2080 skjermkort''',
        'description': '''Selger et 2080 skjermkort pga oppgradering. har funket helt fint til nå. ikke merket noe tull med det, aldri overklokket eller noe sånt.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=369063129'
    },
    '369276174': {
        'heading': '''Lenovo ThinkCentre med I5-8500T, 16Gb RAM, 256Gb NVME''',
        'description': '''Lenovo ThinkCentre liten, men rask minidatamaskin til salgs med følgende konfigurasjon:1. Prosessor Intel I5-8500T 6 kjerner/6 tråder, 2.1-3.5GHz, 9Mb Cache2. 16Gb RAM (2x 8Gb 2666)3.  Harddisk 256Gb NVME SkHynix4. Nettverk 1Gbe Intel I219-V5. Skjermkort Intel UHD Graphics 6306. 65W StrømforsyningDenne lille PC-en er perfekt for Smart Home servere (Home assistant, OpenHAB) eller for å bygge din egen router/firewall (jeg kan tilby brakett og nettverkskort).PCIE Bracket for ekstra 500krMellanox ConnectX-3 CX322A 10Gbps, Dual port for ekstra 1000krIntel 10GbE X520-DA2 DUAL SFP+ for ekstra 900krIntel X520-SR1 SFP+ 10Gbps for ekstra 750krIntel I350-T4 Quad 1Gbe for ekstra 700krMellanox Connect X2 MNPA19-XTR SFP+ 10Gbps for ekstra 450krPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=369276174'
    },
    '369286763': {
        'heading': '''ASUS GeForce RTX 2080 ROG Strix OC 8GB''',
        'description': '''Selger min ASUS GeForce RTX 2080 ROG Strix OC 8GB GDDR6 SDRAM,Pent bruktSpecs:Powered by NVIDIA Turing with 1890 MegaHertz Boost Clock (OC Mode) featuring overclocked 8 GigaBytes GDDR6 256 bit memory and 2944 CUDA coresSupports up to 4 monitors with Display Port 1. 4, HDMI 2. 0 and a VR headset via USB Type C portsAuto Extreme and Max Contact Technology deliver premium quality and reliability with aerospace grade Super Alloy Power II components while maximizing heat sink contact.ASUS Aura Sync RGB lighting features a nearly endless spectrum of colors with the ability to synchronize effects across an ever expanding ecosystem of AURA Sync enabled productsGPU Tweak II makes monitoring performance and streaming in real time easier than ever, and includes additional software like Game Booster, X Split Game caster, WT Fast and Quantum Cloud.Triple Axial Tech 0db Fans increase airflow through the heat sink and boasts IP5X dust resistanceDybde 29.97 cmHøyde 13.04 cmBredde 5.41 cmPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=369286763'
    },
    '369821672': {
        'heading': '''Cooler Master Cosmos C700p''',
        'description': '''Den er en beist av en kabinett!Du kan bygge 2 systemer på det.Det er 100% modulært, det er mulig til å skift alt på rammen.RGB på utside( følger med RGB og vifter kontroller.Følger også med Gpu brakett.Selger pga flyttet og har dessverre ikke plass til så store kabinett.Må hentes.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=369821672'
    },
    '369868244': {
        'heading': '''Dell T7500 workstation''',
        'description': '''Dell Precision T7500 Workstation selges. Denne har tidligere blitt brukt som  labPC. men endt opp stående ubrukt da jeg har 2. Kjekk og kraftig maskin for å lære seg virtualisering med f.eks Proxmox eller ESXi eller sette opp NAS med merSpesifikasjoner:CPU: Intel(R) Xeon X5650 @ 2.66GHz(Man kan om ønskelig utvide med å få tak i et datterkort med extra cpu/ram.Denne har ikke det.men enkelt å finne på nett om behov endrer seg)RAM: 24 GB (3x8 GB 1333 MHz DDR3) (+1 reserve)GPU: Nvidia Quadro FX 4800https://i.dell.com/sites/doccontent/shared-content/data-sheets/en/Documents/dell_precision_t7500_specsheet.pdfMaskinen må hentes i Sandnes, da den er stor og tung.Selges uten disker (plass til 4 disker)Stått en stund, men fungerte ved boot nylig.Pris kan diskuteres ved kjapp handelKan også vurdere bytte om du har noe moro å tilby.Søkeord:DellServerHomeassistantNASdual socketXeonIntelPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=369868244'
    },
    '369908670': {
        'heading': '''Skjermkort - GeForce GTX 1070''',
        'description': '''Lett brukt /prøvdSelges kr 2.000,-Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=369908670'
    },
    '370342064': {
        'heading': '''ASUS TUF SABERTOOTH X58, i7 960, 12GB Kingston DDR3''',
        'description': '''Selger et ASUS Sabertooth X58 hovedkort med installert i7 960-prosessor og 12GB Kingston DDR3 RAM i god tilstand. Disse har fungert veldig fint, og har ikke opplevd noen problemer med denne. Alle delene selges for 1200,-.Ta gjerne kontakt hvis det er noe du lurer på!skjermkort grafikkort pc-deler pc i deler komponenter gpu gtxCpu prosessor pc-deler pc i deler komponenter gpu harddisk lagringPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=370342064'
    },
    '370351250': {
        'heading': '''Asia Geforce etc 3080 TUF GAMING''',
        'description': '''Har brukt til gamingpc - selges fordi det ikke brukes lenger.Har opplevd bluescreens - men dette trenger ikke å være grunnet gpu.Selger derfor litt rimeligere.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=370351250'
    },
    '370405331': {
        'heading': '''MSI Radeon 6600''',
        'description': '''Amd skjermkort selges. Kan sendes eller møtes I Oslo.Tar seriøse bud.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=370405331'
    },
    '370432532': {
        'heading': '''MSI Gaming PS''',
        'description': '''Selger min gamle PC. Den klarer å kjøre de fleste gamle spill, og til å med de nye spillene på medium grafikk.Intel Core i7-6700K CPU 4.00 GHzGPU Geforce GTX 1070RAM 16 GBOS Windows 10 HomeLokal disk(C) 237GBLokal disk (D) 1TBPSU 500WPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=370432532'
    },
    '370781696': {
        'heading': '''NVIDIA Quadro P4000 8GB VRAM''',
        'description': '''Selger brukt NVIDIA Quadro P4000 8GB VRAM som er tatt ut av fungerende arbeidsstasjon.Den har stått i en Dell workstation. Kortet har Dell nummer 0TWPW0 / TWPW0Den kan leveres dell brakett for montering i Rack workstation, se bilder.Har flere kort, prisen er per kort.CUDA Cores 1792Peak Single Precision FP32 Performance 5.3 TFLOPSGPU Memory 8 GB GDDR5Memory Bandwidth 243 GB/SecMemory Interface 256-BitSystem Interface PCI Express 3.0 x16Display Connectors DisplayPort 1.4 (4)Maximum DVI-D DL Resolution 1920 x 1200 at 60Hz with Included AdapterHDMI Support Optional AccessoryStereo Connector Optional AccessoryThermal Management Ultra-Quiet FansinkMax Power Consumption 105 WNVIDIA Quadro Power GuidelinesMax Digital Resolution(2x DP Links) 5120 x 2880 x24 bpp at 60hz(7680 x 4320 x24 bpp at 60hz)NVIDIA Quadro and NVS Display Resolution SupportPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=370781696'
    },
    '370794263': {
        'heading': '''Nvidia Quadro P2200 5GB GDDR5X GPU Grafikk kort''',
        'description': '''**Nvidia Quadro P2200 5GB GDDR5X GPU – Ubrukt og klart for salg!**Selger et helt ubrukt **Nvidia Quadro P2200** grafikkort som passer perfekt for grafiske designere, ingeniører, og andre profesjonelle som jobber med krevende applikasjoner innen CAD, 3D-modellering, animasjon og visualisering. Kortet har aldri vært tatt i bruk, og er derfor i ny tilstand.**Spesifikasjoner:**- **Modell**: Nvidia Quadro P2200- **Minne**: 5GB GDDR5X- **Porter**: 4 x DisplayPort 1.4 – Støtter opp til 4 skjermer samtidig- **CUDA Cores**: 1280- **Minnebåndbredde**: 200 GB/sDette grafikkortet er designet for å håndtere profesjonelle arbeidsflyter på en kostnadseffektiv måte, og tilbyr pålitelig ytelse til krevende grafiske programmer som **AutoCAD, SolidWorks, Adobe Creative Cloud, 3D Studio Max**, og andre DCC-programmer.**Quadro P2200** gir også muligheten til å kjøre flere skjermer med 4 x DisplayPort 1.4, noe som er ideelt for designere som trenger en utvidet arbeidsflate eller ønsker å kjøre avanserte visualiseringsprosjekter.**Fordeler:**- Skreddersydd for profesjonelle brukere som trenger høy ytelse til krevende grafikkprogrammer- Gir en pålitelig og stabil opplevelse, også under tunge arbeidsbelastninger- Ubrukt – kortet er som nytt!Ta kontakt ved interesse eller spørsmål! Dette er et kvalitetskort til en svært konkurransedyktig pris.NY-PRIS: 5500-6000kr**Pris: 3499 **Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=370794263'
    },
    '370875638': {
        'heading': '''GIGABYTE RTX 3080 VISION OC''',
        'description': '''Pent brukt Gigabyte Vision OC selges.Kun brukt til gaming, sjeldent vært over 70°C. Fungere som nySendes i originalemballasje.Kan selges eller byttes i et kraftigere grafikkort +  mellomlegg.Pris kan selvfølgelig diskuteres! Gjerne ta kontakt :)(Bilder fra nett fordi gpu\'en står i pc, kan selfølgelig ta ut å sende bilder om ønskelig.)Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=370875638'
    },
    '371305683': {
        'heading': '''Selges Billig: kraftig desktop, Lenovo ThinkStation P510''',
        'description': '''-------------------------------------------------Selges billig.-Kjempegod tilstand.Høy kvalitet, kraftig, holdbar, allsidig desktop/arbeidsstasjon/serverstasjon.-Kostet mer enn 30000kr da den ble kjøpt.-Pris:med 32GB ECC RAM: 5250krmed 64GB ECC RAM: 5830kr--------------------------------------------------Model: Lenovo, ThinkStation P510.-SPECS:-CPU:Intel Xeon E5-1650 v4, 6C/12T, 3.6-4.0 GHz, 15MB cache, 140W.-RAM:Hynix, Registered ECC, 64GB(4x16) eller 32GB(2x16), 2400MHZ / CL17, DDR4, (HMA42GR7AFR4N-UH).-GPU:Nvidia Quadro K620, 2GB, Displayport + DVI-I.-Disk 1:SSD, NVMe M.2, 256GB, Samsung SM951 (MZVPV256HDGL), 2150/1260MB/s read/write.-Disk 2:HDD, 2TB, 7200RPM, Seagate Barracuda (ST2000DM001), cache 64MB.-USB:4x USB 3.0 (rear) + 4x USB 2.0 (rear) + 4x USB 3.0 (front).-Other:Ethernet, Card Reader, HD Audio.-Chassis:01EF302-Link:https://www.lenovo.com/au/en/workstations/thinkstation-p-series/ThinkStation-P510/p/33TS3TPP510-------------------------------------------------Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=371305683'
    },
    '371473839': {
        'heading': '''i9 9900k 5.0 GHz''',
        'description': '''Intel® Core™ i9-9900K Processor16M Cache, up to 5.00 GHzAdd to CompareSpecificationsExport specificationsEssentialsProduct Collection9th Generation Intel® Core™ i9 ProcessorsCode NameProducts formerly Coffee LakeVertical SegmentDesktopProcessor Numberi9-9900KLithography14 nmRecommended Customer Price$488.00Sign in with your CNDA account to view additional SKU details.CPU SpecificationsTotal Cores8Total Threads16Max Turbo Frequency5.00 GHzIntel® Turbo Boost Technology 2.0 Frequency‡5.00 GHzProcessor Base Frequency3.60 GHzCache16 MB Intel® Smart CacheBus Speed8 GT/sTDP95 WSupplemental InformationMarketing StatusDiscontinuedLaunch DateQ4\'18Embedded Options AvailableNoUse ConditionsPC/Client/TabletIncluded ItemsPlease note: The boxed product does not include a fan or heat sinkDatasheetView nowAdditional InformationView nowMemory SpecificationsMax Memory Size (dependent on memory type)128 GBMemory TypesDDR4-2666Max # of Memory Channels2Max Memory Bandwidth41.6 GB/sECC Memory Supported ‡NoGPU SpecificationsGPU Name‡Intel® UHD Graphics 630Graphics Base Frequency350 MHzGraphics Max Dynamic Frequency1.20 GHzGraphics Video Max Memory64 GB4K SupportYes, at 60HzMax Resolution (HDMI)‡4096 x 230x424HzMax Resolution (DP)‡4096 x 2304x60HzMax Resolution (eDP - Integrated Flat Panel)‡4096 x 2304x60HzDirectX* Support12OpenGL* Support4.5Intel® Quick Sync VideoYesIntel® InTru™ 3D TechnologyYesIntel® Clear Video HD TechnologyYesIntel® Clear Video TechnologyYes# of Displays Supported ‡3Device ID0x3E98Expansion OptionsScalability1S OnlyPCI Express Revision3.0PCI Express Configurations ‡Up to 1x16, 2x8, 1x8+2x4Max # of PCI Express Lanes16Package SpecificationsSockets SupportedFCLGA1151Max CPU Configuration1Thermal Solution SpecificationPCG 2015DTJUNCTION100°CPackage Size37.5mm x 37.5mmAdvanced TechnologiesIntel® Optane™ Memory Supported ‡YesIntel® Turbo Boost Technology ‡2.0Intel® Hyper-Threading Technology ‡YesIntel® Transactional Synchronization ExtensionsYesIntel® 64 ‡YesInstruction Set64-bitInstruction Set ExtensionsIntel® SSE4.1, Intel® SSE4.2, Intel® AVX2Idle StatesYesEnhanced Intel SpeedStep® TechnologyYesThermal Monitoring TechnologiesYesIntel® Identity Protection Technology ‡YesSecurity & ReliabilityIntel vPro® Eligibility ‡Intel vPro® PlatformIntel® AES New InstructionsYesSecure KeyYesIntel® Software Guard Extensions (Intel® SGX)Yes with Intel® MEIntel® Memory Protection Extensions (Intel® MPX)YesIntel® OS GuardYesIntel® Trusted Execution Technology ‡YesExecute Disable Bit ‡YesIntel® Boot GuardYesIntel® Stable IT Platform Program (SIPP)YesIntel® Virtualization Technology (VT-x) ‡YesIntel® Virtualization Technology for Directed I/O (VT-d) ‡YesIntel® VT-x with Extended Page Tables (EPT) ‡YesPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=371473839'
    },
    '371591158': {
        'heading': '''Skjermkort''',
        'description': '''Asus Radeon RX 5700 Duall Evo OCKjøpt for 4 år siden.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=371591158'
    },
    '371619717': {
        'heading': '''Nvidia 1080 Seahawk Vannkjølt. Stillegående (bare GPU)''',
        'description': '''Selges se bilderPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=371619717'
    },
    '371725136': {
        'heading': '''GeForce RTX™ 3060 Ti GAMING OC PRO 8G (rev. 2.0)''',
        'description': '''Velfungerende skjermkort selges til fordel for videre oppgradering. Funger fintPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=371725136'
    },
    '371727614': {
        'heading': '''RX 6700 XT Speedster Qick 319 GPU''',
        'description': '''Selges en fint brukt rx 6700 xt gpu har blitt brukt 1-2 år og fungerer fortsatt utmerket jeg har akkurat skiftet kjølepasta på gpu så da er det bare å kjøre på å spille :)Letter etter også en RTX 4060om du har jeg villig til å bytte men da betaler du mer.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=371727614'
    },
    '371758716': {
        'heading': '''AMD RADEON RX 6900 XT''',
        'description': '''AMD XFX Radeon RX 6900XT (6900-XT). Ikke mye bruktXFX Speedster MERC319 RX 6900XT (Limited Black edition)Er interessert i å bytte med en 7900 XT, 7900 XTX, 4080, eller 4080 super med mellomlegg fra min side (:Opptil 2495 MHz i klokkefrekvens16 GB GDDR6-minnePCI Express 4.0 x16AMD RDNA 2-arkitekturDirectX 12 UltimateNypris på denne var 15 990 kr. Kun brukt til gaming, maks 10 ganger. Ingen mining.6900 XT er på par med RTX 3090 og RTX 3080 Ti, og bedre enn 4070. Ta kontakt for informasjon☺️Søkeord: GPU, Grafikkort, 7900 XTPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=371758716'
    },
    '371834349': {
        'heading': '''Rog Strix RX580 T8G Gaming''',
        'description': '''Selger to skjermkort pga oppgradering.Kortene har funket supert for min del. Drar ikke de tyngste spillene, men klarer mye.Ikke overklokket.Kjøpt på komplett.Selges hver for seg 1200,- eller samlet 2000,-.Kan sendes som fiks ferdig.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=371834349'
    },
    '371966730': {
        'heading': '''SONNET eGFX Breakaway Box 550''',
        'description': '''Connect a Demanding Graphics or PCIe Card to a Thunderbolt 3 Mac or PCSonnet’s eGFX Breakaway Boxes are a family of Thunderbolt 3 to PCIe card expansion solutions that support any Thunderbolt compatible PCIe card, but are designed specifically for bandwidth-intensive AMD and NVIDIA graphic video cards. The eGFX Breakaway Box 550 includes two 8-pin (6+2 pin) auxiliary power connectors and supports cards requiring 375W of power (equivalent to 600W recommended system power) more than enough capability to support nearly every compatible GPU card, with the exception of ones such as the AMD Radeon RX Vega 64, Vega Frontier Edition, WX 9100, and overclocked NVIDIA cards with extremely high peak power requirements. Depending on your OS, there\'s a graphics card suitable for your needs.Ready for Work and Always Game to Play – eGFX Breakaway Box, the Coolest and Quietest eGFX Graphics Card Box on the MarketThe coolest and quietest graphics card expansion systems on the market, eGFX Breakaway Boxes feature a large variable-speed, temperature-controlled fan that quietly and effectively cools the installed card – perfect for noise-sensitive environments. For professionals, the Breakaway harnesses the computational engine in today’s GPU cards that are accelerate special effects, animation, color grading, rendering, and editing. For gamers, the Breakaway Box is ideal for enabling graphic-intensive gaming on computers (such as thin/light notebooks) that otherwise would not be able to produce an acceptable gaming experience. Additionally, the eGFX Breakaway Box supports graphics cards with 120mm water block coolers. Water block coolers run quieter than active fans; plus water block coolers enable higher overclocking.Eco-friendly Thunderbolt 3 Power FeaturesThunderbolt 3 provides eco-friendly power features to help save power and energy when your computer is not in use. Sonnet\'s eGFX Breakaway Box, like all Thunderbolt devices, powers on when connected via a Thunderbolt cable to a live Thunderbolt computer. This features allows the Breakaway Box to power down and save energy when the computer is shut down, disconnected, or put to sleep. As a bonus, the device still provides power to charge most computers even when the computer is sleeping. Thunderbolt 3 Power Delivery (PD) allows devices to power and charge notebook computers. The eGFX Breakaway Box 550 provides 87W of upstream power, useful for quickly charging your notebook.eGFX Breakaway Box 550: Add Your Own Choice of Graphics Cards AccelerationSonnet\'s Breakaway Boxes boost the graphics performance of an eGFX-compatible computer by connecting a high-performance desktop GPU card via a Thunderbolt 3 port. Add your choice of compatible graphics card to the Breakaway Box and connect to your computer with a Thunderbolt cable. Alternatively, if you need a cost-effective Thunderbolt expansion system for a Thunderbolt-compatible, non-GPU PCIe card (such as the Avid Pro Tools|HDX [power adapter cable sold separately] or RED ROCKET-X), the Breakaway Box offers all the space and power you could possibly need for single PCIe card expansion.- Power Supply: 550 power supply (equivalent to 600W recommended system power)- Power Connector: Two 8-pin (6+2 pin) power connectors- Card Power Support: Supports up to 375W card- Notebook Charging: Charging up to 87WPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=371966730'
    },
    '372529667': {
        'heading': '''Acer Aspire // i5-11400f // 16gb RAM // GTX 1650''',
        'description': '''Selger en brukbar gaming PC som også passer fint til mye annet bruk. Den er rask og jeg har innstallert bedre kjøler for CPU slik at den jobber enda bedre :) Grunnet størrelsen på kjøleren så må den ene siden være åpen, men det gjør bare at det er enda bedre lufting, med tanke på at det er et lite kabinett, så det gagner resten av delene der inne også :)CPU: i5-11400fRAM: 16GB DDR4SSD: m.2 500gbGPU: GTX 1650Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=372529667'
    },
    '372580059': {
        'heading': '''Strøken ikke brukt Quadro M4000 Nvidia  8GB Vram''',
        'description': '''Selger en helt strøken og så godt som ikke brukt M4000 kort brukt 1 dag til AI testing/ rendering.  Dette er korte du trenger for AI og video rendering. 4 stk displayport utganger (har ikke HDM). Mulig å koble til 4 skjermer.Ny pris 24.000 kr.- Kan få med bracket for bak feste. (følgte med i esken)GPU Memory 8 GB GDDR5Memory Interface 256-bitMemory Bandwidth 192 GB/sNVIDIA CUDA® Cores 1664System Interface PCI Express 3.0 x16Max Power Consumption 120 WThermal Solution ActiveForm Factor 4.4” H × 9.5” L,Single Slot, Full HeightDisplay Connectors 4x DP 1.2Max SimultaneousDisplays4 direct, 4 DP 1.2Multi-StreamMax DP 1.2 Resolution 4096 × 2160 at 60 HzMax VGA Resolution 2048 × 1536 at 85 HzGraphics APIs Shader Model 5.0,OpenGL 4.54,DirectX 12.05Compute APIs CUDA, DirectCompute,OpenCL™Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=372580059'
    },
    '372663343': {
        'heading': '''3060 Geforce Rtx''',
        'description': '''Selger et RTX 3060 dual 12 g skjermkort.Kortet tar liten plass da det er kun 24 cm langt, 3,8 cm bredt og 11 cm høyt.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=372663343'
    },
    '372850314': {
        'heading': '''Selger kabinett samt power supply og skjermkort. Det medfører et hovedkort.''',
        'description': '''Asus Z87-pro med I7 prosessor, dette kan ha skader og vifte til prosessor er defekte. Så tar bare betalt for power supply og kabinet. Skjermkort medfølger eller ting kan selges separert.Selger kabinett samt power supply og skjermkort. Det medfører et hovedkort som jeg ikke vet om at den viker. AltsåPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=372850314'
    },
    '372925719': {
        'heading': '''Acer Nitro N50-640 (LES BESKRIVELSE)''',
        'description': '''Selger det som er igjen av en Acer Nitro N50-640 etter deler ble brukt til bygging av ny pc. Prosessor, RAM, lagringsenhet og skjermkort mangler. Kan gi rabatt om den hentes i HaugesundPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=372925719'
    },
    '373076316': {
        'heading': '''Asus ROG Strix GeForce GTX 1080 Ti OC grafikkort 11G''',
        'description': '''Med Asus ROG Strix GeForce GTX 1080 Ti OC-grafikkort kan du øke gamingytelsen til din stasjonære gaming-PC og gjøre den i stand til å takle selv AAA-spill med fullt detaljnivå og 4 K-oppløsning. Grafikkortet bruker et meget bredt 352-bit grensesnitt og 11 GB rask GDDR5X RAM for å takle de mest krevende spillene. Med OC Mode kan du øke både klokke- og kjernefrekvensen når du trenger mer kraft til krevende applikasjoner og program.Kjøling: Med triple Wing Blade-vifter og MaxContact-radiator med varmerør har direktekontakt med CPU-en, slik at varmen fjernes raskere og ytelsen holdes stabil selv ved krevende gaming. Samtidig gjør vingeformene på viftene at lydnivået holdes lavt. Med Asus FanConnect kan du også koble to GPU-styrte viftetilkoblinger til hovedkortet og gi hele PC-en optimal kjøling.Nvidia G-Sync: Denne teknologien synkroniserer oppdateringsfrekvensen til G-Sync-kompatible skjermer med grafikkortet for å minimere hakking og forsinkelse.VR Ready: Nvidia VR Ready-sertifisering gjør kortet ideelt for VR-spill og apper. Med HDMI-utgang kan du koble til ditt VR-headset uten å koble fra skjermen.AuraSync RGB-belysning: Velg blant over 16,7 millioner farger og seks ulike effekter for LED-belysninger på bakplaten og på frontkjøleren.Egenskaper:- PCI Express x16 3.0 bus- 11 GB GDDR5X minne- 3584 CUDA cores- 11010/11100 MHz memory clock frekvens (OC-modus/Gaming-modus)- 1594/1708 MHz GPU core clock frekvens i OC-modus (GPU Boost off/on)- 1569/1683 MHz GPU core clock frekvens i Gaming-modus (GPU Boost off/on)- 2x HDMI, 1x DVI-I og 2x DisplayPort-tilkoblinger- Støtte for 8K-skjermer (7680 x 4320)- Støtte for opptil 4 skjermer samtidig- DirectX 12-støtte- Asus GPU Tweak 2-app- Nvidia SLI-støtte- Nvidia VR Ready- Robust bakplate som hindrer at kortet bøyesPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=373076316'
    },
    '373098923': {
        'heading': '''Asus strix gtx1070 8g gaming''',
        'description': '''fullt fungerende skjermkort, kjøleren sprekker litt ved oppstart, men alt er i orden umiddelbart, jeg selger fordi datamaskinen min ikke er utstyrt med kjøling for dette skjermkortet, ikke utvunnet, ikke brukt i det hele tattPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=373098923'
    },
    '373201202': {
        'heading': '''Grafikkort EVGA 3070 stor utgave, pent brukt!''',
        'description': '''Selger skjermkortet EVGA stor utgave 3070 non LHRPris: 4.000krFørste mann til mølla!NB! Kun seriøse henvendelser blir besvart, ingen bytter er aktuellePluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=373201202'
    },
    '373202202': {
        'heading': '''Salg på palit 3070 rtx skjermkort! Salg!''',
        'description': '''Salg på 3070 rtx skjermkort!Kun seriøse henvendelser blir besvart!Pris 4000!Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=373202202'
    },
    '373202303': {
        'heading': '''RTX 2070 super! Salg!''',
        'description': '''Selger pent brukt skjermkort 2070 super! Kun seriøse henvendelser blir besvart! Pris 2500Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=373202303'
    },
    '373345714': {
        'heading': '''Asus Dual Radeon RX 7900 GRE OC''',
        'description': '''Asus Dual Radeon RX 7900 GRE OC- Kortet er tatt ut av pcen 26.10.2024 , og klar til sending / bli hentet.Ny pris :7999krhttps://www.komplett.no/product/1306067/datautstyr/pc-komponenter/skjermkort/asus-dual-radeon-rx-7900-gre-ocKortet er kjøpt i August , men blitt brukt minimalt fram til nå grunner sykdomFølger med kvittering , der noe av informasjonen er tatt bort/sensurert . Komplett krever kvittering for garanti .Denne versjonen av 7900 GRE kortet skal være en av modellen med best kjøling og minst støy i følge komplett.Toms Hardware skal være en troverdig kilde for å vite hvordan skjermkortet presterer i spill .https://www.tomshardware.com/reviews/gpu-hierarchy,4388.htmlBILDE 2 : Her her oppløsning 1440p ULTRA vist, og hvordan 7900 GRE forventes å prestere i forhold til andre kort på markedet.*Eneste som ikke følger med er aktiveringskodene til de 2 spillene man får gratis med , for de er koblet til en konto nå og jeg tror ikke jeg får videreført de til en annen konto .Kortet er strøkent.Ønsker helst at kortet hentes , men kan vurdere sending også.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=373345714'
    },
    '373612728': {
        'heading': '''Selger et MSI RTX 3070 Suprim X 8G LHR grafikk-kort.''',
        'description': '''Selger et MSI RTX 3070 Suprim X grafikk-kort. Kjøpt på Komplett i slutten av 2022, men har blitt relativt lite brukt till spilling pga. studier. Kjempebra skjermkort med myte ytelse og god kjøling, som har mange muligheter for instilling av RGB-lys.Ingen feil eller mangler som jeg vet om, der det har blitt brukt med støtte hele veien. Har heller ikke blitt brukt til mining og ingen problem med coil-whine.Kan lese mer om skjermkortet her: https://www.power.no/data-og-tilbehoer/datakomponenter/grafikkort/msi-geforce-rtx-3070-suprim-x-8gb-lhr-grafikkort/p-1465759/Har original boks til kortet.Kort kan sendes på kjøpers regning og risiko.Pris er fastsatt.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=373612728'
    },
    '373644889': {
        'heading': '''ASUS GTX 1080 TI STRIX i perfekt tilstand''',
        'description': '''grafikk kortet virker uten problem og har vert lite brukt, uheldigvis så er original emballasjen rotet vekk men jeg har bra nokk beskyttelse til den for at det ikke er et problem.selges for en høg pris fordi tilstanden er så bra og er perfekt som et samle objekt eller bare som en gpu som fortsatt er kraftig og med mer en nokk vram.om du lurer på noe så er det bare å spørPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/373644889'
    },
    '373835804': {
        'heading': '''NVIDIA GeForce 1080 SeaHawk X''',
        'description': '''Selger et pent brukt vannkjølt skjermkort som yter utrolig bra til 1080p gaming. Har selv brukt kortet til å spille Fortnite, Call of Duty, League of Legends og div andre spill og kortet har taklet det helt fint. Kortet har vært i samme rig hele livet sitt og aldri blitt flyttet på / solgt brukt før nåFølger med vifte til radiator.Har ikke original boks men kommer i en antistatisk pose pluss godt innpakket ved sending i post.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=373835804'
    },
    '373940998': {
        'heading': '''Lenovo legion t5''',
        'description': '''Det er en pc med skjermkort Geforce rtx 3060 og ryzen 5 3600 prosessor. Jeg utviklet ramme med 2x 16 altså 32gb og 3 nye rgb vifter.Jeg har også utstyr om du er interessert er deg bare til og spør 😊Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/373940998'
    },
    '248292079': {
        'heading': '''PowerColor Red Dragon Radeon™ RX 570 4GB - Nytt kort''',
        'description': '''Nytt skjermkort / grafikkort selges.PowerColor Red Dragon Radeon™ RX 570 4GB.Har hatt dette kortet liggende som backup. Kortet er aldri tatt i bruk. Eske er uåpnet.Fastpris 1200https://www.powercolor.com/product?id=1544155762Kan sendes for 69,- med PostNord og forskuddsbetaling, eller med \"Fiks ferdig\".Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=248292079'
    },
    '262092327': {
        'heading': '''ZOTAC ZBOX ID90''',
        'description': '''CPU: Intel i7-3770T 2.5GHz (3.7GHz Turbo)GPU: Intel HD Graphics 4000RAM: 16GB SO-DIMM DDR3DISK: Support 2.5-inch SATA 3.0 Gb/s HDD/SSDhttp://old.zotac.com/kr/products/mini-pcs/zbox/product/zbox/detail/zbox-id90/sort/starttime/order/DESC/amount/10/section/specifications.htmlPent brukt , men trenger \"19V PSU 90W\"https://www.enter.no/zotac-power-supply-90w-zbox/cat-p/c/p8046983Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/262092327'
    },
    '301727097': {
        'heading': '''Selger 9 stk skjermkort!''',
        'description': '''Selger 9 stk skjermkort:2 stk Radeon rx5700 ,2000 kr1 stk  Radeon rx 5600  1800 kr2 stk msi 1080 ti,  1500 krOg noen andre kortEr ikke pris for alle kort!Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=301727097'
    },
    '320435726': {
        'heading': '''GeForce RTX ZOTAC 2060''',
        'description': '''Brand ZotacGraphics RAM size 6 GBGPU clock speed 1680 MHzVideo output interface HDMIGraphics processor manufacturer NVIDIAGraphics RAM type DRAMRecommended uses for product GamingPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/320435726'
    },
    '325177640': {
        'heading': '''Hp Z600 workstation''',
        'description': '''Kraftig maskin44gb minne (20 gb brukbar)Quadro4000 skjermkortXeon E5630 2;52ghz500gb hddWin 10 pro uten lisensnøkkel6Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/325177640'
    },
    '338264544': {
        'heading': '''LOUQE Ghost S1 MK III  Arctic White - [NY]''',
        'description': '''LOUQE Ghost S1 mini ITX kabinett i fargen Arctic White vurderes solgt. Dette er ett eksklusivt mini ITX kabinett i anodisert aluminium fra den svenske produsenten LOUQE.Produktet er nytt og i uåpnet eske.Her har du muligheten til å sikre deg dette eksklusive mini ITX kabinettet fra Louqe i ny og ubrukt tilstand.PCIe 16x Gen4 riser medfølger.https://www.louqe.com/portfolio/ghost-s1/Spesifikasjoner:• DIMENSIONS (H x W x D): 188 x 140 x 322 mm• VOLUME: 8.2 L• WEIGHT: 2.5 kg• COLOR: Ash, Limestone and Arctic White• MATERIAL: Glass blasted hard anodized & cerakoted aluminum• RAGTAG: Vegan leather• TOPHATS (ACCESSORY): M: 26 mm, L: 57 mm• GPU SUPPORT: Dual-Slot up to 145 x 45 x 305 mm• MOTHERBOARD SUPPORT: Mini-ITX• POWER SUPPLY SUPPORT: SFX, SFX-L• CPU HEATSINK SUPPORT: Up to 66 mm• WATER COOLING SUPPORT: 240 mm AIO radiator thickness 31.5 mm, 2 x 25 mm high fans w. L TopHat• STORAGE SUPPORT: Up to 3 x 2.5″ HDD/SSD with tray + M.2 SSD• PCI RISER: Included Twin Axial 260 mm PCIe 16x Gen4 riserFastpris 3000,-. Frakt med Norgespakke koster 135,-. Betaling med Vipps på forskudd, eller kjøp med \"Fiks ferdig\".Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=338264544'
    },
    '338944206': {
        'heading': '''NVIDIA Jetson Nano 2GB (Ny)''',
        'description': '''NVIDIA Jetson Nano 2GB(kun kortet, nytt/uåpnet)GPU 128-kjerners NVIDIA Maxwell™CPU Quad-kjerne ARM® A57 1,43 GHzMinne 2 GB 64-bit LPDDR4 25,6 GB/sLagringsplass microSD (kort ikke inkludert)Videokoding 4Kp30 | 4x 1080p30 | 9x 720p30 (H.264/H.265)Videodekoding 4Kp60 | 2x 4Kp30 | 8x 1080p30 | 18x 720p30 (H.264/H.265)Tilkoblingsmuligheter Gigabit EthernetKamera 1 x MIPI CSI-2-kontaktSkjerm HDMIUSB 1x USB 3.0 type A, 2x USB 2.0 type A, 1x USB 2.0 Micro-BAnnet 40-pinners hode (GPIO, I2C, I2S, SPI, UART)12-pinners hode (strøm og relaterte signaler, UART)4-pinners viftehode*Maskinvare 100 mm x 80 mm x 29 mm(Wifi USB-dongle følger ikke med)Søkeord: Belabox encoder irl streamingPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=338944206'
    },
    '341853146': {
        'heading': '''Dell Presision 3640 Perfekt for VR Gaming.''',
        'description': '''Selger min VR Gaming pc da jeg ikke har bruk for denne lenger. Den er super til alle oppgaver om det skulle være VR, hjemmekontor eller videoredigering.NøkkelspesifikasjonCPU: Intel i7-10700RAM: 16GBLagring: 512 SSDGPU: NVIDIA GeForce RTX 2080 TiWindows 11 ferdig installert.Dell Precision 3640 MT stasjonær PC gir deg kraften du trenger for å lage VR-innhold, modellere eller rendre bilder og filmer. Den har en 10. generasjons Intel Core-prosessor som sikrer deg stabil arbeidsflyt hver eneste dag. Bedriftsapplikasjoner vil kjøre effektivt takket være Independent Software Vendor-sertifisering (ISV).10. generasjons ytelsePC-en er utstyrt med en kraftig 10. generasjons åttekjernet Intel Core i7-prosessor fra Comet Lake-serien som kan kjøre flere ressurskrevende programmer samtidig. Ved behov kan den øke klokkefrekvensen til 5,1 GHz i turbomodus, og den støttes av integrert Intel UHD Graphics 630 og 16 GB rask DDR4 RAM (kan utvides opptil 128 GB).SSD-diskPC-en er utstyrt med en lynrask 512 GB SSD-disk som sikrer ekstra rask oppstart av både PC og programmer.Power-off-ladingDen ene USB-porten lar deg lade dine mobilenheter når PC-en er avslått.Tilkoblingsmuligheter- 2 stk. DisplayPort 1.4-utganger for skjerm eller projektor- 4 stk. USB-A 2.0-porter- 5 stk. USB-A 3.2-porter- 1 stk. USB-C 3.2 Gen2-port med evne til strømforsyning- Gigabit Ethernet LAN-port- 3,5 mm port til hodetelefonerCD spiller medfølgende ikke!Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=341853146'
    },
    '341971152': {
        'heading': '''RED DRAGON RX 6800XT 16GB GDDR6 RAM''',
        'description': '''Kjøpt dette skjermkortet i 2022 og har blitt pent brukt siden.Brukt mest til gaming som CS, WZ og WOW.Et veldig bra kort som gir bra fps i så og si alle spill, men selger dette pga oppgradering.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=341971152'
    },
    '343030548': {
        'heading': '''Skjermkort MSI GeForce GTX 1070 ARMOR 8G OC''',
        'description': '''Разгонная версия видеокарты GeForce GTX 1070 от MSIЯ продаю эту видеокарту, потому что она использовалась в дополнительном компьютере, которым я больше не пользуюсь.Я не играл на дополнительном компьютере. Видеокарта использовалась для работы на компьютере. Он никогда не использовался для добычи полезных ископаемых. påВидеокарта в хорошем состоянии и работает без проблем.Внутри нет пыли, болельщики работают тихо, без нагрузки болельщики останавливаются и их вообще не слышно.Это не оригинальная упаковка.Не отправляет по почте.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=343030548'
    },
    '345311634': {
        'heading': '''Samsung Radeon Rx Vega 64 8gb graphics card/ skjermkort''',
        'description': '''Funger veldig braEngine Clock: Up to 1677 MHzMemory: 8GB/2048 bit HBM2 945 MHz 1.89 GbpsStream Processors: 40964K GamingLiquid CoolingPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/345311634'
    },
    '346082927': {
        'heading': '''Zotac GeForce GTX 1080 AMP EXTREME 8GB''',
        'description': '''Selger Zotac GeForce GTX 1080 AMP EXTREME 8GBKjøpt brukt av gamer og brukt til gaming selv, fungerer utmerket.Testet kortet og det gir fremdels bra resultater:Fortnite: 3440x1440 - ca 100 fpsHeaven Benchmark: 2560x1440 - 100 fps, 1920x1080 - 180 fpsSolid og veldig stabilt og kjølig skjermkort. Kortet sluker ikke strøm, og trenger bare 270W, med 500W powersupply som anbefalt og 2stk 8 pins koblinger. Dette kortet har 5 utganger og støtter 4 skjermer 3 Displayport, 1 HDMI og DualLink DVI!Viftene kan skru seg litt av og på, men dette kan styres i Firestorm appen. Den ene viften er byttet.Specs:GPUGeForce® GTX 1080CUDA kjerner 2560Video RAM 8GB GDDR5XMemory Bus 256-bitMer specs:https://www.zotac.com/us/product/graphics_card/zotac-geforce-gtx-1080-amp-extremeKan sendes i (4070 esken) eller hentes.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/346082927'
    },
    '351376977': {
        'heading': '''Ekstern GPU m thunderbolt''',
        'description': '''Jeg har to flotte eksterne kabinetter for skjermkort som muilgjjør spilling på laptops og andre svakere ting. Hvis du f.eks har et Geforce 1080TI liggende, og kjører det inn, kan de lett kjøre AAAA gamles på laptopen da at kjøres på grafikkkortet. Enkelt å ta med eg og trenger ikke noe vedlikehold.Kan også brukes i serverer hvor du trenger en ekstre GPU for redering og transcoding.Er mer testet fra min del, men jeg puttet et 1080TI i det, og spilte både FFXIV og kunne transcode og bruke LLM til native ytelse på kortet.P.S Jeg har to, så prisen på 3500 er for en. Ønsker du begge gi beskjed når du kjøper, eller by dpbbel 6500 (så er ndet rabatt på nummber 2)Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=351376977'
    },
    '354979726': {
        'heading': '''AMD RX5700 i god stand selges''',
        'description': '''Dette skjermkortet selges pågrunn av overgang til nytt.Har brukt denne selv til masse fps spill så dette kortet tåler en trykk.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/354979726'
    },
    '355002214': {
        'heading': '''RX6750 Skjermkort''',
        'description': '''Lite brukt RX 6750 XT selges pga oppgradering!RX 6750 XT yter ca. likt med RTX 3070 fra Nvidia, til og med bedre på enkelte spill! Så her får du en rask GPU til en god penge!https://prisguiden.no/produkt/amd-radeon-rx-6750-xt-550984?source=google&ref-site=SEM&ref-ad=google&gclid=Cj0KCQjw2v-gBhC1ARIsAOQdKY1rcAtdQ_f7WX2lUylgPpJiW4zuxX7M4CnaoTKOgLb8-Lw5TSYc_QIaAsxXEALw_wcBSøkeord: Skjermkort, PCI-Express 4.0, 16GB GDDR6X, Ampere, grafikkort, gpu, pc, gaming, mining, nvidia, graphics card, build, rtx 3080, radeon, desktop, redigering, warzone, rocket league, gta 5,xt, fortnite, minecraft, stream, streaming.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=355002214'
    },
    '360692311': {
        'heading': '''14stk. Diverse Vintage Grafikkort''',
        'description': '''Diverse vintage GPU fra rundt 2003 frem til ca. 2013Nvidia:GTS450Quadro FX 1000GeForce FX5500Dell GeForce GT330Quadro FX 570GeForce 605 1GBGeForce 405 1GBQuadro FX3500Quadro 2000AMD / ATI:ATI Radeon X1300 PROAMD Radeon HD 6950 1GBATI Radeon HD 3450AMD Firepro 2270Matrox P69-MDDE128FSelges samlet. Usikker stand. Pris er for alle kort. Kom gjerne med bud.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=360692311'
    },
    '360932309': {
        'heading': '''HP EliteDesk 800 G3 (TWR) med Windows 11 Pro, 32GB RAM, 512GB NVMe, 1TB SSD''',
        'description': '''Her får du en svært god og kraftig datamaskin fra merkevareprodusent:- HP EliteDesk 800 G3 (TWR kabinett) med Windows 11 Pro (64-bit)- CPU: Intel Core i5-7500 (3.4 GHz, up to 3.8 GHz maximum Turbo Frequency)/(4-cores)- Optisk stasjon: HP 9.5 mm Super Multi DVD Writer (PLDS DVDRW DU8AESH)- Lagring: 512 GB NVMe drive, 1 TB SSD drive- RAM: 32GB (DDR4)- GPU: Intel UHD Graphics 630 (1GB RAM)- Trusted Platform Module (TPM) 2.0- USB 2.0: (2) front; (2) baksiden- USB 3.1 Gen 1: (2) front (inkludert 1 hurtilader); (4) baksiden- USB Type-C 3.1 Gen1, front- 1x HDMI videoutgang- 2x DisplayPort videoutganger- 1x Ethernet, Fast Ethernet, Gigabit Ethernet port- Headset (front)- Front: Audio-out (headphone)/Audio-in (microphone) combo jack; (1) Audio-out (headphone) jack- Baksiden: Audio-out jack for powered audio devices; (1) Audio-in jack- Innebygget strømforsyning: 180 Watt PSU- W x D x H (mm): 388.11 x 308.10 x 100.08- Vekt: ca. 5.4 kgFor mer info: https://support.hp.com/us-en/document/c05369814Leveres med strømkabel og DisplayPort kabel. Klar til bruk.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=360932309'
    },
    '361959373': {
        'heading': '''Lenovo V520S, Intel i5-7400, DDR4-8gb, SSD M2-128Gb, HDD-1Tb, Wi-Fi, Win 10 Pro''',
        'description': '''Lenovo V520S stasjonær pcFungerer som de skal.Klar til full bruk, ingen koder eller kontoerSpesifikasjoner:- Lenovo V520S- Windows 10 Pro 64-bit- 8 gb ram DDR4 2400Mhz-Intel  i5-7400- 3.00Ghz cpu, turbo boost til 3,50Ghz 4/4 core, cache 6Mb- SSD M2- 128Gb,  HDD - 1000 Gb- Intel HD graphics 630 Skjermkort- PCIe kortplass for ekstra grafikkort- DVD-RW Brenner- 8x USB (4x USB 3.0) VGA, HDMI, DP,  LAN- Strømledning inkludert- Dimensjoner: 345x275x85 mm.- Pris: 1800 kr. er fast !- Kan leveres til Skedsmokorset, Jessheim......Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=361959373'
    },
    '367271764': {
        'heading': '''ASUS Radeon RX6600XT DUAL OC''',
        'description': '''Pent brukt skjermkort selges, kommer med DP kabel.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/367271764'
    },
    '368075062': {
        'heading': '''Server HP Proliant DL380 gen9''',
        'description': '''Til salgs pent brukt min server som ble brukt som arbeidsmaskin.HP Proliant DL380 gen9CPU 2 x Xeon E5-2673 v3 12c/24thRAM 64GB DDR4 2133 ECCRAID HP B140iLFF -SSD converter x2LFF HOTSWAP X2ETHERNET HP 331FLR Quad PortFIBER Emulex LPe12000 Single Port - 8Gbps SFP+Extra kort ST Lab PCIe 3.0 USB3.1 4-PortGPU (kan demonteres om  ønskelig) AMD Radeon Pro WX2100 2GBStrøm 2  x 500W PlatinumKlistremerke med lisens Windows 10 proEDITJeg fant rail kit KINGSLIDE som passer denne maskinAlt virker som den skal, selges pga oppgradering til nyere arbeidsmaskin.Pris kan diskuteres ved hurtig handel. Kan selge med faktura (pris plus mva)Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/368075062'
    },
    '368158855': {
        'heading': '''HP ProDesk 400 G4 (SFF) med Windows 11 Pro, 32GB RAM og 1TB SSD''',
        'description': '''Her får du en svært god og kraftig datamaskin fra merkevareprodusent:- HP ProDesk 400 G4 (SFF kabinett) med Windows 11 Pro (24H2 versjon)- CPU: Intel Core i5-7500 (3.4 GHz)/(Up to 3.8 GHz maximum Turbo Frequency)- Optisk stasjon: HP 9.5 mm Super Multi DVD Writer (GUD1N)- Lagring: 1TB SSD drive- RAM: 32GB (DDR4)- GPU: Intel UHD Graphics 630- Trusted Platform Module (TPM) 2.0- USB 2.0: (4) baksiden- USB 3.1: (2) front, (2) baksiden- 1x VGA videoutgang- 1x DisplayPort 1.2 videoutgang- 1x Ethernet, Fast Ethernet, Gigabit Ethernet port- Headset inngang (front)- Audio linje-inn (baksiden)- Audio linje-ut (baksiden)- Innebygget strømforsyning: 180 Watt PSU- W x D x H (mm): 269.24 x 297.18 x 93.98- Vekt: ca. 4.6 kgFor mer info: https://support.hp.com/us-en/document/c05362196Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/368158855'
    },
    '368624257': {
        'heading': '''Sapphire RX 590 Special Edition 8GB GDDR5 Graphics Card''',
        'description': '''Et av de raskeste RX 590 8GB skjermkortene som er lansert.Spillytelse på linje med NVIDIA GTX 1650 Super.Passer godt til 1080p budsjettgaming.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=368624257'
    },
    '368633429': {
        'heading': '''SilverStone Sugo SG15''',
        'description': '''Som nytt, pent brukt. Helt rått PC kabinett av ren kvalitet.Nypris på 2500++Kan bruke stort skjermkort + 240MM AiO vannkjøler.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=368633429'
    },
    '368963933': {
        'heading': '''HP ProDesk''',
        'description': '''Windows 11- 8 GB RAM- 500 GB Disk- Intel i5- 2 x Displayport- LAN-port- 6x USB- Intel HD 4600 skjermkort- 2x inngang for hodetelefonerDenne passer perfekt som media PC, student PC, og til kontorarbeid og nettsurfing.Utrolig fleksibel Intel i5 med oppgraderingsmuligheter både av Minne og lagring. Udødelige PCer som takler det meste fra gaming til stand og skilt oppgaver.Se bilder eller ta kontakt for mer info.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=368963933'
    },
    '369463637': {
        'heading': '''Geforce RTX 3060 12G''',
        'description': '''Skjermkort som fungerer meget bra…selges p.g.a oppgradering av PC.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=369463637'
    },
    '369822861': {
        'heading': '''RTX 2060 gaming setup, 144hz monitor''',
        'description': '''PCSpecifications:Motherboard: MSI B450 tomahawk maxCPU: Ryzen 3600 (stock cooler)GPU: gigabyte Rtx 2060Memory: Corsair ddr4 16gb (8gbx2) 3200mhzPsu: bronze cx550m (modular)Storage: 250gb SSD (not mvme), 1tb hard driveCase brand: sharkoonOthers: high quality pci  wifi cardBluetooth USB extensionMonitorAOC 144hz freesync 1920x1080Mechanical keyboard included (blue switches)-no mouse includedPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=369822861'
    },
    '369971200': {
        'heading': '''6900xt''',
        'description': '''Vurderer salg av 6900xt 16GB ram.Kortet gjør det bedre en 3090 (selv testet det selv da en kompis har 3090)Vurderer å selge da jeg bygger en hvit pc, så trenger hvit GPU!Kan være interessert i 7800XTKommer mer bilder fortløpende!Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=369971200'
    },
    '370138656': {
        'heading': '''Asus ROG-STRIX-RX580-T8G-GAMING''',
        'description': '''Pent brukt skjermkort selges da jeg har kjøpt ny pc. Er pent brukt og har alldri vært noe problem med det.Tok utgangspunkt i priser jeg fant på ebay. Har original esken det kom i hvis det hjelper noe.Kom gjerne med bud.Kan sendes.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=370138656'
    },
    '370352732': {
        'heading': '''GeForce RTX™ 3070 VENTUS 3X OC # PRIS KAN DISKUTERES #''',
        'description': '''LES  OPRISEN SOM ER SATT ER PGA EN MÅTTE SETTE INN EN PRIS!KOSTER 9399.- Hos POWER!# PRIS KAN DISKUTERES #GeForce RTX™ 3070 VENTUS 3X OC selges pga oppgraderingerMSI GeForce RTX™ 3070 VENTUS 3X OC er et grafikkort som benytter NVIDIAs Ampere-arkitektur og har 8 GB GDDR6-minne. Grafikkortet er fullspekket med den nyeste teknologien, for eksempel strålesporing og DLSS AI-akselerasjon, og tar grafikkytelsen til et helt nytt nivå.Nyt den nye generasjonen innen grafikkytelseNVIDIAs RTX 30-serie med Ampere-arkitektur tilbyr fantastisk grafikkytelse for både kreativt arbeid og gaming. GeForce RTX™ 3070 VENTUS 3X OC har forbedrede RT- og Tensor-kjerner, 5888 CUDA-kjerner og 8 GB superraskt GDDR6-minne med 256-bit minnebuss.Ytelse kommer førstGrafikkort i VENTUS-serien er designet med ytelse i høysetet. Trippel viftestruktur med solid industriell design gir grafikkortet et flott utseende. En lett bakplate i grafen går langs hele grafikkortet og gir bedre varmeledning.Toppmoderne termisk designGrafikkortet er utstyrt med prisvinnende TORX 3.0-vifter hvor bladene går i alternerende retninger for mer fokusert luftstrøm inn i kjøleribben. Kjølesystemet Zero Frozr stopper viftene helt når temperaturen blir lav og eliminerer støy når det ikke er behov for aktiv kjøling. Presise Core Pipes sprer varmen langs hele kjøleribben for optimal kjøling.Ampere-arkitekturNVIDIAs Ampere-arkitektur med nye RT-kjerner, Tensor-kjerner og multiprosessorer for strømming leverer superrealistisk grafikk med strålesporing og banebrytende AI-funksjoner. Ampere-arkitekturen er et enormt skritt framover sammenlignet med sine forgjengere.Utrolig bildefrekvens og strålesporingDLSS (Deep Learning Super Sampling) er NVIDIAs AI-baserte gjengivelsesteknikk som akselererer bildefrekvenser opptil 1,5x uten å gå på akkord med bildekvaliteten. Akselerasjonen utføres av de dedikerte Tensor Core AI-prosessorene på GeForce RTX-grafikkort. Strålesporing simulerer lysets fysiske oppførsel, som gir gjengivelse av kinokvalitet i selv de mest visuelt intense spillene.NVIDIA ReflexGrafikkprosessorer i GeForce RTX 30-serien og NVIDIA G-Sync skjermer gir deg konkurransefortrinn med den laveste latens og den beste responstiden. Den revolusjonerende teknologien gjør at du sikter deg inn raskere, reagerer raskere og får bedre presisjon.Slipp kreativiteten løsAI-akselerasjonen du får med GeForce RTX 30 er til stor hjelp i kreative prosjekter. RTX 30-serien er bygget for å levere på rekordtid og gir deg ytelsen du trenger til ditt beste arbeid, enten det er komplekse 3D-scener, 8K videoredigering eller høykvalitets livestrømming.SpesifikasjonerProdusentMSILeverandørens IDGeForce RTX 3070 VENTUS 3X OCArtikkel ID1147092EAN4719072763084VarenummerMSI3070V3XOCVekt og dimensjonerNettomål uten emballasje (D x B x H)305 x 121 x 52 mmBruttomål med emballasje (D x B x H)402 x 257 x 84 mmNettovekt990 gBruttovekt1.58 kgGrafikkegenskaperGrafikkort MerkeNVIDIAGrafikkarkitekturAmpereGrafikkprosessor (familie)NVIDIA GeForce RTXGrafikkprosessor (modell)GeForce RTX 3070Minnekapasitet8 GBMinnetype for grafikkGDDR6Minnehastighet14000 MHzTekniske egenskaperBoost klokkehastighet1755 MHzAnbefalt systemkraft650 WGPU effekt220 WLHR (Lite Hash Rate)NeiGPU egenskaperMax. digital oppløsning7680X4320CUDA-kjerner5888 stykkG-SYNC-kompatibelJaAntall støttede skjermer4 stykkInformasjon hentet ifra power sin sidehttps://www.power.no/data-og-tilbehoer/datakomponenter/grafikkort/msi-geforce-rtx-3070-8-gb-ventus-3x-oc-grafikkort/p-1147092/#specsInformasjon hentet fra produsentens hjemmesidehttps://www.msi.com/Graphics-Card/GeForce-RTX-3070-VENTUS-3X-OC# PRIS KAN DISKUTERES #Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=370352732'
    },
    '370497980': {
        'heading': '''Intel i7-7700, ASUS ROG Strix B250F Gaming, Ballistix 16GB RAM''',
        'description': '''Kanon oppgraderingspakke til en grei pris.Se også mine andre annonser for skjermkort.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=370497980'
    },
    '370581148': {
        'heading': '''Intel i9-10900X Prosessor LGA2066 (Uåpnet)''',
        'description': '''Selger en ny og uåpnet Intel Core i9-10900X prosessor til LGA2066-socket.Ny pris på denne er rundt 10000,-, men selger den nå til 5000,-.Denne prosessoren er en del av Intels X-serie og er kjent for sin høye ytelse, spesielt designet for krevende oppgaver som videoredigering, 3D-rendering og andre ressurskrevende applikasjoner.Ta gjerne kontakt hvis det er noe du lurer på!skjermkort grafikkort pc-deler pc i deler komponenter gpu rtxCpu prosessor pc-deler pc i deler komponenter gpuPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=370581148'
    },
    '370643612': {
        'heading': '''Rtx 3060 Ti 8gb MSI''',
        'description': '''Kan bytes i aner skjermkort også med mellomlegg send gjerne hvilken type :)Har orginal eskePris 3500krÅpen for bud :)Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=370643612'
    },
    '370971848': {
        'heading': '''ASUS GeForce RTX 2080 SUPER DUAL EVO OC V2''',
        'description': '''Specs:Modell DUAL-RTX2080S-O8G-EVO-V2Produktserie ASUSVideoutgangVR-klar JaHDCP-kompatibel JaKlokkehastighetsøkning 1860 MHzMaks ekstern oppløsning 7680 x 4320Grafikkprosessorfabrikant NVIDIAGrensesnittype PCI Express 3.0 x16Maks antall skjermer 4Antall CUDA-kjerner 3072Type GrafikkortGrafikkprosessor NVIDIA GeForce RTX 2080 SUPERStøttede API OpenGL 4.6Støttet videosignal DisplayPort, HDMIVideoadapterfunksjoner Klar for NVIDIA G-Sync, MaxContact technology, AUTO-EXTREME-teknologi, 0dB Technology, NVIDIA Turing GPU-arkitektur, Axial-tech Fan Design, 2,7-spors Fan Cooler, NVIDIA NVLink-teknologi, GPU Tweak IIUtgangsporter (kompakt liste) 3 x DisplayPort, HDMIVideominneBussbredde 256-bitInstallert størrelse 8 GBTeknologi GDDR6 SDRAMKlokkefrekvens minne 15500 MHzSystemkravPåkrevd strømforsyning 650 WEkstrakrav 2 x 8 pin PCI Express-strømkontaktDiverseFargekategori SvartTilpassede standarder DisplayPort 1.4, HDCP 2.2Størrelser og vektDybde 26.7 cmBredde 5.8 cmHøyde 11.8 cmGrensesnittdetaljer HDMI, 3 x DisplayPortPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=370971848'
    },
    '371075547': {
        'heading': '''*RESERVERT* IBM Aptiva P233mhz med 3dfx Voodoo 1''',
        'description': '''Veldig fin IBM Aptiva 2137 selges.Maskinen er fra 1997 og fungerer utmerket. Den er oppgradert og bygget for spill fra Win95 og tidlig Win98 eraen. Med tidsriktig 3dfx Voodoo akselerator kan du kjøre Glide kompatible spill som f.eks Quake og Need for Speed SE med 3d rendering som gir en helt annen og bedre spillopplevelse i motsetning til standard software rendering i spill. Et integrert ATI Rage II+ skjermkort med 2MB håndterer 2D-akselerasjon, som brukes til skrivebordsapplikasjoner og 2d spill.Lydkortet er et Crystal 4237 som er soundblaster kompatibelt og fungerer veldig bra til DOS- og Win95 spill.USB-støtte: USB-driver for Windows 95 installert, slik at man kan bruke en minnepenn for enkel dataoverføring.Det følger også med en 19” Iiyama Prolite 4:3 lcd skjerm som har praktisk oppsett for justering av posisjon og lysstyrke/kontrast og innebygd høyttaler.PC-en leveres med Windows 95 Plus! og alle drivere ferdig installert, samt diverse spill, programmer (som Office 97, 7zip, osv.) og all nødvendig dokumentasjon om maskinvaren.Alt er nøye rengjort, og kjølepastaen er skiftet.Komplett info om miroHISCORE Voodoo kort finnes her: https://thandor.net/object/111Spesifikasjonene er som følger:OS: Windows 95 Plus!Grafikk: Ati Rage II + 2MB og miroHISCORE 3DFX Voodoo 6 MBProsessor: Intel Pentium 233Mhz MMXRam: 64MB sdramLagring: Seagate ST32122A HDD, 2GBLydkort: Crystal 4237 (soundblaster kompatibelt)3.5\" 1.44MB floppy diskNec 16X IDE DVD-RWAtapi 20X CD-Rom - ikke tilkoblet da den er defekt.Andre tilkoblinger: Gameport, COM, LPT, VGA ut samt 2 x USBJeg har dessverre ikke vga gjennomgangskabelen som hører til Voodoo-kortet, men man kan bruke en VGA-switch eller bare bytte VGA-kabelen fra ATI til Voodoo-kortet etter at 3Dfx spillet er startet.Søkeord: IBM, Pentium, 586, 486, 386, 286, retro gaming, w95, Windows 95, w98, Windows 98, MS-DOS, DOS, 3dfx, VoodooPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=371075547'
    },
    '371546209': {
        'heading': '''Msi Nightblade MI3''',
        'description': '''Grei inngangs gaming pcBrukt til å spille Fortnite, GTA 5, Hitman 3 ++128 ssd harddisk til operativsystemet1 tb hdd til lagring av spill16 gb ramGeForce GTX 1060 3gb skjermkortMulighet til å koble til ekstra ssd harddisk på toppSender ikkePluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=371546209'
    },
    '372209649': {
        'heading': '''RTX 2060 12GB''',
        'description': '''Skjermkort som jobber godt.ASUS Dual GeForce RTX2060 12GB EVO OC12GB kan passe fint til mindre AI prosjekt som tale f.eks.Kjøpt 09.03.2022 - 3 år garantiKvittering medfølger.Kjøper betaler frakt. Kan prøve å levere i Stavanger.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=372209649'
    },
    '372349051': {
        'heading': '''Nvidia Quadro 6000''',
        'description': '''Pent brukt.Original HP reservedelHP Assy No: 612953-001HP Spare No: 616078-001Spesifikasjoner:HPE NVIDIA Quadro 6000 PCIe 6GB. Graphics processor family: NVIDIA, Graphics processor: Quadro 6000. Discrete graphics card memory: 6 GB, Graphics card memory type: GDDR5, Memory bus: 384 bit. Maximum resolution: 2560 x 1600 pixels. DirectX version: 11, OpenGL version: 4.4, Dual Link DVI. Interface type: PCI Express 2.0. Cooling type: ActiveNVIDIA Quadro 6000 PCIe graphics card - With 6.0GB GDDR5 GPU memory, max resolution 2560 x 1600, max power consumption 204 Watts, one Dual Link DVI-I and two DisplayPorts connectionsPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=372349051'
    },
    '372724808': {
        'heading': '''Asus 27\" 4K gamingskjerm ROG Strix XG27UQ''',
        'description': '''• 27-tommers 4K IPS-gamingskjerm med oppdateringsfrekvens på 144 Hz for ekstremt jevn gaminggrafikk• Støtter Display Stream Compression-teknologi for å transportere UHD-videostrømmer over et enkelt grensesnitt med høy hastighet uten merkbart tap av bildekvalitet.• HDR-teknologi (High Dynamic Range) med DisplayHDR™ 400-sertifisering og profesjonelt 90% DCI-P3-fargespekter sikrer enestående kontrast og fargegjengivelse• Adaptive Sync gir en sømløs spillopplevelse uten skjermriving (G-SYNC-kompatibel i programprosess)Verdens første 27\" DSC-gamingskjermFANTASTISKE FARGER. LYNRASK HASTIGHET.ROG Strix XG27UQ er verdens første 27-tommers DSC-gamingskjerm med DSC-teknologi (Display Stream Compression) som leverer jevne 4K-bilder på opptil 144 Hz. Den er G-SYNC-kompatibel og DisplayHDR™ 400-sertifisert, med eksepsjonell kontrast og 90 % dekning av DCI-P3-fargeområdet.SUVEREN BILDEKVALITET MED DSC-TEKNOLOGIDisplay Stream Compression-teknologi er en industriomfattende komprimeringsstandard for overføring av videostrømmer i ultrahøy kvalitet gjennom en enkel grensesnitt i høy hastighet uten merkbart tap av visuell kvalitet. Med DSC-teknologi, kan ROG Strix XG27UQ vise utrolige detaljerte og myke bilder på naturlig 4K-oppløsning med en 144 Hz oppdateringsfrekvens via en enkel DisplayPort 1.4-tilkoblingn uten chroma subsampling som kan påvirke negativt visuell gjengivelse.*For å aktivere 4K-oppløsning på 144 Hz med DSC kreves et skjermkort i NVIDIA® GeForce® RTX 20 Series, AMD Radeon™ RX 5700 eller høyere. Kontakt skjermkortprodusenten hvis du vil ha mer informasjon om aktivering av DSC.RASK OPPDATERINGSFREKVENS PÅ 144 HZ OG RESPONSTID PÅ (MPRT) 1 MSROG Strix XG27UQ tilbyr en superrask oppdateringsfrekvens på 144 Hz og en responstid (MPRT) på 1 ms, slik at selv de raskeste spillene som spilles på de høyeste bildeinnstillingene forblir silkemyke og helt uten forsinkelser.NVIDIA G-SYNC-KOMPATIBELMed Adaptive Sync (G-SYNC-kompatibel) leverer ROG Strix XG27UQ en sømløs spillopplevelse uten skjermriving ved å aktivere VRR som standard på skjermkort i NVIDIA GeForce GTX 10 Series og NVIDIA GeForce RTX 20 Series.*G-SYNC-kompatibel i programprosessBREDT FARGEOMRÅDE OG HØY KONTRAST, UTVIDET DYNAMISK REKKEVIDDE (HDR) MED DCI-P3 90 % OG DISPLAYHDR™ 400ROG Strix XG27UQ støtter HDR-teknologi på forskjellige grader av lystetthet (opptil 400 cd/m2) for å levere et bredere fargeområde og høyere kontrast enn vanlige skjermer. De lyseste hvittonene og de mørkeste svarttonene bringer frem detaljer som aldri før. ROG Strix XG27UQ leverer også 90 % dekning av DCI-P3-fargeområdet og kontrastytelse som oppfyller DisplayHDR™ 400-sertifisering. For å sikre fargenøyaktighet er hver ROG Strix XG27UQ fabrikkalibrert.FLERE HDR-MODUSERNå kan du velge mellom flere HDR-moduser for å justere skjermens HDR-ytelse basert på ditt nåværende scenario.SHADOW BOOST-TEKNOLOGIShadow Boost-teknologi gjør mørke områder i spillet klarere uten å overeksponere lysere områder, noe som forbedrer den generelle visningen og samtidig gjør det enklere å få øye på fiender som skjuler seg i mørke områder på kartet.ASUS DISPLAYWIDGET-PROGRAMVAREDisplayWidget er et intuitivt programvareverktøy som lar brukerne finjustere skjerminnstillingene. Justeringer av disse verktøyene kan gjøres via skjermmenyen (OSD) eller navigasjonsspaken, men ASUS DisplayWidget gjør det lettere å få tilgang til og bruke disse forskjellige innstillingene.APP SYNC™AppSync lar deg tilordne spesifikke ASUS GameVisual-moduser til individuelle applikasjoner og spill for å sikre at programmet du bruker, er i ønsket modus. Du har også muligheten til å endre disse tilordnede innstillingene raskt.PARAMETER FOR DELBARE SKJERMINNSTILLINGERAlle tilpassede GameVisual-innstillinger kan lagres i et AXML-filformat som kan deles med andre brukere av samme skjermtype.MULTIFRAMEMultiFrame lar brukere organisere flere vinduer på skrivebordet og ordne dem på en slik måte at de ikke overlapper med hverandre på en stor skjerm.HURTIGTASTERHurtigtaster lar brukere raskt endre innstillingene ved å trykke på en bestemt tastekombinasjon.ULTRA-LOW BLUE LIGHT-TEKNOLOGIROG Strix XG27UQ har TÜV Rheinland-sertifiserte ASUS Ultra-low Blue Light-filtre for å beskytte øynene og forhindre belastninger fra skadelig blått lys. Velg mellom fire forskjellige filterinnstillinger via skjermmenyen eller ved å bruke den femveis joysticken.FLICKER-FREE-TEKNOLOGIROG Strix XG27UQ reduserer flimring på skjermen for å gir deg en mer komfortabel spillopplevelse. Dette minimerer belastningen på øynene under maraton-spilløkter.ROBUSTE TILKOBLINGSMULIGHETERROG Strix XG27UQ tilbyr et bredt utvalg av tilkoblingsalternativer, inkludert to HDMI 2.0-innganger og to DisplayPort 1.4-grensesnitt.ERGONOMISK DESIGNROG Swift XG27UQ er spesialdesignet for maratonspilling. Den har et ergonomisk utformet fot med høyde, rotasjon, dreining og vinkeljustering slik at du alltid kan finne den ideelle posisjonen enten du sitter i sofaen eller i sengen.ASUS AURA SYNC-BELYSNINGMed den eksklusive belysningsteknologien ASUS Aura Sync sørger ROG Strix XG27UQ for omgivelsesbelysning som kan synkroniseres med andre Aura-aktiverte komponenter og periferiutstyr.https://www.komplett.no/product/1153176?noredirect=true#Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=372724808'
    },
    '372856549': {
        'heading': '''Nvidia Geforce RTX 3070 Ti Founders Edition''',
        'description': '''Selger skjermkort Nvidia Geforce RTX Founders Edition 8GB GDDR6X PCI Express 4.0 pga oppgradering.Fungerer helt fintMedfølger med original boks.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=372856549'
    },
    '373026502': {
        'heading': '''Full gaming pakke (Komplett premium i120++)''',
        'description': '''Selger komplett gaming pakke. Inkluderer komplett premium i120 gaming pc (specs nedenfor), AOC G2460PQU monitor, Logitech G Pro wireless gaming mus, Logitech G Pro X headset, Razer Kiyo X kamera, logitech G413 carbon keyboardNZXT H510 SortVifter: 1x 120mm top, 1x 120mm bak, ATX, mITX, mATX, Tempered GlassASUS GeForce GTX 1660 SUPER ROG StrixSkjermkort, PCI-Express 3.0, 6GB GDDR6, TuringIntel Core i5-9400F ProsessorSocket-LGA1151, 6-Core, 6-Thread, 2.90Hz, uten grafikk, uten kjølerCM Hyper H411R RGB Black EditionLGA115x, 92mm fan with RGB, Aura Sync/Mystic Light, PWM, Komplett LogoCorsair Vengeance LPX DDR4 2666MHz 16GB2x8GB, DDR4, 2666MHz, CL16, XMP 2.0, SortKingston A2000 500GB NVMe M.2 SSDM.2 2280, PCIe 3.0 x4, NVMe, 3D NAND, up to 2200/2000MB/s, 350TBWASUS TUF B360-PRO GAMING, Socket-1151Hovedkort, ATX, B360, DDR4, 2xPCIe-x16, M.2, CFXCorsair TX550M, 550W PSUATX 12V v2-4, 80 PLUS Gold, Semi Modular, 6+2-pin PCIeWindows 10 HomePluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/373026502'
    },
    '373201615': {
        'heading': '''RTX geforce 3070 gpu! Salg!!''',
        'description': '''Salg på 3070 rtx skjermkort!Kun seriøse henvendelser blir besvart!Pris 4000!Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=373201615'
    },
    '373202118': {
        'heading': '''Gainward Salg på 3070 rtx skjermkort! Salg!''',
        'description': '''Salg på 3070 rtx skjermkort!Kun seriøse henvendelser blir besvart!Pris 4000!Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=373202118'
    },
    '373537465': {
        'heading': '''Dell 9020 pakke med Windows 11 Pro, 16GB RAM og 256GB SSD''',
        'description': '''Her får du en svært god komplett løsning for kontorbruk med alt du trenger for å komme i gang. Pakken består av utstyr fra merkevareprodusent:- Dell OptiPlex 9020 (SFF kabinett) med Windows 11 Pro (64-bit)- CPU: Intel Core i5-4590 (3.3 GHz)- Optisk stasjon HL-DT-ST CD / DVD +/- R / RW- Lagring: SSD drive 256 GB- RAM: 16GB- GPU: Intel HD Graphics 4600- 10x External USB 2.0 porter (4 stk. i front)- 1x VGA videoutgang- 2x DisplayPort videoutganger- 1x Serial port- 1x PS / 2 tastatur port- 1x PS / 2 museport- 1x Ethernet, Fast Ethernet, Gigabit Ethernet port- 2x Line-out (headphone/speaker)- 2x Line-in (stereo/microphone)- H x B x D (cm): 31.0 x 29 x 9.5- Vekt: ca. 6kgSkjerm: DELL Ultra Sharp U2412H  24\" 1920 x 1080px (med original DELL stereo høyttaler)- Brightness: 250 cd/m²- Contrast Ratio: 1000:1 / 10000:1 (dynamisk)- Color Support: 24-bit (16.7 millionner farger)- Tastatur og mus fra DellPakken leveres med: Strømkabler, DisplayPort kabel, USB kabel (fra PC til USB-hub tilkobling), Dell tastatur og mus. Klar til bruk.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=373537465'
    },
    '373740208': {
        'heading': '''Hovedkort, CPU og Skjermkort selges''',
        'description': '''Hovedkort: Msi Z87-GD65Skjermkort: Gtx 970Prosessor: Intel i7 4700kKabinett og intern dvd spiller kan følge med gratisPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=373740208'
    },
    '373923203': {
        'heading': '''MSI GE66 Raider Gaming Laptop''',
        'description': '''MSI GE66 Valhalla Limited Edition gaming laptop selges da den ikke er i bruk lenger.Blitt brukt mest til film osv. Så er veldig pent brukt.- RTX 2070 GPU- i7-10875H CPU- 240hz SkjermSend gjerne mld ang spørsmål :)Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=373923203'
    },
    '374042153': {
        'heading': '''MSI gtx 1070 8gb''',
        'description': '''Fint brukt skjermkort. Nylig renset og hatt på ny kjølepastaChipset: NVIDIA GeForce GTX 1070Video Memory: 8GB GDDR5 and card dimension(mm)-6-pin x 1, 8-pin x 1Memory Clock: 8108 MHz (oc mode) ; Memory 8GB GDDR5 (256-bit) , Interface: PCI Express x16 3.0. DirectX Version Support - 12, OpenGL Version Support- 4.5, Multi-GPU Technology - SLI, 2-WayMax. Resolution: 7680 x 4320, support 4x Display monitorsPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=374042153'
    },
    '374109514': {
        'heading': '''GamingPoint CHARGER RGB''',
        'description': '''BeskrivelseDenne gaming-PC-en med RGB, en Intel i5-prosessor, og et 6 GB skjermkort vil gi deg god ytelse i mange moderne spill. Her er en kort oversikt over hva du kan forvente:Ytelse og spillopplevelse:Spill som f.eks Fortnite, Rocket League, Apex Legends, Forza Horizon, Minecraft, GTA og FIFA vil alle kjøre godt på denne PC-en, spesielt i 1080p oppløsning.Prosessor: En Intel i5, som gir god ytelse i spill, multitasking og andre daglige oppgaver.Denne maskinen er godt balansert for gaming, spesielt hvis du spiller i 1080p-oppløsning. De fleste av de nevnte spillene vil kjøre flytende med gode grafikkinnstillinger, så dette er et godt valg for en midrange-gamer som ønsker kraft og stil.Ytterligere spesifikasjoner:Prosessor: Intel i5-4670K - 3.8 GHz, 4 kjerner og 4 tråderCPU-kjøler: RGB-opplyst cpu kjølerRAM: Ballistix Sport 16GB ramSkjermkort: ASUS GTX 1060 - 6GB (Yter opptil 60% bedre enn f.eks Gtx 1050ti 4gb)Lagring:Ssd på 240gb som gir rask oppstart av Windows, programmer og spill + 1000gb hdd for ekstra lagringOperativsystem: Windows 11Egenskaper:Design: Lekkert kabinett med sidevindu i glass, og RGB lysTilbehør: Adapter for tilkobling til trådløst nett og Bluetooth enheter som f.eks headsett eller kontroller (Verdi 329kr)Leveres med følgende:1 års garantiStrømkabelGratis fraktKan også hentes på vårt kontor i Sandefjord etter avtale.Betal med Vipps eller del opp betalingen med Klarna.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/webstore/ad.html?finnkode=374109514'
    },
    '374156380': {
        'heading': '''ASUS ROG Strix B550-E GAMING Hovedkort''',
        'description': '''Selger et ASUS ROG Strix B550-E GAMING hovedkort. Det har kun vært brukt i en PC, er i utmerket tilstand og fungerer perfekt. Dette er et solid hovedkort for gaming og arbeidsstasjoner. Original boks følger med.• Socket: AM4, passer til AMD Ryzen 3.-generasjons prosessorer.• Minne: 4 spor for DDR4-minne, støtter opptil 128 GB.• Lagring: To M.2-spor (ett med PCIe 4.0 x4 og ett med PCIe 3.0 x4) og seks SATA III-porter.• Nettverk: 2.5Gb Ethernet fra Intel, innebygd WiFi 6 (802.11ax) og Bluetooth 5.1.• Utvidelsesplasser: To PCIe 4.0 x16 spor for flere grafikkort.• Tilkoblinger: Flere USB 3.2 Gen 2-porter (inkludert Type-C), HDMI og DisplayPort.• RGB: AURA Sync for tilpasset belysning.Dette hovedkortet er solid bygd og har god kjøling med flere kjøleribber som holder temperaturen lav, selv under belastning. Har også et brukervennlig BIOS-system som lar deg justere ytelsen enkelt. Kan også sendes utenom fiks ferdig for 135kr.Søkeord:ASUS, ROG, Strix, B550-E, GAMING, hovedkort, motherboard, PC, gaming, WiFi 6, DDR4, M.2, PCIe, USB, RGB, AURA Sync, kvalitet, quality, ytelse, performance, minne, memory, lagring, storage, gaming PC, komponenter, grafikkort, GPU, skjermkort, graphic card, AM4, AMD, prosessor, CPU, HDMI, DisplayPort, RAM, chipset.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=374156380'
    },
    '374199803': {
        'heading': '''Dell Tower 7910 + Lenovo D32\"''',
        'description': '''Dell Tower 7910:* CPU Processor: Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz 2.30 GHz (2 processors)* Installed RAM: 64 GB DDR4* HDD: 1TB* GPU: NVIDIA Quardi M5000 8GBMonitor: lenovo D32q-20Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/374199803'
    },
    '374352532': {
        'heading': '''RTX 2080 ti''',
        'description': '''Hei, vil selge min 2080ti pga oppgradering til 4090. Skjermkort funker veldig bra og har lignende ytelse som rtx 4060 ti. Fastpris 3250kr. Kan hentes i Kristiansand område.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/374352532'
    },
    '374393869': {
        'heading': '''HP EliteDesk 800 G3 Mini 65W med Windows 11 Pro, 16GB RAM, 256GB SSD''',
        'description': '''Spesifikasjoner for HP EliteDesk 800 G3 Mini 65W:- Operativsystem: Windows 11 Pro (24H2 versjon)- Formfaktor: Ultrakompakt (B x D x H: 17.5 x 17.7 x 3.4 cm)- Prosessor: Intel(R) Core(TM) i5-7500 (3.40 GHz / 4 kjerner)- Up to 3.80 GHz maximum Turbo Frequency- RAM: 16GB- Lagring: 256GB SSD- GPU: Intel(R) HD Graphics 630 (1 GB)- Innebygde enheter: Høyttaler- Trusted Platform Module (TPM 2.0) Security Chip- Supports Intel vPro Technology and Intel Stable Image Platform Program (SIPP)- USB 3.1 Gen 1: (2) front (including 1 fast charging); (4) rear- USB Type-C 3.1 Gen1, front- Ethernet LAN (RJ-45)-port: Ethernet, Fast Ethernet, Gigabit Ethernet- Antall Videoutganger VGA: 1- Antall Videoutganger DisplayPort: 2- Maks. antall skjermer som støttes: 3- 1 x hodetelefon (1 foran)- 1 x hodetelefon/mikrofon (1 foran)- Formfaktor: Ultrakompakt (B x D x H: 17.5 x 17.7 x 3.4 cm)For med info: https://support.hp.com/ro-en/document/c05371240Leveres med original HP strømadapter. Klar til bruk.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/374393869'
    },
    '374460089': {
        'heading': '''Nvidia Quadro RTX 5000 16Gb GPU''',
        'description': '''Tatt ut av fungerende pc pga endrete behov, i veldig fin stand !Kan sendes etter avtale med kjøperPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/374460089'
    },
    '374622137': {
        'heading': '''(Vurderes solgt!) HP Pavilion TG01 R5-5''',
        'description': '''Vurderer å selge min HP Pavilion-Gaming PcInfo om Gaming beistet:HDMIVia HDMI-utgangen på grafikkortet kan det kobles til en HD-TV eller projektor for å vise bilder og videoer i opptil 4K UHD-oppløsning på en stor skjerm.LagringMed rask 512 GB SSD-lagring vil oppstarts- og lastetider være raske, slik at du kan bruke mer tid på spilling og mindre tid på venting.AMD Ryzen™-prosessorAMD Ryzen™ 5 5600G APU-en samler ytelsen fra CPU-en og GPU-en i én kompetent brikke. Den har en basishastighet på 3,9 GHz med muligheten til å øke til 4,4 GHz – alt sammen ved bruk av seks kjerner. Den støttes av 16 GB DDR4 RAM.Strålesporende grafikkNeste generasjons Ampere-arkitektur leverer en økt mengde dedikerte strålesporende kjerner, Tensor Core AI-drevet rendering og forbedret CUDA-ytelse. Dette sikrer at Nvidia GeForce RTX 3060 er her for å skyve grensene for grafikk i videospill. Opplev livaktige bilder og høy bildefrekvens i superskarp 4K 2160p-oppløsning samtidig som driftstemperaturen holdes nede.Tilkobling:- 3 stk. DisplayPort 1.4, 1 stk. HDMI- 1 stk. USB-C 3.2 Gen 1-port- 2 stk. USB-A 3.2 Gen 1-porter- 2 stk. USB-A 3.2 Gen2-porter- 4 stk. USB-A 2.0-porter- Lynrask dual band WiFi-ac, Bluetooth 5.0, Gigabit LAN-port- 1 stk. line-in, 1 stk. line-out, 1 stk. mikrofon-port- 1 stk. 3,5 mm kombinert jack til hodetelefoner/mikrofonAndre egenskaper:- Windows 11- 5.1 surroundlyd- 400 W strømforsyningSpesifikasjoner (Kort Info)AMD Ryzen™ 5 5600G-prosessorNVIDIA GeForce RTX 3060-grafikk16 GB DDR4 RAM, 512 GB SSDPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/374622137'
    },
    '374780709': {
        'heading': '''GIGABYTE GeForce RTX 3070 AORUS MASTER 8GB GRAFIKKORT''',
        'description': '''GIGABYTE GeForce RTX 3070 AORUS MASTER 8GB i topp stand selges.Heftig grafikkort med: NVIDIA Ampere Streaming Multiprocessors, 2nd Generation RT Cores, 3rd Generation Tensor Cores, Powered by GeForce RTX™ 3070, Integrated with 8GB GDDR6 256-bit memory interface, MAX-COVERED cooling, LCD Edge View, RGB Fusion 2.0, 6 video outputs, Protection metal back plate.Modellbetegnelse:  GV-N3070AORUS M-8GDKjøpt 2021. Har kvitteringSe her for mer info:https://www.gigabyte.com/Graphics-Card/GV-N3070AORUS-M-8GD-rev-10-11#kfKjøpte dette for en liten tid tilbake her på Finn.no, men har for svak prosessor, så det ble ingen god match. Selger det derfor videre.Det tas forbehold om feil i annonsen.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/374780709'
    },
    '374788058': {
        'heading': '''Geforce RTX 2070 Super''',
        'description': '''Palit Geforce RTX 2070 Super 8GBSelges pga overgang til nyere skjermkort.Fremstår som pent brukt med kvittering og orginal emballasje.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/374788058'
    },
    '374896144': {
        'heading': '''ASUS GeForce RTX 2080 SUPER ROG STRIX OC - 8GB''',
        'description': '''Strøkent skjermkort som er perfekt for 1440p.Nylig renset og fått ny kjølepasta, så temperaturene er som ny.Sendes godt pakket inn i skumplast og antistatisk pose, eller hentes i Oslo.Specs:Busstype: PCI Express 3.0 x16Grafikkprogram: NVIDIA GeForce RTX 2080 SUPERMinne: 8 GB GDDR6Kjerneklokke: 1680 MHzBoost Clock: 1890 MHzCUDA-kjerner: 3072Grensesnitt: 2 x DisplayPort, USB-C, 2 x HDMIDimensjoner (BxDxH): 5.41 cm x 29.97 cm x 13.04 cmFull specs: https://www.proshop.no/Grafikkort/ASUS-GeForce-RTX-2080-SUPER-OC-8GB-GDDR6-RAM-Grafikkort/2788848Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/374896144'
    },
    '374978883': {
        'heading': '''BELKIN Thunderbolt 3 Dock Plus''',
        'description': '''Selger en Belkin Thunderbolt 3 Dock Plus. Fungerer prikkfritt.Original Thunderbolt 3 Gen 2 kabel medfølger ikke, men USB-C til USC-C medfølger.For alle de som bruker PC vil dette fungere slik det skal, men for mac-brukere kan det å bruke en Thunderbolt 3 Gen 2 kabel gi noen flere funksjoner og hastighetsøkning. Imidlertid vil USB-C-kabelen også fungere for mac-brukere da Thunderbolt og USB-C er kompatible med hverandre.Med denne docken kan du koble til masse eksterne enheter – skjermer, mus, tastaturer, høyttalere, nettverk, harddisker og mer – til den bærbare datamaskinen via en enkelt USB-C kabel.Du trenger ikke bruke laptopens strømforsyning siden docken lader pcen din mens du bruker den (60W).Du kan koble til to skjermer via Display portene. Hvilken oppløsning du kan oppnå er fullstendig avhengig av hvor heftig skjermkort du har i maskinen du skal koble til.Dette må du selv sjekke på forhånd.Her er link til Belkins nettside med mer info om produktet:https://www.belkin.com/p/thunderbolt-3-dock-plus/P-F4U109.htmlHar ikke lenger original emballasje. Kjøper betaler fraktPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/374978883'
    },
    '375123025': {
        'heading': '''Acer Nitro N50-600 Gaming''',
        'description': '''Acer Nitro N50-600 Gaming pcProsessor:  i5-8400 6-core 2.8 GHz8 GB  RAMLagring :256 GB SSDSkjermkort :GeForce GTX 1050 TiWindows 11Fastpris , kan sendes mot 125 kr frakt eller Fiks ferdigPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/375123025'
    },
    '375144232': {
        'heading': '''selger datamaskin for deler''',
        'description': '''Datamaskinens skjermkort fungerer ikke ellers slår maskinen seg på og alt fungererSkjermkort: Geforce gtx 580Hovedkort: Asus sabertooth 990fxInternminne/RAM: corsair xms3 3x6(18gb)Prosessor: intelcore i7 960Strømforsyning: corsair tx850 (840watt)væskekjøling: Antec Kuhler H2O 620Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/375144232'
    },
    '375206544': {
        'heading': '''GTX 1080 fra Asus Rog Strix - Perfekt for gamingriggen''',
        'description': '''Skal du oppgradere gamingriggen eller bygge en helt ny?Sliter du med FPS eller overoppheting?Look no further!Asus Rog Strix GTX 1080 (8gb) er det perfekte grafikkkortet for de som ønsker valuta for pengene.Kjør de nyeste AAA-spillene uten problemer. Stillegående og god kjøling med 3 vifter.Dette er et stort skjermkort som vil se dominerende ut i din rigg, uavhengig av størrelse på kabinettet.Selges da jeg ikke bruker PC-en min lenger, og syns noen som har behov for et såpass skjermkort skal få muligheten.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/375206544'
    },
    '375258842': {
        'heading': '''Gaming oppsett''',
        'description': '''Selger mitt gamle PC-oppsett grunnet oppgradering.PC-en håndterer de fleste nye spill uten problemer og jeg har vært veldig fornøyd med ytelsen.* Maskinvare:CPU: AMD Ryzen 3 1200GPU: NVIDIA GeForce GTX 1060 3GBRAM: 16 GBSSD: Corsair Force 3 120 GBHDD: Seagate Barracuda 1 TBMotherboard: B350 TOMAHAWKPSU: Corsair VS550* PC-en har fått ny kjølepasta i skrivende stund, og resten av kjølepastaen kommer med. Kjølepastaen er av merket Corsair XTM50.*PC-en har totalt blitt brukt i 6 år, har likevel ikke opplevd noen problemer med dette, og den har blitt godt behandlet. Den opererer bedre enn forventet på benchmark.* Power-knappen på forsiden funker ikke, istedenfor er det installert en power-knapp på baksiden av PC-en.* Det er rom for overclocking, men jeg har selv aldri prøvd dette.* Da jeg har glemt koden til windows lisensen, er det inkludert en USB stick med passord til en vedlagt windows-aktiveringsfil. Den fornyer windows på samme måte, så det har ikke vært et problem:)* I tillegg til PC-en er det inkludert:Monitor: AOC G2460PFTastatur og mus: Cooler Master Masterkeys Lite LMusematte: Arachnid ATRAXUSB stick: usikker på modell og lagringsplass1 strømkabelDisplayport kabelOppsettet kan hentes i kristiansand. Kan også fraktes via fiks ferdig.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/375258842'
    },
    '375364761': {
        'heading': '''Kraftig Gaming maskin selges BILLIG!''',
        'description': '''Jeg selger min kraftige gaming maskin grunnet overgang til mini-ITX portabel pakke!Denne er i fantastisk stand! Alt er kjøpt nytt i september 2021! Har derfor mange år igjen!Den spiller alle spill lett 1080p og spiller selv mye 1440p og det kjøres smuud! Gode frames over hele linja!Med RX 6600xt som grafikkort får du hakket bedre ytelse enn RTX 3060. Dette kortet er en perfekt middelklasse kort med utrulig mye kraft for penga! Sammen med Amd cpu får du perfekt pakke for det du vil trenge til en billig penge!Selges for 7800,-Kan være tilbøyelig ved rask avgjørelse!Specsa er:CPU - Ryzen 5 5600XHovedkort - MSI Mag B550 ThomahawkRAM - 16GB DDR4 Corsair Vengeance RGB PRO 3600MHzGPU - Radeon RX 6600XTSSD - 1TB WB Blue SN550 Nvme M.2PSU - Corsair RM650xKabinett - Corsair Carbide 275RJeg blir nok å installere en ny CPU kjøler før jeg selger så du kan oppleve lave gode temperaturer mens du gamer!Gamingpc, gaming Pc, stasjonær gaming, spillemaskin,Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/375364761'
    },
    '237636385': {
        'heading': '''Gtx880m 4gb og kjøleplate for asus g750 serien''',
        'description': '''Har liggende skjermkort og kjøleplate.Gtx880m 4gb skjermkort for asus rog g750 serien.Meningen jeg skulle oppgradere min g750, men fikk ikke brukt dette fordi bærbaren min sluttet å virke før jeg fikk skjermkortet.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=237636385'
    },
    '327871429': {
        'heading': '''skjermkort msi gtx 960 gi bud''',
        'description': '''lite brukthentes i randaberg eller sendes i postPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/327871429'
    },
    '328239638': {
        'heading': '''Skjermkort - Sapphire Pulse RX 580 8GB''',
        'description': '''Selger et Sapphire Pulse RX 580 8GB skjermkort. Ypperlig til FullHD og 1440p spilling og mediabehov. Støtter 4K oppløsning. Kommer i orginalesken. Usikker på om jeg har alle papirmanualer, men det og drivere finner du online. Kortet er rensket godt for støv.Engine Clock: Up to 1366 MHz (Boost)Memory: 8GB GDDR5 8000 MHz Effective2304 Stream ProcessorsDual-X CoolingQuick ConnectSpecs: https://www.sapphiretech.com/en/consumer/pulse-rx-580-8g-g5Hentes på Grønland, Oslo, eller sendes for kjøpers kost.X076Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=328239638'
    },
    '330556392': {
        'heading': '''Dell T3600 Xeon E5-1620  Quatro K4000''',
        'description': '''Selger en Dell Precision T3600 stasjonær PC som kan brukes til det meste. Er i utgangspunktet en fantastisk arbeidsstasjon, men sett i skjermkort og få gaming PC.Xeon er flott hvis man skal ha hjemmeserver, men kan også brukes til enkle spill uten alt for høye krav. Både Fortnite, Roblox og Minecraft kan spilles med medium detaljnivå.Dette er en kvalitets pc som kostet mye for noen år siden.Nyinstallert Windows 10220GB SSD disk16 GB ramK4000 er i utgangspunktet et kort laget for profesjonell 3D design, den har 2 DisplayPort utganger.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/330556392'
    },
    '332007145': {
        'heading': '''Datamaskin''',
        'description': '''Jeg selger min pent brukte gaming-PC grunnet nytt prosjekt. Jeg har fått hjelp av en erfaren PC entusiast til å selge mitt personlige tårn. Jeg har håndplukket solide og brukervennlige deler som sørger en god spill-opplevelse. Den drar moderne, tunge spill. Fortnite, Mordern warfare 2, Battlefield 5, Borderlands 3, Sons of forest og Gta 5 er alle spill man kan kjøre på denne. Personlig har jeg sett til at temperatur har vært lav gjennom livsløpet. Dette gjør at delene har lengre levetid, Alt fungerer som det skal, og jeg har aldri hatt problemer med den. Har hatt denne i rundt 8 år, og må si meg ekstremt fornøyd. Denne PCen vil holde i flere år, og jeg mener det er en flott investering for de som liker å spille. Send gjerne en melding om du har noen spørsmål, og ved rask handel så kan prisen diskuteres:)Specs:CPU: Intel i7-2600RAM: 16gbGpu: Radeon Rx 480Lagring: 1 ssd på 168gb samt em hdd på 700gbPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=332007145'
    },
    '333070541': {
        'heading': '''Nvidia Graffikkort RTX 2060S 8GB!''',
        'description': '''Selges en skjermkort som er Nvidia RTX 2060S turbo 8gb, har ikke brukt den så mye, bare for å spille av og til i kvelder. Jeg har aldri overklokkert den. Hadde ikke problemer med grafikk.. Skjermkort har stått ubrukt kanskje 4/5 måneder 🤷🏻 . Har koblet den igjen til PC og alt fungerer som den skal og uten problemerSånn ser ut PC ilag med Ryzen 3600X som jeg hadde fra før. https://www.youtube.com/watch?v=PC2PRI68ePo&t=835s Veldig bra resultat i high/veryhigh setting når jeg har spilt på den.Kan sendes varen via Post om kjøper betale alle fraktgebyrer.Om mer info tar du kontakt PMPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/333070541'
    },
    '349072622': {
        'heading': '''Skjermkort Gigabyte RTX 3070ti''',
        'description': '''Selger skjermkort Gigabyte RTX 3070ti, selges i orginaleske. Aldri vært overclocked og i bra stand.Ta kontakt ved evt spm.Kan sendes, kjøper betaler frakt.Pris kan diskuteres ved rask avgjørelsePluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=349072622'
    },
    '350424764': {
        'heading': '''Viftefrie skjermkort''',
        'description': '''Selger 2 ubrukte skjermkort type SILENTASUS GEFORCE GT640 Kr1170eller ASUS GEFORCE GTX750 Kr1180Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/350424764'
    },
    '355431993': {
        'heading': '''3060ti skjermkort gpu''',
        'description': '''Fantastisk skjermkort med høy ytelse. Trekker veldig lite strøm. Den har vært i vår kontor PCer. Men er nå byttet ut med 3090 kort. Passer små kabinett. Har to stk kort, tenkte 2500 stk.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/355431993'
    },
    '358981520': {
        'heading': '''Datamaskin sett''',
        'description': '''Datamaskin selges med alt tilbehør!AMD Ryzen 5 2600 - 3.85 GHZ all coreNVIDIA GTX 1070 Ti  8 GB16GB DDR4 RAM 3600MHZKabinett med 3+6 USB og lydutgang.Ekstra komponenter er inkludert i totalprisen:Skjerm Acer E1242QRTastatur Logitech G213 Prodigy Gaming KeyboardMus Logitech G203 LIGHTSYNC Gaming MouseMikrofon Razer Seiren XWifi antenne Asus pce-68 wifi cardDatamaskinkomponentene er ikke nye, etter oppdatering av skjermkortet, prosessoren. Jeg tror det ville være mulig å spille praktisk talt de nyeste spillene. Jeg spilte hovedsakelig CS2, GTA5 onlineAlt selges samlet.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/358981520'
    },
    '360236019': {
        'heading': '''NZXT Gaming datamaskin''',
        'description': '''Selger min NZXT spille data da den aldri ble brukt. Har vert startet en gang siden pakket ned pga. overgang til Gaming laptop.er satt opp med Corsair vengeance  16Gb. ramMSI GeForce GTX 970 Gaming 4GB skjermkort2  stk. 1 tb. Westerndigital  sata disker med 32 gb cache2 stk. Sandisk 128 gb ssd intern disksPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=360236019'
    },
    '361317238': {
        'heading': '''NZXT H510 Alliance Limited Edition''',
        'description': '''Denne varen selges kun med forskuddsbetaling via vipps.Sjekker interessen for kabinettet.Dette er noe en WOW Fan må ha. Det er kun lagd 1000 stk av denne Alliance versjonen i verden.——————————————————World of warcraftNzxt H510 Alliance Limited EditionNummer 0724/1000 i hele verden.Kommer i original emballasje.-------------------------------------------Tilbehør som følger med:Blå led Corsair vifter 1 stk 120mm og 1 stk 140mm2 stk Svarte Nzxt vifterBlå kabel utvider:24 pin hovedkort8 pin CPU2 x 8 pin GPUSøkeord:World of Warcraft, Diablo, BlizzardPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=361317238'
    },
    '362483988': {
        'heading': '''Hp z4 G4 Server/workstation i9-7900x''',
        'description': '''Selger min hp z4 G4 med 10 core i9-7900x prosessor pga jeg har oppgradertFlott maskin som er stillegående og greiDet er windows 11 pro engelsk installert på denDen kommer med 512gb m.2 nvme System diskHar også 1stk 1 tb 2.5\" SSD og 1stk 3.5\" 4tb 7200k disker montert64gb ram 4x16gb brikker (4 ledige spor)Skjermkort er Nvidia Quadro m4000 8gbIkke det som er avbildetDen har også cd/dvdSelges for 8000krJeg gidder ikke skambudJeg sender mot betaling av frakt og betaling er via bankoverføring på denne (helst)Gjør den også tilgjengelig via fiks ferdigØnsker du å bruke fiks ferdig, så kontakt meg først så kan jeg kontroll veie den i forhold til frakt pris med emballasje , usikker om den går som 20kg eller opp til 35kgEr det noe du lurer på, så send meg en mldPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=362483988'
    },
    '362490234': {
        'heading': '''gaming setup (ny pris!!!)''',
        'description': '''PC:gpu: gtx 1060 3gb MSIcpu: ryzen 7 2700hovedkort: Asrock b450 steel legendram: 16gb 3200 g.skill tridentZ.neossd: m.2 512gbcase: deep cool matrex 55strømforsyning: chieftec proton 750w silverskjerm: qube 27\" 165hz 1980 x 1080muse: hyperx (uten boks)mikrofon: hyperx quadcast (med boks)Jeg gir også bort en som ikke fungerer hyperx quadcast Shodetelefoner: hyperx cloud 2 (med boks)tastatur: 60% red nøkkelsvitsjtypePluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=362490234'
    },
    '246389117': {
        'heading': '''Riserless hovedkort med plass til 8 GPU''',
        'description': '''Riserless mining hovedkort med plass til 8 GPUkommer med CPU sata disk og 4GB RamBetaling: Vipps eller til kontoKan sendes om kjøper dekker frakt kr 129har flere, om du vil ha flere, kan diskutere prisen om du tar alle 3Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=246389117'
    },
    '254206491': {
        'heading': '''Skjermkort Nvidia Titan X 12 GB''',
        'description': '''Nvidia Titan X 12 GB MaxwellDette er ikke mye brukt og aldri overklokket. Har heller aldri blitt brukt til mining.Yter veldig bra og kommer til å bli samler kort etter vært.Hentes min adresse, eller sendes med Posten med sporing til 70,-Ønsker betaling med VIPPS før sending.SPECIFICATIONSBase Clock: 1127 MHZBoost Clock: 1216 MHzMemory Clock: 7010 MHz EffectiveCUDA Cores: 3072Bus Type: PCIe 3.0Memory Detail: 12288MB GDDR5Memory Bit Width: 384 BitMemory Speed: 0.28nsMemory Bandwidth: 336.5 GB/sLED Logo: YesUPC: 843368034788EAN: 4250812408587DIMENSIONSHeight: 4.376in - 111.15mmLength: 10.5in - 266.7mmWidth: Dual SlotKEY FEATURESHDMI 2.0, DisplayPort 1.2 and Dual-link DVIMicrosoft DirectX 12 (feature level 12_1)NVIDIA GameWorks TechnologyNVIDIA Adaptive Vertical SyncNVIDIA CUDA Technology with OpenCL supportNVIDIA Dynamic Super Resolution TechnologyNVIDIA G-SYNC ReadyNVIDIA GameStream TechnologyNVIDIA GPU Boost 2.0NVIDIA MFAA TechnologyNVIDIA SLI ReadyNVIDIA Surround TechnologyOpenCL SupportOpenGL 4.4 SupportPCI Express 3.0 x16RESOLUTION & REFRESHMax Monitors Supported: 4Max Analog: 2048x1536Max Digital: 4096x2160REQUIREMENTS600 Watt or greater power supply.PCI Express, PCI Express 2.0 or PCI Express 3.0 compliant motherboard with one graphics slot.An available 6-pin PCIe power connector and an available 8 pin PCIe power connectorWindows 10 32/64bit, Windows 8 32/64bit, Windows 7 32/64bit, Windows Vista 32/64bitPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=254206491'
    },
    '287543955': {
        'heading': '''Utrulig arbeidsstasjoner med GPU og Windows 11 Pro''',
        'description': '''Gaming Dell med 12 core CPUWindows 11 pro activertCpuXeon e5-1650 ( 6 core 12 threads)44 GB DDR3 ram quad channelAMD Radeon R9 380 ( 4 GB GDDR5 )256 GB SSD1 TB HDDWiFi kortE-Sport/Entry Gaming PC i et Stilig og Tidløst Kabinett.God Airflow og Lave Temperaturer.Alle deler er Renset og Testet samt ny kjølepasta.Perfekt til Fortnite, Overwatch, CS:GO, Apex, Valorant, Minecraft etc.Kommer med Windows 11 Pro. (Aktivert)Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=287543955'
    },
    '343127039': {
        'heading': '''ZOTAC GAMING GeForce RTX 3080 Trinity''',
        'description': '''Selger en brukt ZOTAC GAMING GeForce RTX 3080 Trinity Skjermkort.Kjøpt nytt ved release, har kun stått i pc.orginal emballasje følger med.Kjøper betaler frakt.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=343127039'
    },
    '365399486': {
        'heading': '''Hovedkort - ROG STRIX X570-E Gaming''',
        'description': '''!!!RESERVERT!!!Helt Nytt ROG STRIX X570-E Gaming Hovedkort - Ytelse i Toppklasse for Seriøse Gamere og SkapereBESKRIVELSE:Selger et ubrukt ASUS ROG STRIX X570-E Gaming hovedkort, kjøpt i september 2021 fra Komplett. Dette hovedkortet er en kraftpakke, ideelt for deg som ønsker å bygge en høytytende gaming-PC eller en arbeidsstasjon for innholdsskaping.Selges ettersom pc-byggeprosjektet den var egnet til aldri ble noe av. Hovedkortet har aldri vært montert i noen datamaskin, heller ikke har den blitt trekt ut av den antistatiske innpakningen.HOVEDKORTFUNKSJONER:- Støtte for AMD Ryzen 5000-serien: Optimalisert for AMDs prosessorer, som sikrer topp ytelse og fremtidsrettet teknologi i systemet ditt.- PCIe 4.0 Klar: Opplev lynraske dataoverføringshastigheter og fremtidssikker tilkobling med støtte for PCIe 4.0, perfekt for de nyeste GPU-ene og NVMe SSD-ene.- WiFi 6 og Bluetooth 5.0: Nyt ultrarask trådløs nettverking og sømløs tilkobling av enheter med de nyeste standardene WiFi 6 og Bluetooth 5.0.- Robuste Kjøleløsninger: Hovedkortet har omfattende kjølealternativer, inkludert flere kjøleribber og hybrid viftehoder, for å sikre at systemet ditt forblir kjølig og stabilt under tung belastning.- Aura Sync RGB-belysning: Tilpass oppsettet ditt med Aura Sync RGB-belysning, som lar deg synkronisere lyseffekter med andre kompatible komponenter for en visuelt imponerende rigg.- USB 3.2 Gen 2: Rask dataoverføring og tilkoblingsmuligheter, inkludert flere USB 3.2 Gen 2-porter, sikrer at systemet ditt kan håndtere de mest krevende enhetene.ROG STRIX X570-E Gaming er fortsatt et svært godt hovekort, selv i 2024. Det konkurrerer direkte med nyere kort som B650 og X670, men med en mer moden BIOS og bedre verdi for de som vil utnytte hver dråpe ytelse fra sin Ryzen-prosessor. Dette kortet er perfekt for entusiaster som ønsker en balanse mellom banebrytende funksjoner og pålitelighet. Det er også lett å få et billigere prosjekt generelt, ettersom hovedkortet er kompatibelt med er lass av andre komponenter, som er enklere å få billig, enn om man skulle kjøpt det nyeste av alt.Varen kan både hentes privat, men også sendes på kjøpers kostnad og risiko.Gleder meg til å motta din hendvendelse😁Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/365399486'
    },
    '367180380': {
        'heading': '''2 x Geforce GTX 680 kort''',
        'description': '''Selger 2 stk GTX 680 skjermkort. Er du ute etter å bygge eller oppgradere en eldre pc og ikke skal spille eller kjøre de nyeste og råeste spillene eller programmer så har du en bra løsning her.Jeg spilte bla.a Mafia III, Call of Duty Modern Warfare 3, WOT, CS, GTA, Deus Ex + på bra fps. Kortene ble mest brukt til rendring og jobb med video og 3D.Kortene selges samlet. En liten \"disclaimer\". 2 kort gir ikke dobbel ytelse og det er flere programmer som ikke støtter å kjøre 2 og vil da bare bruke det ene men du vil da i mange tilfeller kunne kjøre andre ting på det andre kortet. Du må også være sikker på at du har et hovedkort som har to porter ledige og helst litt plass i mellom. Les mer om kortet her : https://www.techpowerup.com/gpu-specs/geforce-gtx-680.c342Selv om de er noen år så finnes det en bra artikkel her om å bruke disse kortene: https://www.reddit.com/r/lowendgaming/comments/10jo29h/gtx_680_is_surprisingly_not_that_bad_for_its_age/Kan hentes eller leveres i Oslo eller sendes.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/367180380'
    },
    '367562535': {
        'heading': '''Rimelig gaming maskin''',
        'description': '''PC pakke  selgesCPU: i5 4460sRam: 8GBHarddisk1: 240GB SSDHarddisk 2:500GBGPU: GTX 960   4GBWindows 10 HomeWiFi Nettverkskort500watt PSUMusTastatur24inch Skjerm (sendes ikke)Passer fint for kontor arbeid å litt enkle spill som Roblox, Minecraft, Fortnite mmKan levere i nærområdet10% depositum ved leveringPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/367562535'
    },
    '367667852': {
        'heading': '''ASUS Radeon RX 6650 XT Dual OC''',
        'description': '''Skjermkort selgesPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/367667852'
    },
    '368419172': {
        'heading': '''2400w psu. 1200w psu. 750w psu. Hovedkort. Skjermkort etc''',
        'description': '''2400w psu. 2000kr per stk. Fungerer optimalt. Lite brukt. Ta kontakt for pris På de andre tingene som er avbildet i annonsenPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=368419172'
    },
    '369419877': {
        'heading': '''KFA2 GeForce RTX 3080 SG LHR''',
        'description': '''RESERVERT.Kjøpt brukt på Finn i April 2023.Tidligere annonse her:https://www.finn.no/bap/forsale/ad.html?finnkode=297858267Har kun blitt brukt til spilling/VR.Original kvittering fra NetOnNet, original eske og alt innhold er tatt vare på og medfølger.Kjølepasta ble bytta for ca 1,5 måned siden (Arctic MX-6). Kjølepads ble byttet av forrige selger da e kjøpte kortet (April 2023).Tilstand er satt til \"Godt Brukt\" fordi e ikke hadde mulighet til å bytte kjølepads. De skal holde minimum et halvt år til, og om du er heldig, mange år.Anbefaler kjøper og følge med på hotspot temperatur av den grunn.Temperaturer e har ligget på med detta kortet i mitt kabinett (Bilde 7):GPU Temp ingen/lite last, ca 30 grader med 30% vifte.Hotspot ca 5-10 grader mer.GPU Temp tung last/100% bruk, ca 70 grader med 60-70% vifte.Hotspot ca 15-20 grader mer. (Oftere 15 grader, men krøp av og til opp til 20 over tid med veldig tung last, men ikke høyere.)Kjølepads bør byttes om hotspot blir mer enn 25 grader varmere enn GPU Temp (Så bruk alarm funksjonen på hotspot temp i HWinfo.)(Satte kortet til å kjøre vifte på minimum 30% med MSI afterburner fordi \"stock\" vifte styring skrudde av vifter under 30 grader. Noe som endte opp med at kortet hele tiden skrudde vifter av og på om og om igjen.)Skambud besvares ikke.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/369419877'
    },
    '369442800': {
        'heading': '''Skjermkort Nvidia RTX 3080 OEM - 10 gb''',
        'description': '''Bilder kommer.Brukt til gaming, selgast grunna oppgradering. Kan sendast, he ikkje original embalasje.NON-LHR til dei som bryr seg om slikt.GA102-200-KD-A1Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=369442800'
    },
    '369797821': {
        'heading': '''EVGA GEFORCE RTX 2070 Super XC Ultra Skjermkort''',
        'description': '''Pent brukt skjermkort, litt støvete men ellers flott!Kjøpt i 2019. Ekstra tykk kjøleribbe for lave temperaturer. selges grunnet oppgradering.jeg kan ta den med meg til byen og møtes ila ukePluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=369797821'
    },
    '370424423': {
        'heading': '''GeForce GTX 1070 Quick Silver 8G OC''',
        'description': '''GPU / Skjermkort selges fra MSI.DisplayPort x 3 (Version 1.4) / HDMI 2.0b / DL-DVI-DKjerne instillinger:1797 MHz / 1607 MHz (OC Mode)1771 MHz / 1582 MHz (Gaming Mode)1683 MHz / 1506 MHz (Silent Mode)8GB GDDR5 (256-bit) minne.Maks oppløsning: 7680x4320Testet og fungerer som det skal!Mangler desverre original eskePluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=370424423'
    },
    '371599734': {
        'heading': '''XFX Radeon RX 6950 XT Speedster MERC 319 Skjermkort GPU Grafikkort''',
        'description': '''🤦 Nei,  jeg er ikke intressert i byttehandelProduktserie: XFX Speedster MERC319Skjermkort, PCI-Express 4.0, 16 GB GDDR6NøkkelfunksjonerGrafikkprosessor: AMD Radeon RX 6950 XT med RDNA 2-arkitektur.Compute Units: 80 enheter.Infinity Cache: 128 MB, som forbedrer båndbredden og ytelsen.Minne: 16 GB GDDR6.Minnebuss: 256-bit.Game Clock: Opptil 2100 MHz.Boost Clock: Opptil 2368 MHz.Strømforbruk: Maksimalt 335 W, anbefalt strømforsyning på 700 W.Utganger: 1x HDMI 2.1, 2x DisplayPort 1.4a.Kjølesystem: Triple-slot design med avansert kjøling og Zero DB fan system for stille drift123.YtelseOppløsninger: Optimalisert for 4K gaming med høy bildefrekvens.Teknologier: Støtter DirectX 12 Ultimate, AMD FidelityFX, og AMD Smart Access Memory for forbedret ytelse når kombinert med AMD Ryzen-prosessorer💯 Skjermkortet fungerer som det skal✅ Fast pris - pruting blir ikke besvart✅ Kjøpsdato oktober 2023  Komplett.no✅ Kvittering følger med✅Pent bruk - støvfritt✅ Original emballasje følger med🚗 Kan sendes - kjøper betaler frakt✅ Kan hentes i Lørenskog &  Gardermoen(Hverdager)Du finner mer informasjon her:https://www.xfxforce.com/shop/xfx-speedster-merc-319-amd-radeon-tm-rx-6950-xt-blackog her:https://www.komplett.no/product/1221527/datautstyr/pc-komponenter/skjermkort/xfx-radeon-rx-6950-xt-speedster-merc-319#Søkeord: Skjermkort, GPU, Grafikkort, ASUS , 3070. RTX,  XFX, Radeon.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/371599734'
    },
    '372202786': {
        'heading': '''GAMING PAKKE SELGES!!!!''',
        'description': '''Jeg selger min gaming pc og tastaturet og musen på grunn av at jeg bruker det lite kjøpte den ny for cirka 11,000kr for rundt 6-7 måneder siden, er villig til å gå til 7000kr gjerne gi en lyd om du er intresert! PS for hele pakken 9000krSpesifikaskjoner:TASTATUR OG MUStastaturet er en steelseries apex pro mini som ble kjøpt helt ny i straten av juni, og musen rundt samme tidspunkt går ikke under 2,500kr for begge to.PC:Pcen sin cpu er en intel(R) Core(TM) i5-8600kRAM 16gbSkjermkort er en geforce 3060tiGI LYD FOR MER INFORMASJONUten tastatur og mus 10,000krMed mus og tastatur 12,500krPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=372202786'
    },
    '372960714': {
        'heading': '''Gaming setup''',
        'description': '''Selger gaming utstyret fordi det ikke blir brukt.Pc 3000 ny pris 8000 ( når jeg kjøpte den)HP TG 01-0107NOKjøpt i juni 2021 men lite bruk de siste 2 årenehttps://www.power.no/data-og-tilbehoer/pc-og-mac/stasjonaer-pc/hp-tg01-0107no-stasjonaer/p-1027261/GPU NVIDIA Geforce GTX 1650Prosessorer ryzen 5 3500 6- Core8 GB RAM250 Gb ssd1000 Gb lagringGaming skjerm 1200 ny pris 1990 ( når jeg kjøpte den( MSI Optix 24\" LED Curved MAG24C )Hertz 144MS 1Tommer 24Muse matte pris 350 ny pris 690( razer gigantus v2 )Tastatur pris 300 ny pris 599( exo rascal mini keyboard rgb )Mus pris 400 ny pris 799( razer basilisk essential )Ratt og pedal pris 1500 ny pris 2990( Logitech G920 Driving Force Racing )Alt dette blir 6750Men du kan får det får 6200Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=372960714'
    },
    '374523080': {
        'heading': '''Radeon RX 6600 - 8 GB''',
        'description': '''https://www.computersalg.no/i/7708172/powercolor-fighter-radeon-rx-6600-grafikkort-radeon-rx-6600-8-gb-gddr6-pcie-4-0-hdmi-3-x-displayport?utm_source=prisjaktno&utm_medium=1001-it-elektronik-komponenter-grafikkort&utm_campaign=tul-corporation&utm_content=96&fwd=1Veldig fint skjermkort som jeg aldri har hatt problem med. Selger på grunn av jeg har oppgraderingPris kan diskuteres ved raskt kjøp👌👌Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/374523080'
    },
    '374632603': {
        'heading': '''Gainward GeForce RTX 2060 SUPER Ghost 8gb''',
        'description': '''Meget bra skjermkort. Har fungert utmerket. Har oppgradert så dette må dessverre ut. Tatt ut av PC oktober 24\' og lagt rett i eske.https://www.gainward.com/main/vgapro.php?id=1111&lang=enPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/374632603'
    },
    '375099773': {
        'heading': '''Amd Radeon RX 6800 16GB''',
        'description': '''Selger et pent brukt XFX AMD Radeon RX 6800 fra Speedster-serien. Dette kraftige skjermkortet har 16 GB GDDR6-minne og er bygget på AMDs RDNA 2-arkitektur. Det støtter 4K UHD-gaming, har PCIe 4.0-støtte og er optimalisert for å levere høy ytelse i både gaming og grafisk krevende applikasjoner.Spesifikasjoner:Modell: XFX AMD Radeon RX 6800 QICK 319 BLACK16 GB GDDR6 VRAMPCIe 4.0 støtte4K UHD gamingRDNA 2-arkitekturIdeell for high-end gaming og tyngre arbeidsoppgaverSelges grunnet oppgradering. Kortet er i topp stand og har aldri vært overklokket.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/375099773'
    },
    '375233518': {
        'heading': '''Asus GeForce ROG Strix RTX 2070 OC grafikkort 8G''',
        'description': '''Asus GeForce ROG Strix RTX 2070 OC grafikkort 8GSkjermkort som virker bra på spill i 2024Ingen problemer med skjermkort.Selges kun pga oppgradering.Har dessverre ikke kvitteringReviewhttps://www.tomshardware.com/reviews/asus-rog-strix-geforce-rtx-2070-o8g-gaming-gpu,5930.htmlLink til Elkjøphttps://www.elkjop.no/product/gaming/pc-komponenter/grafikkort/asus-geforce-rog-strix-rtx-2070-oc-grafikkort-8g/13591Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/375233518'
    },
    '375288343': {
        'heading': '''XFX Radeon RX 6600 SPEEDSTER SWFT 210 CORE''',
        'description': '''Säljer en GPU då jag uppgraderat för längesen.Köpte den då jag behövde en ny men ersatt så fort ett 4k kort blev tillgängligt, så inte mycket använt.Fungerar fint och står just nu bara i en plex server som jag inte orkar hålla på med.Önskar helst inte sända pga stötskador som fort kan uppstå, men gör det på köparens ansvar och räkning om önskligt.Har inte förpackning kvar då den försvann när vi flytta.Mer infohttps://www.netonnet.no/art/datakomponenter/skjermkort/amd/xfx-radeon-rx-6600-speedster-swft-210-core/1021378.11110/Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/375288343'
    },
    '375321896': {
        'heading': '''RTX 2060 6GB •RESERVERT•''',
        'description': '''Selges grunnet kjøp av ny. Pris kan diskuteres, men ikke kom med skambud (40%) under spørrepris.Blir sendt når jeg får mitt nye skjermkort. Antar det tar ca 2 uker (22.10.24)Søkeord: skjermkort, gpu, rtx, nvidia 2070 ti, 2080, 3060, 3060 ti, 4060 ti, 3050 ti,Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/375321896'
    },
    '375835453': {
        'heading': '''Komplett epic gaming Rtx 3060''',
        'description': '''-Selger denne pent brukte pc’en grunnet oppgradering.-kjøpt i ny i komplett 2022 for 14000 kr.-Spesifikasjoner:-Gpu Rtx 3060-Cpu: i5-10400f-Motherboard: Rog strix b560-RAM: 16gb ddr4-lagring: 500 gb-Send mld hvis du lurer på noePluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/375835453'
    },
    '375916333': {
        'heading': '''ASUS GeForce RTX 3070 Ti TUF OC''',
        'description': '''TUF-RTX3070TI-O8G-GAMINGGPU kjøpt med komplett-PC, 05/2022, selges grunnet oppgraderinger.Fungerer utmerket.Kan hentes på Carl-BernerPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/375916333'
    },
    '375986952': {
        'heading': '''ASUS DUAL GeForce RTX 4060 TI OC''',
        'description': '''Selger min 4060 ti skjermkort fordi jeg ønsker den samme, bare i hvit, for å bygge meg en hvit pc. Den er kjøpt fra komplett 16. januar i år og har 3 års garanti, følger med kopi av kvitteringa. Dersom du lurer på noe mer gjerne send en melding:)Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/375986952'
    },
    '376023380': {
        'heading': '''Gaming setup''',
        'description': '''Selger komplett gamingsetup.Dette er en god pc som jeg har hatt i 3 år nå, aldri hatt noe problemer eller feil kjører alle spillene som jeg har spilt med god kvalitet.Prosessor: i5-10400 CPUSkjermkort: GTX 1660 superRAM: 8gb ddr4 ramTastatur: Steelseries Apex Pro TklMus: logitech g402Skjerm: LG 144hz 1ms og en HP 60hzKamera: Trust HD 720pHeadset: HyperX Cloud II (Ingen mikrofon)Musematte: logitech G640ssd Disk: 1tb Samsung ssd diskUSB Hub: Logik (4 porter)Pris kan diskuteresPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376023380'
    },
    '376030780': {
        'heading': '''RTX Asus tuf 3070 Skjermkort''',
        'description': '''Brukt to år. Fungerer utmerket.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376030780'
    },
    '376163907': {
        'heading': '''Komplett Battlebox Ultimate GeForce GTX 1080Ti 11GB , Core i7-8700K, 32GB''',
        'description': '''Selger min Gaming PC fra Komplett da den sliter litt med de tyngste flysimulatorer i VR som jeg bruker den til. Men som en maskin til alt mulig annet av spill så klarer den det meste helt fint ennå. Og skal man bruke den til enklere VR spill så går det også helt fint :-)Var i utgangspunkt 16gb ram på denne men det er oppgradert til 32gb.Satt inn en ekstra Samsung SSD på 1TB for noen år sidenOgså nylig kjøpt en WD Black 1TB M2 SSD (5150/4900Mb/s) for å ha spill på da denne har raskest read/write.Ellers er det også en helt vanlig harddisk på 1TB som maskinen kom med og en M2 SSD på 512GB som operativsystemet er på.Leverer med mus og tastatur inkludert i prisen og alle restdeler, pc eske og bruksanvisninger fra da komplett bygde den.KOMPONENTER:Komplett Battlebox Ultimate-Windows 11-GeForce GTX 1080Ti 11GB, Core i7-8700K, 32GB, 512GB + 1TB SATA + 1TB SSD + 1TB M2 SSD-Cooler Master MasterKeys Lite Combo RGB kablet, nordisk, 3500 dpi, mechanical taster, rgb lys,   spillmus + tastatur-Fractal Design Define C Temp G, Vifter: 1x120mm front, 1x 120mm bak, mITX, mATX, ATX-Corsair TX750M, 750W PSU ATX 12V v2-4, 80 Plus Gold, Semi Modular, 6+2-pin PCIe-Intel Core i7-8700K Prosessor, Socket-LGA1151, 6-Core, 12-Thread, 3.7/4.7GHz, 95W-Corsair Hydro Series H105 CPU Kjøler, 240mm Radiator-ASUS ROG STRIX Z370-F Gaming, S1151, Hovedkort,ATX,Z370,DDR4,3xPCIe-x16,SLI/CFX, 2xM.2, USB 3.1, AuraSync, SupremeFX-EVGA GeForce GTX 1080 Ti FTW3 GAMING, Skjermkort, PCI-Express 3.0, 11GB GDDR5X, 1569/1683MHz-WD Black 512GB M.2 PCIe SSD, M.2 2280, PCIe, NVMe, up to 2050/800MB/s read/write-Seagate Barracuda 1TB 3.5\'\' HDD, SATA 6.0Gb/s, 7200RPM, 64MB cache, 3.5\'\'-Støtsikker PC-eskeKan fint sende denne da jeg har den store støt sikre esken som nevnt over her ennå. Veier 16-18 kg ferdig pakker så derfor noe dyrere frakt.Kan overklokkes opp mot 5GHzSlettet, formatert, rengjort og klar for oppsett av ny bruker i Windows 11Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376163907'
    },
    '376184828': {
        'heading': '''2 stk RTX 2070 Super og 1 stk RTX 2080''',
        'description': '''Skjermkortene er kun gamet med og fungerer utmerket. Disse takler dagens spill fint på høye innstillinger og gir god FPS.Priser:MSI Geforce RTX 2070 Super Gaming X Trio 8GB - 2100,-Gigabyte Geforce RTX 2070 Super Windforce 3X 8GB - 1900,- SOLGTMSI Geforce RTX 2080 Ventus V2 8GB - 2600,- SOLGTKan sendes med liten postnord pakke til 69kr eller medium norgespakke til 135krPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376184828'
    },
    '376208776': {
        'heading': '''GeForce RTX 3060 Ti VENTUS 2X OC''',
        'description': '''Pent brukt skjermkort selges. Har kun stått i en reservemaskin, så nesten ikke brukt.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376208776'
    },
    '376352146': {
        'heading': '''RTX 2070 selges til rimelig pris''',
        'description': '''Selger denne 2070 dersom jeg sparer til nytt skjermkort. Alt funker som det skal.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376352146'
    },
    '298403201': {
        'heading': '''MSI Radon R9 380 Gaming 4gb''',
        'description': '''Selger 2stk pent brukte skjermkort.Disse har fått ny kjølepasta og custom lys i de røde rillene. Noe disse kortene ikke er utstyrt med originalt.Fungerer veldig bra til en god del spill fortsatt.Shadow of the Tomb Raider, Stray, Far Cry 5 og GTA 5 er blant noen av spillene disse kortene fungerer kjempebra til med høy til ultra grafikk.Selges som par.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=298403201'
    },
    '352240276': {
        'heading': '''CPU: i9 9900x Hovedkort: ASUS Prime x299 deluxe''',
        'description': '''selges samletcpu i9 9900xTotal Cores 10Total Threads 20Max Turbo Frequency 4.40 GHzIntel® Turbo Boost Max Technology 3.0 Frequency ‡ 4.50 GHzProcessor Base Frequency 3.50 GHzCache 19.25 MB Intel® Smart CacheBus Speed 8 GT/s# of QPI Links 0TDP 165 WHovedkort prime x299 deluxeIntel LGA 2066 ATX motherboard with M.2 Heatsink, DDR4 4133MHz, 802.11ad Wi-Fi, Dual M.2, U.2, Intel VROC support, SATA 6Gb/s, Front-panel USB 3.1 Gen 2 connector5-Way Optimization: One-click, system-wide tuning, delivering optimized overclocks and intelligent cooling for CPU or GPU-intensive tasks.Industry-leading cooling options: Comprehensive controls for fans and water pumps, via Fan Xpert 4 software or the acclaimed ASUS UEFI.Next-gen connectivity: Supreme flexibility with 2x2 802.11ad Wi-Fi, Thunderbolt 3, U.2, M.2 and front USB 3.1 Gen 2 connector.M.2 heatsink: Ultra-efficient heatsink reduces M.2 SSD temperatures by up to 20°C for unthrottled transfer speeds and enhanced reliability.LiveDash: A customizable onboard display that shows system temperature, CPU frequency, fan speeds or even your own logo.Aura Sync and addressable-LED header: Controllable onboard RGB lighting and addressable-LED-strip header, easily synced with an ever-growing portfolio of Aura-capable hardware.(mangler iso shield)PS: SENDER IKKE.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=352240276'
    },
    '362958481': {
        'heading': '''GIGABYTE GeForce RTX 3070 Ti EAGLE - Grafikkort''',
        'description': '''GIGABYTE GeForce RTX 3070 Ti EAGLE selges grunnet oppgradering.Kortet fungerer fint, men kunne sikkert trengt nytt kjølepasta/themal pads.Kan sendes i emballasje og eske til en annen GPU.Søkeord:(ignorer)GPU, Grafikkort, 3070 RTX, gaming, kraftig, RGB, fortnite, cod, call of duty, wow, pc, data, computer, esport, cs2, csgo, DLSS, ray tracing, 4k, datautstyr,Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/362958481'
    },
    '370254835': {
        'heading': '''Quadro P2200 skjermkort''',
        'description': '''Nvidia Quadro P2200 skjermkort med 4 DisplayPort utganger. 5GB.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=370254835'
    },
    '374506297': {
        'heading': '''Nvidia Geforce RTX 3060 TI''',
        'description': '''bra skjermkort 1.5 år gammel alt ok. Aldri overklokket.  Brukt litt for gaming valorant . CsgoPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/374506297'
    },
    '259045002': {
        'heading': '''Asrock H110 Pro BTC''',
        'description': '''Selger hovedkort for mining.Svært lite brukt !Kan selges komplett med cpu,ram og vifte. Plug and play !Plass til 13 gpu !Kun ett hovedkort igjen !Kan sende mot at kjøper betaler frakt.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/259045002'
    },
    '343360620': {
        'heading': '''GTX skjermkort''',
        'description': '''ROG STRIX GTX1660S skjermkort selges. Har ligget i avbildet boks i et par år urørt. Denne er helt fin å bruke, men jeg oppgraderte til RTX 3060Ti skjermkort (Vurderer å selge denne også for å kunne oppgradere pånytt, evt si ifra ved interesse for en av de to).Trenger standard pleie før bruk, er litt støv.Boksen er fra mitt nåværende skjermkort, derfor følger ikke med til GTX skjermkortet dessverre, kom med noe beskyttende for transport❤️Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=343360620'
    },
    '371517170': {
        'heading': '''Fractal Design Node 202 med strømforsyning''',
        'description': '''Selger Fractal Design Node 202 kabinett med modifikasjoner, inkludert Fractal Design SFX Integra 450W PSU.Kabinettet leveres også med en spesialtilpasset, støtsikker koffert.Modifikasjoner:Støtte for større skjermkort (B: 54mm, D: 305mm, H: 130mm)Ekstra kjøling til skjermkortet (inkludert 4 kabinettsvifter)Dette er en perfekt løsning for deg som ønsker å bygge en kompakt, stillegående og kraftig PC. Kabinettet passer utmerket til hjemmekino-PC, gaming eller en minimalistisk skrivebords-PC.Spesifikasjoner:Fractal Design Node 202:Formfaktor: Mini-ITXDimensjoner: 377 x 82 x 330 mm (B x H x D)Vekt: 3,5 kgStøtte for GPU: Opptil 310 mm lengdeLagringsplasser: 2 x 2,5” SSD/HDDVifter: Støtte for 2 x 120 mm vifterI/O-porter: 2 x USB 3.0, Audio in/outMateriale: Stål og plastPlassering: Kan brukes både horisontalt og vertikaltPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/bap/forsale/ad.html?finnkode=371517170'
    },
    '374702676': {
        'heading': '''PNY NVIDIA RTX  A2000 6GB''',
        'description': '''selger et veldig fint brukt PNY NVIDIA RTX  A2000 6GB skjermkortdette er et enormt strøm effektivt skjermkort som eg har brukt som transcoding i plex media server. i omtrent 1mnd.  blir byttet ut da det er heilt overkill for dette.  trenger ikke ekstern strøm tilkobling, henter strøm rett ifra hovedkort.hadde også tenkt å benytte dette i ein kompakt gaming pc build men gjekk for større kabinett så då blir dette liggene på hylla.Memory Size: 6 GPCI Express 4.0 x16Maks ekstern oppløsning7680 x 4320Maks. antall skjermer som støttes4GDDR6 SDRAMWorld’s Fastest ITX Card: Low-Profile and Slot-Poweredfølger med brakett for å benytte dette som halv slot kort. samt den som står på som er full size.kan bli sendt i original emballasjenhttps://www.multicom.no/pny-nvidia-rtx-a2000-grafikkort/cat-p/c/p1002211062https://www.pny.com/nvidia-rtx-a2000Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/374702676'
    },
    '374820954': {
        'heading': '''RTX 2070 - intel core i7-8700''',
        'description': '''Bra og pent brukt gaming pc for de som ikke vil sviav lønna- selges grunnet jeg har kjøpt ny pcSpecsCPU: Intel Core i7-8700GPU: MSI GeForce RTX 2070 VENTUSRAM: 16 GB 2666MHzlagring: 1TB 64GBPris kan diskuteresPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/374820954'
    },
    '374981509': {
        'heading': '''RX 6950 XT || Med kvittering!''',
        'description': '''FORTSATT TILGJENGELIG! Førstemann.XFX Radeon RX 6950 XT Speedster MERC 319Kan sendes! Evt hentes i Oslo, eller Hønefoss etter avtale.Ikke brukt til mining eller liknende.VideoutgangKlokkehastighetsøkning 2368 MHzGrensesnittype PCI Express 4.0Grafikkprosessorfabrikant AMDAntall strømningsprosessorer 5120Type GrafikkortProsessteknologi 7 nmGrafikkprosessor AMD Radeon RX 6950 XTKlokkehastighet 2009 MHzStøttet videosignal DisplayPort, HDMIVideoadapterfunksjoner Video Streaming inntil 8 K, AMD Infinity Cache, Dual Bios, Frame Rate Target Control(FRTC), AMD WattMan, Variable Refresh Rate (VRR), XFX Iconic Ghost Thermal Design, AMD Eyefinity Technology, Radeon Anti-Lag, AMD Smart Access Memory, AMD FidelityFX Super Resolution (FSR), RDNA 2 Architecture, Dual ball Bearing Fans, Virtual Super Resolution (VSR), DTS-HD Master Audio-støtte, Dolby True HD-støtte, AMD FidelityFx, FreeSync Technology, Radeon Image Sharpening, 0dB TechnologyStøttede API DirectX 12 Ultimate, OpenGL 4.5, OpenCLUtgangsporter (kompakt liste) 3 x DisplayPort, HDMIVideominneBussbredde 256-bitInstallert størrelse 16 GBMinnehastighet 18 GbpsTeknologi GDDR6 SDRAMSystemkravPåkrevd strømforsyning 850 WEkstrakrav 2 x 8 pin PCI Express-strømkontaktOS påkrevd Windows 11, Windows 10DiverseFarge SvartFargekategori Sølv, SvartTilpassede standarder DisplayPort 1.4, DSC, RoHSStørrelser og vektBredde 5.7 cmDybde 34 cmHøyde 13.9 cmStørrelser og vekt (forsendelse)Fraktbredde 12.5 cmFraktvekt 2.41 kgFraktdybde 344.5 cmFrakthøyde 23.5 cmService og støtteType 3 års garantiService- og støttedetaljerService og støtte Begrenset garanti - 3 årGrensesnittGrensesnitt HDMI, 3 x DisplayPortProgramvareType Displaydrivere, AMD Radeon SoftwareSøkeord: GPU, Skjermkort, PC, Data, Stasjonær, Bærbar, gaming, GTX, RTX, grafikkort, GPU, hovedkort, AM4, AM5, Intel, CPU, ProsessorKan også vurdere å kjøpe GTX, RTX 980, 1060, 1070, 1070 Ti, 1080, 2060, 2070, 2080, 2080 Ti, 3060, 3060 Ti, 3070, 3070 Ti, 3080, 3080 Ti, 3090, 3090 ti, 4060, 4060 TI, 4070, 4080, 4090, RX6900XT, RX 6900XT, RX6900 XT, RX 6900-XT, Ryzen, Intel, AMD, RX6950XT, RX6950 XT, RX 6950XT, 4050, 4060, 4060 Ti, 4070, 4070 Super, 4070 Ti, 4070 Ti Super, 4080, 4080 Super, 4090Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/374981509'
    },
    '375129972': {
        'heading': '''Old School Gamer''',
        'description': '''Selger en old School Gamer som inneholderEtt romslig Fractal Design Core 2500 - tower - ATX med 2 vifterHovedkortMSI Z77 MPowew Med trådløs wifiCPUi7 3770kKjøler Cooler MasterMinne 4xKingston HyperX K... 4 GB DDR3 - 1600 SDRAM 800 MHZ  x4 stkSkjermkortGeForce GTX 970 4 GBHarddiskSanDisk 256 GBStrømforsyningCorsair CX600MOperativsystemWindows 11 Home AktivertOffice 2007 Full pakkeKan selges med skjerm og mus/tastatur for ett tilleggPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/375129972'
    },
    '375419768': {
        'heading': '''ASUS RTX 4060 TI DUAL OC 8GB''',
        'description': '''Skjermkortet er nytt, ble åpnet for bilder. Jeg ombestemte meg om å sette den inn i forsamlingen.  Kvittering og full garanti fra Komplett👍For eventuelle spørsmål, skriv 😉Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/375419768'
    },
    '375629474': {
        'heading': '''InWin GRone Full Tower Svart RGB  i5 7400 3,0GHz, 16GB, 128GB SSD, 1TB''',
        'description': '''En Super stasjonær til surfing, kontor, Foto, redigering, AutoCAD og Gaming som kjøter det på fult fortinte, PUBG, CS:GO og mange andre spill i 1080p. Bygget med gode deler fra Kingston Asus, Corsair, Klink Intel. Delene som har vært i bruk og er nøye gjennomgått grundig testing. PC-en leveres med aktivert Windows 11.SpesifikasjonerKabinett: InWin GRone Full Tower Svart RGBSkjermkort: Msi rx5700xtCPU vifte: coller masterStrømforsyning: DeepCool 700WHovedkort: MSI Z170A PC MATE Socket-1151Prosessor: i5 7400 3,0GHz 4 kjerner og 4 tråderTurbo: 3,5GHzRam: Fury 16GB DDR4 300HzHarddisk: 1TB Western Digital og samsung  256GB SSDOperativsystem: Ekte Windows 11 Norsk med Libreoffice 7,6(NY)Tastatur: Denver Gaming tastarur og Mus (NY)Nettverk: D-link USB wifi (Ny)Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/375629474'
    },
    '375966586': {
        'heading': '''ASUS GeForce GTX 1080Ti ROG Strix Gaming''',
        'description': '''ASUS GeForce GTX 1080Ti ROG Strix Gaming selges.Kan sendesMed Asus ROG Strix GeForce GTX 1080 Ti OC-grafikkort kan du øke gamingytelsen til din stasjonære gaming-PC og gjøre den i stand til å takle selv AAA-spill med fullt detaljnivå og 4 K-oppløsning. Grafikkortet bruker et meget bredt 352-bit grensesnitt og 11 GB rask GDDR5X RAM for å takle de mest krevende spillene. Med OC Mode kan du øke både klokke- og kjernefrekvensen når du trenger mer kraft til krevende applikasjoner og program.Kjøling: Med triple Wing Blade-vifter og MaxContact-radiator med varmerør har direktekontakt med CPU-en, slik at varmen fjernes raskere og ytelsen holdes stabil selv ved krevende gaming. Samtidig gjør vingeformene på viftene at lydnivået holdes lavt. Med Asus FanConnect kan du også koble to GPU-styrte viftetilkoblinger til hovedkortet og gi hele PC-en optimal kjøling.Nvidia G-Sync: Denne teknologien synkroniserer oppdateringsfrekvensen til G-Sync-kompatible skjermer med grafikkortet for å minimere hakking og forsinkelse.VR Ready: Nvidia VR Ready-sertifisering gjør kortet ideelt for VR-spill og apper. Med HDMI-utgang kan du koble til ditt VR-headset uten å koble fra skjermen.AuraSync RGB-belysning: Velg blant over 16,7 millioner farger og seks ulike effekter for LED-belysninger på bakplaten og på frontkjøleren.Egenskaper:- PCI Express x16 3.0 bus- 11 GB GDDR5X minne- 3584 CUDA cores- 11010/11100 MHz memory clock frekvens (OC-modus/Gaming-modus)- 1594/1708 MHz GPU core clock frekvens i OC-modus (GPU Boost off/on)- 1569/1683 MHz GPU core clock frekvens i Gaming-modus (GPU Boost off/on)- 2x HDMI, 1x DVI-I og 2x DisplayPort-tilkoblinger- Støtte for 8K-skjermer (7680 x 4320)- Støtte for opptil 4 skjermer samtidig- DirectX 12-støtte- Asus GPU Tweak 2-app- Nvidia SLI-støtte- Nvidia VR Ready- Robust bakplate som hindrer at kortet bøyesPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/375966586'
    },
    '376052489': {
        'heading': '''CPU hovedkort osv selges''',
        'description': '''Cupen som er på bilde selges sammen med en Acer predator uten skjermkort.Det som følger med er psu CPU hovedkort og ram, hvis du ønsker følger tårnet med, der er ledningsnettet ødelagt og psu gir strøm selv om pcen skrues av... Fungerer forttsatt men psu burde byttesPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376052489'
    },
    '376506528': {
        'heading': '''Quadro P2000 skjermkort''',
        'description': '''Nvidia Quadro P2000 skjermkort med 4 DisplayPort utganger. 5GB.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376506528'
    },
    '376565651': {
        'heading': '''ASUS TUF Gaming GeForce RTX™ 3070''',
        'description': '''1stk ASUS TUF Gaming GeForce RTX™ 3070 skjermkort.(har totalt 8stk)Grunnet stor etterspørsel på ASUS TUF kort så er det ikke mulig med kvantum rabattBuffed-up design with chart-topping thermal performance.NVIDIA Ampere Streaming Multiprocessors: The building blocks for the world’s fastest, most efficient GPU, the all-new Ampere SM brings 2X the FP32 throughput and improved power efficiency.2nd Generation RT Cores: Experience 2X the throughput of 1st gen RT Cores, plus concurrent RT and shading for a whole new level of ray tracing performance.3rd Generation Tensor Cores: Get up to 2X the throughput with structural sparsity and advanced AI algorithms such as DLSS. Now with support for up to 8K resolution, these cores deliver a massive boost in game performance and all-new AI capabilities.Axial-tech Fan Design has been newly tuned with a reversed central fan direction for less turbulence.Dual Ball Fan Bearings can last up to twice as long as sleeve bearing designs.Military-grade Capacitors and other TUF components enhance durability and performance.GPU Tweak II provides intuitive performance tweaking, thermal controls, and system monitoring.--   Q&A.  —Har kortet blitt brukt til Mining?SVAR:Så å si samtlige GPU som jeg selger er brukt til MiningSamtlige GPU var brukt til Mining.(a) Kortene har ikke vært overklokket(b) Kortene har ikke hatt temperaturer over +50 grader.(c) Det har vært konstant og stabilt bruk noe som gir mindre slitasje enn gaming.(d) Ikke minst så har kortene kun vært i bruk 8-11 måneder beroende på kort.Samtlige GPU 3060Ti, 3070, 3080 og 3090 kort, ble kjøpt når det kun var 8-11 måneder igjen for ETH skulle gjennomføre fra PoW til PoS.Jeg gamblet at PoS skulle bli utsatt «igjen» eller at ny Crypto skulle overta hvis ETH gikk over på PoS.  Jeg bommet på begge….Deretter har kortene ikke vært brukt grunnet at jeg har ventet i det lengste for at det skulle bli lønnsomt å mine eller AI med GPU.For 9 måneder begynte vi demonterte hele GPU parken. Vi har solgt ut både ASIC og GPU etter gjennomgang av hvert produkt.Har du kvittering, hvor er kort kjøpt?SVAR:Hadde totalt over 300 GPU, og funnet flytt har jeg ikke kvitteringer på disse. Alle kort ble kjøpt der det var mulig å kjøpe GPU. (i en periode var det omtrent umulig å kjøpe GPU)Alle GPU ble kjøpt hos:* Nettbutikker,* Private* Import fra utlandet* Helt nye Gaming PC der GPU ble tatt ut fra PC for montering i Mining rigg.Tar du bytte?SVAR: ja, KryptoKan du gi bedre pris?Etterspørsel etter GPU er stor, og hvis en type ikke blir solgt er det bare å gå ned noen hundre så selges det uansett.Følger originaleske med?Det var ikke mulig for oss å lagre flamme hindre esker. Forsendelse. Pakkes godt, jeg kan også sende bilde ved sendning.Rabatt gis ved kjøp av flere kort:(3060Ti, 3070, 3080 og 3090)Alternativ kom med bud, skambud besvares ikke.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376565651'
    },
    '376570994': {
        'heading': '''Gigabyte GeForce RTX 3070 GAMING OC 8G''',
        'description': '''PCI Express 4.0 x16Videoutgang / Støttet videosignal: HDMI, DisplayPortMaks ekstern oppløsning: 7680 x 4320—-Generelt—-Produkt spesifikasjonslisteEnhetstype: GrafikkortBusstype: PCI Express 4.0 x16Grafikkprogram: NVIDIA GeForce RTX 3070CUDA-kjerner: 5888Maks. oppløsning: 7680 x 4320 ved 60 HzMaks. antall skjermer som støttes: 4Grensesnittdetaljer: 2 x DisplayPort, 2 x HDMIStøttede: API, DirectX 12, OpenGL 4.6—-Egenskaper—-NVIDIA Ampere GPU-teknologi, Nvidia RT Core, NVIDIA Tensor Core, GIGABYTE WindForce 3x, RGB Fusion 2.0 Minne—-Produkt spesifikasjonsliste—-Størrelse: 8 GBTeknologi: GDDR6 SDRAMFaktisk klokkehastighe; 14000 MHzBussbredd: 256-bitBåndbredd; 448 GBpsSystemkra: Produkt spesifikasjonslistePåkrevd strømforsynin: 650 WEkstrakrav:6-pins + 8-pins PCI Express-strømkontakter—-Diverse—-Produkt spesifikasjonslisteTilpassede standarder DisplayPort 1.4aBredde 5.1 cmDybde 28.6 cmHøyde 11.5 cm--   Q&A.  —Har kortet blitt brukt til Mining?SVAR:Så å si samtlige GPU som jeg selger er brukt til MiningSamtlige GPU var brukt til Mining.(a) Kortene har ikke vært overklokket(b) Kortene har ikke hatt temperaturer over +50 grader.(c) Det har vært konstant og stabilt bruk noe som gir mindre slitasje enn gaming.(d) Ikke minst så har kortene kun vært i bruk 8-11 måneder beroende på kort.Samtlige GPU 3060Ti, 3070, 3080 og 3090 kort, ble kjøpt når det kun var 8-11 måneder igjen for ETH skulle gjennomføre fra PoW til PoS.Jeg gamblet at PoS skulle bli utsatt «igjen» eller at ny Crypto skulle overta hvis ETH gikk over på PoS.  Jeg bommet på begge….Deretter har kortene ikke vært brukt grunnet at jeg har ventet i det lengste for at det skulle bli lønnsomt å mine eller AI med GPU.For 9 måneder begynte vi demonterte hele GPU parken. Vi har solgt ut både ASIC og GPU etter gjennomgang av hvert produkt.Har du kvittering, hvor er kort kjøpt?SVAR:Hadde totalt over 300 GPU, og funnet flytt har jeg ikke kvitteringer på disse. Alle kort ble kjøpt der det var mulig å kjøpe GPU. (i en periode var det omtrent umulig å kjøpe GPU)Alle GPU ble kjøpt hos:* Nettbutikker,* Private* Import fra utlandet* Helt nye Gaming PC der GPU ble tatt ut fra PC for montering i Mining rigg.Tar du bytte?SVAR: ja, KryptoKan du gi bedre pris?Etterspørsel etter GPU er stor, og hvis en type ikke blir solgt er det bare å gå ned noen hundre så selges det uansett.Følger originaleske med?Det var ikke mulig for oss å lagre flamme hindre esker. Forsendelse. Pakkes godt, jeg kan også sende bilde ved sendning.Rabatt gis ved kjøp av flere kort:(3060Ti, 3070, 3080 og 3090)Alternativ kom med bud, skambud besvares ikke.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376570994'
    },
    '376581898': {
        'heading': '''Asus RTX Geforce 3070 turbo 8G''',
        'description': '''ASUS TURBO-RTX3070-8GGrafikkort - GF RTX 3070 -8 GB GDDR6 -PCIe 4.0 -HDMI, 3 x DisplayPort--   Q&A.  —Q1.  Har kortet blitt brukt til Mining?SVAR:Samtlige GPU var brukt til Mining.(a) Kortene har ikke vært overklokket(b) Kortene har ikke hatt temperaturer over +50 grader.(c) Det har vært konstant og stabilt bruk noe som gir mindre slitasje enn gaming.(d) Ikke minst så har kortene kun vært i bruk 8-11 måneder beroende på kort.Samtlige GPU 3060Ti, 3070, 3080 og 3090 kort, ble kjøpt når det kun var 8-11 måneder igjen for ETH skulle gjennomføre fra PoW til PoS.Jeg gamblet at PoS skulle bli utsatt «igjen» eller at ny Crypto skulle overta hvis ETH gikk over på PoS.  Jeg bommet på begge….Deretter har kortene ikke vært brukt grunnet at jeg har ventet i det lengste for at det skulle bli lønnsomt å mine eller AI med GPU.For 9 måneder begynte vi demonterte hele GPU parken. Vi har solgt ut både ASIC og GPU etter gjennomgang av hvert produkt.Q2.  Har du kvittering, hvor er kort kjøpt?SVAR:Hadde totalt over 300 GPU, og funnet flytt har jeg ikke kvitteringer på disse. Alle kort ble kjøpt der det var mulig å kjøpe GPU. (i en periode var det omtrent umulig å kjøpe GPU)Alle GPU ble kjøpt hos:* Nettbutikker,* Private* Import fra utlandet* Helt nye Gaming PC der GPU ble tatt ut fra PC for montering i Mining rigg.Q3.  Tar du bytte?SVAR: ja, KryptoQ4.  Kan du gi bedre pris?Etterspørsel etter GPU er stor, og hvis en type ikke blir solgt er det bare å gå ned noen hundre så selges det uansett.Rabatt gis ved kjøp av minimum 4 kort:(3060Ti, 3070, 3080 og 3090)Q5.  Følger originaleske med?Det var ikke mulig for oss å lagre mange hundre esker. Forsendelse. Pakkes godt, jeg kan også sende bilde ved sendning.Alternativ kom med bud, skambud besvares ikke.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376581898'
    },
    '376691620': {
        'heading': '''ITX-bundle(B660/12400F/16GB)''',
        'description': '''ITX-pakke med hovedkort, CPU og RAM samt Intel-kjøler og CPU contact frame. Krever separat GPU da dette er en såkalt \"F\"-variant, dvs. at den mangler iGPU.Hovedkort: ASUS ROG STRIX B660-I GAMING WIFICPU: Intel Core i5-12400F(6 cores/12 threads)RAM: HyperX FURY DDR5 5600MHz CL36 16GB(2x8)Om hovedkortet: kjøpte det her på Finn som reparasjonsobjekt da det hadde bøyde pins i socket. Etter å ha rettet på disse virker kortet som det skal.Kan sendes.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376691620'
    },
    '376702098': {
        'heading': '''ASUS GeForce RTX 2070 SUPER ROG Strix OC Advanced Edition''',
        'description': '''En av de beste versjonene av rtx 2070 super, pent brukt og fungerer veldig bra med høy fps til både 1080p & 1440p, har aldri vært overclocket eller brukt til mining. Kjøpt på komplett.no.Kan også selge en vertical gpu mount for 300kr om den blir hentet.Bare spøre om du lurer på noe.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376702098'
    },
    '376706452': {
        'heading': '''GeForce GTX TITAN X (12GB)''',
        'description': '''GeForce GTX TITAN X, NVIDIA GPU.3072 kjerner, 12GB GDDR5 minne.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376706452'
    },
    '376743349': {
        'heading': '''Blackmagic eGPU''',
        'description': '''Ekstern GPU designet i samarbeid med AppleMed en AMD Radeon Pro 580 ombord har den boostet min gamle macbook dramatiskJeg selger fordi jeg har gått over på Apple Silicon og eGPU’en ikke fungerer med M2 chipenPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376743349'
    },
    '376756096': {
        'heading': '''RTX 3060 12(!)GB''',
        'description': '''Veldig pent brukt RTX 3060 til salgs, har boks og alt som følger med. Fremstår som nytt!Generelt godt skjermkort som skiller seg ut med 12GB VRAM, noe som gjør ar kortet kommer til å takle fremtidige spill godt i god tid fremover.Kan sendes men i så fall med forhåndsbetaling.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376756096'
    },
    '376777632': {
        'heading': '''Skjermkort/AMD Radeon 6700xt 12gb''',
        'description': '''Selger ett rått skjermkort. Kan selges for 3500kr. Har kvittering.XFX Radeon RX6700XT QICK 319 er en kraftig grafikkort med den nye AMD RDNA 2-arkitektur, som gir høyere bildekvalitet til dine favorittspill. Her får du 12 GB av det raske grafikkminnet GDDR6, slik at du kan spille med høye innstillinger og utrolig høy bildefrekvens. Nå trenger du ikke lenger å gå på akkord med oppløsningen for å spille med høy oppdateringsfrekvens. Grafikkortet er også utstyrt med funksjoner som DirectX 12 Ultimate, AMD FidelityFX og Radeon Anti-Lag.12 GB GDDR6-minneAMD RDNA 2-arkitekturen introduserer betydelige fremskritt i form av en forbedret databehandlingsenhet, ny visuell pipeline og ny AMD Infinity Cache, som muliggjør høyoppløselig spillytelse med levende bilder.AMD RDNA 2-arkitekturAMD RDNA 2-arkitekturen introduserer betydelige fremskritt i form av en forbedret databehandlingsenhet, ny visuell pipeline og ny AMD Infinity Cache, som muliggjør høyoppløselig spillytelse med levende bilder.DirectX 12 UltimateNå kan utviklere legge til enda mer fantastiske grafikkeffekter til Microsoft Windows-baserte spill. Grafikkortet har avanserte DX12-funksjoner som strålesporing og VRS (variabel hastighetsskygge), noe som gjør spillene mer livlige, med virkelige visuelle effekter og raskere bildefrekvens.AMD FidelityFXAMD FidelityFX er AMDs open source bildekvalitetsverktøykasse som består av syv forskjellige løsninger som utviklere kan implementere i spillene sine, og er optimalisert for AMD RDNA og RDNA 2-arkitekturer. FidelityFX bidrar til å gi den ultimate bildekvalitet.Effektivt kjølesystemGrafikkortet er utstyrt med et effektivt kjølesystem ved hjelp av tre vifter. I tillegg har systemet heatpipes som sørger for maksimal kontakt med GPU og distribuerer varme langs hele kjøleribben.Radeon Anti-LagDen nye Radeon Anti-Lag-funksjonen i Radeon Software er utviklet for å redusere inngangsforsinkelse. Radeon Anti-Lag styrer tempoet i prosessoren for å sikre at det ikke havner for langt foran GPU-en, som reduserer mengden prosessorkø for bedre respons i spillet.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376777632'
    },
    '376782459': {
        'heading': '''Sapphire Radeon RX 5700''',
        'description': '''Selger et veldig lite brukt skjermkort fra Radeon.Har ikke orginaleske til kortet siden den sto i en pc jeg kjøpte. Denne pakkes veldig godt inn og blir sendt på en trygg måte.Selger står for porto.Her er link til kortet som er kjøpt i 2019:https://www.komplett.no/product/1133404?noredirect=truePluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376782459'
    },
    '376880031': {
        'heading': '''ASUS TUF Gaming RTX 3060 OC 12GB''',
        'description': '''ASUS TUF Gaming RTX 3060 OCINNEBYGD TUFTUF GAMING GeForce RT 3060 har blitt strippet ned og bygget opp igjen for å gi mer solid kraft og kjøling. Et nytt metalldeksel inneholder tre kraftige aksialteknologiske vifter som bruker holdbare vifter med dobbelt kulelager. Vifterotasjon er optimalisert for å redusere turbulens, og en stoppmodus får alle tre viftene til å stoppe ved lave temperaturer. Under holder en tykk kjøleribbe kjølingen under tett kontroll. Ytterligere funksjoner, inkludert TUF-komponenter, Auto-Extreme Technology, og en bakplateventilasjon gjør TUF til et ordentlig kraftsenter. For byggere som leter etter en ny \"gammel trofast\", er dette kortet det riktige.NVIDIA Ampere Streaming Multiprocessors:Byggesteinene for verdens raskeste og mest effektive grafikkprosessor, den flunkende nye Ampere SM, gir deg dobbelt så høy FP32-gjennomstrømning og forbedret energieffektivitet.2. generasjons RT-kjerner:Opplev dobbelt så høy gjennomstrømning som 1. generasjons RT-kjerner, pluss samtidig RT og skyggelegging for et helt nytt nivå av strålesporing.3. generasjons Tensor-kjerner:Få opptil dobbelt så høy gjennomstrømning med strukturell spredthet og avanserte AI-algoritmer som DLSS. Disse kjernene leverer et enormt løft for spillytelsen og tilbyr helt nye AI-muligheter.Aksialviftedesigner blitt innstilt på nytt med en omvendt sentral vifteretning for å gi mindre turbulens.Vifter med dobbelt kulelagerkan vare opptil dobbelt så lenge som modeller med enkelt kulelager.Etdeksel i 100 % aluminiumogmetallbakplateforbedrer holdbarheten.GPU Tweak IIsørger for intuitiv ytelsestilpasning, varmestyring og overvåkning av systemet.Les mer:https://www.komplett.no/product/1186967?noredirect=true#technical-detailsPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376880031'
    },
    '376926740': {
        'heading': '''Asus GeForce RTX 3060 Ti TUF Gaming OC V2 8GB''',
        'description': '''Asus GeForce RTX 3060 Ti TUF Gaming OC V2 2xHDMI 3xDP 8GB skjermkort selges.Lite brukt.I original eske med antistatisk pose.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/376926740'
    },
    '377028227': {
        'heading': '''Razer Core X Chroma RC21-01430''',
        'description': '''Razor eGPU modell RC21-01430Funker som den skal, har brukt den på både en dell xps laptop og en asus gaminglaptop med 4070TI skjermkort og 1060. Selges grunnet overgang til stasjonær PC.Kort thunderbolt 3 kabel følger med.gi beskjed om du ønsker at power kabel skal følge med så kan jeg hoste opp en.GPU følger selvfølgelig ikke med, om du ikke har dette kan jeg supplere et 1060TI 6gb for 500krBredde 17cmDybde 38cmHøyde 23cmPluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/377028227'
    },
    '377066532': {
        'heading': '''GeForce RTX 2060 DUAL EVO OC''',
        'description': '''Pent brukt skjermkort selges. Stått i en masking som utelukkende har blitt brukt til surfing.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/377066532'
    },
    '377086143': {
        'heading': '''Asus Radeon RX 6800 XT''',
        'description': '''Selger mitt Asus Radeon RX 6800 XT skjermkort. Ekstremt høy ytelse til en god pris. PCen har ikke vært brukt mye siden kjøpet av skjermkortet. Send gjerne en melding ved eventuelle spørsmål.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/377086143'
    },
    '377151492': {
        'heading': '''Ducky Zero 6108''',
        'description': '''Nytt og ubrukt Ducky Zero 6108 tastatur selgesKan hentes i Bergen vest/Loddefjord/Olsvik eller sendes mot forskuddsbetaling og at kjøper dekker porto.Hvis du bor i nærheten kan jeg vurdere bytte i gpu f.eks rtx2070 eller nyere.Ta gjerne også en titt på mine andre ting jeg har ute for salg.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/377151492'
    },
    '377273776': {
        'heading': '''GeForce RTX 3090 24Gb''',
        'description': '''Selger et kraftig RTX 3090, ideelt for gaming og krevende grafikkarbeid. Kortet er brukt, men fungerer feilfritt og yter svært godt. Selges uten originalemballasje og kvittering.Krever 32 cm klaring i kabinettet.Strømforbruk: ca. 300–400W ved full last.Kan sendes med posten, men merk at Fiks Ferdig ikke er mulig på grunn av felles inngang.Forsendelse skjer på kjøpers ansvar og regning, med forhåndsbetaling etter avtale.Selges som det er, uten garanti. Kortet har fungert problemfritt i min PC, men som med all brukt elektronikk bør kjøper gjøre en selvstendig vurdering.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/377273776'
    },
    '377342777': {
        'heading': '''ZOTAC GeForce 1070 8GB SKJERMKORT''',
        'description': '''Selger mitt Zotac gtx1070 da jeg har oppgradert min pc. Kortet fungerer helt som det skal.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/377342777'
    },
    '377495278': {
        'heading': '''Radeon RX Vega 64 Air Boost 8G''',
        'description': '''Brukt Radeon RX Vega 64 Air Boost 8G til salgs!Kan hentes eller fraktes!Selger et pent brukt Radeon RX Vega 64 Air Boost 8G. Kortet har vært godt ivaretatt og gir fortsatt solid ytelse i de fleste spill og applikasjoner. Perfekt for deg som vil oppgradere til en kraftig GPU uten å tømme lommeboka.Spesifikasjoner:• Modell: Radeon RX Vega 64 Air Boost 8G• Minne: 8 GB HBM2• Kjøling: Air Boost - effektiv luftkjøling for stabile temperaturer• Tilkoblinger: HDMI, DisplayPort (flere porter for fleksibel tilkobling)Tilstand:• Kortet fungerer utmerket uten noen kjente problemer.• Renset for støv og klar for montering.• Aldri vært overklokket eller kjørt på høye  temperaturer.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/377495278'
    },
    '377525888': {
        'heading': '''NVIDIA Jetson TX2 Developer Kit''',
        'description': '''Mye kraftigere enn Jetson Nano.NVIDIA Pascal™ Architecture GPUDenver 64-bit CPUs + Quad-Core A57 Complex4GB L128 bit DDR4 Memory32 GB eMMC 5.1 Flash StorageConnectivity to 802.11ac Wi-Fi and Bluetooth-Enabled Devices10/100/1000BASE-T EthernetI/OUSB 3.0 Type AUSB 2.0 Micro AB (supports recovery and host mode)HDMIM.2 Key EPCI-E x4Gigabit EthernetFull-Size SDSATA Data and PowerGPIOs, I2C, I2S, SPI, CAN*TTL UART with flow controlDisplay Expansion Header*Camera Expansion Header**I/O expansion headers: refer to product documentation for header specification.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/377525888'
    },
    '377606872': {
        'heading': '''Asus GTX1070 Skjermkort''',
        'description': '''Selger Asus 8GB GTX1070.Kortet har fungert veldig fint og har kun blitt brukt til gaming og ikke mining. Men har nå oppgradert så ønsker derfor å selge dette kortet.Gir ca. 165 fps i Fortnite i 1080p med i5-7600 cpu og 16GB DDR4 ram, så det er mye ytelse for pengene :)Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/377606872'
    },
    '377668382': {
        'heading': '''Sapphire PULSE AMD Radeon RX 7700 XT''',
        'description': '''Selger et Sapphire Pulse AMD Radeon RX 7700 XT skjermkort i topp stand. Perfekt for gaming og gir høy ytelse på nye spill i 1080p og 1440p.Info:• Minne: 12 GB GDDR6• Kjøling: Effektiv, lavt støynivå under spill• Lite brukt, ingen skader, fungerer perfekt• Klar for høye FPS på høye innstillingerKan sende mot Vipps og kjøper betaler frakt. Ta kontakt for rask handel eller ved spørsmål!Nypris: 5568.- hos komplettPris: 4000.-Ta kontakt for rask handel eller ved spørsmål!Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/377668382'
    },
    '377699877': {
        'heading': '''Gigabyte Nvidia 1080 GPU''',
        'description': '''Ønsker at skjermkortet hentes i Trondheim. Har ikke testet det på ca et 1 år, men ser ikke noe grunn til at det ikke skulle fungere. Er ikke noe problem å komme tilbake med det, dersom det ikke fungerer.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/377699877'
    },
    '377706612': {
        'heading': '''ASUS GeForce GTX 1080 Ti ROG Strix''',
        'description': '''Supert skjermkort med 11gb vram selges grunnet oppgradering.Dette kortet var det raskeste kortet i nvidia sin legendariske 10-serie grafikkort. Her er det mye ytelse for pengene!Aldri vært overklokket eller brukt til mining.Bare å sende meld om du lurer på noe!Søkeord:1080ti, rtx, 2070, super, 3060ti, 3070, 4060, 1070, 1060,Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/377706612'
    },
    '377707696': {
        'heading': '''Nvidia Gefors Gtx1080 Fonder Edition''',
        'description': '''Skjelden mulighet.  Vanskelig å få fatt i Nvidia Gefors Gtx1080 Fonders editon. Kostet en formue da det var nytt. Solid gpu . Tilsvarende rtx3060.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/377707696'
    },
    '377709592': {
        'heading': '''Geforce RTX 3060Ti 8GB''',
        'description': '''1stk Geforce RTX 3060 Ti 8GB Turbine GamingGraphics Card 256bitGDDR6 GUP PCI-E 4.0 rtx 3060ti 8gℹ️   Q&A   ℹ️Q1.  Har kortet blitt brukt til Mining?SVAR:Samtlige GPU var brukt til Mining.(a) Kortene har ikke vært overklokket(b) Kortene har ikke hatt temperaturer over +50 grader.(c) Det har vært konstant og stabilt bruk noe som gir mindre slitasje enn gaming.(d) Ikke minst så har kortene kun vært i bruk 8-11 måneder beroende på kort.Samtlige GPU 3060Ti, 3070, 3080 og 3090 kort, ble kjøpt når det kun var 8-11 måneder igjen for ETH skulle gjennomføre fra PoW til PoS.Jeg gamblet at PoS skulle bli utsatt «igjen» eller at ny Crypto skulle overta hvis ETH gikk over på PoS.  Jeg bommet på begge….Deretter har kortene ikke vært brukt grunnet at jeg har ventet i det lengste for at det skulle bli lønnsomt å mine eller AI med GPU.For 9 måneder begynte vi demonterte hele GPU parken. Vi har solgt ut både ASIC og GPU etter gjennomgang av hvert produkt.Q2.  Har du kvittering, hvor er kort kjøpt?SVAR:Hadde totalt over 300 GPU, og funnet flytt har jeg ikke kvitteringer på disse. Alle kort ble kjøpt der det var mulig å kjøpe GPU. (i en periode var det omtrent umulig å kjøpe GPU)Alle GPU ble kjøpt hos:* Nettbutikker,* Private* Import fra utlandet* Helt nye Gaming PC der GPU ble tatt ut fra PC for montering i Mining rigg.Q3.  Tar du bytte?SVAR:Ja, KryptoQ4.  Kan du gi bedre pris?SVAR:Etterspørsel etter GPU er stor, og hvis en type ikke blir solgt er det bare å gå ned noen hundre så selges det uansett.Rabatt gis ved kjøp av minimum 4 kort:Q5.  Følger originaleske med?SVAR:Det var ikke mulig for oss å lagre mange hundre esker. Forsendelsen pakkes godt, jeg kan også sende bilde før jeg leverer pakken.Q6. Her kortene stått i ventilert rom?SVAR:GPU’ene har vært i ventilert i rigger på et av konferanserommene på hotellet jeg eier.Q7. Er kortene rengjort regelmessig?SVAR:Når kortene var i bruk: fra kjøpsdato frem til noen måned etter Etherium gjennomførte proof-of-stake (PoS) den 15.08.2022 så ble kortene sjekket ukentlig.Nå før salg sjekker vi vifter og blåser GPU’ene på nytt.Nå ved salg så sjekkes vi viftene på kortene på nytt.Skambud besvares ikke.Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/377709592'
    },
    '377734033': {
        'heading': '''GeForce RTX 2060 Dual OC, 8GB skjermkort''',
        'description': '''Geforce RTX 2060 Dual OC, 8GB selges.Har vert i bruk i ca 2,5 år. Ikke blitt benyttet i det siste da jeg måtte oppgradere flere deler pga tyngre arbeidsoppgaver på jobb.Se bilderSkjermkortet har ikke blitt benyttet til mining. Kun vanlig spilling og jobb.Kan sendes per post på kjøpers kostnad (135kr sporet frakt via posten).Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt.''',
        'url': 'https://www.finn.no/recommerce/forsale/item/377734033'
    },
}

# Mock functions for testing
def mock_fetch_page(page):
    """Mock version of fetch_page for testing"""
    if page == 1:
        return {
            'docs': [
                {
                    'id': ad_id,
                    'heading': data['heading'],
                    'canonical_url': data['url']
                }
                for ad_id, data in archived_listings.items()
            ]
        }
    return {'docs': []}

def mock_fetch_description(url):
    """Mock version of fetch_description for testing"""
    for listing in archived_listings.values():
        if listing['url'] == url:
            return listing['description']
    return ""
