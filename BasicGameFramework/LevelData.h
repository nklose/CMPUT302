#ifndef LEVELDATA_H_
#define LEVELDATA_H_

#include "SetData.h"

class LevelData {
public:
	LevelData(int numSets);
	int getNumSets();
private:
	int NumSets;
	SetData setDataArray[];
};


#endif