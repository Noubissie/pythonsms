
window.onload = ()=> {

    let admin_nav = document.getElementById('admin_nav_div');

// anchor identifiers
    let school_info = document.getElementById('school_info');
    let staff_info = document.getElementById('staff_info');
    let student_info = document.getElementById('student_info');
    let themes_info = document.getElementById('themes_info');
    let community_info = document.getElementById('community-info')

// various control pages
    let school_information = document.getElementById('school_information');
    let staff_information = document.getElementById('staff_information');
    let student_information = document.getElementById('student_information');
    let community_information = document.getElementById('community');
    let themes = document.getElementById('themes');
    let fix_list_size = document.getElementById('size_controller');

// FIX THE WINDOW SIZE SO THAT ELEMENTS CAN GET TO FIT THE SCREEN OF A PHONE, MACCBOOK AND PC

    if (window.innerWidth >= 1100) {
        fix_list_size.style.fontSize = '100%'
    } else {
        fix_list_size.style.fontSize = '50%';
    }
    window.onresize = () => {
        if (window.innerWidth >= 1100) {
            fix_list_size.style.fontSize = '100%'
        } else {
            fix_list_size.style.fontSize = '50%';
        }
    };

    let stopito = (e) => {
        e.preventDefault()
    };
    school_info.addEventListener('click', stopito);
    student_info.addEventListener('click', stopito);
    staff_info.addEventListener('click', stopito);
    themes_info.addEventListener('click', stopito);
    community_info.addEventListener('click', stopito);
    school_info.onmouseover = () => {
        school_information.style.display = 'block';
        staff_information.style.display = '';
        student_information.style.display = '';
        themes.style.display = '';
        // community_information.style.display = '';

    };
    staff_info.onmouseover = () => {
        staff_information.style.display = 'block';
        school_information.style.display = '';
        student_information.style.display = '';
        themes.style.display = '';
        // community_information.style.display = '';
    };
    student_info.onmouseover = () => {
        school_information.style.display = '';
        staff_information.style.display = '';
        student_information.style.display = 'block';
        themes.style.display = '';
        // community_information.style.display = '';
    };
    themes_info.onmouseover = () => {
        school_information.style.display = '';
        staff_information.style.display = '';
        student_information.style.display = '';
        themes.style.display = 'block';
        // community_information.style.display = '';
    };
    community_info.onmouseover = () => {
        school_information.style.display = '';
        staff_information.style.display = '';
        student_information.style.display = '';
        themes.style.display = '';
        // community_information.style.display = 'block';
    };
}