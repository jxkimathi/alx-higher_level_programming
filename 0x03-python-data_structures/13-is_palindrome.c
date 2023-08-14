#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: A double pointer to the head of the list
 *
 * Return: 0 if not a palindrome, otherwise return 1
*/

int is_palindrome(listint_t **head)
{
    listint_t *first = *head;
    listint_t *second = *head;
    listint_t *prev = NULL;
    listint_t *temp;

    if (*head == NULL || (*head)->next == NULL)
    {
        return (1);
    }

    while (first != NULL && first->next != NULL)
    {
        first = first->next->next;
        temp = second->next;
        second->next = prev;
        prev = second;
        second = temp;
    }

    if (first != NULL)
    {
        second = second->next;
    }

    while (second != NULL)
    {
        if (prev->n != second->n)
        {
            return (0);
        }

        prev = prev->next;
        second = second->next;
    }

    return (1);
}
