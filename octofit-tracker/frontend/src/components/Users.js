import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setUsers(results);
        setLoading(false);
      })
      .catch(err => {
        setLoading(false);
        console.error('Error fetching users:', err);
      });
  }, [endpoint]);

  if (loading) return (
    <div className="d-flex justify-content-center my-5">
      <div className="spinner-border text-primary" role="status">
        <span className="visually-hidden">Loading...</span>
      </div>
    </div>
  );

  return (
    <div className="card">
      <div className="card-header bg-primary text-white">
        <h3 className="mb-0">Users</h3>
      </div>
      <div className="card-body p-0">
        <table className="table table-striped table-hover mb-0">
          <thead>
            <tr>
              <th>#</th>
              <th>Name</th>
              <th>Email</th>
              <th>Team</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user, idx) => (
              <tr key={user.id || idx}>
                <td>{idx + 1}</td>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td><span className="badge bg-info text-dark">{user.team}</span></td>
              </tr>
            ))}
          </tbody>
        </table>
        {users.length === 0 && (
          <p className="text-muted text-center my-3">No users found.</p>
        )}
      </div>
    </div>
  );
};

export default Users;
