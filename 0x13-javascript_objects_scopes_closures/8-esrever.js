#!/usr/bin/node

exports.esrever = function (list) {
  const myArr = [];

  for (let i = 0; i < list.length; i++) {
    myArr.unshift(list[i]);
  }
  return myArr;
};
