#ifndef VIDEOJUEGO_H
#define VIDEOJUEGO_H

#include <iostream>
#include "Entregable.h"
using namespace std;

class Videojuego : public Entregable {
private:
	string titulo;
	int horasEstimadas;
	string genero;
	string compania;
	
public:
	Videojuego();
	Videojuego(const string& titulo, int horasEstimadas);
	Videojuego(const string& titulo, int horasEstimadas, const string& genero, const string& compania);
	
	string getTitulo() const;
	int getHorasEstimadas() const;
	string getGenero() const;
	string getCompania() const;
	
	void setTitulo(const string& titulo);
	void setHorasEstimadas(int horasEstimadas);
	void setGenero(const string& genero);
	void setCompania(const string& compania);
	
	string to_String() override;
};

#endif 
