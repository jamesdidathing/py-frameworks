# py-frameworks

This README guide provides step-by-step instructions on how to set up a repository for practicing with Python frameworks, using a virtual environment (venv). The repository will serve as a dedicated workspace to explore and develop Flask applications.

## Current Progress
- Created home page that displays a couple of mock posts by users, and implements template inheritance for a homepage link.
- Added a login page using flask-wtf to create a form.
- Using SQLite to store users in a database
- Added registration form for new users which will utilise the database, using authentication for usernames and emails
- Added 'Edit Profile' page for users, where they can change username

## Prerequisites

Before proceeding with the repository setup, ensure that you have the following installed:

- Python (version 3.6 or higher)
- `venv` package (usually included with Python)

## Repository Setup

Follow the steps below to set up your repository for practicing Dash:

1. **Create a New Repository**: Start by creating a new repository on your preferred version control platform (e.g., GitHub, GitLab, Bitbucket).

2. **Clone the Repository**: Clone the newly created repository to your local machine using a Git client or the command line. For example:

  ```shell
   git clone <repository-url>
   ```
   
3. **Navigate to the Repository**: Change your working directory to the cloned repository folder:

  ```shell
   cd <repository-folder>
   ```
   
4. **Create a Virtual Environment**: Set up a virtual environment using the venv module. Run the following command:

 ```shell
   python -m venv venv
   ```

5. **Activate the Virtual Environment**: Activate the newly created virtual environment. The process varies depending on your operating system:
### Windows:

 ```shell
   venv\Scripts\activate
   ```

### macOS/Linux:

 ```shell
   source venv/bin/activate
   ```

6. **Install Dependencies**: Install the required packages and dependencies for Dash by using the package manager pip.

 ```shell
   pip install -r requirements.txt
   ```

This will install the Dash package and any additional dependencies specified.
