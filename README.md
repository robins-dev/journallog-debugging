# Simple python script which will take input as a txt file(here journal_log.txt which contains logs from multiple subsystems) and subsystem name and takes all logs for your subsytem from journal_log.txt and store in other file <subsystem_name>-<log>.txt and all WARNING and ERROR into another file <subsystem_name>-<error>.txt


Script description : It takes all the logs for any specific subsystem from journal log and generate two files for that subsystem
                      1.	File name with <subsystem_name>-<log>.txt        This file contains only your subsystem log
                      2.	File name with <subsystem_name>-<error>.txt     This file contains all WARNING and ERROR log of your subsystem.


Step to execute this script :
               
	python  <script_name>  <journal_log_file_name>  <subsystem_name>
                              
e.g :  > python file_read_write_generic.py journal_log.txt NE3SAgent
               
output : files will be generated in same folder where script and journal log are present.

         NE3SAgent_log.txt
         NE3SAgent_error.txt      

