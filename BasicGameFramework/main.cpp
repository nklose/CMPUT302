
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

// COLORS
const RGB565 BLACK = RGB565::fromRGB(0x000000);
const RGB565 WHITE = RGB565::fromRGB(0xFFFFFF);
const RGB565 BLUE = RGB565::fromRGB(0x0900FF);
const RGB565 RED = RGB565::fromRGB(0xFF0900);
const RGB565 GREEN = RGB565::fromRGB(0x00FF09);
const RGB565 YELLOW = RGB565::fromRGB(0xFFFF00);

// GLOBALS
static VideoBuffer vid[CUBE_ALLOCATION];
static TiltShakeRecognizer motion[CUBE_ALLOCATION];

static RGB565 makeColor(uint8_t alpha)
{
    // Linear interpolation between foreground and background

    const RGB565 bg = BLUE;
    const RGB565 fg = YELLOW;

    return bg.lerp(fg, alpha);
}

void initDrawing()
{
    /*
     * Init framebuffer, paint a solid background.
     */

    vid[0].initMode(SOLID_MODE);
    vid[0].colormap[0] = makeColor(0);
    vid[0].attach(0);

    System::paint();

    /*
     * Now set up a letterboxed 128x48 mode. This uses windowing to
     * start drawing on scanline 40, and draw a total of 48 scanlines.
     *
     * initMode() will automatically wait for the above rendering to finish.
     */

    vid[0].initMode(FB128, 40, 48);
    vid[0].colormap[0] = makeColor(0);
}

void onRefresh(void*, unsigned cube)
{
    /*
     * This is an event handler for cases where the system needs
     * us to fully repaint a cube. Normally this can happen automatically,
     * but if we're doing any fancy windowing effects (like we do in this
     * example) the system can't do the repaint all on its own.
     */

    LOG("Refresh event on cube %d\n", cube);
    if (cube == 0)
        initDrawing();
}

void main()
{
	// Setup a SensorListener that will handle event calls for sensory input
    static SensorListener sensors(vid, motion);
    sensors.install();

    // Sample draw text on cube 0
    TextRenderer text(vid[0].fb128);
    Events::cubeRefresh.set(onRefresh);
    initDrawing();

    text.position.y = 16;
	text.fb.fill(0);
	text.drawCentered("This is some text");
	vid[0].colormap[1] = makeColor(255);

    while (1)
		System::paint();
}
