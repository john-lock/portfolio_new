# Overview
This is the project of my Portfolio site. While starting out with a basic single page HTML site I soon found it to be cumbersome to have so much HTML in one place, esspecially when I knew I would want to update this in the future. I then implemented CRUD (Create, Read, Update, Delete) functionality in which projects for display can be input, edited and deleted from the site. This means that each project is easier to handle when putting on the site - for each new project just the text needs to be added, along with any pictures, rather than any new lines of code written. This also makes it easy to edit any text, and archive older projects if desired. 

# Instalation
The follow environment varibles will need to be set to run application. My own instances runs using Dokku, thus the commands take the form:
`$ dokku config:set <APP> <ENV VAR>`
eg: `$ dokku config:set portfolio admin_username=wittyname`

- For access to CRUD controls:
```
export admin_username=username
export admin_password=password
```

- SendGrid Key for 'Contact Me' form (You can get your own credentials from https://sendgrid.com/)
` export sg_apikey=key`

-Set DATABASE_URI, else otherwise a sqlite3 db will be created
` export DATABASE_URI=newdb`

# Usage
To Add, Update or Delete any projects visit: /projects/list of the application, and then use the admin usernmae and password set during set up. 

- name: Full project name displayed for the project on the main page
- idname: used for internal reference including modals
- card_text: Text visible on the main page for the project (200 char limit)
- modal_body:
- modal_tech: listed in soft text at the bottom of the project modal (400 char limit)
- preview: Used for project demo url
- github: Used for github link
- show: Set to `True` to have the project show on the main page. Otherwise set to `False`
- top: Set to `True` for projects to appear in the upper section of the projects(so long as show is also set to `True`). Set top to `False` and then projects will appear in the 'click to reveal' 

(modal_short and images are not currently used but can be invoked if desired)

# TODO
- Expand test coverage
- Improved user registration
- Image upload functionality
