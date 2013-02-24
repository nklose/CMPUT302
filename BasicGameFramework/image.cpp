/*
 * image.cpp
 *
 *  Created on: Feb 24, 2013
 *      Author: Andrew Neufeld
 */

#include "image.h"

ImageRenderer::ImageRenderer(unsigned _cube, VideoBuffer &_vid)
	: cubeid(_cube), vid(_vid)
{ }

/* Initialize this renderer by attaching the VideoBuffer to the cube */
void ImageRenderer::init()
{
	vid.initMode(BG0);
	vid.attach(cubeid);
}

/* Draw the specific frame of the AssetImage at pos on the cube */
void ImageRenderer::drawImage(UInt2 pos, const AssetImage &image, unsigned int frame)
{
	vid.bg0.image(pos, image, 1);
	System::paint();
}

/* Draw the specific frame of the AssetImage on the cube at the y height, and centered on the x axis */
void ImageRenderer::drawCentered(unsigned y, const AssetImage &image, unsigned int frame)
{
	unsigned x = (18 - image.tileWidth()) / 2;

	vid.bg0.image(vec(x, y), image, 1);
	System::paint();
}

/* Change the cube that this renderer is attached to, and call init() again */
void ImageRenderer::changeCube(unsigned cube)
{
	cubeid = cube;
	init();
}
