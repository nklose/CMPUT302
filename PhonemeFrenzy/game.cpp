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
#include "GameData.h" //if you add this, add the following to the MakeFile:
/*	GameData.o \
LevelData.o \
SetData.o \
*/
#include <sifteo/time.h>
#include <sifteo/menu.h>
#include <sifteo/filesystem.h>
using namespace Sifteo;

// Globals
TiltShakeRecognizer motion[NUM_CUBES];
VideoBuffer vid[NUM_CUBES];
CubeSet allCubes(0,NUM_CUBES);
CubeSet imageCubes(0,NUM_IMAGES);
MyLoader loader(allCubes, MainSlot, vid);
AudioChannel audio(0);
struct LevelSet *lvl;
int playthrough;
//Volume storage = Volume::previous();
StoredObject lvlData = StoredObject::allocate();
//GameData gameData;

void Game::init()
{
	//GameData gameData;

	// initialize playthrough counter to 0
	playthrough = -1;
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
		}

		prevTilt = tilt;
	}
}

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
	if(playthrough == -1){//this would be the menu screen
		running = false;
	}else{
		/*
		* A touch event occurs when first touching a cube screen as well as upon stopping touching
		* 	the cube screen. The touched array ensure that only one of these 2 events calls this func fully
		*/
		static bool touched[NUM_CUBES] = {false, false, false};

		// TODO?: Highlight cube and display/speak "Are you sure" <- or equivalent
		// ->On clicking a confirmed cube continue else repeat above

		touched[id] = !touched[id];

		if (touched[id])
		{
			// if cube is the speaker cube, replay goal sound
			if (id == NUM_CUBES-1)
			{
				audio.play(lvl->goalsound);
				lvl->numHints++;
				gameData.incrementHints();
			} 
			else
			{
				if (id == lvl->indexes[0])
				{
					LOG(" was goal\n");
					running = false;
					gameData.incrementSet();
				}
				else
				{
					vid[id].bg0.image(vec(0,0), Grid);
					lvl->numAttempts++;
					audio.play(lvl->goalsound);
					LOG(" was not goal\n");
					gameData.incrementAttempts();
				}
			}
		}
	}
}


void Game::startRun(){
	Events::cubeTouch.set(&Game::onTouch, this);

	loader.load(LevelAssets[0].grp, MainSlot);
	running = true;

	// load start image on cubes
	for (unsigned i = 0; i < NUM_CUBES; i++){
		vid[i].bg0.image(vec(0,0), Title);
	}
	wait(0.5);

	while(running)	// wait for events to be handled
		System::paint();
	running = true;
	playthrough = 0;
	Events::cubeTouch.unset();	// disable touch temporarily (clears touch)
	wait(.5);	

}

/* Main game loop over defined levels */
void Game::run()
{
	// TODO: Make a game ending. It just repeats at the moment
	for (unsigned i = 0; i < numLevels; i++)
	{
		loader.load(LevelAssets[i].grp, MainSlot);
		lvl = &Levels[i];
		// TESTING
		loadAll();
		running = true;

		// load images onto cubes
		shuffleLoad();
		wait(0.5);

		// play goal sound once
		audio.play(lvl->goalsound);

		// Level loop
		SystemTime initTime = SystemTime::now();
		Events::cubeTouch.set(&Game::onTouch, this);
		while(running)	// wait for events to be handled
			System::paint();


		// if here level was completed!
		SystemTime finalTime = SystemTime::now();
		updateTime(initTime, finalTime);
		for (unsigned k = 0; k < NUM_CUBES; k++)
			vid[k].bg0.image(vec(0,0), Bravo);

		System::paint();

		// TODO: write all info that need be recorded
		bool advance = evaluateResults();
		//TODO: Find a better way to do this!
		//and Move this to a function.
		lvl->numAttempts = 0;
		lvl->numHints = 0;
		if(!advance){
			i--;
		}
		if (i == numLevels-1){
			saveAll();
		}

		Events::cubeTouch.unset();	// disable touch while showing "bravo"
		wait(2);	// show the "bravo" for 2 second before next level
	}
	// TODO: Doesn't get called yet
	playthrough++;
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
		lvl->indexes[inds[i]] = i;
		vid[i].bg0.image(vec(0,0), lvl->phonemes[inds[i]]);
	}

	// also display the "speaker" icon for the 4th cube
	vid[NUM_IMAGES].bg0.image(vec(0,0), Speaker);

	System::paint();
}

//TODO: Only allow increments once per level-try per cube?

void updateTime(SystemTime initTime, SystemTime finalTime)
{
	float playTime = (finalTime.uptime() - initTime.uptime());
	lvl->time = playTime;
	LOG("\n---Time %f---\n\n", lvl->time);
}

// evaluate the results of the level
// return true iff player did well enough to advance to next level
bool evaluateResults(){
	//TODO: Tweak, and or change to sliders (Waiting on client)

	unsigned hintsWeight = hintSliderWeight;
	unsigned attemptsWeight= attemptSliderWeight;
	unsigned timesWeight = timeSliderWeight;

	unsigned finalResult;
	//TODO: Change to a better threshold (user study)
	unsigned threshold = 12000;

	finalResult = (hintsWeight * lvl->numHints)
		+ (attemptsWeight * lvl->numAttempts)
		+ (timesWeight * lvl->time);

	//	LOG("Hints -> %i \nattempt -> %i \ntime -> %i \ntotal: %i\n",
	//			hintsWeight*lvl->numHints, attemptsWeight*lvl->numAttempts,
	//			timesWeight*lvl->time, finalResult);

	if(finalResult > threshold){
		return false;
	}

	return true;
}

// Creates a 2D array to hold the 3 result parameters and a pointer to it
// uses write() to the global StoredObject to overwrite it with all new data
void saveAll(){
	void *dataPointer;
	unsigned dataSize;
	float allResults[numLevels][3];
	for (int i = 0; i < numLevels; i++){
		allResults[i][0] = lvl->numHints;
		allResults[i][1] = lvl->numAttempts;
		allResults[i][2] = lvl->time;
	}
	dataPointer = &allResults;
	dataSize = sizeof(float)*numLevels*3;
	LOG("\nSAVING---Size %i------Pointer %p---\n\n", dataSize, dataPointer);
	lvlData.write(dataPointer, dataSize);
}

// Reads the storedObject from the current volume into the dataBuffer array
// TODO: Still not saving/loading all the data, also saveAll and loadALL
// need to be repositioned.
void loadAll(){
	float dataBuffer[numLevels][3];
	unsigned dataSize = 36;
	int temp = lvlData.read(&dataBuffer, dataSize);

	LOG("\nLOADING---Pointer %p------Temp %i---\n\n", &dataBuffer, temp);
	LOG("Loaded Values:\n");
	for (int i = 0; i < numLevels; i++){
		for (int j = 0; j < 3; j++){
			LOG("%f ", dataBuffer[i][j]);
		}
		LOG("\n");
	}
}

