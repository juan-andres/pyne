from pyne.expectations import expect
from pyne.matchers import contains
from pyne.pyne_result_reporters import PyneFailureSummaryReporter
from pyne.pyne_test_blocks import ItBlock
from tests.test_helpers.fake_print import StubPrint, printed_text


def test__report_end_result__when_test_had_assertion_error__includes_the_file_location():
    reporter = PyneFailureSummaryReporter()
    with StubPrint():
        exception = Exception()
        try:
            raise exception
        except Exception as e:
            block = ItBlock(None, None, None)
            reporter.report_failure(block, block, e, 0)
            reporter.report_end_result()

    expect(printed_text).to_contain(contains("reporters/pyne_failure_summary_reporter_test.py"))
