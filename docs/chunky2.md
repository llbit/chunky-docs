# Chunky 2

Chunky 2 is being developed to support Minecraft 1.13 and beyond. With Chunky
2, the whole block handling system is redesigned to handle the new world
format used by Minecraft 1.13+. Chunky 2 does not load pre-1.13 worlds or
scenes created with Chunky 1.4.X.

To get the latest release please follow the button/link below.

<center>
	<a href="https://chunky.lemaik.de/" class="button"> Chunky @MODERN_VERSION@ <br><btnsub>Minecraft 1.13 or newer</btnsub></a>
</center>
![Chunky 2 preview](chunky2preview.png)

## Features

* New single-window interface using a new dark theme.
* Custom themes can be added by adding a stylesheet in the settings directory.
* Support for Minecraft 1.13, 1.14, 1.15, and 1.16 ([see a list of supported blocks here](https://chunky.lemaik.de/supported-blocks)).
* A large part of Chunky internals were redesigned (including plugin API).
* Numerous other improvements


## Known Bugs

* Rendering speed is lower overall and in particular with water.
* Pre-1.13 chunks are not loaded (shown with an error icon in the 2D map).
* Minecraft 1.13 worlds can contain pre-1.13 chunks and need to be converted
  for Chunky 2 to load them.
	NOTE - Worlds made with Spigot, or similar, may not convert automatically and would require manual exploration to function correctly.
