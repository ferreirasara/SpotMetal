# SpotMetal

SpotMetal is a tool that uses the advanced search from [Metal Archives](https://www.metal-archives.com) to get Spotify links (these links are in 'Related Links' tab, in bands pages).
You can simply search and click in links to open the band profile in Spotify (and listen, obviously).
Or, after search, you can download a CSV file with all links, or make a playlist in Spotify, with the band's top songs.

in this project, it was used:
* Python 3.8
* Django 3.0.8
* Gunicorn 20.0.4
* WhiteNoise 5.1.0
* Beautiful Soup 4.9.1
* Spotify API
* Bootstrap 4.5
* Font Awesome 5
* Heroku
* PostgreSQL (from Heroku)


To be executed, the project needs two environment variables:
* SPOTMETAL_SECRET_KEY -> Key for project execution.
* DJANGO_DEBUG -> Used to define whether the project will run in debug mode or not.

![Home](https://i.imgur.com/k6e7xfL.png)
![About Us](https://i.imgur.com/t71nuvd.png)
