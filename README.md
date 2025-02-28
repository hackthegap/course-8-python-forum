
---

# Forum Application

**Created by Fabricio Braga**  
**Last Updated: February 28, 2025**

---

## Project Overview

This is a simple **Forum Application** built with **Flask**, a Python micro-framework for web development. The application allows users to:

- **Create Topics**: Add new topics with a title, content, and author name.
- **Reply to Topics**: Add replies to existing topics.
- **List Topics**: View all topics along with their replies.

The application demonstrates key Flask concepts, including routing, request handling, templates, and error handling.

---

## Features

- **Create a Topic**: Add a new topic with a title, content, and author name.
- **Reply to a Topic**: Add replies to existing topics.
- **List Topics**: View all topics and their replies in a clean, minimalist design.
- **Navigation Menu**: Easily navigate between the home page and the "Create Topic" page.
- **Flash Messages**: Display success and error messages for user actions.

---

## Technologies Used

- **Flask**: A lightweight Python web framework.
- **Jinja2**: Templating engine for rendering HTML.
- **CSS**: Custom styles for a modern and minimalist design.
- **Python**: Backend logic and application development.

---

## Prerequisites

Before running the project, ensure you have the following installed:

### 1. **Python**
- Download and install Python from [https://www.python.org/](https://www.python.org/).
- Verify the installation:
  ```bash
  python3 --version
  ```

### 2. **Git (Optional)**
- Git is used for version control. You can download it from [https://git-scm.com/](https://git-scm.com/).

---

## Getting Started

Follow these steps to set up and run the project locally.

### 1. **Clone the Repository**

Clone the repository to your local machine:

```bash
git clone https://github.com/hackthegap/course-8-python-forum.git
cd course-8-python-forum
```

### 2. **Set Up a Virtual Environment**

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. **Install Dependencies**

Install the required dependencies:

```bash
pip install Flask
```

### 4. **Run the Application**

Start the Flask development server:

```bash
python3 run.py
```

The application will be available at `http://localhost:5000`.

---

## Project Structure

```
forum-app/
├── app/
│   ├── __init__.py       # Flask application setup
│   ├── routes.py         # Routes and request handling
│   ├── models.py         # Data models (in-memory storage)
├── templates/
│   ├── base.html         # Base template for all pages
│   ├── index.html        # Home page (list of topics)
│   ├── topic.html        # Topic details and replies
│   ├── create_topic.html # Form to create a new topic
│   ├── 404.html          # Custom 404 error page
├── static/
│   ├── styles.css        # Custom CSS styles
├── requirements.txt      # List of dependencies
├── run.py                # Entry point for the application
```

---

## Key Features and Technical Details

### 1. **Routing**
- Routes are defined in `app/routes.py`.
- Key routes:
  - `/`: Home page (lists all topics).
  - `/create_topic`: Form to create a new topic.
  - `/topic/<int:topic_id>`: Displays a topic and its replies.
  - `/topic/<int:topic_id>/reply`: Handles replies to a topic.

### 2. **Templates**
- Uses **Jinja2** for templating.
- Templates are located in the `templates` folder.
- `base.html` is the base template extended by other pages.

### 3. **Static Files**
- Custom CSS styles are located in `static/styles.css`.
- Linked in the `base.html` template using Flask’s `url_for` function.

### 4. **Error Handling**
- Custom 404 error page (`templates/404.html`).
- Flash messages for success and error notifications.

### 5. **In-Memory Data Storage**
- Topics and replies are stored in an in-memory list (`app/models.py`).

---

## Usage

### 1. **Home Page**
- Displays a list of all topics.
- Click on a topic to view its details and replies.

### 2. **Create a Topic**
- Click the "Create Topic" link in the navigation menu.
- Fill out the form and submit to create a new topic.

### 3. **Reply to a Topic**
- Navigate to a topic’s detail page.
- Fill out the reply form and submit to add a reply.

### 4. **Navigation**
- Use the navigation menu at the top of the page to switch between the home page and the "Create Topic" page.

---

## Running Tests

The application includes unit tests for the `ToDoList` class. Run the tests using the following command:

```bash
python3 -m unittest discover tests
```

---

## Deployment

To deploy the application in a production environment:

1. Install **Gunicorn**:
   ```bash
   pip install gunicorn
   ```

2. Run the application with Gunicorn:
   ```bash
   gunicorn run:app
   ```

3. Access the application at `http://localhost:8000`.

---

## Contributing

If you'd like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## Acknowledgments

- This project was created as part of a course to teach Flask and web development.
- Special thanks to the Flask and Python communities for providing excellent resources and tools.

---

## Questions?

If you have any questions or need further assistance, feel free to reach out to the instructor or open an issue in the repository.

---
