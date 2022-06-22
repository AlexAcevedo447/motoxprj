//EDITAR REGISTROS


const llamarFormEditarPasajero = (id) => {
    console.log(id)

    fetch("http://localhost:8000/motoxapp/filtrarCond/"+id)
    .then(response =>response.json())
    .then(conductor=>{
        console.log(conductor[0])
    }).catch((err)=>{
        console.log(err)

    })
}

//GUARDAR REGISTROS
const formularioGuardarPasajero = document.getElementById("guardarPas");
const formularioGuardarConductor = document.getElementById("guardarCond")

formularioGuardarConductor.addEventListener("submit",(e)=>{
    e.preventDefault()
    let formulario = new FormData(formularioGuardarConductor)
    fetch("/motoxapp/guardarCond", {
        method: "POST",
        body: formulario
    })
    .then(res => {
        formularioGuardarConductor.reset()
        location.reload()
    })
})


formularioGuardarPasajero.addEventListener("submit",(e)=>{
    e.preventDefault()
    let formulario = new FormData(formularioGuardarPasajero)
    fetch("/motoxapp/guardarPas", {
        method: "POST",
        body: formulario
    })
    .then(res => {
        formularioGuardarPasajero.reset()
        location.reload()
    })
})

//ELIMINAR REGISTROS
const eliminarConductor = (id) => {
    console.log(id)

    

    Swal.fire({
        title: '¿Estás seguro que quieres borrar el registro?',
        text: "No puedes revertir el cambio",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si'
    }).then((result) => {
        if (result.isConfirmed) {
            fetch("http://localhost:8000/motoxapp/eliminarCond/" + id)
                .then(res => {
                    res.json()
                })
                .then(response => {
                    
                    Swal.fire(
                        'Registro borrado',
                        'success'
                    )
                    location.reload()
                })
            
        }
    })



}


const eliminarPasajero = (id) => {
    console.log(id)
    Swal.fire({
        title: '¿Estás seguro que quieres borrar el registro?',
        text: "No puedes revertir el cambio",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si'
    }).then((result) => {
        if (result.isConfirmed) {
            fetch("http://localhost:8000/motoxapp/eliminarPas/" + id)
                .then(res => {
                    res.json()
                })
                .then(response => {
                    Swal.fire(
                        'Registro borrado',
                        'success'
                    )
                    location.reload()
                })
            
        }
    })

}