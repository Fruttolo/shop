#include <iostream>

bool isPrime(int number) {
    if (number <= 1) {
        return false;
    }
    for (int i = 2; i * i <= number; ++i) {
        if (number % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int N;

    std::cout << "Inserisci un numero N: ";
    std::cin >> N;

    std::cout << "Numeri primi da 0 a " << N << ":\n";

    for (int i = 2; i <= N; ++i) {
        if (isPrime(i)) {
            std::cout << i << " ";
        }
    }

    std::cout << "\n";

    return 0;
}
