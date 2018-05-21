
#include "readMatrix.h"
#include <iostream>

using namespace std;


void readMatrix(int** matrixSquare, int matrixSize)
{
	int num;

	cout << "Please enter " << matrixSize*matrixSize << " values for the square matrix." << endl;

	for (int row = 0; row < matrixSize; row++)
		for (int col = 0; col < matrixSize; col++)
		{
			cin >> num;
			matrixSquare[row][col] = num;
		}
}
