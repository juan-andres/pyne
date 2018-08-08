from pyne.pyne_test_collector import it, fit, fdescribe, describe
from pyne.pyne_tester import pyne


@pyne
def sample_test():
    @fit("can be focused")
    def _(self):
        pass

    @fit("can be focused")
    def _(self):
        pass

    @it("can be ignored")
    def _(self):
        pass

    @fdescribe("a focused block")
    def _():
        @it("runs its children")
        def _(self):
            pass

        @describe("its grandchildren")
        def _():
            @it("also run")
            def _(self):
                pass