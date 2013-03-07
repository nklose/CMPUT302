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
#include "assets.gen.h"

using namespace Sifteo;

#define NUM_CUBES     3

extern AssetSlot MainSlot;

class Game {
public:
    Game() : running(true) {};

    void title();
    void init();
    void run();
    void cleanup();

    void draw();

private:
    bool running;

    // Event handlers
    void onNeighborAdd(unsigned c0, unsigned s0, unsigned c1, unsigned s1);
    void onNeighborRemove(unsigned c0, unsigned s0, unsigned c1, unsigned s1);
    void onAccelChange(unsigned id);
    void onShake(unsigned id);
    void onTilt(unsigned id, Byte3 tiltInfo);
    void onRestart();
};

#endif
