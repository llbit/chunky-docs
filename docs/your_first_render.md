Your first render from start to finish!
===
> This guide will be written from openSUSE, but everything should work just fine with Windows, macOS or your linux distro of choice :)
___

## Download

First, download Chunky [here](http://chunky.llbit.se/download.html).

- Windows: Download and run the Windows installer
- Linux: Download the cross platform binary, extract it to a folder of your choice
- macOS: Download and install using the Mac Bundle

Windows / macOS: Once it has installed / been extracted, run the launcher.

Linux: Open the extracted folder, right click anywhere in the file browser window and open your favourite terminal emulator.

Run: ```
java -jar chunky-1.4.5.jar```, making sure to replace 1.4.5 with the correct version number.

Or for later versions of Chunky: ```java -jar chunkylauncher.jar```

___
## Install and Launch

When running for the first time, you will be prompted where to install.

Use the reccomended directory:
- AppData on Windows
- /home/ on Linux

![Launcher](https://i.imgur.com/dCtQUKI.png)

In the launcher, you shouldn't need to change any settings, unless your `.minecraft` folder is installed in a place other then where Chunky thinks it is.
Allocate more RAM if your PC can handle it, but if it fails to start, try allocating less. 1024mb should be more then enough for most things.

Click launch.
___

## Getting camera position
> This is the simplest way to get your camera in the correct position, feel free to skip this part if you are more confident!



Now that Chunky is set up, you can close it for now.
Open the Minecraft world you want to render inside of Minecraft, and move your player to wherever you want your camera to be in the render. Face the direction too!
Hit F3:

![f3 screen](https://i.imgur.com/zKH4wp7.gif)

Take note of the fields highlighted in red!
You will need them to get your camera in the correct place inside of Chunky.

Close your game.
___
## Selecting Chunks
If you aren't already inside of Chunky, go ahead and launch it again. You should see something like this:

![Chunky Open](https://i.imgur.com/KmqSsck.png)

Hit 'Change World' and select the Minecraft world you want to render.

![Chunky Chunks](https://i.imgur.com/RqaVU7R.png)

Select the correct dimension using the buttons on the right, then select the chunks you want to be loaded in the render.

- Left click a chunk to select / unselect the chunk
- Shift click + drag to select a rectangular area
- Crtl Shift click + drag to unselect a rectangular area
- Click and drag to pan around the world
- Zoom in and out using the scroll wheel

> Selecting less chunks can decrease rendering time, but they will be completely missing from the render. Try and only select what the camera can see!

___
## Setting up your render:
> This is the part where you can customise settings to your heart's content! I will only be going through basic settings, but feel free to customise and experiment however you want!

Click the '3D Render' tab, then click 'New scene'.

![Render Settings](https://i.imgur.com/sYUCI3Z.png)
You will be greeted by a menu that looks like this and a preview pane.
Set the canvas size to whatever you want, but be aware that a larger canvas size will significantly increase render times!
For the purpose of this guide, I will use 960x540.
___

Set the Save Dump every x frames to a whatever you want. Set it to a lower number to dump more often. 
> If you think your PC / Chunky may crash during the render, set this to a lower number x)

Turn on Save Snapshot for each dump as well if you also want to save the current state of the canvas with each dump.

> The above settings shouldn't affect perfomance.

Feel free to load players and biome colours, but be aware that this may increase render times slightly.

Next, hit the Camera tab.
![Camera Position](https://i.imgur.com/dCCwFgX.png)
Click the Position and Orientation dropdown.
Enter in the X Y Z you took note of earlier in the respective fields.
Enter the two Direction Facing numbers you took note of earlier in the second row of the dropdown. If the world appears upside down, try adding a `-` in front of the value in the middle box.
The 3rd box is the camera rotation. Leave it blank for the camera to be horizontal.
> Feel free to tweak the positions so they fit the preview!

> If changes don't appear to be happening to the preview, hit enter after every field you change!

If you want to focus on a specific object, edit the field of view, subject distance and depth of field. If the thing you want to focus on is in the middle of the image as shown by the crosshair, click autofocus.
Otherwise, you can leave this setting unchanged.

Hit the lighting tab.
![Lighting Tab](https://i.imgur.com/NpKrSkf.png)

Change the values here as you please.
Set skylight to a lower value for a more night-time looking result.

Enable emitters if you want things like torches, lava, glowstone, etc emit light in the render.

> Emitters will *significantly* increase render times, and require a much higher SPP to look smooth!

Change the sun position, etc to whatever you want to affect shadows, etc

Adjust the sky and fog tab as you please, not much to explain there.

Hit the water tab.

![Water Tab](https://i.imgur.com/iYn7CDe.png)

Adjust water however you see fit.
Still water removes the natural 'ripple' effect from water.
Water Visibility affects how far under water you can see.
Water Opacity affects how transparent the water appears. 1 = Solid. 0 = Completely clear.
Set the water colour to whatever you like.

> Having unstill water, a high water visibility and low water opacity can make render times longer!

Feel free to adjust whatever you want in the entity tab.
Press `-` to remove the entity from the render, and `+` to add new ones.

> Entities usually have a minimal effect on render times.

> I am not going to cover the Materials tab or post-processing tab in this guide, but feel free to experiment with it!

> Post Processing can have a large impact on render times while the preview window is open. Close it while Chunky is rendering!

Click the Advanced Tab.

![Advanced Tab](https://i.imgur.com/hOlrMiQ.png)

Adjust CPU load and threads as you see fit. Chunky renders using solely CPU. GPU support may come Soon (tm)
> If you plan to use your PC while it is rendering / have a weaker computer, reduce CPU load to around 40-60% and reduce threads as you see fit. Be aware that lower CPU load / less threads can significantly increase render times!

Set Ray Depth to whatever you want. 3-8 is usually good enough.

Click the Shutdown on render complete if you want your computer to shutdown after the target SPP has been reached.

> If you are using linux, this option will have no effect unless you allow the `shutdown` command to run without needing `sudo` as the command requires `sudo` permissions. For obvious reasons, Chunky won't store your sudo password for when it's time to execute the command x). You can find a guide on the internet fairly easily for allowing the shutdown command to run without `sudo`.

Set the target SPP to whatever you want.

> SPP means samples per pixel. A lower SPP has significantly faster render times, but the image may appear grainy. A higher SPP takes longer to render, but the image will have much less grains.
If you are using emitters, you will need a much higher SPP then if you weren't.
There is no right or wrong amount of SPP, but 500-3000 is good place to aim :)

When you are ready, hit render, and wait for your beautiful image to be produced!
> This could take anywhere between two minutes and two days. Sit tight!

> If you get an error complaining about a missing directory, hit OK and let it create the folder for you. It should continue as normal.

Here is what my finished image looks like:

![Final](https://i.imgur.com/POsTgzy.png)

Your result will be stored in your .chunky/scenes folder:

- Windows: C:\Users/Your_User_Name/AppData/Local/.chunky/scenes (if it is not in AppData/Local, try AppData/Roaming)
- Linux: /home/.chunky/scenes

Move the image somewhere safe and delete what you don't need from inside the scenes folder, ready for your next render. While it isn't required, it helps keep your scene list clean.

> The number next to the image name is the number of SPP the image was exported as. You may have multiple images if you set 'Save Snapshot for each dump' to checked. The image with the highest number is your finished result!

> This guide was written by EmeraldSnorlax :)

