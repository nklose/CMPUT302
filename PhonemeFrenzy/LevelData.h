#ifndef LEVELDATA_H_
#define LEVELDATA_H_

#include "LevelData.h"
#include "PlayData.h"
#include <sifteo.h>

class LevelData {
public:
	LevelData();
	//below here performed in LevelData
	int getNumPlays();
	PlayData getCurrentPlay();

	//below here called from PlayData
	unsigned getHints();
	unsigned getAttempts();
	float getTime();
	void setTime(float seconds);
	void incrementHints();
	void incrementAttempts();
	void incrementPlay();

private:
	static int NumPlays;
	int CurrentPlayCounter;
	PlayData DataArray[5];//cannot have variable length of non-POD element type
};


#endif