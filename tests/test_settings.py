from ezboilerplate.config import settings


def test_retrieve_string(monkeypatch):
    monkeypatch.setenv("APP_NAME", "EzBoilerplate")
    assert settings.retrieve_setting("APP_NAME") == "EzBoilerplate"


def test_retrieve_string_default(monkeypatch):
    monkeypatch.delenv("NOT_EXISTING", raising=False)
    assert settings.retrieve_setting("NOT_EXISTING", "default_value") == "default_value"


def test_retrieve_int(monkeypatch):
    monkeypatch.setenv("PORT", "8080")
    assert settings.retrieve_int_setting("PORT") == 8080


def test_retrieve_int_invalid(monkeypatch):
    monkeypatch.setenv("PORT", "not_a_number")
    # Deve ritornare il default se non convertibile
    assert settings.retrieve_int_setting("PORT", 5000) == 5000


def test_retrieve_bool_true(monkeypatch):
    for val in ["1", "true", "TRUE", "yes", "on", "On"]:
        monkeypatch.setenv("DEBUG", val)
        assert settings.retrieve_bool_setting("DEBUG") is True


def test_retrieve_bool_false(monkeypatch):
    for val in ["0", "false", "no", "off", ""]:
        monkeypatch.setenv("DEBUG", val)
        assert settings.retrieve_bool_setting("DEBUG") is False

def test_retrieve_bool_default(monkeypatch):
    monkeypatch.delenv("DEBUG", raising=False)
    assert settings.retrieve_bool_setting("DEBUG", False) is False
    assert settings.retrieve_bool_setting("DEBUG", True) is True
