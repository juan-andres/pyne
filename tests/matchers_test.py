from pyne.expectations import expect
from pyne.matchers import anything, match, contains_text, contains, instance_of


def test__anything__satisfies_to_be():
    expect(anything()).to_be(1234)
    expect(1234).to_be(anything())


def test__match__can_match_regex():
    expect("hello (world)").to_be(match("h.*\(world\)"))


def test__match__when_string_is_different__does_not_match():
    expect("hello world").not_to_be(match("happy.*world"))


def test__contains_text__can_match_text():
    expect("hello world").to_be(contains_text("world"))


def test__contains_text__when_string_is_different__does_not_match():
    expect("hello world").not_to_be(contains_text(".*"))


def test__contains_text__when_subject_is_not_iterable__does_not_match():
    expect(None).not_to_be(contains_text("world"))


def test__contains__can_match_array():
    expect(["some-other-item", "some-item"]).to_be(contains("some-item"))


def test__contains__when_subject_is_not_iterable__does_not_match():
    expect(None).not_to_be(contains("world"))


def test__instance_of__can_match_type():
    expect("hello").to_be(instance_of(str))


def test__instance_of__when_subject_is_different_type__does_not_match():
    expect("hello").not_to_be(instance_of(int))
