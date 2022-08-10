Objectives of this assignment

• Understand a problem description, along with the role of the provided sample input and output.
• Use the programming language C to implement a Unix filter―an event processor named
event_manager.c―without resorting to dynamic memory allocation.
• Leverage Unix commands, such as diff, in your coding and testing. The lab instructors will explain
in the labs how to use the diff command.
• Use git to manage changes in your source code and annotate the continuous evolution of your
solution with “messages” given to commits.
• Test your code against the provided test cases.

This Project: event_manager.c

In this Project, you will learn C by solving a problem involving the iCalendar file format used by
several calendar programs, such as Google Calendar. Files following the iCalendar specification usually
have the “.ics” filename suffix. To simplify your solution, the iCal files provided for this term will be less
complex than what is possible using the full iCalendar standard.
You are to write a C program that inputs lines of data from a provided calendar file, accepts options and
arguments from the command line, and then outputs to the console events from the calendar file into a
more readable form
