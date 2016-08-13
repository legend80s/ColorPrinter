from ColorPrinter import ColorPrinter

printer = ColorPrinter('Legend:')
printer.log('Hello world', 'and', 'hello kitty')
printer.info('Hello world', 'and', 'hello kitty')
printer.warn('Hello world', 'and', 'hello kitty')
printer.error('Hello world', 'and', 'hello kitty')

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
