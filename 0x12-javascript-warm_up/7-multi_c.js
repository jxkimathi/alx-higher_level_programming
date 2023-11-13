#!/usr/bin/node
if (process.argv[2] === undefined || NaN(process.argv[2])) {
  console.log('Missinf number of occurrences');
} else {
  const x = Number(process.argv[2]);
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
