#include "LevelData.h"
#include "PlayData.h"

LevelData::LevelData(){
    static int NumPlays;
    int CurrentPlayCounter = 0;
    // hardcoded 5 plays per level
    PlayData DataArray[5];
}

// getters and setters for LevelData Properties
int LevelData :: getNumPlays(){
    return NumPlays;
}

PlayData LevelData :: getCurrentPlay(){
    return DataArray[CurrentPlayCounter];
}

// getters and setters for specific play data for the current play
unsigned LevelData :: getHints(){
    return DataArray[CurrentPlayCounter].getHints();
}

unsigned LevelData :: getAttempts(){
    return DataArray[CurrentPlayCounter].getAttempts();
}

float LevelData :: getTime(){
    return DataArray[CurrentPlayCounter].getTime();
}

void LevelData :: setTime(float seconds){
    DataArray[CurrentPlayCounter].setTime(seconds);
}

// Increment number of hints or attempts in the specficied play number 
// of this level
void LevelData :: incrementHints(){
    DataArray[CurrentPlayCounter].incrementHints();
}

void LevelData :: incrementAttempts(){
    DataArray[CurrentPlayCounter].incrementAttempts();
}

// Increment the current play in the DataArray of this level
// TODO: Better not fail an infinite number of times.
void LevelData :: incrementPlay(){
    CurrentPlayCounter++;
}
