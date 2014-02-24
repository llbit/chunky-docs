import sys
import markdown
import codecs

if len(sys.argv) > 1:
	with codecs.open(sys.argv[1], mode='r', encoding='utf-8') as f:
		text = f.read()
else:
	with codecs.getreader('utf-8')(sys.stdin) as f:
		text = f.read()

title = text.split('\n', 1)[0]
sys.stdout.write("""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>%s</title>
<link href="style.css" rel="stylesheet" type="text/css">
<link href='http://fonts.googleapis.com/css?family=Open+Sans:400,800' rel='stylesheet' type='text/css'>
</head>
<a name="top"></a>
<body>
	<table id="wrapper">
		<tr id="header">
			<th id="logo">
				<a href="index.html"><img src="logo.png"></a>
			</th>
			<th id="title">
				<h1 class="title">Chunky</h1>
				<h2 class="subtitle">Minecraft World Renderer</h2>
			</th>
		</tr>
		<tr id="content">
			<td id="menu">
				<ul class="menu-text">
			<li><a href="index.html">Home</a></li>
			<li><a href="getting_started.html">Getting Started</a></li>
				<ul class="menu-text-indented">
					<li><a href="install.html">Installation</a></li>
					<li><a href="tips_tutorials.html">Tips / Tutorials</a></li>
				</ul>
			<li><a href="faqs.html">FAQs</a></li>
			<li>User Guides</li>
				<ul class="menu-text-indented">
				<li><a href="path_tracing.html">Path Tracing</a>
				</li><li><a href="headless.html">Headless Rendering</a></li>
				<li><a href="scene_format.html">Scene Discription Format</a></li>
				</ul>
			<li>UI Guides</li>
				<ul class="menu-text-indented">
				<li><a href="2d_map_view.html">2D Map View</a></li>
				<li><a href="render_controls.html">Render Controls</a></li>
				<li><a href="render_preview.html">Render Preview Window</a></li>
				</ul>
			</ul>
			<hr class="hr-padded">
			<ul class="menu-text">
				<li><a href="http://github.com/llbit/chunky">GitHub Page</a></li>
				<li><a href="http://github.com/llbit/chunky/issues">Issue Tracker</a></li>
				<li><a href="http://www.reddit.com/r/chunky">Reddit Community</a></li>
			</ul>
			<hr class="hr-padded">
			<ul class="menu-text">
				<li><a href="galleries.html">Galleries</a></li>
				<li><a href="skymaps.html">Skymaps</a></li>
			</ul>
			<hr class="hr-padded">
			<ul class="menu-text">
				<li><a href="contributing.html">Contributing</a></li>
				<li><a href="credits.html">Credits</a></li>
			</ul>
		</td><!--End Menu Div-->
		<!--Content goes here -->
		<td id="article">
""" % title)
sys.stdout.write(markdown.markdown(text, ['extra']).encode('utf-8'))
sys.stdout.write("""
		</td>
		</tr>
	</table>
</body>
</html>""")
sys.stdout.flush()
