Chunky Documentation
====================

This is the repository for the Chunky Documentation. Any help with keeping this
documentation up to date is much appreciated. The simplest way to request a
change or addition is to send me a pull request.

New Site: [http://docs.llbit.se/][0]

Workflow
--------

The webpages can be generated in the local directory `out` using the
[Apache Ant][1] build script in the project root. If you have Ant installed
you only need to run Ant using a shell or command prompt in the project root.

The build script runs a Python script named `tools/mdwrapper.py` on all
Markdown files (`*.md`) in the `docs` directory. Before the python script is
run some special tokens such as `%VERSION%` are replaced for the values listed
in the `version.properties` file. The build script finally copies all files in
the `images` and `style` directories into the output directory.

After you have run the build script you will need a web server to serve the
pages in the `out` directory. One simple way to do this is with a [small
nodejs web server script][2].

Requirements
------------

The build script `build.xml` requires [Apache Ant][1] to run.

Python and python-markdown are required to generate the documentation pages.

    pip install markdown


[0]:http://docs.llbit.se/
[1]:http://ant.apache.org/
[2]:http://stackoverflow.com/a/13635318
