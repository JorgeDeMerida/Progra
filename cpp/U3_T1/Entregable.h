#ifndef ENTREGABLE_H
#define ENTREGABLE_H
#include <iostream>

using namespace std;

class Entregable {
private:
	bool entregado;
	
public:
	Entregable(); 
	void entregar();
	void devolver();
	bool isEntregado();
	virtual string to_String() = 0; 
};

#endif  // ENTREGABLE_H
