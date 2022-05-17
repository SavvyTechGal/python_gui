# ReadMe
## Project Description: 
Music Player Gui using PyQt5

## How to run final app
Run app.py

Click file in menu bar and open a folder of music -> folder contents will appear as a list in the directory list (the top list)

Click play to play from directory list. It will play sequetially unless shuffle or loop is clicked on.

### How To create a playlist
Select a song by single clicking on it so that is highlighted in the directory list box (top box on the left)

Click the + icon and the highlighted song will be added to your playlist

Keep adding songs till playlist is complete

You can remove a song by singal clicking it to highlight and clicking the - button.

You can clear your playlist and start over by clicking the clear button

To play your final playlist, check the checkbox play from playlist and click the play button on the player. 

Your playlist will now play. 

Note: You will not be able to add or remove or clear songs from the playlist while it is playing. To edit your playlist and play from the directory again, uncheck the play from playlist box. 




### Intended Features included:
Play | Pause | Mute | Loop | Shuffle | Next Track | Back Track

Song Label

Scroll through song

Volume Control Knobe

Create Playlist 

See list of playlists

Open playlist and see tracks

Play Playlist

Open folder/Directory and display that inside sidebar

### Potential Additional Fun Features:
Display Wave of Song 

Select Snippet of Song as a Ringtone

EQ


## Collaboration Best Practices
Create branch for each Feature in format:
feature/feature_name

commit as you make changes to that branch 

When feature is finished, Create pull request, and merge to master.


## Create a Virtual Env
```
$ python3 -m venv gui
```

This activates the virtual environment

```
$ source gui/bin/activate
```
This installs the dependencies in the virtual environment

```
$ pip install -r requirements.txt
```

If you get an error: 
set the path

```
$ PATH="/usr/local/opt/icu4c/sbin:/usr/local/opt/icu4c/bin:$PATH"
```

Then run:

```
$ pip install pyicu

```

Then run this again:

```
$ pip install -r requirements.txt

```

# Requirements: 

You can create an app that does anything you want it to, but there are some minimum requirements. 

Your app needs to be:
   1. Written in Python, 
   2. must have a GUI
   3. must host the app 
   4. must write commits to GitHub
   5. need to use a collaboration strategy while building the app

## App logic requirements:
You need to create:
   1. at least 4 functions (outside of the classes) 
   2. 3 classes for the logic of the application. 
NOTE: This is not the GUI section, it is what happens in the backend. 

App logic (10 points): 2 points per class, 1 point per function. Each class must have an init and at least two methods

## App GUI requirements:

You need to have:
   1. a window  
   2. at least 6 different widgets on your application. 
NOTE: Built in widgets like close or minimize are not included here. 

GUI (9 points): Each on screen widget is worth 1.5 points.


## Github Collaborative Strategy

Must define each feature of the project and the individual issues of each of those features 

Each branch should be one Issue and only once a full issue is completed should it be pushed to the master branch. 

GitHub (8 points): Each issue is worth a point. Using a collaborative strategy is worth 4 points.


## Spec Documentation

You should have:
   1. ReadMe which describes what your project is attempting to do
   2. technical spec detailing your functions, classes and what each does
   3. md file which details the problems you ran into and how you solved them (I recommend periodically updating a sheet like this when you encounter an interesting issue)

Other specs (3 points): Each of the spec documents above are worth 1 point.