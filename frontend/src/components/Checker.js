import React, { useState } from "react";
import axios from "axios";
import { Button, Form } from 'react-bootstrap';

const Checker = () => {
  const [data, setData] = useState("");
  const apiUrl = "http://localhost:8100/api/check";

  const messageChecker = (e) => {
    e.preventDefault();
    const messagePayload = { message: data };
    axios.post(apiUrl, messagePayload).then((result) => {
      alert(result.data.result);
    });
  };

  const handleChange = (e) => {
    setData(e.target.value);
  };

  return (
    <div className='App d-flex flex-column align-items-center'>
      <Form style={{ width: '500px' }} onSubmit={messageChecker}>
        <Form.Group>
          <Form.Label>Your Message</Form.Label>
          <Form.Control as='textarea' value={data} onChange={handleChange} />
        </Form.Group>
        <Button type='submit'>Check</Button>
      </Form>
    </div>
  );
};

export default Checker;
