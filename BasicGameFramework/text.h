/*
 * text.h
 *
 *  Created on: Feb 21, 2013
 *      Author: Andrew Neufeld
 */

#pragma once

#include <sifteo.h>
#include "constants.h"
using namespace Sifteo;

class TextRenderer {
public:

    TextRenderer(VideoBuffer &_vid, RGB565 _fb, RGB565 _g);

    void init(const unsigned firstLine, const unsigned numLines);

    /* Given x, y coords draw text in the given color on the VideoBuffer */
    void drawText(const unsigned x, const unsigned y, const char *str);

    /* Get the size of a text segment */
    static unsigned measureText(const char *str);

    /* Given a y coord draw text in a given color, centered on the x axis, on the VideoBuffer */
    void drawCentered(const unsigned y, const char *str);

private:
    // Member variables
    VideoBuffer &vid;
	FB128Drawable &fb;
	UByte2 position;
	RGB565 fg, bg;

    void renderText(const char *str);

    static unsigned measureGlyph(char ch);

    void renderGlyph(char ch);

};

RGB565 makeColor(uint8_t alpha);
