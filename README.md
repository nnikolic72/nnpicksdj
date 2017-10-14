# nnpicksdj
NN Picks tools
--------------

 am creating a Django project nnpicksdj to be able to track good Instagram photographers and create a database of them.

This project will help me learn Django programming, and in the same time help with my next projects regarding Instagram.

// Heroku Git push
// It will collectstatic automatically
cd nnpicksdj
git add -A
git commit -am "versionx"
git push heroku master

// Heroku migrate django models
heroku run python manage.py migrate

// collect static files
heroku run python manage.py collectstatic

// Heroku status - you have to be in deployment directory
cd nnpicksdj
heroku ps
heroku logs

//Windows Powerhell environment variable setup
$env:DJANGO_SETTINGS_MODULE="nnpicksdj.settings.local"

// requirements.txt - Heroku
1. Add this string without quotes to the end of requrements.txt. "-r requirements_heroku.txt"
2. Convert requirements.txt file in Notepad++ to Encoding > Encode in ANSI
