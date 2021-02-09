import React, { Component } from 'react';
import { Navbar,Nav } from 'react-bootstrap';
import Dropdown from 'react-bootstrap/Dropdown'
import { Person,Search } from 'react-bootstrap-icons';

export default class Header extends React.Component {
  render(){
  return (

  	<div className="container-fluid">
  	 <div className="row">
   
      	<Navbar bg="white" expand="lg" style={{marginTop:"10px"}}>

  			<Navbar.Brand href="/"><img src="/img/pruthatek.png" title="logo" style={{height: "45px"}} alt="logo" /></Navbar.Brand>
  			<Navbar.Toggle aria-controls="basic-navbar-nav" style={{color: "white"}} />

  			<Navbar.Collapse id="basic-navbar-nav">

  				<form class="d-flex" style={{marginLeft:"auto"}}>
			        <input class="form-control me-2" type="search" placeholder="Find Amazon Products" aria-label="Search" style={{width:"350px"}}/>
			        <button class="btn btn-outline-success" type="submit"><Search /></button>
     			</form>

			    <Nav className="ml-auto" style={{marginLeft: "auto",marginRight:"auto"}}>
			      <Nav.Link href="/popularproducts">Popular Products</Nav.Link>
			      <Nav.Link href="/toppricedrops">Top Price Drops</Nav.Link>

			      <Nav.Link href="/signup">SignUp</Nav.Link>
				  <Nav.Link href="/login">Login</Nav.Link>

			      {/*<NavDropdown title="SignUp/Login" id="basic-nav-dropdown">
			        <NavDropdown.Item href="/signUp">Sign Up</NavDropdown.Item>
			        <NavDropdown.Item href="/login">Login</NavDropdown.Item>
			      </NavDropdown>*/}
			    </Nav>
    
  			</Navbar.Collapse>
		</Navbar>
	 </div>	
	</div>	

  );
  }
}


