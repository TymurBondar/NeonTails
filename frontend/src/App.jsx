import { useState, useEffect } from 'react'

function App() {
  const [message, setMessage] = useState("1")

useEffect(() => {
  fetch('/api/message')
  .then(res => res.json())
  .then(message => setMessage(message.message))
  .catch(error => console.error(error))
},[])

  return (
    <div className='flex flex-col items-center justify-center h-screen'>
      <h1 className=''>Vite + React + Flask</h1>
      <h1 className=''>INFO FROM FLASK - {message}</h1>
    </div>
  )
}

export default App

//git checkout main
//git pull
//git checkout -b name
//git add. commit push
//
