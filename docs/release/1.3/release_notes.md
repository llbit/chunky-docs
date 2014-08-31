Chunky 1.3
============

###Downloads

* [Windows installer](https://launchpad.net/chunky/1.3/1.3/+download/Chunky-1.3.exe)
* [Cross-platform binaries](https://launchpad.net/chunky/1.3/1.3/+download/Chunky-1.3.zip)
* [Only launcher (win, mac, linux)](http://chunkyupdate.llbit.se/ChunkyLauncher.jar)

###Release Notes

This release features a big overhaul of the sky rendering in Chunky. New sky
rendering modes have been added, with lots of new features such as support for
HDRI sky maps and 3D clouds.

The release also includes several bug fixes and user interface improvements.
Some known issues with saving and loading scenes in the previous version have
been fixed.


###ChangeLog

    * Attempted to make PNG writing more efficient by splitting PNGs into
      1 MiB chunks.
    * Removed the "render lock/auto lock" features. These are replaced
      by a render reset confirmation dialog which appears if anything that
      would reset the render has been changed after rendering for at least
      thirty seconds.
    * Added Red Sandstone blocks, slabs, and stairs (from Minecraft snapshots)
    * Fixed a problem causing render progress to reset after loading a scene
    * Clouds can now be moved in all directions
    * HDRI sky textures can now be used, supported formats are:
        + RGBE (.hdr)
        + PFM
    * Added new sky rendering modes:
        + gradient
	+ spherical skymap
	+ skybox
    * Added sky light parameter, affecting indirect sky lighting contribution
    * The simulated sky has been modified (less pink, more bright)
    * Enable "Clear Selection" button after selecting region
    * Fixed regular glass blocks not letting light pass through (since 1.2.0).
      This could also affect other transparent blocks where the transparent
      texels had dark RGB values.
