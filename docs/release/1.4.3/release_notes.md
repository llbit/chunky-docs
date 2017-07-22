Chunky 1.4.3
============

## Downloads

* [Windows installer](https://launchpad.net/chunky/1.4/1.4.3/+download/Chunky-1.4.3.exe)
* [Mac bundle](https://launchpad.net/chunky/1.4/1.4.3/+download/Chunky-1.4.3.dmg)
* [Cross-platform binaries](https://launchpad.net/chunky/1.4/1.4.3/+download/Chunky-1.4.3.zip)
* [Only launcher (win, mac, linux)](http://chunkyupdate.llbit.se/ChunkyLauncher.jar)

## Release Notes

This release adds support for Minecraft 1.12 blocks.

A new Materials tab has been added to the Render Controls dialog.
The Materials tab allows modifying emittance, specular coefficient
(reflectiveness), and index of refraction for all block types.

The reflection rendering algorithm has been changed to allow
modifying the reflectiveness of differrent block types. As a result,
water now renders slightly differently.

Fog is now blended with the sky near the horizon.

The launcher now includes a plugin manager. The plugin manager is accessed via
the advanced settings, and makes it easy to install new plugins.

Bed textures were renamed in Minecraft 1.12, and don't work well with Chunky
yet. A workaround is to use a pre-1.12 texture pack. Bed rendering will be
improved in a future release.

Thanks to our GitHub contributors!

* leMaik - Improved plugin loading, added plugin metadata.
* electron93 - Improved world chooser dialog.



## ChangeLog

* Various small UI improvements and bug fixes.
* Improved the way fences, stone walls, glass panes, and iron bars
  connect to other blocks.
* Added plugin manager in the launcher, among the advanced settings.
* The Plugin API now expects plugins to provide metadata.
* Made resource pack loading more flexible.
* Fog is now blended with the sky near the horizon.
* Minecraft block IDs are now displayed in the block info tooltip.
* Improved error handling for skymap loading.
    * Added -f option to ignore headless skymap loading errors.
* Fixed incorrect top texture for inverted daylight sensors.
* Added rendering for Minecraft 1.12 blocks:
    * Glazed Terracotta
    * Concrete
    * Concrete Powder
    * Beetroots
* Made block material properties configurable per-scene.
* Modified specular reflection rendering.
