import pyblish.api


class SelectCurrentFile(pyblish.api.Selector):
    """Inject the current working file into context"""

    hosts = ["softimage"]

    def process(self, context):
        self.log.warning("Not actually doing anything, implement me!")
