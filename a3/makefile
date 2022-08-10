
CC=gcc

# The line with -DDEBUG can be used for development. When
# building your code for evaluation, however, the line *without*
# the -DDEBUG will be used.
#

CFLAGS=-c -Wall -g -DDEBUG -D_GNU_SOURCE -std=c99 -O0


all: song_analyzer

song_analyzer: song_analyzer.o list.o emalloc.o
	$(CC) song_analyzer.o list.o emalloc.o -o song_analyzer

song_analyzer.o: song_analyzer.c list.h emalloc.h
	$(CC) $(CFLAGS) song_analyzer.c

list.o: list.c list.h emalloc.h
	$(CC) $(CFLAGS) list.c

emalloc.o: emalloc.c emalloc.h
	$(CC) $(CFLAGS) emalloc.c

clean:
	rm -rf *.o song_analyzer 
