##Render Controls -- Sky  
 
[General][0] | [Lighting][1] | **Sky** | [Camera][3] | [Post-Processing][4] | [Advanced][5] | [Global][6]  

[0]:render_controls_general.html
[1]:render_controls_lighting.html
[2]:render_controls_sky.html
[3]:render_controls_camera.html
[4]:render_controls_post-processing.html
[5]:render_controls_advanced.html
[6]:render_controls_global.html

![(win) render controls sky panel](render_controls_sky.png)  
 
----  

**Load Skymap**
:   Brings up a dialogue which can be used to browse for and then load a skymap.  

**Unload Skymap**
:   Unloads the skymap currently loaded in favour of the default sky.  

**Skymap Rotation**
:   Rotates the skymap on a Horizontal plane.

**Mirror sky at horizon**
:   Toggles whether or not the skymap is mirrored on the horizon. By default this option is toggled on.  

**Change Ground Color**
:   Changed the color of the ground beyond and below the Minecraft world. This setting will not have any effect if 'Mirror sky at horizon' and/or 'Water World Mode' is enabled.  

----  

**Enable Atmosphere**
:   Toggles the display a very weak depth fog effect resembling the atmosphere.  

**Enable Volumic Fog**
:   Toggles the display of a thick fog which can only be seen where direct sunlight is passing through it. The thickness of the fog is related to the amount of direct sunlight that has passed through it. The effect can only be seen against objects in the world, light paths that lead to the sky will completely ignore this fog, regardless of whether sunlight has passed through it or not. This option can advantageously be used to simulate the rays of sun falling through the window of a dusty library or the sun rays entering a misty cavern.  

**Enable Clouds**
:   Toggles Minecraft style, blocky clouds. Currently only renders as flat planes, similar to clouds seen in Minecraft's fast graphics mode.  

**Cloud Height**
:   Controls the level at which Chunky will place the clouds to render. Default value is 128.  