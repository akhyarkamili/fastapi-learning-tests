def test_startswith() -> None:
    valid_paths = ("/v1/hello", "/v1/hi", "/v1/greetings/hello", "/v1/greetings/hi")

    assert "/v1/hello?text=hello".startswith(valid_paths), "hello should be a valid path"
    assert "/v1/hi?text=hello".startswith(valid_paths), "hi should be a valid path"
    assert not "/v1".startswith(valid_paths), "v1 should not be a valid path"