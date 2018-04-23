all: callpy

callpy: callpy.cpp
	g++ -g -o callpy callpy.cpp -I/usr/local/include/python2.7 -L/usr/local/lib/python2.7/config -lpython2.7 -lpthread -ldl -lutil

clean: 
	rm -f *.o callpy
