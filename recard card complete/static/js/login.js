
window.onload = ()=> {
    let c = document.getElementById('login-container_id');
    let a = document.getElementById('nav_anchor_login');
    let b = document.getElementById('login');
    let g = document.getElementById('general_nav_bar');
    let m = document.getElementById('main_heading');
    let nav_container = document.getElementById('nav_container');

    b.style.left = (window.innerWidth - (0.4) * window.innerWidth) / 2 + "px";
    // g.style.width = window.innerWidth + "px";
    // m.style.width = window.innerWidth + "px";
    // c.style.width = window.innerwidth + "px";
    // c.style.height = window.innerHeight + "px";
    // nav_container.style.width = window.innerWidth + "px";


    show_password = document.getElementById("password-visibility");
    user_password = document.getElementById("user_password");
    show_password.addEventListener('click', (e) => {

            if (user_password.type == 'text') {
                user_password.type = 'password';
            } else if (user_password.type == 'password') {
                user_password.type = 'text';
            }
        }
    );


    window.onresize = () => {
        b.style.left = (window.innerWidth - (0.4) * window.innerWidth) / 2 + "px";
        // g.style.width = window.innerWidth + "px";
        // m.style.width = window.innerWidth + "px";
        // c.style.width = window.innerWidth + "px";
        // c.style.height = window.innerHeight + "px";
        // nav_container.style.width = window.innerWidth + "px";
    }
};