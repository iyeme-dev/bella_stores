# Bella Stores
 
Project by: Iyeme Salubi 

[View live project](https://bella-store-1b93e73638e2.herokuapp.com/)

Bella Store is a user-friendly e-commerce platform offering a collection of beautiful jewellery pieces, designed to deliver a seamless and engaging shopping experience. The website features a clean, structured layout powered by Bootstrap, with intuitive navigation that guides users through product categories, product detail pages, and secure checkout. Its main sections include a home page, product categories, user account management, managing a shopping cart, and completing a purchase with Stripe payment integration. Bella Store is designed to attract new customers, inspire confidence through thoughtful design, and provide a trustworthy and enjoyable online jewellery shopping experience.

# Table of Contents

1. [Project Overview](#project-overview)
2. [User Stories](#user-stories)
3. [Rationale](#rationale)
   - [Target Audience](#target-audience)  
   - [Motivation](#motivation)  
   - [Background](#background)  
   - [Proposed Solution](#proposed-solution)  
   - [Overall Improvements Over Current Alternatives](#overall-improvements-over-current-alternatives)  
   - [Project Scope and Limitations](#project-scope-and-limitations)  
   - [Future Improvements](#future-improvements)  
   - [Summary](#summary)  
4. [Design](#design)
   - [Brand Colours](#brand-colours)  
   - [Layout & Structure](#layout-and-structure)  
   - [Wireframes](#wireframes)  
5. [Database Schema](#database-schema)
6. [Deployment](#deployment)
7. [Testing](#testing)
   - [Browser Testing](#browser-testing)  
   - [Code Validation](#code-validation)  
   - [Lighthouse Test](#lighthouse-test)
8. [Testing Errors and Improvements](#testing-errors-and-improvements)
9. [Technologies Used](#technologies-used)
10. [Credit and Reference](#credit-and-reference)
11. [Author](#author)

# Project Overview
Bella Stores is a responsive, user-centric online jewellery shop designed to make browsing and purchasing elegant accessories simple and enjoyable. The website organizes products into clear categories and provides detailed product pages with high-quality images, helping users quickly find what they want. It features an intuitive shopping cart and secure Stripe payment integration, so buyers can confidently complete purchases, view order confirmations, and manage their accounts. Built with a clean, visually appealing layout and seamless navigation, Bella Stores addresses common online shopping frustrations—like difficulty finding products, confusing checkout, and unclear site structure—while catering to fashion-aware buyers seeking a trustworthy and engaging e-commerce experience.

# User Stories

As a shopper, I want to filter products by category (e.g., bracelets, earrings), so I can easily find what I’m interested in.

As a buyer, I want to see clear product images and descriptions, so I can feel confident in the purchase.

As a shopper, I want to add items to my cart, so I can collect the items I plan to purchase.

As a user, I want the cart to update the total price and quantities dynamically, so I can easily track how much I will pay.

As a customer, I want to securely checkout, so my payment information stays safe.

As a buyer, I want a confirmation page after checkout, so I know my order was successful.

As a new user, I want to create an account, so I can track orders and save my information.

As a returning shopper, I want to sign in, so I can see my past orders and repeat purchases.

# Rationale
The Bella Stores project was developed as a full-stack e-commerce web application with the aim of providing users with a simple, secure, and engaging online jewellery shopping experience. The rationale for this project is grounded in the need to address common usability challenges faced by online shoppers, such as poor navigation, limited product information, and complex checkout processes. By applying user-centred design principles and clearly defined user stories, the project focuses on improving accessibility, trust, and overall user satisfaction. This section outlines the motivation, target audience, and design decisions behind Bella Stores, while explaining how the implemented features respond to real-world user needs and e-commerce best practices.

### Target Audience

Bella Stores is designed for fashion-conscious shoppers who value stylish, affordable jewellery and want a smooth, reliable online shopping experience. The primary audience includes young adults and professionals who prefer browsing and purchasing jewellery online, as well as returning customers who want quick access to their order history. The site also targets first-time online shoppers who need clear navigation, visual reassurance, and a simple checkout process.

### Motivation

The motivation behind Bella Stores was to address common frustrations experienced when shopping for jewellery online, such as cluttered product listings, unclear pricing, poor product images, and complicated checkout flows. Many existing jewellery websites overwhelm users with excessive content or lack transparency, leading to abandoned carts and lost trust. This project was created to offer a clean, intuitive, and trustworthy platform that prioritizes ease of use and customer confidence.

### Background

With the growth of e-commerce, customers increasingly expect fast, secure, and visually appealing shopping experiences. Jewellery, in particular, requires high-quality presentation and clear information to encourage purchases. Bella Stores was developed as a full-stack Django-based e-commerce platform to demonstrate how thoughtful design, structured navigation, and secure payment processing can improve the online retail experience while meeting real-world user needs.

### Proposed Solution

This project offers a responsive and user-friendly home staging website that is clear, helpful, and easy to navigate. It offers some features and functionalities that helps to offer solutions to the user stories.

#### Key Features and Functionalities

- **Category-Based Product Navigation**
  - Products are organised into clearly defined categories such as bracelets, earrings, necklaces, and sets.
  - A dropdown category menu allows users to filter products quickly.
  - **Addresses user story:**  
    *As a shopper, I want to filter products by category so I can easily find what I’m interested in.*

- **Detailed Product Pages**
  - Each product includes a high-quality image, price, description, and stock availability.
  - Clear visual presentation helps users evaluate items before purchasing.
  - **Addresses user story:**  
    *As a buyer, I want to see clear product images and descriptions so I can feel confident in the purchase.*

- **Shopping Cart Functionality**
  - Users can add products to a cart, increase or decrease quantities, or remove items entirely.
  - The cart displays item quantities and individual prices.
  - **Addresses user story:**  
    *As a shopper, I want to add items to my cart so I can collect the items I plan to purchase.*

- **Dynamic Cart Total Calculation**
  - The total price updates automatically based on item quantities in the cart.
  - This allows users to monitor their spending before checkout.
  - **Addresses user story:**  
    *As a user, I want the cart to update the total price and quantities dynamically so I can easily track how much I will pay.*

- **Secure Checkout and Payment Processing**
  - Stripe is integrated to handle secure online payments.
  - Sensitive payment data is processed externally, ensuring user security.
  - **Addresses user story:**  
    *As a customer, I want to securely checkout so my payment information stays safe.*

- **Order Confirmation and Thank You Page**
  - After successful payment, users are redirected to a confirmation page.
  - The page confirms that the order has been placed successfully.
  - **Addresses user story:**  
    *As a buyer, I want a confirmation page after checkout so I know my order was successful.*

- **User Registration and Authentication**
  - New users can create accounts and securely log in.
  - Authentication ensures personalised access to order history.
  - **Addresses user story:**  
    *As a new user, I want to create an account so I can track orders and save my information.*

- **Order History for Registered Users**
  - Logged-in users can view past orders and order details.
  - This supports repeat purchases and builds user trust.
  - **Addresses user story:**  
    *As a returning shopper, I want to sign in so I can see my past orders and repeat purchases.*


### Overall Improvements Over Current Alternatives

Compared to many existing small-scale jewellery websites, Bella Stores offers a more streamlined and intuitive user experience. The platform offers clear navigation and category filtering, minimizes confusion during checkout with secure payment handling, and improves transparency through order confirmations and order history access. Its responsive design ensures usability across devices, making it more accessible than less optimized alternatives.

### Project Scope and Limitations

The scope of this project focuses on core e-commerce functionality, including product browsing, cart management, secure checkout, and user accounts. While the site successfully supports essential shopping features, it does not currently include advanced functionalities such as wishlists, product recommendations, discount codes, or multi-currency support. The project is also limited to a single storefront without vendor management or inventory analytics.

### Future Improvements

Future enhancements could include user reviews and ratings, wishlist functionality, improved search and filtering options, email order confirmations, and promotional features such as discount codes. Additional improvements may also involve performance optimization, enhanced mobile UX, and expanded payment options to support a broader customer base.

### Summary

Bella Stores was developed to solve common online jewellery shopping challenges by offering a clean, secure, and intuitive e-commerce experience. Guided by user-centered design principles and real user stories, the project delivers clear product presentation, smooth navigation, and reliable checkout functionality. Overall, Bella Stores demonstrates how thoughtful design and robust backend implementation can significantly improve customer satisfaction and trust in online retail platforms.

# Design

The design of the Bella Store website prioritises clarity, usability, and visual appeal, ensuring a seamless experience across devices. A responsive grid layout and Bootstrap framework are used to maintain consistent alignment and spacing, enhancing readability and navigability. Navigation elements, such as the main menu and category dropdown, are positioned prominently to facilitate easy browsing and product discovery. High-resolution product images and clear typography engage the user visually while conveying essential information effectively. Functionality and aesthetics are balanced throughout the design; interactive elements such as buttons and links provide immediate feedback, while whitespace and structured sections reduce cognitive load. Overall, the site’s design fosters intuitive interaction, guiding users from initial exploration through to checkout with minimal friction.

## Brand Colours

Bella Store implements a cohesive and purposeful colour palette that communicates elegance and professionalism appropriate for an online jewellery retailer. The dominant colours are dark-toned backgrounds paired with light text, which establish strong contrast and visual hierarchy, making key elements such as navigation text and call-to-action buttons easily legible. Warm accent colours, especially in interactive elements such as the search button, draw user attention to important actions and reinforce clickability without overwhelming the interface. The consistent application of brand colours across the navbar, buttons, and footer enhances overall visual unity and supports brand recognition. These colour choices promote a sense of luxury and reliability, aligning with user expectations for a premium shopping experience while maintaining functional clarity.

## Layout and Structure of the Website

The Bella Store website follows a clear, logical layout designed to guide users smoothly through browsing, purchasing, and account management. Each section of the site directly supports the identified user stories by prioritising usability, clarity, and intuitive navigation.

---

### Navigation Bar and Global Layout

The navigation bar is fixed at the top of every page and provides consistent access to the core sections of the site. It includes:
- A **category dropdown menu**
- Links to **Contact** and **About** pages
- **Sign Up** and **Sign In** options
- A **shopping cart icon** displaying the current item count
- A **search bar** for quick product discovery

This consistent structure ensures users can navigate the site easily from any page, supporting both new and returning shoppers.

---

### Product Categories and Filtering

The homepage is structured around a **category-based browsing system**.  
Users can filter products by selecting categories such as bracelets, earrings, necklaces, and watches from the dropdown menu.

- Each category opens a dedicated product listing page
- Only relevant products are displayed per category
- The category name is clearly shown, helping users stay oriented

This layout directly supports the user story:

> *As a shopper, I want to filter products by category, so I can easily find what I’m interested in.*

---

### Product Listings and Product Detail Pages

Products are displayed in a clean grid layout featuring:
- High-quality product images
- Clear product names and prices
- A consistent visual structure across all listings

Clicking a product opens a **dedicated product detail page**, which includes:
- A larger product image
- A detailed description
- Price and stock availability
- An **Add to Cart** button

This structure supports confidence in purchasing and addresses the user story:

> *As a buyer, I want to see clear product images and descriptions, so I can feel confident in the purchase.*

---

### Shopping Cart Page

The cart page is divided into two clear sections:
1. **Item Summary**
   - Product image and name
   - Quantity controls (increase, decrease, remove)
   - Individual item subtotal
2. **Order Summary**
   - Total price
   - Checkout button

The cart dynamically updates quantities and totals as users add or remove items, supporting:

> *As a user, I want the cart to update the total price and quantities dynamically.*

---

### Secure Checkout Process

The checkout section is integrated directly into the cart page and uses **Stripe** for payment processing.  
The structure includes:
- Secure payment modal
- Billing and shipping information fields
- Clear display of the total amount before payment

This ensures user confidence and data security, addressing:

> *As a customer, I want to securely checkout, so my payment information stays safe.*

---

### Order Confirmation Page

After a successful payment, users are redirected to a **Thank You / Order Confirmation page** which includes:
- Order reference number
- Confirmation message
- Payment success feedback

This provides reassurance and closure, fulfilling:

> *As a buyer, I want a confirmation page after checkout, so I know my order was successful.*

---

### User Account Registration and Authentication

The site includes dedicated pages for:
- **User registration (Sign Up)**
- **User login (Sign In)**

Once authenticated, users can:
- View order history
- Access individual order details
- Make repeat purchases more easily

This supports both new and returning users, addressing:

> *As a new user, I want to create an account…*  
> *As a returning shopper, I want to sign in…*

---

### Order History and Order Detail Pages

Authenticated users can access an **Order History page** listing previous purchases.  
Each order links to a detailed view showing:
- Purchased items
- Quantities and prices
- Billing and shipping information

This enables users to track and review past orders efficiently.

---

### Summary

Overall, the site layout follows a clear user journey:

**Browse → Filter → View → Add to Cart → Checkout → Confirm → Track Orders**

Each section is logically structured to meet user needs while maintaining simplicity, clarity, and usability throughout the shopping experience.

## Wireframes 

Wireframe for Desktop and mobile screen sizes respectively

# Database Schema
Bella Stores uses Django ORM models to represent the core ecommerce data: products, categories, shopping carts, orders, reviews, and contact messages. 
The core workflow is:

Category → Product → Cart/CartItem → Order/OrderItem

# Models and Relationships

## USER
The User table stores all registered customer and administrator accounts for the site. It contains authentication and identification details such as username, email address, and encrypted password, as well as profile information including first and last names. Additional boolean fields determine whether a user account is active or has staff permissions. This table is central to the application, as it links to orders, carts, and contact messages, allowing users to place orders, manage their shopping activity, and interact with the site.

### Relationships
#### User → Cart
Type: One-to-Many (1 → Many)
One user can have multiple carts over time
Each cart belongs to one user (or is NULL for guests)

#### User → Order
Type: One-to-Many (1 → Many)
One user can place many orders
Each order belongs to exactly one user

#### User → ContactMessage
Type: One-to-Many (1 → Many)
One user can submit many contact messages
Each message optionally belongs to one user

| Key | Name | Type | Extra Info |
| --- | ---- | ---- | ---------- |
| PK | id | AutoField | primary_key=True |
|  | username | CharField | unique=True |
|  | first_name | CharField |  |
|  | last_name | CharField |  |
|  | email | EmailField | unique=True |
|  | password | CharField | hashed |
|  | date_joined | DateTimeField | auto_now_add=True |
|  | is_active | BooleanField | default=True |
|  | is_staff | BooleanField | default=False |

## CATEGORY
Stores product groupings (e.g., Necklace, Bracelets).
The Category table is used to organise products into logical groupings to improve navigation and browsing. Each category has a name and a unique slug that is used in URLs, making the site more SEO-friendly and readable. Categories allow products to be filtered and displayed by type, helping users quickly find relevant items and supporting a scalable product catalogue structure.
### Relationship
- One **Category** has many **Products** (1 → many)

| Key | Name       | Type          | Extra Info        |
| --- | ---------- | ------------- | ----------------- |
|     | name       | CharField     |                   |
|     | slug       | SlugField     | unique=True       |
|     | created_on | DateTimeField | auto_now_add=True |

## PRODUCT
Stores items for sale.
The Product table stores detailed information about all items available for sale on the site. This includes the product name, description, price, image reference, and availability status. Each product is linked to a category, enabling structured browsing. The table also tracks when products are created and whether they are active, allowing administrators to manage listings without permanently deleting data.

### Relationships
- Belongs to one **Category** (many → 1)  
- Can appear in many carts via **CartItem** (1 → many)  
- Can appear in many orders via **OrderItem** (1 → many)


| Key        | Name        | Type                  | Extra Info        |
| ---------- | ----------- | --------------------- | ----------------- |
| ForeignKey | category    | Category model        | on_delete=CASCADE |
|            | name        | CharField             |                   |
|            | slug        | SlugField             | unique=True       |
|            | description | TextField             |                   |
|            | price       | DecimalField          |                   |
|            | image       | ImageField / URLField |                   |
|            | is_active   | BooleanField          | default=True      |
|            | created_on  | DateTimeField         | auto_now_add=True |

## CART
Represents a shopping cart session (guest or logged-in).
The Cart table represents a user’s shopping cart and temporarily stores selected products before checkout. A cart may be associated with a registered user or, if applicable, identified by a session key for guest users. Timestamps are used to track when the cart is created and updated, supporting cart persistence and allowing users to return to previously selected items.

### Relationships
- One **Cart** contains many **CartItems** (1 → many)

| Key        | Name        | Type          | Extra Info                    |
| ---------- | ----------- | ------------- | ----------------------------- |
| ForeignKey | user        | User model    | null=True, on_delete=SET_NULL |
|            | session_key | CharField     | null=True                     |
|            | created_on  | DateTimeField | auto_now_add=True             |
|            | updated_on  | DateTimeField | auto_now=True                 |

## CART_ITEM
The Cart Item table acts as a junction between the cart and product tables, storing individual items added to a cart. It records the quantity of each product and captures the product price at the time it was added. This structure allows a cart to contain multiple products while preserving pricing accuracy, even if product prices change later.

### Relationships
- Many **CartItems** belong to one **Cart** (many → 1)  
- Many **CartItems** reference one **Product** (many → 1)

| Key        | Name                | Type                 | Extra Info        |
| ---------- | ------------------- | -------------------- | ----------------- |
| ForeignKey | cart                | Cart model           | on_delete=CASCADE |
| ForeignKey | product             | Product model        | on_delete=CASCADE |
|            | quantity            | PositiveIntegerField | default=1         |
|            | unit_price_snapshot | DecimalField         | price at add time |

## ORDER
Stores checkout and payment/billing/shipping information.
The Order table stores completed checkout transactions and represents a confirmed purchase made by a user. It includes a unique order number, order status, cost breakdown (subtotal, shipping, and total), and timestamps for creation and payment. Each order is linked to a user, enabling order history functionality and allowing customers to review past purchases.

### Relationships
- One **Order** has many **OrderItems** (1 → many)  
- Optionally linked to a Django **User** (if used in your project)
- 
| Key        | Name          | Type          | Extra Info               |
| ---------- | ------------- | ------------- | ------------------------ |
| ForeignKey | user          | User model    | on_delete=CASCADE        |
|            | order_number  | CharField     | unique=True              |
|            | status        | CharField     | PENDING / PAID / SHIPPED |
|            | subtotal      | DecimalField  |                          |
|            | shipping_cost | DecimalField  |                          |
|            | total         | DecimalField  |                          |
|            | created_on    | DateTimeField | auto_now_add=True        |
|            | paid_on       | DateTimeField | null=True                |

## ORDER_ITEM
The Order Item table records the individual products associated with an order. It stores the quantity, unit price at checkout, and total cost per line item. This table ensures accurate historical records by preserving pricing details even if product information changes in the future. It also supports detailed order summaries and invoicing.

### Relationship
- Many **OrderItems** belong to one **Order** (many → 1)
  
| Key        | Name                | Type                 | Extra Info        |
| ---------- | ------------------- | -------------------- | ----------------- |
| ForeignKey | order               | Order model          | on_delete=CASCADE |
| ForeignKey | product             | Product model        | on_delete=PROTECT |
|            | quantity            | PositiveIntegerField |                   |
|            | unit_price_snapshot | DecimalField         | price at checkout |
|            | line_total          | DecimalField         | quantity \* price |

## CONTACT_MESSAGE 
The Contact Message table stores messages submitted through the site’s contact or support form. Messages may optionally be linked to a registered user, but also support guest submissions. Each record includes sender details, subject, message content, and a timestamp, enabling administrators to manage customer enquiries and provide support efficiently.

### Relationship
User → ContactMessage
Type: One-to-Many (1 → N)
- One User can submit many ContactMessages
- Each ContactMessage belongs to one User
- The relationship is optional (user can be NULL for guest messages)

| Key        | Name       | Type          | Extra Info                    |
| ---------- | ---------- | ------------- | ----------------------------- |
| ForeignKey | user       | User model    | null=True, on_delete=SET_NULL |
|            | name       | CharField     |                               |
|            | email      | EmailField    |                               |
|            | subject    | CharField     |                               |
|            | message    | TextField     |                               |
|            | created_on | DateTimeField | auto_now_add=True             |


## Schema Design Rationale

This schema avoids duplication:

- Products are stored once in **Product**
- Many-to-many behavior is handled using junction models:
  - **CartItem** (Cart ↔ Product) stores quantity and active status
  - **OrderItem** (Order ↔ purchased items) stores checkout snapshots

---

# Deployment
## Deployment Process (Heroku)

This section outlines the process used to deploy the Bella Store Django website to Heroku, including production settings, database setup, static/media hosting with AWS S3, and final release steps.

---

### 1) Prepare the Project for Deployment

#### 1.1 Add required packages
Install the dependencies needed for production hosting, Postgres, environment variables, and S3 storage:

- `gunicorn` (production WSGI server)
- `dj-database-url` (parse `DATABASE_URL`)
- `psycopg2-binary` (PostgreSQL adapter)
- `python-dotenv` (local `.env` loading)
- `django-storages` + `boto3` (AWS S3 storage)
- `crispy-forms` / `crispy-bootstrap4` (form styling)

Then update `requirements.txt`

---

### 2) Configure Django for Production

#### 2.1 Environment Variables

Move sensitive values out of `settings.py` into environment variables (Heroku config vars):

- `SECRET_KEY`
- `DATABASE_URL`
- `STRIPE_SECRET_KEY`
- `STRIPE_PUBLISHABLE_KEY`
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `USE_AWS=True` *(to switch on S3)*

---

#### 2.2 Update `settings.py`

**Key production changes:**

- Use environment variables for secrets
- Configure `ALLOWED_HOSTS` with Heroku domain
- Configure database with `dj_database_url`
- Configure static/media with S3 if `USE_AWS` is enabled
- Ensure `storages` is included in `INSTALLED_APPS`

---

### 3) Create a Procfile (Gunicorn)

In the project root, create a file named Procfile (no extension)
This tells Heroku how to run the application.

---

### 4) Create and Configure the Heroku App
#### 4.1 Create a Heroku app

Using the Heroku dashboard (or CLI), create an app (example name: bella-store).

#### 4.2 Add Heroku remote (Git)
[heroku git:remote -a bella-store]
Now you can deploy using Git push:
[git push heroku main]

---

### 5) Add a Production Database (PostgreSQL)

Heroku Postgres addon: [heroku addons:create heroku-postgresql:mini --app bella-store]

---

### 6) Run Migrations on Heroku

After deploy, create your database tables:[heroku run --app bella-store -- python manage.py migrate]

---

### 7) Configure Static & Media Files

AWS S3 for static + media (used in this project)

This project uses AWS S3 via django-storages and boto3.

Steps:

- Create an S3 bucket (e.g. amzn-s3-bella-store-bucket)
- Set region (e.g. eu-north-1)
- Create an IAM user with S3 permissions
- Add credentials and USE_AWS=True as Heroku config vars
- Add storages to INSTALLED_APPS
- Create custom_storages.py to define: StaticStorage and MediaStorage
- Update STATIC_URL and MEDIA_URL to point to S3.

---

### 8) Collect Static Files

Heroku runs collectstatic during deployment automatically

---

### 10) Deploy the Application

Once everything is configured:
git add .
git commit -m "Deploy Bella Store to Heroku"
git push heroku main

Heroku will:
- Install dependencies
- Run collectstatic
- Start Gunicorn via the Procfile

## Hosting
The Bella Stores website was hosted using the Heroku cloud platform to provide a scalable and accessible production environment.
Static and media files were managed using Amazon S3 to ensure reliable storage and fast content delivery. This hosting approach ensures the site is stable, secure, and accessible to users across different devices and locations.























