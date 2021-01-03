Chunky 2.3.0
============

## Downloads

* [Chunky Launcher v1.12.0 (win, mac, linux)](https://chunkyupdate.lemaik.de/ChunkyLauncher.jar)

## Release Notes

Add emitter sampling for faster convergence and less emitter noise.

Add support for player head blocks with custom skins.

Render the books on lecterns and enchanting tables and make them poseable in the entities panel.

Fix jello water caused by interaction between water plane and normal water.

Add biome-based water color.

Performance and memory usage improvements.


## ChangeLog

### New Features
* Add emitter sampling for faster convergence and less emitter noise
* Add support for player head blocks with custom skins
* Render the books on lecterns
* Render the books on enchanting tables and allow posing them
* Add new 1.16 jigsaw block orientations
* Add a new big packed octree for very large scenes and a selector for the octree implementation; plugins can now add custom octrees
* Add rule of thirds guides
* Add support for exporting rendered images in PFM format

### Improvements
* Allow changing the output format in the Save current frame dialog
* Improve alpha computation performance
* Make fog work underwater
* Make the fog slider logarithmic
* Update the chain model for 1.16.2-pre1
* Refactor chunk textures and water normal map to reduce memory usage
* Improve octree optimization and scene loading
* Add a selector for the octree implementation
* Show a confirm dialog when trying to overwrite an existing scene
* Save scenes in per-scene directories (old scenes can still be loaded)
* Update biome names and grass/foliage colors
* Improve biome colors in the 2d map
* Optimize the octree size
* Reduce memory usage of textures (especially when using high-resolution resourcepacks)

### Bug Fixes
* Fix rendering deadlock caused by cloud intersections
* Fix jello water caused by interaction between water plane and normal water
* Fix water block below vines
* Fix player helmet rotation
* Fix selection rectangle alignment in the 2d map view
* Fix Chunky not exiting in headless mode
* Fix scene zip export
* Fix camera tab not updating when moving the camera in the 2d map view
* Fix loading of (partially) corrupted chunks, should
* Fix loading spigot/papercraft worlds
* Fix tall flowers in the materials tab
* Fix position of skulls attached to walls
* Fix missing texture for turtle helmet
* Fix hat and helmet sizes not matching the ingame sizes
* Fix some headless mode options not working
* Fix campfire rendering bug (flame clipping)
* Fix render not being reset when the ray depth is changed
* Disable the load chunks button if no world is loaded
* Fix not being able to load some 1.16 chunks
* Fix spruce and birch leaves and lily pads color
* Fix wrong render time when rendering a scene that was rendered before but that doesn't have the dump anymore
