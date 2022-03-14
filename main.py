#!/usr/bin/env python3

import argparse
import json
import sys

import tidalapi


def backup(session, filename):
    tidal_favorites = dict(albums=[], artists=[], tracks=[], playlists=[])
    artists = session.user.favorites.artists()
    for e in artists:
        tidal_favorites['artists'].append(dict(name=e.name, id=e.id))

    tracks = session.user.favorites.tracks()
    for e in tracks:
        tidal_favorites['tracks'].append(dict(name=e.name, id=e.id))

    albums = session.user.favorites.albums()
    for e in albums:
        tidal_favorites['albums'].append(dict(name=e.name, id=e.id))

    playlists = session.user.favorites.playlists()
    for e in playlists:
        tidal_favorites['playlists'].append(dict(name=e.name, id=e.id))

    with open(filename, 'w') as outfile:
        json.dump(tidal_favorites, outfile, indent=4)
    print(tidal_favorites)


def restore(session, filename):
    with open(filename) as json_file:
        tidal_favorites = json.load(json_file)
        for a in tidal_favorites['artists']:
            try:
                session.user.favorites.add_artist(a['id'])
                print(f'Artist {a["name"]} added as favorite')
            except:
                pass
        for a in tidal_favorites['tracks']:
            try:
                session.user.favorites.add_track(a['id'])
                print(f'Track {a["name"]} added as favorite')
            except:
                pass
        for a in tidal_favorites['albums']:
            try:
                session.user.favorites.add_album(a['id'])
                print(f'Album {a["name"]} added as favorite')
            except:
                pass
        #for a in tidal_favorites['playlists']:
        #     session.user.favorites.add_playlist(a['id'])


def parse_args(args):
    """
    Parse command line parameters

    :param args: command line parameters as list of strings
    :return: command line parameters as :obj:`argparse.Namespace`
    """
    parser = argparse.ArgumentParser(description="Backup/Restore Tidal tracks/albums/artist favorites")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--backup', '-b', action='store_true', help='Backup favorites')
    group.add_argument('--restore', '-c', action='store_true', help='Restore favorites')

    parser.add_argument('--user', '-u', dest='user', required=True)
    parser.add_argument('--password', '-p', dest='password', required=True)
    parser.add_argument('--filename', '-o', dest='filename', default=None)

    return parser.parse_args(args)


def main(args):
    args_parsed = parse_args(args)
    print(args_parsed)

    session = tidalapi.Session()
    session.login(args_parsed.user, args_parsed.password)

    if args_parsed.backup:
        backup(session, args_parsed.filename or 'tidal_favorites.json')
    if args_parsed.restore:
        restore(session, args_parsed.filename or 'tidal_favorites.json')


if __name__ == '__main__':
    main(sys.argv[1:])
