Chunky 1.2.3
============

Downloads
---------

* [Windows Installer](https://launchpad.net/chunky/1.2/1.2.3/+download/Chunky-1.2.3.exe)
* [Cross-platform binaries (Mac, Win, Linux)](https://launchpad.net/chunky/1.2/1.2.3/+download/Chunky-1.2.3.zip)
* [Launcher only (Mac, Win, Linux)](http://chunkyupdate.llbit.se/ChunkyLauncher.jar)

Release Notes
-------------

This release of Chunky is in preparation for Minecraft 1.8. The remaining new
blocks from the latest Minecraft 1.8 snapshot (14w28b) are now supported!

This release also includes improvements to the 2D map that should
make it more useful for navigating larger worlds. There have also been many
smaller bugfixes for performance or rendering problems.

Change Log
----------

    * Added Minecraft 1.8 blocks:
        + Coarse Dirt
        + Prismarine (rough, block, dark)
        + Sea Lantern
        + Wet Sponge
        + Iron Trapdoor
        + Slime Block
    * Improved the 2D map:
        + More zoom levels
        + Mouse wheel scrolling zooms, Ctrl+Scroll changes layer
        + Fixed tearing issues
        + Improved performance for large map views
        + The name of the biome under the cursor is now displayed in lower-left
          corner of the map
        + Improved the rendering of many blocks in the block-layer mode
    * Right-clicking in the 2D map now opens a context menu with options to
      cre ate a new scene, load a scene, or clear the current selection
    * (potentially) Fixed issue causing the render preview window to display
      white after being closed and re-opened
    * Using the -snapshot command without arguments now prints a list of all
      available scenes in the scene directory
    * Using the -snapshot command without a destination PNG file name now
      automatically picks a filename based on the scene name and current SPP
    * Depth of field now only uses one scene variable (removed infDof variable)
    * Fixed corner Acacia/Dark Oak stairs rendering issue
    * Hay bales now render with the correct orientation
    * Fixed sign texture loading error (item icon was loaded rather than the
      entity texture)
    * Fixed error causing rayDepth setting to not be saved for scenes
    * Fixed error preventing naming and overwriting of custom camera presets
    * Added checkbox on the Advanced tab of Render controls which enables
      automatic shutdown of the computer after render completion
    * Fixed error in the rendering of iron bars
