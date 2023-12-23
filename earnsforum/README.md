Earns Blog
Introduction
Welcome to Earns Blog, a dynamic platform where imagination flows freely through captivating articles and stories. Our blog is a unique space where readers can immerse themselves in a world of fantasy, creativity, and knowledge. Whether you're looking for a quick read or an in-depth story, Earns Blog offers a rich and varied collection of content.

Features
Fantasy Articles & Stories: Dive into a variety of imaginative articles and stories, each offering a unique escape into realms of fantasy and creativity.
Save Favorites: Logged-in users can save articles and stories for later reading.
Anonymous Comments: Engage with the community through anonymous comments on articles and stories.
Profile Customization: Personalize your experience by modifying your profile.
Super User Story Creation: As a super user, easily create stories by adding images and text. Craft your content like a comic book with multiple images and minimal text, or opt for article-style with one image and extensive text.
Tags for Content: Categorize your articles and stories with tags like 'History', 'News', and more, to clarify and organize the content.
Deployment and Setup Guide
Deploying on Heroku
Create a Heroku Account: If you don’t have an account, sign up at Heroku.
Install Heroku CLI: Download and install the Heroku CLI.
Login to Heroku: Run heroku login and follow the prompts to log in.
Create a Heroku App: Run heroku create to create a new app on Heroku.
Push Code to Heroku: Deploy your code using Git. Run git push heroku main.
Migrate Database: Migrate your Django models to Heroku’s PostgreSQL with heroku run python manage.py migrate.
Setting Up PostgreSQL on Heroku
Add PostgreSQL: Add Heroku Postgres from the 'Resources' tab in your Heroku dashboard or use heroku addons:create heroku-postgresql:hobby-dev.
Configure Database: Set up your database URL in settings.py to use the DATABASE_URL environment variable provided by Heroku.
Setting Up Cloudinary
Create Cloudinary Account: Sign up at Cloudinary.

Get API Credentials: From your Cloudinary dashboard, obtain your API key, API secret, and cloud name.

Configure in Django: In your Django settings.py, configure Cloudinary:

python
Copy code
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'your_cloud_name',
    'API_KEY': 'your_api_key',
    'API_SECRET': 'your_api_secret',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
Install Cloudinary Libraries: Run pip install django-cloudinary-storage pillow.

Running the Application
Collect Static Files: Run heroku run python manage.py collectstatic.
Launch the App: Open your Heroku app’s URL in the browser.
Contributions
Contributions to Earns Blog are welcome! Please read our contributing guidelines for more information.

License
[Your chosen license]
