# Optery Connect - Take Home Assignment
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

# Assignment

## Achievements
* :white_check_mark: Used Django 4.2.
* :white_check_mark: Used Python 3.11.
* :white_check_mark: Implemented HTMX for liking a post and commenting on a post.
* :white_check_mark: Used Django's built-in User model for the author and user fields.
* :white_check_mark: Customized the Django admin interface for the post, like, and comment models.
* :x: Bonus: Customized the Django admin to view the post with the HTMX view and add a comment as admin.
> Some customizations were made to the Django admin interface to improve navigability but no with HTMX.
* :white_check_mark: Bonus #2: Extended the features/functionality as desired.
>1. The Registration, Login and Logout for the User were made as the Post, Likes and Comments are related to a User.
>2. A Search feature was implemented to look for Users and Posts.

## Data
The following Users were created. The password for all of them was set up as `P@ssw0rd!`:
- Optery | Superuser: ☑️
- Claudia | Superuser: ☑️
- CyberNinja21
- DataGuardianX
- TechSavvyHacker
- EncryptionMaster99
- NetworkProtector27

## Instructions for Implementation
1. Install Python and the virtualenv package for Python in case they are not installed in the local machine.
```
brew install python
pip install virtualenv
```
2. Get the project repository. For this you can either:
- Clone the git repository: 
```
git clone git@github.com:claugf/optery_django_project.git
```
- Unzip the sent file and copy to your local machine.
3. Access to the project repository.
```
cd optery_django_project/
```
4. Create virtual environment.
```
virtualenv env
```
5. Activate the virtual environment.
```
source env/bin/activate
```
6. Install project dependencies
```
python -m pip install -r requirements.txt 
```
7. Run the server
```
python manage.py runserver
```
8. Browse to: http://127.0.0.1:8000/
