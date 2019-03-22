* api endpoints:

------------ ## /things/ledlights/

GET

-

POST

create a new ledlight thing.

payload should look like:
{
	"title": "some_title",
}

------------ ## /things/ledlights/uuid/

GET

ping a specific ledlight

returns:
´
status 200
´

-

DELETE

deletes instance

------------ ## /things/ledlights/uuid/state/ 

PUT

allowed payloads:
´
{
	"on": "false"
}

{
	"on": "true"
}
´

* arduino endpoints:

------------ ## address/uuid/state/

GET

returns

------------ ## address/uuid/0/

PUT

------------ ## address/uuid/1/

PUT

--------------------------------------------------------------------------------

SPRINT

* [ARDUINO]+[THINGS] should be getstate and setstate.
* [RASP] Start hosting on RaspberryPi
* [ARDUINO] Add ping to ESP
* [ARDUINO]+[THINGS] Change endpoint "status" to "update"
* [ARDUINO] Add ping to ESP
* [ARDUINO] Fix getState in ESP
* [THINGS] maybe do something with the returned text from arduinos?
* [ARDUINO]+[THINGS] things should update states automatically in some time interval.

* Setup control/analytics service that:
    * Bases control on analysis of logging data.
    * Has an interface which let you choose when and how to analyse/control data.
    * Can be set to control automatically
* Look into:
	* Safety for opening ports on local network
	* Static vs. dynamic IP's - Is it possible to host on dynamic IP?
* Arduino and ESP should be more reliable:
	* ESP should loop reconnection to wifi after power outage.
	* Arduino should continue loop its script after power outage.
	* Fix external power supply for ESP

DOING

* Setup logging service that:
    * Periodically gather status data from things.
    * Stores the data in (separate? time series?) database.
    * Has a graphics function.

DONE

* [ARDUINO] All ESP’s should be identified with the ID generated when creating its thing.
* [SERVICE] Return response to things from communication
* [ARDUINO] Setup authentication in ESP (keep ID secret)
    * Test opening up port on router to allow non local requests
* [API] Use SessionAuthentication
