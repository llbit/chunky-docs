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
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>%s</title>
<link rel="stylesheet" href="/style.css">
</head>
<body>
<table id="wrapper">
<tr id="header">
  <th id="logo">
    <a href="/"><img alt="Chunky logo" src="/logo.png"></a>
  </th>
  <th id="title">
    <h1>Chunky Documentation</h1>
    <h2>Documentation of the Minecraft renderer</h2>
  </th>
</tr>
<tr id="content">
  <td id="menu"></td>
  <td id="article">
""" % text.split('\n', 1)[0])
sys.stdout.write(markdown.markdown(text).encode('utf-8'))
sys.stdout.write("""
  </td>
</tr>
</table></body></html>""")
sys.stdout.flush()
