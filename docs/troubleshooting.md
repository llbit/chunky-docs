Troubleshooting Chunky
======================

This page lists some common issues and how to fix them.

## Chunky does not launch anymore (Windows)

If you installed Chunky using the Windows installer and later updated the Java installation,
Chunky may stop working because the path to the Java-installation has changed. This can
usually be fixed by uninstalling Chunky and reinstalling it again.

## I see a lot of black blocks with a red X

The black box with a red cross over it is the texture used in place of missing textures.

This happens when Chunky could not find a Minecraft installation to load textures from.

Chunky needs to load textures from a Minecraft installation or a resource pack,
otherwise it uses its own built-in textures or the missing texutre.

The problem can be fixed by either:

* Updating the path to your Minecraft installation in the Chunky launcher.
* Loading a resource pack that contains the missing textures.

## I try to create a new scene but it is empty

First, make sure that you have selected some chunks before creating a new scene.

If you still have the problem it may be caused by the "Y cutoff" setting.
The "Y cutoff" setting in the Render Controls window can prevent the blocks from being loaded,
especially if you are loading a superflat world. All blocks that have a Y value (height) less
than the Y cutoff value will not be loaded.

The problem can be fixed by setting the "Y cutoff" value to 0 in the Render Controls window
and then reloading the chunks, or creating a new scene.

[Typical GitHub issue with a similar problem.](https://github.com/llbit/chunky/issues/380)

