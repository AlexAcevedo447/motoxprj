const llamarFormEditarConductor = (id) => {
    console.log(id)
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
            fetch("http://localhost:8000/motoxapp/conductor/eliminar/" + id)
                .then(res => {
                    res.json()
                })
                .then(response => {
                    form.reset()
                    Swal.fire(
                        'Registro borrado',
                        'success'
                    )
                })
            
        }
    })



}

const llamarFormEditarPasajero = (id) => {
    console.log(id)
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
            fetch("http://localhost:8000/motoxapp/pasajero/eliminar/" + id)
                .then(res => {
                    res.json()
                })
                .then(response => {
                    Swal.fire(
                        'Registro borrado',
                        'success'
                    )
                })
            
        }
    })

}