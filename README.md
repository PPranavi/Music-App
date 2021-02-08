# Project 1
This is a simple "music discovery" web application that shows the top 10 songs from some of my favorite artists. This data is dynamically generated
using the Spotify API.

## Requirements
In your terminal:
1. `pip install python-dotenv`
2. `pip install requests`
3. `pip install -U Flask`
4. `npm install -g heroku`
​
## Sign up for a Spotify Developer Account
1. Follow the instructions here: [Spotify Developer Account](https://developer.spotify.com/dashboard/)
2. Register your application to get authorization keys: [Register your application](https://developer.spotify.com/documentation/general/guides/app-settings/#register-your-app) 

## Copy this repo
1. On your GitHub account, create a new repository
2. In the terminal of your home directory, clone this repo: `git clone https://github.com/NJIT-CS490-SP21/project1-pp668.git`
3. Change the current working directory into the clned directory and you should see all of these project files.
4. Connect this cloned repo to your GitHub repo from Step 1: `git remote set-url origin https://www.github.com/{your-username}/{your-repo-name}`
5. Push the local repo to the remote repo: `git push origin main`

## Setup
1. Create a `.env` file in your main directory and add your Spotify client ID key and client secret key with the lines: `export CLIENT_ID='YOUR_ID'` and `export CLIENT_SECRET='YOUR_SECRET'`
2. To add your favorite artists to the list, add the artist's Spotify ID to line 18 in `app.py`. You can find the artist id [here!](https://support.tunecore.com/hc/en-us/articles/360040325651-How-to-Find-my-Spotify-Artist-ID)
​
## Run Application
1. Run command in terminal: `python app.py`
2. See output with the top 10 songs from a favorite artist as well as a preview of one of the listed songs! 

## Heroku Deployment
1. Create an account on Heroku: [Sign up for a free account](https://signup.heroku.com/login)
2. Create a `requirements.txt` file in your main directory and add all non-standard dependencies. In this project, they are `Flask`, `requests`, and `python-dotenv`.
3. Create a `Procfile` in your main directory and add the commands that Heroku needs to use to run your app: `python app.py`
4. Add and commit all of the files using git
5. Login got your Herohu account on your terminal: `heroku login -i`
6. Create a Heroku app: `heroku create`
7. Push all code to Heroku: `git push heroku main`
8. Go to your [Heroku dashboard](https://dashboard.heroku.com/apps) and open your application's settings
9. In "Reveal Config Vars", add your client id key and client secret key from your .env file with matching variable names and values
10. Run your application in you terminal: `heroku open`

## Known Problems
1. A few songs from several artists do not have any preview links. On the web application, the audio feature is greyed out as a result. I have yet to address this issue in my code, but I will attempt to get around it by only fetching information of songs with all required fields filled in. 
2. The code iss slightly unorganized. In order to enhance user readibility, I will attempt to add more comments to my code and create classes where necessary to separate methods/function definitions.
3. My web application has yet to be beautified. The UI is very rigid and is not layed out in an organized manner. I will attemp to beautify my web app by choosing more attractive colors, mature fonts, and styling elements (rounded image corners, etc.).

## Technical Issues
1. HTML/CSS updates: When I first started this project, I made a simple css file and html file to track my changes on the web app as I updated my code. However, after the creation of the HTML and CSS files, any changes I made would not come up in the browser preview for my web app. I initially thought I wrote bad code, so I decided to search the web for an answer to this problem. After spending an hour looking on Stackoverflow and other forums, I still had not found a solution. I decided it was time for me to pose a question on Slack, but someone had already beat me to it. I found out that a hard refresh was the solution to my problem. My browser was caching my old css file and wasn't reading the updates I made. A hard refresh (shift+cmd+R) solved the issue.
2. GitHub: I started the project on Sunday, January 31. I had written out most of the backend dev code for my web app and I was getting ready to push it to a GitHub repo I made on my personal account. After the organization account was created later that week, I decided to push the same code to a repo I made in the organization but I encountered an issue. On my Cloud9 terminal, an error came up stating that my local branch was behind my remote branch. I executed a bad command (git push --force) without understanding the consequences and had lost all of my commit history. I tried to undo my changes but it was to no avail. In the end, I recreated a git repo, linked it to a new remote repo, and pushed all of my existing code. 
3. JSON readability: I started the project by using the Spotipy wrapper class. The documentation for the wrapper class had very detailed explanations for how to use the methods within the class and how to access all the information required for this project. however, I decided to rewrite my code where I created methods using the Spotify APU documentation to gain a better understanding of how information could be fetced using APIs. In this attempt, I had a very hard time understanding the JSON elements because there was no clear indentation provided when viweing the elements.In order fo rme to understand whether or not I was reaching the write information, I needed a better way to map the JSON information. I used the [JSON formatter](https://jsonformatter.curiousconcept.com/) to make the information more readable. Doing so proved to be very useful to me because now I was able to easily traverse the information to access necessary elements to complete this project.