#ifndef _LISTS_H_
#define _LISTS_H_

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: Singly linked lists node structure a school project
 *
 **/

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);

#endif /*LISTS FILE*/
