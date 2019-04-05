class WrongLocationError(Exception):
    """Raise when a specific subset of values in context of app is wrong"""

    def __init__(self, *args):
        super(WrongLocationError, self).__init__(*args)
