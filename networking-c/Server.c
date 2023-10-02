#include "Server.h"
#include <stdio.h>
#include <stdlib.h>

struct Server server_constructor(
    int domain,
    int service,
    int protocol,
    u_long interface,
    int port,
    int backlog,
    void (*launch)(void))
{
    struct Server server;
    server.domain = domain;
    server.service = service;
    server.protocol = protocol;
    server.interface = interface;
    server.port = port;
    server.backlog = backlog;

    server.address.sin_family = domain;
    server.address.sin_port = htons(port);
    server.address.sin_addr.s_addr = htonl(interface);

    server.socket = socket(domain, service, protocol);

    // checking for the validity of the socket connection
    if (server.socket == 0)
    {
        perror("Failed to connect to socket...\n");
        exit(1);
    }

    // binds my socket to the network interface and port
    if (bind(server.socket, (struct sockaddr *)&server.address, sizeof(server.address)) < 0)
    {
        perror("Failed to bind to socket...\n");
        exit(1);
    }

    // listen for incoming connections
    if (listen(server.socket, server.backlog))
    {
        perror("Failed to start listening...\n");
        exit(1);
    }

    server.launch = launch;

    return server;
}