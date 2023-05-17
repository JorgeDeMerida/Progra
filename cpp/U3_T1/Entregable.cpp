#include "Entregable.h"

Entregable::Entregable() {
	entregado = false;
}

void Entregable::entregar() {
	entregado = true;
}

void Entregable::devolver() {
	entregado = false;
}

bool Entregable::isEntregado() {
	return entregado;
}
