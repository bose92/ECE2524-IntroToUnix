#ECE 2524: Intro to Unix
#Anamitra Bose
#Homework 6 - Heard it on the Pipeline

CC = g++
CFLAGS = -Wall -g

all: consumer dispatcher generator

consumer: consumer.cpp
	${CC} ${CFLAGS} -c consumer.cpp
dispatcher: dispatcher.cpp
	${CC} ${CFLAGS} -c dispatcher.cpp
generator: generator.cpp
	${CC} ${CFLAGS} -c generator.cpp

clean:
	rm -f *.o *~ *.hh consumer dispatcher generator
