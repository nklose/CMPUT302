/*
 * game.h
 *
 *  Created on: Mar 6, 2013
 *      Author: Andrew Neufeld
 */

#ifndef GAME_H_
#define GAME_H_

#include <sifteo.h>
#include "loader.h"
#include "levels.gen.h"
#include "assets.gen.h"
#include "GameData.h"

using namespace Sifteo;

#define NUM_IMAGES	(NUM_PHONEMES + 0)
#define NUM_CUBES	(NUM_IMAGES + 1)

extern AssetSlot MainSlot;

class Game {
public:
    Game() : running(false) {};

    void displayMenu();
    void init();
	void startRun();
    void run();
    void cleanup();
    void saveToStoredObject();
    void updateTime(SystemTime initTime, SystemTime finalTime);

private:
    bool running;
	GameData gameData;

    // Event handlers
    void onAccelChange(unsigned id);
    void onShake(unsigned id);
    void onTilt(unsigned id, Byte3 tiltInfo);
    void onTouch(unsigned id);
    void onRestart();
};

// utility funcs

void wait(float n);
void shuffleLoad();
void getSetIndex();
bool evaluateResults();
void loadStoredObject();

#endif
