# Anamitra Bose 
# Homework 5

all: exprtest
	make exprtest

CF = -Wall -g

parser.tab.hpp parser.tab.cpp: parser.ypp
	bison parser.ypp
scanner.cpp: scanner.ll
	flex -t scanner.ll > scanner.cpp
driver.o: scanner.hpp driver.hpp parser.tab.hpp driver.cpp
	g++ ${CF} -c driver.cpp
scanner.o: scanner.hpp scanner.cpp parser.tab.hpp
	g++ ${CF} -c scanner.cpp
exprtest: parser.tab.hpp parser.tab.cpp scanner.cpp exptrtest.o driver.o parser.tab.o scanner.o
	g++ ${CF} -o exprtest exptrtest.o driver.o parser.tab.o scanner.o
exptrtest.o: exprtest.cpp
	g++ ${CF} -o exptrtest.o -c exprtest.cpp
parser.tab.o: parser.tab.hpp parser.tab.cpp expression.hpp scanner.hpp driver.hpp
	g++ ${CF} -c parser.tab.cpp
clean:
	rm -f *.o parser.tab.hpp parser.tab.cpp scanner.cpp location.hh stack.hh position.hh
	rm exprtest

