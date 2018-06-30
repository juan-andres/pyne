from pyne.expectations import expect
from pyne.pyne_result_reporter import PyneResultReporter

printed_text = []


def fake_print(text):
    printed_text.append(text)


def test_report_result__when_a_test_fails__it_prints_an_x():
    printed_text.clear()
    reporter = PyneResultReporter(fake_print)

    def failing_method():
        expect(True).to_be(False)

    reporter.report_result(failing_method)

    expect(printed_text[0]).to_be("x")


def test_report_result__when_a_test_succeeds__it_prints_a_dot():
    printed_text.clear()
    reporter = PyneResultReporter(fake_print)

    def passing_method():
        pass

    reporter.report_result(passing_method)

    expect(printed_text[0]).to_be(".")


def test__end_result__when_a_test_has_failed__it_raises_test_failed():
    reporter = PyneResultReporter(fake_print)

    def failing_method():
        expect(True).to_be(False)

    reporter.report_result(failing_method)
    expect(reporter.report_end_result).to_raise_error_message("Tests failed.")


def test__end_result__when_all_tests_passed__it_prints_success():
    printed_text.clear()
    reporter = PyneResultReporter(fake_print)

    def passing_method():
        pass

    reporter.report_result(passing_method)

    reporter.report_end_result()

    expect(printed_text[1]).to_be("Success!")


def test__end_result__when_no_tests_run():
    pass