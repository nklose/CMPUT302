/*
 * levels.gen.h
 *
 *  Created on: Mar 7, 2013
 *      Author: Andrew Neufeld
 */

#pragma once

/* for now assume the target/goal word info is stored at index 0 in the arrays */
// intention: 3 images/sounds per level. Currently 3 for example.
struct LevelSet {
	Sifteo::AssetImage phonemes[3];			// Image options for cubes
	Sifteo::AssetAudio sounds[3];			// Sound corresponding to cubes
	unsigned indexes[3];					// index in vid[] that each image was placed
	Sifteo::AssetAudio goalsound;
	//TODO: float is smaller than double.
	double time;
	//TODO: unsigned short is smaller than unsigned
	// unsigned short: 0 to 65535
	unsigned numHints;
	unsigned numAttempts;
};

struct Group {
	Sifteo::AssetGroup &grp;
};

extern const unsigned numLevels;
extern struct LevelSet Levels[];
extern struct Group LevelAssets[];

extern unsigned failedAttemptsWeight;
extern unsigned hintsRequestedWeight;
extern unsigned timeWeight;
