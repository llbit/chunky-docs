Chunky Documentation
====================

This is the repository for the [Chunky Documentation][0].  The documentation is
currently hosted at [http://chunky.llbit.se/][0].

Any help with keeping this documentation up to date is much appreciated!
[Click here for more info about editing the documentation.][5]


Editing
-------

You can edit any file easily right here on GitHub. All you need is a GitHub
account. You can navigate to a file you want to edit via the file tree and
click the `Edit` button after selecting a file. We use [Markdown syntax][3] for
all documentation pages.

Dependencies
------------

* [Apache Ant][1]
* Python
    * Python-Markdown
    * PIL

Testing
-------

The webpages can be generated in the local directory `out` using the [Apache
Ant][1] build script in the project root. If you have Ant and the other
dependencies installed you only need to run Ant using a text terminal in the
project root. The script will do the rest.

The build script runs a Python script named `tools/mdwrapper.py` on all
Markdown files (`*.md`) in the `docs` directory. Before the python script is
run some special tokens such as `%VERSION%` are replaced with the values listed
in the `version.properties` file. The build script then creates thumbnails for
the gallery and finally copies all files in the `images` and `style`
directories into the output directory.

After you have run the build script you will need a web server to serve the
pages in the `out` directory in order to get them to render correctly in the
web browser. One of the simplest ways to set this up, if you have NodeJS and
NPM installed, is to run the following commands:

    $ npm install http-server -g
    $ cd out
    $ http-server -o --cors

Another way to do this with nodejs is with your own [small nodejs web server
script][2].

Requirements
------------

The build script `build.xml` requires [Apache Ant][1] to run.

Python and python-markdown are required to generate the documentation pages.

    pip install markdown

The Python Imaging Library (PIL) is required to create thumbnail images for
the gallery. PIL can be installed by the command

    pip install pil

Alternatively, for Windows users, you can download Pillow from [here][4].


[0]:http://chunky.llbit.se/
[1]:http://ant.apache.org/
[2]:http://stackoverflow.com/a/13635318
[3]:http://daringfireball.net/projects/markdown/syntax
[4]:http://www.lfd.uci.edu/~gohlke/pythonlibs/
[5]:http://chunky.llbit.se/contributing.html#documentation
