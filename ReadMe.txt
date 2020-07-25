Read Me

Instructions: 

	Enter Location options under variable loc:
		Brookfield
		Gray
		Melcor
		Remington
		Saddletowne
		Shane
		Shawnessy
		South Health

	Enter first name under variable fname

	Enter last name under variable lname

	Enter date of birth day under variable dobD

	Enter date of birth year under variable dobY

	Enter date of birth month options under variable dobM
		Jan
		Feb
		Mar
		Apr
		May
		Jun
		Jul
		Aug
		Sep
		Oct
		Nov
		Dec

	Enter email address under variable email

	Enter phone number under variable phone

	Save script with as a python file (fileName.py)


Automation Process
	
For PC
	1. Create a batch file to to run on the python script

		i) Open a text/notepad file then apply instructions 
			"Path where your Python exe is stored\python.exe" "Path where your Python script is stored\scriptname.py" pause

		ii) Save the file with the extension .bat (fileName.bat)

	2. Schedule the script with Windows Scheduler 
		
		i) Open administrative tools

		ii) Double click task scheduler and choose ‘Create Basic Task’

		iii) Name the Task, select the time frame you would like the to perform (ie daily at 6am)

		iv) Select the action function and select start a program 

		v) Use the browse function or paste the path where your bat file is located
 
		vi) select finish 

For Mac 
	1. Create an Executable file
		i) Save the file with no file extension from ide to convert into a Unix executable or 

			- open a text editor and type 
				 Python “Path where your Python exe is stored.py” fileName

			- make sure there is no file extension specified 

			- Open terminal and type 
				chmod 755 “path where your document is saved”

			- this will save it as a unix executable

		ii) Open the application automator 

		iii) Select application 

		iv) Under the actions box search “Get specific finder item” and double click it

		v) Click the add button and select your Unix executable
 
		vi) Save your file with a .app extension 

	2.  Create a Custom calendar event to schedule run time

		i) Open Calendar and create a new event with the time you want the script to run 

		ii) Add an alert and select custom 

		iii) Under message with sound select Open file

		iv) Under Calendar select Other and find your application within finder 

		v) Select At time of event and select ok

		vi) Finally select repeat daily and save the calendar event 
	





