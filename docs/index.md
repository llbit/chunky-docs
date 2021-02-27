# Chunky

Chunky is a Minecraft rendering tool that uses Path Tracing to create realistic images of your Minecraft worlds.  Check out [the gallery][15]
for examples of what Chunky can do!

## Downloads
<center>
	<a href="/release/@VERSION@/release_notes.html" class="button"> Chunky @VERSION@ <br><btnsub>Minecraft 1.12 or older</btnsub></a>
	<a href="/download.html" class="button"> Chunky @MODERN_VERSION@ <br><btnsub>Minecraft 1.13 or newer</btnsub></a>
</center>

New users are recommended to look at the [Installation Instructions][13] and
the [Getting Started Guide][14], or for a full guide check [Your First Render!](./your_first_render.html)

For help and development updates, join our Discord:

[![Join our Discord server!](discord_icon.png)](https://discord.gg/VqcHpsF)

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
  
	Note - There are techniques and plugins which can help reduce noise. For more information please visit [jackjt8's Guide to Chunky - Denoising][5].

* **Q: How long does it take to render an image?**
  There is no exact answer to this question. The main thing that affects render
  time is your CPU, the size of the image, and the lighting conditions in the
  scene you are rendering. It can take anywhere from an hour to a couple of
  days to render a nice image. You can reduce the size of the canvas, disable
  emitters, enable ESS, or use a denoising technique to speed up the convergence rate. See the [Path Tracing](/path_tracing.html) article or [jackjt8's Guide to Chunky - Denoising][5] for more details.

* **Q: Is GPU rendering supported?**
  GPU rendering support for Chunky 2.4.0-77 or later is currently in development in the form of an OpenCL 1.2 renderer plugin. This renderer is still under development and many features of the CPU renderer are not yet supported. For more information and WIP builds please visit [the plugins GitHub][6].
  
* **Q: What about the SpigotMC Plugin?**
  [Chunky (SpigotMC)](https://www.spigotmc.org/resources/chunky.81534/) is an unrelated project which has an unfortunate name collision. Said plugin is used to quickly pre-generate server chunks.

Question still not answered? [Check the FAQ page.][8]

## License & Copyright

Chunky is free software and the source code is made available under the [GNU
General Public License, version 3][16].  The source code is managed on
[GitHub][9].

Chunky is Copyright (c) 2010-2021, Jesper &Ouml;qvist and [Chunky Contributors][18];
these are also listed in the relevant source files and on the [Credits][17] page.
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
[18]: https://github.com/chunky-dev/chunky/graphs/contributors
