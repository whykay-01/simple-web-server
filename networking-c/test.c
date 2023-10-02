#include <stdio.h>
#include <Server.h>

void launch(struct Server *server)
{
    char buffer[30000];
    printf("==== WAITING FOR CONNECTION ====\n");
    int address_length = sizeof(server->address);
    int new_socket = accept(server->socket, (struct sockaddr *)&server->address, (socklen_t *)&address_length);
    read(new_socket, buffer, 30000);
    printf("%s\n", buffer);

    printf("HTTP/1.1 200 OK\r ");
}

int main()
{
    struct Server server = server_constructor(AF_INET, SOCK_STREAM, 0, INADDR_ANY, 80, 10, NULL);
}