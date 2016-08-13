# ColorPrinter
print message to terminal with colored header


## usage
```python
printer = ColorPrinter('Legend:')
printer.log('hello world', 'and', 'hello kitty')
printer.info('hello world', 'and', 'hello kitty')
printer.warn('hello world', 'and', 'hello kitty')
printer.error('hello world', 'and', 'hello kitty')

print

printer.setHeader('[LEGEND]:')
printer.log('hello world', 'and', 'hello kitty')
printer.info('hello world', 'and', 'hello kitty')
printer.warn('hello world', 'and', 'hello kitty')
printer.error('hello world', 'and', 'hello kitty')

print

printer.setHeader('[legend]:')
printer.log('hello world', 'and', 'hello kitty') \
    .info('hello world', 'and', 'hello kitty') \
    .warn('hello world', 'and', 'hello kitty') \
    .error('hello world', 'and', 'hello kitty')
```