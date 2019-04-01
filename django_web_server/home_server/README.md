# Development Environment

# Prod. Environment

# API Endpoints:

## /things/ledlights/

### GET

Returns a list of existing ledlights.

### POST

payload should look like:
```python
{
    "title": "some_title",
}
```
## /things/ledlights/uuid/

### GET

See info (state) about a specific ledlight

### DELETE

deletes instance

## /things/ledlights/uuid/state/ 

### PUT

allowed payloads:
```python
{
    "on": "false"
}

{
    "on": "true"
}
```

# Arduino Endpoints:

## address/uuid/state/

### GET

returns (not decided yet)

## address/uuid/0/

### PUT

Turns led light off

## address/uuid/1/

### PUT

Turns led light on

--------------------------------------------------------------------------------

# SPRINT

* [ARDUINO]+[THINGS] should be getstate and setstate.
* [RASP] Start hosting on RaspberryPi
* [ARDUINO] Add ping to ESP
* [ARDUINO]+[THINGS] Change endpoint "status" to "update"
* [ARDUINO] Fix getState in ESP
* [THINGS] maybe do something with the returned response from arduinos?
* [ARDUINO]+[THINGS] things should update states automatically in some time interval.
* [ARDUINO] Switch port to 89 on ESP.

* Setup control/analytics service that:
    * Bases control on analysis of logging data.
    * Has an interface which let you choose when and how to analyse/control data.
    * Can be set to control automatically
* Look into:
	* Safety for opening ports on local network
	* Static vs. dynamic IP's - Is it possible to host on dynamic IP? dns?
* Arduino and ESP should be more reliable:
	* Steps for uploading to arduino and ESP should be documented and work!
	* ESP should loop reconnection to wifi after power outage.
	* Arduino should continue loop its script after power outage.

## DOING

* Setup logging service that:
    * Periodically gather status data from things.
        - set up a background scheduler
    * Stores the data in (separate? time series?) database.
    * Has a graphics function (in template? trough api?).

## DONE

* [ARDUINO] All ESP-arduino pairs should be identified with the UUID generated when creating its thing.
* [SERVICE] Return response to things from communication
* [ARDUINO] Setup authentication in ESP (keep UUID secret)
    * Test opening up port on router to allow non local requests
* [API] Use SessionAuthentication
* Fix external power supply for ESP
* [THINGS] Set up a mock webserver to fake arduino response during testing
* [THINGS] Each app should have its own service and receiver file
