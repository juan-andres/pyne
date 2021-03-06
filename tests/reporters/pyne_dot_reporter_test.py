from pyne.expectations import expect
from pyne.pyne_result_reporters import PyneDotReporter
from pyne.pyne_test_blocks import ItBlock
from tests.test_helpers.fake_print import StubPrint, printed_text


def test__report_failure__prints_an_x():
    with StubPrint():
        reporter = PyneDotReporter()
        it_block = ItBlock(None, None, None)
        printed_text.clear()

        reporter.report_failure(it_block, it_block, Exception("some exception"), 1000)

        expect(printed_text[0]).to_be("x")


def test__report_pending__prints_a_dash():
    with StubPrint():
        reporter = PyneDotReporter()
        it_block = ItBlock(None, None, None)
        printed_text.clear()

        reporter.report_pending(it_block)

        expect(printed_text[0]).to_be("-")



def test__report_success__prints_a_dot():
    with StubPrint():
        reporter = PyneDotReporter()

        it_block = ItBlock(None, None, None)
        printed_text.clear()

        reporter.report_success(it_block, 0)

        expect(printed_text[0]).to_be(".")
