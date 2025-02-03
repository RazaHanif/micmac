import Header from "./Header"
import Footer from "./Footer"
import Food from "./Food";
import Card from "./Card";
import Button from './Button/Button'
import PropCard from "./PropCard";

function App() {
  
  return(
    <>
      <Header></Header>
      {/* <Food></Food> */}
      <Card></Card>
      <PropCard name="Harry" age={25} isStudent={true}></PropCard>
      <PropCard name="Ron" age={24} isStudent={false}></PropCard>
      <PropCard></PropCard>
      <Button></Button> 
      <Footer></Footer>
    </>
  );
}

export default App
