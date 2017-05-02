cython3 multiplication5.py -o multiplication.c --embed
gcc -Os -I /usr/include/python3.5m  multiplication.c -o multiplication -lpython3.5m -lpthread -lm -lutil -ldl
