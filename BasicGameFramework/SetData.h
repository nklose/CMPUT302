#ifndef SETDATA_H_
#define SETDATA_H_

class SetData {
public:
	SetData();
	int getNumHints();
	void setHints(int numHints);
	int getNumAttempts();
	void setAttempts(int numAttempts);
	int getNumSeconds();
	void setSeconds(int numSeconds);
	//String getGoal();
private:
	//String Goal;
	int Hints;
	int Attempts;
	int Seconds;
};


#endif