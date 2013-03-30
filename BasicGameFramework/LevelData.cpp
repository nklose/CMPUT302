#include "LevelData.h"

LevelData::LevelData(){
	currentSet = 0;
	//currentSet = setDataArray[currentSetCounter];
	LOG("***Starting Set: %d ***\n", getCurrentSet()); //commented out because of structure change
}

//getters and setters for LevelData Properties
int LevelData :: getNumSets(){
	return NumSets;
}

void LevelData :: incrementSet(){
	currentSet++;
	//currentSet = setDataArray[currentSetCounter];
	LOG("***Starting Set: %d ***\n", getCurrentSet()); //commented out because of structure change
}

int LevelData :: getCurrentSet(){
	return currentSet;
}

void LevelData :: setHints(int hints){
	setDataArray[currentSet].setHints(hints);
}

void LevelData :: setAttempts(int attempts){
	setDataArray[currentSet].setAttempts(attempts);
}

int LevelData :: getNumHints(){
	return setDataArray[currentSet].getNumHints();
}

int LevelData :: getNumAttempts(){
	return setDataArray[currentSet].getNumAttempts();
}

int LevelData :: getNumSeconds(){
	return setDataArray[currentSet].getNumSeconds();
}
