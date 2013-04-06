#ifndef PLAYDATA_H_
#define PLAYDATA_H_

#include <sifteo.h>

class PlayData {
public:
	PlayData();
	unsigned getHints();
	unsigned getAttempts();
	float getTime();
	void setTime(float Seconds);
	void incrementHints();
	void incrementAttempts();
private:
	//String Goal;
	unsigned Hints;
	unsigned Attempts;
	float Time;
};


#endif