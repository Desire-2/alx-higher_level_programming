#ifndef LISTS_H
#define LISTS_H
#include <stdio.h>
#include <stdlib.h>
/**
 * struct listint_s - Singly linked list
 * @m: integer to be listed
 * @nxt: Next node Pointer
 *
 * Description: Singly linked list node structure
 */
typedef struct listint_s
{
	int m;
	struct listint_s *nxt;
} listint_t;

listint_t *insert_node(listint_t **head, int number);
listint_t *add_nodeint_end(listint_t **head, const int n);
size_t print_listint(const listint_t *h);
void free_listint(listint_t *head);

#endif
