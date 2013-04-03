/*
 * levels.gen.cpp
 *
 *  Created on: Mar 7, 2013
 *      Author: Andrew Neufeld
 */

#include <sifteo.h>
#include "levels.gen.h"
#include "assets.gen.h"

extern const unsigned numLevels;

struct LevelSet Level1 = { {L1Phoneme1, L1Phoneme2, L1Phoneme3}, {L1Sound1, L1Sound2, L1Sound3}, {0}, L1GoalSound, 0, 0, 0};
struct LevelSet Level2 = { {L2Phoneme1, L2Phoneme2, L2Phoneme3}, {L2Sound1, L2Sound2, L2Sound3}, {0}, L2GoalSound, 0, 0, 0};
struct LevelSet Level3 = { {L3Phoneme1, L3Phoneme2, L3Phoneme3}, {L3Sound1, L3Sound2, L3Sound3}, {0}, L3GoalSound, 0, 0, 0};

struct LevelSet Level4 = { {L4Phoneme1, L4Phoneme2, L4Phoneme3}, {L4Sound1, L4Sound2, L4Sound3}, {0}, L4GoalSound, 0, 0, 0};
struct LevelSet Level5 = { {L5Phoneme1, L5Phoneme2, L5Phoneme3}, {L5Sound1, L5Sound2, L5Sound3}, {0}, L5GoalSound, 0, 0, 0};
struct LevelSet Level6 = { {L6Phoneme1, L6Phoneme2, L6Phoneme3}, {L6Sound1, L6Sound2, L6Sound3}, {0}, L6GoalSound, 0, 0, 0};
struct LevelSet Level7 = { {L7Phoneme1, L7Phoneme2, L7Phoneme3}, {L7Sound1, L7Sound2, L7Sound3}, {0}, L7GoalSound, 0, 0, 0};
struct LevelSet Level8 = { {L8Phoneme1, L8Phoneme2, L8Phoneme3}, {L8Sound1, L8Sound2, L8Sound3}, {0}, L8GoalSound, 0, 0, 0};
struct LevelSet Level9 = { {L9Phoneme1, L9Phoneme2, L9Phoneme3}, {L9Sound1, L9Sound2, L9Sound3}, {0}, L9GoalSound, 0, 0, 0};
struct LevelSet Level10 = { {L10Phoneme1, L10Phoneme2, L10Phoneme3}, {L10Sound1, L10Sound2, L10Sound3}, {0}, L10GoalSound, 0, 0, 0};

struct LevelSet Levels[numLevels] = {Level1, Level2, Level3, Level4, Level5, Level6, Level7, Level8, Level9, Level10};

struct Group LevelAssets[numLevels] = {{Level1Assets}, {Level2Assets}, {Level3Assets}, {Level4Assets},
		{Level5Assets}, {Level6Assets}, {Level7Assets}, {Level8Assets}, {Level9Assets}, {Level10Assets}};

unsigned failedAttemptsWeight = 100;
unsigned hintsRequestedWeight = 100;
unsigned timeWeight = 40;
