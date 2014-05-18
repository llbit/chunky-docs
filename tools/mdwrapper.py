import sys
import markdown
import codecs
import re

if len(sys.argv) > 1 and sys.argv[1] == 'prepare':
    # create menu template
    with codecs.open('misc/menu.md', mode='r', encoding='utf-8') as f:
        menu = f.read()
    with codecs.open('tmp/menu-template.html', mode='w', encoding='utf-8') as f:
        f.write(markdown.markdown(menu, ['extra']).encode('utf-8'))
    sys.exit(0)

if len(sys.argv) > 1:
	with codecs.open(sys.argv[1], mode='r', encoding='utf-8') as f:
		text = f.read()
else:
	with codecs.getreader('utf-8')(sys.stdin) as f:
		text = f.read()

# load menu template
with codecs.open('tmp/menu-template.html', mode='r', encoding='utf-8') as f:
	menu = f.read()

title = text.split('\n', 1)[0]
title = re.match('#*(.+)', title).group(1)
sys.stdout.write("""<!doctype html>
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
""" % title)
sys.stdout.write(menu)
sys.stdout.write("""
			</td>
			<!--Content goes here -->
			<td id="article">
""")
sys.stdout.write(markdown.markdown(text, ['extra']).encode('utf-8'))
sys.stdout.write("""
			</td>
		</tr>
	</table>
</body>
</html>""")
sys.stdout.flush()
