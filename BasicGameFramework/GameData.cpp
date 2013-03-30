#include "GameData.h"

GameData::GameData(){
	currentLevel = 0;
	//currentLevel = levelDataArray[currentLevelCounter];
	LOG("***Starting Level: %d ***\n", getCurrentLevel()); //commented out because of structure change
}

void GameData :: saveGameData(){

	//todo: figure out how other games are storing their top scores
	//and implement the same thing for ours.

}

void GameData :: incrementSet(){

	//so, this needs some logic to determine if I've reached the end of the level

}

void GameData :: incrementLevel(){
	currentLevel++;
	//currentLevel = levelDataArray[currentLevelCounter];
	LOG("***Starting Level: %d ***\n", getCurrentLevel()); //commented out because of structure change
}

int GameData :: getCurrentLevel(){
	return currentLevel;
}

void GameData :: setHints(int hints){
	levelDataArray[currentLevel].setHints(hints);
}

void GameData :: setAttempts(int attempts){
	levelDataArray[currentLevel].setAttempts(attempts);
}

void GameData :: setSeconds(int seconds){
	levelDataArray[currentLevel].setSeconds(seconds);
}

int GameData :: getNumHints(){
	return levelDataArray[currentLevel].getNumHints();
}

int GameData :: getNumAttempts(){
	return levelDataArray[currentLevel].getNumAttempts();
}

int GameData :: getNumSeconds(){
	return levelDataArray[currentLevel].getNumSeconds();
}