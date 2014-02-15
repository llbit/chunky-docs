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

* **Q: Why are mobs and paintings not rendered?**
  Chunky cannot currently render entities. These are objects that are separate from the blocks that make up the Minecraft worlds, such as players, mobs, minecarts, projectiles, etc. Future support for rendering entities is planned, but there is no deadline for this feature yet, so stay tuned!

* **Can Chunky render mod blocks?**
  No, only Vanilla blocks. It is not likely that any mod blocks will be supported as there are far too many for it to be feasible.

* **Why does the sky look so bad?**
  No, only Vanilla blocks. It is not likely that any mod blocks will be supported as there are far too many for it to be feasible.

* **Where can I find Skymaps?**
  The Skymap page has some useful links for obtaining high quality skymaps.
