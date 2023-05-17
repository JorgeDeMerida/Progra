#ifndef SERIE_H
#define SERIE_H

#include <iostream>
#include "Entregable.h"
using namespace std;

class Serie : public Entregable {
private:
	string titulo;
	int numeroTemporadas;
	string genero;
	string creador;
	
public:
	Serie();
	Serie(const string& titulo, const string& creador);
	Serie(const string& titulo, int numeroTemporadas, const string& genero, const string& creador);
	
	string getTitulo() const;
	int getNumeroTemporadas() const;
	string getGenero() const;
	string getCreador() const;
	
	void setTitulo(const string& titulo);
	void setNumeroTemporadas(int numeroTemporadas);
	void setGenero(const string& genero);
	void setCreador(const string& creador);
	
	std::string to_String() override;
};

#endif 
