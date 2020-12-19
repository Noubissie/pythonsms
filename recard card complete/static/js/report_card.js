fs_container = document.getElementById("fieldset-prime-container");
                noct = document.getElementById("number_of_class_thought"); // noct = number_of_class_thought
                fdisb = document.getElementById("fall_down_input_subject_button");

                teacher_name = document.getElementById('teacher_name');


                show_password_set = document.getElementById("password_set_visibility");
                user_password_set = document.getElementById("user_set_password");
                show_password_set.addEventListener('click',(e)=>
                {

                    if(user_password_set.type === 'text'){

                        user_password_set.type = 'password';
                        }

                    else if(user_password_set.type === 'password'){
                        user_password_set.type = 'text';

                    }
                    e.preventDefault();
                    }

                );

                show_password_confirm = document.getElementById("password_confirm_visibility");
                user_password_confirm = document.getElementById("user_confirm_password");
                show_password_confirm.addEventListener('click',(e)=>
                    {

                    if(user_password_confirm.type === 'text'){
                        user_password_confirm.type = 'password';}

                    else if(user_password_confirm.type === 'password'){
                        user_password_confirm.type = 'text';
                    }
                    e.preventDefault();
                    }
                );


                fdisb.addEventListener('click', (e) => {
                    let a = teacher_name.value;
                    fs_container.style.display = 'block';
                    fs_container.innerHTML = '';
                    function creatField(){
                        for (let i = 1; i <= noct.value; i++) {

                            // let fs_c = fs_container.innerHTML = fs_container.innerHTML + `

                            fs_container.innerHTML = fs_container.innerHTML + `
                            <fieldset class="fs2" id='fieldset_class_thought${i}'>
                                <legend class='legend'>

                                    <select name='class_th${i}' id="class_th${i}" class="registration_input">
                                        <option>class thought</option>
                                        {% for j in school_info %}
                                            <option>{{ j.classs }}
                                        {% endfor %}
                                    </select>
                                <button type="submit" id="test${i}" >&plus;</button>
                                </legend>
                                <label for="subject_thought" class="label">subjects thought<br>
                                    <select  multiple name = 'subject_th${i}' id="subject_th${i}" class="registration_input" >
                                            <option> </option>

                                    </select>
                                </label>
                            </fieldset>`;

                            // e.preventDefault();
                        }


                    }
                if(noct.value>=1){
                        creatField();
                    }
                else{
                    window.alert('number of subject most be greater than 0');
                    // location.reload();
                    }

                }
                );
            pwd_confirm = document.getElementById('confirm password');
            pwd_fs = document.getElementById('pwd_fs');
            inconsitentcy = document.getElementById("inconsitentcy");
            pwd_confirm.addEventListener('click', (e)=>{
            if(user_password_set.value!== user_password_confirm.value)
            {
                inconsitentcy.style.display = "block";
                e.preventDefault();
            }
            else{
                inconsitentcy.style.display = "none";
                // e.preventDefault();
            }
            });