==========
gitbackhub
==========

A script to backup / mirror GitHub repositories.

Config
======

Config file in ``~/.config/gitbackhub/config.ini``::

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


Help
====

::

   $ gitbackhub --help
   Usage: gitbackhub [OPTIONS]

   Options:
     --access-token TEXT
     --user TEXT
     --directory DIRECTORY  The data directory to clone to
     --config PATH
     --help                 Show this message and exit.
