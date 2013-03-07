/*
 * game.cpp
 *
 *  Created on: Mar 6, 2013
 *      Author: Andrew Neufeld
 */

/*
 * Sifteo SDK Example.
 */

#include <sifteo.h>
#include "game.h"
using namespace Sifteo;

// GLOBALS
static VideoBuffer vid[NUM_CUBES];
static TiltShakeRecognizer motion[NUM_CUBES];
CubeSet allCubes(0,NUM_CUBES);
MyLoader loader(allCubes, MainSlot, vid);

void Game::title()
{
	loader.load(TestAssets, MainSlot); // will load(Level1Assets, Mainslot
}

void Game::init()
{
    for (unsigned i = 0; i < NUM_CUBES; i++)
        vid[i].initMode(BG0);


    Events::neighborAdd.set(&Game::onNeighborAdd, this);
    Events::neighborRemove.set(&Game::onNeighborRemove, this);
    Events::cubeAccelChange.set(&Game::onAccelChange, this);
    Events::gameMenu.set(&Game::onRestart, this, "« Restart »");
}

void Game::cleanup()
{
    Events::neighborAdd.unset();
    Events::neighborRemove.unset();
    Events::gameMenu.unset();
}

void Game::onNeighborAdd(unsigned c0, unsigned s0, unsigned c1, unsigned s1)
{
    if (c0 >= NUM_CUBES || c1 >= NUM_CUBES)
        return;

}

void Game::onNeighborRemove(unsigned c0, unsigned s0, unsigned c1, unsigned s1)
{
    if (c0 >= NUM_CUBES || c1 >= NUM_CUBES)
        return;

}

/* Called upon the event of a cube's acceleration changing measurably */
void Game::onAccelChange(unsigned id)
{
	unsigned changeFlags = motion[id].update();

	if (changeFlags) {
		// Tilt/shake changed
		static Byte3 prevTilt = {0, 0, 0};

		Byte3 tilt = motion[id].tilt;
		if (tilt.x != prevTilt.x || tilt.y != prevTilt.y || tilt.z != prevTilt.z)
			onTilt(id, tilt);

		bool shake = motion[id].shake;
		if (shake)
			onShake(id);

		prevTilt = tilt;
	}
}

/* Called upon the event of a cube being shaken. This is a sub-call of onAccelChange. */
void Game::onShake(unsigned id)
{
	LOG("Cube shaken: %02x\n", id);
}

/* Called upon the event of a cube being tilted. This is a sub-call of onAccelChange. */
void Game::onTilt(unsigned id, Byte3 tiltInfo)
{
	LOG("Cube %02X tilted: x = %02x, y = %02x, z = %02x\n", id, tiltInfo.x, tiltInfo.y, tiltInfo.z);
}

void Game::onRestart()
{
    running = false;
}

void Game::draw()
{
    for (unsigned i = 0; i < NUM_CUBES; i++)
	{

    }
}

void Game::run()
{

    while (running)
	{
    	for (unsigned i = 0; i < NUM_CUBES; i++)
    	{
    		vid[i].bg0.image(vec(0,0), Title);
    	}
        draw();
        System::paint();
    }
}
