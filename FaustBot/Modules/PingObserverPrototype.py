from FaustBot.Modules.ModulePrototype import ModulePrototype
from FaustBot.Modules.ModuleType import ModuleType


class PingObserverPrototype(ModulePrototype):
    """
    The Prototype of a Class who can react to every action
    """

    @staticmethod
    def get_module_types():
        return [ModuleType.ON_PING]

    def __init__(self):
        pass

    def update_on_ping(self, data):
        raise NotImplementedError("Some module doesn't do anything")
