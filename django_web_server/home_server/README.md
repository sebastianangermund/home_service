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
