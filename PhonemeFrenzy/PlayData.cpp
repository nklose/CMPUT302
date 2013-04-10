#include "PlayData.h"


PlayData::PlayData(){
    unsigned hints = 0;
    unsigned attempts = 0;
    unsigned time = 0;
}

// getters and setters for object variables
unsigned PlayData :: getHints(){
    return hints;
}

unsigned PlayData :: getAttempts(){
    return attempts;
}

unsigned PlayData :: getTime(){
    return time;
}

void PlayData :: setTime(unsigned seconds){
    time = seconds;
}

// increment number of hints or attempts for one play
void PlayData :: incrementHints(){
    hints++;
}

void PlayData :: incrementAttempts(){
    attempts++;
}

// reset hints and attempts to zero
void PlayData :: reset(){
    hints = 0;
    attempts = 0;
}
