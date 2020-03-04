# hartija

RSS reader for drobilica


##Todo
- `make run` to run project
- `make cache` to make cache 
- `make clean` cleans all data and generates new one
- Wheather info on the right side openweathermap https://openweathermap.org/ 
- internalization - language switcher i18n ( on lower left side)
- On click they should open with short content - 500chars
- There should be a tags ( #gaming, #dev, #news, #local_news, #devops, #tech)   
- You should be able to add new rss feeds to
- read feed list from yaml app/data/rss-feeds.yaml  --- done 
- Terminal todo app
- generate right menu from YAML keys and check if there is data for that tab and if there is not then make data and render that page 

## RSS Feeder Sites
Site lists are located in app/data/rss-feeds.yaml



### API endpoints


#### GET

Get info on what news are available
`curl -X GET localhost:5000/api/cache`


Get info when cache is created
`curl -X GET localhost:5000/api/get_cache_info/`


#### Set
Make cache for individual category
`curl -X GET localhost:5000/api/cache/games`

Make cache for all 
`curl -X GET localhost:5000/api/generate_cache/`