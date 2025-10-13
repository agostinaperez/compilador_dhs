int suma (int a, int b) {

    for (int i = 0; i < 5; i = i + 1) {
        a = a + i;
    }

    if (a>b) {
        a = a + 1;
    }
    return a + b;
}

int main() {
    int x = 5, y= 10;
    int z;
    z = 0;

    z = z / 2;
    z = z % 4;
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


    z = suma(x, y);

    return 0;
}
