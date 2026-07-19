# -*- coding: utf-8 -*-

{
    "name": "Garage service",
    "version": "19.0.1.0.0",
    "description": """
    Application for vehicle repair
    garage service".
    """,
    "depends": [
        "base",
    ],
    "data": [
        "security/ir.model.access.csv",

        "views/garage_vehicle_views.xml",
        "views/garage_mechanic_views.xml",
        "views/garage_service_views.xml",
        "views/garage_repair_order_veiws.xml",
        
        "views/garage_menu_views.xml",
    ],
    "application": True,
    "author": "Angry andrii",
    "license": "LGPL-3",
}