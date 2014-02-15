import sys
import markdown
import codecs

if len(sys.argv) > 1:
	with codecs.open(sys.argv[1], mode='r', encoding='utf-8') as f:
		text = f.read()
else:
	with codecs.getreader('utf-8')(sys.stdin) as f:
		text = f.read()

sys.stdout.write("""
<body>
	<div id="wrapper">
		<div id="header">
	    <div id="logo">
	    	<a href="index.html"><img src="images/logo.png" /></a>
	    </div>
	    <div id="title">
	    	<h1 class="title">Chunky</h1>
	        <h2 class="subtitle">Minecraft World Renderer</h2>
		</div>
	       </div>
	<div id="content">
		<div id="menu">
	      <ul class="menu-text">	
	        <li><a href="index.html">home</a></li>
	        <li><a href="getting started.html">getting started</a></li>
	            <ul class="menu-text-indented">
	                <li><a href="install.html">installation</a></li>
	                <li><a href="#">tutorials</a></li>
	            </ul>
	        <li><a href="#">faqs</a></li>
	        <li><a href="#">user guides</a></li>
	            <ul class="menu-text-indented">
	            	<li><a href="path_tracing.html">path tracing</a>
	                <li><a href="headless.html">headless rendering</a></li>
	                <li><a href="scene_format.html">scene discription format</a></li>
	            </ul>
	        <li><a href="#">control guides</a></li>
	            <ul class="menu-text-indented">
	                <li><a href="#">2d map preview</a></li>
	                <li><a href="#">render controls</a></li>
	                <li><a href="render_preview.html">render preview window</a></li>
	            </ul>
	        <li><a href="skymaps.html">skymaps</a></li>
	      </ul>
	      <hr class="hr-padded"/>
	      <ul class="menu-text">
	        <li><a href="http://github.com/llbit/chunky">github page</a></li>
	        <li><a href="http://github.com/llbit/chunky/issues">issue tracker</a></li>
	        <li><a href="http://www.reddit.com/r/chunky">reddit community</a></li>
	      </ul>
	      <hr class="hr-padded"/>
	      <ul class="menu-text">
	        <li><a href="galleries.html">galleries</a></li>
	      </ul>
	      <hr class="hr-padded"/>
	      <ul class="menu-text">
		<li><a href="contributing.html">contributing</a></li>
		<li><a href="credits.html">credits</a></li>
	      </ul>
	    </div><!--End Menu Div-->
	    <!--Content goes here -->
""" % text.split('\n', 1)[0])
sys.stdout.write(markdown.markdown(text).encode('utf-8'))
sys.stdout.write("""
       	</div>
</div>
</body>
</html>""")
sys.stdout.flush()
