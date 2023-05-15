Senior attributes:

understand algorithm

can they show a winder understanding of db

do they have approach to modelling



questions?

how do you stay up to date with latest developments

book/blogs/ etc

Side project

Open source

Try to do a read a blog or two a day, typically medium or I have a couple of mailing lits

I have several o'reilly books in my ipad so read some terraform, eth or python info


are you active on github? passionate outside?

Yes i have several personal projeects and several other ideas
I attend meetups
I really enjoy networking with fellow technical people or other interseted in what i am in.
I learn a lot from these actually, it can be refreshing to get perspetives on things you think you know from people with other skill sets


implement binary search of a sorted array of integers

todo

describe principles of rest API, compare it to rpc

1. uniform interface

principle of generaliy, we can simplify overall system arcitecture

2. Client - Server

separation of concerns

improves portability
improves testability

a client separate from the backend

3. Stateless

Statelessness - each requrest from the client to the server must contai all of the information necessary to understand and complete the request

Server cannot take advantage of any reviously stored contect information on the server, therefore client must keep session state

4. Cacheable

This contriant requires that a response should label itself as a cacheable or non-cacheable

if response is cacheable, the client app gets the right to reuse the response data later for equivalent requests and a specific period.

5. Layered System

the layered sytem style defines an architecture to be composed of hierachical layers by contraining component behaviour such that they can't see beyond what they are interacting with. Eg - a simple component button doesn't need access to the amount of traffic passed in on the server

6. Code on Demand (optional)

REST also allows client functionality to extend by downloading and executing code in the form applets or scripts

Example when HTML is loaded by browser, <script> tags allow an application to be loaded on demand

why use mongo over postgres?


Resource representation - REST APIs

- the data
- the metadata describing the data
- hypermedia links that can help clients transition to the next desired state

In simple words, in the REST architectural style, data and functionality are considered resources and are accessed using Uniform Resource Identifiers (URIs).

The clients and servers exchange representations of resources by using a standardized interface and protocol. Typically HTTP is the most used protocol, but REST does not mandate it.


RPC DIFF -

rpc is a bunch of functions where the method name is in the url string

APIs can look better because you can pass the arguments int  url string, instaead of passing in sql



Python questions

Do arguments in Python get passed by reference or by value

Passses by assignment

PBV - creates copy of argument to alter
PBR - uses argument itself, no additional memory for new value

assigning return values to variables is the best way to achieve the same results as passing by reference in python

Python’s language reference for assignment statements provides the following details:

    If the assignment target is an identifier, or variable name, then this name is bound to the object. For example, in x = 2, x is the name and 2 is the object.
    If the name is already bound to a separate object, then it’s re-bound to the new object. For example, if x is already 2 and you issue x = 3, then the variable name x is re-bound to 3.

All Python objects are implemented in a particular structure. One of the properties of this structure is a counter that keeps track of how many names have been bound to this object.

What tools do you use for linting, debugging and profiling?

Formatting - Black
Linting - Flake, radon
Debugging - VSCODE debugger env, tests, refacotor
profiling - datadog, grafana etc, prometheus

Profling - define  - Closely monitor the memory, CPU, and network utilized by each component during peak load testing

Give an example of filter and reduce over an iterable object

map - map(function, iterable(s))

def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(starts_with_A, fruit)

print(list(map_object))

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(lambda s: s[0] == "A", fruit)

print(list(map_object))

filter(function, iterable(s))

def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(starts_with_A, fruit)

print(list(filter_object))

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(lambda s: s[0] == "A", fruit)

print(list(filter_object))
['Apple', 'Apricot']

reduce(function, sequence[, initial])

rom functools import reduce

def add(x, y):
    return x + y

list = [2, 4, 7, 3]
print(reduce(add, list))

16

What is list and dict comp?

ITerating over data structure and altering values

What is a closure?

A closure is any function which closes over the environment in which it was defined. This means that it can access variables not in its parameter list. Examples:

def func(): return h
def anotherfunc(h):
   return func()

This will cause an error, because func does not close over the environment in anotherfunc - h is undefined. func only closes over the global environment. This will work:

def anotherfunc(h):
    def func(): return h
    return func()
`

How is memory managed in python?

Memory management in Python involves the management of a private heap. A private heap is a portion of memory that is exclusive to the Python process. All Python objects and data structures are stored in the private heap. The operating system cannot allocate this piece of memory to another process.

continue - https://www.honeybadger.io/blog/memory-management-in-python/

What will be the output of the following code?
list = ['a', 'b', 'c', 'd', 'e']
print list[10:]

an empty list since there is no start from 10th index

Python uses a Global Interpreter Lock. Does that mean it doesn’t use real threads?

The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter. This means that only one thread can be in a state of execution at any point in time.

Read more and add info about multi processing

What database to use and when?
