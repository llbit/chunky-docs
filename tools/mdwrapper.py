import sys
import markdown
import codecs

if len(sys.argv) > 1:
	with codecs.open(sys.argv[1], mode='r', encoding='utf-8') as f:
		text = f.read()
else:
	with codecs.getreader('utf-8')(sys.stdin) as f:
		text = f.read()

sys.stdout.write("""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>%s</title>
<link rel="stylesheet" href="/style.css">
</head>
<body>
<div id="content">
<header>
<h2 id="logo">
  <a href="/">
    <img alt="Chunky logo" src="/logo.png">
  </a>
</h2>
<div id="title">
  <h1>Chunky Documentation</h1>
  <h2>Documentation of the Minecraft renderer</h2>
</div>
</header>
<nav></nav>
<div id="article">
""" % text.split('\n', 1)[0])
sys.stdout.write(markdown.markdown(text).encode('utf-8'))
sys.stdout.write("</div></div></body></html>")
sys.stdout.flush()
