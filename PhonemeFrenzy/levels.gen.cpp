// THIS FILE IS GENERATED BY file_customizer.py DURING COMPILATION, DO NOT EDIT MANUALLY WITHOUT GREAT CAUTION

#include <sifteo.h>
#include "levels.gen.h"
#include "assets.gen.h"

const unsigned numLevels = 2;
const unsigned numSets = 3;

struct LevelSet Level1 = { {L1Phoneme1, L1Phoneme2, L1Phoneme3}, {L1Sound1, L1Sound2, L1Sound3}, {0}, L1GoalSound};

struct LevelSet Level2 = { {L2Phoneme1, L2Phoneme2, L2Phoneme3}, {L2Sound1, L2Sound2, L2Sound3}, {0}, L2GoalSound};

struct LevelSet Level3 = { {L3Phoneme1, L3Phoneme2, L3Phoneme3}, {L3Sound1, L3Sound2, L3Sound3}, {0}, L3GoalSound};

struct LevelSet Levels[numSets] = {Level1, Level2, Level3};

struct Group LevelAssets[numSets] = {{Level1Assets}, {Level2Assets}, {Level3Assets}};

int setsInLevel[numLevels] = {2, 1};

unsigned failedAttemptsWeight = 50;
unsigned hintsRequestedWeight = 26;
unsigned timeWeight = 87;

