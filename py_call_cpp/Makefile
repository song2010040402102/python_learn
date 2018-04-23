all: wrapper_c wrapper_cpp

wrapper_c: wrapper.c
	gcc -fPIC wrapper.c -o wrapper_c.so -shared  -I/usr/local/include/python2.7 -I/usr/local/lib/python2.7/config

wrapper_cpp: wrapper.cpp
	g++ -fPIC wrapper.cpp -o wrapper_cpp.so -shared  -I/usr/local/include/python2.7 -I/usr/local/lib/python2.7/config

clean:
	rm -f *.o *.so
