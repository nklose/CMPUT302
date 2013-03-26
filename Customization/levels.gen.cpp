#include <sifteo.h>
#include "levels.gen.h"
#include "assets.gen.h"

const unsigned numLevels = 4;

struct Level Level1 = { {L1Phoneme1, L1Phoneme2, L1Phoneme3, }, {L1Sound1L1Sound2L1Sound3}, {0}, L1GoalSound, 0, 0, 0};

struct Level Level2 = { {L2Phoneme1, L2Phoneme2, L2Phoneme3, }, {L2Sound1, L2Sound2L2Sound3}, {0}, L2GoalSound, 0, 0, 0};

struct Level Level3 = { {L3Phoneme1, L3Phoneme2, L3Phoneme3, }, {L3Sound1, L3Sound2, L3Sound3}, {0}, L3GoalSound, 0, 0, 0};

struct Level Level4 = { {L4Phoneme1, L4Phoneme2, L4Phoneme3, }, {L4Sound1, L4Sound2, L4Sound3, }, {0}, L4GoalSound, 0, 0, 0};

struct LevelSet Levels[numLevels] = {Level1, Level2, Level3, Level4};

struct Group LevelAssets[numLevels] = {{Level1Assets}, {Level2Assets}, {Level3Assets}, {Level4Assets}};

