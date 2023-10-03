#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of the first node of the list
 * @number: integer to be included in the new node
 * Return: address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nw_nd, *curr_nd;

	if (head == NULL)
		return (NULL);

	nw_nd = malloc(sizeof(listint_t));

	if (nw_nd == NULL)
		return (NULL);
	curr_nd = *head;
	nw_nd->m = number;
	nw_nd->nxt = NULL;
	if (*head == NULL)
	{
		*head = nw_nd;
		return (nw_nd);
	}
	if (curr_nd->m > number)
	{
		nw_nd->nxt = curr_nd;
		*head = nw_nd;
		return (nw_nd);
	}

	while (curr_nd->nxt != NULL)
	{
		if (curr_nd->nxt->m > number)
		{
			nw_nd->nxt = curr_nd->nxt;
			curr_nd->nxt = nw_nd;
			return (nw_nd);
		}
		curr_nd = curr_nd->nxt;
	}
	curr_nd->nxt = nw_nd;
	return (nw_nd);
}
