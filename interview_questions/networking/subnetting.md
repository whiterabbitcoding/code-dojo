What is subnetting?

Subnettign is the process of dividing an IP network into smaller subnetworks called subnets. IT provides benefites such as organisation control and security for the network

Whatis an IP address?

An ip address is a unique identifier for devices on a network

Has two parts - the network address and the host adress

For example, in the IP address 192.168.1.5, and subnet mask 255.255.255.0, the network address is 192.168.1.0, and the host address is 5.

Why do we use subnets?

Subnetting has several advantages:

security - control spread of threats
performance - reduce congestion
easier admin - easier to track and allocate resources

separation of concerns

What is processs of subnetting

Choose subnet mask based of numbero f subnets and hosts
Divide the network into subnets by calculationg the addresses and incrementing the network portion of the IP address by the value of the borrowed bits

Determine host ranges

Assign IP addresses

How would you split a network of x for subnet of y?

Let’s suppose we have the network 192.168.1.0 with a subnet mask of 255.255.255.0. We want to create four smaller subnets. Here’s how we can do it:

    255.255.255.0 in binary is 11111111.11111111.11111111.00000000. We can borrow 2 bits from the host portion to create four subnets: 11111111.11111111.11111111.11000000, which is 255.255.255.192 in decimal format.

    Our subnets will have the following network addresses:
        192.168.1.0
        192.168.1.64
        192.168.1.128
        192.168.1.192

    The valid host ranges within each subnet are:
        192.168.1.1 - 192.168.1.62
        192.168.1.65 - 192.168.1.126
        192.168.1.129 - 192.168.1.190
        192.168.1.193 - 192.168.1.254

    Allocate IP addresses from these host ranges to devices within their respective subnets, and configure devices with the correct subnet mask (255.255.255.192).

Understanding the basics of subnetting is essential to properly configuring and securing your network. By efficiently dividing your network into smaller subnets, you can optimize performance, organization, and security.
