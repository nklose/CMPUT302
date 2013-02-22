/*
 * text.cpp
 *
 *  Created on: Feb 21, 2013
 *      Author: Andrew Neufeld
 */

#include <sifteo.h>
#include "text.h"

/* Given the position.x and position.y of the TextRenderer, draw the text there */
void TextRenderer::drawText(const char *str) {
	LOG("Drawing text: \"%s\" at (%d, %d)\n",
		str, position.x, position.y);

	char c;
	while ((c = *str)) {
		str++;
		drawGlyph(c);
	}
}

/* Measure the size of the given text */
unsigned TextRenderer::measureText(const char *str) {
	unsigned width = 0;
	char c;
	while ((c = *str)) {
		str++;
		width += measureGlyph(c);
	}
	return width;
}

/* Given the position.y of the TextRenderer, draw the text centered horizontally, then increment
 * 		position.y so that further text can easily be drawn with subsequent calls. */
void TextRenderer::drawCentered(const char *str) {
	position.x = (LCD_width - measureText(str)) / 2;
	drawText(str);
	position.y += 8;
}

/* Measure one character font glyph */
unsigned TextRenderer::measureGlyph(char ch) {
	uint8_t index = ch - ' ';
	const uint8_t *data = font_data + (index << 3) + index;
	return data[0];
}

/* Draw one character font glyph given TextRenderer position var */
void TextRenderer::drawGlyph(char ch) {
	// Specifics of our font format
	uint8_t index = ch - ' ';
	const uint8_t *data = font_data + (index << 3) + index;
	uint8_t escapement = *(data++);
	const Int2 size = {8, 8};

	fb.bitmap(position, size, data, 1);
	position.x += escapement;
}
