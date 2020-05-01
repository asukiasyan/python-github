import confuse
import requests
import logging
import argparse
import json
from github import Github

class ObjectView(object):
    def __init__(self, d):
        self.__dict__ = d

config = confuse.LazyConfig('github-python')
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s: %(message)s')

def main(token):
    gl = Github(token)
    create_repo(gl)


def create_repo(gl):
    if 'create_repo' not in config.get():
        return
    repository = config['create_repo'].get()
    for name in repository:
        name = ObjectView(name)
        repo = name.repository
        gl.get_user().create_repo(str(repo))
        # for key, value in item.attributes.items():
            # try:
                # repository = gl.get_user().get_repo("temporary")
                # print(repository.name)
                # repository.edit(key, value)
            #     setattr(gl_project, key, value)
            # except TypeError as err:
            #     logging.warning(f'skip creation of {repo}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--token', dest='token', help='Github Token', required=True)
    parser.add_argument('-f', '--config-file', dest='config_file', help='Repository List', required=True, default='config.yaml')
    args = parser.parse_args()
    config.set_file(args.config_file)
    main(args.token)
