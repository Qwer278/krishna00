import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES={
	'default':{
		'ENGINE':'django.db.backends.sqlite',
		'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
		}
}