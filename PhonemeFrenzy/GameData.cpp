#include "GameData.h"
#include "levels.gen.h"

/*
 * GameData holds functions that call LevelData, which in turn calls PlayData.
 * These functions include getters for Time, Hints, and Attempts, setters for Time,
 * and incrementers for Hints and Attempts.
 * GameData keeps track of the LevelsArray, current level, and incrementing levels,
 * as well as the saving of results into PlayData objects.
 */
GameData::GameData(){
    currentLevelCounter = 0;
    LevelData levelsArray[10];
}

int GameData :: getLevelCounter(){
    return currentLevelCounter;
}

void GameData :: setLevelCounter(int i){
    currentLevelCounter = i;
}

void GameData :: incrementLevel(){
    if (currentLevelCounter < numLevels){
	currentLevelCounter++;
    }
}

LevelData* GameData :: getCurrentLevel(){
    return &levelsArray[currentLevelCounter];
}

// getters and setters for play data for the current level's current play
unsigned GameData :: getHints(){
    return levelsArray[currentLevelCounter].getHints();
}

unsigned GameData :: getAttempts(){
    return levelsArray[currentLevelCounter].getAttempts();
}

unsigned GameData :: getTime(){
    return levelsArray[currentLevelCounter].getTime();
}

void GameData :: addTime(unsigned seconds){
    levelsArray[currentLevelCounter].addTime(seconds);
}

// increment hints or attempts in the current level's current play
void GameData :: incrementHints(){
    levelsArray[currentLevelCounter].incrementHints();
}

void GameData :: incrementAttempts(){
    levelsArray[currentLevelCounter].incrementAttempts();
}

// reset the level counter at the end of a playthrough
void GameData :: resetLevelCounter(){
    currentLevelCounter = 0;
}

// completely clear the GameData object, and set to 0
void GameData :: clear()
{
	// clear every level
	for (int i = 0; i < numLevels; i++)
	{
		setLevelCounter(i);
		getCurrentLevel()->clear();
	}
	resetLevelCounter();
}
