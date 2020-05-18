
class lazy_object:
    '''
    Class for deferred instantiation of objects.  Init is called
    only when the first attribute is either get or set.
    '''

    def __init__(self, callable, *args, **kw):
        '''
        callable -- Class of objeсt to be instantiated or functionnn to be called
        *args -- arguments to be used when instantiating object
        **kw  -- keywords to be used when instantiating object
        '''
        self.__dict__['callable'] = callable
        self.__dict__['args'] = args
        self.__dict__['kw'] = kw
        self.__dict__['obj'] = None

    def initObj(self):
        '''
        Instantiate object if not already done
        '''
        if self.obj is None:
            self.__dict__['obj'] = self.callable(*self.args, **self.kw)

    def __getattr__(self, name):
        self.initObj()
        return getattr(self.obj, name)

    def __setattr__(self, name, value):
        if name == 'reset' and value == 1 and self.obj is not None:
            self.__dict__['obj'] = None
        else:
            self.initObj()
            setattr(self.obj, name, value)

    def __len__(self):
        self.initObj()
        return len(self.obj)

    def __getitem__(self, idx):
        self.initObj()
        return self.obj[idx]
