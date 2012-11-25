//ECE 2524: Intro to Unix
//Anamitra Bose
//Homework 6: Heard it on the Pipeline

#include <string.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[])
{
	char str;
	int fdPipe[2];
	pid_t chpid;

	if (argc != 2)
	{
		fprintf(stderr, "Argument Error", argv[0]);
		exit(EXIT_FAILURE);
	}

	chpid = fork();

	if (chpid == -1)
	{
		perror("fork");
		exit(EXIT_FAILURE);
	}

	if (pipe(fdPipe) == -1)
	{
		perror("pipe");
		exit(EXIT_FAILURE);
	}

	if (chpid == 0)
	{
	close(fdPipe[1]);
	while (read(fdPipe[0], &str, 1) > 0)
		write(STDOUT_FILENO, &str, 1);
	write(STDOUT_FILENO, "\n", 1);
	close(fdPipe[0]);
	exit(EXIT_SUCCESS);
	}

	else
	{
	close(fdPipe[0]);
	write(fdPipe[1], argv[1], strlen(argv[1]));
	close(fdPipe[1]);
	wait(NULL);
	exit(EXIT_SUCCESS);
	}
}
