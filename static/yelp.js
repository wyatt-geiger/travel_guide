

// collect data from the API
let url = 'https://api.yelp.com/v3/businesses/search'

let bus_name = document.querySelector('#name')
let location = document.querySelector('#location')
let Radius = document.querySelector('#Radius')
let limit = document.querySelector('#limit')
let tableData = document.querySelector('#tabdata')   

//do table to show all the data side by side 



fetch(url) // fetching the url and returns a promise
    .then( (res) => res.json())
        .then( (businesses) => {
        let businessesdata = businesses // this will pull the api code that will display on the table 
        //get specific data value from API
        let term =  businen_names.name


                    // naming this term 
      
                        businen_names =rating
                        businen_names['location']['address1'],
                        businen_names['location']['city'],
                        businen_names['phone'],
                        businen_names['review_count'],
                        businen_names['coordinates']['latitude']



                       
              
                        
        

                        let tableterm = document.createElement('tr')
                        let tablelocation = document.createElement('td')
                        let tablecity = document.createElement('td')
                        let tabletelephone = document.createElement('td')
                        let tableRating = document.createElement('td')
                        let tableDistance = document.createElement('td')
                
                
                        // add them to the table 
                        tableterm.appendChild(tableterm)
                        tablelocation.appendChild(tablelocation)
                        tablecity.appendChild(tablecity)
                        tabletelephone.appendChild(tabletelephone)
                        tableRating.appendChild(tableRating) 
                        tableDistance.appendChild(tableDistance)
                
                        // put the  api data in table
                        tableterm.innerHTML = term
                        tablelocation.innerHTML = location
                        tablecity.innerHTML = 
                        tabletelephone.innerHTML =
                       
                
                            
                            
                            
                      
            
        }) // error handler if it occurs/ a promise is rejected
        .catch((error) => { //deals with errors  
            console.log(error);
       
        })

            







            