from pyne.pyne_test_collector import it
from pyne.pyne_tester import pyne


@pyne
def some_second_file_test():
    @it("can also pass")
    def _(self):
        pass
