
#include "SensorListener.h"

void SensorListener::install()
{
	Events::neighborAdd.set(&SensorListener::onNeighborAdd, this);
	Events::neighborRemove.set(&SensorListener::onNeighborRemove, this);
	Events::cubeAccelChange.set(&SensorListener::onAccelChange, this);
	Events::cubeTouch.set(&SensorListener::onTouch, this);
	Events::cubeBatteryLevelChange.set(&SensorListener::onBatteryChange, this);
	Events::cubeConnect.set(&SensorListener::onConnect, this);

	// Handle already-connected cubes
	for (CubeID cube : CubeSet::connected())
		onConnect(cube);
}

/* Called upon the event of a cube first connecting to the base */
void SensorListener::onConnect(unsigned id)
{
	LOG("Cube %d connected\n", id);

	vid[id].initMode(BG0_ROM);
	vid[id].attach(id);
	motion[id].attach(id);
}

/* Called upon the event of a cubes battery charge changing measurably */
void SensorListener::onBatteryChange(unsigned id)
{
	LOG("Battery changed: %02x\n", id);
}

/* Called upon the event of a cube being touched */
void SensorListener::onTouch(unsigned id)
{
	LOG("Cube touched: %02x\n", id);
}

/* Called upon the event of a cube's acceleration changing measurably */
void SensorListener::onAccelChange(unsigned id)
{
	unsigned changeFlags = motion[id].update();

	if (changeFlags) {
		// Tilt/shake changed
		static Byte3 prevTilt = {0, 0, 0};

		Byte3 tilt = motion[id].tilt;
		if (tilt.x != prevTilt.x || tilt.y != prevTilt.y || tilt.z != prevTilt.z)
			onTilt(id, tilt);

		bool shake = motion[id].shake;
		if (shake)
			onShake(id);

		prevTilt = tilt;
	}
}

/* Called upon the event of a cube being shaken. This is a sub-call of onAccelChange. */
void SensorListener::onShake(unsigned id)
{
	LOG("Cube shaken: %02x\n", id);
}

/* Called upon the event of a cube being tilted. This is a sub-call of onAccelChange. */
void SensorListener::onTilt(unsigned id, Byte3 tiltInfo)
{
	LOG("Cube %02X tilted: x = %02x, y = %02x, z = %02x\n", id, tiltInfo.x, tiltInfo.y, tiltInfo.z);
}

/* Called upon the event of a cubes neighbour being removed */
void SensorListener::onNeighborRemove(unsigned firstID, unsigned firstSide, unsigned secondID, unsigned secondSide)
{
	LOG("Neighbor Remove: %02x:%d - %02x:%d\n", firstID, firstSide, secondID, secondSide);
}

/* Called upon the event of a cube getting a new neighbour */
void SensorListener::onNeighborAdd(unsigned firstID, unsigned firstSide, unsigned secondID, unsigned secondSide)
{
	LOG("Neighbor Add: %02x:%d - %02x:%d\n", firstID, firstSide, secondID, secondSide);
}
