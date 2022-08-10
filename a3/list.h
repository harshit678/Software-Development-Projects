/** @file listy.h
 *  @brief Function prototypes for the linked list.
 */
#ifndef _LINKEDLIST_H_
#define _LINKEDLIST_H_

#define MAX_WORD_LEN 50

/**
 * @brief An struct that represents a node in the linked list.
 */


typedef struct song_t
{
    char artist[80];
    char song[80];
    int year;
    int popularity;
    float danceability;
    float energy;
} song_t;


typedef struct node_t
{  
    song_t *data;
    struct node_t *next;
} node_t;



/**
 * Function protypes associated with a linked list.
 */
node_t *new_node(song_t *data);
node_t *add_front(node_t *, node_t *);
node_t *add_end(node_t *, node_t *);
node_t *add_inorder(node_t *, node_t *);
node_t *peek_front(node_t *);
node_t *remove_front(node_t *);
void apply(node_t *, void (*fn)(node_t *, void *), void *arg);

#endif
