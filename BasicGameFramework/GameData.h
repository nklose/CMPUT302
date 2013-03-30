#ifndef GAMEDATA_H_
#define GAMEDATA_H_

#include "LevelData.h"

class GameData {
public:
	GameData();
	void saveGameData();
private:
	int NumLevels;
	LevelData levelDataArray[];
};


#endif