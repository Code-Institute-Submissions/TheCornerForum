# Earn's - Creative Articles and Stories Platform

Earn's is a unique storytelling platform where creativity and imagination meet interactive reading. Dive into a universe of engaging articles, comic-style stories, and vivid narratives. Explore, read, and become part of a community where every story matters, and every reader is valued.

**Live demo:** View Earn's live site [here](#)

## Table of Contents
- [Design](#design)
- [Colour Scheme](#colour-scheme)
- [Typography](#typography)
- [Wireframes](#wireframes)
- [User Experience (UX)](#user-experience-ux)
- [User Stories](#user-stories)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Deployment and Local Development](#deployment-and-local-development)
- [Testing](#testing)
- [Scrum - progress](#scrum-progress)
- [Setups] (#setups)
- [Credits](#credits)

### Design
The design of Earn's embraces a comic book aesthetic with a modern twist, ensuring an immersive reading experience. The platform is built with the user in mind, focusing on simplicity and ease of navigation.

#### Colour Scheme
https://res.cloudinary.com/dzxr3hsus/image/upload/v1702813191/themecolor_earns_jf2ewk.png
The colour palette is a mix of earthy tones and vibrant highlights, creating a balance between comfort and excitement.


#### Typography
We use a combination of serif and sans-serif fonts to delineate between story narration and user interface elements.

#### Wireframes
https://res.cloudinary.com/dzxr3hsus/image/upload/v1703507093/Sk%C3%A4rmbild_2023-12-25_132358_cunbld.png
Wireframes for Earn's were developed to plan the layout and user flow for both desktop and mobile views.
And after deciding how i wanted it i asked AI to make it under this condissions and this was the resault i have been working from.

### User Experience (UX)

#### User Stories
- As a First-Time Visitor, I want to easily understand the main purpose of the site and learn more about the content provided.
- As a Reader, I want to explore different stories and articles, so I can enjoy reading in my leisure time.
- As a Registered User, I want to save my favorite reads and manage my profile, so I can personalize my experience on the platform.

### Features
- **Dynamic Reading Lists:** Curate your reading experience by saving stories and articles for later enjoyment.
- **Interactive Comments:** Engage with the content by posting anonymous comments.
- **User Profiles:** Customize your profile to reflect your reading preferences and interests.
- **Super User Capabilities:** Create and manage content with the ability to add images and text to your stories and articles. With this admin panel & AI, you can make an article within minutes.
- **Content Tagging:** Utilize tags to categorize and navigate through the variety of content available.

### Technologies Used
- **Languages:** HTML5, CSS3, JavaScript, Python
- **Framework:** Django
- **Database:** PostgreSQL, SQLite (development)
- **Static File Storage:** WhiteNoise
- **Media Storage:** Cloudinary
- **Deployment:** Heroku

### Deployment
[The deployed version of it can be visit here:](https://deploy-earns-c68fad364740.herokuapp.com/) 


### Testing
Testing was carried out throughout the development process. Please see the Testing Document for details. Some is not perfect and could be i just had a couple of days more.
[test](https://res.cloudinary.com/dzxr3hsus/image/upload/v1703507090/Sk%C3%A4rmbild_2023-12-23_003443_gurebg.png)
[Test](https://res.cloudinary.com/dzxr3hsus/image/upload/v1703507090/Sk%C3%A4rmbild_2023-12-23_003540_plp9q2.png)
[Test](https://res.cloudinary.com/dzxr3hsus/image/upload/v1703507090/Sk%C3%A4rmbild_2023-12-22_160540_jg35oo.png)
[Test](https://res.cloudinary.com/dzxr3hsus/image/upload/v1703507092/Sk%C3%A4rmbild_2023-12-23_003216_ubim3h.png)
[Test](https://res.cloudinary.com/dzxr3hsus/image/upload/v1703507092/Sk%C3%A4rmbild_2023-12-23_003355_n6wrzv.png)
[Test](https://res.cloudinary.com/dzxr3hsus/image/upload/v1703507091/Sk%C3%A4rmbild_2023-12-22_161547_ubhm3w.png)
[Test](https://res.cloudinary.com/dzxr3hsus/image/upload/v1703507091/Sk%C3%A4rmbild_2023-12-22_161602_xa2vo4.png)
[Test](https://res.cloudinary.com/dzxr3hsus/image/upload/v1703507091/Sk%C3%A4rmbild_2023-12-22_164925_tr8ppc.png)
[Test](https://res.cloudinary.com/dzxr3hsus/image/upload/v1703507092/Sk%C3%A4rmbild_2023-12-25_123145_mx52uy.png)


### Scrum Progress

[The Issues](https://res.cloudinary.com/dzxr3hsus/image/upload/v1703510074/Sk%C3%A4rmbild_2023-12-25_140621_plc989.png)
These are without any milestones sense the milestone where so obvius and because its a MVP i havent been afriad of leaving some of issues for future work.
But they are labeled and very easy to view and to point out whats need to be done. Tests for examples are something that never will be done but who has labels for (Todo after TEST) that should be choosen if an issue has come up after running an test. PRIO is also obvious. Bacause when you see that yello label you know thats where you should begin. 

[The Dashboard](https://res.cloudinary.com/dzxr3hsus/image/upload/v1703510073/Sk%C3%A4rmbild_2023-12-25_140523_k80fjf.png)
In the dashboard you have now: Inprogress, PRIO, testing and "wontfix or future feature". Before there was also a todo, but since have started on all issues already this one is no more. But will be added the day there are Todo to do.
### Setups

## Prerequisites

- Python installed on your system
- Code editor of your choice (e.g., VSCode, Sublime Text)
- Heroku CLI installed
- Git version control installed
- Cloudinary account

## Setting Up Django

1. **Install Django**:
    ```bash
    pip install django
    ```
2. **Create a New Django Project**:
    ```bash
    django-admin startproject your_project_name
    ```
3. **Create a New Django App**:
    ```bash
    cd your_project_name
    python manage.py startapp your_app_name
    ```

## Configure PostgreSQL on Heroku

1. **Create a New Heroku App**:
    ```bash
    heroku create your_heroku_app_name
    ```
2. **Add Heroku PostgreSQL**:
    ```bash
    heroku addons:create heroku-postgresql:hobby-dev --app your_heroku_app_name
    ```
3. **Get Your Database URL**:
    ```bash
    heroku config --app your_heroku_app_name
    ```

## Configure Cloudinary for Media Storage

1. **Install Cloudinary's Python Library**:
    ```bash
    pip install cloudinary
    ```
2. **Configure Cloudinary**:
    - Set up the Cloudinary environment variables with your API credentials.

## Deploying to Heroku

1. **Prepare your application for deployment**:
    - Use `pip` to install `gunicorn`, `dj-database-url`, `whitenoise`, and `psycopg2`.
    - Create a `requirements.txt` file.
    - Configure `settings.py` for Heroku deployment.
    - Create a `Procfile` for Heroku.

2. **Initialize Git**:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```

3. **Deploy to Heroku**:
    ```bash
    heroku git:remote -a your_heroku_app_name
    git push heroku master
    ```

4. **Run Migrations**:
    ```bash
    heroku run python manage.py migrate
    ```

## Linking the Project

1. **Set Environment Variables on Heroku**:
    - Set `DJANGO_SECRET_KEY`, `CLOUDINARY_URL`, and other required environment variables using Heroku's dashboard or CLI.

2. **Update Your Code Editor Settings** (if needed):
    - This step varies based on the code editor, but you may need to update settings for the Python interpreter or linters.

## Setting Up

1. **Finalize Your Application's Settings**:
    - Make sure all configurations for Django settings are complete, including allowed hosts, database configurations, and static files handling.

2. **Create Superuser for Django Admin**:
    ```bash
    heroku run python manage.py createsuperuser
    ```

3. **Launch Your App**:
    - Open your Heroku app URL in the browser.

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/en/3.2/)
- [Heroku Python Support](https://devcenter.heroku.com/articles/python-support)
- [Cloudinary Documentation](https://cloudinary.com/documentation)

Remember to replace placeholder text with your actual project and account details. Good luck with your Django project!


### Credits
Earn's is not just a platform but a community, and it wouldn't be possible without the contributions from our readers and writers alike. A special thank you to:
- **Contributors:** To all the wonderful people who have invested time in making Earn's rich with content.
- **Code Institute:** For providing the knowledge base to embark on building this project.
- **Udemy Course:** Python Django - The Practical Guide by Maximilian Schwarzmüller
- **Udemy Course:** Mega Web Development Course: Full stack web application 2023 by Pouya Eli
- **Christoffer Hurtig:** A good friend who has guide me thru problems when I have been stuck or searching for sulotions for features.
- **My Girlfriend:** Who has been very supporting ang given me time to work on the project even on christmas eve. And made miricals at home with the kids while i have been stuck with the project.

