#include <iostream>
using namespace std;

int main() {
	// This is a little function to test lex analyzer
    int result = 2;
    result = result + 1;
    cout << result << endl;

    while(result<=10)	//while loop with condition
	{
		result++;		//incrementing operation
		}
    if (result > 0){
        return result <= 1;
    } else return result >= 0;
	return 0;
}
