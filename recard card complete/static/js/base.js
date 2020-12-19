//
// window.onload = ()=>{
//     let c =document.getElementById('login-container_id');
//     let a = document.getElementById('nav_anchor_login');
//     let b = document.getElementById('login');
//     let g = document.getElementById('general_nav_bar');
//     let m =document.getElementById('main_heading');
//     let user_name = document.getElementById(''); 
//     let user_password = document.getElementById('user_password');
//     let nav_container = document.getElementById('nav_container');
//
//         // b.style.left = (window.innerWidth - (0.4)*window.innerWidth)/2 +"px";
//         // g.style.width = window.innerWidth + "px";
//         // m.style.width = window.innerWidth + "px";
//         // c.style.width = window.innerwidth + "px";
//         // c.style.height = window.innerHeight + "px";
//         // nav_container.style.width = window.innerWidth + "px";
//     // if(window.innerWidth < 1200){
//     //     // c.style. ='30px'
//     //     c.style.width = '210%';
//     //     c.style.height = '180%';
//     //     c.style.fontSize ='40px';
//     //
//     // }
//
//     a.addEventListener('click',(e)=>{
//         if(c.style.display === ''){
//
//             c.style.display ='block';
//
//             window.screenY;}
//
//
//         else if(c.style.display ==='block'){
//             c.style.display = '';
//             window.screenY;
//         }
//             e.preventDefault();
//
//     });
//     show_password = document.getElementById("password-visibility");
//     user_password = document.getElementById("user_password");
//     show_password.addEventListener('click',(e)=>
//     {
//
//         if(user_password.type === 'text'){
//             user_password.type = 'password';}
//
//         else if(user_password.type === 'password'){
//             user_password.type = 'text';
//         }
//         }
//     );
//
//     window.onclick = (e)=>{
//         if(e.target === c ){
//            c.style.display = '';
//         }
//     }
//     // window.onresize = ()=>{
//     //     b.style.left = (window.innerWidth - (0.4)*window.innerWidth)/2 +"px";
//     //     // g.style.width = window.innerWidth + "px";
//     //     // m.style.width = window.innerWidth + "px";
//     //     // c.style.width = window.innerWidth + "px";
//     //     // c.style.height = window.innerHeight + "px";
//     //     // nav_container.style.width = window.innerWidth + "px";
//     // }
//
// };
// // window.onresize =()=>{
// //       if(window.innerWidth < 1200){
// //         // c.style. ='30px'
// //         c.style.width = '210%';
// //         c.style.height = '180%';
// //         c.style.fontSize ='40px';
// //
// //     }
// //       else{
// //           c.style.width = '100%';
// //         c.style.height = '100%';
// //         c.style.fontSize ='15px'
// //       }
// // };

window.onload=()=>{
    let change_to_english = document.getElementById("change-to-english");
    let change_to_french = document.getElementById("change-to-french");
    let change_to_english1 = document.getElementById("change-to-english1");
    let change_to_french1 = document.getElementById("change-to-french1");
    let english = document.getElementById("english");
    let french = document.getElementById("french");

    change_to_english.addEventListener('click',(e)=>{
        english.style.display = "block";
        french.style.display = "none";
        e.preventDefault();
    })
    change_to_french.addEventListener('click',(e)=>{
        french.style.display = 'block';
        english.style.display ="none";
        e.preventDefault();
    })

    change_to_english1.addEventListener('click',(e)=>{
        english.style.display = "block";
        french.style.display = "none";
        e.preventDefault();
    })
    change_to_french1.addEventListener('click',(e)=>{
        french.style.display = 'block';
        english.style.display ="none";
        e.preventDefault();
    })
}

let carouselExampleSlidesOnly1 = document.getElementById("carouselExampleSlidesOnly1")
let carouselExampleSlidesOnly2 = document.getElementById("carouselExampleSlidesOnly2")
let frenchContainer = document.getElementById("carouselExampleIndicators")

window.onscroll=()=>{
    console.log(frenchContainer.offsetTop)
    if(frenchContainer.offsetTop > 130){
        carouselExampleSlidesOnly1.style.display = "none";
        carouselExampleSlidesOnly2.style.display = "inline";

    }
    else{
        carouselExampleSlidesOnly1.style.display = "inline";
        carouselExampleSlidesOnly2.style.display = "none";
    }
}
