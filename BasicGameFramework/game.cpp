/*
 * game.cpp
 *
 *  Created on: Mar 6, 2013
 *      Author: Andrew Neufeld
 */

#include <sifteo.h>
#include "game.h"
#include "assets.gen.h"
#include "levels.gen.h"
using namespace Sifteo;

// Globals
TiltShakeRecognizer motion[NUM_CUBES];
VideoBuffer vid[NUM_CUBES];
CubeSet allCubes(0,NUM_CUBES);
MyLoader loader(allCubes, MainSlot, vid);
AudioChannel audio(0);
struct Level *lvl;

void Game::title()
{
	/* Hey Jake, turns out you won't need to load any AssetGroups in the title screen here
	 * 		because of how I handled the multiple levels within the main gameloop below.
	 */
}

void Game::init()
{
	// set up the mode as well as attach the TiltShakeRecognizer
    for (unsigned i = 0; i < NUM_CUBES; i++)
    {
        vid[i].initMode(BG0);
        motion[i].attach(i);
    }

    Events::cubeAccelChange.set(&Game::onAccelChange, this);
}

/* Unset some event handlers */
void Game::cleanup()
{
    Events::neighborAdd.unset();
    Events::neighborRemove.unset();
    Events::cubeTouch.unset();
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

/* Called upon the event of a cube being shaken. In this game this repeats the goal sound */
void Game::onShake(unsigned id)
{
	LOG("Cube shaken: %02x\n", id);
	// If shaken strongly this may cause multiple plays...
	//		It may need a timer of some sort to prevent this
	audio.play(lvl->sound);
}

/* Called upon the event of a cube being tilted. This is a sub-call of onAccelChange. */
void Game::onTilt(unsigned id, Byte3 tiltInfo)
{
	LOG("Cube %02X tilted: x = %02x, y = %02x, z = %02x\n", id, tiltInfo.x, tiltInfo.y, tiltInfo.z);
}

/* Called upon the event of a cube being touched */
void Game::onTouch(unsigned id)
{
	/* ensure only begin touch triggers end of level */
	static bool touched[NUM_CUBES] = {false, false, false};

	// ensure it is the goal word cube
	if (id != lvl->goalIndex)
		return;

	if (!touched[id])
		running = false;
	touched[id] = !touched[id];
	LOG("Cube touched: %u\n", id);
}

/* Main game loop over defined levels */
void Game::run()
{
    for (unsigned i = 0; i < numLevels; i++)
    {
    	loader.load(LevelAssets[i].grp, MainSlot);
    	lvl = &Levels[i];
    	running = true;

		// load images onto cubes
    	shuffleLoad();
    	wait(1);

    	// play goal sound once
    	audio.play(lvl->sound);

    	// Level loop
    	Events::cubeTouch.set(&Game::onTouch, this);
    	while(running)	// wait for events to be handled
    	{
    		System::paint();
    	}

    	// if here level was completed!
    	for (unsigned k = 0; k < NUM_CUBES; k++)
    		vid[k].bg0.image(vec(0,0), Bravo);

    	System::paint();

    	Events::cubeTouch.unset();	// disable touch while showing "bravo"
    	wait(2);	// show the "bravo" for 2 second before next level
    }
}

/* 	pause for roughly n seconds */
void wait(unsigned n)
{
	SystemTime start = SystemTime::now();
	float elapsed = 0;
	while(elapsed < n)
		elapsed = ((SystemTime::now() - start).seconds());
}

/* This function randomly shuffles and renders an image from the level on a cube. It also records
 * 		what cube that the goal image in placed upon within the current Level. Then paints to display.
 */
void shuffleLoad()
{
	Random rand;
	int inds[NUM_CUBES], randint;

	// Generate 0-NUM_CUBES randomly in the inds array
	for(int i = 0; i < NUM_CUBES; i++)
	{
		bool found = false;
		randint = rand.randrange(NUM_CUBES);
		for (int j = 0; j < i; j++)
		{
			LOG("i = %i, inds[j] = %i, randint = %i\n", i, inds[j], randint);
			if (inds[j] == randint)
				found = true;
		}
		LOG("inds[i] = %i\n", randint);
		if (!found)
			inds[i] = randint;
		else
			i--;
	}

	// display the corresponding image on the cubes, and record the goal cube
	for (int i = 0; i < NUM_CUBES; i++)
	{
		LOG("%i: %i\n", i, inds[i]);
		if (inds[i] == 0)
			lvl->goalIndex = i;
		vid[i].bg0.image(vec(0,0), lvl->phonemes[inds[i]]);
	}

	System::paint();
}
