Headless Rendering
==================

This article describes how to work with Chunkys command-line interface.
Rendering using the command-line interface is also referred to as Headless
Rendering.

Chunky Launcher
---------------

When working with Chunky from the command line, you must be aware of what the
Chunky launcher does. The launcher is bundled with Chunky since version 1.2.0
and it is responsible for launching Chunky by starting a new Java process. This
means that JVM options (memory limit etc.) you use when starting Chunky will
normally only apply to the launcher and not the actually Chunky process.

To see the command used to start Chunky itself you can add the `--verbose`
option to your Chunky. This makes the launcher echo the command it used to
launch Chunky.

Any JVM options you want to add to the Chunky command must be added to the
`javaOptions` variable in the `chunky-launcher.json` file in your local
Chunky settings directory (`~/.chunky` is the default directory). You can
also use the `--setup` command which can be used to set up the launcher
settings via the command-line.

If you send any command line arguments to the launcher it will assume that
Chunky should run in headless mode, unless the `--nolauncher` option is
given in which case Chunky is started as regular, but without showing
the launcher window. The `--launcher` option overrides everything else
and forces the launcher to appear.

Custom Settings Directory
-------------------------

Since version 1.4 Chunky allows specifying a custom settings directory via
the `chunky.home` system property. The system property can be passed to the
Chunky launcher and the launcher will then pass it on to Chunky itself.

Changing the settings directory can be useful if you need to run multiple
instances of Chunky on the same computer, or if you just need more control
over where the Chunky settings are stored.

Here is an example showing how to use a custom scene directory:

    $ mkdir ~/chunky
    $ java -Dchunky.home="~/chunky" -jar ChunkyLauncher.jar --update


Note that the `-Dchunky.home` argument must be passed before `-jar`.
It may be convient to make an alias out of the `java` command above.
For example:

    CHUNKY_HOME=~/chunky
    alias chunky java -Dchunky.home="$CHUNKY_HOME" -jar ChunkyLauncher.jar


The above lines could be added to your `.bashrc`.

Setting Things Up
-----------------

It may be necessary to do some setup before you can start rendering in headless
mode.

The following steps should be done before the first time you start rendering
in headless mode, and some of these steps may need to be repeated later to
update Chunky or Minecraft:

1. Download Chunky and place the Jar-file on your rendering machine. It is
  sufficient to download the latest version of the Launcher by issuing this
  command:

        wget http://chunkyupdate.llbit.se/ChunkyLauncher.jar

2. Download the latest version of Chunky:

        java -jar ChunkyLauncher.jar --update

3. Make Chunky download some Minecraft version (for example 1.7.4):

        java -jar ChunkyLauncher.jar -download-mc 1.7.4

4. Optional: create an alias for Chunky. For Bash you can do this:

        echo "alias chunky='java -jar $(pwd)/ChunkyLauncher.jar'" >> ~/.bashrc


Rendering
---------

Rendering a scene using the command-line interface is simple, assuming that
you have set up the scene parameters and copied your scene files to your directory
(default=`~/.chunky/scenes`).

The simplest way to render a scene is to just run the command

    chunky -render SceneName

Replace `SceneName` with the name of your scene. Omitting the scene name prints
a list of available scenes and the path to the current scene directory.

Chunky will keep rendering until it reaches the target SPP or until the process
is ended. You can terminate Chunky prematurely by hitting `Ctrl-C`. However,
remember that the scene is not saved except for every so many samples, as
determined by the `dumpFrequency` scene setting, or when the render has
completed.

If you have rendered a scene for a while and just want to be able to create a
snapshot without waiting for it to complete you can use the `-snapshot`
command which takes the latest render dump and creates a snapshot from that:

    chunky -snapshot SceneName snapshot.png

The `snapshot.png` part of the command is the path to the Png file to create.

Command-Line Options
--------------------

Run Chunky with the `-help` command to see a list of all available command-line
options. Currently these options are available:

* `-render <SCENE>` - render in headless mode
* `-texture <FILE>` - load the specified texture pack
* `-snapshot <SCENE> <PNG>` - create a snapshot from a scene
* `-scene-dir <DIR>` - specify scene directory
* `-threads <NUM>` - change number of render threads
* `-tile-width <NUM>` - modifies the frame subdivision size per worker thread
* `-target <NUM>` - set the SPP target for the current headless render
* `-set <NAME> <VALUE>` - modify a Chunky setting value
* `-set <NAME> <VALUE> <SCENE>` - modify a scene setting
* `-reset <NAME>` - reset a Chunky setting to its default value
* `-reset <NAME> <SCENE>` - reset a scene setting to its default value
* `-download-mc <VERSION>` - download a particular version of Minecraft
* `-list-scenes` - list available scenes in the scene directory (since 1.4.0)
* `-merge-dump <SCENE> <PATH>` merge a render dump into the specified scene (since 1.4.0)
* `-help` - print the command-line help

The launcher accepts these commands:

* `--update` - download the latest version of Chunky
* `--setup` - interactive command-line Chunky setup
* `--nolauncher` - should not be used in headless mode
* `--launcher` - force the launcher UI to be shown
* `--version` - display the launcher version
* `--verbose` - enable verbose logging

