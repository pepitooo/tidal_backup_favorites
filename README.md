# tidal backup/restore favorites

Simple python program backup and restore data from/to account
Use full when you have to change account evey months.

```
$ python main.py
usage: main.py [-h] (--backup | --restore) --user USER --password PASSWORD [--filename FILENAME]
main.py: error: the following arguments are required: --user/-u, --password/-p

$ python main --backup --user mail@address.com --pass 123456
```
It will create a json file `tidal_favorites.json` with tidal favorites data

to restore it 
```
$ python main --restore --user other_mail@address.com --pass 123456
```