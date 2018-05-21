#include "determinant.hpp"
#include <iostream>

using namespace std;

int determinant(int** matrixSquare, int matrixSize)
{
	int determinant;

	if (matrixSize == 2)
	{
		determinant = matrixSquare[0][0] * matrixSquare[1][1] - matrixSquare[0][1] * matrixSquare[1][0];

	}

	if (matrixSize == 3)
	{

		int a = matrixSquare[0][0] * (matrixSquare[1][1] * matrixSquare[2][2] - matrixSquare[1][2] * matrixSquare[2][1]);

		int b = matrixSquare[0][1] * (matrixSquare[1][0] * matrixSquare[2][2] - matrixSquare[1][2] * matrixSquare[2][0]);

		int c = matrixSquare[0][2] * (matrixSquare[1][0] * matrixSquare[2][1] - matrixSquare[1][1] * matrixSquare[2][0]);

		determinant = a - b + c;

	}
	return determinant;
}
