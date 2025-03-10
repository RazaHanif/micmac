import { useState } from "react";
import Button from "./components/HelloButton";
import ClosableAlert from "./components/ClosableAlert";

function App() {
  const [alertVisable, setAlertVisable] = useState(false);

  const handleShowAlert = () => {
    setAlertVisable(true);
  };

  const handleHideAlert = () => {
    setAlertVisable(false);
  };

  const message = (
    <ClosableAlert onClose={handleHideAlert}>
      You are being alerted :O
    </ClosableAlert>
  );

  return (
    <div>
      {alertVisable && message}
      <Button type="primary" onClick={handleShowAlert}>
        Alert?
      </Button>
    </div>
  );
}

export default App;
