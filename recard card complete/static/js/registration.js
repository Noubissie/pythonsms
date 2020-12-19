
window.onchange = () => {
    let submit = document.getElementById("registration-submit-button");
    let fs_container = document.getElementById("tableset-prime-container");
    let noct = document.getElementById("number_of_class_thought"); // noct = number_of_class_thought
    let fdisb = document.getElementById("fall_down_input_subject_button");
    let teacher_name = document.getElementById('teacher_name');


    show_password_set = document.getElementById("password_set_visibility");
    user_password_set = document.getElementById("user_set_password");
    show_password_set.addEventListener('click', (e) => {

            if (user_password_set.type === 'text') {
                user_password_set.type = 'password';
                e.preventDefault();
            } else if (user_password_set.type === 'password') {
                user_password_set.type = 'text';
                e.preventDefault();
            }
        }
    );

    show_password_confirm = document.getElementById("password_confirm_visibility");
    user_password_confirm = document.getElementById("user_confirm_password");
    show_password_confirm.addEventListener('click', (e) => {

            if (user_password_confirm.type === 'text') {
                user_password_confirm.type = 'password';
            } else if (user_password_confirm.type === 'password') {
                user_password_confirm.type = 'text';
            }
        }
    );
let school_section = document.getElementById('school_section');
console.log(school_section.value);
if(school_section.value !== '') {
    school_section.style.backgroundColor ='white';
    fetch('/api/'+school_section.value).then(res => {
        return res.text();
    }).then(data => {
        data = JSON.parse(data);

        fdisb.addEventListener('click', (e) => {
                fs_container.style.display = 'block';
                fs_container.innerHTML = '';
                fs_container.style.width = '100%';
                if (school_section.value === '') {
                    school_section.style.backgroundColor = 'red';
                } else {

                    school_section.style.backgroundColor = 'white';

                    function creatField() {
                        for (let i = 1; i <= noct.value; i++) {
                            let tr_fieldset = document.createElement("tr");
                            tr_fieldset.id = 'fieldset_class_thought' + i;
                            let td = document.createElement('td');
                            td.innerHTML = 'class';
                            td.width = '50%';


                            let td_select_class = document.createElement('td');
                            td_select_class.width = '50%%';
                            let select = document.createElement('select');

                            select.name = 'class_th' + i;
                            select.id = 'class_th' + i;
                            tr_fieldset.appendChild(td);

                            let b = tr_fieldset.appendChild(td_select_class);
                            let a = b.appendChild(select);

                            Object.keys(data).forEach(key => {
                                let option = document.createElement('option');
                                option.innerHTML = key;
                                a.appendChild(option);
                                // data[key].forEach(opt => {
                                //     let option = document.createElement('option');
                                //     option.innerHTML = opt;
                                //     a.appendChild(option);
                                // })
                            });

                            let subject_button = document.createElement('button');
                            subject_button.type = 'button';
                            subject_button.id = 'subject_give_but' + i;
                            subject_button.innerHTML = '&plus;';
                            b.appendChild(subject_button);

                            let placement = document.createElement('td');
                            placement.id = 'placement' + i;
                            placement.width = '50%';

                            subject_button.addEventListener('click', (e) => {
                                placement.innerHTML = ``;
                                let select2 = document.createElement('select');

                                select2.multiple = true;
                                select2.required = true;
                                select2.name = 'subject_th' + i;
                                select2.id = 'subject_th' + i;
                                placement.appendChild(select2);

                                Object.keys(data).forEach(key => {
                                    if (key === select.value) {

                                        data[key].forEach(opt => {
                                            let option = document.createElement('option');
                                            option.innerHTML = opt;

                                            select2.appendChild(option);
                                        })
                                    }
                                });
                                e.preventDefault();
                            });


                            tr_fieldset.appendChild(placement);

                            fs_container.appendChild(tr_fieldset);
                        }

                    }


                    if (noct.value >= 1) {
                        creatField();
                    } else {
                        window.alert('number of subject most be greater than 0');
                        // location.reload();
                    }

                }
            }
        );
    }).catch(err => {
        console.log(err);
    });
}else {
    school_section.style.backgroundColor ='red';
}



    let pwd_confirm = document.getElementById('confirm password');
    let pwd_fs = document.getElementById('pwd_fs');
    let inconsitentcy = document.getElementById("inconsitentcy");
    pwd_confirm.addEventListener('click', (e) => {
        if (user_password_set.value !== user_password_confirm.value) {
            inconsitentcy.style.display = "block";
            e.preventDefault();
        } else {
            inconsitentcy.style.display = "none";
            // e.preventDefault();
        }
    });



};
     // <select  multiple name = 'subject_th${i}' id="subject_th${i}">
     //                            <option></option>
     //                            <option>physics</option>
     //                            <option>chemistry</option>
     //                            <option>biology</option>
     //                            <option>maths</option>
     //                            <option>computer science</option>
     //                            <option>A.maths</option>
     //                            <option>human biology</option>
     //                            <option>history</option>
     //                            <option>English language</option>
     //                            <option>English literature</option>
     //                    </select>