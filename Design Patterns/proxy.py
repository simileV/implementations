"""
an object funnels operations to something else
Add functionality or logic (e.g. logging, caching, authorization) to a resource
without changing its interface.

Proxy is used in places where you want to add functionality to a class without
changing its interface. The main class is called `Real Subject`. A client should
use the proxy or the real subject without any code change, so both must have the
same interface. Logging and controlling access to the real subject are some of
the proxy pattern usages.

"""

