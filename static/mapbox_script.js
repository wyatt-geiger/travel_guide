// This is the script that creates the mapbox map on the page using user input

function loadData(city, country) {

    mapboxgl.accessToken = 'pk.eyJ1IjoibWFuZGlibGVjbGF3IiwiYSI6ImNrNmxpcWJ4MzBhamozZXBiZzVoNm11cmgifQ.lt7or9puZArJpANdrnIrUg';
    
    const mapboxClient = mapboxSdk({ accessToken: mapboxgl.accessToken });

    mapboxClient.geocoding
        .forwardGeocode({
            query: `${city}, ${country}`, // this is the 'formatted string' of the user input. This determines where the map centers itself
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

            // Adds a zoom control feature for the map
            const nav = new mapboxgl.NavigationControl()
            map.addControl(nav)
        });

}
