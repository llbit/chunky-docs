Scene Description Format
========================

The JSON format is used to store scene configurations. The JSON files are
stored in the scene directory and the filename is based on the scene name.

For a scene named MyScene the corresponding scene description file would be
`MyScene.json`.

An average scene description file may look like this:

    {
      "sdfVersion": 2,
      "name": "flowers",
      "width": 400,
      "height": 400,
      "exposure": 1.0,
      "postprocess": 1,
      "renderTime": 81177,
      "spp": 100,
      "sppTarget": 1200,
      "pathTrace": true,
      "dumpFrequency": 50,
      "saveSnapshots": true,
      "emittersEnabled": true,
      "emitterIntensity": 13.0,
      "sunEnabled": true,
      "cloudsEnabled": false,
      "cloudHeight": 128,
      "stillWater": false,
      "clearWater": false,
      "biomeColorsEnabled": true,
      "atmosphereEnabled": false,
      "volumetricFogEnabled": false,
      "waterHeight": 0,
      "world": {
        "path": "C:\\Users\\Steve\\AppData\\Roaming\\.minecraft\\saves\\test_1_7_4",
        "dimension": 0
      },
      "camera": {
        "position": {
          "x": 442.6930821130635,
          "y": 87.1632718486006,
          "z": 49.918400631443504
        },
        "orientation": {
          "roll": 0.0,
          "pitch": -1.2276800914515056,
          "yaw": -2.358491700687768
        },
        "projectionMode": "PINHOLE",
        "fov": 52.599999999999994,
        "dof": 8.0,
        "infDof": true,
        "focalOffset": 2.0
      },
      "sun": {
        "altitude": 1.0471975511965976,
        "azimuth": 5.711986642890533,
        "intensity": 1.5,
        "color": {
          "red": 1.0,
          "green": 1.0,
          "blue": 1.0
        }
      },
      "sky": {
        "skymap": "C:\\Users\\Steve\\Desktop\\skymap.jpg",
        "skyYaw": 1.3327968833411243,
        "skyMirrored": true,
        "groundColor": {
          "red": 0.0,
          "green": 0.0,
          "blue": 1.0
        }
      },
      "chunkList": [
        [
          28,
          2
        ]
      ]
    }

Version History
---------------

* **Version 2** (Chunky 1.2.0 through 1.2.3)
* **Version 3** (Chunky 1.3-alpha1 through 1.3.3)
* **Version 4** (Chunky 1.3.4)
    * removed clearWater
    * added waterOpacity (`=float`)
    * added waterVisibility (`=float`)
    * added waterColor (`={"red"=float,"green"=float,"blue"=float}`)
    * added useCustomWaterColor (`=bool`)
* **Version 5** (Chunky 1.3.5-alpha5)
    * removed atmosphereEnabled
    * removed volumetricFogEnabled
    * added fogDensity (`=float`)
    * added fogColor (`={"red"=float,"green"=float,"blue"=float}`)
    * added fastFog (`=bool`)


