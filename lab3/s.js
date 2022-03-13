let tasks = document.querySelector('.tasks');
console.log(tasks);
let AddBtn = document.querySelector('.add-btn');
let InputFill = document.querySelector('.input-fill');

let task = document.querySelectorAll('.task');
tasks.append(task[0]);
let deleteimg = document.querySelectorAll('.delete-img');

function add(){
    if (InputFill.value != ""){
        let div = document.createElement('div');
        div.className = "task";

        let input = document.createElement('input');
        input.type = "checkbox";
        input.className = "task-checkbox";

        let span = document.createElement('span');
        span.innerHTML = InputFill.value;

        let delimg = document.createElement('img');
        delimg.src = "delete.png";
        delimg.className = "delete-img";
        delimg.addEventListener('click', remove);

        tasks.appendChild(div);
        div.appendChild(input);
        div.appendChild(span);
        div.appendChild(delimg);

        InputFill.value = '';
    }
}

function remove(){
    this.parentNode.remove();
}
AddBtn.addEventListener('click', add);
if (!!deleteimg){

    for(let i = 0; i< deleteimg.length; i++){
        deleteimg[i].addEventListener('click', remove);
    }
}
// deleteimg.addEventListener('click', remove);
