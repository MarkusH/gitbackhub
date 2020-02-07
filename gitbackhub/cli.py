#!/usr/bin/env python
import configparser
import os
import subprocess

import click
import requests

APP_NAME = "gitbackhub"
GITHUB_API_URL = "https://api.github.com"
OWN_REPOS_URL = "/user/repos?page={page}&affiliation=owner"
USER_REPOS_URL = "/users/{user}/repos?page={page}"
ORG_REPOS_URL = "/orgs/{org}/repos?page={page}"


def read_config(file=None):
    cfg = file or os.path.join(click.get_app_dir(APP_NAME), "config.ini")
    parser = configparser.ConfigParser(default_section="*")
    parser.read([cfg])
    return parser


def _fetch_repos(base_url, access_token, **kwargs):
    page = 1
    repos = []
    headers = {"Authorization": "token {token}".format(token=access_token)}
    while True:
        url = GITHUB_API_URL + base_url.format(page=page, **kwargs)
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        json = response.json()
        if json:
            repos.extend([r["full_name"] for r in json])
        else:
            break
        page += 1
    return repos


def get_own_repos(access_token):
    return _fetch_repos(OWN_REPOS_URL, access_token=access_token)


def get_user_repos(user, access_token):
    return _fetch_repos(USER_REPOS_URL, access_token=access_token, user=user)


def get_org_repos(org, user, access_token):
    return _fetch_repos(ORG_REPOS_URL, access_token=access_token, org=org)


def clone_repo(name, path):
    parent_dir = os.path.dirname(path)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)

    with open("/dev/null", "w") as null:
        return subprocess.call(
            ["git", "clone", "--mirror", "git@github.com:%s.git" % name, path],
            stdout=null,
            stderr=null,
        )


def update_repo(name, path):
    with open("/dev/null", "w") as null:
        return subprocess.call(
            ["git", "remote", "update", "--prune"], cwd=path, stdout=null, stderr=null,
        )


def prepare_progressbar_string_list(strings):
    sl = []
    max_length = 0
    for s in strings:
        max_length = max(max_length, len(s))
        sl.append(s)
    return sl, max_length


@click.command()
@click.option("--access-token")
@click.option("--user")
@click.option(
    "--directory",
    help="The data directory to clone to",
    type=click.Path(file_okay=False, writable=True, resolve_path=True),
)
@click.option(
    "--config", type=click.Path(exists=True, dir_okay=False, resolve_path=True)
)
def cli(access_token, user, directory, config):
    cfg = read_config(config)
    access_token = access_token or cfg["main"]["access_token"]
    user = user or cfg["main"]["user"]
    directory = directory or cfg["main"]["directory"]
    directory = os.path.expanduser(directory)

    repos = []
    sections, max_length = prepare_progressbar_string_list(
        (section for section in cfg.sections() if section != "main")
    )
    click.secho("Fetching repos", color="blue")
    with click.progressbar(sections, label="".ljust(max_length)) as bar:
        for section in bar:
            bar.label = section.ljust(max_length)
            bar.render_progress()

            kind, _, value = section.partition(":")
            if kind == "user":
                if value == user:
                    repos.extend(get_own_repos(access_token))
                else:
                    repos.extend(get_user_repos(value, access_token))
            elif kind == "org":
                repos.extend(get_org_repos(value, user, access_token))
            elif kind == "repo":
                repos.append(value)

    repo_dir = os.path.join(directory, "repositories")
    git_errors = []

    repos, max_length = prepare_progressbar_string_list(repos)
    click.secho("Cloning and updating repos", color="green")
    with click.progressbar(repos, label="".ljust(max_length)) as bar:
        for repo in bar:
            bar.label = repo.ljust(max_length)
            bar.render_progress()

            path = os.path.join(repo_dir, repo)
            if os.path.exists(path):
                rc = update_repo(repo, path)
            else:
                rc = clone_repo(repo, path)

            if rc != 0:
                git_errors.append(repo)

    for repo in sorted(git_errors):
        click.secho("Error while processing %s" % repo, err=True, color="red")


if __name__ == "__main__":
    cli()
