Chunky 1.2.2
============

Downloads
---------

* [Windows Installer](https://launchpad.net/chunky/1.2/1.2.2/+download/Chunky-1.2.2.exe)
* [Cross-platform binaries (Mac, Win, Linux)](https://launchpad.net/chunky/1.2/1.2.2/+download/Chunky-1.2.2.zip)
* [Launcher only (Mac, Win, Linux)](http://chunkyupdate.llbit.se/ChunkyLauncher.jar)

Release Notes
-------------

This release includes several small bug fixes and general interface
improvements:

* Pressing the U key in the 3D preview window makes it go full-screen.
* The 2D map has been improved and now updates dynamically.
* The 3D rendering interface was made more compact by replacing the
  camera preset buttons with a drop-down list.
* It is now possible to save/load custom camera presets for each scene.
* The scene selector can delete scenes and export scenes to a Zip archive.
* Reduced default Sun intensity a bit.

Headless rendering has been improved and there are some new commands in the
command-line interface:

    -snapshot <SCENE> <PNG> render the latest saved render dump to a PNG image
    -download-mc <VERSION>  download the specified version of Minecraft
    -version                report the current Chunky version
    --update                download the latest Chunky version
    --setup                 configure the maximum memory limit and Java options
    --verbose               shows the command used to run Chunky
    --version               report the current launcher version

Note that the Minecraft version downloaded with the -download-mc command is
used as the default texture source *only if* no other Minecraft version is
found by Chunky.

Change Log
----------

    * Added "follow player" option for the 2D map
    * Made 2D map drawing more efficient
    * Adjusted default Sun intensity to 1.25
    * It is now possible to save and load custom camera presets
    * Made Render Controls dialog more compact
    * Moved camera presets to drop-down list
    * Added Granite, Diorite, and Andesite stone blocks
    * Chunky now dynamically refreshes the main map view based on
      changes to the Minecraft world as detected in the filesystem
    * Added Chunky commands: -snapshot, -version, -download-mc
    * Added launcher commands: --setup, --update, --version, --verbose
    * Fixed error causing the launcher to crash when running in headless mode
      if the launcher GUI had not previously been run
    * The launcher (v1.7.0 and later) now ignores older releases if a newer
      version already is installed
    * Using -render without a scene name argument prints out available scenes
    * Added Help tab listing keyboard shortcuts in the Render Controls window
    * Pressing U in the Render Preview window makes it go fullscreen
    * The scene selector can now to delete scenes or export scenes to Zip file
    * Fixed potential crash in the launcher from a clean install
