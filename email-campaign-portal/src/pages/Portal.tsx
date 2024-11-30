import { useState } from "react";

const Portal = () => {
    const [linkedin, setLinkedin] = useState('');
    const [product1, setProduct1] = useState('');
    const [product2, setProduct2] = useState('');
    const [product3, setProduct3] = useState('');
  
    const handleSubmit = async (e: React.FormEvent) => {
      e.preventDefault();
  
      try {
        const response = await fetch('http://localhost:5000/process_linkedin', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ linkedin: linkedin }),
        });
  
        const data = await response.json();
        console.log(data)
        
        setProduct1(data.product1)
        setProduct2(data.product2)
        setProduct3(data.product3)
      } catch (error) {
        console.error('Error:', error);
        setProduct1('Error occurred while processing');
        setProduct2('Error occurred while processing')
        setProduct3('Error occurred while processing')
      }
    };
  
    return (
      <div className="App">
        <h2>Linkedin Processor</h2>
        <form onSubmit={handleSubmit}>
          <label>Linkedin:</label><br></br>
          <input
            type="text"
            value={linkedin}
            onChange={(e) => setLinkedin(e.target.value)}
            style={{ width: '800px', padding: '3px', fontSize: '16px' }} 
          /><br></br><br></br>
          <button type="submit">Generate Email Campaign</button>
        </form>

        <div className="result">
          <h3>Product 1</h3>
          <pre>{product1}</pre>
          <h3>Product 2</h3>
          <pre>{product2}</pre>
          <h3>Product 3</h3>
          <pre>{product3}</pre>
        </div>
      </div>
    );
};

export default Portal;