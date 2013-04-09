/*
 * levels.gen.h
 *
 *  Created on: Mar 7, 2013
 *      Author: Andrew Neufeld
 */

#pragma once

#include "constants.h"

#define MAX_LEVELS 10	// maximum number of levels for the game
#define MAX_SETS 3		// maximum number of sets per level
#define NUM_PHONEMES 3	// number of phonemes in each set

/* for now assume the target/goal word info is stored at index 0 in the arrays */
// intention: 3 images/sounds per level. Currently 3 for example.
struct LevelSet {
	Sifteo::AssetImage phonemes[NUM_PHONEMES];			// Image options for cubes
	Sifteo::AssetAudio sounds[NUM_PHONEMES];			// Sound corresponding to cubes
	unsigned indexes[NUM_PHONEMES];					// index in vid[] that each image was placed
	Sifteo::AssetAudio goalsound;
};

struct Group {
	Sifteo::AssetGroup &grp;
};

extern struct LevelSet Levels[];

extern struct Group LevelAssets[];

// setsInLevel[0] will give the number of sets that the level 1 has, and so on for setsInLevel[1] for level2, etc.
extern int setsInLevel[];

extern unsigned hintRequestedWeight;

extern unsigned failedAttemptsWeight;

extern unsigned timeWeight;

extern const unsigned numLevels;
