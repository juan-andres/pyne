from pyne.expectations import expect
from pyne.matchers import anything, equal_to, match
from tests.test_helpers import SomeClass, expect_expectation_to_fail_with_message


def test__to_be__can_pass():
    expect(1).to_be(1)


def test__to_be__fails_with_message():
    expect_expectation_to_fail_with_message(
            lambda: expect(1).to_be(2),
            "Expected <1> to be <2>")


def test__to_be__with_a_matcher_can_pass():
    expect(anything()).to_be(1234)
    expect(1234).to_be(anything())


def test__not_to_be__can_pass():
    expect(3).not_to_be(4)
    expect(None).not_to_be("hello")


def test__not_to_be__when_equal__fails_with_message():
    expect_expectation_to_fail_with_message(
            lambda: expect(1).not_to_be(1),
            "Expected <1> not to be <1>")


def test__to_have_length__can_pass():
    expect([123, 123, 123, "123"]).to_have_length(4)


def test__to_have_length__fails_with_message():
    expect_expectation_to_fail_with_message(
            lambda: expect([123, 123, 123, "123"]).to_have_length(5),
            "Expected <\[123, 123, 123, '123'\]> to have length <5>")


def test__not_to_have_length__can_pass():
    expect([123, 123]).not_to_have_length(3)


def test__not_to_have_length__fails_with_message():
    expect_expectation_to_fail_with_message(
            lambda: expect([123, 123]).not_to_have_length(2),
            "Expected <\[123, 123\]> not to have length <2>")


def test__to_raise_error_with_message__can_pass():
    def error_method():
        raise Exception("some message")

    expect(error_method).to_raise_error_with_message("some message")


def test__to_raise_error_with_message__can_fail_because_the_message_is_wrong():
    def error_method():
        raise Exception("some message")

    expect_expectation_to_fail_with_message(
            lambda: expect(error_method).to_raise_error_with_message("some other message"),
            "to raise an exception with message",
            "but the exception was")


def test__to_raise_error_with_message__can_fail_because_no_error_is_raised():
    def successful_method():
        pass

    expect_expectation_to_fail_with_message(
            lambda: expect(successful_method).to_raise_error_with_message("some message"),
            "but no exception was raised")


def test__to_raise_error_with_message__can_pass_with_matcher():
    def error_method():
        raise Exception("some message")

    expect(error_method).to_raise_error_with_message(anything())


def test__to_raise_error_of_type__can_pass():
    class SomeException(Exception):
        pass

    def error_method():
        raise SomeException()

    expect(error_method).to_raise_error_of_type(SomeException)


def test__to_raise_error_of_type__can_fail_because_the_type_is_wrong():
    def error_method():
        raise Exception("some error")

    class SomeException(Exception):
        pass

    expect_expectation_to_fail_with_message(
            lambda: expect(error_method).to_raise_error_of_type(SomeException),
            "to raise an exception of type <SomeException>", "but the exception was")


def test__to_raise_error_of_type__can_fail_because_no_error_is_raised():
    def successful_method():
        pass

    class SomeException(Exception):
        pass

    expect_expectation_to_fail_with_message(
            lambda: expect(successful_method).to_raise_error_of_type(SomeException),
            "but no exception was raised")


def test__to_raise_error_of_type__can_pass_with_matcher():
    def error_method():
        raise Exception("some error")

    expect(error_method).to_raise_error_of_type(anything())


def test__to_raise_error_with_message__with_unmatched_matcher__failures_shows_matcher_name():
    def error_method():
        raise Exception("some message")

    expect_expectation_to_fail_with_message(
            lambda: expect(error_method).to_raise_error_with_message(match("other message")),
            ".*to raise an exception with message <match\('other message',\).*")


def test__to_raise_error_with_message__when_actual_message_contains_curly_braces__shows_message():
    def error_method():
        raise Exception("{oh man} {stuff!} {whoa}")

    expect_expectation_to_fail_with_message(
            lambda: expect(error_method).to_raise_error_with_message(match("other message")),
            "{oh man\} {stuff!\} {whoa\}")


def test__to_be_a__can_pass():
    expect(1).to_be_a(int)
    expect('').to_be_a(str)
    expect(SomeClass()).to_be_a(SomeClass)


def test__to_be_a__when_the_type_is_different__fails_with_message():
    expect_expectation_to_fail_with_message(
            lambda: expect('hello').to_be_a(SomeClass),
            "Expected <hello> to be a .*SomeClass.*")


def test__to_contain__can_pass():
    expect(["hello"]).to_contain("hello")
    expect("hello").to_contain("he")


def test__to_contain__when_item_not_contained__fails_with_message():
    expect_expectation_to_fail_with_message(
            lambda: expect(["some-item"]).to_contain("some-other-item"),
            "Expected <\['some-item'\]> to contain <some-other-item>")


def test__to_contain__can_pass_with_matcher():
    expect(["hello"]).to_contain(equal_to("hello"))
