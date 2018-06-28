class BehaviorBlock:
    def __init__(self, parent, method):
        self.method = method
        self.parent = parent

    def run(self):
        pass


class DescribeBlock(BehaviorBlock):
    def __init__(self, parent, context_description, method):
        class Context(object):
            def __init__(self):
                if parent is not None:
                    for attr in dir(parent.context):
                        if not hasattr(self, attr):
                            setattr(self, attr, getattr(parent.context, attr))

        super().__init__(parent, method)
        self.describe_blocks = []
        self.before_each_blocks = []
        self.it_blocks = []
        self.context = Context()
        self.context_description = context_description


class ItBlock(BehaviorBlock):

    @staticmethod
    def pending():
        pass

    def __init__(self, parent, description, method):
        super().__init__(parent, method)
        self.description = description

    def run(self):
        try:
            self.method()
        except Exception as e:
            print("Test failed: " + self.description)
            raise e


class BeforeEachBlock(BehaviorBlock):
    def __init__(self, parent, method):
        super().__init__(parent, method)

    def run(self):
        self.method()