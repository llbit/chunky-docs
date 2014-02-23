##Render Controls -- Advanced  

[General][0] | [Lighting][1] | [Sky][2] | [Camera][3] | [Post-Processing][4] | **Advanced** | [Global][6]  

[0]:render_controls_general.html
[1]:render_controls_lighting.html
[2]:render_controls_sky.html
[3]:render_controls_camera.html
[4]:render_controls_post-processing.html
[5]:render_controls_advanced.html
[6]:render_controls_global.html

![(win) render controls advanced panel](render_controls_advanced.png)  
 
----  

**Render Threads**
:   Specifies the amount of processing threads utilized for rendering. This can be helpful if you would like to do other tasks while rendering in the background. Chunky automagically detects and sets the maximum render threads available. Going any higher will have no effect in the overall "speed" of the render.  

**CPU Load**
:   Sets the capacity in percentage, of how much processing thread is utilized.  

----  

**Ray Depth**
:   Controls how many times the rays can "jump". While higher settings will result in more realistic lightning the realism gain from increased number of jumps will be diminishing. Higher values will also increase the render times drastically. 

----  

**Water World Mode**
:   Toggles water world mode. Chunks must be reloaded in order for this setting to take effect.
This will fill unloaded chunks with water up to the set height in the render.  

----  

**Merge Render Dump**
:   Combines saved render dumps into one, allows for manual distributed rendering.