let staff  = document.getElementById('fall_staff_button');
let delete_staff = document.getElementById('delete_staff');
let student = document.getElementById('fall_student_button');
let delete_student = document.getElementById('delete_student');
let number_of_staff_to_delete = document.getElementById('number_of_staff_to_delete');
let number_of_student_to_delete = document.getElementById('number_of_student_to_delete');
staff.onmouseover = (e)=>{
    e.preventDefault();
    delete_staff.style.display = 'block';
    delete_student.style.display = '';
};

student.onmouseover = (e)=>{
    e.preventDefault();
    delete_student.style.display = 'block';
    delete_staff.style.display = '';
};
