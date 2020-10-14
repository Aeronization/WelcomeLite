# (R. Friel - October 14, 2020) - Core Testing Logic.

# For a standard CRUD App, I would test the following:
    # Use django.test to import the correct classes to inherit from for testing.

    # 1) URLs: Urls resolve correctly and use the correct view.
        # 1.a) Example: use resolve(url) and assert that the .func or .func.view_class equals the view name.

    # 2) Views: Views resolve correctly and return the correct status code (ex: 200)
        # 2.a) Ensure that POST works and will create, update, or delete objects from DB.
        # 2.b) Ensure that the right template is being used.

    # 3) Models: Objects can be created when necessary fields are passed.
        # 3.a) Objects can also be updated, and deleted.

    # 4) Forms: Just test that the forms are valid when presented with valid data.
        # 4.a) Forms will return an error when presented with blank or invalid data.

    # 5) Functional Testing: Basically needs to use selenium and the StaticLiveServerTestCase.
        # 5.a) I don't think this testing would be required for a sample CRUD app.