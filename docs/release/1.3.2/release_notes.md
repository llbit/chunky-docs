Chunky 1.3.2
============

###Downloads

* [Windows installer](https://launchpad.net/chunky/1.3/1.3.2/+download/Chunky-1.3.2.exe)
* [Cross-platform binaries](https://launchpad.net/chunky/1.3/1.3.2/+download/Chunky-1.3.2.zip)
* [Only launcher (win, mac, linux)](http://chunkyupdate.llbit.se/ChunkyLauncher.jar)

###Release Notes

This release fixes some bugs and adds some minor improvements.

Chunky now avoids saving the octree if it was not modified since the last
snapshot. This should improve headless rendering which typically does not
modify the octree.


###ChangeLog

    * Added option to the sky tab for rendering the sky transparent.
    * Minor improvements to Launcher command-line interface.
    * Fixed rendering of the 1.8 fence blocks using Birch, Spruce, Jungle,
      Dark Oak, and Acacia wood
    * Octree and grass/foliage textures are not saved to disk again if they
      were not changed since the last time they were saved
    * Added Stereographic projection mode
    * The launcher now remembers Java options changed in the launch settings
    * More descriptive error message when failing to open a texture pack
