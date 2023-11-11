# EdumPass - Learning Management System (LMS) Project

Welcome to the EdumPass Learning Management System (LMS) project! This project is developed using Vue.js for the front end and Django for the backend.

## Project Overview

1. Base Templates Setup:
   - Implemented base templates for the front page, about page, and login/sign up pages.

2. Authentication:
   - Implemented user authentication, allowing users to sign up, log in, and log out.

3. Courses Page:
   - Set up HTML for the courses page.
   - Used Axios to fetch course data from the Django backend using Django REST framework.

4. Course Detail Page:
   - Enabled clicking on a course to view the detail page.
   - Restricted access to courses based on authentication.

5. Lessons Implementation:
   - Set up database models for lessons.
   - Used Axios to fetch lesson information and display it in the browser.
   - Implemented comments functionality for lessons.

6. Additional Features:
   - Added validation to the comments form.
   - Displayed the comment list.
   - Converted the course list object to a component.
   - Showed newest courses on the front page.
   - Added thumbnails to courses.

7. Categories Functionality:
   - Implemented functionality around course categories.

8. General Enhancements:
   - Fixed issues in the admin interface.
   - Improved data loading when not authenticated.

9. Quiz Implementation:
   - Created a database model for quizzes.
   - Registered quizzes in the admin panel.
   - Implemented a serializer for quizzes.
   - Created views for quizzes and questions.
   - Enabled answering quizzes and disabled comments for quizzes.

10. Embedding YouTube Videos:
    - Made it possible to embed YouTube videos into lessons.
    - Tracked user progress in courses.

11. Tracking Mechanism:
    - Set lessons as started when initiated.
    - Enabled marking a lesson as done.

12. Author Management:
    - Added authors to courses.
    - Created an author detail page.

13. Course Creation by Authors:
    - Began work on letting authors create their own courses.

14. Author-Created Courses with Lessons:
    - Continued working on letting authors create courses with lessons.


## Technologies Used

- **Frontend:**
  - Vue.js
  - Bulma
  - Axios

- **Backend:**
  - Django
  - Djoser
  - Django REST framework
  - CORSheaders
  - Django Authtoken


## Setup Instructions

1. Clone the repository.
2. Set up the frontend and backend environments.
3. Run the development servers.

Feel free to contribute or provide feedback!

