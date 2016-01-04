Scene Description Format
========================

Most of the settings in a Chunky scene are stored in a JSON plain-text format.
Such Scene Description files have the extesion `.json`. This page documents the
structure fields that exist in the Scene Description files and what they mean.
This page may be out of date with the current version of Chunky as it is not
updated very frequently. Check the version history at the end of this page to
see the latest updates made to this documentation.

The JSON files are stored in the scene directory and the filename is based on
the scene name. For example, the JSON file for a scene named `MyScene` would be
`MyScene.json`.

##Structure

[Click here](/example_scene.html) to view an example scene description file.

The JSON file contains one JSON object with these named elements:

Key        | Value range  | Default value | Description
-----------|--------------|---------------|------------
sdfVersion | Integer      | 6 | Scene Description Format (SDF) version
name       | String       | | Scene name
width      | Integer      | 400 | Canvas width
height     | Integer      | 400 | Canvas height
exposure   | Number       | 1.0 | Camera exposure
postprocess | `{"NONE", "GAMMA", "TONEMAP1"}` | `"GAMMA"` | Tonemapping operator
outputMode | `{"PNG", "TIFF_32"}` | "PNG" | Image output mode
renderTime | Number       | | Current cumulative rendering time
spp        | Integer      | | Current samples per pixel (SPP)
sppTarget  | Integer      | 1000 | Render SPP target
rayDepth   | Integer      | 5 | Ray recursion depth
pathTrace  | Boolean      | false |  Rendering mode (true = path tracing, false = preview)
dumpFrequency | Integer   | 500 | How often the current render state is saved (samples per state save)
saveSnapshots | Boolean   | false | Whether a snapshot image is saved for each render dump
emittersEnabled | Boolean | false |
emitterIntensity | Number | 13.0 |
sunEnabled | Boolean      | true |
stillWater | Boolean      | false |
waterOpacity | Number (0-1) | 0.42 |
waterVisibility | Number  | 9.0 |
useCustomWaterColor | Boolean  | false |
fogColor   | RGB Object   | | See below
fastFog    | Boolean      | |
biomeColorsEnabled | Boolean | true | Color grass and trees differently per biome
transparentSky | Boolean | false | Renders the sky transparent in the output image so a custom sky background can be easily used
fogDensity | Number       | 0.0 |  Zero fog density disables fog
waterHeight | Number      | 0 | Zero water height disables water world mode, non-zero height enables water world mode
world      | World Object | | See below
camera     | Camera Object | | See below
sun        | Sun Object | | See below
sky        | Sky Object | | See below
cameraPresets | Camera Preset Object | | See below
chunkList  | Array of integer arrays | | Chunks in the scene
entities   | Array of Entity Objects | | Entities in the scene

###RGB Object

Key   | Value range
------|------------
red   | Number (0-1)
green | Number (0-1)
blue  | Number (0-1)

###XYZ Object

Key   | Value range
------|------------
x     | Number
y     | Number
z     | Number

###Direction Object

Key   | Value range
------|------------
roll  | Number
pitch | Number
yaw   | Number

###World Object

Key       | Value range
----------|------------
path      | String
dimension | Integer (0-2)

###Camera Object

Key        | Value range  | Default value | Description
-----------|--------------|---------------|------------
position  | XYZ Object | |
orientation | Direction Object | |
projectionMode | `{}` | "PINHOLE" | Camera projection mode
fov | Number | 70.0 | Field of view
dof | Number | "Infinity" | Depth of field
focalOffset | Number | | Distance to target

Scripting
---------

A simple way to process scene files is by using a scripting language like
Python. For example, here is a Python script that generates individual scenes
for each chunk in a square grid of chunks. The script uses an original scene as
template for the new scenes.

    import json
    import os.path

    original_scene = 'D:\Users\Jesper\.chunky\scenes\shore-sun.json'
    scene_dir = os.path.abspath(os.path.join(original_scene, os.pardir))

    with open(original_scene, 'r') as f:
    	scene = json.load(f)

    for x in range(-10, 1):
    	for z in range(110, 119):
    		scene_name = 'chunk_%dx_%dz' % (x, z)
    		scene['name'] = scene_name
    		scene['chunkList'] = [ [ x, z ] ]
    		scene['spp'] = 0
    		scene['renderTime'] = 0
    		new_scene = os.path.join(scene_dir, scene_name + '.json')
    		print('Writing scene file %s' % new_scene)
    		with open(new_scene, 'w') as f:
    			json.dump(scene, f)


Version History
---------------

* **Version 2** (Chunky 1.2.0 to 1.2.3)
* **Version 3** (Chunky 1.3-alpha1 to 1.3.3)
* **Version 4** (Chunky 1.3.4)
    * removed clearWater (Boolean)
    * added waterOpacity (Number)
    * added waterVisibility (Number)
    * added waterColor (RGB Object)
    * added useCustomWaterColor (Boolean)
* **Version 5** (Chunky 1.3.5-alpha5)
    * removed atmosphereEnabled (Boolean)
    * removed volumetricFogEnabled (Boolean)
    * added fogDensity (Number)
    * added fogColor (RGB Object)
    * added fastFog (Boolean)
* **Version 6** (Chunky 1.3.5-alpha5)
    * Changed postprocess from Integer to Enum
    * Added outputMode (Enum)

