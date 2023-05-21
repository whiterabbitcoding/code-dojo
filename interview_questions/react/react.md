What are the features of react?

JSX

A syntax extension to JS. Used with react to describe what the UI should look
like. With JSX you can write HTML structures in the file that contains
javascript code.

Components

Blocks of JS/React code with represent a portion or element of UI. For example a
button, a header etc. It splits the UI up making it easier to work with as a
codebase due to separation of concerns.

Virtual DOM

React keeps a lightweight representation of the DOM in memory, when a component
changes, the virtual DOM changes only that component in the Real DOM rather than
updating all objects/ the whole webpage

One-way-data-binding

A unidirectional data flow means that when designing react apps you should often
nest child components within parent components

Action -> store -> view

High performance

react updates only those components needed to be, so the result is fast web
applications

Can web browsers read jsx directly?

Web browsers cannot read JSX directly. This is because they are built to only
read regular JS objects and JSX is not a regular JavaScript object For a web
browser to read a JSX file, the file needs to be transformed into a regular
JavaScript object. For this, we use Babel

What is the real DOM?

DOM stands for Document Object Model. The DOM represents an HTML document with a
logical tree structure. Each branch of the tree ends in a node, and each node
contains objects.

Why use React instead of other frameworks, like Angular?

Because of its virtual DOM implementation and rendering optimizations, React
outperforms Angular. It's also simple to switch between React versions; unlike
Angular, you don't have to install updates one by one. Finally, using React,
developers have access to a wide range of pre-built solutions.

What is the difference between ES6 and ES5 standards?

Slight syntax differences

Instead of settting components to a varialbe you set it to a class which extends
a ReactComponent module

require vs import as well

How do you create a react app?

create-react-app in cli

What is an event in react?

an event is an action that a user can trigger such as mouseclick etc

They are written in camel case

How do you create an event?

Attach a function to an onclick, or onhover etc parameter of a componenent

What are synthetic events in react?

Synthetic events combine the response of different browser's native events into
one API, ensuring that the events are consistent across different browsers.

expand

Explain how lists work in React?

The traversal of lists is done using the map() function

Why is there a need for using keys in Lists?

Keys are very important in lists for the following reasons:

A key is a unique identifier and it is used to identify which items have
changed, been updated or deleted from the lists It also helps to determine which
components need to be re-rendered instead of re-rendering all the components
every time. Therefore, it increases performance, as only the updated components
are re-rendered

Keys can be a value of an object or the object itself if its a vector or array

What are forms in React?

Forms allow user to enter data and save it to a variable defined in the
component ordinarily.

What is an arrow function and how is it used in React?

An arrow function is a short way of writing a function to React. It is
unnecessary to bind ‘this’ inside the constructor when using an arrow function.
This prevents bugs caused by the use of ‘this’ in React callbacks.

What are the two types of react componenets?

Stateful and stateless

stateful take arguments upon definition stateless does not

What is the use of render() in React?

It is required for each component to have a render() function. This function
returns the HTML, which is to be displayed in the component. If you need to
render more than one element, all of the elements must be inside one parent tag
like <div>, <form>.

What is state in react?

The state is a built-in React object that is used to contain data or information
about the component. The state in a component can change over time, and whenever
it changes, the component re-renders. The change in state can happen as a
response to user action or system-generated events. It determines the behavior
of the component and how it will render.

state is mutable

What are props in react?

props are short for properties

props are immutable

Explain the lifecycle methods of components.

getInitialState(): This is executed before the creation of the component.
componentDidMount(): Is executed when the component gets rendered and placed on the DOM.
    shouldComponentUpdate(): Is invoked when a component determines changes to the DOM and returns a “true” or “false” value based on certain conditions.
componentDidUpdate(): Is invoked immediately after rendering takes place.
componentWillUnmount(): Is invoked immediately before a component is destroyed and unmounted permanently.
