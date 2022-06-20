const llamarFormEditarConductor = (id) => {
    console.log(id)

    fetch("http://localhost:8000/motoxapp/filtrarCond/"+id)
    .then(response =>response.json())
    .then(conductor=>{
        console.log(conductor[0])
    }).catch((err)=>{
        console.log(err)

    })
}

const eliminarConductor = (id) => {
    var form = document.getElementById("guardarCond")
    // console.log(id)

    

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
            fetch("http://localhost:8000/motoxapp/admin/eliminarCond/" + id)
                .then(res => {
                    res.json()
                })
                .then(response => {
                    form.reset()
                    Swal.fire(
                        'Registro borrado',
                        'success'
                    )

                    location.reload()
                })
            
        }
    })



}

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
            fetch("http://localhost:8000/motoxapp/admin/eliminarPas/" + id)
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