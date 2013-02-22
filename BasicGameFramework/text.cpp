/*
 * text.cpp
 *
 *  Created on: Feb 21, 2013
 *      Author: Andrew Neufeld
 */

#include <sifteo.h>
#include "text.h"
using namespace Sifteo;

TextRenderer::TextRenderer(VideoBuffer &_vid, RGB565 _fg, RGB565 _bg)
	: vid(_vid), fb(vid.fb128), fg(_fg), bg(_bg)
{
	position.x = 0;
	position.y = 0;
}

void TextRenderer::init(const unsigned firstLine = 0, const unsigned numLines = LCD_height)
{
	/*
	 * Init framebuffer, paint a solid background.
	 */

	vid.initMode(SOLID_MODE);
	vid.colormap[0] = bg;
	vid.attach(0);

	System::paint();

	/*
	 * Now set up a letterboxed 128x48 mode. This uses windowing to
	 * start drawing on scanline 40, and draw a total of 48 scanlines.
	 *
	 * initMode() will automatically wait for the above rendering to finish.
	 */

	vid.initMode(FB128, firstLine, numLines);
	vid.colormap[0] = bg;
}

void TextRenderer::renderText(const char *str)
{
	LOG("Drawing text: \"%s\" at (%d, %d)\n",
		str, position.x, position.y);

	char c;
	while ((c = *str)) {
		str++;
		renderGlyph(c);
	}
}

/* Given x, y coords draw text in the given color on the VideoBuffer */
void TextRenderer::drawText(const unsigned x, const unsigned y, const char *str)
{
	position.x = x;
	position.y = y;
	renderText(str);
	// now color the raw rendering
	vid.colormap[1] = fg;
	System::paint();
}

/* Get the size of a text segment */
unsigned TextRenderer::measureText(const char *str)
{
	unsigned width = 0;
	char c;
	while ((c = *str)) {
		str++;
		width += measureGlyph(c);
	}
	return width;
}

/* Given a y coord draw text in a given color, centered on the x axis, on the VideoBuffer */
void TextRenderer::drawCentered(const unsigned y, const char *str)
{
	position.x = (LCD_width - measureText(str)) / 2;
	drawText(position.x, y, str);
}

/* Measure one character font glyph */
unsigned TextRenderer::measureGlyph(char ch) {
	uint8_t index = ch - ' ';
	const uint8_t *data = font_data + (index << 3) + index;
	return data[0];
}

/* Draw one character font glyph given TextRenderer position var */
void TextRenderer::renderGlyph(char ch) {
	// Specifics of our font format
	uint8_t index = ch - ' ';
	const uint8_t *data = font_data + (index << 3) + index;
	uint8_t escapement = *(data++);
	const Int2 size = {FONT_HEIGHT, FONT_HEIGHT};

	fb.bitmap(position, size, data, 1);
	position.x += escapement;
}

// UTILITY FUNCTIONS

/* Create an in-between color based upon the alpha value */
RGB565 makeColor(RGB565 fg, RGB565 bg, uint8_t alpha)
{
    // Linear interpolation between foreground and background

    return bg.lerp(fg, alpha);
}

