from phoneme import *

"""
Some basic constant values
"""
# Static string for includes of levels.gen.cpp
LEVELS_GEN_CPP_TOP = '#include <sifteo.h>\n#include "levels.gen.h"\n#include "assets.gen.h"\n'
# Static string that contains the static assets within assets.lua
ASSETS_LUA_TOP = (
		'-- Metadata\nIconAssets = group{quality=9.95}\nIcon = image{"assets/icon.png"}\n\n'
		'-- Asset Group loaded initially to all cubes\nBootAssets = group{quality=8.90}\n'
		'LoadingBg = image{"assets/loading.png"}\nBravo = image{"assets/bravo.png"}\n'
		'Title = image{"assets/welcomeTitle.png"}\nGrid = image{"assets/playfield.png", pinned=1}\n'
		'Speaker = image{"assets/speaker.png"}\n\n-- Menu Assets\nMenuAssetGrp = group{quality=9.05}\n'
		'BgTile = image{ "assets/Menu/bg.png", pinned=1 }\nGrid = image{"assets/playfield.png", pinned=1}\n'
		'IconSandwich = image{ "assets/Menu/IconSandwich.png" }\nIconChroma = image{ "assets/Menu/IconChroma.png" }\n'
		'Tip0 = image{ "assets/Menu/Tip0.png" }\nTip1 = image{ "assets/Menu/Tip1.png" }\n'
		'Footer = image{ "assets/Menu/Footer.png" }\nLabelEmpty = image{ "assets/Menu/LabelEmpty.png" }\n'
		'LabelUser1 = image{"assets/Menu/LabelAdrian.png"}\nLabelUser2 = image{"assets/Menu/LabelMatthew.png"}\n'
	)
# Number of images per set
NUM_IN_SET = 3

"""
	generate_files(levels, path): 	- levels is a list of Level() objects containing game data
									- path is a string with a file path to the target directory
											for the file creation

	This function will create the "assets.lua" file and the "levels.gen.cpp" generate_files
		that are used for the custom game data of the Sifteos Phoneme Awareness game
"""
def generate_files(game, path):
	# handle each file generation
	generate_assetsLua(game.levels, path)
	generate_levelGenCpp(game, path)

def generate_assetsLua(levels):
	# get the overall number of LevelSets
	numLevels = 0
	for x in range(0, len(levels)):
		level = levels[x]
		numLevels += len(level.sets)

	# keep track of the overall LevelSet num
	levelNum = 0

	assetsLua = open(path + 'assets.lua', mode='w')		# write mode will replace any existing file
	assetsLua.write(ASSETS_LUA_TOP)

	# write levels
	for i in range(0, numLevels):
		level = levels[x]
		for j in range(0, len(level.sets)):
			levelNum += 1
			set = level.sets[j]
			generate_levelAssets(assetsLua, set, levelNum)	

	# and remember to close the file
	assetsLua.close()

def generate_levelAssets(assetfile, set, num):
	# write intro comment and lua group descriptor
	assetfile.write('\n-- Level' + str(num) + ' asset group\n')
	assetfile.write('Level' + str(num) + 'Assets = group{quality=10}\n')

	# filepath to sound for goal filepath
	goalFilepath = "" 

	# write LevelSet phonemes and sounds for cubes
	for x in range(1,4):
		phoneme = set.phonemes[x-1]
		imgFilepath = phoneme.image_path
		soundFilepath = phoneme.sound_path

		# if goal phoneme then get filepath for GoalSound write below
		if phoneme.goal == True:
			goalFilepath = soundFilepath

		assetfile.write('L' + str(num) + 'Phoneme' + str(x) + ' = image{"' + imgFilepath + '"}\n')
		assetfile.write('L' + str(num) + 'Sound' + str(x) + ' = sound{"' + soundFilepath + '", encode="pcm"}\n')

	# write goal sound 
	assetfile.write('L' + str(num) + 'GoalSound = sound{"' + goalFilepath + '", encode="pcm"}\n\n')

def generate_levelGenCpp(levels):
	# get the overall number of LevelSets
	numLevels = 0
	for x in range(0, len(levels)):
		level = levels[x]
		numLevels += len(level.sets)

	# open the file!
	levelsGenCpp = open(path + 'levels.gen.cpp', mode='w') 	# write mode will replace entire file each time

	# Write the begining, constant portion with includes to the file
	levelsGenCpp.write(LEVELS_GEN_CPP_TOP + '\n')

	# write the constant numLevels var
	levelsGenCpp.write('const unsigned numLevels = ' + str(numLevels) + ';\n\n')

	# write out the struct LevelSets
	for x in range(1, numLevels+1):
		levelsGenCpp.write(create_level_line(x) + '\n')

	# write out the LevelSet Levels array var and it's initializer
	levelsGenCpp.write('struct LevelSet Levels[numLevels] = {')
	for x in range(1,numLevels+1):
		levelsGenCpp.write('Level' + str(x))	
		# write the commas only for non-last items
		if x < numLevels:
			levelsGenCpp.write(", ")	
	levelsGenCpp.write('};\n\n')

	# write out the struct Group for level assets
	levelsGenCpp.write('struct Group LevelAssets[numLevels] = {')
	for x in range(1, numLevels+1):
		levelsGenCpp.write('{Level' + str(x) + 'Assets}')
		if x < numLevels:
			levelsGenCpp.write(", ")	
	levelsGenCpp.write('};\n\n')

	# add the initializers for slider weights for difficulty scaling
	levelsGenCpp.write('unsigned failedAttemptsWeight = ' + str(game.failedAttemptsWeight) + ';\n')
	levelsGenCpp.write('unsigned hintsAttemptsWeight = ' + str(game.hintsAttemptsWeight) + ';\n')
	levelsGenCpp.write('unsigned timeWeight = ' + str(game.timeWeight) + ';\n\n')

	# and remember to close the file!
	levelsGenCpp.close()

def create_level_line(num):
	line = "struct Level Level" + str(num) + " = { "
	
	# add the static initializer for Level.phonemes[] "{L1Phoneme1, L1Phoneme2, etc" etc
	line += '{'
	for x in range (1, NUM_IN_SET+1):
		line += create_asset_token(num, x, 'Phoneme')
		line += ', '
	line += '}, '

	# add the static initializer for Level.sounds[] "{L1Sound, L1Sound, etc" etc
	line += '{'
	for x in range (1, NUM_IN_SET+1):
		line += create_asset_token(num, x, 'Sound')
		if x < num:
			line += ', '
	line += '}, '

	# add the initializers for indexes, goalsound, time, numHints, and numAttempts
	line += '{0}, ' + "L" + str(num) + 'GoalSound, 0, 0, 0};\n'

	return line

def create_asset_token(levelNum, phonemeNum, assetType):
	return "L" + str(levelNum) + assetType + str(phonemeNum)
