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
CubeSet imageCubes(0,NUM_IMAGES);
MyLoader loader(allCubes, MainSlot, vid);
AudioChannel audio(0);
struct Level *lvl;

// TEST - Add Menu Item images and Asset Images
static struct MenuItem menItems[] = { {&IconChroma, &LabelUser1}, {&IconSandwich, &LabelUser2}, {&IconSandwich, &LabelEmpty}, {NULL, NULL} };
static struct MenuAssets menAssets = {&BgTile, &Footer, &LabelEmpty, {&Tip0, & Tip1, NULL}};

//TODO: As listed below
/* Display title screen and set up user's game */
void Game::title()
{
	for(int i = 0; i < NUM_CUBES; i++){
		vid[i].bg0.image(vec(0,0), Title);
	}
	System::paint();
	LOG("Waiting in title\n");
	wait(1);

	displayMenu();
}

// Display menu of available users
void Game::displayMenu(){

	loader.load(MenuAssetGrp, MainSlot);
	// Ask user to select user from a list
	// (list made in customization screen by client?)
    Menu m(vid[0], &menAssets, menItems);
    m.anchor(2);

    struct MenuEvent e;
    uint8_t item;

    while (1) {
        while (m.pollEvent(&e)) {

            switch (e.type) {

                case MENU_ITEM_PRESS:
                        m.anchor(e.item);
                    break;

                case MENU_EXIT:
                    // this is not possible when pollEvent is used as the condition to the while loop.
                    // NOTE: this event should never have its default handler skipped.
                    ASSERT(false);
                    break;

                case MENU_NEIGHBOR_ADD:
                    LOG("found cube %d on side %d of menu (neighbor's %d side)\n",
                         e.neighbor.neighbor, e.neighbor.masterSide, e.neighbor.neighborSide);
                    break;

                case MENU_NEIGHBOR_REMOVE:
                    LOG("lost cube %d on side %d of menu (neighbor's %d side)\n",
                         e.neighbor.neighbor, e.neighbor.masterSide, e.neighbor.neighborSide);
                    break;

                case MENU_ITEM_ARRIVE:
                    LOG("arriving at menu item %d\n", e.item);
                    item = e.item;
                    break;

                case MENU_ITEM_DEPART:
                    LOG("departing from menu item %d, scrolling %s\n", item, e.direction > 0 ? "forward" : "backward");
                    break;

                case MENU_PREPAINT:
                    // do your implementation-specific drawing here
                    // NOTE: this event should never have its default handler skipped.
                    break;

                case MENU_UNEVENTFUL:
                    // this should never happen. if it does, it can/should be ignored.
                    ASSERT(false);
                    break;
            }
            m.performDefault();
        }

        LOG("Selected User: %d\n", e.item);
    	// TODO: Load "file" of user. Current level, recorded stats, etc
    	// -> Load 'game' Dr. designed for this user? Or use same 'game' for everyone?
    	// --> Jake can explain if this doesn't make sense

        return;
    }
}

void Game::init()
{
	// set up the mode as well as attach the TiltShakeRecognizer and VidBuffs
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

	if (id == NUM_CUBES-1)
				return;

	// Basic protection against multiple-plays of the audio clip
	static SystemTime start = SystemTime::now();
	float delay = 0.5f;
	if(!(SystemTime::now() - start < delay)){
		start = SystemTime::now();
		LOG("Playing sound on cube %i", id);

		// figure out which sound is for this cube id
		unsigned ind = 0;	// index within sounds array for appropriate sound
		for (int i = 0; i < NUM_IMAGES; i++)
		{
			if (lvl->indexes[i] == id)
				ind = i;
		}

		audio.play(lvl->sounds[ind]);
	}
}

/* Called upon the event of a cube being tilted. This is a sub-call of onAccelChange. */
void Game::onTilt(unsigned id, Byte3 tiltInfo)
{
	LOG("Cube %02X tilted: x = %02x, y = %02x, z = %02x\n", id, tiltInfo.x, tiltInfo.y, tiltInfo.z);
}

/* Called upon the event of a cube being touched */
void Game::onTouch(unsigned id)
{
	LOG("Cube touched: %u\n", id);
	/*
	 * A touch event occurs when first touching a cube screen as well as upon stopping touching
	 * 	the cube screen. The touched array ensure that only one of these 2 events calls this func fully
	 */
	static bool touched[NUM_CUBES] = {false, false, false};

	// TODO: Highlight cube and display/speak "Are you sure" <- or equivalent
	// ->On clicking a confirmed cube continue else repeat above

	touched[id] = !touched[id];

	if (touched[id])
	{
		// if cube is the speaker cube, replay goal sound
		if (id == NUM_CUBES-1)
			audio.play(lvl->goalsound);
		else
		{
			if (id == lvl->indexes[0])
			{
				LOG(" was goal\n");
				running = false;
			}
			else
			{
				vid[id].bg0.image(vec(0,0), Grid);
				LOG(" was not goal\n");
			}
		}
	}
}

/* Main game loop over defined levels */
void Game::run()
{
	// TODO: Make a game ending. It just repeats at the moment
    for (unsigned i = 0; i < numLevels; i++)
    {
    	loader.load(LevelAssets[i].grp, MainSlot);

    	lvl = &Levels[i];
    	running = true;

		// load images onto cubes
    	shuffleLoad();
    	wait(0.5);

    	// play goal sound once
    	audio.play(lvl->goalsound);
    	LOG("Played sound for level %d in run()\n", i);

    	// Level loop
    	Events::cubeTouch.set(&Game::onTouch, this);
    	while(running)	// wait for events to be handled
    		System::paint();

    	// if here level was completed!
    	for (unsigned k = 0; k < NUM_CUBES; k++)
    		vid[k].bg0.image(vec(0,0), Bravo);

    	System::paint();

    	// TODO: record all info that need be recorded

    	Events::cubeTouch.unset();	// disable touch while showing "bravo"
    	wait(2);	// show the "bravo" for 2 second before next level
    }
}

/* 	pause for roughly n seconds */
void wait(float n)
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
	int inds[NUM_IMAGES], randint;

	// Generate 0-NUM_CUBES randomly in the inds array
	for(int i = 0; i < NUM_IMAGES; i++)
	{
		bool found = false;
		randint = rand.randrange(NUM_IMAGES);
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
	for (int i = 0; i < NUM_IMAGES; i++)
	{
		lvl->indexes[inds[i]] = i;
		vid[i].bg0.image(vec(0,0), lvl->phonemes[inds[i]]);
	}

	// also display the "speaker" icon for the 4th cube
	vid[NUM_IMAGES].bg0.image(vec(0,0), Speaker);

	System::paint();
}
