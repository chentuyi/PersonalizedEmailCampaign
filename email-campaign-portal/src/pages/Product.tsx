import { useState } from "react";

const Product = () => {
    const [message, setMessage] = useState('');
    const [result, setResult] = useState('');
  
    const handleSubmit = async (e: React.FormEvent) => {
      e.preventDefault();
  
      try {
        const response = await fetch('http://localhost:5000/product_info', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ message: message }),
        });
  
        const data = await response.json();
        setResult(data);
      } catch (error) {
        console.error('Error:', error);
        setResult('Error occurred while processing');
      }
    };
  
    return (
      <div className="App">
        <h2>Product Information</h2>
        <form onSubmit={handleSubmit}>
          <label>Which product would you like to learn more about?</label><br></br>
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            style={{ width: '800px', padding: '3px', fontSize: '16px' }} 
          /><br></br><br></br>
          <button type="submit">Ask Us</button>
        </form>
        <div className="result">
          <pre>{result}</pre>
        </div>
      </div>
    );
};

export default Product;