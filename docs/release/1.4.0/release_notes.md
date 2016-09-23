Chunky 1.4.0
============

## Downloads

* [Windows installer](https://launchpad.net/chunky/1.4/1.4.0/+download/Chunky-1.4.0.exe)
* [Mac bundle](https://launchpad.net/chunky/1.4/1.4.0/+download/Chunky-1.4.0.dmg)
* [Cross-platform binaries](https://launchpad.net/chunky/1.4/1.4.0/+download/Chunky-1.4.0.zip)
* [Only launcher (win, mac, linux)](http://chunkyupdate.llbit.se/ChunkyLauncher.jar)

## Release Notes

NOTE: This version **REQUIRES** Java 8 update 40 or later!

The User Interface has been modernized by rewriting it in JavaFX.

This release also includes the following changes:

* Minecraft 1.10 blocks are now supported.
* Improvements to the command-line interface.
* Small rendering fixes (fog, droppers, dispensers, chorus plant, end rods).
* Many bug fixes.



## ChangeLog

* Chunky now requires Java 8 update 40, or a later version.
* Added rendering for Minecraft 1.10 blocks:
    * Bone Block
    * Magma Block
    * Red Nether Brick
    * Nether Wart Block
* Modernized the Chunky User Interface by rewriting it in JavaFX.
* Most of the UI remains similar to the old version, but some parts
  were redesigned:
    * Controls for multiple cameras have been simplified.
    * The Highlight tab has been merged into the Options tab.
    * The gradient editor and color pickers were slightly redesigned.
    * Added some sky gradient presets.
    * Removed the fullscreen option for the preview window.
* Removed old features that were not well supported. The goal is to
  make these into separate plugins:
    * Removed the benchmark tool.
    * Removed the experimental OpenCL renderer.
* Holding Control while moving the camera multiplies move distance by 100.
* The render preview scaling option has been moved into a context menu.
  Right clicking the render preview window brings up the scaling menu.
* Added option to show guide grid in the render preview. The option is
  accessed through the right-click context menu.
* Pressing Space in the render preview window starts/pauses/resumes rendering.
* Fixed player entities not being saved if they were the only entity type in a
  scene.
* Fixed bug preventing new players from being added to a scene if no players
  were already loaded.
* Minor changes to the UI:
    * Added an icon to the camera view visualization.
    * Removed the chunk loading indicator icon.
    * Removed the player Y position indicator.
    * Removed fullscreen preview.
* Added new command-line options:
    * Added -list-scenes command.
    * Added -merge-dump command.
    * Made it possible to manually set the Chunky settings directory using a
      system property (java -Dchunky.home=DIR).
* Added Omni-Directional Stereo projector (thanks leMaik!)
* Rendering improvements and fixes:
    * End rods now emit light.
    * Vertical droppers and dispensers are now rendered correctly.
    * Improved fog rendering through glass and other transparent materials.
    * Fixed issue causing Chorus Plant to not connect to End Stone blocks.
* Experimental Plugin API added.
