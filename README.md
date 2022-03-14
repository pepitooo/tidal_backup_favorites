# tidal backup/restore favorites

Simple python program backup and restore data from/to account
Use full when you have to change account evey months.

## First install dependency with pip
```
$ pip install -r requirements.txt
```

## Do your first backup
```
$ python main.py
usage: main.py [-h] (--backup | --restore) [--ini INI] [--filename FILENAME]
main.py: error: one of the arguments --backup/-b --restore/-c is required

$ python main --backup
```

It will print a URL you have to visit for authentication and – after
successful authentication – the configuration you can provide via an
INI file for later runs:

```
authenticating new session
Visit link.tidal.com/FOOBA to log in, the code will expire in 300 seconds
To load the session next time you run this program, supply the following information via INI file:

[session]
id = …
token_type = …
access_token = …
refresh_token = …
```

It will also create a json file `tidal_favorites.json` with tidal favorites data.

On later runs, you can provide an INI file with the data mentioned
above (e.g., in `config.ini`), so you don't have to authenticate
manually again:

```
$ python main --backup --ini config.ini
```

## Then restore it
```
$ python main --restore  --ini config.ini
```
