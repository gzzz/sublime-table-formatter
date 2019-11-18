TableFormatter – simple plugin, formatting TSV-data into space-indented table.

# Usage
## Format (left-aligned)
```
1	a	z
2	bbbb	y
3	cccccccc	x
```
→
```
1 a        z
2 bbbb     y
3 cccccccc x
```

## Format (right-aligned)
```
1	a	z
2	bbbb	y
3	cccccccc	x
```
→
```
1        a z
2     bbbb y
3 cccccccc x
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
