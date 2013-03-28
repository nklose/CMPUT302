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

using namespace Sifteo;

#define NUM_CUBES	4
#define NUM_IMAGES	(NUM_CUBES - 1)

extern AssetSlot MainSlot;

class Game {
public:
    Game() : running(false) {};

    void displayMenu();
    void init();
	void startRun();
    void run();
    void cleanup();

private:
    bool running;

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
void incrementAttempts();
void incrementHints();
void updateTime(SystemTime initTime, SystemTime finalTime);
bool evaluateResults();
void saveAll();
void loadAll();

#endif
