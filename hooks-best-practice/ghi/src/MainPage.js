import { useState } from 'react';
import ClueCard from './ClueCard';



function MainPage() {
  const [score, setScore] = useState(0);

  return (
    <div className="px-4 my-5 text-center">
      <h1 className="display-5 fw-bold">Trivial Game</h1>
      <h2>Score: {score}</h2>
      <ClueCard setScore={setScore} />
    </div>
  );
}

export default MainPage;
