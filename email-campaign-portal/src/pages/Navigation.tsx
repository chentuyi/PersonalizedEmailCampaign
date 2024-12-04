import { NavLink } from 'react-router-dom';

const Navigation = () => {
  return (
    <nav>
      <ul>
        <li>
          <NavLink to='/home'>Home</NavLink>
        </li>
        <li>
          <NavLink to='/portal'>Email Campaign Portal</NavLink>
        </li>
        <li>
          <NavLink to='/product'>Product Chat</NavLink>
        </li>
      </ul>
    </nav>
  );
};

export default Navigation;
