# 👥 Team Availability Tracker

### A Python Flask and SQLite-Based Web Application

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)
![HTML5](https://img.shields.io/badge/HTML5-Frontend-orange?logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-Styling-blue?logo=css3)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

## 📌 1. Project Overview

The **Team Availability Tracker** is a web-based application developed using Python Flask, HTML, CSS, and SQLite.

The application provides a dashboard that displays a list of team members along with their respective roles and availability statuses.

Users can change an individual's availability using an interactive toggle button. Whenever a toggle is clicked, the application updates the corresponding Boolean value in the SQLite database and reflects the updated status on the frontend.

The application uses conditional rendering to visually distinguish between available and busy team members.

This project demonstrates database integration, Boolean data management, interactive frontend components, and synchronization between the backend and frontend.

## 🎯 2. Project Objective

The main objective of this project is to develop a team management dashboard that allows users to view and update the availability status of different team members.

The project focuses on:

- Developing a web application using Python Flask.
- Displaying team member information dynamically.
- Implementing interactive availability toggles.
- Understanding Boolean values in databases.
- Updating database records based on user interactions.
- Implementing conditional rendering.
- Synchronizing frontend and backend data.
- Managing team availability information using SQLite.

## ✨ 3. Key Features

### 1. Team Member Listing
The application displays a list of team members along with their names and professional roles.

### 2. Interactive Availability Toggle
Users can change a team member's availability using an interactive toggle button.

### 3. Boolean Database Updates
Availability is stored as a Boolean-style integer value in SQLite:
- `1` represents Available.
- `0` represents Busy.

### 4. Dynamic Status Updates
When a toggle is clicked, the backend updates the corresponding database value.

### 5. Conditional Rendering
The frontend visually displays different status indicators based on each member's availability.

### 6. Team Availability Summary
The dashboard displays the number of available team members compared with the total number of members.

### 7. Persistent Data Storage
Availability changes remain saved in the SQLite database even after refreshing or restarting the application.

### 8. User Feedback
The application displays success and error messages after availability updates.

### 9. Responsive Interface
The application uses CSS to provide a clean layout across different screen sizes.

## 🛠️ 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| SQLite | Database management |
| HTML5 | Frontend structure |
| CSS3 | Styling and layout |
| Jinja2 | Dynamic HTML rendering |
| HTTP GET | Retrieving team information |
| HTTP POST | Updating availability |
| VS Code | Development environment |
| GitHub | Source code management |

## 📂 5. Project Folder Structure

```text
Team-Availability-Tracker/
│
├── app.py
│
├── requirements.txt
│
├── team_availability.db
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

**Note:** The `team_availability.db` database file is automatically generated when the application is first executed.

### File Description

**app.py**
- Contains the main Flask application.
- Defines application routes.
- Initializes the SQLite database.
- Creates the team members table.
- Inserts initial team member records.
- Retrieves team member information.
- Handles availability toggle requests.
- Updates Boolean availability values.
- Calculates the total number of available members.

**requirements.txt**
- Contains the Python dependencies required for the application.
- Specifies Flask as the main web framework.

**team_availability.db**
- SQLite database used to store team member information.
- Stores names, roles, and availability statuses.
- Maintains updated availability information.

**templates/index.html**
- Contains the frontend HTML structure.
- Displays the team dashboard.
- Shows member names and roles.
- Provides interactive toggle buttons.
- Displays availability status indicators.
- Uses Jinja2 expressions for dynamic content rendering.

**static/style.css**
- Contains the application's styling.
- Defines the dashboard layout.
- Styles team member rows and status indicators.
- Designs the availability toggle buttons.
- Implements responsive styling and hover effects.

## ⚙️ 6. System Requirements

The following tools and software are required:

- Python 3.x
- Visual Studio Code
- Flask framework
- SQLite database
- Google Chrome or another modern web browser

## 🚀 7. Installation and Setup

Follow these steps to run the project locally.

### Step 1: Clone the Repository

```bash
git clone https://github.com/Arshi-yaaaa/Team-Availability-Tracker.git
```

### Step 2: Open the Project Folder

```bash
cd Team-Availability-Tracker
```

Open the folder using Visual Studio Code.

### Step 3: Install Dependencies

Execute the following command in the terminal:

```bash
py -m pip install -r requirements.txt
```

This installs the Flask framework required for the application.

### Step 4: Run the Application

Execute:

```bash
py app.py
```

The Flask development server will start, and the SQLite database will be initialized automatically.

### Step 5: Open the Application

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

The Team Availability Tracker dashboard will now be displayed.

## 🔄 8. Application Workflow

The application follows a frontend-backend-database workflow.

1. The user opens the Team Availability Tracker.
2. Flask retrieves team member information from the SQLite database.
3. The backend calculates the total number of available members.
4. The information is passed to the HTML template.
5. The frontend displays team members, roles, and availability statuses.
6. The user selects an availability toggle.
7. The browser sends an HTTP POST request to the Flask backend.
8. Flask identifies the selected team member using their unique ID.
9. The backend retrieves the current availability value.
10. The Boolean-style value is changed from `1` to `0` or from `0` to `1`.
11. The SQLite database is updated.
12. The application redirects to the dashboard.
13. The updated status is retrieved and displayed on the frontend.

## 🧠 9. Backend Implementation

The backend is developed using Python Flask.

### Flask Application

Flask is used to create and manage the web application.

### Routing

The application contains two main routes.

**Home Route (`/`)**
- Handles GET requests.
- Retrieves all team member records.
- Calculates the number of available members.
- Displays the dashboard.

**Toggle Route (`/toggle/<member_id>`)**
- Handles POST requests.
- Identifies the selected team member.
- Retrieves the current availability status.
- Changes the availability value.
- Updates the database.
- Redirects the user to the dashboard.

### Availability Toggle Logic

The application uses conditional logic to switch availability.

- If the current value is `1`, it changes to `0`.
- If the current value is `0`, it changes to `1`.

### Database Update

The updated availability value is stored in SQLite using an SQL UPDATE statement.

### Template Rendering

The `render_template()` function passes team member information to the HTML frontend using Jinja2.

## 🗄️ 10. Database Implementation

SQLite is used as the database management system.

The database is automatically initialized when the application starts.

### Database Table: team_members

| Column | Data Type | Description |
|---|---|---|
| id | INTEGER | Unique team member identifier |
| name | TEXT | Team member's name |
| role | TEXT | Professional role |
| available | INTEGER | Availability status (0 or 1) |

### Initial Team Members

The application starts with six sample team members:

| Name | Role | Initial Status |
|---|---|---|
| Alex Rivers | Senior Developer | Available |
| Maya Chen | UX Designer | Busy |
| Jordan Taylor | Project Manager | Available |
| Sofia Garcia | Marketing Lead | Busy |
| Noah Williams | Backend Developer | Available |
| Ava Patel | Data Analyst | Available |

### SQL Operations Used

**CREATE TABLE**

Creates the team members table if it does not already exist.

**INSERT**

Adds the initial team member records when the database is empty.

**SELECT**

Retrieves team member details and availability values.

**UPDATE**

Changes the availability status of a selected team member.

## 🔀 11. Boolean Values and Conditional Rendering

One of the important concepts demonstrated in this project is Boolean data management.

The availability column stores integer values representing Boolean states.

| Database Value | Availability | Frontend Display |
|---|---|---|
| 1 | True | AVAILABLE |
| 0 | False | BUSY |

The frontend uses conditional expressions to display the appropriate status.

For example:

```python
'AVAILABLE' if member.available else 'BUSY'
```

The CSS classes also change depending on the stored value.

- Available members display a green status indicator.
- Busy members display an orange status indicator.

This demonstrates how backend data controls the visual appearance of frontend components.

## 🎨 12. Frontend Implementation

The frontend is developed using HTML5 and CSS3.

### HTML Components

- Application heading.
- Team overview section.
- Available member count.
- Team member table.
- Member names and roles.
- Availability status indicators.
- Interactive toggle buttons.
- Success and error messages.

### CSS Components

- Modern dashboard layout.
- Gradient header background.
- White content cards.
- Circular member avatars.
- Green and orange status indicators.
- Interactive toggle switches.
- Rounded corners and shadows.
- Responsive table layout.
- Mobile-friendly styling.

## 🧪 13. Testing and Verification

The application supports the following testing scenarios.

| Test Case | Expected Result |
|---|---|
| Open the application | Team dashboard displayed |
| View team members | Names and roles displayed |
| Toggle an available member | Status changes to Busy |
| Toggle a busy member | Status changes to Available |
| Refresh the webpage | Updated status remains |
| Restart the application | Saved availability remains |
| Toggle different members | Only selected member is updated |
| Check availability summary | Correct available count displayed |
| Submit an invalid member ID | Error feedback displayed |

## 🔐 14. Error Handling and Data Management

Basic error handling and database management techniques are implemented.

- Invalid team member IDs are handled.
- Database queries use parameterized values.
- Availability is restricted to valid values of `0` and `1`.
- Database connections are managed using context managers.
- Existing member records are preserved.
- Availability updates are stored persistently.
- User feedback messages are displayed after updates.

## 📸 15. Application Output

The application successfully displays a team availability dashboard.

Users can view:
- Team member names.
- Professional roles.
- Current availability status.
- Interactive availability toggles.
- Total number of available members.

Whenever an availability toggle is changed, the database is updated and the frontend displays the new status.

The application demonstrates synchronization between database values and frontend presentation.

## 📚 16. Learning Outcomes

Through this project, I gained practical experience in:

- Developing web applications using Python Flask.
- Connecting Python applications with SQLite.
- Creating and managing database tables.
- Performing SQL INSERT, SELECT, and UPDATE operations.
- Understanding Boolean values in databases.
- Implementing interactive toggle functionality.
- Handling HTTP GET and POST requests.
- Implementing conditional rendering using Jinja2.
- Synchronizing frontend and backend information.
- Dynamically updating database records.
- Designing responsive dashboards using CSS.
- Managing persistent application data.
- Organizing source code using GitHub.

## 🔮 17. Future Enhancements

The application can be further improved by introducing:

- User authentication and login.
- Admin dashboard for managing team members.
- Ability to add and remove team members.
- Search and filtering functionality.
- Real-time updates without page refreshing.
- Department-wise availability tracking.
- Availability history and activity logs.
- Team member profile pictures.
- Exporting availability reports.
- Integration with calendar applications.

## 🏁 18. Conclusion

The Team Availability Tracker successfully demonstrates how Python Flask, SQLite, HTML, and CSS can be integrated to develop an interactive team management application.

The application allows users to view team members and manage their availability through interactive toggle buttons.

By implementing Boolean database values, conditional rendering, and persistent data storage, this project provides practical experience in backend development, database management, and frontend-backend synchronization.

This project strengthened my understanding of full-stack web development and interactive database-driven applications.

## 👩‍💻 19. Developer Information

**Developed by:** Arshiya Thaslim K

**Domain:** Full Stack Development

**Project:** Team Availability Tracker

**Internship Organization:** VirtualWorks

**Project Number:** Task 5

**Task ID:** task5

**GitHub Repository:**

https://github.com/Arshi-yaaaa/Team-Availability-Tracker

---
