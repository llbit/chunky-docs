Chunky 1.3.6
============

###Downloads

* [Windows installer](https://launchpad.net/chunky/1.3/1.3.6/+download/Chunky-1.3.6.exe)
* [Mac bundle](https://launchpad.net/chunky/1.3/1.3.6/+download/Chunky-1.3.6.dmg)
* [Cross-platform binaries](https://launchpad.net/chunky/1.3/1.3.6/+download/Chunky-1.3.6.zip)
* [Only launcher (win, mac, linux)](http://chunkyupdate.llbit.se/ChunkyLauncher.jar)

###Release Notes

Rendering improvements in this release include sign text rendering, mob heads,
plus many of the upcoming Minecraft 1.9 blocks.

The first HDR output mode has been added to Chunky: 32-bit floating point TIFF
can be selected under the Advanced tab in the Render Controls window.

Several small changes have been made in the user interface. Most notably the
render preview window can be scaled by a new button in the bottom left corner
of the window.

Bug fixes include fixes to headless rendering and "Water World" rendering.


###ChangeLog

* Fire textures are now loaded from resource pack.
* New scenes have emitters turned off by default.
* Cloud offset is now fixed relative to world origin.
* Added chunk count column in scene selector table.
* Added output mode selector in the advanced tab, with an option to select
  32-bit TIFF output.
* Changed the postprocess JSON variable to String.
* Added black sky mode, useful for rendering an emitter-only pass.
* Improved glass pane and iron bars rendering.
* Added rendering for the following Minecraft 1.9 block types:
    + End Rod
    + Chorus Plant, Flower
    + Purpur Block, Pillar, Slab, Stairs
    + End Stone Bricks
    + Grass Path
* Added buttons to uniformly scale the 3D canvas.
* Replaced the status text embedded in the render preview by an overlay label.
* Added mob head rendering.
* Added sign text rendering.
* Signs are now rendered slightly taller, the same size as they appear in
  Minecraft.
* Fixed error causing the sun location to reset when rendering in headless mode.
* Added chunk grid at bedrock level in preview rendering mode.
* Fixed the parallel camera sometimes clipping world chunks.
* Fixed an issue with the water world rendering mode causing the water plane to
  have an incorrect vertical offset in large scenes.
