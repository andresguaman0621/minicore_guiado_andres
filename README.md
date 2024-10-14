Project Description
The Task Manager is a web application built using Django and Python that allows users to efficiently manage their tasks. Users can create, update, delete, and organize tasks, making it easier to keep track of their responsibilities. This project aims to provide a user-friendly interface for task management, addressing the common challenges of organization and prioritization.
Motivation
The motivation behind this project is to simplify task management for users who struggle with keeping track of their daily responsibilities. By providing an intuitive platform, we hope to enhance productivity and reduce stress.
Problem Solved
This application solves the problem of task overload by allowing users to categorize and prioritize their tasks effectively. It also offers features like deadlines and reminders to help users stay on track.
Table of Contents
Installation
Usage
Features
Contributing
License
Installation
To install the Task Manager application, follow these steps:
Clone the repository:
bash
git clone https://github.com/andresguaman0621/minicore_guiado.git

Navigate into the project directory:
bash
cd minicore_guiado

Create a virtual environment:
bash
python -m venv venv

Activate the virtual environment:
On Windows:
bash
venv\Scripts\activate

On macOS/Linux:
bash
source venv/bin/activate

Install the required dependencies:
bash
pip install -r requirements.txt

Run database migrations:
bash
python manage.py migrate

Start the development server:
bash
python manage.py runserver

Usage
Once the server is running, navigate to http://127.0.0.1:8000 in your web browser. You can create an account or log in to access your task management dashboard.
Example Usage
Creating a Task: Click on "Add Task" and fill in the details.
Updating a Task: Click on the task you wish to update, make changes, and save.
Deleting a Task: Click on the delete icon next to the task.
Features
User authentication (registration and login)
Create, update, and delete tasks
Categorization of tasks (e.g., work, personal)
Deadline setting and reminders
Contributing
Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Follow these guidelines for contributions:
Ensure your code follows our coding standards.
Write tests for new features.
Update documentation as needed.
License
This project is licensed under the MIT License - see the LICENSE file for details. Feel free to reach out if you have any questions or need further assistance!
