import pytest
import pytest_asyncio
import ezboilerplate.config.settings
from ezboilerplate.adapters.mongodb_adapter import MongoDBAdapter

@pytest_asyncio.fixture
async def mongo_adapter():
    adapter = MongoDBAdapter()
    await adapter.connect()
    yield adapter
    await adapter.disconnect()


@pytest.mark.asyncio
async def test_connect_and_health(mongo_adapter):
    assert mongo_adapter._client is not None
    assert mongo_adapter._db is not None

    is_alive = await mongo_adapter.health_check()
    assert is_alive is True


@pytest.mark.asyncio
async def test_get_collection(mongo_adapter):
    coll = mongo_adapter.get_collection("notes")
    assert coll is not None
    # puoi testare un insert/delete minimo
    result = await coll.insert_one({"title": "Hello Test"})
    doc = await coll.find_one({"_id": result.inserted_id})
    assert doc["title"] == "Hello Test"
