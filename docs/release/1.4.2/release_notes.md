Chunky 1.4.2
============

## Downloads

* [Windows installer](https://launchpad.net/chunky/1.4/1.4.2/+download/Chunky-1.4.2.exe)
* [Mac bundle](https://launchpad.net/chunky/1.4/1.4.2/+download/Chunky-1.4.2.dmg)
* [Cross-platform binaries](https://launchpad.net/chunky/1.4/1.4.2/+download/Chunky-1.4.2.zip)
* [Only launcher (win, mac, linux)](http://chunkyupdate.llbit.se/ChunkyLauncher.jar)

## Release Notes

This release adds Minecraft 1.11 support, quality of life improvements, and bugfixes.

Quality of life improvements:

* Added a scene settings import/export system.
* Added multiple resource pack support.
* Small improvements in the command-line interface.


## ChangeLog

* Added support for multiple resource packs. The resource pack
  load order can be changed via Options->Edit resource packs.
* Added rendering for Minecraft 1.11 blocks:
    * Observer Block
    * Shulker Box
* Added scene settings export/import system.
* It is now possible to temporarily change the view target via the
  render preview context menu. This is useful for autofocus and moving
  entities.
* Updated command block rendering to be compatible with Minecraft 1.9+.
* Added scale setting for player entities.
* Improved error checking for resource packs.
* Fixed rendering errors for trapdoors, redstone dust, and comparator blocks.
* The --update command now creates a settings directory if needed.
* Default settings should be generated when running headless commands for the
  first time.
