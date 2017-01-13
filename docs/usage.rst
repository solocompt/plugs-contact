=====
Usage
=====

To use Plugs Contact in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'plugs_contact.apps.PlugsContactConfig',
        ...
    )

Add Plugs Contact's URL patterns:

.. code-block:: python

    from plugs_contact import urls as plugs_contact_urls


    urlpatterns = [
        ...
        url(r'^', include(plugs_contact_urls)),
        ...
    ]
