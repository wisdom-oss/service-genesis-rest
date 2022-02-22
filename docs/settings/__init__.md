---
sidebar_label: settings
title: settings
---

Python Package for the different settings which need to be configured


## BaseSettings

## Field

## GENESISOnlineLanguage

## GENESISAPISettings Objects

```python
class GENESISAPISettings(BaseSettings)
```

A Settings class handling the needed information for the access to the GENESIS Online database


#### username

GENESIS Online Username

The username which was issued by the GENESIS Online database during the signup. The signup is 
possible on the following page: `https://www-genesis.destatis.de/genesis/online?Menu=Registrierung`


#### password

GENESIS Online Password

The password used to access the GENESIS Online database. The initial password received via the
registration confirmation may not be used here. This is a restriction imposed by the GENESIS 
Online database. Please change your password beforehand.


#### language

GENESIS Online Language

The language used by GENESIS Online in the text fields in the responses.

Possible values
 - de (German/Deutsch)
 - en (English/Englisch) [default]


## ServiceRegistrySettings Objects

```python
class ServiceRegistrySettings(BaseSettings)
```

A settings class used to handle settings for the service registry


#### host

Service Registry Host

The hostname or ip address of the service registry which this service uses to register and 
set its status.


#### port

Service Registry Port

The port on which the service registry listens on, defaults to `8761`


## ApplicationSettings Objects

```python
class ApplicationSettings(BaseSettings)
```

A settings class managing the general settings of the application


#### name

Application Name

The name under which this service will register itself on the service registry and under 
which is it callable via the service registry, defaults to: `genesis-rest`


#### port

Application Port

The port which will be bound by the HTTP server for incoming traffic


