#include "LevelData.h"
#include "levels.gen.h"

LevelData::LevelData(){
    numPlays = 1;
    currentPlayCounter = 0;
    // this is the array of 10 possible plays per level
    PlayData dataArray[10];
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

PlayData LevelData :: getCurrentPlay(){
    return dataArray[currentPlayCounter];
}

// getters and setters for specific play data for the current play
unsigned LevelData :: getHints(){
    return dataArray[currentPlayCounter].getHints();
}

unsigned LevelData :: getAttempts(){
    return dataArray[currentPlayCounter].getAttempts();
}

float LevelData :: getTime(){
    return dataArray[currentPlayCounter].getTime();
}

void LevelData :: setTime(float seconds){
    dataArray[currentPlayCounter].setTime(seconds);
}

// Increment number of hints or attempts in the current play number 
// of this level
void LevelData :: incrementHints(){
    dataArray[currentPlayCounter].incrementHints();
}

void LevelData :: incrementAttempts(){
    dataArray[currentPlayCounter].incrementAttempts();
}

// Increments the currentPlayCounter and the numPlays.
void LevelData :: incrementPlay(){
    if (currentPlayCounter < 10){
	currentPlayCounter++;
	numPlays++;
    } else {
	LOG("---Play Overflow [you fail]---\n");
    }
}

// reset hints and attempts of the current level's current play to zero
void LevelData :: reset(){
    dataArray[currentPlayCounter].reset();
}
