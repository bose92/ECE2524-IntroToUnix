//ECE 2524: Intro to Unix
//Anamitra Bose
//Homework 10: Process Object
//Date: December 12, 2012


#include "Process.h"
#include <sys/wait.h>
#include <string.h>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>


Process:: Process (const std::vector<std::string> &args)
{
if(pipe(readpipe) == -1)
{
perror("Read pipe could not be created successfully");
throw("Read pipe could not be created successfully");
}
if(args.size() < 1)
{
perror("Argument size is not acceptable");
throw("Argument size is not acceptable");
}
if(pipe(writepipe) == -1)
{
perror("Write pipe could not be created successfully");
throw("Write pipe could not be created successfully");
}
m_pid = fork();
if(m_pid < 0)
{
perror("Fork could not be successfully created");
throw("Fork could not be succesfully created");
}
if(m_pid == 0)
{
close(writepipe[1]);
close(readpipe[0]);
if((dup2(readpipe[1],1)) == -1)
{
close(readpipe[1]);
perror("Could not successfully readpipe[1]");
throw("Could not successfully readpipe[1]");
}
close(readpipe[1]);
if((dup2(writepipe[0],0)) == -1)
{
close(writepipe[0]);
perror("Could not successfully writepipe[0]");
throw("Could not successfully writepipe[0]");
}
close(writepipe[0]);
std::vector<const char*> cargs;
std::transform(args.begin(), args.end(), std::back_inserter(cargs), [](const std::string s)
{
return s.c_str();
}
);
cargs.push_back(NULL);
if(execv(cargs[0], const_cast<char**>(&cargs[0])) == -1)
{
perror("Could not succesfully run the generator program");
exit(-1);
}
}
else
{
close(readpipe[1]);
close(writepipe[0]);
m_pread = fdopen(readpipe[0], "r");
cout << "Parent process number: " << pid()-1 << endl;
}
}

Process::~Process()
{
fclose(m_pread);
close(writepipe[1]);
close(readpipe[0]);
int current;
if(waitpid(m_pid, &current, 0) == -1)
{
perror("Could not successfully terminate the process");
throw("Could not successfully terminate the process");
}
kill(m_pid, SIGTERM);
}

void Process::write(const std::string& cur_str)
{
if((::write(writepipe[1], cur_str.c_str(), cur_str.length())) == -1)
{
perror("Could not successfully write to pipe");
throw("Could not successfully write to pipe");
}
}

std::string Process::readline()
{
size_t now_size;
char* now = NULL;
string present;
if((getline(&now, &now_size, m_pread)) == -1)
{
perror("Could not successfully read line");
throw("Could not successfully read line");
}
present = now;
return present;
}
