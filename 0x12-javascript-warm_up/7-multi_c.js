#!/usr/bin/node
if (process.argv[2] === undefined || NaN(process.argv[2])) {
  console.log('Missinf number of occurrences');
} else {
  const x = Number(process.argv[2]);

  for (index = 0; index < x; index++) {
    console.log('C is fun');
  }
}