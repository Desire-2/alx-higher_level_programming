#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 *  * struct listint_s - C Singly linked list
 * @n: Int
 * @next: Pointer to the next node
 *
 * Description: Singly linked list node struct
 *		for Holberton project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);
listint_t *add_nodeint(listint_t **head, const int n);
size_t print_listint(const listint_t *h);
void free_listint(listint_t *head);

#endif
