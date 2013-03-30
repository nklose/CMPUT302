#ifndef SETDATA_H_
#define SETDATA_H_

class SetData {
public:
	SetData();
	int getHints();
	void setHints(int numHints);
	int getAttempts();
	void setAttempts(int numAttempts);
	int getSeconds();
	void setSeconds(int numSeconds);
	//String getGoal();
private:
	//String Goal;
	int Hints;
	int Attempts;
	int Time;
};


#endif