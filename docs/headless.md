Headless Rendering
==================

This article describes rendering scenes using Chunkys command-line interface.
This is referred to as "Headless Mode".

Chunky Launcher
---------------

When working with Chunky from the command line, you must be aware of what the
Chunky launcher does. The launcher is bundled with Chunky since version 1.2.0
and it is responsible for actually launching Chunky by spawning a new Java
process. This means that JVM options (memory limit etc.) you use when starting
Chunky will only apply to the launcher and not the actually Chunky process.

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
you have set up the scene parameters and copied your scene files to your directory (default=`~/.chunky/scenes`).

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

* `-render <SCENE>`
* `-texture <FILE>`
* `-snapshot <SCENE> <PNG>`
* `-scene-dir <DIR>`
* `-benchmark`
* `-threads <NUM>`
* `-tile-width <NUM>`
* `-target <NUM>`
* `-set <NAME> <VALUE>`
* `-set <NAME> <VALUE> <SCENE>`
* `-reset <NAME>`
* `-reset <NAME> <SCENE>`
* `-download-mc <VERSION>`
* `-help`

The launcher accepts these commands:

* `--update`
* `--setup`
* `--nolauncher`
* `--launcher`
* `--version`
* `--verbose`

