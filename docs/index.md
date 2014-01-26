Chunky
======

Chunky is a Minecraft mapping and rendering tool.

Download links for version [@VERSION@](release/@VERSION@/release_notes.html):

* [Windows Installer](@EXE_DL_LINK@)
* [Cross-platform binaries (Mac, Win, Linux)](@ZIP_DL_LINK@)
* [Launcher only (Mac, Win, Linux)](http://chunkyupdate.llbit.se/ChunkyLauncher.jar)

If you are new to Chunky you may want to look at the [Getting Started
Guide!](getting_started.html)

Useful links:

* [GitHub Page](https://github.com/llbit/chunky)
* [Issue Tracker](https://github.com/llbit/chunky/issues)
* [Reddit Community](http://www.reddit.com/r/chunky)

License & Copyright
-------------------

Chunky is free software and the source code is made available under the [Gnu
General Public License, version 3](http://opensource.org/licenses/gpl-3.0.html).
The source code is managed on [GitHub](https://github.com/llbit/chunky).

Chunky is Copyright (c) 2010-2014, Jesper Öqvist. Additional contributors are
listed in the relevant source files and in the credits. Copyright notices for
third-party libraries used in Chunky are listed in the README file.

Frequently Asked Questions
--------------------------

* **Q: Why do I get random dots in the render?**
  Torches and other small light sources cause a very random illumination and it
  t takes many samples per pixel to render such light smoothly. For more
  information see the [Path Tracing](pathtracing.html) article! You can disable
  emitters under the Lighting tab in the Render Controls dialog to remove the
  random bright dots. Note that rendering for a longer time will eventually
  remove the dots as the render approaches the expected value.

* **Q: How long does it take to render an image?**
  There is no exact answer to this question. The main thing that affects render
  time is your CPU, the size of the image, and the lighting conditions in the
  scene you are rendering. It can take anywhere from an hour to a couple of
  days to render a nice image. You can reduce the size of the canvas or disable
  emitters to speed up the convergence rate. See the Path Tracing article for
  more details.

* **Q: Is GPU rendering supported?**
  Not currently, but in the distant future Chunky may be able to render using
  GPUs that support OpenCL.

Pages:

* [Headless Rendering](headless.html)
* [Scene Description Format](scene_format.html)

