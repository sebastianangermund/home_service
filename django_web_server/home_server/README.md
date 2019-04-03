# Development Environment

### Mock arduino response

With DEBUG=True you can run the python web server locatet in the folder one level up with the name "mock_things".

## Setup things

### Using Mock webserver

Either in Django admin or trough the API documentet below: Create a LedLight with any local IP (192.168.x.x) and let the status be "-".
When you create the LedLight object, an object from analytics.models.LedLightData will be created automatically, with field active=False. Also a csv file will be automatically created as home_server/data_files/ledlights/<pk>.csv.
If you now change the LedLight state (either trough admin or API) to either "on" or "off", the LedLightData object will automatically changed to have field active=True. And if a LedLightData object is active, then its csv file will be automatically populated with (timestamp, state)-rows periodically.

### Using Arduino

Same as above with some exceptions:

* Create an object without address. Get the arduino going and give it the uuid generated as the LedLight objects uuid.
* Make sure to note the arduino local IP and port number. Update the LedLight object with these.
* Either set DEBUG = False in settings, or overwrite DEBUG as True in things.models.

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

## /uuid/

Returns greeting and uuid in text/html format.

## /uuid/get-state/

returns "ON" or "OFF" in text/html format.

## /uuid/set-state=0/

Turns led light off.

## /uuid/set-state=1/

Turns led light on.

--------------------------------------------------------------------------------

# SPRINT

## TODO

* [RASP] Fix RaspberryPi compability (docker?)
* [ARDUINO]+[THINGS] Change endpoint "status" to "update"
* [ARDUINO] Fix getState in ESP
* [THINGS] maybe do something with the returned response from arduinos?
* [THINGS] Handle other cases than 200 in analytics.models.write_data_point
* [ARDUINO]+[THINGS] LedLight.get_state() : 
    - response message from ESP8266WebServer must be extracted (use print in save method)
    - ESP8266WebServer has status code messages. extract this and raise if not 200.
    - catch exception that is reised when no response is given.

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
* Setup logging service that:
    * Periodically gather status data from things.
        - set up a background scheduler
    * Stores the data in (separate? time series?) database.
    * Has a graphics function (in template? trough api?).

## DOING

* [ENV] Put project in docker container
    - Debian? Ubuntu?
    - Set up a cron job that can run manage commands periodically

* [THINGS] analytic things should update states automatically in some time interval (if status is active)
    - create manage command for scheduler tasks and run via cron jobs

## DONE

* [ARDUINO]+[THINGS] should be getstate and setstate.
* [ARDUINO] All ESP-arduino pairs should be identified with the UUID generated when creating its thing.
* [SERVICE] Return response to things from communication
* [ARDUINO] Setup authentication in ESP (keep UUID secret)
    * Test opening up port on router to allow non local requests
* [API] Use SessionAuthentication
* Fix external power supply for ESP
* [THINGS] Set up a mock webserver to fake arduino response during testing
* [THINGS] Each app should have its own service and receiver file
* [THINGS] A data file should be added to analytics automatically when a led is created
    - Add a field that is automatically put to "active" when LedLigh changes from state "-" to either "on" or "off"
* [ARDUINO] Add ping to ESP
