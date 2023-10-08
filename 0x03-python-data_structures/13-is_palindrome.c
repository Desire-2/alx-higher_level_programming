#include "lists.h"

/**
 * reverse_listint - Reverses linked list
 * @head: Pointer to be pointed to the first node in the list
 * Return: Pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *nxt = NULL;
	listint_t *prv = NULL;
	listint_t *curr = *head;

	while (curr)
	{
		nxt = curr->next;
		curr->next = prv;
		prv = curr;
		curr = nxt;
	}

	*head = prv;
}

/**
 * is_palindrome - Function that checks if a linked list is a palindrome
 * @head: Double pointer of the linked list
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slw = *head, *fst = *head, *tmp = *head, *dp = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fst = fst->next->next;
		if (!fst)
		{
			dp = slw->next;
			break;
		}
		if (!fst->next)
		{
			dp = slw->next->next;
			break;
		}
		slw = slw->next;
	}

	reverse_listint(&dp);

	while (dp && tmp)
	{
		if (tmp->n == dp->n)
		{
			dp = dp->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}

	if (!dp)
		return (1);

	return (0);
}
