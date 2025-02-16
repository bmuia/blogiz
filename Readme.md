# Blog API

This API allows developers to interact with the Blog Website platform.  You can create, retrieve, update, and delete blog posts, manage user accounts, and more.

## API Endpoints

### Authentication

* **Register:** `POST /api/auth/register/`
    * Parameters: `email` (string, required), `password` (string, required)
* **Login:** `POST /api/auth/login/`
    * Parameters: `email` (string, required), `password` (string, required)
* **Refresh Token:** `POST /api/auth/token/refresh/`
    * Parameters: `refresh_token` (string, required)
* **Password Reset:** `POST /api/password_reset/`
    * Parameters: `email` (string, required)
* **Confirm Password Reset:** `POST /api/password_reset/reset-password-validate/`
    * Parameters: *(Add parameters, e.g., token, new_password)*

### Posts

* **List Posts:** `GET /api/posts/`
    * *(Optional) Query parameters for filtering/pagination*
* **Post Details:** `GET /api/posts/<int:id>/`
    * Parameters: `id` (integer, required)
* **Like Post:** `POST /api/posts/<int:post_id>/like/`
    * Parameters: `post_id` (integer, required)
* **Create Post:** `POST /api/posts/create/`
    * Request Body: *(Specify JSON structure for title, content, etc.)*
* **Delete Post:** `DELETE /api/posts/delete/<int:pk>/`
    * Parameters: `pk` (integer, required)
* **Update Post:** `PUT /api/posts/update/<int:pk>/` *(or PATCH)*
    * Parameters: `pk` (integer, required)
    * Request Body: *(Specify JSON structure for title, content, etc.)*
* **User's Posts:** `GET /api/posts/user/`
    * *(Optional) Query parameters for filtering/pagination*

### Media

* **Serve Media:** `GET /media/<path>`
    * Parameters: `path` (string, required)

## Notes

* Replace placeholders like `*(Add parameters)*` and `*(Specify JSON structure)*` with the actual details.
* This is a simplified README.  For production APIs, include more details about request/response formats, error handling, authentication methods, etc.