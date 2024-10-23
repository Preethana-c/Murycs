# Murycs - Web Client Application for Song Lyrics and Visualization

## Introduction
This web client application helps in finding lyrics and facts about the user’s favorite song and visualizes the music data. Once the user is logged in, it lists down the user’s favorite artist’s hitlist songs, their release dates, and featuring artists. It also provides the lyrics of the selected song by directing the user to a page that helps them understand more about the song and the artist.

## Features
- **Signup**: New users can register and access the application.
- **Login**: Registered users can log in to access the application.
- **Filtering**: Filter hit songs based on the artist's name and search for artists.
- **Default View**: The application lists the hitlist of the artist Billie Eilish by default.
- **List View**: Displays song title, main artist, featuring artist, and release date.
- **Lyrics Access**: Clicking "click here" below the song thumbnail directs to the Genius website to display the lyrics of the selected song.

## Technologies Used
- Python
- Django 4.1
- SQLite Ver-3.39.4
- HTML
- CSS

## How It Works
This application utilizes the Genius-Song Lyrics APIs available on RapidAPI to find the hitlist of songs and their lyrics.

### What is RapidAPI?
RapidAPI is the world's largest API hub, providing APIs to over three million developers to find, test, and connect to thousands of APIs. Signing up for a free RapidAPI account is required to use this application.

### What is the Genius - Song Lyrics API?
The Genius - Song Lyrics API is used to search for songs, artists, and lyrics, as well as to fetch the hitlist songs for the specified artist. A subscription to the API is required to test APIs, integrate them into the application, and track analytics.

#### Genius API Provides:
- **Search Musical Metadata**: Access Genius's vast repository of musical metadata about artists, albums, and songs.
- **Artist Information**: Programmatically access artist information including details like social media handles, followers count, and relevant images.
- **Song Information**: Retrieve information on songs and leverage community-powered annotations available on Genius.com.

## Functions Used

| Function                      | Description                                                                                                                                          |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `connect_genius(self)`        | Connects to the Genius database, providing the `X-RapidAPI-Key` & `X-RapidAPI-Host` values required for connection.                               |
| `name_to_url_string(name)`    | URL encodes the given name, converting characters into a format suitable for transmission over the Internet.                                        |
| `home_view(request)`          | Returns the home HTML page based on the request.                                                                                                   |
| `index_view(request)`         | Connects to the Genius database and retrieves the hit list, extracting required data and storing it in a dictionary.                               |
| `register_request(request)`   | Handles the signup page functionality for new user registration using Django's built-in `UserCreationForm`.                                         |
| `login_request(request)`      | Handles the login page functionality using `AuthenticationForm` for user login and verifies credentials.                                            |
| `logout_request(request)`     | Logs the authenticated user out and redirects them to the homepage.                                                                                 |
| `clean_username(self)`        | Cleans the username prior to its use to get or create a user object.                                                                               |
| `clean_email(self)`           | Cleans the email address prior to its use to get or create a user object.                                                                          |
| `save(self, commit=True)`     | Saves the user object to the backend when the commit argument is True (default is True).                                                             |

## Classes Used

| Class                     | Description                                                                                                                                      |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `MusicstoreConfig`       | Application configuration object that contains the required configurations for the application, subclassing Django's `AppConfig`.               |
| `NewUserForm`            | Derived from `UserCreationForm` and used for user sign-in registration, leveraging Django's built-in user creation capabilities.                   |
| `ListViewForm`           | Implements the functionality required for the index view, connecting to the Genius database and retrieving the hit list using HTTP GET requests. |
| `Meta`                    | Used to change the behavior of the model fields.                                                                                                 |
| `HTTPSConnection`         | Creates an object providing the client-side of the HTTP and HTTPS protocols for connecting to the Genius database.                               |
| `HttpResponse`            | Handles the response and status code received for HTTP requests.                                                                                 |
| `json`                    | Converts JSON data into a Python object, using `json.loads()` to parse the JSON object retrieved from the HTTP response into a Python dictionary. |

