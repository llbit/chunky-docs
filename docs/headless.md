Headless Rendering
==================

Headless rendering in Chunky can be used to render scenes without using the
GUI, and is useful for example when rendering on a server or when automating
or scripting renders.

Chunky Launcher
---------------

When working with Chunky from the command line, you should be aware of what the
launcher does. The launcher is bundled with Chunky since version 1.2.0 and it
is responsible for launching Chunky by starting a new Java process.

Command-line arguments that start with one dash, like `-snapshot` are sent
to Chunky, while arguments starting with two dashes, like `--update`, are
options to the launcher.

### JVM Options

JVM options (memory limit etc.) used when starting Chunky normally only
apply to the launcher and not the actually Chunky process.
Any JVM options you want to add to the Chunky command must be added to the
`javaOptions` variable in the `chunky-launcher.json` file in your local
Chunky settings directory (`~/.chunky` is the default directory).

To see the Java command line arguments used to start Chunky you can add
the `--verbose` flag when running Chunky. This makes the launcher print the
command it used to start Chunky.

Custom Settings Directory
-------------------------

Since version 1.4 Chunky allows specifying a custom settings directory via
the `chunky.home` Java property. The property can be passed to the
Chunky launcher and the launcher will then pass it on to Chunky itself.

Changing the settings directory can be useful if you need to run multiple
instances of Chunky on the same computer, or if you just need more control
over where the settings and scenes are stored.

Here is an example showing how to specify a custom scene directory:

    $ mkdir ~/chunky
    $ java -Dchunky.home="~/chunky" -jar ChunkyLauncher.jar --update


Note that the `-Dchunky.home` argument must be passed before `-jar`.  If you
are using Bash it is convient to make an alias for the `java` command
above, for example:

    CHUNKY_HOME=~/chunky
    alias chunky java -Dchunky.home="$CHUNKY_HOME" -jar ChunkyLauncher.jar


The lines above could also be added to your `.bashrc` file.


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

3. Make Chunky download some Minecraft version (for example 1.11.2):

        java -jar ChunkyLauncher.jar -download-mc 1.11.2


Rendering
---------

Rendering a scene using the command-line interface is simple, assuming that you
have set up the scene parameters and copied your scene files to your scene
directory (default=`$CHUNKY_HOME/scenes`).

The simplest way to render a scene is to run the command

    chunky -render SceneName


Replace `SceneName` with the name of your scene. Run this command to print
a list of all available scenes:

    chunky -list-scenes


Chunky will keep rendering until it reaches the target SPP. You can stop Chunky
prematurely by hitting `Ctrl-C`, however this does not save the current
rendering progress! The render progress is normally saved after intervals
determined by the `dumpFrequency` scene setting.

Snapshots can be created from a scene with some saved rendering progress by
using the `-snapshot` command:

    chunky -snapshot SceneName snapshot.png

The `snapshot.png` part of is the filename for the Png file to create.

Command-Line Options
--------------------

Run Chunky with the `-help` command to see a list of all available command-line
options. Currently these options are available:

* `-render <SCENE>` - render in headless mode.
	You may also need to add the `-f` flag to force a scene to render.
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

