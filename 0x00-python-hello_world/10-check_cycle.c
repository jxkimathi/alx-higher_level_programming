#include "lists.h"

/**
 * check_cycle - Function that checks if a singly linked list has a cycle in it
 * @list: Head of the linked list
 *
 * Return: 0 if no cycle is present, otherwise return 1
*/

int check_cycle(listint_t *list)
{
    listint_t *head, *tail;

    if(!list || !list->next)
    return (0);

    head = list;
    tail = list->next;

    while(tail && tail->next)
    {
        if (head == tail)
        {
            return (1);
        }
        head = head->next;
        tail = tail->next->next;
    }
    return (0);
}