
#pragma once

#include <sifteo.h>
using namespace Sifteo;

/**
 * This class is essentially an example un-implemented class base for handlng events for sensory
 * 		input. For each different situation where specific controls are needed a different
 * 		implementation of this class can be used. That was one object can be created for each
 * 		control situation and they can be swapped between in the game loop via install()
 */
class SensorListener {
public:
	VideoBuffer *vid;
	TiltShakeRecognizer *motion;

	SensorListener(VideoBuffer* _vid, TiltShakeRecognizer* _motion) : vid(_vid), motion(_motion) {}

	/** Set up SensorListener and connect events to their on[Event] handling functions here */
    void install();

private:

    /* Called upon the event of a cube being touched */
    void onTouch(unsigned id);

    /* Called upon the event of a cube's acceleration changing measurably */
    void onAccelChange(unsigned id);

    /* Called upon the event of a cube being shaken. This is a sub-call of onAccelChange. */
    void onShake(unsigned id);

    /* Called upon the event of a cube being tilted. This is a sub-call of onAccelChange. */
	void onTilt(unsigned id, Byte3 tiltInfo);

	/* Called upon the event of a cubes neighbour being removed */
    void onNeighborRemove(unsigned firstID, unsigned firstSide, unsigned secondID, unsigned secondSide);

    /* Called upon the event of a cube getting a new neighbour */
    void onNeighborAdd(unsigned firstID, unsigned firstSide, unsigned secondID, unsigned secondSide);

};
