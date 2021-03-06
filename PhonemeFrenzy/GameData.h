#ifndef GAMEDATA_H_
#define GAMEDATA_H_

#include "LevelData.h"
#include "levels.gen.h"
#include <sifteo.h>

class GameData {
public:
	GameData();
	//below here performed in GameData
	LevelData* getCurrentLevel();
	void incrementPlay();
	int getLevelCounter();
	void setLevelCounter(int i);

	// below here called from LevelData
	unsigned getHints();
	unsigned getAttempts();
	unsigned getTime();
	void addTime(unsigned seconds);
	void incrementHints();
	void incrementAttempts();
	void incrementLevel();
	void resetLevelCounter();
	void clear();
private:
	int currentLevelCounter;
	LevelData levelsArray[10];
};

#endif
