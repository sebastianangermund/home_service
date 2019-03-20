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

edit a specific ledlight

GET

-

PUT

-

PATCH

-

DELETE

------------ ## /things/ledlights/uuid/status/

PUT

{
	"on": "false"
}

--------------------------------------------------------------------------------

SPRINT

* Add ping to ESP
* Fix getState in ESP 
* ESP should loop reconnection to wifi after power outage + arduino should loop its script too.
* Setup logging service that:
    * Periodically gather status data from things.
    * Stores the data in (separate? time series?) database.
    * Has a graphics function.
* Setup control/analytics service that:
    * Bases control on analysis of logging data.
    * Has an interface which let you choose when and how to analyse/control data.
    * Can be set to control automatically
* All ESP’s should be identified with the ID generated when creating its thing.

DONE

* Return response to things from communication
* Setup authentication in ESP (keep ID secret)
    * Open up port on router to allow non local requests (test)







