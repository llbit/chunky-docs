Chunky 1.3.5
============

###Downloads

* [Windows installer](https://launchpad.net/chunky/1.3/1.3.5/+download/Chunky-1.3.5.exe)
* [Mac bundle](https://launchpad.net/chunky/1.3/1.3.5/+download/Chunky-1.3.5.dmg)
* [Cross-platform binaries](https://launchpad.net/chunky/1.3/1.3.5/+download/Chunky-1.3.5.zip)
* [Only launcher (win, mac, linux)](http://chunkyupdate.llbit.se/ChunkyLauncher.jar)

###Release Notes

This version adds rendering of paintings and has a reworked fog rendering
system that is simpler, more efficient, and allows customization.  Fog color
and density can now be changed in the "Sky & Fog" tab. This allows rendering
thick fog, light haze, or anything inbetween.

A camera view indicator is now drawn in the 2D map as a yellow rectangle, and
by using the right-click context menu anywhere in the 2D map it is possible to
select all visible chunks inside the camera view. This is useful for setting up
new scenes.

The UI has been improved with new icons and bug fixes.

More cool stuff:

* Single-color texture option
* Corner stairs, buttons, and mushroom block render issues fixed
* Underwater light pollution fixed


###ChangeLog

    * Added option to select visible chunks in the 2D map context menu
      (selects visible chunks inside the camera view indicator)
    * Nether portals now emit light
    * Re-engineered atmosphere and fog rendering, replaced it with a simpler
      but more customizable fog system. Fog density and color can be changed
      by the user (in the "Sky & Fog" tab).
    * Fixed stairs with fog render issue
    * Added a notification after changing the Y cutoff setting about reloading
      the chunks for the setting to take effect.
    * Added new tab icons in the Render Controls window. This fixes the issue
      with huge tabs when a high-resolution texture pack was used.
    * Improved huge mushroom rendering: mushroom blocks with some data values
      were rendered incorrectly
    * Fixed a rendering issue for corner stairs causing various configurations
      to render incorrectly
    * Fixed an error causing incorrect lighting of underwater blocks
    * Fixed button rendering (render new button orientations correctly)
    * The render reset confirmation feature now works as it should when the
      target SPP has been reached
    * Added slider for the target SPP setting
    * Added scroll bars to the render preview when the window is too small to
      fit the entire image
    * The render preview window no longer stretches the image to fit the window
    * Added "Move camera here" item in the map context menu
    * Added "follow camera" option to the Map View tab of the main window
    * Added camera field of view indicator in the 2D map
    * Added single color textures option, found under the Options tab in
      the main window
    * Added paintings rendering
    * The sky light modifier can now be set to zero by typing "0" in the
      text field next to the sky light slider
