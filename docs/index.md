# Chunky

Chunky is a Minecraft mapping and rendering tool.  Check out [the gallery][15]
for examples of what Chunky can do!

## Downloads
<center>
	<a href="/download.html" class="button"> Chunky @VERSION@ <br><btnsub>Minecraft 1.12 or older</btnsub></a>
	<a href="https://chunky.lemaik.de/" class="button"> Chunky @MODERN_VERSION@ <br><btnsub>Minecraft 1.13 or newer</btnsub></a>
</center>

New users are recommended to look at the [Installation Instructions][13] and
the [Getting Started Guide][14], or for a full guide check [Your First Render!](./your_first_render.html)

For help and development updates, join our Discord:

[![Join our Discord server!](discord_icon.png)](https://discord.gg/VqcHpsF)

## Chunky for Minecraft 1.13+

Chunky 1.4.X only supports Minecraft 1.12 and earlier. For full Minecraft 1.13+ support, including Minecraft 1.16, [please see leMaik's site on Chunky @MODERN_VERSION@](https://chunky.lemaik.de/).

---

## Frequently Asked Questions

* **Q: Why is there noise/grain/random bright dots in the render?**
  This is not a bug, but an unfortunate effect of the rendering algorithm used
  in Chunky. Torches and other small light sources cause a very random
  illumination and it takes a long time to render such light nicely. For more
  information please read the [Path Tracing](/path_tracing.html) article. You can disable
  emitters under the Lighting tab in the Render Controls dialog to remove most
  of the random bright dots.  **Note that rendering for a longer time will
  eventually remove the noise**, though it may take a very long time.

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

Question still not answered? [Check the FAQ page.][8]

## License & Copyright

Chunky is free software and the source code is made available under the [GNU
General Public License, version 3][16].  The source code is managed on
[GitHub][9].

Chunky is Copyright (c) 2010-2014, Jesper &Ouml;qvist. Additional contributors
are listed in the relevant source files and [on the credits page][17].
Copyright notices for third-party libraries used in Chunky are listed in the
README file.

## Releases

[RSS feed for releases.](https://www.reddit.com/user/releasebot.rss)

[1]: /release/@VERSION@/release_notes.html
[2]: @EXE_DL_LINK@
[3]: @ZIP_DL_LINK@
[4]: http://chunkyupdate.llbit.se/ChunkyLauncher.jar
[5]: https://github.com/llbit/chunky
[6]: https://github.com/llbit/chunky/issues
[7]: http://www.reddit.com/r/chunky
[8]: /faq.html
[9]: https://github.com/llbit/chunky
[13]: /install.html
[14]: /getting_started.html
[15]: /gallery.html
[16]: http://opensource.org/licenses/gpl-3.0.html
[17]: /credits.html
