# optery_django_project
## Instructions
You have been tasked with building a social network app where a user can post a post, get likes from other users, and users can comment on their post. Your task is to implement the following features:
1. Implement a view to display a list of all posts with their title, content, author, and number of likes. Use HTMX to allow a user to like a post without leaving the page. When a user likes a post, create a new like object and display the updated number of likes in real-time without a page refresh.
2. Implement a view to display the detail of a post. The view should display the title, content, author, and number of likes for the post. Use HTMX to allow a user to comment on the post without leaving the page. The comments should be saved to the database and displayed on the page in real-time without a page refresh.
## Requirements
- Use Django 3.2 or higher.
- Use Python 3.8 or higher.
- Use HTMX for liking a post and commenting on a post.
- Use Django's built-in User model for the author and user fields.
- Use Django's admin customization features to customize the admin interface for the post, like, and comment models.
- Bonus - Customize the django admin to view the post with the htmx view and add a comment as admin.
- Bonus #2 - Extend as many features / functionality as you’d like.
## Submission
Please submit your code as a zip file containing a Django project with the above features implemented. Your submission should include instructions on how to run the project and any relevant notes about the implementation.
