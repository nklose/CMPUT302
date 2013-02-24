
#include <sifteo.h>
#include "SensorListener.h"
#include "text.h"
#include "image.h"
#include "assets.gen.h"
using namespace Sifteo;

AssetSlot MainSlot = AssetSlot::allocate()
    .bootstrap(BootAssets);

const int NUMCUBES = 3;

static Metadata M = Metadata()
    .title("Basic Game Framework")
    .package("com.sifteo.sdk.basicgame", "0.1")
    .icon(Icon)
    .cubeRange(NUMCUBES);

// GLOBALS
static VideoBuffer vid[NUMCUBES];
static TiltShakeRecognizer motion[NUMCUBES];

void main()
{
	// Setup a SensorListener that will handle event calls for sensory input
    static SensorListener sensors(vid, motion);
    sensors.install();

	// Create a new audio channel and init it's id to 0
	AudioChannel audio(0);

    // Sample draw text on cube 0
    TextRenderer cube0text(0, vid[0], YELLOW, BLUE);
    // 98 can be thought of as the y-coord for the "window" the text will be drawn
    //	in. 30 can be thought of as the height.
    cube0text.init(98, 30);
	cube0text.drawCentered(16, "This is some text");

	// Sample image draw on cube 1
	/*ImageRenderer cube1image(1, vid[1]);
	cube1image.init();
	cube1image.drawImage(vec(0, 0), Icon);
*/
    while (1)
    {
    	audio.play(SampleSound, AudioChannel::ONCE);
		System::paint();
    }
}
