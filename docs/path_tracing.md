Path Tracing
============

Path Tracing is a rendering algorithm similar to [ray tracing][1] in that rays
are cast from a virtual camera and traced through a virtual scene. The rays are
distributed randomly from within each source pixel and at each intersection
with an object in the scene a new reflection ray is picked at random. Each ray
eventually exits the scene or is killed of. When a ray has finished boucing
about in the scene a *sample* value is calculated from the materials the ray
bounced against. The sample value is added back to the average for the source
pixel.

The random components in path tracing cause the rendered image to appear noisy.
The noise decreases over time as more and more samples are calculated.

Samples Per Pixel (SPP)
-----------------------

The defining factor for render quality is the number of samples per pixel
(SPP).

A simple way to understand SSP is to imagine a camera in a dark room taking a
long exposure shot. In the room there is laser that shines white light. The
laser quickly switches on and off, while also rotating wildly so that each time
it is switched on it points in a random direction. Each laser light burst is
one sample, if enough of them are seen by the camera during the exposure you
will get a nicely lit photo, assuming that all samples were uniformly
distributed.

The higher SPP you have in a rendered image, the lower the noise, or
graininess, will be noticeable. However after a certain point, there will be
diminishing returns.  The difference in image quality between, for example,
20,000 SSP and 21,000 SSP will not be as noticeable as between 1,000 SSP and
2,000 SSP.

Sunlight does not require high SSP to give a nice image. Outdoor scenes can be
rendered with relatively low SPP if sunlight is enabled. Emitters (torches,
lava, glowstone, pumpkins, etc.) require a lot of SSP to reduce the noise, so
indoor scenes and similar scenes in low-light environments take a much higher
SPP number to look good.

An indoor scene rendered with increasing SPP. The white numbers show SPP:

![Outdoor scene SPP comparison](spp-compare-1.png)

![Outdoor scene SPP comparison](spp-compare-2.png)

![Outdoor scene SPP comparison](spp-compare-3.png)

[1]: http://en.wikipedia.org/wiki/Ray_tracing_(graphics)
