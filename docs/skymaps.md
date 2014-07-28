##Sky Maps

You can change the skymap under the "Sky" tab of the Render Controls dialog.
You can also change the sun position relative to the skymap.

Chunky currently only accepts skymaps using equirectangular projection with 90
degree vertical field of view (clamped at horizon).

It is recommended to use a large skymap in order to avoid the sky looking
blurry.  However, if the skymap is too large it will take a long time to load.

Vertical Resolution
-------------------

With a 90&deg; vertical resolution, the skymap will only cover the sky above
the horizon. The skymap is mirrored at the horizon. If the skymap has 180&deg;
vertical resolution the mirroring is not needed, the skymap will cover both sky
and ground.

![Skymap vertical resolution](skymap_vertical_resolution.png)

Where to find skymaps
---------------------

These pages provide links to other pages, or downloads of non-HDR skymaps:

* [http://www.wuala.com/Olson/Photos/Optikz_360_Skies/][1]
* [http://www.reddit.com/r/chunky/comments/17ts4b/some_more_skymaps/][3]

HDR Skymaps
-----------

HDR skymaps have the advantage that they can be used to provide most
of the light for a scene. HDR skymap support is coming to Chunky shortly.
If HDR is not required, it is possible to convert them to regular JPEG
images.

Most of sites provide paid-for skymaps, but most of them have a few free
samples available:

* [CGSkies][2]
* [openfootage.net][4]
* [HDRMill][5]
* [nordicFX][6]
* [HDRI-Hub.com][7]
* [sIBL Archive][8]
* [hdrmaps.com][8]

You can also try searcing Google for [Panoramic Sky Texture][0]

[0]: https://www.google.com/search?q=panoramic+sky+texture
[1]: http://www.wuala.com/Olson/Photos/Optikz_360_Skies/
[2]: http://www.cgskies.com/skies.php
[3]: http://www.reddit.com/r/chunky/comments/17ts4b/some_more_skymaps/
[4]: http://www.openfootage.net/?cat=15
[5]: http://www.hdrmill.com/Freebies.htm
[6]: http://www.nordicfx.net/?works=hdri
[7]: http://www.hdri-hub.com/free-samples
[8]: http://www.hdrlabs.com/sibl/archive.html
[9]: http://hdrmaps.com/freebies
