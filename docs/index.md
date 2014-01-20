Chunky
======

Chunky is a Minecraft mapping and rendering tool.

Download links for version [1.2.2](release/1.2.2/release_notes.html):

* [Windows Installer](https://launchpad.net/chunky/1.2/1.2.2/+download/Chunky-1.2.2.exe)
* [Cross-platform binaries (Mac, Win, Linux)](https://launchpad.net/chunky/1.2/1.2.2/+download/Chunky-1.2.2.zip)
* [Launcher only (Mac, Win, Linux)](http://chunkyupdate.llbit.se/ChunkyLauncher.jar)

Useful links:

* [GitHub Page](https://github.com/llbit/chunky)
* [Issue Tracker](https://github.com/llbit/chunky/issues)
* [Reddit Community](http://www.reddit.com/r/chunky)

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

