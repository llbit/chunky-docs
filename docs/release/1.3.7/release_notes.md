Chunky 1.3.7
============

###Downloads

* [Windows installer](https://launchpad.net/chunky/1.3/1.3.7/+download/Chunky-1.3.7.exe)
* [Mac bundle](https://launchpad.net/chunky/1.3/1.3.7/+download/Chunky-1.3.7.dmg)
* [Cross-platform binaries](https://launchpad.net/chunky/1.3/1.3.7/+download/Chunky-1.3.7.zip)
* [Only launcher (win, mac, linux)](http://chunkyupdate.llbit.se/ChunkyLauncher.jar)

###Release Notes

This version adds basic player entity rendering. The player in a singleplayer
world is loaded by Chunky. This can be disabled if needed. Alex and Steve
models are supported.

Multiple players are not handled yet, and custom player textures ("skins"),
armor, and equipped items are not rendered, but support for these features will
be added in future releases.

This version also fixes a fire rendering bug that could crash Chunky.


###ChangeLog

* Launcher v1.8.11: added --console option to show the GUI console even in
  headless mode.
* Added player entity rendering.
* Added option to disable player loading in the General tab in the
  Render Controls window.
* Fixed potential crash when rendering fire.
* Fixed potential crash when loading custom resource pack while the default
  resource pack could not be found.
* Store the current world dimension and re-open the current world in the same
  dimension next time Chunky starts.
