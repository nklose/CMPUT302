#include "GameData.h"
#include "LevelData.h"

/*
 * GameData holds functions that call LevelData, which in turn calls PlayData.
 * These functions include getters for Time, Hints, and Attempts, setters for Time,
 * and incrementers for Hints and Attempts.
 * GameData keeps track of the LevelsArray, current level, and incrementing levels,
 * as well as the saving of results into PlayData objects.
 */
GameData::GameData(){
    // static int NumLevels;
    int CurrentLevelCounter = 0;
    LevelData LevelsArray[10];
    LevelData currentLevel = LevelsArray[CurrentLevelCounter];
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
    //    levelDataArray[currentLevel].incrementSet();
    //}
    //levelDataArray[currentLevel].incrementSet();
}

void GameData :: incrementLevel(){
    CurrentLevelCounter++;
}

PlayData* GameData :: getCurrentLevel(){
    return LevelsArray[CurrentLevelCounter].getCurrentLevel();
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


// reset hints and attempts in the current level's current play
void GameData :: reset(){
    LevelsArray[CurrentLevelCounter].reset();
}
