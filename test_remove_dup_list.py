def test_remove_dup_from_list():
    mylist = ["a", "b", "a", "c", "c"]
    mylist = list(dict.fromkeys(mylist))
    assert sorted(mylist) == ["a", "b", "c"]
