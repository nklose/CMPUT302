#ifndef LEVELDATA_H_
#define LEVELDATA_H_

#include "PlayData.h"
#include "levels.gen.h"
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
	void setTime(unsigned seconds);
	void incrementHints();
	void incrementAttempts();
	void incrementPlay();
	void reset();

private:
	int numPlays;
	int currentPlayCounter;
	PlayData dataArray[10];
};


#endif
