import { Outlet } from 'react-router-dom';
import Navigation from './Navigation';
import Footer from './Footer';
import '../App.css';

const Root = () => {
  return (
    <div className="root-container">
      <Navigation />
      <div className="main-content">
        <Outlet />
      </div>
      <Footer />
    </div>
  );
};

export default Root;