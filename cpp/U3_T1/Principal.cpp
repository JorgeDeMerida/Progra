#include <iostream>
#include "Serie.h"
#include "Videojuego.h"

using namespace std;

int contarEntregados(Entregable** arr, int size) {
	int count = 0;
	for (int i = 0; i < size; i++) {
		if (arr[i]->isEntregado()) {
			count++;
		}
	}
	return count;
}

void mostrarMaxHorasEstimadas(Videojuego** arr, int size) {
	int maxHoras = 0;
	int maxIndex = 0;
	
	for (int i = 0; i < size; i++) {
		if (arr[i]->getHorasEstimadas() > maxHoras) {
			maxHoras = arr[i]->getHorasEstimadas();
			maxIndex = i;
		}
	}
	
	cout << "Videojuego con mas horas estimadas:\n";
	cout << arr[maxIndex]->to_String() << endl;
}

void mostrarMaxTemporadas(Serie** arr, int size) {
	int maxTemporadas = 0;
	int maxIndex = 0;
	
	for (int i = 0; i < size; i++) {
		if (arr[i]->getNumeroTemporadas() > maxTemporadas) {
			maxTemporadas = arr[i]->getNumeroTemporadas();
			maxIndex = i;
		}
	}
	
	cout << "Serie con mas temporadas:\n";
	cout << arr[maxIndex]->to_String() << std::endl;
}

int main() {
	const int size = 5;
	
	Serie* series[size];
	Videojuego* videojuegos[size];
	
	// Crear objetos de series y videojuegos
	series[0] = new Serie("Game of Thrones", 8, "Fantasia", "David Benioff");
	series[1] = new Serie("Breaking Bad", 5, "Drama", "Vince Gilligan");
	series[2] = new Serie("Friends", 10, "Comedia", "David Crane");
	series[3] = new Serie("Stranger Things", 4, "Ciencia ficcion", "The Duffer Brothers");
	series[4] = new Serie("The Office", 9, "Comedia", "Greg Daniels");
	
	videojuegos[0] = new Videojuego("The Witcher 3: Wild Hunt", 80, "RPG", "CD Projekt Red");
	videojuegos[1] = new Videojuego("Grand Theft Auto V", 60, "Acción", "Rockstar Games");
	videojuegos[2] = new Videojuego("The Last of Us Part II", 30, "Accion-aventura", "Naughty Dog");
	videojuegos[3] = new Videojuego("Minecraft", 40, "Sandbox", "Mojang Studios");
	videojuegos[4] = new Videojuego("FIFA 22", 20, "Deportes", "EA Sports");
	
	videojuegos[0]->entregar();
	series[1]->entregar();
	series[3]->entregar();
	
	int seriesEntregadas = contarEntregados(reinterpret_cast<Entregable**>(series), size);
	int videojuegosEntregados = contarEntregados(reinterpret_cast<Entregable**>(videojuegos), size);
	
	std::cout << "Cantidad de series entregadas: " << seriesEntregadas << std::endl;
	std::cout << "Cantidad de videojuegos entregados: " << videojuegosEntregados << std::endl;

	mostrarMaxHorasEstimadas(reinterpret_cast<Videojuego**>(videojuegos), size);
	mostrarMaxTemporadas(reinterpret_cast<Serie**>(series), size);
	
	for (int i = 0; i < size; i++) {
		delete series[i];
		delete videojuegos[i];
	}
	
	return 0;
}

