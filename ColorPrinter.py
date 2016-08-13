class ColorPrinter:
    """
    Print message to terminal with colored header
    """
    def __init__(self, header=''):
        self.__header = header
        self.__levels = {
            'log': '\033[0m',  # terminal color header
            'info': '\033[1;32;40m',  # green header
            'warn': '\033[1;33;40m',  # yellow header
            'error': '\033[1;31;40m',  # red header
        }

    def setHeader(self, header=''):
        self.__header = header

    def __format(self, message, level='log'):
        header = self.__levels.get(level, self.__levels['log']) + self.__header + self.__levels['log'] if self.__header else ''
        body = ' ' + message if message else ''
        return header + body

    # `info` print the message with terminal color header
    def log(self, message='', *others):
        print self.__format(' '.join((message,) + others), 'log')
        return self

    # `info` print the message with green header
    def info(self, message='', *others):
        print self.__format(' '.join((message,) + others), 'info')
        return self

    # `warn` print the message with yellow header
    def warn(self, message='', *others):
        print self.__format(' '.join((message,) + others), 'warn')
        return self

    # `error` print the message with red header
    def error(self, message='', *others):
        print self.__format(' '.join((message,) + others), 'error')
        return self
