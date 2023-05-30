What kind of language is python?

High level - memory is managed for you for the most part

Can be dynamically or staticlly typed

interpreted - no compliation

How is memory managed in python?

Reference counting - counts references to object, when it hits 0 it is considered garbage

Uses an algorithm called 'tracing garbage collection'

Saves time for developer lifecycle, but can have more overheads in terms of perfomrance.

What is the GIL?

The global interpreter lock is a mechanism used to ensure thread safety in the presence of multiple threads

Prevents multiple threads executiong pyton bytecodes at the same time, it is a limitation of python but GIL can be released when running I/O operations

What is an I/O operation?

Input operations involve receiving data from external source and bringing into the program, eg reading data from file

Output operation - sending data to external destination
