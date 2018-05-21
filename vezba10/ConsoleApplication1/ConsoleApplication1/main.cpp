
#include <iostream>
#include "readMatrix.h"
#include "determinant.h"

using namespace std;

int main() {

	int matrixSize;

	cout << "Dali je velicina matrice 2 ili 3?" << endl;
	cout << "Pritisnite 2 ako je 2" << endl;
	cout << "Pritisnite 3 ako je 3" << endl;
	cin >> matrixSize;

	int** matrixSquare = new int*[matrixSize];
	for (int row = 0; row < matrixSize; row++)
		matrixSquare[row] = new int[matrixSize];


	readMatrix(matrixSquare, matrixSize);

	int d = determinant(matrixSquare, matrixSize);


	cout << "Matrica: " << endl;
	if (matrixSize == 2)
	{
		cout << matrixSquare[0][0] << " " << matrixSquare[0][1] << endl;
		cout << matrixSquare[1][0] << " " << matrixSquare[1][1] << endl;
	}

	if (matrixSize == 3)
	{
		cout << matrixSquare[0][0] << " " << matrixSquare[0][1] << " " << matrixSquare[0][2] << endl;
		cout << matrixSquare[1][0] << " " << matrixSquare[1][1] << " " << matrixSquare[1][2] << endl;
		cout << matrixSquare[2][0] << " " << matrixSquare[2][1] << " " << matrixSquare[2][2] << endl;
	}

	cout << "Determinanta: " << d << endl;


		for (int row = 0; row < matrixSize; row++)
		{
			delete[] matrixSquare[row];
		}
	delete[] matrixSquare;


	return 0;
}
