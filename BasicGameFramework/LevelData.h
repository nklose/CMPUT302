#ifndef LEVELDATA_H_
#define LEVELDATA_H_

#include "SetData.h"
#include <sifteo.h>

class LevelData {
public:
	LevelData();//below here performed in LevelData
	int getNumSets();
	void incrementSet();
	int getCurrentSet();//below here called from SetData
	void setHints(int hints);
	void setAttempts(int attempts);
	void setSeconds(int seconds);
	int getNumHints();
	int getNumAttempts();
	int getNumSeconds();
private:
	static int NumSets;
	int currentSet;
	SetData setDataArray[3];//cannot have variable length of non-POD element type
	//SetData currentSet;
};


#endif