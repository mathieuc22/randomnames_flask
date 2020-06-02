document.addEventListener('DOMContentLoaded', () => {
    document.getElementById("refresh").onClick = () => {
        // Initialize new request
        const request = new XMLHttpRequest();
        request.open('GET', '/refresh');

        // Callback function for when request completes
        request.onload = () => {
            document.querySelector('#CoolName').innerHTML = coolname;
        }

        return false;
    };

});
