# KisanChikitsa Project

## Overview
KisanChikitsa is a web application designed for user account management, allowing users to sign up and sign in to access various features related to agricultural support and information.

## Project Structure
The project is organized into two main directories: `backend` and `frontend`.

### Backend
The backend is built using Django and contains the following components:

- **manage.py**: Command-line utility for managing the Django project.
- **kisan_chikitsa/**: Main Django project directory containing:
  - **settings.py**: Configuration settings for the Django project.
  - **urls.py**: URL routing for the project.
  - **wsgi.py**: Entry point for WSGI-compatible web servers.
- **accounts/**: Django application for user account management, including:
  - **models.py**: Defines user account data models.
  - **views.py**: Contains logic for user registration and authentication.
  - **serializers.py**: Serializes user data for API responses.
  - **urls.py**: URL routing specific to account-related views.

### Frontend
The frontend consists of HTML files for user interaction:

- **signup.html**: User interface for creating a new account.
- **signin.html**: User interface for logging into an existing account.

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd kisan-chikitsa
   ```

2. **Set up a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```
   python backend/manage.py migrate
   ```

5. **Start the development server**:
   ```
   python backend/manage.py runserver
   ```

## Features
- User registration and authentication.
- Responsive design for mobile and desktop users.
- Secure password handling and validation.

## Usage
- Navigate to `http://localhost:8000/signup` to create a new account.
- Navigate to `http://localhost:8000/signin` to log into your account.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.