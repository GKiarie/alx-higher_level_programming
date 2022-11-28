#include "lists.h"

/**
 * check_cycle - function that checks if
 * a singly linked list has a cycle in it
 * @list: list to check
 * Return: 0 if no cycle, 1 if theres a cycle
 */

int check_cycle(listint_t *list)
{
  listint_t *head;
  listint_t *tmp;

  head = list;
  tmp = list;

  while (tmp != NULL && head->next != NULL && head->next->next != NULL)
    {
      head = head->next->next;
      tmp=tmp->next;

      if(head == tmp)
	return (1);
    }
  return (0);
}
