# Blog API website

This API allows developers to interact with the Blog Website platform, enabling actions such as creating, retrieving, updating, and deleting blog posts, as well as managing user accounts and comments.

## Features

1. **User Management**:
   - User registration with JWT token generation.
   - User password reset
   - Login and token refresh endpoints.
   
2. **Blog creation**:
   - Create blogs
   - Update blogs
   - Display all the blogs 
   - Display an individual blog
   - Delete a blog

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.12.1
- PostgreSQL >= 14.13
- `pip` (Python package manager)

---

## Installation

### 1. Clone the repository

```bash
git clone git@github.com:bmuia/blogiz.git
cd blogiz
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a .env file in the root directory and add the following variables:

```bash
SECRET_KEY=your_secret_key
#localhost
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port

EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_email_app_password
# Don't use your account password. Instead, use an app password.
# To generate an app password:
# 1. Go to your Google Account settings.
# 2. In the search bar, type "App passwords" and click on it when it appears.
# 3. A pop-up will appear where you can enter a name for the app password.
# 4. Enter the name and click "Generate."
# 5. Copy the generated app password and paste it above for [EMAIL_PASSWORD].

# To use render database instead of localhost
DB_URL=your_render_postgres_internal_url
# To find your internal URL on Render:
# 1. Go to Render and click "New."
# 2. Choose "PostgreSQL."
# 3. Select a free instance and create it.
# 4. Once created, you’ll see the internal URL. Copy it and paste it for [DB_URL].

```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

# API Endpoints

## Authentication

- Register a new user:

  - URL: http://localhost:8000/api/auth/register/

  - Method: POST

  - Body:

```json
{
  "username": "your_username",
  "email": "your_email@example.com",
  "password": "your_password"
}

```
  - Response:
```json
{
  "username": "your_username",
  "email": "your_email@example.com",
  "access": "access_token",
  "refresh": "refresh_token"
}
```
- Login:

  - URL: http://localhost:8000/api/auth/token/login/

  - Method: POST

  - Body:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

  - Response:

```json
{
  "access": "access_token",
  "refresh": "refresh_token"
}
```

- Refresh Token:

  - URL: http://localhost:8000/api/auth/token/login/refresh/

  - Method: POST

  - Body:

```json
{
  "refresh": "refresh_token"
}
```

  - Response:

```json

{
  "access": "new_access_token"
}
```

### Newsletter Subscription
- Subscribe/Unsubscribe:

  - URL: http://localhost:8000/newsletter/subscribe/

  - Method: POST

  - Headers:

```plaintext
Authorization: Bearer <access_token>
```

  - Body:

```bash
{
  "subscribed": true  # or false to unsubscribe
}
```

  - Response:

```bash
{
  "message": "Subscription updated successfully."
}
```
- Check Subscription Status:

  - URL: http://localhost:8000/newsletter/subscribe/

  - Method: GET

  - Headers:

```plaintext
Authorization: Bearer <access_token>
```
  - Response:

```bash
{
  "subscribed": true  # or false
}
```

## Admin Panel
You can access the Django admin panel at `/admin/`. Use the superuser credentials you created earlier to log in.

## Contributing
If you'd like to contribute to this project, please follow these steps:
   1. Fork the repository.

   2. Create a new branch for your feature or bugfix.

   3. Commit your changes and push to your branch.

   4. Submit a pull request.

## License
his project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.



