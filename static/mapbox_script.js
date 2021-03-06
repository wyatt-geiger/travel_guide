// This is the script that creates the mapbox map on the page using user input

function loadData(city, state, country, yelpID, map_box_key) {

    mapboxgl.accessToken = map_box_key;
    
    const mapboxClient = mapboxSdk({ accessToken: mapboxgl.accessToken });

    mapboxClient.geocoding
        .forwardGeocode({
            query: `${city}, ${state}, ${country}`, // this is the 'formatted string' of the user input. This determines where the map centers itself
            autocomplete: false,
            limit: 1
        })
        .send()
        .then((response) => {
            if (
                !response ||
                !response.body ||
                !response.body.features ||
                !response.body.features.length
            ) {
                console.error('Invalid response:');
                console.error(response);
                return;
            }
            const feature = response.body.features[0];
    
            const map = new mapboxgl.Map({
                container: 'map',
                style: 'mapbox://styles/mapbox/streets-v11',
                center: feature.center,
                zoom: 10
            });
    
            // Create a marker and add it to the map.

            new mapboxgl.Marker().setLngLat(feature.center).addTo(map);

            // loop that handles yelp business map markers
            yelpID.forEach(element =>
            // adds map markers for all businesses that the yelp API returned
            new mapboxgl.Marker({color: "#FF0000"}).setLngLat([element[6], element[5]])
            .setPopup( // makes pop ups that appear when the business marker is clicked
                new mapboxgl.Popup({ offset: 25 }).setHTML(
                    `<h3>${element[0]}</h3><p>${element[2]}</p>`
                )
            )
            .addTo(map));

            // Adds a zoom control feature for the map
            const nav = new mapboxgl.NavigationControl()
            map.addControl(nav)
        });

}
