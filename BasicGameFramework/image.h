/*
 * image.h
 *
 *  Created on: Feb 24, 2013
 *      Author: Andrew Neufeld
 */

#pragma once

#include <sifteo.h>
using namespace Sifteo;

class ImageRenderer
{
public:

	ImageRenderer(unsigned _cube, VideoBuffer &_vid);

	/* Initialize this renderer by attaching the VideoBuffer to the cube */
	void init();

	/* Draw the specific frame of the AssetImage at pos on the cube */
	void drawImage(UInt2 pos, const AssetImage &image, unsigned int frame = 0);

	/* Draw the specific frame of the AssetImage on the cube at the y height, and centered on the x axis */
	void drawCentered(unsigned y, const AssetImage &image, unsigned int frame = 0);

	/* Change the cube that this renderer is attached to, and call init() again */
	void changeCube(unsigned cube);

private:
	unsigned cubeid;
	VideoBuffer &vid;

};
