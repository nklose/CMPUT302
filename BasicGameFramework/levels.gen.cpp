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

struct LevelSet Level1 = { {L1Phoneme1, L1Phoneme2, L1Phoneme3}, {L1Sound1, L1Sound2, L1Sound3}, {0}, L1GoalSound, 0, 0, 0};
struct LevelSet Level2 = { {L2Phoneme1, L2Phoneme2, L2Phoneme3}, {L2Sound1, L2Sound2, L2Sound3}, {0}, L2GoalSound, 0, 0, 0};
struct LevelSet Level3 = { {L3Phoneme1, L3Phoneme2, L3Phoneme3}, {L3Sound1, L3Sound2, L3Sound3}, {0}, L3GoalSound, 0, 0, 0};

struct LevelSet Levels[numLevels] = {Level1, Level2, Level3};

struct Group LevelAssets[numLevels] = {{Level1Assets}, {Level2Assets}, {Level3Assets}};

unsigned failedAttemptsWeight = 100;
unsigned hintsRequestedWeight = 100;
unsigned timeWeight = 40;
