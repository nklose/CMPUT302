#ifndef LEVELDATA_H_
#define LEVELDATA_H_

#include "levels.gen.h"
#include <sifteo.h>

class LevelData {
public:
	LevelData();
	//below here performed in LevelData
	int getNumPlays();
	int getPlayCounter();
	void setPlayCounter(int i);

	//below here called from PlayData
	unsigned getHints();
	unsigned getAttempts();
	unsigned getTime();
	void addTime(unsigned seconds);
	void incrementHints();
	void incrementAttempts();

private:
	int numPlays;
	int currentPlayCounter;
	unsigned totalAttempts;
	unsigned totalHints;
	unsigned totalTime;
};


#endif
