from phoneme import *
import subprocess
import platform
import os

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
# Number of image + phoneme per set
NUM_IN_SET = 3

# file paths needed for compilation of game
winbinpath = os.path.join('..', 'bins', 'windowsbin')
linuxbinpath = os.path.join('..', 'bins', 'linuxbin')
macbinpath = os.path.join('..', 'bins', 'macbin')
gamesourcepath = os.path.join('..', 'PhonemeFrenzy')

# direct filepaths to command shells for OS types
winshellpath = os.path.join(winbinpath, 'sifteo-sdk-shell.cmd')
linuxshellpath = os.path.join(linuxbinpath, 'sifteo-sdk-shell.sh')
macshellpath = os.path.join(macbinpath, 'sifteo-sdk-shell.command')

"""
	compile_elf(): based upon OS, runs the appropriate executables to compile the 
						PhonemeFrenzy game from source. To be called after
						generate_files.
"""
def compile_elf():
	# detect which OS to determine which executables to use
	ostype = platform.system()
	binpath = ""
	shellpath = ""

	if (ostype == 'Windows'):
		binpath = winbinpath
		shellpath = winshellpath
	elif (ostype == 'Linux'):
		binpath = linuxbinpath
		shellpath = linuxshellpath
	elif (ostype == 'Darwin'):	# This is Mac OSX
		binpath = macbinpath
		shellpath = macshellpath

	# somewhat magic function that will call make on the appropriate source folder
	makepath = os.path.join(binpath, "make")
	shell = subprocess.call(makepath + " -C "+ gamesourcepath, stdin=subprocess.PIPE, shell=True)

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

def generate_assetsLua(levels, path):
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
	goalPhoneme = ""
	# non-goal phonemes list
	nonGoalPhonemes = []	

	# separate goal phoneme from others for later ordering in writing
	for x in range(1,4):
		phoneme = set.phonemes[x-1]

		if (phoneme.goal):
			goalPhoneme = phoneme
		else:
			nonGoalPhonemes.append(phoneme)

	# write first phoneme, goalPhoneme, to list
	assetfile.write('L' + str(num) + 'Phoneme' + str(1) + ' = image{"' + goalPhoneme.image_path + '"}\n')
	assetfile.write('L' + str(num) + 'Sound' + str(1) + ' = sound{"' + goalPhoneme.sound_path + '", encode="pcm"}\n')

	# write LevelSet phonemes and sounds for cubes
	for x in range(1,3):
		phoneme = nonGoalPhonemes[x-1] 
		imgFilepath = phoneme.image_path
		soundFilepath = phoneme.sound_path

		assetfile.write('L' + str(num) + 'Phoneme' + str(x+1) + ' = image{"' + imgFilepath + '"}\n')
		assetfile.write('L' + str(num) + 'Sound' + str(x+1) + ' = sound{"' + soundFilepath + '", encode="pcm"}\n')

	# write goal sound
	assetfile.write('L' + str(num) + 'GoalSound = sound{"' + goalPhoneme.sound_path + '", encode="pcm"}\n\n')

def generate_levelGenCpp(game, path):
	levels = game.levels
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
	levelsGenCpp.write('unsigned hintsRequestedWeight = ' + str(game.hintsRequestedWeight) + ';\n')
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

def generate_game():
	game = Game()
	levels = []

	# create some levels with sets with phonemes within
	for x in range(0, 2):
		levels.append(Level())
		for y in range(0,2):
			level = levels[x]
			level.sets.append(Set())
			sett = level.sets[y]
			for z in range(0,3):
				ph = Phoneme()
				ph.name = "Test"
				ph.text = "testtxt"
				ph.image_path = "full/image_path" + str(z+1) + ".file"
				ph.sound_path = "full/sound_path" + str(z+1) + ".file"
				if z == 0:
					ph.goal = True
				else:
					ph.goal = False
				sett.add_phoneme(ph)

	game.levels = levels
	return game

# if run directly, this will generate test files to show it works
if __name__ == "__main__":	
	#game = generate_game()
	#generate_files(game, "")
	compile_elf()