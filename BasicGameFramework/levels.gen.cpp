/*
 * levels.gen.cpp
 *
 *  Created on: Mar 7, 2013
 *      Author: Andrew Neufeld
 */

#include <sifteo.h>
#include "levels.gen.h"
#include "assets.gen.h"

const unsigned numLevels = 3;

struct Level Level1 = { 3, {L1Phoneme1, L1Phoneme2, L1Phoneme3}, L1Sound, 0};
struct Level Level2 = { 3, {L2Phoneme1, L2Phoneme2, L2Phoneme3}, L2Sound, 0};
struct Level Level3 = { 3, {L3Phoneme1, L3Phoneme2, L3Phoneme3}, L3Sound, 0};

struct Level Levels[numLevels] = {Level1, Level2, Level3};

struct Group LevelAssets[numLevels] = {{Level1Assets}, {Level2Assets}, {Level3Assets}};
