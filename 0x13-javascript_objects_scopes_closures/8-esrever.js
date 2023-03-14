#!/usr/bin/node
exports.esrever = function (list) {
  const result = [];
  while (list.length) {
    result.push(list.pop());
  }
  return result;
};
