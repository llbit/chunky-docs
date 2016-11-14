Plugin API
==========

Chunky 1.4 added experimental plugin support. This page documents how to build a new plugin
for Chunky, and the available plugin API interfaces.


## Creating a basic plugin

Chunky plugins are packaged as Jar files with a main class extending the
interface `se.llbit.chunky.plugin.Plugin`.

The simplest way to get started with your own plugin is perhaps to copy one of
these existing demo plugins:


* [Ambient occlusion renderer][1]
* [Block model changing (grass into lava)][2]
* [Custom Render Controls tab][3]

The Chunky plugin API can also be used to build new applications based on Chunky. Here is
an application that uses parts of the Chunky rendering system to render different kinds of
Minecraft blocks and items:

* [Test Renderer][7]


For building your plugin you can use [Gradle][5]. Here is the Gradle build script from
the custom Render Controls tab plugin:

```
apply plugin: 'java'
apply plugin: 'application'

repositories {
    mavenLocal()
    mavenCentral()
}

sourceCompatibility = '1.8'
targetCompatibility = '1.8'

dependencies {
    compile 'se.llbit:chunky-core:1.4.1'
}

defaultTasks 'jar'

mainClassName = 'se.llbit.chunky.plugin.TabMod'
```

If you want to test running your plugin using Gradle you will have to change the
`mainClassName` property to your plugin class name. The plugin class then also
needs a main method. Here is how you can launch Chunky from your plugin main class:

```
import se.llbit.chunky.Plugin;
import se.llbit.chunky.main.Chunky;
import se.llbit.chunky.main.ChunkyOptions;
import se.llbit.chunky.resources.TexturePackLoader;
import se.llbit.chunky.ui.ChunkyFx;

public class MyPlugin implements Plugin {
  public static void main(String[] args)
      throws FileNotFoundException, TexturePackLoader.TextureLoadingError {
    // Start Chunky normally with this plugin attached.
    Chunky.loadDefaultTextures();
    Chunky chunky = new Chunky(ChunkyOptions.getDefaults());
    new MyPlugin().attach(chunky);
    ChunkyFx.startChunkyUI(chunky);
  }
}
```


## Plugin manager

Plugin support has not yet been added to the regular Chunky launcher. A
separate plugin manager application can be used instead. You have to build it
yourself, but if you have Gradle installed, it should be fairly easy to build.
The plugin manager is available from [this GitHub repository][4].


## Plugin API methods

The plugin API will be expanded as needed for future plugins. If you have a
request for a new plugin API method, please suggest it over at the [Chunky
Issue Tracker][6].

This is a list of the methods available to plugins currently in the plugin API:

* `se.llbit.chunky.main.Chunky`:
    * `setRenderContextFactory()` - changes the `RenderContext` factory.
    The render context is used for  locating the scene directory and
    controlling some renderer configurations like the number of render threads.
    * `setSceneFactory()` - changes the `Scene` factory for the renderer.
    The `Scene` class encapsulates most of the scene state in the renderer.
    * `setPreviewRayTracerFactory()` - this sets the factory that builds
    the preview ray tracer. The preview ray tracer is used for rendering preview
    frames.
    * `setRayTracerFactory()` - this can be used to change the default Java path
    tracing renderer to a completely different renderer. This is done in the
    [ambient occlusion plugin demo][1].
    * `setRenderControlsTabTransformer()` - sets a callback for transforming
    the list of Render Controls tab. This can be used to insert a custom
    tab in the Render Controls window. See [the demo plugin][3] for a usage example.
* `se.llbit.chunky.world.Block`:
    * `set(int, Block)` - used to change the representation for a Minecraft block
    in the renderer. This can be used for simple things like changing textures or
    material properties (emittiance, shinyness, ...), as well as more advanced things like
    completely changing the block rendering model. See [the demo plugin][4] for
    an example.

## Things that will change

Since the plugin API is very new, with currently no third-party plugins using it,
it is very much unstable. Anything may change at this point, but in particular
these things will probably change:

* The `Scene` class is not well suited for encapsulating the scene state in a
  clean way. Some parts of the state are intentionally shared between threads
  in a way that is likely confusing to other developers. It also uses a very
  unintuitive synchronization scheme. The current implementation makes it
  difficult for plugins to safely extend or alter the scene state.
* Building a new type of renderer is not very well supported right now since
  there is only one current implementation: the default Java renderer. Adding
  an OpenCL renderer is likely very difficult right now just because the
  rendering architecture has been tightly integrated with the default renderer.
* The way block rendering for most blocks works is not pretty. It uses
  nonstandard triangle and quadrilateral representations for most block
  geometry. The ray tracing for these is not well documented and should
  probably be replaced by more standard triangle-based ray tracing.

[1]: https://github.com/llbit/Chunky-AOPlugin
[2]: https://github.com/llbit/Chunky-BlockMod
[3]: https://github.com/llbit/Chunky-TabMod
[4]: https://github.com/llbit/Chunky-PlugMan
[5]: https://gradle.org/
[6]: https://github.com/llbit/chunky/issues
[7]: https://github.com/llbit/Chunky-TestRenderer
