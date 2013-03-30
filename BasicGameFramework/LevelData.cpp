#include "Data.h"

LevelData::LevelData(int numSets){
	NumSets = numSets;
	SetDataArray[numSets] setDataArray;
}

//getters and setters for LevelData Properties
int LevelData :: getNumSets(){
	return NumSets;
}