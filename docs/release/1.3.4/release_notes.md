Chunky 1.3.4
============

###Downloads

* [Windows installer](https://launchpad.net/chunky/1.3/1.3.4/+download/Chunky-1.3.4.exe)
* [Cross-platform binaries](https://launchpad.net/chunky/1.3/1.3.4/+download/Chunky-1.3.4.zip)
* [Only launcher (win, mac, linux)](http://chunkyupdate.llbit.se/ChunkyLauncher.jar)

###Release Notes

This release improves water rendering. Many ugly water related bugs have been
fixed, and the performance has been significantly improved (for scenes with
much water the rendering speed may have increased by more than a factor 4).

There is a new tab in the Render Controls dialog that groups together all water
settings. The new water tab has settings water opacity, visibility, and color.
The default water settings can replaced with your own configuration.


###ChangeLog

    * Added Y cutoff setting (blocks below the Y cutoff are not loaded)
    * Added new tab in the Render Controls dialog for water related settings
    * Added slider for water visibility
    * Added slider for water opacity
    * Removed the "clear water" option (which is made obsolete by water
      visibility slider)
    * Added custom water color setting
    * All water settings can now be stored as custom defaults
    * Removed the visible sea border in water world rendering mode
    * Lily pads now cast shadows
    * Display a warning when a scene from a newer version of Chunky is loaded
    * Saving a scene with a different name no longer hides the old scene by
      renaming the old scene description file with the .backup suffix
    * Added scrollbar to Render Controls dialog for small screens (only visible
      when the whole window does not fit on screen)
