import React, { createContext, useState } from 'react';

// Create a context for user data
export const UserContext = createContext(null);

// Create a provider component
export const UserProvider = ({ children }) => {
  // State to keep track of user's login status and data
  const [user, setUser] = useState(JSON.parse(localStorage.getItem('user')));

  // The provider component will wrap app components, 
  // allowing them to access the user context
  return (
    <UserContext.Provider value={{ user, setUser }}>
      {children}
    </UserContext.Provider>
  );
};
