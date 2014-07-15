Chunky
======

Chunky is a Minecraft mapping and rendering tool.  Check out [the gallery][15]
to see what it is possible with Chunky!

Download links for [version @VERSION@][1]:

* [Windows Installer][2]
* [Cross-platform binaries (Mac, Win, Linux)][3]
* [Launcher only (Mac, Win, Linux)][4]

If you are new to Chunky you may want to look at the [Installation
Instructions][13] and the [Getting Started Guide][14].  

Frequently Asked Questions
--------------------------

* **Q: Why do I get random dots in the render?**
  Torches and other small light sources cause a very random illumination and it
  t takes many samples per pixel to render such light smoothly. For more
  information see the [Path Tracing][10] article! You can disable emitters
  under the Lighting tab in the Render Controls dialog to remove the random
  bright dots. Note that rendering for a longer time will eventually remove the
  dots as the render approaches the expected value.

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

Question still not answered? [Check the FAQ page.][8]

License & Copyright
-------------------

Chunky is free software and the source code is made available under the [GNU
General Public License, version 3][16].  The source code is managed on
[GitHub][9].

Chunky is Copyright (c) 2010-2014, Jesper &Ouml;qvist. Additional contributors
are listed in the relevant source files and [on the credits page][17].
Copyright notices for third-party libraries used in Chunky are listed in the
README file.

[1]: release/@VERSION@/release_notes.html
[2]: @EXE_DL_LINK@
[3]: @ZIP_DL_LINK@
[4]: http://chunkyupdate.llbit.se/ChunkyLauncher.jar
[5]: https://github.com/llbit/chunky
[6]: https://github.com/llbit/chunky/issues
[7]: http://www.reddit.com/r/chunky
[8]: faqs.html
[9]: https://github.com/llbit/chunky
[10]: path_tracing.html
[13]: install.html
[14]: getting_started.html
[15]: gallery.html
[16]: http://opensource.org/licenses/gpl-3.0.html
[17]: credits.html
