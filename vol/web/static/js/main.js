function myFunction() {
    alert("Hello from a static file!");
}

function trogleDrawer() {
    const drawer = document.getElementById("my-drawer")
    console.log(drawer.checked)
    drawer.checked = !drawer.checked
    // alert(drawer.checked)
}