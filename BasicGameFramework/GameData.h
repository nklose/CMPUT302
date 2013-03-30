#ifndef GAMEDATA_H_
#define GAMEDATA_H_

#include "LevelData.h"
#include "levels.gen.h"
#include <sifteo.h>

class GameData {
public:
	GameData();
	void saveGameData();//below here performed in GameData
	int getCurrentLevel();
	void incrementSet();// below here called from LevelData
	void setHints(int hints);
	void setAttempts(int hints);
	void setSeconds(int hints);
	int getNumHints();
	int getNumAttempts();
	int getNumSeconds();
	void incrementHints();
	void incrementAttempts();
private:
	static int NumLevels;
	int currentLevel;
	void incrementLevel();
	LevelData levelDataArray[numLevels];//cannot have variable length of non-POD element type
	//LevelData currentLevel;
};

#endif