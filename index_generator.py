import os

BASE_DIR = "."
INDEX_FILE = "index.html"

html = """
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Novels</title>

<style>
body{
  font-family: Arial;
  max-width: 900px;
  margin: auto;
}

h2{
  border-bottom: 1px solid #ccc;
}

a{
  display:block;
  margin:4px 0;
}
</style>

</head>
<body>

<h1>Novel Index</h1>
"""

for folder in sorted(os.listdir(BASE_DIR)):

    if os.path.isdir(folder):

        html += f"<h2>{folder}</h2>\n"

        files = sorted(os.listdir(folder))

        for file in files:
            if file.endswith(".html"):
                html += f'<a href="{folder}/{file}">{file}</a>\n'

html += """
</body>
</html>
"""

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print("index.html regenerated")