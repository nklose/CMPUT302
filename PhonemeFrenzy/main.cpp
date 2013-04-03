
#include <sifteo.h>
#include "SensorListener.h"
#include "text.h"
#include "loader.h"
#include "game.h"
#include "assets.gen.h"
using namespace Sifteo;

AssetSlot MainSlot = AssetSlot::allocate()
    .bootstrap(BootAssets);

static Metadata M = Metadata()
    .title("Basic Game Framework")
    .package("com.sifteo.sdk.phonemefrenzy", "0.8")
    .icon(Icon)
    .cubeRange(NUM_CUBES);

void main()
{
	Game game;

	/* For now, loop the game */
	while(1)
	{
		LOG("NEW MAIN WHILE LOOP\n");
		game.init();
		game.startRun();
		game.run();
		game.cleanup();
	}
}
