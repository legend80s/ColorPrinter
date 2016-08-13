# ColorPrinter
Print Message to Terminal with Colored Header Supporting `log`, `info`, `warn`, `error`
## usage
- Snippets

```python

from ColorPrinter import ColorPrinter

printer = ColorPrinter('Legend:')
printer.log('Hello world', 'and', 'hello kitty')
printer.info('Hello world', 'and', 'hello kitty')
printer.warn('Hello world', 'and', 'hello kitty')
printer.error('Hello world', 'and', 'hello kitty')

print '\nset header to [LEGEND]:\n'

printer.setHeader('[LEGEND]:')
printer.log('Hello world', 'and', 'hello kitty')
printer.info('Hello world', 'and', 'hello kitty')
printer.warn('Hello world', 'and', 'hello kitty')
printer.error('Hello world', 'and', 'hello kitty')

print '\ncall in chain\n'

printer.setHeader('[legend]:')
printer.log('Hello world', 'and', 'hello kitty') \
    .info('Hello world', 'and', 'hello kitty') \
    .warn('Hello world', 'and', 'hello kitty') \
    .error('Hello world', 'and', 'hello kitty')

```

- Results

![usage](https://github.com/legend80s/statics/blob/master/ColorPrinter-result.png?raw=true)
