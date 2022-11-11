from django.apps import AppConfig
from . import mqtt


class DataServerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'data_server'

    def ready(self) -> None:
        mqtt.MqttThread("192.168.0.11", 1883, 60, ["test"]).start()
