from .plugin import KnowledgeBasePlugin


class Propagations(KnowledgeBasePlugin):

    def __init__(self, kb):
        self._kb = kb
        self._propagations = {}

    def __exists__(self, func_loc):
        """
        Internal function to check if a func, specified as a CodeLocation
        exists in our known propagations

        :param func_loc:    CodeLocation of function
        :return:            Bool
        """
        exists = False
        for props in self._propagations:
            if props.block_addr == func_loc.block_addr:
                exists = True

        return exists

    def update(self, func_loc, replacements):
        """
        Add the replacements to known propagations

        :param func_loc:        CodeLocation of function
        :param replacements:    Dict of replacements
        """
        self._propagations[func_loc] = replacements

    def get(self, func_loc):
        """
        Gets the replacements for a specified function location.
        If the replacement does not exist in the known propagations, it
        returns None.

        :param func_loc:    CodeLocation of function
        :return:            Dict or None
        """
        if self.__exists__(func_loc):
            return self._propagations[func_loc]
        else:
            return None

    def copy(self):
        o = Propagations(self._kb)
        o._propagations = {k: v for k, v in self._propagations.items()}


KnowledgeBasePlugin.register_default('propagations', Propagations)
