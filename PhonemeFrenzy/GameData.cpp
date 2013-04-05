#include "GameData.h"
#include "LevelData.h"

GameData::GameData(){
    static int NumLevels;
    int CurrentLevelCounter = 0;
    LevelData LevelsArray[10];
    //LevelData currentLevel = LevelsArray[CurrentLevelCounter];
}

void GameData :: saveGameData(){

	//todo: figure out how other games are storing their top scores
	//and implement the same thing for ours.

}

void GameData :: incrementPlay(){

	//so, this needs some logic to determine if I've reached the end of the level
	/*if (levelDataArray[currentLevel].getNumSets() == levelDataArray[currentLevel].getCurrentSet()){
		incrementLevel();
	}else{
		if (){
			levelDataArray[currentLevel].incrementSet();
		}
	}*/
	//int numberOfSets = levelDataArray[currentLevel].getNumSets();
	//int myCurrentSet = levelDataArray[currentLevel].getCurrentSet();
	//if(numberOfSets != myCurrentSet){
	//	levelDataArray[currentLevel].incrementSet();
	//}
	//levelDataArray[currentLevel].incrementSet();
}

void GameData :: incrementLevel(){
	CurrentLevelCounter++;
}

int GameData :: getCurrentLevel(){
	return CurrentLevelCounter;
}

// getters and setters for play data for the current level's current play
unsigned GameData :: getHints(){
	return LevelsArray[CurrentLevelCounter].getHints();
}

unsigned GameData :: getAttempts(){
	return LevelsArray[CurrentLevelCounter].getAttempts();
}

float GameData :: getTime(){
	return LevelsArray[CurrentLevelCounter].getTime();
}

void GameData :: setTime(float seconds){
	LevelsArray[CurrentLevelCounter].setTime(seconds);
}


// increment hints or attempts in the current level's current play
void GameData :: incrementHints(){
	LevelsArray[CurrentLevelCounter].incrementHints();
}

void GameData :: incrementAttempts(){
	LevelsArray[CurrentLevelCounter].incrementAttempts();
}
