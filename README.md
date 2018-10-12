# portfolio_new

Environmental variables:
The follow varibles will need to be set to run application. My own instances runs using Dokku, thus the commands take the form:
$ dokku config:set <APP> <ENV VAR>
eg: $ dokku config:set portfolio admin_username=wittyname

# For CMS access:
admin_username
admin_password

# SendGrid Key for Contact me form
sg_apikey

# Set DATABASE_URI, else otherwise a sqlite3 db will be created
DATABASE_URI
