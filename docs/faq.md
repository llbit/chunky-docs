Frequently Asked Questions
==========================

Post any questions un-answered here to the [reddit community][0].
Please post bugs on the [chunky GitHub page.][1]

* **Q: Why is there noise/grain/random bright dots in the render?**
  This is not a bug, but an unfortunate effect of the rendering algorithm used
  in Chunky. Torches and other small light sources cause a very random
  illumination and it takes a long time to render such light nicely. For more
  information please read the [Path Tracing](/path_tracing.html) article. You can disable
  emitters under the Lighting tab in the Render Controls dialog to remove most
  of the random bright dots.  **Note that rendering for a longer time will
  eventually remove the noise**, though it may take a very long time.
  
	Note - There are techniques and plugins which can help reduce noise. For more information please visit [jackjt8's Guide to Chunky - Denoising][5].

* **Q: How long does it take to render an image?**
  There is no exact answer to this question. The main thing that affects render
  time is your CPU, the size of the image, and the lighting conditions in the
  scene you are rendering. It can take anywhere from an hour to a couple of
  days to render a nice image. You can reduce the size of the canvas or disable
  emitters to speed up the convergence rate. See the [Path Tracing](/path_tracing.html) article for
  more details.

* **Q: Is GPU rendering supported?**
  GPU support is not actively being worked on right now. GPU rendering *may* be
  added in the future, and some partial progress has been made toward this goal
  but there are very many hurdles before it is fully supported.

* **Q: Why are mobs not rendered?**
  Chunky cannot currently render entities, with the exception of paintings. Entities are objects that are separate from the blocks that make up the Minecraft worlds, such as players, mobs, minecarts, projectiles, etc. Future support for rendering entities is planned, but there is no deadline for this feature yet, so stay tuned!

* **Q: Can Chunky render mod blocks?**
  No, only Vanilla blocks. It is not likely that any mod blocks will be supported as there are far too many for it to be feasible. Check out [this page][4] to read more about which blocks Chunky can render.

* **Q: Why does the sky look bad?**
  You might have a low resolution skymap, or it may be the wrong format.

* **Q: Where can I find Skymaps?**
  The [Skymap][3] page has some useful links for obtaining high quality skymaps.


[0]:http://www.reddit.com/r/chunky
[1]:https://github.com/llbit/chunky/issues
[3]:/skymaps.html
[4]:minecraft_compatibility.html
[5]: https://jackjt8.github.io/ChunkyGuide/docs/advanced_techniques/denoising.html
