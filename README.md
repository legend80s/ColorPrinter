# ColorPrinter
Print message to terminal with <span style="color:green;">colored</span> header

## usage
- Snippets

```
python

from ColorPrinter import ColorPrinter

printer = ColorPrinter('Legend:')
printer.log('Hello world', 'and', 'hello kitty')
printer.info('Hello world', 'and', 'hello kitty')
printer.warn('Hello world', 'and', 'hello kitty')
printer.error('Hello world', 'and', 'hello kitty')
# <span style="color:red;">Hello world<span>
print

printer.setHeader('[LEGEND]:')
printer.log('Hello world', 'and', 'hello kitty')
printer.info('Hello world', 'and', 'hello kitty')
printer.warn('Hello world', 'and', 'hello kitty')
printer.error('Hello world', 'and', 'hello kitty')

print

printer.setHeader('[legend]:')
printer.log('Hello world', 'and', 'hello kitty') \
    .info('Hello world', 'and', 'hello kitty') \
    .warn('Hello world', 'and', 'hello kitty') \
    .error('Hello world', 'and', 'hello kitty')

```

- Results

<span style="color:gray;">Legend: Hello world and hello kitty</span>
<span style="color:green;">Legend</span>: Hello world and hello kitty
<span style="color:yellow;">Legend</span>: Hello world and hello kitty
<span style="color:red;">Legend</span>: Hello world and hello kitty

<span style="color:gray;">[LEGEND]: Hello world and hello kitty<span>
<span style="color:green;">[LEGEND]</span>: Hello world and hello kitty
<span style="color:yellow;">[LEGEND]</span>: Hello world and hello kitty
<span style="color:red;">[LEGEND]</span>: Hello world and hello kitty

<span style="color:gray;">\[legend]: Hello world and hello kitty</span>
<span style="color:green;">[legend]</span>: Hello world and hello kitty
<span style="color:yellow;">[legend]</span>: Hello world and hello kitty
<span style="color:red;">[legend]</span>: Hello world and hello kitty
