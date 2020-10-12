def test_solution():
    from solution import reverse

    assert reverse("hello") == "olleh"
    assert reverse("") == ""
    assert reverse("h") == "h"
    assert reverse("yes") == "sey"
