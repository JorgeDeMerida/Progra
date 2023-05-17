#include "Serie.h"
#include <iostream>

using namespace std;
Serie::Serie() : numeroTemporadas(3), genero(""), creador("") {}

Serie::Serie(const string& titulo, const string& creador)
	: titulo(titulo), numeroTemporadas(3), genero(""), creador(creador) {}

Serie::Serie(const string& titulo, int numeroTemporadas, const string& genero, const string& creador)
	: titulo(titulo), numeroTemporadas(numeroTemporadas), genero(genero), creador(creador) {}

string Serie::getTitulo() const {
	return titulo;
}

int Serie::getNumeroTemporadas() const {
	return numeroTemporadas;
}

string Serie::getGenero() const {
	return genero;
}

string Serie::getCreador() const {
	return creador;
}

void Serie::setTitulo(const string& titulo) {
	this->titulo = titulo;
}

void Serie::setNumeroTemporadas(int numeroTemporadas) {
	this->numeroTemporadas = numeroTemporadas;
}

void Serie::setGenero(const string& genero) {
	this->genero = genero;
}

void Serie::setCreador(const string& creador) {
	this->creador = creador;
}

string Serie::to_String() {
	string entregadoString = (isEntregado() ? "Si" : "No");
	
	return "Titulo: " + titulo + "\n"
		+ "Numero de temporadas: " + to_string(numeroTemporadas) + "\n"
		+ "Genero: " + genero + "\n"
		+ "Creador: " + creador + "\n"
		+ "Entregado: " + entregadoString + "\n";
}
