import pkgutil

from sqlalchemy.ext.declarative import DeclarativeMeta


def discover_project_for_models(path=''):
    models_package_name = "models"
    main_package = path
    available_object_list = []
    for importer, package_name, _ispkg in pkgutil.iter_modules([main_package]):
        full_package_name = f"{main_package}.{package_name}"
        for sub_importer, sub_package_name, sub_ in pkgutil.iter_modules([f"{main_package}/{package_name}"]):
            if sub_package_name == models_package_name:
                module = __import__(f"{full_package_name}.{sub_package_name}", fromlist=[''])
                for attr in dir(module):
                    if isinstance(module.__dict__[attr], DeclarativeMeta):
                        available_object_list.append(module.__dict__[attr])
    return available_object_list
