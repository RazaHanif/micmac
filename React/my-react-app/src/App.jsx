import Header from "./Header"
import Footer from "./Footer"
import Food from "./Food";
import Card from "./Card";
import Button from './Button/Btn'
import PropCard from "./PropCard";
import UserGreeting from "./UserGreeting";
import List from "./List";
import PropList from "./PropList";

function App() {

  const fruits = [
    {id: 1, name: "apple", calories: 95},
    {id: 2, name: "orange", calories: 45},
    {id: 3, name: "banana", calories: 105},
    {id: 4, name: "coconut", calories: 159},
    {id: 5, name: "pineapple", calories: 37},
  ]
  
  const veg = [
    {id: 1, name: "potatoes", calories: 110},
    {id: 2, name: "celery", calories: 15},
    {id: 3, name: "carrots", calories: 25},
    {id: 4, name: "corn", calories: 63},
    {id: 5, name: "broccoli", calories: 50},
  ]

  
  return(
    <>
      <Header></Header>
      {/* <Food></Food> */}
      <List></List>
      <PropList items={fruits} category="Fruits"></PropList>
      <PropList items={veg} category="Vegtable"></PropList>
      <Card></Card>
      <PropCard name="Harry" age={25} isStudent={true}></PropCard>
      <PropCard name="Ron" age={24} isStudent={false}></PropCard>
      <PropCard></PropCard>
      <Button></Button>
      <UserGreeting isLoggedIn={true} username="Raza"></UserGreeting>
      <UserGreeting isLoggedIn={false} username="Bob"></UserGreeting>
      <UserGreeting isLoggedIn={true}></UserGreeting>
      <Footer></Footer>
    </>
  );
}

export default App
