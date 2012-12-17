#ECE 2524: Intro To Unix
#Anamitra Bose
#Assignment Assignment


#Description

The user is given a phone data file called numbers.dat that has the phone numbers of a wide ranage of people. The format is as follows:

- Each person's name and number are on each line: the person's first name, followed by a semicolon, their last name, followed by a semicolon, and then their phone number with the area code in parenthesis and a hyphen preceding the last 4 digits of the phone number.

- The first letters of the last name and the first name of each person is capitalized.

Each line can thus be represented as follows:
First name; Last name; (XXX)XXX-XXXX

The file numbers.dat is provided to the user along with the assignment description.

The solution provided by the user must work on any data file of this format which may contain similar content. The tasks that must be performed are as follows:

Task 1:
Create a Unix command line that returns the number of people with the 703 and 757 area code phone number. 

Note: The user may not use the echo command since the echo command may workd for this particular data file but not a more extensive data file. 

Task2:
Create a Unix command line that displays the information in numbers.dat with every entry in the data file with area code (919) or last name beginning with a 'J' changed to area code (303) and first letter of last name changed to 'L'.

Note: Do not actually change the contents of numbers.dat but just show to standard output what it would look like with the above mentioned changes.

Task 3:
Create a Unix command line that displays a list of the unique first names in the numbers.dat data file. Show the list of first names only with no repeated first names and adding an additional tab for first names that do have more than one occurence. 

Note: It can be assumed that all the first names begin with a capital letter but they may have varying number of tabs in front of them.

#Execution

While exectuing the Unix command lines, the user must show the answers to each of the Unix pipes and filters tasks. For each task, put the label "TASK n:" to the left of the answer on the same line for the nth task number. The user's answer to the right of the label should be the complete Unix command line that will yield the answer required.

