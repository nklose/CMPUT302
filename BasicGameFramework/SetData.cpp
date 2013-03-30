#include "SetData.h"


SetData::SetData(){
	//Goal = goal;
	Hints = 0;
	Attempts = 0;
	Seconds = 0;
}

//getters and setters for object variables
int SetData :: getNumHints(){
	return Hints;
}
void SetData :: setHints(int hints){
	Hints = hints;
 }
int SetData :: getNumAttempts(){
	return Attempts;
}
 void SetData :: setAttempts(int attempts){
	 Attempts = attempts;
 } 
int SetData :: getNumSeconds(){
	return Seconds;
}
 void SetData :: setSeconds(int seconds){
	 Seconds = seconds;
 }
 /*String SetData :: GetGoal(){
	 return Goal;
 }*/
 void SetData :: incrementHints(){
	Hints++;
	LOG("***Hints Given: %d ***\n", Hints); //commented out because of structure change
 }

 void SetData :: incrementAttempts(){
	 Attempts++;
	 LOG("***Arrempts made: %d ***\n", Attempts); //commented out because of structure change
 } 