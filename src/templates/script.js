function get_data(){  
    var ip = document.getElementById("ip_value").value  
    var port = document.getElementById("port_value").value
    var token = document.getElementById("token_value").value
    return eel.camera_params(ip, port, token)
}