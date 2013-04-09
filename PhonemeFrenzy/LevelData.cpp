#include "LevelData.h"

LevelData::LevelData(){
    numPlays = 1;
    currentPlayCounter = 0;
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
// Then it moves the dataArray data to a tempArray, reallocates dataArray
// as a bigger array, and transfers all original data back from tempArray.
void LevelData :: incrementPlay(){
    currentPlayCounter++;
    numPlays++;
    /*PlayData* tempArray = dataArray;
    dataArray = new PlayData[numPlays];
    for (int i = 0; i < numPlays; i++){
	dataArray[i] = tempArray[i];
    }
    delete [] tempArray;
    */
}

// reset hints and attempts of the current level's current play to zero
void LevelData :: reset(){
    dataArray[currentPlayCounter].reset();
}
