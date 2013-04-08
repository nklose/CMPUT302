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
	int getPlayCounter();
	void setPlayCounter(int i);

	//below here called from PlayData
	unsigned getHints();
	unsigned getAttempts();
	float getTime();
	void setTime(float seconds);
	void incrementHints();
	void incrementAttempts();
	void incrementPlay();
	void reset();

private:
	static int numPlays;
	int currentPlayCounter;
	PlayData *dataArray = new PlayData[1];
};


#endif