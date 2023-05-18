What is the OSI Model?

The open systems interconnection (OSI) model is made up of serveral layers that standardise the functions of telecommunication or computing system. There are 7 layers total

Phyical layer
Deals witht the connection bwtween devices, cables or wireless signals. Responsible for transmittting raw data

Data Link Layer

creates reliable link between 2 devices on a network. Ensures reliables data transfer

Network Layer

Routes packets of data between different devices on a network, regardless of phyical connection medium. Determines optimal path to transfer and assigns logical addresses (IP) to devies on the network

Transport Layer

Ensures error-free and reliable data transmissions between devices. Achieved by flow control, error checking and data segmentation. Does this using protocols such as TCP and UDP.

Session Layer

Manages sessions, which are continuous connections between devices. ensure proper syncronization and data exchange between them

Application Layer

Is ther interface between the use and the communications system. Responsible for provinding netowrking for different apps like email, web apps or file sharing


What is a network protocol?

A set of rules and procedures that define how data should be transmitted, formatted and processed over a network

what is HTTP and HTTPs?

HyperText Transfer Protocol is foundation of comms on wwww. Defines how data should be sent between clcient and server. HTTP is stateless, they are independant and do not store state, passes info from a to b.

HTTPS - plus secure is a secure version of HTTP that encrypts between the client and server using SSL or TLS to protect sensitive data from being intercepted or tampered with.

What is Transmission Control Protocol ( TCP )?

TCP is a reliable connection-oriented protocol that ensures data is delivered correctly between applications over a network. It ensures accurate and complete data delive. Segments and reorders packets and verifies them

What is internet protocol (IP)?

Responsible for delivering packets from host to destination based on IP addresses. IP is primary protocol in internet layer. Has 2 versions

Expand

What is UDP?

User datagram protocol - connectionless communication - doesn't provide error checking, making it suitable for real-time applications like video streaming and online gaming where low latency is crucial

What is Domain Name System ?

The domain name system (dns) is responsible for translating human readable domain names - into corresponding IP addresses that computers understand. This process is called domain name resolution. DNS is part of internet communcation as it allows users to access website using easy to remember names.

Expand - what are all dns parameters for

What is FTP?

File transfer protocol is a standard used for transferring files over a TCP-based network such as the internet.

What is SMTP?

Simple main transfer protocol is the standard protocol for sending email messages across a network.

What is SSL?

Secure Socket layer - cryptographic protocol to add security. Not reccommended in modern applications

What is TLS?

SUccessor to SSL

How does SSL/TLS work?

encryption achieved using a combination of algotrithms, key exchanges and digital certs

Steps in TLS connection -

Handshake - agress on which version of TLS to use and choose cipher suites that will secure the connection

Key Exchange - Both generate and share encryption keys. There encrypt and decrypt data sent

Certification Verificaion - server provides a digital cert. which contains public key and information about te server, client checks validity by confirming it was issued by a trusted auth

Secure Communicaion - Can begin sharing data

What are advantages of SSL and TLS ?

Secure communication

AUthentication

Data integrity
