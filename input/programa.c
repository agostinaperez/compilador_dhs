int suma (int a, int b) {
    return a + b;
}

int main() {
    int x = 5, y= 10;
    int z;

    z = x + y;
    z = z - 2;
    z = z * 3;
    z = z / 2;
    z = z % 4;

    z = x << 2;
    z = y >> 1;

    int mayor = (x > y) ? x : y;

    if (x < y) {
        z = z + 1;
    } else {
        z = z - 1;
    }

    while (x < 10) {
        x = x + 1;
    }

    for (int i = 0; i < 5; i = i + 1) {
        z = z + i;
    }

    z = suma(x, y);

    return 0;
}
