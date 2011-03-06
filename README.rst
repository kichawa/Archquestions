Arch questions
==============

demo_


Dev howto
---------

Aplikacja pisana jest na platformę GAE_ w Django_ 1.2. Z oczywistych wzlgędów,
djangowy ORM zastępuje datastore_.

Aby uruchomić lokalną instancję aplikacji, trzeba pobrać najnowsze SDK_,
sklonować repozytorium_, a następnie z katalogu `src` uruchomić serwer.
Wymagany jest Python 2.x::

    $ git clone git://github.com/husio/Archquestions.git
    $ cd src
    $ python2 <path_to_sdk>/dev_appserver.py .
    INFO     2011-03-06 18:23:29,711 appengine_rpc.py:153] Server: appengine.google.com
    INFO     2011-03-06 18:23:29,716 appcfg.py:413] Checking for updates to the SDK.
    INFO     2011-03-06 18:23:30,346 appcfg.py:427] The SDK is up to date.
    INFO     2011-03-06 18:23:30,483 dev_appserver_main.py:507] Running application archquestions on port 8080: http://localhost:8080


.. _demo: http://archquestions.appspot.com/
.. _GAE: http://code.google.com/intl/pl-PL/appengine/docs/python/gettingstarted/
.. _Django: http://www.djangoproject.com/
.. _datastore: http://code.google.com/intl/pl-PL/appengine/docs/python/datastore/
.. _SDK: http://code.google.com/intl/pl-PL/appengine/downloads.html
.. _repozutorium: https://github.com/husio/Archquestions
