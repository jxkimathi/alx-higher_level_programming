#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: The head of the list
 * @number: The number to be inserted
 *
 * Return: Address of the new node otherwise NULL
*/

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *node = *head;

    new = malloc(sizeof(listint_t)); // Allocate space for new node
    if (new == NULL) // Upon failure
    return (NULL);

    new->n = number; // Placed 

    if (node == NULL || node->n >= number)
    {
        new->next = node;
        *head = new;
        return (new);
    }

    while (node && node->next && node->next->n < number)
    node = node->next;

    new->next = node->next;
    node->next = new;

    return (0);
}