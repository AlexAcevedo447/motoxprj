//EDITAR REGISTROS
const editarConductor = (id) => {

    fetch("/motoxapp/editarCond/"+id)
}

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
<<<<<<< HEAD
            fetch("http://localhost:8000/motoxapp/eliminarCond/" + id)
=======
            fetch("http://localhost:8000/motoxapp/admin/eliminarCond/" + id)
>>>>>>> 654be4f0520b1e0f19bdc43385b92ceda64e467b
                .then(res => {
                    res.json()
                })
                .then(response => {
                    
                    Swal.fire(
                        'Registro borrado',
                        'success'
                    )
<<<<<<< HEAD
=======

>>>>>>> 654be4f0520b1e0f19bdc43385b92ceda64e467b
                    location.reload()
                })
            
        }
    })



}

<<<<<<< HEAD

=======
const llamarFormEditarPasajero = (id) => {
    console.log(id)

    fetch("http://localhost:8000/motoxapp/filtrarPas/"+id)
    .then(response =>response.json())
    .then(pasajero=>{
        console.log(pasajero[0])
    }).catch((err)=>{
        console.log(err)

    })
}
>>>>>>> 654be4f0520b1e0f19bdc43385b92ceda64e467b

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
<<<<<<< HEAD
            fetch("http://localhost:8000/motoxapp/eliminarPas/" + id)
=======
            fetch("http://localhost:8000/motoxapp/admin/eliminarPas/" + id)
>>>>>>> 654be4f0520b1e0f19bdc43385b92ceda64e467b
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