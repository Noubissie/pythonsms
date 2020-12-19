
let today = new Date();
let dd = today.getDate();
let mm = today.getMonth()+1;
let yyyy = today.getFullYear()-9
today = yyyy+'-'+mm+'-'+dd;
let admin_nav =document.getElementById('admin_nav_div');

// anchor identifiers
let school_info = document.getElementById('school_info');
let staff_info =document.getElementById('staff_info');
let student_info = document.getElementById('student_info');
let themes_info = document.getElementById('themes_info');
let community_info = document.getElementById('community-info')

// various control pages
let school_information = document.getElementById('school_information');
let staff_information =document.getElementById('staff_information');
let student_information = document.getElementById('student_information');
let community_information = document.getElementById('community');
let themes = document.getElementById('themes');
let fix_list_size = document.getElementById('size_controller');

// FIX THE WINDOW SIZE SO THAT ELEMENTS CAN GET TO FIT THE SCREEN OF A PHONE, MACCBOOK AND PC
// console.log(fix_list_size);
if(window.innerWidth >=1100){
    fix_list_size.style.fontSize = '100%'
}else{
    fix_list_size.style.fontSize = '50%';
}
window.onresize = ()=>{
    if(window.innerWidth >=1100){
    fix_list_size.style.fontSize = '100%'
}else{
    fix_list_size.style.fontSize = '50%';
}
}
// each window size
// let sizes = function(){
  // admin_nav.style.height = String(window.innerHeight) + 'px';
  //   admin_nav.style.width = String(0.2 * window.innerWidth) + 'px';
  //   school_information.style.height = String(window.innerHeight) + 'px';
  //   staff_information.style.height = String(window.innerHeight) + 'px';
  //   student_information.style.height = String(window.innerHeight) + 'px';
  //   themes.style.height = String(window.innerHeight) + 'px';
// };
// sizes();

// window.onresize= ()=>
// {
    // admin_nav.style.height = String(window.innerHeight) + 'px';
    // admin_nav.style.width = String(0.2 * window.innerWidth) + 'px';
    // school_information.style.height = String(window.innerHeight) + 'px';
    // staff_information.style.height = String(window.innerHeight) + 'px';
    // student_information.style.height = String(window.innerHeight) + 'px';
    // themes.style.height = String(window.innerHeight) + 'px';
// };

let stopito = (e)=>{
    e.preventDefault()
};
school_info.addEventListener('click',stopito);
student_info.addEventListener('click',stopito);
staff_info.addEventListener('click',stopito);
themes_info.addEventListener('click',stopito);
community_info.addEventListener('click',stopito);
school_info.onmouseover = ()=> {
    school_information.style.display = 'block';
    staff_information.style.display = '';
    student_information.style.display = '';
    themes.style.display = '';
    community_information.style.display ='';

};
staff_info.onmouseover = ()=> {
    staff_information.style.display = 'block';
    school_information.style.display = '';
    student_information.style.display = '';
    themes.style.display = '';
    community_information.style.display ='';
};
student_info.onmouseover = () =>{
    school_information.style.display = '';
    staff_information.style.display = '';
    student_information.style.display = 'block';
    themes.style.display = '';
    community_information.style.display ='';
};
themes_info.onmouseover = ()=>{
    school_information.style.display = '';
    staff_information.style.display = '';
    student_information.style.display = '';
    themes.style.display = 'block';
    community_information.style.display ='';
};
community_info.onmouseover = ()=>{
    school_information.style.display = '';
    staff_information.style.display = '';
    student_information.style.display = '';
    themes.style.display = '';
    community_information.style.display ='block';
};

let change_background_color =document.getElementById('change-background-color');
let body_object = document.querySelector('body');
document.addEventListener('onchange',(e)=>{
    console.log(change_background_color.value);
    body_color.style.backgroundColor = change_background_objecct.value;
});

// make sure neither school section or school year are zero


// fall down menu for school information make a fall dowm menu to input the subjects athought and the class of the subject


    let creat_school_info_about_classes_and_subject = function () {
        let noc = document.getElementById('number_of_class');



        let class_and_subject_falldown = document.getElementById('class_and_subject_falldown');
        let class_and_subject_thought = document.getElementById('class_and_subject_thought');


        class_and_subject_falldown.addEventListener('click', (e) => {
            let school_section = document.getElementById('school-section');
            let school_year = document.getElementById('school_year');
            let number_of_class = noc.value;
            console.log(school_section.value);
            console.log(school_year.value);
            if(school_year.value ==='' || school_section.value === '' ) {
                alert('fill in the information');
                // window.location.reload()
            }
            else{
            let castinner = class_and_subject_thought.innerHTML = `
                    <table border="solid red" style="width: 100%; text-align: center">
                        <tr>
                            <td>number</td>
                            <td><label style="width: 90%" for="class" >class</label></td>
                            <td><label style="width: 90%" for="subject_thought" >subjects thought</label></td>
                            <td><label style="width: 90%" for="class_file_subject" >subjects thought file</label></td>
                        </tr>`;

            for (let i = 1; i <= parseInt(number_of_class); i++) {

                let ct = class_and_subject_thought.innerHTML = castinner + `    
                        <tr>
                            <td>${i}</td>
                            <td><input style="width: 90%;margin: 0px 0px 0px 0px;" type="text" id="class${i}" name="class${i}"></td>
                            <td><textarea style="width: 90%;margin: 0px 10px 0px 0px;" id="subjects_thought${i}" name="subjects_thought${i}"></textarea></td>
                            <td><input type="file" style="width: 90%;margin: 0px 10px 0px 0px;" id="class${i}_file_subject" name="class${i}_file_subject" ></td>
                        </tr>
                     
                    `;
                castinner = ct
            }
            class_and_subject_thought.innerHTML = class_and_subject_thought.innerHTML +`</table>`
                };
            e.preventDefault();
        });

    };
    creat_school_info_about_classes_and_subject();


//fall down menu for staff information

// if(school_section == ''|| school_year==''){
//     alert('fill in the information');
// }
    let creat_staff_and_rank = function () {
        let noc = document.getElementById('number_of_staffs');


            console.log();

            let staff_and_rank_falldown = document.getElementById('staff_and_rank_falldown');
            let staff_and_rank = document.getElementById('staff_and_rank');


            staff_and_rank_falldown.addEventListener('click', (e) => {
                let staff_school_section = document.getElementById('staff_school_section');
                let staff_school_year = document.getElementById('staff_school_year');
                let number_of_class = noc.value;
                console.log(staff_school_section.value);
                console.log(staff_school_year.value);
                if (staff_school_section.value == '' || staff_school_year.value == '') {
                    alert('fill in the information');
                } else {
                    let castinner = staff_and_rank.innerHTML = `
                    <table border="solid red" style="width: 100%; text-align: center">
                        <tr>
                            <td>number</td>
                            <td>staff name</td>
                            <td>rank</td>
                        </tr>`;
                    console.log(number_of_class);
                    for (let i = 1; i <= parseInt(number_of_class); i++) {

                        let ct = staff_and_rank.innerHTML = castinner + `    
                    
                     <tr>
                        <td>${i}</td>
                         <td>
                            <input style="width: 90%;margin: 0px 0px 0px 0px;" type="text" id="staff_name${i}" name="staff_name${i}"> 
                         </td>
    
                         <td>
                             <input type="text" style="width: 90%;margin: 0px 0px 0px 0px;" id="rank${i}" name="rank${i}">
                         </td>
                     </tr>
                    `;
                        castinner = ct
                    }
                    staff_and_rank.innerHTML = staff_and_rank.innerHTML + `</table>`;
                }
                e.preventDefault()
            })
        };

    creat_staff_and_rank();

//create student section, name, class, guidant

// if(school_section == ''|| school_year==''){
//     alert('fill in the information');
// }
    let creat_student_info = function () {
        let noc = document.getElementById('number_of_students');


        console.log();

        let student_info_falldown = document.getElementById('student_info_falldown');
        let student_info_div_block = document.getElementById('student_info_div_block');


        student_info_falldown.addEventListener('click', (e) => {
            let number_of_class = noc.value;
            let student_school_section = document.getElementById('student_school_section');
            let student_school_year = document.getElementById('student_school_year');
            if(student_school_section.value == ''|| student_school_year.value ==''){
    alert('fill in the information');
}
            else {
            let castinner = student_info_div_block.innerHTML =`
                    <table border="solid red" style="width: 100%; text-align: center">
                        <tr>
                            <td>number</td>
                            <td>student name</td>
                            <td>student class</td>
                            <td>date of birth</td>
                            <td>student age</td>
                            <td>sex</td>
                            <td>guidant</td>
                        </tr>`;
            for (let i = 1; i <= parseInt(number_of_class); i++) {

                let ct = student_info_div_block.innerHTML = castinner + `    
                    <tr">
                        <td>${i}</td>
                         <td>
                            <input style="width: 90%;margin: 0px 0px 0px 0px;" type="text" id="student_name${i}" name="student_name${i}">
                         </td>
    
                         <td>
                             <input type="text" style="width: 90%;margin: 0px 0px 0px 0px;" id="student_class${i}" name="student_class${i}">
                         </td>
                         <td>
                             <input type="date" max="${today}" style="width: 90%;margin: 0px 0px 0px 0px;" id="student_date_of_birth${i}" name="student_date_of_birth${i}">
                         </td>
                         <td>
                            <input type="number" style="width: 90%;margin: 0px 0px 0px 0px;" id="student_age${i}" name="student_age${i}">
                         </td>
                         <td>
                            <select style="width: 90%;margin: 0px 0px 0px 0px;" id="student_sex${i}" name="student_sex${i}">
                                <option></option>
                                <option>M</option>
                                <option>F</option>
                            </select>
                         </td>
                         <td>
                             <input type="text" style="width: 90%;margin: 0px 0px 0px 0px;" id="guidant${i}" name="guidant${i}">
                         </td>
                     </tr>
                   </div> `;
                castinner = ct
            }
                student_info_div_block.innerHTML = student_info_div_block.innerHTML +`</table>`
            }

            e.preventDefault()
        });

    };

    creat_student_info();

// window.onresize = ()=>{
//     body_object.style.height =String(window.innerHeight)+'px';
//     body_object.style.width = String(window.innerWidth)+'px';
// };
// body_object.style.height =String(window.innerHeight)+'px';
// body_object.style.width = String(window.innerWidth)+'px';

