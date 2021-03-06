# progress
An app for maintaining weekly snippets of progress on goals or tasks.

## Screenshots
### Weekly Snippet
![](https://raw.githubusercontent.com/csu/progress/master/screenshots/main.jpg)

### Editor
![](https://raw.githubusercontent.com/csu/progress/master/screenshots/editor.jpg)

## Installation
```
pip install makeprogress
progress goals/
```

Open `localhost:5000` in a browser.

## Usage
* Click on `Current` in the navigation to view your snippet for the current week.
* Click on `Edit` in the nav bar on any snippet page to open the editor for it.
* Click on `Archive` in the nav bar to view a list of weeks in the year and get to past snippets.
* Click on `Goals` in the nav bar to view your goals (Only works if you created a `_goals.md` file. Currently hard-coded in.)

### Options
```
$ progress -h
usage: progress [-h] [-t TEMPLATE] [-e FILEEXT] data_store_path

positional arguments:
  data_store_path

optional arguments:
  -h, --help            show this help message and exit
  -t TEMPLATE, --template TEMPLATE
                        template file name
  -e FILEEXT, --fileext FILEEXT
                        file extension
```
