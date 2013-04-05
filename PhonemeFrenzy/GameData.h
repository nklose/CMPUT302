#ifndef GAMEDATA_H_
#define GAMEDATA_H_

#include "LevelData.h"
#include "levels.gen.h"
#include <sifteo.h>

class GameData {
public:
	GameData();
	//below here performed in GameData
	void saveGameData();
	int getCurrentLevel();
	void incrementPlay();

	// below here called from LevelData
	unsigned getHints();
	unsigned getAttempts();
	float getTime();
	void setTime(float seconds);
	void incrementHints();
	void incrementAttempts();
private:
	static int NumLevels;
	int CurrentLevelCounter;
	//LevelData currentLevel;
	
	void incrementLevel();
	LevelData LevelsArray[10];
};

#endif
