/*
 * levels.gen.h
 *
 *  Created on: Mar 7, 2013
 *      Author: Andrew Neufeld
 */

#ifndef LEVELS_GEN_H_
#define LEVELS_GEN_H_

/* for now assume phoneme[0] is the goal word... */
struct Level {
	unsigned num;
	Sifteo::AssetImage phonemes[3];	// List of images
	Sifteo::AssetAudio sound;			// goal sound
	unsigned goalIndex;				// index in phonemes[] of the goal image
};

struct Group {
	Sifteo::AssetGroup &grp;
};

extern const unsigned numLevels;

extern struct Level Levels[];

extern struct Group LevelAssets[];

#endif /* LEVELS_GEN_H_ */
