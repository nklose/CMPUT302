/*
 * levels.gen.h
 *
 *  Created on: Mar 7, 2013
 *      Author: Andrew Neufeld
 */

#ifndef LEVELS_GEN_H_
#define LEVELS_GEN_H_

/* for now assume the target/goal word info is stored at index 0 in the arrays */
// intention: 4 images/sounds per level. Currently 3 for example.
struct Level {
	Sifteo::AssetImage phonemes[3];			// Image options for cubes
	Sifteo::AssetAudio sounds[3];			// Sound corresponding to cubes
	unsigned indexes[3];					// index in vid[] that each image was placed
	Sifteo::AssetAudio goalsound;
};

struct Group {
	Sifteo::AssetGroup &grp;
};

extern const unsigned numLevels;

extern struct Level Levels[];

extern struct Group LevelAssets[];

#endif /* LEVELS_GEN_H_ */
