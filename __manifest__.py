# Copyright (c) Delektre Ltd 2018-
# Authors:
#   Tommi Rintala (New Cable Corporation Ltd)

# noinspection PyStatementEffect
{
    "name": "HR - Travel support (simple)",
    "category": "Human Resources",
    "version": "0.0.1",
    "summary": "Travelsupport (Simple)",
    "description": """
    Simple travel support extension.

    This extension adds support for travelling, namely:
    - loyalty cards
    """,
    "author": "Tommi Rintala, Delektre Ltd",
    "depends": [
        "hr",
    ],
    "data": [
        'views/hr_travelsupport_views.xml',
    ],
    "installable": True,
}
