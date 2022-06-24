function get_data() {
    var ip = document.getElementById("ip_value").value
    var port = document.getElementById("port_value").value
    var user = document.getElementById("user_value").value + ':' + document.getElementById("pass_value").value + ':'
    var password = document.getElementById("user_value").value + ':' + document.getElementById("pass_value").value + ':'
    
    return eel.InitialScreenHandler.camera_params(ip, port, user, password);
    
}