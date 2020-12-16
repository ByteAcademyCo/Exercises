def test_solution():
    from solution import reverse_words

    assert reverse_words("hi there") == "there hi"
    assert reverse_words("hello") == "hello"
    assert reverse_words("") == ""
    assert reverse_words("don't forget to be awesome") == "awesome be to forget don't"