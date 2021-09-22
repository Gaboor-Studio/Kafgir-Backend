## App Structure  

![Sructure](https://user-images.githubusercontent.com/60196448/131831902-37f25f4d-a164-414e-9391-ee6c10def570.PNG)  

├── `urls.py` *Contains url mappings of the app. It uses url patterns defined in url_patterns package.*  

├── `apps.py` *Contains app config and sets wiring of the containers.*  
  
├── [models](models/): *Contains all models. Related models can be defined in the same file but its better to seperate them all.*  
│   ├── `__init__.py` All models should be imported in this file.    
│   └── `<model_name>.py` Contains definition of a model or some related models.

├── [repositories](repositories/): *Contains abstract definitions of repositories.*   
│   └── `<model_name>_repo.py` Contains definition of a repository. Each class must extend abc.ABC class.  

├── [repositories_impl](repositories_impl): *Contains implementations of repositories.*      
│   └── `<repository_name>_impl.py` Contains implementation of a repository. Each class must extend its own repository.

├── [dto](dto/): *Contains all DTOs of the app. use case related DTOs should be placed in the same file.*  
│   └── `<usecase_name>_dto.py` Contains all DTOs of a specific use case.  

├── [exceptions](exceptions/): *Contains all custom defined exceptions. Each file contains errors with the same error code.*  
│   ├── `bad_request.py` Bad request errors should be defined here.  
│   ├── `common.py` Common errors such as validation error can be defined here.  
│   └── `not_found.py` Not found errros should be defined here.  

├── [mappers](mappers/): *Contains all mappers. Mappers with same model should be placed in the same file.*  
│   └── `<model_name>_mapper.py` Contains all mappers of a specific model.  

├── [usecases](usecases/): *Contains abstract definitions of services.*  
│   ├── [auth](usecases/auth/): *All auth related use cases should be defined in this package*  
│   │   └── `auth_<usecase_name>.py` Contains definition of an auth related use case. Each class must extend abc.ABC class.  
│   └── [member](usecases/member/): *All member side related use cases should be defined in this package*  
│        └── `member_<usecase_name>.py` Contains definition of a member side related use case. Each class must extend abc.ABC class.   

├── [services](services/): *Contains implementations of services.*  
│   ├── [auth](services/auth): *All auth related services should be defined in this package*  
│   │   └── `auth_<service_name>.py` Contains definition of an auth related service. Each class must extend its own use case.  
│   ├── [member](services/member/): *All member side related services should be defined in this package*  
│        └── `member_<service_name>.py` Contains definition of a member side related service. Each class must extend its own use case.

└── [serializers](serializers/): *Contains definitions of all serializers. Model related serializers should be placed in the same file.*  
│   └── `<model_name>.py` Contains  definitions of serializers with the same model.
  
├── [views](views/): *Contains definition of REST API views.*  
│   ├── [auth](views/auth/): *Contains definition of all auth related views.*  
│   │   └── `auth_<view_name>.py` Contains definition of an auth related view.  
│   └── [member](views/member/): *Contains definition of all member side related views.*  
│        └── `member_<view_name>.py` Contains definition of a member side related view.    
  
├── [containers](containers/): *Contains all containers. We use 3 containers to organize objects.*  
│   ├── `repo_container.py` All repositories are defined inside this container.  
│   ├── `mapper_container.py` All mappers are defined inside this container.   
│   └── `usecase_container.py` All use cases are defined inside this container.  
  
├── [url_patterns](url_patterns/): *Contains url mappings of each use case.*  
│   ├── [auth](views/auth/): *Contains url mappings of all auth related use cases.*  
│   │   └── `auth_<usecase_name>_urls.py` Contains url mappings of an auth related use case.  
│   └── [member](views/member/): *Contains definition of all member side related views.*  
│        └── `member_<usecase_name>_urls.py` Contains url mappings of an auth related use case.      
