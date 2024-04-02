# result-fetcher
Objective:
The objective of the code is to automate the process of fetching the results of multiple students from a website and storing the data in an Excel file.

Tools Used:
Python: The programming language used to write the script.
Selenium: A web automation tool used to interact with the website.
Excel: Used to store the fetched data in an organized manner.

Steps in the Process:
Input Data Preparation: The user prepares an Excel file containing student registration numbers and their subjects. Each row in the Excel file represents a student, with registration number in one column and subject in another.

Execution of the Code: The user executes the Python script.

Script Execution: The script uses Selenium to automate the process of fetching results from a website.
It opens a web browser (e.g., Chrome, Firefox) and navigates to the website where student results are available.

Data Retrieval: The script iterates through each row of the input Excel file. For each student, it extracts the registration number and subject. It enters the registration number into the website's search or input field and selects the appropriate subject. It then retrieves the student's result from the website.

Data Storage: The script organizes the fetched data, typically in a dictionary or list format, containing the student's information and result.
It writes this data into an Excel file, usually with each student's information in a separate row and their result in corresponding columns.

Excel File Creation: The script creates an Excel file, typically named data1.xlsx, to store the fetched results. The Excel file is populated with the fetched data, making it easy for the user to view and analyze the results.

User Interaction: The user interacts with the script by providing the input Excel file containing student information. Once the script is executed, it operates without further intervention, automating the entire process of fetching results and storing them in an Excel file.

Expected Output: Upon successful execution, the script generates an Excel file (data1.xlsx) containing the fetched results, organized in a format suitable for analysis.
By automating the process, the code streamlines the task of fetching results for multiple students, saving time and effort compared to manual retrieval.
