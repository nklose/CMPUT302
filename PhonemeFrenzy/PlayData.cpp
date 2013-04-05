#include "PlayData.h"


PlayData::PlayData(){
	Hints = 0;
	Attempts = 0;
	Time = 0;
}

// getters and setters for object variables
unsigned PlayData :: getHints(){
    return Hints;
}

unsigned PlayData :: getAttempts(){
    return Attempts;
}

float PlayData :: getTime(){
    return Time;
}

void PlayData :: setTime(float seconds){
    Time = seconds;
}

// increment number of hints or attempts for one play
void PlayData :: incrementHints(){
    Hints++;
    LOG("***Hints Given: %d ***\n", Hints);
}

void PlayData :: incrementAttempts(){
    Attempts++;
    LOG("***Attempts made: %d ***\n", Attempts);
 } 
