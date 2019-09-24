# Coffee Culture Club: 

[Visit Site](https://coffee-culture-club.herokuapp.com/)

Coffee Culture Clubs misson is to bring people together through the love of high quality and environment ethically sourced coffee. 

New age milenaials are done with night clubs and other demographics are removing alcohol from their lifes for multiple different reasons. 

There's not yet a set space for individuals to be social without the pressure of alcohol 
~ Coffee Culture Club solves that while also providing luxury coffee beans for purchase.

##

This web application is built with responsive, mobile first design. Users have the ability to plan new meetups and comment on exisiting meetups, they can buy & review products and 
becoming a member of the club. 


#### User Stories 

**As a new user I want to be able to**:
- Visit a homepage with a site description
- Easily navigate to register a new account by either selecting `Join club` in nav bar **or** by seeing `Join Club`
card on the homepage
- See a form that creates a new user 
- Be redirected to a login page to sign in for the first time



**As a user looking to purchase a product I want to be able to**:
- Navigate to `Products` 
- See a list of products
- Search for products
- See a product details page 
- Add to cart
- View Cart, amend quality see total price
- Go to a checkout page which contains a form accepting my shipping and billing details
- See a message confirming order and payment



**As a user interested in Meetups I want to be able to**:
- Navigate to `Meetups`
- See a list of different Meetups 
- See more information about the meetup
- Get more detail about specfic meets
- See and add comments on meetups
- Back to all meetups and see the ability to add a new meetup


### Wireframes:

Home page:

[Desktop](https://coffee-culture-club.s3-eu-west-1.amazonaws.com/wireframes/homedesktop.png)

[Mobile](https://coffee-culture-club.s3-eu-west-1.amazonaws.com/wireframes/homemobile.png)

Products/Coffee:

[Desktop](https://coffee-culture-club.s3-eu-west-1.amazonaws.com/wireframes/productsdesktop.png)

[Mobile](https://coffee-culture-club.s3-eu-west-1.amazonaws.com/wireframes/productsmobile.png)


## Features

### Existing Features

- Create account
- Sign in/out
- Reset Password
- Products page
- Cart
- Checkout page using Stripe
- Review Products
- Create Meetups
- Comment on Meetups

### Features Left to Implement
- Survay
- Discounts

## Technologies Used

[HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)

[CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)

[Materialize CSS](https://materializecss.com/)

[JavaScript](https://www.javascript.com/)

[Flask](https://flask.palletsprojects.com/en/1.0.x/)

[Python](https://www.python.org/)

[Heroku](https://dashboard.heroku.com/)

[Django](https://www.djangoproject.com/)

[Amazon S3](https://aws.amazon.com/s3/features/)

[Stipe](https://stripe.com/ie)

[PostgreSQL](https://www.postgresql.org/)



## Testing
- Tested on all new age desktop and mobile browsers to ensure cross compatibility & functionality.
- Tested to be responsive and to ensure it would be correctly displayed across different mobile screens sizes.
- Each one of the user stories were tested without errors.
- Testing for this project was done manually. The majority of testing covered the different Django apps.
- All forms are validated to ensure each field is included when submitting. Messages respond to the user whether they've been successful or not.
- For account registration, logic is included to ensure emails and usernames do not already exist in the database.
- The Checkout is secured and payment can be successfully taken via Stipe.
- Users cannot add reviews to products, add meetups or add comments to meetups without being logged in.
- Defensive programming to prevent non-logged in users to visit urls they don't have access too


## Deployment

### I deployed my site using Heroku & GitHub

Initalzie Git (if you haven't already)
```
$ git init

$ git add .

$ git commit -m "initial commit"
```

Connect Github Repository:
```
$ git remote add origin https://github.com/jessdevine/project-coffeecultureclub.git

$ git push -u origin master
```


Add Requirements.txt
```
$ sudo pip3 freeze —local > requirements.txt
```
Add ProcFile
```
echo web: gunicorn coffeecultureclub.wsgi:application > Procfile
```


In the Heroku application
Go to Settings > Config Vars 
```
AWS_SECRET_ACCESS_KEY
STRIPE_SECRET
STRIPE_PUBLISHABLE
SECRET_KEY
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
DISABLE_COLLECTSTATIC
DATABASE_URL
```

Deploy Site:

- In the Heroku web client connect GitHub account
- Select GitHub Repository 

```
git push
```



### Media
- The photos used in this site were obtained from [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/search/coffee/)

