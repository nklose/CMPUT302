-- Metadata

IconAssets = group{quality=9.95}
Icon = image{"assets/icon.png"}

-- Asset Group loaded initially to all cubes
BootAssets = group{quality=8.90}
LoadingBg = image{"assets/loading.png"}

-- Test AssetGroup
TestAssets = group{quality=9.05}
Title = image{"assets/playfield.png"}
SampleSound = sound{"assets/sounds/test.wav"}

-- Function to load a series of image frames
function frames(fmt, count, pingPong)
    t = {}
    for i = 1, count do
        t[1+#t] = string.format(fmt, i)
    end
    return t
end