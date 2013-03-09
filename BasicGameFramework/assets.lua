-- Metadata


IconAssets = group{quality=9.95}

Icon = image{"assets/icon.png"}



-- Asset Group loaded initially to all cubes

BootAssets = group{quality=8.90}

LoadingBg = image{"assets/loading.png"}

Bravo = image{"assets/bravo.png"}
Title = image{"assets/welcomeTitle.png"}


--TEST

Grid = image{"assets/playfield.png", pinned=1}

--TEST
-- Menu Assets
TestAssets = group{quality=9.05}
Title = image{"assets/welcomeTitle.png", flat=1}
SampleSound = sound{"assets/test.wav"}

BgTile = image{ "assets/Menu/bg.png", pinned=1 }
Grid = image{"assets/playfield.png", pinned=1}

IconSandwich = image{ "assets/Menu/IconSandwich.png" }
IconChroma = image{ "assets/Menu/IconChroma.png" }

Tip0 = image{ "assets/Menu/Tip0.png" }
Tip1 = image{ "assets/Menu/Tip1.png" }

Footer = image{ "assets/Menu/Footer.png" }

LabelEmpty = image{ "assets/Menu/LabelEmpty.png" }
LabelUser1 = image{"assets/Menu/LabelAdrian.png"}
LabelUser2 = image{"assets/Menu/LabelMatthew.png"}
--LabelSandwich = image{ "assets/Menu/LabelSandwich.png" }
-- END TEST

-- Level0 TestAssets
Level0Assets = group{quality=9.0}

-- Level1 (Format for 1 level with 3 images in this file)

Level1Assets = group{quality=9.2}

L1Phoneme1 = image{"assets/Level1/phoneme-1.png"}

L1Phoneme2 = image{"assets/Level1/phoneme-2.png"}

L1Phoneme3 = image{"assets/Level1/phoneme-3.png"}

L1Sound = sound{"assets/Level1/goalsound.wav"}



-- Level2
Level2Assets = group{quality=9.2}

L2Phoneme1 = image{"assets/Level2/phoneme-1.png"}

L2Phoneme2 = image{"assets/Level2/phoneme-2.png"}

L2Phoneme3 = image{"assets/Level2/phoneme-3.png"}

L2Sound = sound{"assets/Level2/goalsound.wav"}



-- Level3
Level3Assets = group{quality=9.2}

L3Phoneme1 = image{"assets/Level3/phoneme-1.png"}

L3Phoneme2 = image{"assets/Level3/phoneme-2.png"}

L3Phoneme3 = image{"assets/Level3/phoneme-3.png"}

L3Sound = sound{"assets/Level3/goalsound.wav"}
