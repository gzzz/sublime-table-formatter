TableFormatter – simple plugin, formatting TSV-data into space-indented table.

# Usage
Format (auto-aligned):
```
1	a	z	-1.11
22	bbbb	y	22.22
333	cccccccc	x	333.33
```
→
```
  1 a        z  -1.11
 22 bbbb     y  22.22
333 cccccccc x 333.33
```

Format (left-aligned):
```
1	a	z	-1.11
22	bbbb	y	22.22
333	cccccccc	x	333.33
```
→
```
1   a        z -1.11
22  bbbb     y 22.22
333 cccccccc x 333.33
```

Format (right-aligned):
```
1	a	z	-1.11
22	bbbb	y	22.22
333	cccccccc	x	333.33
```
→
```
  1        a z  -1.11
 22     bbbb y  22.22
333 cccccccc x 333.33
```

# Installation
Supports Sublime Text 2 and 3.
Use your version number in directory path.

## OS X
```
cd ~/"Library/Application Support/Sublime Text 2/Packages"
git clone https://github.com/gzzz/sublime-table-formatter.git TableFormatter
```

## Windows
```
cd %AppData%\Sublime Text 2\Packages\
git clone https://github.com/gzzz/sublime-table-formatter.git TableFormatter
```