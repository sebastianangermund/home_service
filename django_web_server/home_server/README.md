api endpoints:

------------ ## /things/ledlights/

GET

-

POST

create a new ledlight thing. owner and id is set automatically

{
	"title": "some_title",
	"on": "false"
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

------------ ## /things/ledlights/uuid/status/ 

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
------------ ## /things/ledlights/uuid/state/

GET

example return
´
OBSOBSOBSOBS !
´
--------------------------------------------------------------------------------

SPRINT

* [API] Use SessionAuthentication
* [ARDUINO] Add ping on to ESP
* [ARDUINO] Fix getState in ESP 
* [ARDUINO] ESP should loop reconnection to wifi after power outage + arduino should loop its script too.
* [ARDUINO]+[THINGS] Change endpoint "status" to "update"
* Setup logging service that:
    * Periodically gather status data from things.
    * Stores the data in (separate? time series?) database.
    * Has a graphics function.
* Setup control/analytics service that:
    * Bases control on analysis of logging data.
    * Has an interface which let you choose when and how to analyse/control data.
    * Can be set to control automatically
* Look into:
	* Safety for opening ports on local network
	* Static vs. dynamic IP's - Is it possible to host on dynamic IP?
* Start hosting on RaspberryPi

DONE

* All ESP’s should be identified with the ID generated when creating its thing.
* Return response to things from communication
* Setup authentication in ESP (keep ID secret)
    * Test opening up port on router to allow non local requests

