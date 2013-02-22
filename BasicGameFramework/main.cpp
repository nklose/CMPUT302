
#include <sifteo.h>
#include "SensorListener.h"
#include "text.h"
#include "assets.gen.h"
using namespace Sifteo;

static Metadata M = Metadata()
    .title("Basic Game Framework")
    .package("com.sifteo.sdk.basicgame", "1.1")
    .icon(Icon)
    .cubeRange(1);

// GLOBALS
static VideoBuffer vid[CUBE_ALLOCATION];
static TiltShakeRecognizer motion[CUBE_ALLOCATION];

void main()
{
	// Setup a SensorListener that will handle event calls for sensory input
    static SensorListener sensors(vid, motion);
    sensors.install();

    // Sample draw text on cube 0
    TextRenderer text(vid[0], YELLOW, BLUE);
    text.init(98, 30);

	text.drawCentered(16, "This is some text");
	//text.drawCentered(16-(FONT_HEIGHT*2), "More text!");

    while (1)
		System::paint();
}
