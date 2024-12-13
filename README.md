# Carblog

![Responsive Mockup](static/images/smartmockups_lzcvb6po.jpg)

Carblog is a website designed for automotive enthusiasts who want to stay updated on the latest industry news, explore reviews of new car models, and share their own experiences and tips about vehicles. More than just a blog, Carblog addresses the need for centralized, relevant information for car lovers, offering an interactive and informative experience all in one place.
Carblog is ideal for those who:

   - Want to save time by finding all the latest automotive news and reviews in one space.
   - Are looking for a platform to share their opinions and tips with other enthusiasts.
   - Enjoy connecting with a community that shares the same passion for cars.
   - Need a tool to compare car models and make more informed purchasing decisions.
   - Seek inspiration for customizations or car maintenance through real stories and experiences from other users.

 ## Problems Solved by Carblog
  1. Information Fragmentation: Instead of searching for news, reviews, and personal experiences across multiple sources, users can find everything on Carblog.
  2. Difficulty in Making Purchase Decisions: With detailed reviews and the upcoming car comparison feature, Carblog helps users choose the ideal model based on their needs.
  3. Lack of an Interactive Community: Carblog encourages the exchange of ideas and experiences through posts, comments, and discussions.


### Wireframe Description

The wireframe below outlines the structure of the Carblog website, designed to provide a clear and intuitive user experience. Each section is strategically positioned to enhance navigation, content discovery, and user interaction.

1. **Header**:
   - The header contains three key areas:
     - **Brand (Logo)**: Positioned on the left to ensure instant recognition.
     - **Site Navigation Options**: Located centrally, providing links to main sections of the website.
     - **User Navigation Options**: Found on the right, offering access to user-specific features such as login, profile, or account settings.

2. **Page Introduction**:
   - Below the header, there's a dedicated space for the **Brand and Description of the Page**, which provides context about the website and its purpose.

3. **Main Content Area**:
   - This is the central focus of the page, divided into three parts:
     - **Image (img)**: A placeholder for visuals related to the post or topic being displayed.
     - **User-Supplied Content**: A section for displaying written or uploaded content provided by users.
     - **Details Button**: A call-to-action button for users to view more details about the post or content.

4. **Sidebar**:
   - Positioned on the right side, the sidebar contains links to **Categories**:
     - These links allow users to filter content based on their preferences, such as specific types of vehicles or topics of interest.

This wireframe ensures a clean and functional layout, optimized for readability, ease of navigation, and user engagement. It serves as a guide for developing the Carblog's visual and interactive structure.

![Wireframe](static/images/BLOG%20PROJECT.png)

## Features

### Existing Features

- **Navigation Bar**

  - Featured on all pages, the fully responsive navigation bar includes links to the home page, new posts, user informations. It is consistent across all pages to allow for easy and intuitive navigation.
  - This section enables users to seamlessly navigate from one page to another on all devices without needing to use the 'back' button.
  ![Nav Bar](static/images/navbar.png)

- **Home Page**

  - Main page, shows posts according to creation date, categories and images.
  ![Home Page](static/images/home%20page.png)

- **New post page**

  - The create new post page allows the user to create their post with content, image and the category it fits into.
  ![New post](static/images/newpost.jpg)

- **Categories**

  - Categories allow you to display content according to the user's preference
  ![Categories](static/images/category.png)

- **Read More**

  - By clicking on read more the user has more details about the post as well as being able to make comments and if it is a post created by themselves they can edit or delete the post.
  ![Read More](static/images/commnetedit.jpg)

- **User menu**

  - In the user menu you can see personal information, your posts and post management options.
  ![User Menu](static/images/usermenu.png)


### Features Left to Implement

- User feedback survey form
- Car comparison section

## Testing

### Validator Testing

- HTML
  - No errors were found on the other pages, except the "logou/": [W3C validator](https://validator.w3.org)
    ![validator](static/images/html%20valid.png)
  

- CSS
  - No errors were found when passing through the [Jigsaw validator](https://jigsaw.w3.org)
    ![cssvalidator](static/images/css%20valid.png)

### Check List

- A feature checklist was created to ensure all necessary tests.
  
| **Function**                | **Behavior**                               | **Pass/Fail** |
|-----------------------------|--------------------------------------------|---------------|
| **Load Page**               | Page loads with the correct layout         | pass         |
| **Title Display**           | Displays the correct title                 | pass         |
| **Content Display**         | Shows content based on the page type       | pass         |
| **Form Display**            | Form fields are correctly rendered         | pass         |
| **CSRF Token**              | CSRF token is present in forms             | pass         |
| **Submit Button**           | Submit button is visible and clickable     | pass         |
| **Validation Messages**     | Displays validation messages where required| pass         |
| **Success Messages**        | Shows success messages (e.g., on login, logout) | pass     |
| **Error Messages**          | Displays error messages (e.g., on failed login) | pass    |
| **Image Display**           | Displays images if available               | pass         |
| **Form Field Rendering**    | Form fields render correctly (e.g., text fields, dropdowns) | pass |
| **Link Navigation**         | Links navigate to the correct pages        | pass         |
| **Dynamic Content**         | Displays dynamic content (e.g., posts, comments) | pass     |
| **Button Functionality**    | Buttons perform their intended actions (e.g., save, cancel) | pass |
| **Logout Functionality**    | Successfully logs out and displays logout message | pass  |
| **Login Functionality**     | Login form submits correctly and shows login errors | pass  |
| **Password Reset**          | Handles password reset correctly (request, confirm, and success) | pass |
| **Page Responsiveness**     | Page is responsive and works on different screen sizes | pass |
| **User Authentication Check** | User-specific content is displayed correctly | pass    |
| **Comment Form**            | Comment form submits correctly for logged-in users | pass   |
| **Category Links**          | Category links filter posts correctly      | pass         |
| **Post Editing**            | Allows editing of posts and saves changes | pass          |
| **Post Deletion**           | Allows post deletion and confirms action  | pass          |
| **Registration**            | Allows new user registration and shows errors if needed | pass |
| **Admin Access**            | Admin-specific links and functionalities are accessible for superusers | pass |
| **Review Notice**           | Shows review notice when creating new posts | pass        |
| **Result Navigation**       | Navigates to results or summary pages appropriately | pass   |
| **Username Display**        | Displays username on relevant pages (e.g., profile) | pass    |
| **Form Field Styling**      | Form fields are styled correctly           | pass         |
| **Error Handling**          | Handles errors (e.g., form submission errors) gracefully | pass  |


## Automated Tests

This project includes automated tests for the main application models (`Category`, `Post`, and `Comment`). The tests are implemented using Django's built-in testing framework (`django.test`). Below is a detailed description of the tests:

---

### Test Structure

The tests are organized into three classes, each representing a specific model:

1. **CategoryModelTest**
2. **PostModelTest**
3. **CommentModelTest**

Each class uses the `setUp` method to create the necessary data for the tests, ensuring that each test is executed independently with a consistent data set.

---

## Included Tests

### 1. CategoryModelTest
- **Description**: Tests the `Category` model.
- **Tested Methods**:
  - `__str__`: Verifies that the string representation of a category is the name assigned to it.
- **Example**:
  - A category named "Technology" is created, and we verify that `str(category)` returns "Technology".

### 2. PostModelTest
- **Description**: Tests the `Post` model.
- **Tested Methods**:
  - Post creation and attribute verification (`title`, `content`, `author`, `category`).
  - The `approved` field, which should be `False` by default.
  - `__str__`: Verifies that the string representation of a post is its title.
- **Example**:
  - A post with the title "Django Testing" is created, and we verify the attributes and the output of `str(post)`.

### 3. CommentModelTest
- **Description**: Tests the `Comment` model.
- **Tested Methods**:
  - Comment creation and attribute verification (`post`, `author`, `content`).
  - The `approved` field, which should be `False` by default.
  - `__str__`: Verifies that the string representation of a comment follows the expected format (`"Comment by <author> on <post>"`).
- **Example**:
  - A comment is created on a post, and we verify the attributes and the output of `str(comment)`.

---

## How to Run the Tests

To run the tests, use the following command in the terminal:

```bash
python manage.py test
```
### Lighthouse Tests

- Lighthouse tests were conducted on all pages to ensure performance.

    ![Home](static/images/lighthouse.png)
  
### Unresolved errors

- An Html validator error was not resolved, attempts were made to adapt the "POST" method to the request, without success.
\
    ![Error](static/images/Captura%20de%20Tela%202024-08-05%20às%2011.23.12.png)

## Deployment

- The site was deployed to Heroku. The steps to deploy are as follows:
  - Copy the code to your Github or local repository.
  - Install Heroku CLI.
  - Create a new app on the Heroku platform, select the region according to your region.
  - Add add-ons for database and cloud service, recommended Heroku Postgres, Cloudinary.
  - For the password recovery feature to work, you will need an email provider, in this case Gmail was used.
  - Configure the following environment variables:
      * ALLOWED_HOSTS= yourdomain.herokuapp.com.
      * CLOUDINARY_URL= your cloud address.
      * DATABASE_URL= your database url.
      * EMAIL_HOST_USER= the email that you want to use for reset password.
      * EMAIL_HOST_PASSWORD= your APP password.
      * SECRET_KEY= Django secretkey
  - Access your application's terminal on Heroku and perform database migrations.
  - Run Heroku deploy. After this step, the website should now be visible.
  - Create a superuser to have access to the site administrator and interact with the site's content.

The live link can be found here - [https://carblog-6763fde39b1c.herokuapp.com](https://carblog-6763fde39b1c.herokuapp.com)


### Content

- The textual content was sourced from the following:
  - [Edmunds](https://www.edmunds.com)
- The favicon was taken from [Favicon.io](https://favicon.io)

### Media

- The images used were sourced from [Pexels](https://www.pexels.com)