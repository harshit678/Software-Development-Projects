/** @file song_analyzer.c
 *  @brief A small program to analyze songs data.
 *  @author Mike Z.
 *  @author Felipe R.
 *  @author Hausi M.
 *  @author Juan G.
 *  @author Harshit Handa
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"

#define MAX_LINE_LEN 80
int count = 0;
node_t *head_node = NULL , *current_node = NULL ;

// Function to write the data of linked list onto the output.csv file with required the output

void OutputLinkedList(node_t* head_node, FILE* fp, int num, char* sort){
    
    struct node_t* temp = head_node;
    if(strcmp(sort,"popularity")==0){
        fprintf(fp,"artist,song,year,popularity\n");
        while (temp->next != NULL)
        {
        if(count == num){break;}
        fprintf(fp, "%s,%s,%d,%d\n", temp->data->artist, temp->data->song, temp->data->year, temp->data->popularity);
        temp = temp->next;
        count++;
        
        }
    }
    else if(strcmp(sort,"danceability")==0){
        fprintf(fp,"artist,song,year,danceability\n");
        while (temp->next != NULL)
        {
        if(count == num){break;}
        fprintf(fp, "%s,%s,%d,%g\n", temp->data->artist, temp->data->song, temp->data->year, temp->data->danceability);
        temp = temp->next;
        count++;
        
        }
    }
    else{
        fprintf(fp,"artist,song,year,energy\n");
        while (temp->next != NULL)
        {
        if(count == num){break;}
        fprintf(fp, "%s,%s,%d,%g\n", temp->data->artist, temp->data->song, temp->data->year, temp->data->energy);
        temp = temp->next;
        count++;
        
        }
    }
    
}

// Function to sort the linked list according to the column provided from the command line
void SortLinkedList(node_t* head_node,FILE* file, int num, char* sort )
{
    struct node_t *node=NULL, *temp = NULL;
    song_t* tempvar;
    node = head_node;
   
    if(strcmp(sort,"popularity")==0){
        
        while(node != NULL)
        {   
            temp = node->next;
            
            while(temp != NULL)//travel till the second last element 
            {
            if(node->data->popularity == temp->data->popularity){
                    
                    if (strcmp(node->data->song, temp->data->song) < 0)
                    {
                        tempvar = node->data;
                        node->data = temp->data; // swap
                        temp->data  = tempvar;
                    
                    }
                }

                if(node->data->popularity < temp->data->popularity)// compare the data of the nodes 
                {   
                
                tempvar = node->data;
                node->data = temp->data; //swap
                temp->data  = tempvar;
                
                
                }           
                temp = temp->next;
            }
            node = node->next;
        }
    }
    else if(strcmp(sort,"danceability")==0){
        while(node != NULL)
        {   
            temp = node->next;
            
            while(temp != NULL)//travel till the second last element 
            {
            if(node->data->danceability == temp->data->danceability){
                    
                    if (strcmp(node->data->song, temp->data->song) < 0)
                    {
                        tempvar = node->data;
                        node->data = temp->data; // swap
                        temp->data  = tempvar;
                    
                    }
                }

                if(node->data->danceability < temp->data->danceability)// compare the data of the nodes 
                {   
                
                tempvar = node->data;
                node->data = temp->data; //swap
                temp->data  = tempvar;
                
                
                }           
                temp = temp->next;
            }
            node = node->next;
        }
    }
    else{
        while(node != NULL)
        {   
            temp = node->next;
            
            while(temp != NULL)//travel till the second last element 
            {
            if(node->data->energy == temp->data->energy){
                    
                    if (strcmp(node->data->song, temp->data->song) < 0)
                    {
                        tempvar = node->data;
                        node->data = temp->data; //swap
                        temp->data  = tempvar;
                    
                    }
                }

                if(node->data->energy < temp->data->energy)// compare the data of the nodes 
                {   
                
                tempvar = node->data;
                node->data = temp->data; // swap
                temp->data  = tempvar;
                
                
                }           
                temp = temp->next;
            }
            node = node->next;
        }
    }
    OutputLinkedList(head_node, file,num,sort);
}

// Function to store the values provided by the file from the command line to the Linked List 

void makelinkedlist(FILE* song_file){
    
    char row, column , *artist , *song ;
    char *year;
    char *popularity,*danceability,*energy;
    song_t* songs;
    char str[1024]={0};

    while (fgets(str, 1024, song_file)) {

        column = 0;
        
        row++;
        if (row == 1){
        continue;
        }
        char* value = strtok(str, ",");
        
        // storing the values of the required columns to specific variables

        while (value) {
            
            if (column == 0) {
            artist = value;
            }
            
            if (column == 1) {
            song = value;
            }

            if (column == 4) {
            year = value;
            }

            if (column == 5) {
            popularity = value;
            }

            if (column == 6) {
            danceability = value;
            }

            if (column == 7) {
            energy = value;
            }

            value = strtok(NULL, ",");
            column++;
            
        }
            // creating the linked list and storing values
    
            songs = (song_t *)malloc(sizeof(song_t));
            strcpy(songs->artist , artist);
            strcpy(songs->song , song); 
            songs->year = atoi(year);
            songs->popularity = atoi(popularity);
            songs->danceability = atof(danceability);
            songs->energy = atof(energy);
            current_node = new_node(songs);
            head_node = add_front(head_node, current_node);
          
    } 

}
/**
 * @brief The main function and entry point of the program.
 *
 * @param argc The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @return int 0: No errors; 1: Errors produced.
 *
 */
int main(int argc, char *argv[])
{
    // Initial dummy code
    char *files;
    int   num ;

    // getting the values from the command line    

    char *sort = strtok(argv[1] , "=");
    sort = strtok(NULL, "=");
  
    char *display = strtok(argv[2] , "=");
    display = strtok(NULL, display);
    num = atoi(display);
    
    files = strtok(argv[3], "=");
    files = strtok(NULL, "=");

    FILE *song_file;
    FILE* file;
    file = fopen ("output.csv", "w");
    
    song_file = fopen(files, "r");
    makelinkedlist(song_file);
    SortLinkedList(head_node, file, num, sort);
    fclose(file);
    fclose(song_file);

    // deallocating the dynaminc memory    
 
    node_t *temp_n = NULL;
    for (; head_node != NULL; head_node = temp_n)
    {
        temp_n = head_node->next;
        free(head_node);
    }
    free(head_node);

    exit(0);
}


