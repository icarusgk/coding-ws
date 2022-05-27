import { greet } from './utils'

if (21 >= 18) {
  message = (
    <h1>
      Hey, check out this alcoholic beverage!
      {greet('Roger')}
    </h1>
  );
} else {
  message = (
    <h1>
      Hey, check out these earrings I got at Claire's!
    </h1>
  );
}

export default function ifs() {
  return (
    <div>
      {message}
    </div>
  )
}

