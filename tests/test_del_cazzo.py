def test_import_settings():
    import ezboilerplate.config.settings as s
    print("Settings file:", s.__file__)
    assert s is not None