""" Module for sesame2 plugin tests. """

from unittest import TestCase

from rdflib import URIRef
import surf
from surf.test.plugin import PluginTestMixin

class Sesame2TestMixin(object):

    def _get_store_session(self, use_default_context = True):
        """ Return initialized SuRF store and session objects. """

        # FIXME: take endpoint from configuration file,
        kwargs = {"reader": "sesame2",
                  "writer" : "sesame2",
                  "server" : "localhost",
                  "port" : 8080,
                  "root_path" : "/openrdf-sesame",
                  "repository" : "test"}

        if use_default_context:
            kwargs["default_context"] = "http://surf_test_graph/dummy2"

        store = surf.Store(**kwargs)
        session = surf.Session(store)

        # Fresh start!
        store.clear(URIRef("http://surf_test_graph/dummy2"))
        store.clear(URIRef("http://my_context_1"))
        store.clear(URIRef("http://other_context_1"))
        store.clear()

        return store, session

class StandardPluginTest(TestCase, Sesame2TestMixin, PluginTestMixin):
    pass
