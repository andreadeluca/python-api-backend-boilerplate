from motor.motor_asyncio import AsyncIOMotorClient

from ezboilerplate.config import settings, loggerWrapper


class MongoDBAdapter:

    def __init__(self):
        self._client = None
        self._db = None
        self._logger = loggerWrapper.get_logger(__name__)

    async def connect(self):
        logger = loggerWrapper.get_logger(__name__)
        logger.debug("Connecting to MongoDB")


        uri = settings.retrieve_setting('DB_HOST')
        port = settings.retrieve_setting('DB_PORT')
        username = settings.retrieve_setting('DB_USERNAME')
        password = settings.retrieve_setting('DB_PASSWORD')
        dbname = settings.retrieve_setting('DB_NAME')


        logger.debug(f"uri: {uri}, port: {port}")

        if username and password:
            uri = f"mongodb://{username}:{password}@{uri}:{port}"
        else:
            uri = f"mongodb://{uri}:{port}/{dbname}"

        self._config = dict(
            uri=uri, port=port)
        logger.debug(f"uri: {uri}, port: {port}, username: {username}, password: {password}")

        try:
            logger.debug("Initializing MongoDB client")
            client = AsyncIOMotorClient(self._config['uri'])
            if client is not None:
                self._client = client
                self._db = client[settings.retrieve_setting('DB_NAME')]

        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")

    async def disconnect(self):
        if self._client:
            self._client.close()

    def get_collection(self, collection_name):
        if self._client:
            return self._db[collection_name]
        return None

    async def health_check(self):
        try:
            await self._db.command("ping")
            return True
        except Exception:
            return False
