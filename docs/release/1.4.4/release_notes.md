Chunky 1.4.4
============

## Downloads

* [Windows installer](https://launchpad.net/chunky/1.4/1.4.4/+download/Chunky-1.4.4.exe)
* [Mac bundle](https://launchpad.net/chunky/1.4/1.4.4/+download/Chunky-1.4.4.dmg)
* [Cross-platform binaries](https://launchpad.net/chunky/1.4/1.4.4/+download/Chunky-1.4.4.zip)
* [Only launcher (win, mac, linux)](http://chunkyupdate.llbit.se/ChunkyLauncher.jar)

## Release Notes

This version adds rendering for armor stands and banners.
Player rendering has been improved with experimental armor rendering.

To support the new armor rendering, additional options have been added in the
Entities tab for changing entity equipment.  The entity pose editor has been
slightly redesigned to make it more flexible for handling different types of
entities.

Rendering of held items will be added in a later release.

This release also improves rendering of beds in Minecraft 1.12+ worlds:
colored beds are now rendered with the right textures.

Special thanks to our GitHub contributors for this release:

* leMaik
* chland - testing
* electron93 - bugfixes



## ChangeLog

* Windows installer now detects Java 9 installations.
* Added armor rendering for player entities.
* Added armor stand rendering.
* Added banner rendering.
* Added UI elements to modify entity armor in the Entities tab.
  This currently applies to players and armor stands.
* Added a drop down menu to the entity posing controls for selecting which limb
  to pose.
* Tweaked stone wall rendering to behave more like Minecraft.
* Plugins can now modify the main window tabs.
* Added banner rendering.
* Improve bed rendering for Minecraft 1.12 (colored beds).
* Y clipping is now a per-scene setting, with an upper clip value.
* The Y clip planes now cull non-player entities.
* Spruce and birch leaf colors are now fixed like in Minecraft.

