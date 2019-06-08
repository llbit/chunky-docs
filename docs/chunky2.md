# Chunky 2.0

Chunky 2.0 is being developed to support Minecraft 1.13 and beyond. With Chunky
2.0, the whole block handling system is redesigned to handle the new world
format used by Minecraft 1.13+. Chunky 2.0 does not load pre-1.13 worlds or
scenes created with Chunky 1.4.X.

Chunky 2.0 is still being tested and improved and each beta update may break
existing functionality.

To get the latest beta release of Chunky 2.0, follow these steps:

1. Download the Chunky Launcher (v1.11.1 or later).
2. Open the launcher (requires Java 8 installed, does not work with Java 9+).
3. In the launcher, under "Advanced", set the "Update Site" option to: `http://chunkyupdate2.llbit.se/`
4. Click "Check for update" and download the latest Chunky 2.0 release.

![Chunky 2.0 preview](chunky2preview.png)

## Change Log

* New single-window interface using a new dark theme.
* Custom themes can be added by adding a stylesheet in the settings directory.
* Added support for block palettes in Minecraft 1.13.
* A large part of Chunky internals were redesigned (including plugin API).


## Known Bugs

* Rendering speed is lower overall and in particular with water.
* Pre-1.13 chunks are not loaded (shown with an error icon in the 2D map).
* Minecraft 1.13 worlds can contain pre-1.13 chunks and need to be converted
  for Chunky 2.0 to load them.
* Biome colors do not affect water color in Chunky. Set a custom water color
  under the Water settings tab.
* Material properties do not work right now.

