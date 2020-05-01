import requests
import logging
import argparse
import json
from github import Github


def main(token):
    g = Github(token)

    for repo in g.get_user().get_repos():
        print(repo.name)
        repo.edit(has_wiki=False)
        # to see all the available attributes and methods
        print(dir(repo))





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--token', dest='token', help='Github Token', required=True)
    args = parser.parse_args()
    main(args.token)