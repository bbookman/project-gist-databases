import requests, pdb
import os
import json
import responses, pdb
from requests import exceptions

BASE_URL =  'https://api.github.com/'


def import_gists_to_database(db, username, commit=True):
    url = BASE_URL + 'users/{username}/gists'.format(username=username)
    response = requests.get(url)
    response.raise_for_status()
    # if response.status_code == 404:
    #     raise exceptions.HTTPError('{username}-doesnt-exist'.format(username = username))
    data = response.json()
    for gist in data:
        params = {
            'github_id': gist['id'],
            'html_url' : gist['html_url'],
            'git_pull_url': gist['git_pull_url'],
             'git_push_url': gist['git_push_url'],
            'commits_url': gist['commits_url'],
            'forks_url': gist['forks_url'],
            'public': gist['public'],
            'created_at': gist['created_at'],
            'updated_at': gist['updated_at'],
            'comments': gist['comments'],
          'comments_url': gist['comments_url']
        }
        
        INSERT_INTO_GIST = """INSERT INTO gists (
            "github_id", "html_url", "git_pull_url",
            "git_push_url", "commits_url",
            "forks_url", "public", "created_at",
            "updated_at", "comments", "comments_url"
        ) VALUES (
            :github_id, :html_url, :git_pull_url,
            :git_push_url, :commits_url, :forks_url,
            :public, :created_at, :updated_at,
            :comments, :comments_url
        );"""
        
        db.execute(INSERT_INTO_GIST, params)
        if commit:
            db.commit()

        # query = 'SELECT COUNT(*) FROM gists;'
        # cursor = db.execute(query)
        # pdb.set_trace()
        # count = cursor.fetchone()[0]
        # print(count)
        