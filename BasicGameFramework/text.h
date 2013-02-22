/*
 * text.h
 *
 *  Created on: Feb 21, 2013
 *      Author: Andrew Neufeld
 */

#pragma once

#include <sifteo.h>
#include "fontdata.h"
using namespace Sifteo;

class TextRenderer {
public:
    FB128Drawable &fb;
    UByte2 position;

    TextRenderer(FB128Drawable &fb) : fb(fb) {}

    void drawText(const char *str);

    static unsigned measureText(const char *str);

    void drawCentered(const char *str);

private:

    static unsigned measureGlyph(char ch);

    void drawGlyph(char ch);

};
