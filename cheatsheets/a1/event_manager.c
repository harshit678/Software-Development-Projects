/** @file event_manager.c
 *  @brief A pipes & filters program that uses conditionals, loops, and string processing tools in C to process iCalendar
 *  events and printing them in a user-friendly format.
 *  @author Felipe R.
 *  @author Hausi M.
 *  @author Juan G.
 *  @author Harshit H.
 *
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

/**
 * @brief The maximum line length.
 *
 */
#define MAX_LINE_LEN 132

/**
 * Function: main
 * --------------
 * @brief The main function and entry point of the program.
 *
 * @param argc The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @return int 0: No errors; 1: Errors produced.
 *
 */
int count;

struct manage {
    char dates[81];
    char datee[81];
    char freq[81];
    char wkst[81];
    char until[81];
    char byday[81];
    char location[81];
    char summary[81];
};

struct manage event_array[500];

int read_ical_line(char *file);

int process_ical_line(int ystart, int mstart, int dstart, int yend, int mend, int dend,int max, struct manage *event_array);


int main(int argc, char *argv[])
{
    // TODO: your code.
    char *start;
    char *end;
    char *ics_file;
    int ystart, mstart, dstart, yend,mend,dend,max ;

    /* get the start date , end date and file from the argument*/
    
    start = strtok(argv[1] , "=");
    start = strtok(NULL, start);
    sscanf(start, "%d/%d/%d", &ystart, &mstart, &dstart);
  
    end = strtok(argv[2] , "=");
    end = strtok(NULL, end);
    sscanf(end, "%d/%d/%d", &yend, &mend, &dend);
    end = strtok(argv[2] , "=");

    ics_file = strtok(argv[3], "=");
    ics_file = strtok(NULL, "=");
    
    max = read_ical_line(ics_file);
    
    process_ical_line(ystart, mstart, dstart, yend,mend,dend,max,&event_array[0]); 
    
    exit(0);
}


/* this function will read all the values from the file and it will store the values in the struct defined above
   each value is stored in a specific struct value  */


int read_ical_line(char *file){
    FILE *ics_file;
    count = 0;
    char str[MAX_LINE_LEN];
    char *store, *check;
    ics_file = fopen(file, "r");
   
    while(fgets(str, MAX_LINE_LEN, ics_file) != NULL){
         store = strtok(str, ":");
         if (!strcmp(store, "DTSTART")) {
                    check = strtok(NULL,"\n");
                    strncpy(event_array[count].dates,check,strlen(check));

        } else if (!strcmp(store, "DTEND")) {
                    check = strtok(NULL,"\n");
                    strncpy(event_array[count].datee,check,strlen(check));

        } else if (!strcmp(store, "LOCATION")) {
                    check = strtok(NULL,"\n");
                    if (check != NULL) {
                        strncpy(event_array[count].location,check,strlen(check));
                    }

        } else if (!strcmp(store, "SUMMARY")) {
                    check = strtok(NULL,"\n");
                    strncpy(event_array[count].summary,check,strlen(check));

                    count += 1;
                }
            }

    fclose(ics_file);
    return count;


}

/*  this function takes the start and end value from the main function and take the values from the struct
 to print out the specific output required by this program*/

int process_ical_line(int ystart, int mstart, int dstart, int yend, int mend, int dend,int max,struct manage *pointer_array ){
    int i = 0;
    struct tm date_s, date_e, am_pm ;
    char *am = "AM";
    char *pm = "PM";
    int counter = 0; 
    char *dt_s, *dt_e, *time_s, *time_e, formatted_date[40];


    while(i < max){
   
        dt_s = strtok(pointer_array[i].dates,"T"); 
        time_s = strtok(NULL,"\n"); 
        dt_e = strtok(pointer_array[i].datee,"T"); 
        time_e = strtok(NULL,"\n");
        sscanf(dt_s, "%4d%2d%2d", &date_s.tm_year, &date_s.tm_mon, &date_s.tm_mday);
        sscanf(dt_e, "%4d%2d%2d", &date_e.tm_year, &date_e.tm_mon, &date_e.tm_mday);
       
       
        if (date_s.tm_year >= ystart && date_e.tm_year <= yend && ((date_s.tm_mon >= mstart && date_e.tm_mon < mend && date_s.tm_mday >= dstart) || (date_s.tm_mon > mstart && date_e.tm_mon <= mend && date_e.tm_mday <= dend) || (date_s.tm_mon > mstart && date_e.tm_mon < mend) ||  (date_s.tm_mon == mstart && date_e.tm_mon == mend && (date_s.tm_mday >= dstart && date_s.tm_mday <= dend)))) {

       
        if (i == 0 || strncmp(pointer_array[i].dates,pointer_array[i-1].dates,9) ){
           if (counter >0){ printf("\n");}
        
        date_s.tm_year -= 1900; 
        date_s.tm_mon -= 1; 
        strftime(formatted_date, 40, "%B %d, %Y", &date_s);
        puts(formatted_date);
        int dashc = strlen(formatted_date);
        char dash = '-';
        for (int k = 0; k < dashc; k ++) {
            putchar(dash);
        } printf("\n");       
       } 
        sscanf(time_s, "%2d%2d", &date_s.tm_hour, &date_s.tm_min);
        sscanf(time_e, "%2d%2d", &date_e.tm_hour, &date_e.tm_min);
        
         if (date_s.tm_hour > 12) {
                date_s.tm_hour -= 12;
                printf("%2d:%02d ", date_s.tm_hour, date_s.tm_min);
            } 
        
        else {
                printf("%2d:%02d ", date_s.tm_hour, date_s.tm_min);
            }   
         
        sscanf(time_s, "%2d", &am_pm.tm_hour);
        if (am_pm.tm_hour == 12) {
             printf("%s to ", pm);
        } else if (am_pm.tm_hour >= 13) {
            printf("%s to ", pm);
        } else {
            printf("%s to ", am);
        }
   
         if (date_e.tm_hour > 12) {
                date_e.tm_hour -= 12;
                printf("%2d:%02d ", date_e.tm_hour, date_e.tm_min);
            } 

        else {
                printf("%2d:%02d ", date_e.tm_hour, date_e.tm_min);
            }        

        sscanf(time_e, "%2d", &am_pm.tm_hour);
        if (am_pm.tm_hour == 12) {
             printf("%s: ", pm);
        } else if (am_pm.tm_hour >= 13) {
            printf("%s: ", pm);
        } else {
            printf("%s: ", am);
        }
        
        if (pointer_array[i].summary != NULL) {
                printf("%s ", pointer_array[i].summary);
            }

        printf("{{%s}}\n", pointer_array[i].location);
        counter++;    
    }

    i++;

}
}


