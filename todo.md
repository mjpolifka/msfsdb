
### /

- shouldn't this be the list of aircraft?  
- otherwise, put a link to /aircraft I guess  
- if this isn't the list of aircraft, it'll have to be some kind of home page  


### /aircraft

- ~~display list of all aircraft, maybe in alphabetical order (it is)~~
- ~~display a list of categories each plane is in~~
- clicking on one brings you to /aircraft/aircraft_name
- clicking any category brings you to the category list
- maybe a way to save favorites



### /aircraft/aircraft_name

- display details about the aircraft  
- maybe some javascript on this page could let you modify it?  
  - otherwise, add /aircraft/edit/aircraft_name  


### /aircraft/add

- ~~input boxes for aircraft properties and submit~~
- ~~saves to database~~
- ~~able to add from existing categories~~
  - ~~show a list with checkboxes for all existing categories~~
  - ~~add any categories which are checked~~
- don't allow duplicate "name"


### /aircraft/delete

- ~~show the list of aircraft, with links to delete confirmations~~
- confirmation page displays the aircraft details, including the id since there can be dupes
- ~~confirming deletes from database~~


## (we sort of just need to duplicate everything for categories)

### /category

- ~~copy /aircraft~~
- checkboxes next to each category, with a "filter" button
  - after selecting multiple categories and pressing filter, takes you to a view of all aircraft in all categories
  - maybe a way to exclude a category


### /category/category_name

- copy /aircraft/aircraft_name


### /category/add

- ~~copy /aircraft/add~~
- don't allow duplicate "name"

### /category/delete

- ~~copy /aircraft/delete~~


### Other

- add a way to make custom lists; maybe can use categories
- implement login for custom lists and favorites


Models:

https://flask-sqlalchemy.readthedocs.io/en/stable/
https://flask-sqlalchemy.readthedocs.io/en/stable/models/

Aircraft
    id
    name
    description
    categories (foreign key)
    top_speed?
    cruise_speed?
Category
    id
    name
    description
    aircraft (foreign key)
Category_Index (table, not model)
    aircraft_id (Aircraft.id)
    category_id (Category.id)
