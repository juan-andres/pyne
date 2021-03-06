import re


class SomeClass:

    def some_method(self, *args, **kwargs):
        pass

    def some_other_method(self, *args, **kwargs):
        pass


def expect_expectation_to_fail_with_message(expectation, *message_regexes):
    error = None
    try:
        expectation()
    except AssertionError as e:
        error = e
    finally:
        for message_regex in message_regexes:
            assert re.search(message_regex, error.args[0])
