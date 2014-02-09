How to Contribute
=================

The simplest way to help with the development of Chunky is to report any issues
you may come accross on the [Chunky issue tracker][1]. If you do have a bug to
report or a feature to request, please do a quick search on the issue tracker
first to see if your issue has already been reported.

Besides reporting issues you can:

* [Update the documentation](#documentation)
* [Fix bugs](#bug)
* [Implement new features](#feature)

<a name="documentation"></a>Updating the Documentation
------------------------------------------------------

The Chunky documentation is managed in a [separate GitHub project][2]. It is
pretty simple to propose changes to the documentation if you have a GitHub
account. Simply locate the file you wish to edit and click the ["Edit" button
in the GitHub interface][3]. When you are satisfied with the changes you will
be able to submit a ["pull request"][4]. If all is well your changes will soon
be incorporated into the official documentation.

<a name="documentation"></a>Fixing a Bug
----------------------------------------

Fixing bugs for the most part requires some experience in the Java programming
language. If you have found an bug you want to fix in the issue tracker and
think that you are up to the task, comment on the issue to let others know that
you are working on it and get to work.

When you are done with coding the fix you can create a pull request.  These are
the guidelines for pull requests to the main Chunky repository:

* Your work must be licensed under the same license as the rest of the Chunky
  source files. If you create a new file please copy the license header from
  another file and edit the copyright notice with your name or internet handle.
* Please follow the same code style as is used in the rest of Chunky. Chunky
  use the standard Eclipse Java code style, except for some rare exceptions.
* Do not throw unchecked exceptions.
* Please try to implement or fix *one thing* per commit.
* Rebase your commits onto `origin/master`.  I generally try to avoid branching
  commit history.
* Commit messages should be [neatly formatted][5]. The first line must not
  exceeed 50 characters.

<a name="feature"></a>Implementing a New Feature
------------------------------------------------

If there is a new feature you want to have added to Chunky you must first
create a feature request on the issue tracker and clearly state that you want
to work on implementing the feature. If your feature is deemed appropriate feel
free to implement it and submit a pull request by following the instructions
for pull requests listed above.

If you find a feature which nobody appears to be working on you can start
implementing it yourself, but you must tell others in the feature request on
GitHub that you plan to implement it.

The guidelines for new features are:

* Should improve a common user story
* Should generally be self-contained, with as few new library dependencies as
  possible

The maintainer reserves the right to reject features and pull requests, please
don't get mad if your feature doesn't make it in Chunky. The more you
communicate about what you are working on the better.

[1]: https://github.com/llbit/chunky/issues
[2]: https://github.com/llbit/chunky-docs
[3]: https://help.github.com/articles/creating-and-editing-files-in-your-repository
[4]: https://help.github.com/articles/creating-a-pull-request
[5]: http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
