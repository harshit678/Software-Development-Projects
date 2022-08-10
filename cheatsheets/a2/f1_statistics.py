#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 04 14:45:33 2022
@author: Harshit Handa

This is a file processor that allows to generate relevant statistics from F1 data.
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt


def format_message(message: str) -> str:
    """Formats a message to be printed out to the standard output.

    Parameters
    ----------
    message : str, required
        The message to be printed out to the standard output.

    Returns
    -------
    str
        The formatted message.
    """
    return '[' + sys.argv[0] + ']: ' + message


def main():
    """The main entry of the program.
    """
    # sample call to function
    # print(format_message('hello'))
    # TODO: Your code here.
    """
    Reads argument values and store the values in different lists
    """
    ques = sys.argv[1].split("=")
    ques = ques[1]
    files = sys.argv[2].split("=") 
    files = files[1].split(",")    
    f1_questions(ques, files)
    



def f1_questions(ques,files):
    """
    This function checks which Question number is it and calls other functions accordingly
    """

    if (ques == '1'):
         f1_q1(files)
        
    if (ques =="2"):
         f1_q2(files)

    if (ques == "3"):
         f1_q3(files)

    if (ques == "4"):
         f1_q4(files)

    if (ques == "5"):
         f1_q5(files)

   
def f1_q1(files):
    """
    This function reads the files and answers Question 1. This function uses pandas dataframe to read the data, manipulate the data and to extract required data from the input csv files. 
    This function also uses matplotlib to visualize the output.    
    """    

 
    drivers = pd.read_csv(files[0])
    result = pd.read_csv(files[1])
    result = result.loc[result["positionText"]=="1"]
    result = result.sort_values(by="driverId")
    output = result[["driverId"]].value_counts()
    name = drivers[["driverId", "forename", "surname"]].copy()
    output = pd.DataFrame(output)
    output = output.merge(name,left_on='driverId', right_on='driverId')
    output = output.head(20)
    output["subject"] = output[["forename", "surname"]].apply(" ".join, axis=1)
    output["statistic"] = output.iloc[:,1]
    output = output.drop(output.columns[[0, 1, 2,3]], axis=1)  
    output.to_csv('output.csv', index=False)
    plt.barh(output.subject, output.statistic)
    plt.gca().invert_yaxis()
    plt.title('Who are the top 20 drivers with most wins in F1 history?', fontsize=14)
    plt.xlabel('Race Wins', fontsize=14)
    plt.ylabel('Drivers', fontsize=14)
    plt.savefig("output_graph_q1.pdf", bbox_inches='tight')




def f1_q2(files):
    """
   This function reads the files and answers Question 2. This function uses pandas dataframe to read the data, manipulate the data and to extract required data from the input csv files. 
    This function also uses matplotlib to visualize the output.    
    """    
    
    drivers = pd.read_csv(files[0])
    result = pd.read_csv(files[1])
    result = result.loc[result["positionText"]=="1"]
    output = drivers[["driverId","nationality"]].copy()
    copy_df = result[["driverId", "positionText"]].copy()
    output = output.merge(copy_df,left_on='driverId', right_on='driverId')
    output = output[["nationality"]].value_counts()
    output = pd.DataFrame(output)
    output.reset_index(inplace=True)
    output["subject"] = output.iloc[:,0]
    del output["nationality"]
    output["statistic"] = output.iloc[:,0]
    del output[0]
    output = output.head(10)
    output.to_csv('output.csv', index=False)
    plt.pie(output.statistic,labels=output.subject,autopct='%1.1f%%')
    plt.title(' What are the top 10 countries with most race-winners in F1 history?')
    plt.axis('equal')
    plt.savefig("output_graph_q2.pdf" , bbox_inches='tight')



def f1_q3(files):    
    """
    This function reads the files and answers Question 3. This function uses pandas dataframe to read the data, manipulate the data and to extract required data from the input csv files. 
    This function also uses matplotlib to visualize the output.    
    """    
 
    constructors = pd.read_csv(files[0])
    result = pd.read_csv(files[1])
    result = result.loc[result["positionText"]=="1"]
    output = constructors[["constructorId","name"]].copy()
    copy_df = result[["constructorId", "positionText"]].copy()
    output = output.merge(copy_df,left_on='constructorId', right_on='constructorId')
    output = output[["name"]].value_counts()
    output = pd.DataFrame(output)
    output.reset_index(inplace=True)
    output["subject"] = output.iloc[:,0]
    del output["name"]
    output["statistic"] = output.iloc[:,0]
    del output[0]
    output = output.head(10)
    output.to_csv('output.csv', index=False)
    plt.barh(output.subject, output.statistic)
    plt.gca().invert_yaxis()
    plt.title('What are the top 10 constructors with most wins in F1?', fontsize=14)
    plt.xlabel('Race Wins', fontsize=14)
    plt.ylabel('Constructors', fontsize=14)
    plt.savefig("output_graph_q3.pdf", bbox_inches='tight')





def f1_q4(files):
    """
    This function reads the files and answers Question 4. This function uses pandas dataframe to read the data, manipulate the data and to extract required data from the input csv files. 
    This function also uses matplotlib to visualize the output.    
    """    
        
    circuits = pd.read_csv(files[0])
    races = pd.read_csv(files[1])
    output = circuits[["circuitId","country"]].copy()
    copy_df = races[["circuitId", "raceId"]].copy()
    output = output.merge(copy_df,left_on='circuitId', right_on='circuitId')
    output = output[["country"]].value_counts()
    output = pd.DataFrame(output)
    output.reset_index(inplace=True)
    output["subject"] = output.iloc[:,0]
    del output["country"]
    output["statistic"] = output.iloc[:,0]
    del output[0]
    output = output.head(20)
    output.to_csv('output.csv', index=False)
    plt.bar(output.subject, output.statistic)
    plt.title('What are the top 20 countries with most hosted F1 races?', fontsize=14)
    plt.xlabel('Country', fontsize=14 )
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('No. of Races', fontsize=14)
    plt.savefig("output_graph_q4.pdf", bbox_inches='tight')






def f1_q5(files):
    """
    This function reads the files and answers Question 5. This function uses pandas dataframe to read the data, manipulate the data and to extract required data from the input csv files. 
    This function also uses matplotlib to visualize the output.    
    """    
     
    drivers = pd.read_csv(files[0])
    result = pd.read_csv(files[1])
    result = result[result.grid != 1]
    result = result.loc[result["positionText"]=="1"]
    output = drivers[["driverId", "forename", "surname"]].copy()
    copy_df = result[["driverId","positionText"]].copy()
    output = output.merge(copy_df,left_on='driverId', right_on='driverId')
    output["subject"] = output[["forename", "surname"]].apply(" ".join, axis=1)
    output = output[["subject"]].value_counts()
    output = pd.DataFrame(output)
    output.reset_index(inplace=True)
    output["statistic"] = output.iloc[:,1]
    del output[0]
    output = output.head()
    output.to_csv('output.csv', index=False)
    plt.bar(output.subject, output.statistic, color=[ 'red', 'grey', 'yellow', 'purple', 'green'] )
    plt.title('Who are the top 5 drivers with most wins in F1 history who started a race not being on pole position?', fontsize=14)
    plt.xlabel('Drivers', fontsize=14 )
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('race wins without pole', fontsize=14)
    plt.savefig("output_graph_q5.pdf", bbox_inches='tight')






if __name__ == '__main__':
    main()
