# gitbackhub

![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/MarkusH/gitbackhub/CI/master?style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/gitbackhub?style=for-the-badge)

A script to backup / mirror GitHub repositories.

## Config

Get yourself a [personal access token](https://github.com/settings/tokens) on GitHub that has the `repo` scope.

Config file in `~/.config/gitbackhub/config.ini`.

```ini
[main]
user = GitHubUserName
access_token = AccessToken
directory = /path/to/target/directory

[user:GitHubUserName]
[user:AnotherGitHubUserName]

[org:GitHubOrgName]
[org:AnotherGitHubOrgName]

[repo:SomeGitHubUser/some-repo]
[repo:YetAnotherGitHubUserName/another-repo]
[repo:YetAnotherGitHubOrgName/yet-another-repo]
```

Make sure the file is not readable by anybody but yourself since it contains your GitHub token.


## Help

```shell
$ gitbackhub --help
Usage: gitbackhub [OPTIONS]

Options:
    --access-token TEXT
    --user TEXT
    --directory DIRECTORY  The data directory to clone to
    --config PATH
    --help                 Show this message and exit.
```
