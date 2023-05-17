#include "Videojuego.h"
#include <iostream>

using namespace std;

Videojuego::Videojuego() : horasEstimadas(10), genero(""), compania("") {}

Videojuego::Videojuego(const string& titulo, int horasEstimadas)
	: titulo(titulo), horasEstimadas(horasEstimadas), genero(""), compania("") {}

Videojuego::Videojuego(const string& titulo, int horasEstimadas, const string& genero, const string& compania)
	: titulo(titulo), horasEstimadas(horasEstimadas), genero(genero), compania(compania) {}

std::string Videojuego::getTitulo() const {
	return titulo;
}

int Videojuego::getHorasEstimadas() const {
	return horasEstimadas;
}

string Videojuego::getGenero() const {
	return genero;
}

string Videojuego::getCompania() const {
	return compania;
}

void Videojuego::setTitulo(const string& titulo) {
	this->titulo = titulo;
}

void Videojuego::setHorasEstimadas(int horasEstimadas) {
	this->horasEstimadas = horasEstimadas;
}

void Videojuego::setGenero(const string& genero) {
	this->genero = genero;
}

void Videojuego::setCompania(const string& compania) {
	this->compania = compania;
}

string Videojuego::to_String() {
	std::string entregadoString = (isEntregado() ? "Si" : "No");
	
	return "Titulo: " + titulo + "\n"
		+ "Horas estimadas: " + to_string(horasEstimadas) + "\n"
		+ "Genero: " + genero + "\n"
		+ "Compania: " + compania + "\n"
		+ "Entregado: " + entregadoString + "\n";
}
