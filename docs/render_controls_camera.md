##Render Controls -- Camera
 
[General][0] | [Lighting][1] | [Sky][2] | **Camera** | [Post-Processing][4] | [Advanced][5] | [Global][6]  

[0]:render_controls_general.html
[1]:render_controls_lighting.html
[2]:render_controls_sky.html
[3]:render_controls_camera.html
[4]:render_controls_post-processing.html
[5]:render_controls_advanced.html
[6]:render_controls_global.html

![(win) render controls camera panel](render_controls_camera.png)  
 
----  

**Position**
:   Defines the X, Y, Z, coordinates of the Camera. These coordinates correlate with the Minecraft world positions.  

**Direction**
:   The first 2 input fields define the directional constraint of the camera. The Last input field defines the rotation of the camera.  

**Camera to Player**
:   Sets the position and facing of the camera to be the same as that of the player.  

**Center Camera**
:   Moves the camera to the centre of the loaded world and faces the camera to the ground.  

----  

**Skybox Views**
:   Rotates the camera to face towards the selected direction.  

**Isometric Views**
:   Moves the camera to any of the traditional isometric views and changes the projection mode to Parallel.  

**Projection**
:   Changes the path projection method to any of the possible projection modes: Parallel, Pinhole, Fisheye, Panoramic (equirectangular) and Panoramic (slot).  

* *Pinhole* is default and makes Chunky work like a normal camera.  
* *Parallel* removes all perspective, all blocks are the same size, regardless of distance to the camera.  
* *Fisheye* makes Chunky work like a camera with extreme wide angle lens, and distorts the image.  
* *Panoramic (equirectangular)* allows for wide angles, all angles are rendered as though the camera points in all directions at once, so there's less distortion than a wide angle in Pinhole mode.  
* *Panoramic (slot)* ...

**Field of View (zoom)**
:   Controls the field of view in the virtual camera. Lower causes a narrower field of view (higher magnification) and high value will result in a wider field of view (low magnification).  70 is the default value, which corresponds with Minecraft's normal field of view.

**Depth of Field**
:   The depth of field controls the level of blurriness of objects in the scene which are not in focus. A low value will result in lots of blur while a low value will leave the whole image looking fairly sharp. Setting this value to infinite will completely remove the depth of field making the whole image perfectly sharp, this is also the default setting.
A good article explaining how this works can be found on [Wikipedia][10].  


**Focal Offset**
:   Focal offset decides how far the focal plane is from the camera. If you want to focus an object that is 20 blocks away the focal plane should be set to 20. Estimating the distance (in blocks) to a given object is a good way to make an initial guess for the correct focal offset setting. Or by using the "Autofocus" button below. Objects at this range will appear perfectly sharp even if DOF is set to a low value.  

**Autofocus**
:   Sets the Focal Offset and Depth of Field to the point in the middle of the [Render Preview][11], under the crosshair.


[10]:http://en.wikipedia.org/wiki/Depth_of_field
[11]:render_preview.html
