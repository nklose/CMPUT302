from phoneme import *

"""
Some basic constant values
"""
# Static string for includes of levels.gen.cpp
LEVELS_GEN_TOP = '#include <sifteo.h>\n#include "levels.gen.h"\n#include "assets.gen.h"\n'
# Number of images per set
NUM_IN_SET = 3

def generate_files(levels):
	append_assetsLua(levels)
	generate_levelGenCpp(levels)

def append_assetsLua(levels):
	assetsLua = open('assets.lua', mode='a')		# append mode will append, not replace

def generate_levelGenCpp(levels):
	numLevels = len(levels)
	levelsGenCpp = open('levels.gen.cpp', mode='w') 	# write mode will replace entire file each time

	# Write the begining, constant portion with includes to the file
	levelsGenCpp.write(LEVELS_GEN_TOP + '\n')

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

if __name__ == "__main__":
	generate_levelGenCpp([1,2,3,4])
