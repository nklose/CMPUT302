#include "GameData.h"

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

void GameData :: incrementPlay(){
    levelsArray[currentLevelCounter].incrementPlay();
}

int GameData :: getLevelCounter(){
    return currentLevelCounter;
}

void GameData :: setLevelCounter(int i){
    currentLevelCounter = i;
}

void GameData :: incrementLevel(){
    currentLevelCounter++;
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

float GameData :: getTime(){
    return levelsArray[currentLevelCounter].getTime();
}

void GameData :: setTime(float seconds){
    levelsArray[currentLevelCounter].setTime(seconds);
}


// increment hints or attempts in the current level's current play
void GameData :: incrementHints(){
    levelsArray[currentLevelCounter].incrementHints();
}

void GameData :: incrementAttempts(){
    levelsArray[currentLevelCounter].incrementAttempts();
}


// reset hints and attempts in the current level's current play
void GameData :: reset(){
    levelsArray[currentLevelCounter].reset();
}
