
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
    .package("com.sifteo.sdk.basicgame", "0.1")
    .icon(Icon)
    .cubeRange(NUM_CUBES);

void main()
{
	Game game;

	while(1)
	{
		game.title();
		game.init();
		game.run();
		game.cleanup();
	}
}
