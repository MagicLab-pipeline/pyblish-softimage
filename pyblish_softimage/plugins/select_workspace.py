import pyblish.api


class SelectWorkspace(pyblish.api.Selector):
    """Inject the current working file into context"""

    hosts = ["softimage"]

    def process(self, context):
        self.log.warning("Not doing anything, implement me!")
