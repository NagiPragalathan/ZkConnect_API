from django.test import TestCase

# Create your tests here.

# Models Details

# Ind_Profile which is contain [first_name, Last_name, Profile_bio, skills, Resume_image
# write the django models code for SocialLinks which is contains [ id, userid, github, linkedin, twitter]
# write the django models code for Rec_Profile which is contain [first_name, Last_name, Profile_bio, company_name, description, logo]

# write the django models code for Skills which is contains [ id, Name, type-default:tech]

# write the django models code for CompanyDetails which is contains [id, company_name, company_bio, start_year,no_of_emp, SocialLinks, logo]

# write the django models code for JobCreate which is contains [id, CompanyDetails, description, experience, looking_for, sallery, environment ]

# write the django models code for StackReq which is contains [ stackid, JobCreateid, Skills ]

# write the django models code for Applyed_jobs which is contains [id, userid, JobCreateid, status]


'''
reference.......

import React, { useState } from 'react';
import axios from 'axios';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/login/', { username, password });
      console.log(response.data); // Handle the success response
    } catch (error) {
      console.error(error.response.data); // Handle the error response
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Username:
          <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
        </label>
        <br />
        <label>
          Password:
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </label>
        <br />
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default Login;

'''