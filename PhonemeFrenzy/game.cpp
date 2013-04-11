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
#include "GameData.h"
#include <sifteo/time.h>
#include <sifteo/menu.h>
#include <sifteo/filesystem.h>
using namespace Sifteo;

// Globals
TiltShakeRecognizer motion[NUM_CUBES];
VideoBuffer vid[NUM_CUBES];
CubeSet speakerCube(NUM_CUBES-1);	// the "speaker" cube
CubeSet allCubes(0,NUM_CUBES);	// all non-speaker cubes
//MyLoader speakerLoader(speakerCube, MainSlot, vid);
MyLoader loader(allCubes, MainSlot, vid);
AudioChannel audio(0);
struct LevelSet *set;
int playthrough = 0;
bool title;
unsigned finalDemerit;
GameData gameData;
StoredObject playthroughNumber = StoredObject::allocate();
// numbers for saving and loading
int numDataItems = 3;
int maxNumLevels = 10;
int maxNumPlaythroughs = 10;
int totalNum = numDataItems*maxNumLevels*maxNumPlaythroughs;
unsigned dataSize = (sizeof(unsigned)*totalNum);
// initialize all 10 stored objects for level data
StoredObject lvlData1 = StoredObject::allocate();
StoredObject lvlData2 = StoredObject::allocate();
StoredObject lvlData3 = StoredObject::allocate();
StoredObject lvlData4 = StoredObject::allocate();
StoredObject lvlData5 = StoredObject::allocate();
StoredObject lvlData6 = StoredObject::allocate();
StoredObject lvlData7 = StoredObject::allocate();
StoredObject lvlData8 = StoredObject::allocate();
StoredObject lvlData9 = StoredObject::allocate();
StoredObject lvlData10 = StoredObject::allocate();

void Game::init()
{

    // initialize title to 1, which will be changed to 0 once the title is passed
    title = true;

    // read the previous playthrough number from the StoredObjects
    int tempbuf[1];
    int temp = playthroughNumber.read(&tempbuf, sizeof(int));
    LOG("\nnum bytes loaded from playthrough obj: %i\n\n", temp);
    if (temp != 0)
    {
	//	playthrough = 0;
		playthrough = tempbuf[0];
		LOG("tempbuf: %i\n", tempbuf[0]);
    }
    else
    {
    	playthrough = 0;
    }
    LOG("\nPLAYTHROUGH NUMBER: %i\n", playthrough);
    // set up the mode as well as attach the TiltShakeRecognizer and VidBuffs
    for (unsigned i = 0; i < NUM_CUBES; i++)
    {
        vid[i].initMode(BG0);
		vid[i].attach(i);
        motion[i].attach(i);
    }

    /* ensure on repeat-loops that the boot assets are in memory */
    MainSlot.erase();
    loader.load(BootAssets, MainSlot);

	Events::cubeAccelChange.set(&Game::onAccelChange, this);
}

void loadStoredObject(StoredObject obj, void *buffer, unsigned bufsize)
{

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

		Byte3 tilt = motion[id].tilt;
		if (tilt.x != prevTilt.x || tilt.y != prevTilt.y || tilt.z != prevTilt.z){
			onTilt(id, tilt);
		}

		bool shake = motion[id].shake;
		if (shake){
			onShake(id);
		}

		prevTilt = tilt;
	}
}

/* Called upon the event of a cube being shaken. In this game this repeats the goal sound */
void Game::onShake(unsigned id)
{
	LOG("Cube shaken: %02x\n", id);

	// Basic protection against multiple-plays of the audio clip
	static SystemTime start = SystemTime::now();
	float delay = 0.5f;
	if(!(SystemTime::now() - start < delay)){
		start = SystemTime::now();
		LOG("Playing sound on cube %i\n", id);

		// figure out which sound is for this cube id
		unsigned ind = 0;	// index within sounds array for appropriate sound
		for (int i = 0; i < NUM_IMAGES; i++)
		{
			if (set->indexes[i] == id)
				ind = i;
		}
		audio.play(set->sounds[ind]);
		gameData.incrementHints();
		LOG("---incremented hints to %u---\n", gameData.getHints());
	}
}

/* Called upon the event of a cube being tilted. This is a sub-call of onAccelChange. */
void Game::onTilt(unsigned id, Byte3 tiltInfo)
{
    //LOG("Cube %02X tilted: x = %02x, y = %02x, z = %02x\n", id, tiltInfo.x, tiltInfo.y, tiltInfo.z);
}

/* Called upon the event of a cube being touched */
void Game::onTouch(unsigned id)
{
	/* If still on main menu playthrough hasn't started yet */
	if(title){
		running = false;
	}else{
		/*
		 * A touch event occurs when first touching a cube screen as well as upon stopping touching
		 * 	the cube screen. The touched array ensure that only one of these 2 events calls this func fully
		 */
		static bool touched[NUM_CUBES] = {false, false, false};
		touched[id] = !touched[id];

		if (touched[id])
		{
			// if cube is the speaker cube, replay goal sound
			if (id == NUM_CUBES-1)
			{
				audio.play(set->goalsound);
				gameData.incrementHints();
				LOG("---incremented hints to %u---\n", gameData.getHints());
			} 
					else
			{
				// if cube is the goal cube (index 0)
				if (id == set->indexes[0])
				{
					running = false;
				}
				// if cube was incorrect guess
				else
				{
					// Darken cube, replay goal sound and increment attempts
					vid[id].bg0.image(vec(0,0), Grid);
					audio.play(set->goalsound);
					gameData.incrementAttempts();
					LOG("---incremented attempts to %u---\n", gameData.getAttempts());
				}
			}
		}
	}
}

/* Start running the game after levels are initialized */
void Game::startRun(){
		Events::cubeTouch.set(&Game::onTouch, this);

    	loader.load(LevelAssets[0].grp, MainSlot);
    	running = true;

		// load title image on cubes
		for (unsigned i = 0; i < NUM_CUBES; i++){
			vid[i].bg0.image(vec(0,0), Title);
		}
			wait(0.5);

		// wait for cube to be touched
    	while(running)
    		System::paint();
    	// continue running and start playthrough
		running = true;
		title = false;
		// disable touch temporarily (clears touch)
		Events::cubeTouch.unset();
    	wait(.5);
}

// Returns an index to the specified set for the specified level;
// for use in the array of sets.
int getSetIndex(int level, int set)
{
	int index = 0;
	// get up to first set of correct level
	for (int i = 0; i < level; i++)
	{
		for (int j = 0; j < setsInLevel[level]; j++)
		{
			index++;
		}
	}
	// now add the set offset
	index += set-1;
	return index;
}

/* Main game loop over defined levels */
void Game::run()
{
	/*
	 * HUGE NOTE: If you want the current level number below, use i. If you want the current /set/ index within LevelAssets and Levels
	 * then use the setIndex value. set has been changed to "set" to reflect this change in wording, but works the same as
	 * before. Any questions about this change, direct them to Andrew.
	 */
    for (unsigned i = 0; i < numLevels; i++)
    {
    	/* These few lines will get the index of a random set within level i */
    	Random rand;
    	int numSets = setsInLevel[i];
    	int setNum = rand.randrange(numSets)+1;
    	int setIndex = getSetIndex(i, setNum);

    	// if the memory slot has enough room, freely load it
        if (MainSlot.hasRoomFor(LevelAssets[setIndex].grp))
        	loader.load(LevelAssets[setIndex].grp, MainSlot);
        else
        {
        	LOG("\n\nNot enough memory on cubes for images, reloading\n\n\n");
        	// if there is not enough room to load next level, erase, load BootAssets, then load it
        	MainSlot.erase();
        	loader.load(BootAssets, MainSlot);
        	loader.load(LevelAssets[setIndex].grp, MainSlot);
        }
        //
    	set = &Levels[setIndex];

    	running = true;

		// load images onto cubes
    	shuffleLoad();
    	wait(0.5);

    	// play goal sound once
    	audio.play(set->goalsound);

    	// prepare level to be played
    	SystemTime initTime = SystemTime::now();
    	Events::cubeTouch.set(&Game::onTouch, this);
    	// wait for events to be handled
    	while(running)
    		System::paint();

    	// if here level was completed!
    	// Compute and add the time of that play to the current level
        SystemTime finalTime = SystemTime::now();
        updateTime(initTime, finalTime);
        // display BRAVO on all cubes
    	for (unsigned k = 0; k < NUM_CUBES; k++){
    		vid[k].bg0.image(vec(0,0), Bravo);
    	}
    	System::paint();

    	bool advance = evaluateResults();
    	// Didn't perform well enough to start new level
    	if(!advance) {
	    i--;
    	}
    	// Did perform well enough to start new level
    	else {
	    gameData.incrementLevel();
	    LOG("---incrementedLevel to %i---\n", gameData.getLevelCounter());
		}

		if (i == numLevels-1) {
			// at the end of the game, so increment the playthrough number and save objects
		    playthrough++;
			saveToStoredObject();
		}
		// disable touch while showing "bravo"
    	Events::cubeTouch.unset();
    	// show the "bravo" for 2 second before next level
    	wait(2);
    }
    gameData.clear();
    LOG("---playthrough=%i--\n", playthrough);
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
 * what cube that the goal image in placed upon within the current Level. Then paints to display.
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
		set->indexes[inds[i]] = i;
		vid[i].bg0.image(vec(0,0), set->phonemes[inds[i]]);
	}

	// also display the "speaker" icon for the 4th cube
	vid[NUM_IMAGES].bg0.image(vec(0,0), Speaker);

	System::paint();
}

/* Add the latest playTime to gameData's time */
void Game::updateTime(SystemTime initTime, SystemTime finalTime)
{
    unsigned playTime = (finalTime.uptimeMS() - initTime.uptimeMS())/1000;
    gameData.addTime(playTime);
    LOG("---Added %u to Time---\n", playTime);
}

/* Evaluate results of the level
 * Return true iff player did well enough to advance to next level */
bool Game::evaluateResults(){

	// Grab the weights set by the sliders in the Customization UI
	unsigned hintsWeight = hintsRequestedWeight;
	unsigned attemptsWeight= failedAttemptsWeight;
	unsigned timesWeight = timeWeight;

	//TODO: Don't hardcode threshold (may have to be changed by client)
	unsigned threshold = 600 + finalDemerit; // nullify the last attempts finalDemerits
	finalDemerit = (hintsWeight * gameData.getHints())
	    + (attemptsWeight * gameData.getAttempts())
	    + (timesWeight * gameData.getTime());
		LOG("Hints -> %u \nattempt -> %u \ntime -> %u \ntotal: %u\n",
				(hintsWeight * gameData.getHints()),
				(attemptsWeight * gameData.getAttempts()),
				(timesWeight * gameData.getTime()),
				finalDemerit);

	// if finalScore is too high, don't advance
	if(finalDemerit > threshold){
		return false;
	}
	// if finalDemerits is low enough, advance to the next level
	finalDemerit = 0; // reset the final result for the next level
	return true;
}

// Creates a 2D array to hold the 3 result parameters and a pointer to it
// uses write() to the global StoredObject to overwrite it with all new data
void Game::saveToStoredObject(){
    LOG("---SAVING---\n");

    int totalNum = numDataItems*maxNumLevels*maxNumPlaythroughs;
    unsigned dataSize, allResults[maxNumLevels][totalNum];

    if (playthrough == 9)
	{
    	return;
		LOG("\nMore than 10 playthroughs, not saving any more data.\n");
	}

    dataSize = (sizeof(unsigned)*totalNum);
    allResults[maxNumLevels][totalNum];

    // array of Stored Objects to ease loading and saving
    StoredObject objs[10] = { lvlData1, lvlData2, lvlData3, lvlData4, lvlData5, lvlData6, lvlData7, lvlData8, lvlData9, lvlData10 };

    // load any previous levels of data into allResults to keep all of it
    // 		here we want maxNumLevels, but its non-POD so we have to hardcode it
    for (int i = 0; i < maxNumLevels; i++)
    	objs[i].read(allResults[i], dataSize);

    // Save all new data into allResults
    int offset;
    gameData.resetLevelCounter();
    for (int i = 0; i < numLevels; i++)
    {
    	// this offset will account for playthrough so that the level object will
    	//		hold { p1attempt, p1hints, p1time, p2attempts, p2hints, ... }
    	// It is playthrough-1 because playthrough is incremented right before this func call
		offset = (playthrough-1)*3;
		allResults[i][offset] = gameData.getAttempts();
		LOG("----------------------------------------------------------attempts=%u\n",gameData.getAttempts());
		offset++;
		allResults[i][offset] = gameData.getHints();
		offset++;
		allResults[i][offset] = gameData.getTime();
		offset++;
		gameData.incrementLevel();
	}

    // Log the level play data to the screen for verification purposes
    for (int j = 0; j < 10; j++)
    {
    	LOG("Level %i play data:\n", j);
    	for(int i = 0; i < 10; i++)
    	{
    		LOG("%u %u %u\n", allResults[j][0+(3*i)], allResults[j][1+(3*i)], allResults[j][2+(3*i)]);
    	}
    }

    // Write the level play data to their StoredObjects
	for (int i = 0; i < maxNumLevels; i++)
		objs[i].write(allResults[i], dataSize);

	// store the playthrough number in its StoredObject
	int playbuf[1];
    playbuf[0] = playthrough;
    playthroughNumber.write(&playbuf, sizeof(int));
    
    LOG("---savedToStoredObject---\n");
}
