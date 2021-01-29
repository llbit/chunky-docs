Tips
====

General Render Tips
-------------------

* Disable sunlight when rendering underground scenes or indoor scenes where
  there is no visible natural light. This will increase the average number of
  Samples Per Second (SPS) rendered.
* Disable emitters to greatly decrease the required render time. This however
  disables all light emitting blocks such as torches, lava etc.
* Disable gamma correction during long renders to speed up the rendering
  process. When the image starts to get finished gamma correction can be
  re-enabled again without losing progress.  Also, hide the [Render Preview
  Window][1] during renders to speed up overall render time.
	This issue is mostly fixed as of Chunky 2.3.0.
* Increase the Ray Depth if you have a scene with many transparent or shiny
  blocks.
* The rendering technique used in Chunky (Path Tracing) is very CPU intensive.
  Therefore, to maximize the speed and efficiency of a render, all CPU threads
  should be utilized at 100%. If you would like to run Chunky in the
  background, you can adjust how much CPU is allocated to Chunky. Visit the
  [Advanced Render Controls][0] page for more information on how to do this.

[0]:render_controls_advanced.html
[1]:render_preview.html
