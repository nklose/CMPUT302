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
#include <sifteo/time.h>
#include <sifteo/menu.h>
using namespace Sifteo;

// Globals
TiltShakeRecognizer motion[NUM_CUBES];
VideoBuffer vid[NUM_CUBES];
CubeSet allCubes(0,NUM_CUBES);
MyLoader loader(allCubes, MainSlot, vid);
AudioChannel audio(0);
struct Level *lvl;

// TEST - Add Menu Item images and Asset Images
static struct MenuItem menItems[] = { {&Bravo, &Bravo}, {&Bravo, &Bravo}, {&Bravo, &Bravo}, {NULL, NULL} };
static struct MenuAssets menAssets = {&Grid, &Bravo, &Bravo, {&Bravo, &Bravo, &Bravo, NULL}};

//TODO: As listed below
/* Display title screen and set up user's game */
void Game::title()
{
	LOG("TITLE SCREEN\n");
	//TODO: Ask Andrew if he knows of a better way to do this
	// Load "welcome" image from TestGroup[0],
	// which has Title image as welcomeTitle.png

	//loader.load(Level0Assets, MainSlot);
	for(int i = 0; i < NUM_CUBES; i++){
		vid[i].bg0.image(vec(0,0), Title);
	}

	System::paint();
	LOG("Waiting in title\n");
	wait(2);
	
	// Ask user to select username from a list (list made in customization screen?)

// TEST - Failed VM Fault - Stupid Hungry Cat Monkeys always ruining stuff
//    Menu m(vid[0], &menAssets, menItems);

//    m.anchor(2);
//    struct MenuEvent e;
//    uint8_t item;

	// Load "file" of user. Current level, recorded stats, etc
	// -> Load 'game' Dr. designed for this user? Or use same 'game' for everyone?
	// --> Jake can explain if this doesn't make sense

	// Display "PLAY"
	// Return when clicked so run can be executed (or directly call run)

}

void Game::init()
{
	// set up the mode as well as attach the TiltShakeRecognizer
    for (unsigned i = 0; i < NUM_CUBES; i++)
    {
        vid[i].initMode(BG0);
		vid[i].attach(i);
        motion[i].attach(i);
    }

    Events::cubeAccelChange.set(&Game::onAccelChange, this);
}

/* Unset some event handlers */
void Game::cleanup()
{
    Events::cubeTouch.unset();
}

/* Called upon the event of a cube's acceleration changing measurably */
void Game::onAccelChange(unsigned id)
{
	unsigned changeFlags = motion[id].update();

	if (changeFlags) {
		// Tilt/shake changed
		static Byte3 prevTilt = {0, 0, 0};

		LOG("onAccelChange and ");
		Byte3 tilt = motion[id].tilt;
		if (tilt.x != prevTilt.x || tilt.y != prevTilt.y || tilt.z != prevTilt.z){
			onTilt(id, tilt);
		} else{
			LOG("No tilt");
		}


		bool shake = motion[id].shake;
		if (shake){
			onShake(id);
		} else {

			LOG("Not Shaken\n");
		}

		prevTilt = tilt;
	}
}

//TODO: Why is this not being called? (Jake)
/* Called upon the event of a cube being shaken. In this game this repeats the goal sound */
void Game::onShake(unsigned id)
{
	LOG("Cube shaken: %02x\n", id);
	// If shaken strongly this may cause multiple plays...
	//		It may need a timer of some sort to prevent this

	// TODO: Test this. Can't seem to call this function at all.
	// Probably not the right way to go about it, could be attributes of a level,
	//then only created and set once per level. Or of game, only created once.
	// start a static timer (Should probably be set in another class?)
	static SystemTime start = SystemTime::now();
	float delay = 0.5f;
	if(!(SystemTime::now() - start < delay)){
		start = SystemTime::now();
		LOG("Playing Sound");
		audio.play(lvl->sound);
	}

//	audio.play(lvl->sound);
}

//TODO: Why called every time a cube is moved? -> Except when one cube moves another.. (Jake)
/* Called upon the event of a cube being tilted. This is a sub-call of onAccelChange. */
void Game::onTilt(unsigned id, Byte3 tiltInfo)
{
	LOG("Cube %02X tilted: x = %02x, y = %02x, z = %02x\n", id, tiltInfo.x, tiltInfo.y, tiltInfo.z);
}

/* Called upon the event of a cube being touched */
void Game::onTouch(unsigned id)
{
	LOG("Cube touched: %u\n", id);
	/* ensure only begin touch triggers end of level */
	static bool touched[NUM_CUBES] = {false, false, false};

	// TODO: Highlight cube and display/speak "Are you sure" <- or equivalent
	// ->On clicking a confirmed cube continue else repeat above

	// ensure it is the goal word cube
	if (id != lvl->goalIndex){
		// TODO: Darken cube and record incorrect cube guessed
		audio.play(lvl->sound);
		return;
	}

	if (!touched[id])
		running = false;
		touched[id] = !touched[id];
		LOG(" was goal\n");

}

/* Main game loop over defined levels */
void Game::run()
{
	// TODO: Note, loops 0-1-2-0-1-2-0-1-2 as level #.
	// ->Make a game ending
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
    	LOG("Played sound for level %d in run()\n", i);

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
			if (inds[j] == randint)
				found = true;
		}
		if (!found)
			inds[i] = randint;
		else
			i--;
	}

	// display the corresponding image on the cubes, and record the goal cube
	for (int i = 0; i < NUM_CUBES; i++)
	{
		if (inds[i] == 0)
			lvl->goalIndex = i;
		vid[i].bg0.image(vec(0,0), lvl->phonemes[inds[i]]);
	}

	System::paint();
}
