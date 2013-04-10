#include "LevelData.h"
#include "levels.gen.h"

LevelData::LevelData(){
    numPlays = 1;
    currentPlayCounter = 0;
    unsigned totalAttempts = 0;
    unsigned totalHints = 0;
    unsigned totalTime = 0;
}

// getters LevelData Properties
int LevelData :: getPlayCounter(){
    return currentPlayCounter;
}

void LevelData :: setPlayCounter(int i){
    currentPlayCounter = i;
}

int LevelData :: getNumPlays(){
    return numPlays;
}

// getters and setters for specific play data for the current play
unsigned LevelData :: getHints(){
    return totalHints;
}

unsigned LevelData :: getAttempts(){
    return totalAttempts;
}

unsigned LevelData :: getTime(){
    return totalTime;
}

void LevelData :: addTime(unsigned seconds){
    totalTime = totalTime + seconds;
}

void LevelData :: incrementHints(){
    totalHints++;
}

void LevelData :: incrementAttempts(){
    totalAttempts++;
}
