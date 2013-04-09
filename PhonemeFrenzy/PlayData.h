#ifndef PLAYDATA_H_
#define PLAYDATA_H_

#include <sifteo.h>

class PlayData {
public:
	PlayData();
	unsigned getHints();
	unsigned getAttempts();
	unsigned getTime();
	void setTime(float Seconds);
	void incrementHints();
	void incrementAttempts();
	void reset();
private:
	unsigned hints;
	unsigned attempts;
	unsigned time;
};


#endif