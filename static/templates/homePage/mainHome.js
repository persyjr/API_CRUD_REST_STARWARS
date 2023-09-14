//import { people } from "/static/js/restApi.js";

const baseUrl = "https://www.swapi.tech/api/";

window.addEventListener('DOMContentLoaded', async ()=> {
    
    const query =await getQueryPeople()
    render(query,"user")

    const query2 =await getQueryPlanets()
    render(query2,"planet")

    const query3 =await getQuerySpecies()
    render(query3,"species")

    const query4 =await getQueryStarships()
    render(query4,"starships")
    const query5 =await getQueryVehicles()
    render(query5,"vehicles")
});

function render(users,tipe) {
    const userList=document.querySelector(`#${tipe}List`)
    //console.log(userList)
    userList.innerHTML=''
    
    users.forEach(user => {
        const userItem = document.createElement('li')
        userItem.classList='list-group-item my-2'
        userItem.innerHTML = `
            <img src="${user.img}" style="width:150px;"></img>
            <header class="d-flex justify-content-around align-items-center">
                <h5 style="width:60%;">${user.name}</h5>
                
                <div  style="width:30%;">
                    <p>${user.uid}</p>
                    
                    
                </div>
                <div style="width:20%;">
                    <button class="btn btnDelete btn-danger btn-sm" style="width:50%;"><i class="fa fa-close" style="width:36px;"></i></button>
                    <button class="btn btnEdit btn-primary btn-sm" style="width:50%;"><i class="fa fa-edit" style="width:36px;"></i></button>
                </div>
            <header>
            
        `
        const btnDelete = userItem.querySelector('.btnDelete')
        btnDelete.addEventListener('click', async ()=> {
           const response = await fetch(`/api/users/${user.id}`,{
                method:"DELETE"
            })
            const data = await response.json()
            users=users.filter(user => user.id != data.id)
            renderUser(users)
        })
        
        const btnEdit = userItem.querySelector('.btnEdit')
        btnEdit.addEventListener('click',async e=>{
            const response = await fetch(`/api/users/${user.id}`)
            const data =await response.json()
            userForm['username'].value=data.username;
            userForm['especie'].value=data.especie;
            userForm['planeta'].value=data.planeta;
            edditing=true
            userId=data.id
        })
        
        userList.append(userItem)
        
    })
    
}

getQueryPeople = async () => {
    //Declaro una función call back para ingresar parametros numero de pagina y limite de elementos
    // Ejemplo de peticion https://www.swapi.tech/api/people?limit=20&page=2
    //ingreso imagenes de toda la pgina.
    try {
        const res = await fetch(
            `${baseUrl}people/?limit=${100}&page=${0}`
        );
        if (res.ok) {
            //const datapeople = await res.json()
            //data= datapeople.results
           
            //return data
            let resp = await res.json();
            resp.results = resp.results.map((person) => {
                return {
                    img: `https://starwars-visualguide.com/assets/img/characters/${person.uid}.jpg`,
                    ...person,
                };
            });
            return resp.results;
            
        }
    }catch (error) {
            console.error("Error en la api", error);
            return [];
        }
    }

getQueryPlanets = async () => {
//Declaro una función call back para ingresar parametros numero de pagina y limite de elementos
// Ejemplo de peticion https://www.swapi.tech/api/people?limit=20&page=2
//ingreso imagenes de toda la pgina.
try {
    const res = await fetch(
        `${baseUrl}planets/?limit=${100}&page=${0}`
    );
    if (res.ok) {
        //const datapeople = await res.json()
        //data= datapeople.results
        
        //return data
        let resp = await res.json();
        resp.results = resp.results.map((planet) => {
            return {
                img: `https://starwars-visualguide.com/assets/img/planets/${planet.uid}.jpg`,
                ...planet,
            };
        });
        return resp.results;
        
    }
}catch (error) {
        console.error("Error en la api", error);
        return [];
    }
}

getQuerySpecies = async () => {
    //Declaro una función call back para ingresar parametros numero de pagina y limite de elementos
    // Ejemplo de peticion https://www.swapi.tech/api/people?limit=20&page=2
    //ingreso imagenes de toda la pgina.
    try {
        const res = await fetch(
            `${baseUrl}species/?limit=${100}&page=${0}`
        );
        if (res.ok) {
            //const datapeople = await res.json()
            //data= datapeople.results
            
            //return data
            let resp = await res.json();
            resp.results = resp.results.map((specie) => {
                return {
                    img: `https://starwars-visualguide.com/assets/img/species/${specie.uid}.jpg`,
                    ...specie,
                };
            });
            return resp.results;
            
        }
    }catch (error) {
            console.error("Error en la api", error);
            return [];
        }
    }
    
    getQueryStarships = async () => {
        //Declaro una función call back para ingresar parametros numero de pagina y limite de elementos
        // Ejemplo de peticion https://www.swapi.tech/api/people?limit=20&page=2
        //ingreso imagenes de toda la pgina.
        try {
            const res = await fetch(
                `${baseUrl}starships/?limit=${100}&page=${0}`
            );
            if (res.ok) {
                //const datapeople = await res.json()
                //data= datapeople.results
                
                //return data
                let resp = await res.json();
                resp.results = resp.results.map((starship) => {
                    return {
                        img: `https://starwars-visualguide.com/assets/img/starships/${starship.uid}.jpg`,
                        ...starship,
                    };
                });
                return resp.results;
                
            }
        }catch (error) {
                console.error("Error en la api", error);
                return [];
            }
        }
        

        getQueryVehicles = async () => {
            //Declaro una función call back para ingresar parametros numero de pagina y limite de elementos
            // Ejemplo de peticion https://www.swapi.tech/api/people?limit=20&page=2
            //ingreso imagenes de toda la pgina.
            try {
                const res = await fetch(
                    `${baseUrl}vehicles/?limit=${100}&page=${0}`
                );
                if (res.ok) {
                    //const datapeople = await res.json()
                    //data= datapeople.results
                    
                    //return data
                    let resp = await res.json();
                    resp.results = resp.results.map((vehicle) => {
                        return {
                            img: `https://starwars-visualguide.com/assets/img/vehicles/${vehicle.uid}.jpg`,
                            ...vehicle,
                        };
                    });
                    return resp.results;
                    
                }
            }catch (error) {
                    console.error("Error en la api", error);
                    return [];
                }
            }