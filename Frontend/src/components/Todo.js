import axios from "axios";
import React from 'react';

function TodoItem(props){
    const deleteTodoHandler=(title)=>{
        axios.delete(`http://127.0.0.1:8000/api/delete/todo{title}`)
            .then(res=>console.log(res.data))

    }
    return (
        <div>
            <span style={{fontWeight: 'bold, underline'}}>{props.todo.title}:</span> {props.todo.description}
            <button className='btn btn-outline-danger my-2 mx-3' style={{'borderRadius':'50px',"font-weight":"bold"}} onClick={()=>deleteTodoHandler(props.todo.title)}>Delete</button>
        </div>
    )
}

export default TodoItem;