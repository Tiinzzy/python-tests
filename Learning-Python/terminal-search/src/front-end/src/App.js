import { BrowserRouter } from "react-router-dom";

import Home from "./components/Home";

function RealApp() {
  return (
    <div>
      <Home />
    </div>
  );
};

export default function App() {


  return (
    <BrowserRouter basename="/news-sentiment">
      <RealApp />
    </BrowserRouter>
  )
}