import { useState } from 'react';

export const List = props => {
  const [newTask, setNewTask] = useState({});  
  const [allTasks, setAllTasks] = useState([newTask.name, newTask.age])
  
  const handleChange = () => {
    setAllTasks(allTasks.pop())
  }

  return (
    <div>
      <form action="#" onSubmit={handleSubmit}>
        <h1>Tasks</h1>
        <h4>{newTask.name}</h4>
        <h5>{newTask.age}</h5>
        {allTasks.map((task) => <p>{task}</p>)}
        <button>Delete last task</button>
      </form>
    </div>
  )
}