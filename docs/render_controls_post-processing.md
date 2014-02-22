##Render Controls -- Post-Processing  

[General][0] | [Lighting][1] | [Sky][2] | [Camera][3] | **Post-Processing** | [Advanced][5] | [Global][6]  

[0]:render_controls/general.html
[1]:render_controls/lighting.html
[2]:render_controls/sky.html
[3]:render_controls/camera.html
[4]:render_controls/post-processing.html
[5]:render_controls/advanced.html
[6]:render_controls/global.html

![(win) render controls post-processing panel](render_controls_post-processing.png)  
 
----  

**Exposure**
:   Adjusts the brightness of the image. A value lower than one will make the image darker than normal, and a value greater than one will make it brighter. 

**Post-Processing Mode**
:   Selects a tone mapping operator to use in post-processing.
Currently there are three choices here, but these will likely change in the future:  

* __None__ - disables gamma correction  
* __Gamma correction__ - only perform gamma correction  
* __Tonemap op1__ - the fifth tonemapping operator [listed on this page][10]

The post-processing mode does not update the preview image automatically - you have to resume rendering for it to update.  [This should be fixed in a future version.][11]

[10]:http://filmicgames.com/archives/75
[11]:https://github.com/llbit/chunky/issues/116